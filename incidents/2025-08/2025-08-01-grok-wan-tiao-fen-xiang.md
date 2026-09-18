---
id: 2025-08-01-grok-wan-tiao-fen-xiang
title: "370,000 shared Grok conversations indexed"
title_zh: "Grok 37 万条分享对话被索引"
title_ja: "Grokの共有会話37万件がインデックスされる"
title_ko: "Grok 공유 대화 37만 건 색인"
title_de: "370,000 geteilte Grok-Unterhaltungen indexiert"
title_fr: "370 000 conversations Grok partagées indexées"
title_es: "370,000 conversaciones compartidas de Grok indexadas"
date: 2025-08-01
date_precision: month
date_raw: "2025-08"

kind: incident
type: [OTHER]
severity: low
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Grok's "share conversation" links lacked a noindex tag, so search engines indexed around 370,000 user conversations — the same class of problem as ChatGPT's around the same time.


summary_zh: |
  Grok 的「分享对话」链接未加 noindex，约 37 万条用户对话被搜索引擎收录——与 ChatGPT 同期的同类问题同源。

summary_ja: |
  Grokの「会話を共有」リンクにnoindexタグがなく、検索エンジンが約37万件のユーザー会話をインデックスした——ほぼ同時期のChatGPTと同種の問題。

summary_ko: |
  Grok의 "대화 공유" 링크에 noindex 태그가 없어 검색 엔진이 사용자 대화 약 37만 건을 색인했다 — 같은 시기 ChatGPT와 같은 종류의 문제였다.

summary_de: |
  Groks Links zum „Teilen von Unterhaltungen“ hatten kein noindex-Tag, sodass Suchmaschinen rund 370,000 Nutzerunterhaltungen indexierten — dieselbe Problemklasse wie bei ChatGPT etwa zur selben Zeit.

summary_fr: |
  Les liens « partager la conversation » de Grok n'avaient pas de balise noindex, si bien que les moteurs de recherche ont indexé environ 370 000 conversations d'utilisateurs — le même type de problème que chez ChatGPT à la même période.

summary_es: |
  Los enlaces de "compartir conversación" de Grok carecían de la etiqueta noindex, por lo que los motores de búsqueda indexaron alrededor de 370,000 conversaciones de usuarios — el mismo tipo de problema que el de ChatGPT casi al mismo tiempo.

sources:
  - url: https://www.secrss.com/articles/86614
    label: Security Reference 2025 roundup

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# 370,000 shared Grok conversations indexed

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Grok's "share conversation" links lacked a noindex tag, so search engines indexed around 370,000 user conversations — the same class of problem as ChatGPT's around the same time.

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
| Date | `2025-08-01` (raw: 2025-08, precision `month`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Low** `low` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-01-grok-wan-tiao-fen-xiang` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-01-grok-wan-tiao-fen-xiang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
