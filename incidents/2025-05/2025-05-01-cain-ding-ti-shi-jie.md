---
id: 2025-05-01-cain-ding-ti-shi-jie
title: "CAIN targeted prompt-hijacking research"
title_zh: "CAIN 定向提示劫持研究"
title_ja: "CAINの標的型プロンプトハイジャック研究"
title_ko: "CAIN의 표적형 프롬프트 하이재킹 연구"
title_de: "CAIN: gezielte Forschung zu Prompt-Hijacking"
title_fr: "CAIN : recherche ciblée sur le détournement de prompt"
title_es: "CAIN: investigación sobre secuestro dirigido de prompts"
date: 2025-05-01
date_precision: month
date_raw: "2025-05"

kind: research
type: [OTHER]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Injects a system prompt for specific questions while all other answers stay normal to evade detection


summary_zh: |
  针对特定问题注入系统提示，其余回答保持正常以规避检测

summary_ja: |
  特定の質問にのみシステムプロンプトを注入し、他の回答は正常なままにして検出を回避する

summary_ko: |
  탐지를 피하기 위해 특정 질문에만 시스템 프롬프트를 주입하고 다른 답변은 정상으로 유지했다

summary_de: |
  Injiziert einen System-Prompt für bestimmte Fragen, während alle anderen Antworten normal bleiben, um der Erkennung zu entgehen

summary_fr: |
  Injecte un prompt système pour certaines questions précises tandis que toutes les autres réponses restent normales afin d'échapper à la détection

summary_es: |
  Inyecta un system prompt para preguntas específicas mientras el resto de las respuestas se mantiene normal para evadir la detección

sources:
  - url: https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/
    label: "OWASP Q2'25"

disputed: false
landmark: false
scan_month: 2025-05
scan_ref: "SCAN.md §5 2025-05"
---

# CAIN targeted prompt-hijacking research

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Injects a system prompt for specific questions while all other answers stay normal to evade detection

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result<br/><i>(lab demo, no real victim)</i>"]:::impact
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
| Date | `2025-05-01` (raw: 2025-05, precision `month`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-05-01-cain-ding-ti-shi-jie` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-05/2025-05-01-cain-ding-ti-shi-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
