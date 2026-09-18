---
id: 2025-10-01-framelink-figma-mcp-rce
title: "Framelink Figma MCP RCE"
title_zh: "Framelink Figma MCP RCE"
title_ja: "Framelink Figma MCPのRCE"
title_ko: "Framelink Figma MCP RCE"
title_de: "Framelink Figma MCP: RCE"
title_fr: "RCE dans Framelink Figma MCP"
title_es: "Framelink Figma MCP RCE"
date: 2025-10-01
date_precision: day
date_raw: "2025-10-01"

kind: vulnerability
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-53967, Node.js command injection


summary_zh: |
  CVE-2025-53967，Node.js 命令注入

summary_ja: |
  CVE-2025-53967、Node.jsのコマンドインジェクション

summary_ko: |
  CVE-2025-53967, Node.js 명령 주입

summary_de: |
  CVE-2025-53967, Command-Injection in Node.js

summary_fr: |
  CVE-2025-53967, injection de commande Node.js

summary_es: |
  CVE-2025-53967, inyección de comandos en Node.js

sources:
  - url: https://www.practical-devsecops.com/mcp-security-statistics-2026-report/
    label: Practical DevSecOps

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Framelink Figma MCP RCE

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

CVE-2025-53967, Node.js command injection

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
| 1 | Practical DevSecOps | <https://www.practical-devsecops.com/mcp-security-statistics-2026-report/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-01` (raw: 2025-10-01, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-01-framelink-figma-mcp-rce` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-09-03` [Claude Code MCP auto-enable bypass](../2025-09/2025-09-03-claude-code-mcp.md)<br>  <sub>Claude Code MCP auto-enable bypass</sub>
- `2025-09-25` [postmark-mcp malicious npm package](../2025-09/2025-09-25-postmark-mcp-npm.md)<br>  <sub>postmark-mcp malicious npm package</sub>
- `2025-08-05` [Cursor MCPoison (CVE-2025-54136)](../2025-08/2025-08-05-cursor-mcpoison.md)<br>  <sub>Cursor MCPoison (CVE-2025-54136)</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-01-framelink-figma-mcp-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
