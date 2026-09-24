"""Offline regressions for the OrcaRouter-O2 downstream contract.

Every case mutates a copy of the committed dist/incidents.json, so the tests
exercise the real export rather than a fixture that could drift from it.
"""
import copy
import json
import unittest

import downstream_contract as dc


class ContractTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        with open(dc.DIST, encoding="utf-8") as f:
            cls.base = json.load(f)

    def doc(self):
        return copy.deepcopy(self.base)

    def first(self, doc):
        return doc["incidents"][0]

    def assert_rejected(self, doc, fragment):
        problems = dc.check_archive(doc)
        self.assertTrue(problems, "O2's validator would have accepted this")
        self.assertTrue(any(fragment in p for p in problems), problems[:5])

    def assert_accepted(self, doc):
        self.assertEqual(dc.check_archive(doc), [])


class CurrentExportTests(ContractTestCase):
    def test_the_committed_export_loads_in_o2(self):
        self.assertEqual(dc.check(self.doc()), ([], []))


class ValidatorTests(ContractTestCase):
    """Part A: anything here would make O2 reject the whole file."""

    def test_schema_version_other_than_2(self):
        for value in (3, "2", 1):
            with self.subTest(value=value):
                doc = self.doc()
                doc["schema_version"] = value
                self.assert_rejected(doc, "unsupported schema_version")

    def test_new_enum_values(self):
        for field, value in (("kind", "synthetic"), ("severity", "none"),
                             ("confidence", "E"), ("ai_involvement", "confirmed ")):
            with self.subTest(field=field):
                doc = self.doc()
                self.first(doc)[field] = value
                self.assert_rejected(doc, f'unknown {field} "{value}"')

    def test_count_and_version_metadata(self):
        for fields, fragment in (({"count": "354"}, "count="), ({"count": 1}, "count="),
                                 ({"version": "2026-02-30"}, "version"),
                                 ({"version": {"injected": True}}, "version")):
            with self.subTest(fields=fields):
                doc = self.doc()
                doc.update(fields)
                self.assert_rejected(doc, fragment)

    def test_missing_or_empty_incidents(self):
        doc = self.doc()
        del doc["incidents"]
        self.assert_rejected(doc, "no `incidents` array")
        doc = self.doc()
        doc["incidents"], doc["count"] = [], 0
        self.assert_rejected(doc, "incidents[] is empty")

    def test_record_field_types(self):
        for field, value, fragment in (
                ("real_harm", "true", "real_harm must be boolean"),
                ("disputed", "false", "disputed must be boolean"),
                ("landmark", None, "landmark must be boolean"),
                ("title_ja", {}, "title_ja must be a string"),
                ("date", 123, "missing id or date"),
                ("type", [{}], "type[] is empty"),
                ("type", ["__proto__"], "type[] is empty"),
                ("type", ["IPI\n"], "type[] is empty"),
                ("region", ["us"], "region[] is empty"),
                ("month", "1999-01", "inconsistent month")):
            with self.subTest(field=field, value=value):
                doc = self.doc()
                self.first(doc)[field] = value
                self.assert_rejected(doc, fragment)

    def test_an_invalid_calendar_date(self):
        doc = self.doc()
        r = self.first(doc)
        r.update(date="2026-02-29", month="2026-02", path=f"incidents/2026-02/{r['id']}.md",
                 path_zh=None)
        self.assert_rejected(doc, "missing id or date")

    def test_the_english_title(self):
        doc = self.doc()
        self.first(doc)["title"] = "中文标题"
        self.assert_rejected(doc, "English title contains Chinese")
        doc = self.doc()
        self.first(doc)["title"] = "   "
        self.assert_rejected(doc, "no English title")

    def test_record_paths(self):
        doc = self.doc()
        for r in doc["incidents"]:
            r["path"] = f"incidents/{r['id']}.md"
        self.assert_rejected(doc, "expected")
        doc = self.doc()
        self.first(doc)["path_zh"] = "../../bad"
        self.assert_rejected(doc, "invalid Chinese record path")

    def test_duplicate_ids(self):
        doc = self.doc()
        doc["incidents"].append(copy.deepcopy(self.first(doc)))
        doc["count"] += 1
        self.assert_rejected(doc, "duplicate id")

    def test_unsafe_source_urls(self):
        for url in ("javascript:alert(1)", "https://", "https://trusted.example@evil.example/r",
                    "https://example.com/\nreport", "data:text/html,x", "https://exa mple.com/",
                    "https://example.com:99999/", "https:///example.com",
                    "https://example.com\\@localhost/", " https://example.com/", None):
            with self.subTest(url=url):
                doc = self.doc()
                self.first(doc)["sources"][0]["url"] = url
                self.assert_rejected(doc, "source url is not http(s)")

    def test_source_list_shape(self):
        doc = self.doc()
        self.first(doc)["sources"] = []
        self.assert_rejected(doc, "no sources")
        doc = self.doc()
        self.first(doc)["sources"][0]["label"] = 5
        self.assert_rejected(doc, "source label must be a string")

    def test_what_o2_accepts(self):
        # plain http is a link, not a script; O2 renders it
        for url in ("http://example.com/x", "  https://example.com/x", "HTTPS://EXAMPLE.COM/x",
                    "https://xn--exmple-cua.com/", "https://exämple.com/"):
            with self.subTest(url=url):
                doc = self.doc()
                self.first(doc)["sources"][0]["url"] = url
                self.assert_accepted(doc)
        doc = self.doc()
        doc["alignment_manifest"] = "x"
        for r in doc["incidents"]:
            r["alignment"] = {"eligible": True}
        self.assert_accepted(doc)
        doc = self.doc()
        r = self.first(doc)
        r.update(date="2028-02-29", month="2028-02", path=f"incidents/2028-02/{r['id']}.md",
                 path_zh=None, real_harm=False, landmark=False, disputed=False)
        self.assert_accepted(doc)


