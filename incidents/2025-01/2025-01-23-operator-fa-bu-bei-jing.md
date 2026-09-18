---
id: 2025-01-23-operator-fa-bu-bei-jing
title: "OpenAI Operator launches (context entry)"
title_zh: "OpenAI Operator 发布（背景条目）"
title_ja: "OpenAI Operator登場（背景エントリ）"
title_ko: "OpenAI Operator 출시(맥락 항목)"
title_de: "OpenAI Operator startet (Kontext-Eintrag)"
title_fr: "Lancement d'OpenAI Operator (entrée de contexte)"
title_es: "Lanzamiento de OpenAI Operator (entrada de contexto)"
date: 2025-01-23
date_precision: day
date_raw: "2025-01-23"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The first consumer-facing computer-use agent; on 02-01 it opened as a research preview to Pro users in the United States. **The System Card already listed prompt injection as a focus of pre-launch external red-teaming and frontier risk assessment** — the earliest entry in this archive for "the vendor knew at launch that prompt injection was a core risk"


summary_zh: |
  首个面向消费者的计算机使用 agent，02-01 向美国 Pro 用户开放研究预览。**System Card 中已把提示注入列为发布前外部红队与前沿风险评估的重点** —— 这是本档案里「厂商在发布时就知道提示注入是核心风险」的最早一笔

summary_ja: |
  初の一般消費者向けコンピュータ操作エージェント。02-01に米国のProユーザー向けの研究プレビューとして公開された。**システムカードはすでに、プロンプトインジェクションを公開前の外部レッドチーミングとフロンティアリスク評価の重点項目として挙げていた**——「ベンダーがローンチ時点でプロンプトインジェクションを中核リスクと認識していた」ことを示す本アーカイブ最古のエントリ

summary_ko: |
  최초의 소비자용 컴퓨터 사용 에이전트. 02-01 미국 Pro 사용자를 대상으로 연구 프리뷰로 공개되었다. **시스템 카드에는 이미 프롬프트 인젝션이 출시 전 외부 레드팀과 프런티어 위험 평가의 중점 사항으로 명시되어 있었다** — "벤더가 출시 시점에 프롬프트 인젝션이 핵심 위험임을 알고 있었다"는 이 아카이브의 가장 이른 항목

summary_de: |
  Der erste Computer-Use-Agent für Endverbraucher; am 02-01 wurde er als Research Preview für Pro-Nutzer in den Vereinigten Staaten geöffnet. **Die System Card nannte Prompt-Injection bereits als Schwerpunkt des externen Red-Teamings vor dem Start und der Frontier-Risikobewertung** — der früheste Eintrag in diesem Archiv für „der Anbieter wusste beim Start, dass Prompt-Injection ein Kernrisiko ist“

summary_fr: |
  Le premier agent grand public d'usage de l'ordinateur ; le 02-01, il s'est ouvert en aperçu de recherche aux utilisateurs Pro aux États-Unis. **La System Card citait déjà l'injection de prompt parmi les axes du red-teaming externe et de l'évaluation des risques de frontière menés avant le lancement** — l'entrée la plus ancienne de cette archive pour « le fournisseur savait dès le lancement que l'injection de prompt était un risque central »

summary_es: |
  El primer agente de uso de computadora orientado al consumidor; el 02-01 se abrió como vista previa de investigación para usuarios Pro en Estados Unidos. **La System Card ya incluía la inyección de prompt como foco del red-teaming externo previo al lanzamiento y de la evaluación de riesgos de frontera** — la entrada más temprana de este archivo para "el proveedor sabía en el lanzamiento que la inyección de prompt era un riesgo central"

sources:
  - url: https://openai.com/index/operator-system-card/
    label: OpenAI Operator System Card

disputed: false
landmark: false
scan_month: 2025-01
scan_ref: "SCAN.md §5 2025-01"
---

# OpenAI Operator launches (context entry)

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

The first consumer-facing computer-use agent; on 02-01 it opened as a research preview to Pro users in the United States. **The System Card already listed prompt injection as a focus of pre-launch external red-teaming and frontier risk assessment** — the earliest entry in this archive for "the vendor knew at launch that prompt injection was a core risk"

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
| 1 | OpenAI Operator System Card | <https://openai.com/index/operator-system-card/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-01-23` (raw: 2025-01-23, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-01-23-operator-fa-bu-bei-jing` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-01-30` [Italy's Garante blocks DeepSeek](2025-01-30-garante-deepseek-yi-li-feng.md)<br>  <sub>Italy's Garante blocks DeepSeek</sub>
- `2025-02-21` [OpenAI bans accounts behind the "Peer Review" surveillance tool](../2025-02/2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>
- `2025-02-27` [Microsoft sues Storm-2139 and names the defendants](../2025-02/2025-02-27-storm-wei-ruan-qi-su.md)<br>  <sub>Microsoft sues Storm-2139 and names the defendants</sub>
- `2025-03-01` [Sony pulls 75,000+ AI deepfake tracks](../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>

---

[← 2025-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-01/2025-01-23-operator-fa-bu-bei-jing.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
