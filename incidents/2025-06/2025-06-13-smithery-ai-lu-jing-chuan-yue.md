---
id: 2025-06-13-smithery-ai-lu-jing-chuan-yue
title: "Smithery.ai path traversal"
title_zh: "Smithery.ai 路径穿越"
title_ja: "Smithery.aiのパストラバーサル"
title_ko: "Smithery.ai 경로 순회"
title_de: "Smithery.ai: Path Traversal"
title_fr: "Traversée de répertoires chez Smithery.ai"
title_es: "Path traversal en Smithery.ai"
date: 2025-06-13
date_precision: day
date_raw: "2025-06-13"

kind: vulnerability
type: [MCP, CRED]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  An MCP hosting platform leaked a Fly.io token, putting thousands of downstream servers at risk


summary_zh: |
  MCP 托管平台泄露 Fly.io token，威胁数千下游 server

summary_ja: |
  MCPホスティングプラットフォームがFly.ioトークンを漏えいし、数千の下流サーバーがリスクにさらされた

summary_ko: |
  MCP 호스팅 플랫폼이 Fly.io 토큰을 유출해 수천 개의 하위 서버를 위험에 빠뜨렸다

summary_de: |
  Eine MCP-Hosting-Plattform gab ein Fly.io-Token preis, wodurch Tausende nachgelagerte Server gefährdet wurden

summary_fr: |
  Une plateforme d'hébergement MCP a laissé fuiter un jeton Fly.io, mettant en danger des milliers de serveurs en aval

summary_es: |
  Una plataforma de alojamiento MCP filtró un token de Fly.io, poniendo en riesgo a miles de servidores posteriores

sources:
  - url: https://www.secrss.com/articles/86614
    label: Security Reference 2025 roundup

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Smithery.ai path traversal

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

An MCP hosting platform leaked a Fly.io token, putting thousands of downstream servers at risk

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["The agent retrieves and uses it"]:::step
    I["Credential abuse<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Security Reference 2025 roundup | <https://www.secrss.com/articles/86614> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-13` (raw: 2025-06-13, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-13-smithery-ai-lu-jing-chuan-yue` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-06-13` [MCP Inspector unauthenticated RCE](2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-06-30` [McDonald's McHire "Olivia" hiring bot](2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>
- `2025-06-04` [Asana MCP server cross-tenant data exposure](2025-06-04-asana-mcp-server.md)<br>  <sub>Asana MCP server cross-tenant data exposure</sub>
- `2025-07-06` [Supabase MCP prompt injection dumps a private table](../2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md)<br>  <sub>Supabase MCP prompt injection dumps a private table</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
