---
id: 2026-09-01-agent-zu-zhi-guo-qu
title: "\"88% of organisations hit a confirmed or suspected AI agent security incident this year\""
title_zh: "「88% 的组织在过去一年遭遇确认或疑似 AI agent 安全事故」"
title_ja: "「今年、88%の組織がAIエージェントのセキュリティインシデントを確認または疑惑で経験」"
title_ko: "\"올해 88%의 조직이 확인 또는 의심되는 AI 에이전트 보안 사고를 겪었다\""
title_de: "„88% der Organisationen hatten dieses Jahr einen bestätigten oder vermuteten Sicherheitsvorfall mit KI-Agenten“"
title_fr: "« 88 % des organisations ont subi cette année un incident de sécurité d'agent IA confirmé ou suspecté »"
title_es: "\"El 88% de las organizaciones sufrió este año un incidente de seguridad de agentes de IA confirmado o sospechado\""
date: 2026-09-01
date_precision: month
date_raw: "2026-09"

kind: report
type: [GOV]
severity: info
confidence: C
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  But only **6%** of security budget goes to AI agent security. ⚠️ **Conflicts with another survey's "65%"**, and the sample and methodology of both surveys are unclear


summary_zh: |
  但只有 **6%** 的安全预算用于 AI agent 安全。⚠️ **与另一份「65%」的调查冲突**，两份调研的样本与口径均不明

summary_ja: |
  しかしセキュリティ予算のうちAIエージェントセキュリティに充てられるのは**6%**のみ。⚠️ **別の調査の「65%」と矛盾**し、どちらの調査もサンプルと手法が不明確

summary_ko: |
  그러나 보안 예산 중 AI 에이전트 보안에 투입되는 비중은 **6%**뿐이다. ⚠️ **다른 설문의 "65%"와 상충**하며, 두 설문 모두 표본과 방법론이 불분명하다

summary_de: |
  Doch nur **6%** des Sicherheitsbudgets fließen in die Sicherheit von KI-Agenten. ⚠️ **Widerspricht den „65%“ einer anderen Umfrage**, und Stichprobe und Methodik beider Umfragen sind unklar

summary_fr: |
  Mais seuls **6 %** du budget de sécurité vont à la sécurité des agents IA. ⚠️ **En contradiction avec le « 65 % » d'une autre enquête**, et l'échantillon et la méthodologie des deux enquêtes sont flous

summary_es: |
  Pero solo el **6%** del presupuesto de seguridad se destina a la seguridad de agentes de IA. ⚠️ **Entra en conflicto con el "65%" de otra encuesta**, y la muestra y la metodología de ambas encuestas no están claras

sources:
  - url: https://beam.ai/agentic-insights/ai-agent-security-breaches-2026-lessons
    label: Beam.ai roundup
  - url: https://www.kiteworks.com/cybersecurity-risk-management/ai-agent-security-incidents-2026/
    label: "Kiteworks(65%)"

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# "88% of organisations hit a confirmed or suspected AI agent security incident this year"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: C](https://img.shields.io/badge/confidence-C-9A6008?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

> [!WARNING]
> **Confidence C** — second-hand only, no primary source.

## Summary

But only **6%** of security budget goes to AI agent security. ⚠️ **Conflicts with another survey's "65%"**, and the sample and methodology of both surveys are unclear

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Beam.ai roundup | <https://beam.ai/agentic-insights/ai-agent-security-breaches-2026-lessons> |
| 2 | Kiteworks(65%) | <https://www.kiteworks.com/cybersecurity-risk-management/ai-agent-security-incidents-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-01` (raw: 2026-09, precision `month`) |
| Kind | Threat report `report` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **C** — second-hand only, no primary source |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-01-agent-zu-zhi-guo-qu` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-09-03` [US senators introduce the Ban Artificial Superintelligence Act](2026-09-03-ban-artificial-superintelligence-act.md)<br>  <sub>US senators introduce the Ban Artificial Superintelligence Act</sub>
- `2026-09-05` [OpenAI formally acknowledges the "wiki incident", promises a disclosure framework](2026-09-05-wiki-zheng-shi-cheng-ren.md)<br>  <sub>OpenAI formally acknowledges the "wiki incident", promises a disclosure framework</sub>
- `2026-09-07` [Japan's IPA publishes the August 2026 AI Security Bulletin](2026-09-07-ipa-fa-bu-duan-xin.md)<br>  <sub>Japan's IPA publishes the August 2026 AI Security Bulletin</sub>
- `2026-08-03` [CrowdStrike 2026 threat hunting report](../2026-08/2026-08-03-crowdstrike-wei-xie-shou-lie.md)<br>  <sub>CrowdStrike 2026 threat hunting report</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-01-agent-zu-zhi-guo-qu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
