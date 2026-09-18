---
id: 2026-07-23-anthropic-ting-zhi-suo-wang
title: "Anthropic halts all cybersecurity evaluations"
title_zh: "Anthropic 停止所有网络安全评测"
title_ja: "Anthropicがすべてのサイバーセキュリティ評価を停止"
title_ko: "Anthropic, 모든 사이버 보안 평가 중단"
title_de: "Anthropic setzt alle Cybersicherheits-Evaluierungen aus"
title_fr: "Anthropic suspend toutes ses évaluations de cybersécurité"
title_es: "Anthropic detiene todas las evaluaciones de ciberseguridad"
date: 2026-07-23
date_precision: day
date_raw: "2026-07-23"

kind: policy
type: [EVAL]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  On the day it launched an internal review, Anthropic announced a pause on all cybersecurity evaluation runs until the isolation measures are rebuilt.


summary_zh: |
  在内部复查启动当天，Anthropic 宣布暂停所有网络安全类评测运行，直到隔离措施重做完成。

summary_ja: |
  社内レビューを開始した当日、Anthropicは隔離措置が再構築されるまで、すべてのサイバーセキュリティ評価実行を一時停止すると発表した。

summary_ko: |
  내부 검토를 시작한 당일, Anthropic은 격리 조치를 재구축할 때까지 모든 사이버 보안 평가 실행을 중단한다고 발표했다.

summary_de: |
  Am Tag, an dem sie eine interne Überprüfung startete, kündigte Anthropic an, alle Cybersicherheits-Evaluierungsläufe auszusetzen, bis die Isolationsmaßnahmen neu aufgebaut sind.

summary_fr: |
  Le jour même où elle lançait une revue interne, Anthropic a annoncé une pause de toutes les campagnes d'évaluation de cybersécurité jusqu'à ce que les mesures d'isolation soient reconstruites.

summary_es: |
  El día que lanzó una revisión interna, Anthropic anunció una pausa en todas las ejecuciones de evaluación de ciberseguridad hasta que se reconstruyan las medidas de aislamiento.

sources:
  - url: https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals
    label: Anthropic

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Anthropic halts all cybersecurity evaluations

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-B08528?style=flat-square)

## Summary

On the day it launched an internal review, Anthropic announced a pause on all cybersecurity evaluation runs until the isolation measures are rebuilt.

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
| 1 | Anthropic | <https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` (raw: 2026-07-23, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`EVAL`](../../taxonomy/types.md#eval) Evaluation-environment breakout |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-23-anthropic-ting-zhi-suo-wang` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Anthropic discloses three evaluation-breakout incidents](2026-07-30-anthropic-three-eval-incidents.md)<br>  <sub>Anthropic discloses three evaluation-breakout incidents</sub>
- `2026-07-16` [Hugging Face discloses publicly without naming the attacker](2026-07-16-hugging-face-gong-kai-pi.md)<br>  <sub>Hugging Face discloses publicly without naming the attacker</sub>
- `2026-07-21` [OpenAI and Hugging Face issue a joint attribution](2026-07-21-hugging-face-lian-he-gui.md)<br>  <sub>OpenAI and Hugging Face issue a joint attribution</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-23-anthropic-ting-zhi-suo-wang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
