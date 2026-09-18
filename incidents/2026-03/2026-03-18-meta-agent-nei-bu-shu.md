---
id: 2026-03-18-meta-agent-nei-bu-shu
title: "Meta internal AI agent data exposure"
title_zh: "Meta 内部 AI agent 数据暴露"
title_ja: "Meta社内AIエージェントによるデータ露出"
title_ko: "Meta 내부 AI 에이전트 데이터 노출"
title_de: "Meta: Datenexposition durch internen KI-Agenten"
title_fr: "Exposition de données par un agent IA interne de Meta"
title_es: "Exposición de datos del agente de IA interno de Meta"
date: 2026-03-18
date_precision: day
date_raw: "2026-03-18"

kind: incident
type: [ROGUE]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  The agent gave unsafe configuration advice, leaving sensitive user and company data exposed internally for about 2 hours


summary_zh: |
  agent 给出不安全的配置建议，导致敏感用户与公司数据内部暴露约 2 小时

summary_ja: |
  エージェントが安全でない設定助言を行い、機密のユーザーデータと会社データが約2時間にわたり社内で露出した

summary_ko: |
  에이전트가 안전하지 않은 구성 조언을 해 민감한 사용자 및 회사 데이터가 약 2시간 동안 내부에 노출되었다

summary_de: |
  Der Agent gab unsichere Konfigurationsempfehlungen, wodurch sensible Nutzer- und Firmendaten etwa 2 Stunden lang intern offenlagen

summary_fr: |
  L'agent a donné des conseils de configuration dangereux, laissant des données sensibles d'utilisateurs et d'entreprise exposées en interne pendant environ 2 heures

summary_es: |
  El agente dio consejos de configuración inseguros, dejando datos sensibles de usuarios y de la empresa expuestos internamente durante unas 2 horas

sources:
  - url: https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
    label: "OWASP Q1'26"

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Meta internal AI agent data exposure

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

The agent gave unsafe configuration advice, leaving sensitive user and company data exposed internally for about 2 hours

## Attack chain

```mermaid
flowchart LR
    E["An ordinary task handed to the agent"]:::entry
    S0["The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> I
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
| Date | `2026-03-18` (raw: 2026-03-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-03-18-meta-agent-nei-bu-shu` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2026-03-02` [Amazon hit by back-to-back outages from AI-generated code](2026-03-02-amazon-yin-sheng-cheng-dai.md)<br>  <sub>Amazon hit by back-to-back outages from AI-generated code</sub>
- `2026-02-26` [Claude Code runs terraform destroy on all of DataTalks.Club's production](../2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br>  <sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub>
- `2026-04-25` [Cursor and Claude Opus 4.6 wipe production and backups in nine seconds](../2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br>  <sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub>
- `2026-02-18` [Microsoft 365 Copilot summarises confidential mail it shouldn't see](../2026-02/2026-02-18-microsoft-copilot-yue-quan-zong.md)<br>  <sub>Microsoft 365 Copilot summarises confidential mail it shouldn't see</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-18-meta-agent-nei-bu-shu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
