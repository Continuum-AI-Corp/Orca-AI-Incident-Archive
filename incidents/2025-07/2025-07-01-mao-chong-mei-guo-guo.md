---
id: 2025-07-01-mao-chong-mei-guo-guo
title: "AI voice campaign impersonating the US Secretary of State"
title_zh: "冒充美国国务卿的 AI 语音行动"
title_ja: "米国務長官になりすましたAI音声キャンペーン"
title_ko: "미 국무장관 사칭 AI 음성 캠페인"
title_de: "KI-Stimmkampagne gibt sich als US-Außenminister aus"
title_fr: "Campagne de voix IA usurpant le secrétaire d'État américain"
title_es: "Campaña de voz con IA que suplantó al secretario de Estado de Estados Unidos"
date: 2025-07-01
date_precision: month
date_raw: "2025-07"

kind: incident
type: [OTHER]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  Impersonated Marco Rubio with deepfake voice and text, contacting foreign ministers and members of Congress over Signal


summary_zh: |
  用深伪语音与文本冒充 Marco Rubio，经 Signal 接触外国外长与国会议员

summary_ja: |
  ディープフェイク音声とテキストでMarco Rubio氏になりすまし、Signalで他国の外相や連邦議会議員に接触した

summary_ko: |
  딥페이크 음성과 텍스트로 Marco Rubio를 사칭해 Signal로 각국 외교장관과 의회 의원들에게 접촉했다

summary_de: |
  Gab sich mit Deepfake-Stimme und -Text als Marco Rubio aus und kontaktierte Außenminister und Kongressmitglieder über Signal

summary_fr: |
  Usurpation de Marco Rubio par voix deepfake et par texte, contactant des ministres des Affaires étrangères et des membres du Congrès via Signal

summary_es: |
  Suplantó a Marco Rubio con voz y texto deepfake, contactando a ministros de Asuntos Exteriores y miembros del Congreso por Signal

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# AI voice campaign impersonating the US Secretary of State

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Impersonated Marco Rubio with deepfake voice and text, contacting foreign ministers and members of Congress over Signal

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
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
| Date | `2025-07-01` (raw: 2025-07, precision `month`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-07-01-mao-chong-mei-guo-guo` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-01-mao-chong-mei-guo-guo.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
