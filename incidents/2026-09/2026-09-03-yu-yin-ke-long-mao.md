---
id: 2026-09-03-yu-yin-ke-long-mao
title: "Japan: AI voice clone impersonates a CEO, ¥4.5bn lost"
title_zh: "日本：AI 语音克隆冒充社长，损失 45 亿日元"
title_ja: "日本：AI音声クローンがCEOになりすまし、45億円が流出"
title_ko: "일본: AI 음성 복제로 CEO 사칭, 45억 엔 손실"
title_de: "Japan: KI-Stimmklon gibt sich als CEO aus, ¥4.5bn verloren"
title_fr: "Japon : un clonage vocal par IA usurpe un PDG, 4,5 milliards de ¥ perdus"
title_es: "Japón: un clon de voz por IA suplanta a un CEO y se pierden ¥4.5 mil millones"
date: 2026-09-03
date_precision: day
date_raw: "2026-09-03"

kind: incident
type: [OTHER]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [JP]

summary: |
  Cloned the CEO's voice from samples in the company's public talks and videos, called the finance lead to authorise the transfer, **and spoofed the caller ID as the CEO's real number**


summary_zh: |
  从公司公开演讲与视频取样克隆社长声音，致电财务负责人授权汇款，**并伪造来电显示为社长真实号码**

summary_ja: |
  企業の公開講演や動画のサンプルからCEOの声をクローンし、財務責任者に電話して送金を承認させ、**発信者IDをCEOの実番号に偽装した**

summary_ko: |
  회사의 공개 강연과 영상 샘플로 CEO의 음성을 복제해 재무 책임자에게 전화해 이체를 승인하게 했고, **발신자 번호를 CEO의 실제 번호로 위조**했다

summary_de: |
  Klonte die Stimme des CEO aus Aufnahmen in öffentlichen Vorträgen und Videos des Unternehmens, rief die Finanzleitung an, um die Überweisung zu genehmigen, **und fälschte die Rufnummernanzeige auf die echte Nummer des CEO**

summary_fr: |
  Voix du PDG clonée à partir d'échantillons de conférences et vidéos publiques de l'entreprise, appel du responsable financier pour autoriser le virement, **et usurpation de l'identifiant d'appelant avec le vrai numéro du PDG**

summary_es: |
  Clonaron la voz del CEO a partir de muestras de charlas y videos públicos de la empresa, llamaron al responsable de finanzas para autorizar la transferencia, **y falsificaron el identificador de llamada con el número real del CEO**

sources:
  - url: https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/
    label: ITmedia Enterprise (relayed)

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Japan: AI voice clone impersonates a CEO, ¥4.5bn lost

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Cloned the CEO's voice from samples in the company's public talks and videos, called the finance lead to authorise the transfer, **and spoofed the caller ID as the CEO's real number**

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
| 1 | ITmedia Enterprise (relayed) | <https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-03` (raw: 2026-09-03, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Japan](../../regions/jp.md) |
| Archive ID | `2026-09-03-yu-yin-ke-long-mao` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-03-yu-yin-ke-long-mao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
