---
id: 2026-04-07-grafanaghost-jian-jie-ti-shi
title: "GrafanaGhost indirect prompt injection"
title_zh: "GrafanaGhost 间接提示注入"
title_ja: "GrafanaGhostの間接プロンプトインジェクション"
title_ko: "GrafanaGhost 간접 프롬프트 인젝션"
title_de: "GrafanaGhost: indirekte Prompt-Injection"
title_fr: "Injection indirecte de prompt GrafanaGhost"
title_es: "Inyección indirecta de prompt en GrafanaGhost"
date: 2026-04-07
date_precision: day
date_raw: "2026-04-07"

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Noma Security: exfiltrating telemetry, infrastructure, customer and financial data via a URL parameter


summary_zh: |
  Noma Security：经 URL 参数外带遥测、基础设施、客户与财务数据

summary_ja: |
  Noma Security：URLパラメータ経由でテレメトリ、インフラ、顧客、財務データを外部送信

summary_ko: |
  Noma Security: URL 매개변수를 통해 텔레메트리, 인프라, 고객 및 재무 데이터를 유출한다

summary_de: |
  Noma Security: Exfiltration von Telemetrie-, Infrastruktur-, Kunden- und Finanzdaten über einen URL-Parameter

summary_fr: |
  Noma Security : exfiltration de données de télémétrie, d'infrastructure, clients et financières via un paramètre d'URL

summary_es: |
  Noma Security: exfiltración de datos de telemetría, infraestructura, clientes y finanzas mediante un parámetro de URL

sources:
  - url: https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
    label: "OWASP Q1'26"

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# GrafanaGhost indirect prompt injection

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Noma Security: exfiltrating telemetry, infrastructure, customer and financial data via a URL parameter

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OWASP Q1'26 | <https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-07` (raw: 2026-04-07, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-07-grafanaghost-jian-jie-ti-shi` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-15` [ShareLeak (CVE-2026-21520) and PipeLeak](2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>
- `2026-04-17` [Meta AI support bot tricked into handing over an Instagram account](2026-04-17-meta-instagram-ke-fu-ji.md)<br>  <sub>Meta AI support bot tricked into handing over an Instagram account</sub>
- `2026-03-01` [Claudy Day: a three-flaw chain in claude.ai](../2026-03/2026-03-01-claudy-day-claude-ai.md)<br>  <sub>Claudy Day: a three-flaw chain in claude.ai</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-07-grafanaghost-jian-jie-ti-shi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
