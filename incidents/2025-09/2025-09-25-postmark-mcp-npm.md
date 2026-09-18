---
id: 2025-09-25-postmark-mcp-npm
title: "postmark-mcp malicious npm package"
title_zh: "postmark-mcp 恶意 npm 包"
title_ja: "postmark-mcpの悪性npmパッケージ"
title_ko: "postmark-mcp 악성 npm 패키지"
title_de: "postmark-mcp: bösartiges npm-Paket"
title_fr: "Le paquet npm malveillant postmark-mcp"
title_es: "El paquete npm malicioso postmark-mcp"
date: 2025-09-25
date_precision: day
date_raw: "2025-09-25"

kind: incident
type: [MCP, SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **The first malicious MCP server in the wild**. Koi Security: starting with version 15, a single line of code silently BCC'd all passing emails to the author — an estimated **15,000 messages a day**


summary_zh: |
  **首个在野的恶意 MCP server**。Koi Security：第 15 版起加入一行代码，把所有经过的邮件静默 BCC 给作者，估计每天约 **1.5 万封**

summary_ja: |
  **実環境で確認された初の悪性MCPサーバー**。Koi Security：バージョン15から、たった1行のコードが通過するすべてのメールを作者に無言でBCC送信していた——推定**1日15,000通**

summary_ko: |
  **실제 환경에서 발견된 최초의 악성 MCP 서버**. Koi Security: 버전 15부터 코드 한 줄이 지나가는 모든 메일을 작성자에게 조용히 BCC로 보냈다 — 추정 **하루 15,000통**이다

summary_de: |
  **Der erste bösartige MCP-Server in freier Wildbahn**. Koi Security: Ab Version 15 setzte eine einzige Codezeile alle durchlaufenden E-Mails still per BCC an den Autor — geschätzt **15,000 Nachrichten pro Tag**

summary_fr: |
  **Le premier serveur MCP malveillant en conditions réelles**. Koi Security : à partir de la version 15, une seule ligne de code mettait silencieusement en CCI tous les e-mails transitant vers l'auteur — environ **15 000 messages par jour**

summary_es: |
  **El primer servidor MCP malicioso en entornos reales**. Koi Security: a partir de la versión 15, una sola línea de código ponía silenciosamente en CCO todos los correos que pasaban al autor — unos **15,000 mensajes al día**

sources:
  - url: https://www.koi.ai/blog
    label: Koi Security

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# postmark-mcp malicious npm package

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

**The first malicious MCP server in the wild**. Koi Security: starting with version 15, a single line of code silently BCC'd all passing emails to the author — an estimated **15,000 messages a day**

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Koi Security | <https://www.koi.ai/blog> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-25` (raw: 2025-09-25, precision `day`) |
| Kind | Incident `incident` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-25-postmark-mcp-npm` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-09-15` [Shai-Hulud npm worm v1](2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>
- `2025-09-03` [Claude Code MCP auto-enable bypass](2025-09-03-claude-code-mcp.md)<br>  <sub>Claude Code MCP auto-enable bypass</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-26` [Nx "s1ngularity"](../2025-08/2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-25-postmark-mcp-npm.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
