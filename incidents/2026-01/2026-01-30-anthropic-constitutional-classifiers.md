---
id: 2026-01-30-anthropic-constitutional-classifiers
title: "Anthropic ships Constitutional Classifiers++"
title_zh: "Anthropic 发布 Constitutional Classifiers++"
title_ja: "AnthropicがConstitutional Classifiers++を提供開始"
title_ko: "Anthropic, Constitutional Classifiers++ 공개"
title_de: "Anthropic liefert Constitutional Classifiers++ aus"
title_fr: "Anthropic livre Constitutional Classifiers++"
title_es: "Anthropic lanza Constitutional Classifiers++"
date: 2026-01-30
date_precision: day
date_raw: "2026-01-30"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A two-stage cascade (a lightweight linear activation probe screens first → a context-aware ensemble classifier), cutting compute cost **40x** and bringing the false-refusal rate to **0.05%**; 1,700+ hours of red-teaming reported no universal jailbreak


summary_zh: |
  两级级联（轻量线性激活探针筛选 → 上下文感知集成分类器），算力成本降 **40 倍**，误拒率 **0.05%**，1,700+ 小时红队未报告通用越狱

summary_ja: |
  2段階のカスケード（まず軽量な線形活性化プローブでスクリーニング→文脈認識型アンサンブル分類器）で、計算コストを**40分の1**に削減し、誤拒否率を**0.05%**にした。1,700時間以上のレッドチーミングで普遍的なジェイルブレイクは報告されなかった

summary_ko: |
  2단계 캐스케이드(경량 선형 활성화 프로브가 먼저 선별 → 컨텍스트 인식 앙상블 분류기)로 연산 비용을 **40배** 줄이고 오탐 거부율을 **0.05%**까지 낮췄다. 1,700시간 이상의 레드팀에서도 범용 탈옥은 보고되지 않았다

summary_de: |
  Eine zweistufige Kaskade (zuerst prüft eine leichtgewichtige lineare Aktivierungs-Sonde → dann ein kontextbewusster Ensemble-Klassifikator), die die Rechenkosten um das **40-fache** senkt und die Falsch-Ablehnungsrate auf **0.05%** bringt; 1,700+ Stunden Red-Teaming meldeten keinen universellen Jailbreak

summary_fr: |
  Une cascade à deux étapes (une sonde d'activation linéaire légère filtre d'abord → un classifieur d'ensemble sensible au contexte), réduisant le coût de calcul **d'un facteur 40** et ramenant le taux de refus à tort à **0,05 %** ; plus de 1 700 heures de red-teaming n'ont signalé aucun jailbreak universel

summary_es: |
  Una cascada de dos etapas (una sonda de activación lineal ligera filtra primero → un clasificador de conjunto consciente del contexto), que reduce el costo de cómputo **40x** y lleva la tasa de rechazos falsos al **0.05%**; más de 1,700 horas de red-teaming no reportaron ningún jailbreak universal

sources:
  - url: https://www.anthropic.com/research/next-generation-constitutional-classifiers
    label: Anthropic
  - url: https://arxiv.org/abs/2601.04603v1
    label: arXiv

disputed: false
landmark: false
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Anthropic ships Constitutional Classifiers++

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

A two-stage cascade (a lightweight linear activation probe screens first → a context-aware ensemble classifier), cutting compute cost **40x** and bringing the false-refusal rate to **0.05%**; 1,700+ hours of red-teaming reported no universal jailbreak

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
| 1 | Anthropic | <https://www.anthropic.com/research/next-generation-constitutional-classifiers> |
| 2 | arXiv | <https://arxiv.org/abs/2601.04603v1> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-30` (raw: 2026-01-30, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-30-anthropic-constitutional-classifiers` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-12-09` [OWASP Top 10 for Agentic Applications 2026](../2025-12/2025-12-09-owasp-top-agentic-applications.md)<br>  <sub>OWASP Top 10 for Agentic Applications 2026</sub>
- `2025-12-11` [GPT-5.2 system card updates cyber capability](../2025-12/2025-12-11-gpt-xi-tong-ka-wang.md)<br>  <sub>GPT-5.2 system card updates cyber capability</sub>
- `2025-12-22` [OpenAI: browser prompt injection "may never be fully solved"](../2025-12/2025-12-22-liu-lan-qi-ti-shi.md)<br>  <sub>OpenAI: browser prompt injection "may never be fully solved"</sub>
- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](../2026-02/2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-30-anthropic-constitutional-classifiers.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
