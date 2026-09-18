---
id: 2025-07-01-mcp-remote-oauth
title: "mcp-remote OAuth command injection"
title_zh: "mcp-remote OAuth 命令注入"
title_ja: "mcp-remoteのOAuthコマンドインジェクション"
title_ko: "mcp-remote OAuth 명령 주입"
title_de: "mcp-remote: OAuth-Command-Injection"
title_fr: "Injection de commande OAuth dans mcp-remote"
title_es: "Inyección de comandos OAuth en mcp-remote"
date: 2025-07-01
date_precision: month
date_raw: "2025-07"

kind: vulnerability
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-6514: a malicious MCP server can execute arbitrary commands on the client


summary_zh: |
  CVE-2025-6514，恶意 MCP server 可在客户端执行任意命令

summary_ja: |
  CVE-2025-6514：悪性MCPサーバーがクライアント上で任意のコマンドを実行できる

summary_ko: |
  CVE-2025-6514: 악성 MCP 서버가 클라이언트에서 임의 명령을 실행할 수 있다

summary_de: |
  CVE-2025-6514: Ein bösartiger MCP-Server kann beliebige Befehle auf dem Client ausführen

summary_fr: |
  CVE-2025-6514 : un serveur MCP malveillant peut exécuter des commandes arbitraires sur le client

summary_es: |
  CVE-2025-6514: un servidor MCP malicioso puede ejecutar comandos arbitrarios en el cliente

sources:
  - url: https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html
    label: "Japan IPA 2025-12"

disputed: false
landmark: false
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# mcp-remote OAuth command injection

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

CVE-2025-6514: a malicious MCP server can execute arbitrary commands on the client

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
| 1 | Japan IPA 2025-12 | <https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-07-01` (raw: 2025-07, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-07-01-mcp-remote-oauth` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-07-06` [Supabase MCP prompt injection dumps a private table](2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>
- `2025-07-01` [Anthropic Filesystem MCP sandbox escape](2025-07-01-anthropic-filesystem-mcp.md)<br>  <sub>Anthropic Filesystem MCP sandbox escape</sub>
- `2025-06-13` [MCP Inspector unauthenticated RCE](../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-08-05` [Cursor MCPoison (CVE-2025-54136)](../2025-08/2025-08-05-cursor-mcpoison.md)<br>  <sub>Cursor MCPoison (CVE-2025-54136)</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-01-mcp-remote-oauth.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
