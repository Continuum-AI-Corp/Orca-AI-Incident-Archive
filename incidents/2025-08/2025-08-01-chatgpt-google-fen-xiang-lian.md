---
id: 2025-08-01-chatgpt-google-fen-xiang-lian
title: "ChatGPT share links indexed by Google"
title_zh: "ChatGPT 分享链接被 Google 索引"
title_ja: "ChatGPTの共有リンクがGoogleにインデックスされる"
title_ko: "ChatGPT 공유 링크, 구글에 색인"
title_de: "Von Google indexierte ChatGPT-Freigabelinks"
title_fr: "Les liens de partage de ChatGPT indexés par Google"
title_es: "Google indexa enlaces compartidos de ChatGPT"
date: 2025-08-01
date_precision: day
date_raw: "2025-08-01"

kind: incident
type: [OTHER]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Users' private conversations became publicly searchable; OpenAI urgently took the feature offline


summary_zh: |
  用户私密对话公开可搜，OpenAI 紧急下线该功能

summary_ja: |
  ユーザーの非公開の会話が公開検索可能になり、OpenAIは緊急で機能を停止した

summary_ko: |
  사용자의 비공개 대화가 공개 검색 가능해졌고, OpenAI는 긴급히 기능을 내렸다

summary_de: |
  Private Unterhaltungen von Nutzern wurden öffentlich durchsuchbar; OpenAI nahm die Funktion eilig offline

summary_fr: |
  Les conversations privées des utilisateurs sont devenues publiquement recherchables ; OpenAI a retiré la fonctionnalité en urgence

summary_es: |
  Las conversaciones privadas de los usuarios se volvieron públicamente buscables; OpenAI retiró la función urgentemente

sources:
  - url: https://www.secrss.com/articles/86614
    label: Security Reference 2025 roundup

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# ChatGPT share links indexed by Google

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Users' private conversations became publicly searchable; OpenAI urgently took the feature offline

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
| 1 | Security Reference 2025 roundup | <https://www.secrss.com/articles/86614> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-01` (raw: 2025-08-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-01-chatgpt-google-fen-xiang-lian` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-01-chatgpt-google-fen-xiang-lian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
