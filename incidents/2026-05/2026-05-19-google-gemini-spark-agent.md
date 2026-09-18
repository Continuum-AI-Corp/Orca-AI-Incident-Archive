---
id: 2026-05-19-google-gemini-spark-agent
title: "Google ships Gemini Spark autonomous agents"
title_zh: "Google 发布 Gemini Spark 自主 agent"
title_ja: "GoogleがGemini Spark自律エージェントを提供開始"
title_ko: "구글, Gemini Spark 자율 에이전트 출시"
title_de: "Google liefert autonome Gemini-Spark-Agenten aus"
title_fr: "Google livre les agents autonomes Gemini Spark"
title_es: "Google lanza los agentes autónomos Gemini Spark"
date: 2026-05-19
date_precision: day
date_raw: "2026-05-19"

kind: policy
type: [OTHER]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Built on Gemini 3.5 Flash plus the Antigravity control plane; can run multi-step tasks across Workspace


summary_zh: |
  基于 Gemini 3.5 Flash + Antigravity 控制平面，可跨 Workspace 执行多步任务

summary_ja: |
  Gemini 3.5 FlashとAntigravityコントロールプレーン上に構築され、Workspaceをまたいだ多段階タスクを実行できる

summary_ko: |
  Gemini 3.5 Flash와 Antigravity 제어 평면을 기반으로 하며, Workspace 전반에서 다단계 작업을 수행할 수 있다

summary_de: |
  Basiert auf Gemini 3.5 Flash plus der Antigravity-Kontrollschicht; kann mehrstufige Aufgaben über Workspace hinweg ausführen

summary_fr: |
  Construits sur Gemini 3.5 Flash plus le plan de contrôle Antigravity ; peuvent exécuter des tâches multi-étapes dans Workspace

summary_es: |
  Construidos sobre Gemini 3.5 Flash más el plano de control Antigravity; pueden ejecutar tareas de varios pasos en Workspace

sources:
  - url: https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/
    label: Google

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Google ships Gemini Spark autonomous agents

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Built on Gemini 3.5 Flash plus the Antigravity control plane; can run multi-step tasks across Workspace

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
| 1 | Google | <https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-19` (raw: 2026-05-19, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-19-google-gemini-spark-agent` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-19-google-gemini-spark-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
