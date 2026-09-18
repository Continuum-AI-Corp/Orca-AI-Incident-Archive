---
id: 2025-01-20-hk-voice-clone-usdt-fraud
title: "Hong Kong AI voice-clone crypto fraud"
title_zh: "香港 AI 语音克隆加密货币诈骗"
title_ja: "香港、AI音声クローンによる暗号資産詐欺"
title_ko: "홍콩 AI 음성 복제 가상자산 사기"
title_de: "Krypto-Betrug mit KI-Stimmklon in Hongkong"
title_fr: "Fraude crypto à Hong Kong via un clonage vocal par IA"
title_es: "Fraude cripto con clonación de voz por IA en Hong Kong"
date: 2025-01-20
date_precision: day
date_raw: "week of 2025-01-20"

kind: incident
type: [OTHER]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [HK]

summary: |
  Cloned a finance manager's voice; 3 USDT transfers totalling HK$145 million (about US$18.5M)


summary_zh: |
  克隆财务经理声音，3 笔 USDT 转账共 HK$1.45 亿（约 US$18.5M）

summary_ja: |
  財務マネージャーの声をクローンし、USDTを3回送金、総額1億4,500万香港ドル（約1,850万米ドル）

summary_ko: |
  재무 관리자의 음성을 복제했다. HK$1억 4,500만(약 1,850만 달러) 규모의 USDT 이체 3건

summary_de: |
  Sie klonten die Stimme eines Finanzmanagers; 3 USDT-Transfers über insgesamt HK$145 Millionen (etwa US$18.5M)

summary_fr: |
  Voix d'un directeur financier clonée ; 3 virements en USDT pour un total de 145 millions HK$ (environ 18,5 M$ US)

summary_es: |
  Clonaron la voz de un gerente de finanzas; 3 transferencias USDT por un total de HK$145 millones (unos US$18.5M)

sources:
  - url: https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/
    label: "OWASP Jan-Feb'25"

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# Hong Kong AI voice-clone crypto fraud

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Cloned a finance manager's voice; 3 USDT transfers totalling HK$145 million (about US$18.5M)

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
| Date | `2025-01-20` (raw: week of 2025-01-20, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Hong Kong](../../regions/hk.md) |
| Archive ID | `2025-01-20-hk-voice-clone-usdt-fraud` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-20-hk-voice-clone-usdt-fraud.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
