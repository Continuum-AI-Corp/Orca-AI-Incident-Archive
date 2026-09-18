---
id: 2025-01-01-maine-town-deepfake-phishing
title: "AI phishing and deepfake voice hit a small Maine town"
title_zh: "美国缅因州小镇 AI 钓鱼 + 深伪语音"
title_ja: "AIフィッシングとディープフェイク音声がメイン州の小さな町を直撃"
title_ko: "AI 피싱과 딥페이크 음성, 미국 메인주 소도시를 덮치다"
title_de: "KI-Phishing und Deepfake-Stimme treffen eine Kleinstadt in Maine"
title_fr: "Hameçonnage par IA et voix deepfake contre une petite ville du Maine"
title_es: "Phishing con IA y voz deepfake golpean un pequeño pueblo de Maine"
date: 2025-01-01
date_precision: month
date_raw: "2025-01"

kind: incident
type: [OTHER]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  Impersonating town officials to approve tens of thousands of dollars in payments


summary_zh: |
  冒充镇政府官员批出数万美元付款

summary_ja: |
  町の役職員になりすまし、数万ドル規模の支払いを承認させた

summary_ko: |
  시 공무원을 사칭해 수만 달러의 지급을 승인받아냈다

summary_de: |
  Sie gaben sich als Stadtbeamte aus, um Zahlungen in Höhe von Zehntausenden Dollar genehmigen zu lassen

summary_fr: |
  Usurpation de responsables municipaux pour faire approuver des dizaines de milliers de dollars de paiements

summary_es: |
  Suplantaron a funcionarios municipales para aprobar pagos por decenas de miles de dólares

sources:
  - url: https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/
    label: "OWASP Jan-Feb'25"

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# AI phishing and deepfake voice hit a small Maine town

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Impersonating town officials to approve tens of thousands of dollars in payments

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
| 1 | OWASP Jan-Feb'25 | <https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-01-01` (raw: 2025-01, precision `month`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-01-01-maine-town-deepfake-phishing` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-01-maine-town-deepfake-phishing.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
