"""Offline regressions for untrusted archive export and source URLs."""
import csv
import io
import socket
import ssl
import unittest
from unittest.mock import Mock, patch

from export_safety import csv_row
import check_links


def address(ip="93.184.216.34", port=443):
    family = socket.AF_INET6 if ":" in ip else socket.AF_INET
    target = (ip, port, 0, 0) if family == socket.AF_INET6 else (ip, port)
    return (family, socket.SOCK_STREAM, socket.IPPROTO_TCP, "", target)


class CsvSecurityTests(unittest.TestCase):
    def test_formula_cells_remain_text_after_csv_roundtrip(self):
        inputs = ['=HYPERLINK("https://example.com","click")', '+SUM(1,2)',
                  '-1+2', '@SUM(1,2)', '\t=1+1', '\r\n=1', '\x00=1',
                  '\ufeff =1', '\u2003=1', '\x1f=1', '＝1+1', '＋1', '－1', '＠SUM(1)']
        output = io.StringIO()
        csv.writer(output).writerow(csv_row(inputs))
        output.seek(0)
        self.assertEqual(next(csv.reader(output)), ["'" + text for text in inputs])

    def test_normal_prose_and_non_strings_unchanged(self):
        values = ['A new incident', '中文摘要', '2026-09-17', 'a,b\n"c"', '', None, 3]
        self.assertEqual(csv_row(values), values)


class LinkSecurityTests(unittest.TestCase):
    def test_non_http_credentials_controls_and_unusual_ports_blocked_before_dns(self):
        with patch.object(check_links.socket, 'getaddrinfo') as resolve:
            for url in ['file:///etc/passwd', 'javascript:alert(1)',
                        'https://user:pass@example.com/', 'https://example.com:22/',
                        'https://example.com:0/',
                        'https://example.com/\r\nX-Test:yes', 'https://example.com\\@localhost/',
                        'https:///missing-host', 'https://example.com:bad/']:
                with self.subTest(url=url):
                    self.assertEqual(check_links.check(url, 1)[0], 0)
            resolve.assert_not_called()

    def test_private_reserved_and_mixed_dns_answers_are_blocked(self):
        for ip in ['127.0.0.1', '10.0.0.1', '172.16.0.1', '192.168.1.1',
                   '169.254.169.254', '100.64.0.1', '0.0.0.0', '224.0.0.1',
                   '::1', 'fc00::1', 'fe80::1', 'ff02::1', '::ffff:127.0.0.1',
                   '2002:7f00:1::1', '64:ff9b::7f00:1']:
            with self.subTest(ip=ip), patch.object(check_links.socket, 'getaddrinfo',
                                                  return_value=[address(), address(ip)]), \
                    patch.object(check_links, 'connect_public') as connect:
                self.assertEqual(check_links.check('https://untrusted.example/', 1)[0], 0)
                connect.assert_not_called()

    def test_public_ipv4_and_ipv6_accepted(self):
        expected = [address(), address('2606:4700:4700::1111')]
        with patch.object(check_links.socket, 'getaddrinfo', return_value=expected):
            parsed, actual = check_links.public_destination('https://example.com/source')
        self.assertEqual(parsed.hostname, 'example.com')
        self.assertEqual(actual, expected)

    def test_connection_pins_validated_address_without_resolving_again(self):
        sock = Mock()
        with patch.object(check_links.socket, 'socket', return_value=sock), \
                patch.object(check_links.socket, 'getaddrinfo') as resolve:
            self.assertIs(check_links.connect_public([address()], 2), sock)
        sock.connect.assert_called_once_with(('93.184.216.34', 443))
        resolve.assert_not_called()

    def test_failed_address_socket_is_closed(self):
        bad, good = Mock(), Mock()
        bad.connect.side_effect = OSError('unreachable')
        with patch.object(check_links.socket, 'socket', side_effect=[bad, good]):
            self.assertIs(check_links.connect_public([address(), address()], 2), good)
        bad.close.assert_called_once()

    def test_https_verifies_certificate_and_original_hostname(self):
        context = ssl.create_default_context()
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(context.check_hostname)
        conn = check_links.PublicHTTPSConnection('source.example', context=context)
        conn.public_addresses = [address()]
        raw = Mock()
        with patch.object(check_links, 'connect_public', return_value=raw), \
                patch.object(context, 'wrap_socket', return_value=Mock()) as wrap:
            conn.connect()
        wrap.assert_called_once_with(raw, server_hostname='source.example')
        conn.close()

    def test_tls_failure_closes_socket(self):
        context = Mock()
        context.wrap_socket.side_effect = ssl.SSLCertVerificationError('invalid certificate')
        conn = check_links.PublicHTTPSConnection('source.example', context=context)
        conn.public_addresses = [address()]
        raw = Mock()
        with patch.object(check_links, 'connect_public', return_value=raw):
            with self.assertRaises(ssl.SSLCertVerificationError):
                conn.connect()
        raw.close.assert_called_once()

    def test_redirect_is_reported_without_following_private_location(self):
        response = Mock(status=302, reason='Found')
        response.getheader.return_value = 'http://169.254.169.254/latest/meta-data/'
        conn = Mock()
        conn.getresponse.return_value = response
        with patch.object(check_links.socket, 'getaddrinfo', return_value=[address()]), \
                patch.object(check_links, 'PublicHTTPSConnection', return_value=conn) as factory:
            self.assertEqual(check_links.check('https://source.example/path?q=1', 1), (302, 'Found'))
        self.assertEqual(factory.call_count, 1)
        conn.request.assert_called_once_with('HEAD', '/path?q=1', headers={'User-Agent': check_links.UA})
        conn.close.assert_called_once()

    def test_head_rejection_retries_get_with_same_validated_addresses(self):
        first, second = Mock(), Mock()
        first.getresponse.return_value = Mock(status=405, reason='Method not allowed')
        second.getresponse.return_value = Mock(status=200, reason='OK')
        with patch.object(check_links.socket, 'getaddrinfo', return_value=[address()]) as resolve, \
                patch.object(check_links, 'PublicHTTPSConnection', side_effect=[first, second]):
            self.assertEqual(check_links.check('https://source.example/', 1), (200, 'OK'))
        self.assertEqual(resolve.call_count, 1)
        second.request.assert_called_once_with('GET', '/', headers={'User-Agent': check_links.UA})
        first.close.assert_called_once()
        second.close.assert_called_once()


if __name__ == '__main__':
    unittest.main()