class O2TestSuiteTests(ContractTestCase):
    """Part B: O2 still loads the file, but its own test suite would fail."""

    def assert_o2_tests_fail(self, doc, fragment):
        self.assertEqual(dc.check_archive(doc), [], "expected part A to pass")
        problems = dc.check_o2_tests(doc)
        self.assertTrue(any(fragment in p for p in problems), problems)

    def test_a_type_code_o2_has_no_icon_for(self):
        doc = self.doc()
        self.first(doc)["type"].append("ALIGN")
        self.assert_o2_tests_fail(doc, "ALIGN")

    def test_a_featured_record_below_grade_a(self):
        doc = self.doc()
        featured = dc.pick_landmarks(doc["incidents"])[0]["id"]
        next(r for r in doc["incidents"] if r["id"] == featured)["confidence"] = "B"
        self.assert_o2_tests_fail(doc, featured)

    def test_featured_cards_need_three_different_types(self):
        doc = self.doc()
        for r in doc["incidents"]:
            if r["severity"] == "critical" and r["real_harm"] is True:
                r["type"] = ["ROGUE"]
        self.assert_o2_tests_fail(doc, "repeat a type description")

    def test_nothing_to_feature(self):
        doc = self.doc()
        for r in doc["incidents"]:
            if r["severity"] == "critical":
                r["severity"] = "high"
        self.assert_o2_tests_fail(doc, "featured cards would be empty")

    def test_the_methodology_needs_a_mixed_archive(self):
        for change, fragment in ((lambda r: r.update(kind="incident"), "every record is an incident"),
                                 (lambda r: r.update(confidence="A"), "every record is grade A"),
                                 (lambda r: r.update(kind="research"), "same kind")):
            with self.subTest(fragment=fragment):
                doc = self.doc()
                for r in doc["incidents"]:
                    change(r)
                self.assert_o2_tests_fail(doc, fragment)

    def test_pick_landmarks_matches_o2_on_the_committed_export(self):
        # cross-checked against O2's own deriveSummary() on 2026-09-24
        picked = dc.pick_landmarks(self.doc()["incidents"])
        self.assertEqual(len(picked), 3)
        self.assertEqual(len({r["type"][0] for r in picked}), 3)
        self.assertTrue(all(r["confidence"] == "A" for r in picked))


if __name__ == "__main__":
    unittest.main()
