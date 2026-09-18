---
id: 2025-02-25-cot-jailbreak-si-wei-lian
title: "Chain-of-thought jailbreak"
title_zh: "思维链越狱（CoT jailbreak）"
title_ja: "思考連鎖（CoT）ジェイルブレイク"
title_ko: "사고 연쇄(CoT) 탈옥"
title_de: "Chain-of-Thought-Jailbreak"
title_fr: "Jailbreak par chaîne de raisonnement"
title_es: "Jailbreak mediante cadena de pensamiento"
date: 2025-02-25
date_precision: day
date_raw: "2025-02-25"

kind: research
type: [OTHER]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Embeds malicious instructions in the reasoning chain; effective against OpenAI o1/o3, Gemini 2.0 Flash Thinking and Claude 3.7


summary_zh: |
  把恶意指令嵌进推理链，对 OpenAI o1/o3、Gemini 2.0 Flash Thinking、Claude 3.7 均有效

summary_ja: |
  推論チェーンに悪意ある指示を埋め込む手口。OpenAI o1/o3、Gemini 2.0 Flash Thinking、Claude 3.7に対して有効

summary_ko: |
  추론 연쇄에 악성 지시를 삽입한다. OpenAI o1/o3, Gemini 2.0 Flash Thinking, Claude 3.7에 효과적이다

summary_de: |
  Bettet bösartige Anweisungen in die Argumentationskette ein; wirksam gegen OpenAI o1/o3, Gemini 2.0 Flash Thinking und Claude 3.7

summary_fr: |
  Intègre des instructions malveillantes dans la chaîne de raisonnement ; efficace contre OpenAI o1/o3, Gemini 2.0 Flash Thinking et Claude 3.7

summary_es: |
  Incrusta instrucciones maliciosas en la cadena de razonamiento; eficaz contra OpenAI o1/o3, Gemini 2.0 Flash Thinking y Claude 3.7

sources:
  - url: https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/
    label: "OWASP Jan-Feb'25"

disputed: false
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# Chain-of-thought jailbreak

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Embeds malicious instructions in the reasoning chain; effective against OpenAI o1/o3, Gemini 2.0 Flash Thinking and Claude 3.7

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
| 1 | OWASP Jan-Feb'25 | <https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-25` (raw: 2025-02-25, precision `day`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-02-25-cot-jailbreak-si-wei-lian` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-25-cot-jailbreak-si-wei-lian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
