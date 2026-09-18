---
id: 2025-06-16-simon-willison-ti-chu-zhi
title: "Simon Willison names the \"lethal trifecta\""
title_zh: "Simon Willison 提出「致命三元组」"
title_ja: "Simon Willisonが「lethal trifecta（致命的な三要素）」を提唱"
title_ko: "Simon Willison, \"치명적 삼중주\"를 명명하다"
title_de: "Simon Willison benennt die lethal trifecta"
title_fr: "Simon Willison nomme la « lethal trifecta »"
title_es: "Simon Willison nombra la \"trifecta letal\""
date: 2025-06-16
date_precision: day
date_raw: "2025-06-16"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Private data + untrusted content + outbound capability — almost every later exfiltration chain fits this framework


summary_zh: |
  私有数据 + 不可信内容 + 外发能力 —— 后续几乎所有外泄链都套用这个框架

summary_ja: |
  非公開データ＋信頼できないコンテンツ＋外部送信能力——その後のほぼすべての外部送信チェーンがこの枠組みに当てはまる

summary_ko: |
  비공개 데이터 + 신뢰할 수 없는 콘텐츠 + 외부 송신 능력 — 이후의 거의 모든 유출 체인이 이 틀에 들어맞는다

summary_de: |
  Private Daten + nicht vertrauenswürdige Inhalte + Fähigkeit nach außen — nahezu jede spätere Exfiltrationskette passt in dieses Schema

summary_fr: |
  Données privées + contenu non fiable + capacité de sortie réseau — presque toutes les chaînes d'exfiltration ultérieures entrent dans ce cadre

summary_es: |
  Datos privados + contenido no confiable + capacidad de salida — casi toda cadena de exfiltración posterior encaja en este marco

sources:
  - url: https://simonw.substack.com/p/the-lethal-trifecta-for-ai-agents
    label: Simon Willison

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Simon Willison names the "lethal trifecta"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Private data + untrusted content + outbound capability — almost every later exfiltration chain fits this framework

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
| 1 | Simon Willison | <https://simonw.substack.com/p/the-lethal-trifecta-for-ai-agents> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-16` (raw: 2025-06-16, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-16-simon-willison-ti-chu-zhi` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-04-01` [DeepSeek pulled from app stores in South Korea](../2025-04/2025-04-01-deepseek-han-guo-jia.md)<br>  <sub>DeepSeek pulled from app stores in South Korea</sub>
- `2025-08-25` [Anthropic starts the Claude for Chrome pilot](../2025-08/2025-08-25-anthropic-claude-chrome.md)<br>  <sub>Anthropic starts the Claude for Chrome pilot</sub>
- `2025-03-01` [Sony pulls 75,000+ AI deepfake tracks](../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>
- `2025-02-21` [OpenAI bans accounts behind the "Peer Review" surveillance tool](../2025-02/2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-16-simon-willison-ti-chu-zhi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
