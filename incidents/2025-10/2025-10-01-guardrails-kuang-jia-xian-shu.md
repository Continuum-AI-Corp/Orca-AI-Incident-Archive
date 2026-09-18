---
id: 2025-10-01-guardrails-kuang-jia-xian-shu
title: "OpenAI Guardrails broken days after launch"
title_zh: "OpenAI Guardrails 框架上线数日被攻破"
title_ja: "OpenAI Guardrailsが公開数日で破られる"
title_ko: "OpenAI Guardrails, 출시 며칠 만에 뚫려"
title_de: "OpenAI Guardrails wenige Tage nach dem Start durchbrochen"
title_fr: "OpenAI Guardrails cassé quelques jours après son lancement"
title_es: "Guardrails de OpenAI se rompe días después del lanzamiento"
date: 2025-10-01
date_precision: month
date_raw: "2025-10"

kind: research
type: [OTHER]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  HiddenLayer: the new framework's LLM judge can itself be prompt-injected


summary_zh: |
  HiddenLayer：新框架的 LLM 裁判本身可被提示注入

summary_ja: |
  HiddenLayer：新しいフレームワークのLLMジャッジ自体がプロンプトインジェクションを受け得る

summary_ko: |
  HiddenLayer: 새 프레임워크의 LLM 심사자(judge) 자체가 프롬프트 인젝션에 당할 수 있다

summary_de: |
  HiddenLayer: Der LLM-Judge des neuen Frameworks kann selbst per Prompt-Injection manipuliert werden

summary_fr: |
  HiddenLayer : le juge LLM du nouveau framework peut lui-même être victime d'une injection de prompt

summary_es: |
  HiddenLayer: el juez LLM del nuevo marco puede a su vez ser objeto de inyección de prompt

sources:
  - url: https://www.secrss.com/articles/86614
    label: Security Reference 2025 roundup

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# OpenAI Guardrails broken days after launch

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

HiddenLayer: the new framework's LLM judge can itself be prompt-injected

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
| 1 | Security Reference 2025 roundup | <https://www.secrss.com/articles/86614> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-01` (raw: 2025-10, precision `month`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-01-guardrails-kuang-jia-xian-shu` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-01-guardrails-kuang-jia-xian-shu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
