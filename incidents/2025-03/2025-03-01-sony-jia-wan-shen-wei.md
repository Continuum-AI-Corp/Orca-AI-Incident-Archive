---
id: 2025-03-01-sony-jia-wan-shen-wei
title: "Sony pulls 75,000+ AI deepfake tracks"
title_zh: "Sony 下架 7.5 万+ AI 深伪音乐"
title_ja: "Sony、AIディープフェイク楽曲7万5,000曲以上を削除"
title_ko: "소니, AI 딥페이크 음원 7만 5천 건 이상 삭제"
title_de: "Sony entfernt 75,000+ KI-Deepfake-Tracks"
title_fr: "Sony retire plus de 75 000 titres deepfake générés par IA"
title_es: "Sony retira más de 75,000 pistas deepfake generadas con IA"
date: 2025-03-01
date_precision: month
date_raw: "2025-03"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Unauthorized AI training + deepfake distribution


summary_zh: |
  未授权 AI 训练 + 深伪分发

summary_ja: |
  無断のAI学習＋ディープフェイクの配布

summary_ko: |
  무단 AI 학습 + 딥페이크 유통

summary_de: |
  Nicht autorisiertes KI-Training + Verbreitung von Deepfakes

summary_fr: |
  Entraînement IA non autorisé + diffusion de deepfakes

summary_es: |
  Entrenamiento de IA no autorizado + distribución de deepfakes

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# Sony pulls 75,000+ AI deepfake tracks

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Unauthorized AI training + deepfake distribution

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
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-03-01` (raw: 2025-03, precision `month`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-03-01-sony-jia-wan-shen-wei` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-02-21` [OpenAI bans accounts behind the "Peer Review" surveillance tool](../2025-02/2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>
- `2025-02-27` [Microsoft sues Storm-2139 and names the defendants](../2025-02/2025-02-27-storm-wei-ruan-qi-su.md)<br>  <sub>Microsoft sues Storm-2139 and names the defendants</sub>
- `2025-04-01` [DeepSeek pulled from app stores in South Korea](../2025-04/2025-04-01-deepseek-han-guo-jia.md)<br>  <sub>DeepSeek pulled from app stores in South Korea</sub>
- `2025-01-30` [Italy's Garante blocks DeepSeek](../2025-01/2025-01-30-garante-deepseek-yi-li-feng.md)<br>  <sub>Italy's Garante blocks DeepSeek</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-01-sony-jia-wan-shen-wei.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
