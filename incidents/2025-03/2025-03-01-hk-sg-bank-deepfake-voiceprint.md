---
id: 2025-03-01-hk-sg-bank-deepfake-voiceprint
title: "Deepfake voice defeats bank voiceprint auth in HK and Singapore"
title_zh: "港/新银行深伪语音绕过声纹"
title_ja: "ディープフェイク音声が香港・シンガポールの銀行の声紋認証を突破"
title_ko: "딥페이크 음성, 홍콩·싱가포르 은행 성문 인증 뚫어"
title_de: "Deepfake-Stimme überlistet die Stimmabdruck-Authentifizierung von Banken in Hongkong und Singapur"
title_fr: "Une voix deepfake déjoue l'authentification vocale bancaire à Hong Kong et à Singapour"
title_es: "Voz deepfake burla la autenticación por huella de voz bancaria en Hong Kong y Singapur"
date: 2025-03-01
date_precision: month
date_raw: "2025-03"

kind: incident
type: [OTHER]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [SEA, HK]

summary: |
  About US$25 million in unauthorized transactions


summary_zh: |
  约 US$2,500 万未授权交易

summary_ja: |
  約2,500万米ドル相当の不正取引

summary_ko: |
  약 2,500만 달러의 무단 거래

summary_de: |
  Etwa US$25 Millionen an nicht autorisierten Transaktionen

summary_fr: |
  Environ 25 millions de dollars US de transactions non autorisées

summary_es: |
  Unos US$25 millones en transacciones no autorizadas

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-03
scan_ref: "SCAN.md §5 2025-03"
---

# Deepfake voice defeats bank voiceprint auth in HK and Singapore

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

About US$25 million in unauthorized transactions

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
| Date | `2025-03-01` (raw: 2025-03, precision `month`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Southeast Asia](../../regions/sea.md) · [Hong Kong](../../regions/hk.md) |
| Archive ID | `2025-03-01-hk-sg-bank-deepfake-voiceprint` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-03/2025-03-01-hk-sg-bank-deepfake-voiceprint.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
