---
id: 2025-12-01-mcp-typescript-sdk-dns
title: "MCP TypeScript SDK DNS rebinding"
title_zh: "MCP TypeScript SDK DNS 重绑定"
title_ja: "MCP TypeScript SDKのDNSリバインディング"
title_ko: "MCP TypeScript SDK DNS 리바인딩"
title_de: "MCP TypeScript SDK: DNS-Rebinding"
title_fr: "DNS rebinding dans le SDK TypeScript MCP"
title_es: "DNS rebinding en el SDK de TypeScript de MCP"
date: 2025-12-01
date_precision: month
date_raw: "2025-12"

kind: vulnerability
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-66414, **CVSS 8.1**. An unauthenticated HTTP MCP server running on localhost without `enableDnsRebindingProtection` can be made to invoke tools by a malicious website via DNS rebinding that bypasses the same-origin policy. **Fixed in v1.24.0**: `createMcpExpressApp()` now enables protection by default when binding to localhost


summary_zh: |
  CVE-2025-66414，**CVSS 8.1**。localhost 上运行且未开 `enableDnsRebindingProtection` 的无认证 HTTP MCP server，可被恶意网站经 DNS 重绑定绕过同源策略调用工具。**v1.24.0 修复**，`createMcpExpressApp()` 绑定 localhost 时默认开启保护

summary_ja: |
  CVE-2025-66414、**CVSS 8.1**。`enableDnsRebindingProtection`なしでlocalhost上で動作する認証不要のHTTP MCPサーバーは、同一生成元ポリシーをバイパスするDNSリバインディングにより、悪意あるWebサイトからツールを呼び出される可能性がある。**v1.24.0で修正**：`createMcpExpressApp()`がlocalhostバインド時にデフォルトで保護を有効化するようになった

summary_ko: |
  CVE-2025-66414, **CVSS 8.1**. `enableDnsRebindingProtection` 없이 localhost에서 실행되는 무인증 HTTP MCP 서버는, 동일 출처 정책을 우회하는 DNS 리바인딩을 통해 악성 웹사이트가 도구를 호출하게 만들 수 있다. **v1.24.0에서 수정**: `createMcpExpressApp()`이 이제 localhost 바인딩 시 기본적으로 보호를 활성화한다

summary_de: |
  CVE-2025-66414, **CVSS 8.1**. Ein nicht authentifizierter HTTP-MCP-Server, der auf localhost ohne `enableDnsRebindingProtection` läuft, kann von einer bösartigen Website per DNS-Rebinding, das die Same-Origin-Policy umgeht, zum Aufrufen von Tools gebracht werden. **Behoben in v1.24.0**: `createMcpExpressApp()` aktiviert den Schutz nun standardmäßig beim Binden an localhost

summary_fr: |
  CVE-2025-66414, **CVSS 8.1**. Un serveur MCP HTTP non authentifié tournant sur localhost sans `enableDnsRebindingProtection` peut être amené à invoquer des outils par un site malveillant via du DNS rebinding qui contourne la politique de même origine. **Corrigé en v1.24.0** : `createMcpExpressApp()` active désormais la protection par défaut lors d'une liaison à localhost

summary_es: |
  CVE-2025-66414, **CVSS 8.1**. Un servidor MCP HTTP sin autenticación que se ejecuta en localhost sin `enableDnsRebindingProtection` puede ser inducido por un sitio web malicioso a invocar herramientas mediante DNS rebinding, que elude la política de mismo origen. **Corregido en la v1.24.0**: `createMcpExpressApp()` ahora habilita la protección por defecto al enlazar a localhost

sources:
  - url: https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-w48q-cv73-mx4w
    label: "GHSA-w48q-cv73-mx4w"

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# MCP TypeScript SDK DNS rebinding

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

CVE-2025-66414, **CVSS 8.1**. An unauthenticated HTTP MCP server running on localhost without `enableDnsRebindingProtection` can be made to invoke tools by a malicious website via DNS rebinding that bypasses the same-origin policy. **Fixed in v1.24.0**: `createMcpExpressApp()` now enables protection by default when binding to localhost

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GHSA-w48q-cv73-mx4w | <https://github.com/modelcontextprotocol/typescript-sdk/security/advisories/GHSA-w48q-cv73-mx4w> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-01` (raw: 2025-12, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-01-mcp-typescript-sdk-dns` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-12-06` [IDEsaster](2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>
- `2025-12-01` [Three CVEs in Anthropic's Git MCP Server](2025-12-01-anthropic-git-mcp-server.md)<br>  <sub>Three CVEs in Anthropic's Git MCP Server</sub>
- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-01` [Framelink Figma MCP RCE](../2025-10/2025-10-01-framelink-figma-mcp-rce.md)<br>  <sub>Framelink Figma MCP RCE</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-01-mcp-typescript-sdk-dns.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
