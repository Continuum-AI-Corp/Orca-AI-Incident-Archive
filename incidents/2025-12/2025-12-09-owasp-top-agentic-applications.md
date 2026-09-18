---
id: 2025-12-09-owasp-top-agentic-applications
title: "OWASP Top 10 for Agentic Applications 2026"
title_zh: "OWASP Top 10 for Agentic Applications 2026"
title_ja: "OWASP Top 10 for Agentic Applications 2026"
title_ko: "OWASP 에이전틱 애플리케이션 Top 10 2026"
title_de: "OWASP Top 10 for Agentic Applications 2026"
title_fr: "OWASP Top 10 for Agentic Applications 2026"
title_es: "OWASP Top 10 for Agentic Applications 2026"
date: 2025-12-09
date_precision: day
date_raw: "2025-12-09"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Peer-reviewed by 100+ experts, the first Top 10 specifically for autonomous agents. Includes **ASI01 Agent Goal Hijack**, **ASI04 Agentic Supply Chain**, **ASI05 Unexpected Code Execution** and **ASI10 Rogue Agents**


summary_zh: |
  100+ 专家同行评审，首个专门针对自主 agent 的 Top 10。含 **ASI01 Agent Goal Hijack**、**ASI04 Agentic Supply Chain**、**ASI05 Unexpected Code Execution**、**ASI10 Rogue Agents**

summary_ja: |
  100人以上の専門家による査読済みで、自律エージェントに特化した初のTop 10。**ASI01 Agent Goal Hijack**、**ASI04 Agentic Supply Chain**、**ASI05 Unexpected Code Execution**、**ASI10 Rogue Agents**などを収録

summary_ko: |
  전문가 100명 이상의 동료 검토를 거쳤으며, 자율 에이전트만을 위한 최초의 Top 10이다. **ASI01 에이전트 목표 하이재킹**, **ASI04 에이전틱 공급망**, **ASI05 예기치 않은 코드 실행**, **ASI10 로그 에이전트**가 포함된다

summary_de: |
  Von 100+ Experten begutachtet, die erste Top 10 speziell für autonome Agenten. Enthält **ASI01 Agent Goal Hijack**, **ASI04 Agentic Supply Chain**, **ASI05 Unexpected Code Execution** und **ASI10 Rogue Agents**

summary_fr: |
  Évalué par plus de 100 experts, le premier Top 10 spécifiquement consacré aux agents autonomes. Comprend **ASI01 Agent Goal Hijack**, **ASI04 Agentic Supply Chain**, **ASI05 Unexpected Code Execution** et **ASI10 Rogue Agents**

summary_es: |
  Revisado por pares por más de 100 expertos, el primer Top 10 específicamente para agentes autónomos. Incluye **ASI01 Agent Goal Hijack**, **ASI04 Agentic Supply Chain**, **ASI05 Unexpected Code Execution** y **ASI10 Rogue Agents**

sources:
  - url: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
    label: OWASP

disputed: false
landmark: true
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# OWASP Top 10 for Agentic Applications 2026

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Peer-reviewed by 100+ experts, the first Top 10 specifically for autonomous agents. Includes **ASI01 Agent Goal Hijack**, **ASI04 Agentic Supply Chain**, **ASI05 Unexpected Code Execution** and **ASI10 Rogue Agents**

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
| 1 | OWASP | <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-09` (raw: 2025-12-09, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-09-owasp-top-agentic-applications` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-12-11` [GPT-5.2 system card updates cyber capability](2025-12-11-gpt-xi-tong-ka-wang.md)<br>  <sub>GPT-5.2 system card updates cyber capability</sub>
- `2025-12-22` [OpenAI: browser prompt injection "may never be fully solved"](2025-12-22-liu-lan-qi-ti-shi.md)<br>  <sub>OpenAI: browser prompt injection "may never be fully solved"</sub>
- `2025-11-19` [EU "Digital Omnibus" proposes delaying the AI Act](../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>
- `2026-01-30` [Anthropic ships Constitutional Classifiers++](../2026-01/2026-01-30-anthropic-constitutional-classifiers.md)<br>  <sub>Anthropic ships Constitutional Classifiers++</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-09-owasp-top-agentic-applications.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
