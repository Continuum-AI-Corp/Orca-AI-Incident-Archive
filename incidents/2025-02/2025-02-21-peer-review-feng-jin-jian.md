---
id: 2025-02-21-peer-review-feng-jin-jian
title: "OpenAI bans accounts behind the \"Peer Review\" surveillance tool"
title_zh: "OpenAI 封禁「Peer Review」监控工具账号"
title_ja: "OpenAI、「Peer Review」監視ツールに関与したアカウントを停止"
title_ko: "OpenAI, \"Peer Review\" 감시 도구 배후 계정 정지"
title_de: "OpenAI sperrt Konten hinter dem Überwachungstool „Peer Review“"
title_fr: "OpenAI bannit les comptes derrière l'outil de surveillance « Peer Review »"
title_es: "OpenAI bloquea las cuentas detrás de la herramienta de vigilancia \"Peer Review\""
date: 2025-02-21
date_precision: day
date_raw: "2025-02-21"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [CN, GLOBAL]

summary: |
  Development of a social-media surveillance tool with suspected Chinese ties; the same batch banned the "Sponsored Discontent" influence operation


summary_zh: |
  疑似中国背景的社媒监控工具开发；同期封禁 "Sponsored Discontent" 影响力行动

summary_ja: |
  中国との関連が疑われるSNS監視ツールの開発。同じ一括処分で「Sponsored Discontent」世論工作も停止した

summary_ko: |
  중국 연계가 의심되는 소셜 미디어 감시 도구 개발 건. 같은 조치로 "Sponsored Discontent" 여론 조작 작전도 차단했다

summary_de: |
  Entwicklung eines Social-Media-Überwachungstools mit mutmaßlich chinesischen Verbindungen; im selben Vorgang wurde die Einflussoperation „Sponsored Discontent“ gesperrt

summary_fr: |
  Développement d'un outil de surveillance des réseaux sociaux aux liens chinois présumés ; la même vague a banni l'opération d'influence « Sponsored Discontent »

summary_es: |
  Desarrollo de una herramienta de vigilancia de redes sociales con presuntos vínculos chinos; en la misma tanda se bloqueó la operación de influencia "Sponsored Discontent"

sources:
  - url: https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf
    label: OpenAI Feb 2025 PDF

disputed: false
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# OpenAI bans accounts behind the "Peer Review" surveillance tool

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Development of a social-media surveillance tool with suspected Chinese ties; the same batch banned the "Sponsored Discontent" influence operation

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
| 1 | OpenAI Feb 2025 PDF | <https://cdn.openai.com/threat-intelligence-reports/disrupting-malicious-uses-of-our-models-february-2025-update.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-21` (raw: 2025-02-21, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [China](../../regions/cn.md) · [Global](../../regions/global.md) |
| Archive ID | `2025-02-21-peer-review-feng-jin-jian` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-02-27` [Microsoft sues Storm-2139 and names the defendants](2025-02-27-storm-wei-ruan-qi-su.md)<br>  <sub>Microsoft sues Storm-2139 and names the defendants</sub>
- `2025-01-30` [Italy's Garante blocks DeepSeek](../2025-01/2025-01-30-garante-deepseek-yi-li-feng.md)<br>  <sub>Italy's Garante blocks DeepSeek</sub>
- `2025-01-23` [OpenAI Operator launches (context entry)](../2025-01/2025-01-23-operator-fa-bu-bei-jing.md)<br>  <sub>OpenAI Operator launches (context entry)</sub>
- `2025-03-01` [Sony pulls 75,000+ AI deepfake tracks](../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-21-peer-review-feng-jin-jian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
