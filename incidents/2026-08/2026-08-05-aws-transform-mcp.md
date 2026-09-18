---
id: 2026-08-05-aws-transform-mcp
title: "AWS Transform MCP arbitrary file write"
title_zh: "AWS Transform MCP 任意文件写"
title_ja: "AWS Transform MCPの任意ファイル書き込み"
title_ko: "AWS Transform MCP 임의 파일 쓰기"
title_de: "AWS Transform MCP: beliebiges Dateischreiben"
title_fr: "Écriture de fichiers arbitraires dans AWS Transform MCP"
title_es: "Escritura arbitraria de archivos en AWS Transform MCP"
date: 2026-08-05
date_precision: day
date_raw: "2026-08-05"

kind: research
type: [MCP]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2026-18953, **CVSS 8.6 (High)**. A path traversal in `get_resource` of `awslabs.aws-transform-mcp-server` allows arbitrary file write under context-dependent conditions. AWS security bulletin 2026-075


summary_zh: |
  CVE-2026-18953，**CVSS 8.6（High）**。`awslabs.aws-transform-mcp-server` 的 `get_resource` 存在路径穿越，可在上下文相关条件下任意写文件。AWS 安全公告 2026-075

summary_ja: |
  CVE-2026-18953、**CVSS 8.6（High）**。`awslabs.aws-transform-mcp-server`の`get_resource`におけるパストラバーサルにより、状況次第で任意ファイルの書き込みが可能。AWSセキュリティ速報2026-075

summary_ko: |
  CVE-2026-18953, **CVSS 8.6 (높음)**. `awslabs.aws-transform-mcp-server`의 `get_resource`에 있는 경로 순회로 상황에 따라 임의 파일 쓰기가 가능하다. AWS 보안 권고 2026-075

summary_de: |
  CVE-2026-18953, **CVSS 8.6 (High)**. Ein Path Traversal in `get_resource` von `awslabs.aws-transform-mcp-server` erlaubt unter kontextabhängigen Bedingungen beliebiges Dateischreiben. AWS-Sicherheitsbulletin 2026-075

summary_fr: |
  CVE-2026-18953, **CVSS 8.6 (High)**. Une traversée de répertoires dans `get_resource` de `awslabs.aws-transform-mcp-server` permet une écriture de fichiers arbitraires dans des conditions dépendant du contexte. Bulletin de sécurité AWS 2026-075

summary_es: |
  CVE-2026-18953, **CVSS 8.6 (Alta)**. Un path traversal en `get_resource` de `awslabs.aws-transform-mcp-server` permite la escritura arbitraria de archivos en condiciones dependientes del contexto. Boletín de seguridad de AWS 2026-075

sources:
  - url: https://aws.amazon.com/security/security-bulletins/2026-075-aws/
    label: AWS security bulletin

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# AWS Transform MCP arbitrary file write

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

CVE-2026-18953, **CVSS 8.6 (High)**. A path traversal in `get_resource` of `awslabs.aws-transform-mcp-server` allows arbitrary file write under context-dependent conditions. AWS security bulletin 2026-075

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | AWS security bulletin | <https://aws.amazon.com/security/security-bulletins/2026-075-aws/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-05` (raw: 2026-08-05, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-05-aws-transform-mcp` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-18` [Context7 MCP prompt injection (CVE-2026-75130)](2026-08-18-context7-mcp-ti-shi-zhu.md)<br>  <sub>Context7 MCP prompt injection (CVE-2026-75130)</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](../2026-07/2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-30` [RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm](../2026-07/2026-07-30-rufroot-man-fen-zhao-huan.md)<br>  <sub>RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm</sub>
- `2026-06-12` [Agentjacking: one public DSN hijacks AI coding agents](../2026-06/2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-05-aws-transform-mcp.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
