---
id: 2026-05-01-pwn2own-berlin-ling-can-sai
title: "Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list"
title_zh: "Pwn2Own Berlin 2026：47 个零日，AI 把参赛量撑爆"
title_ja: "Pwn2Own Berlin 2026：AIで応募が殺到し47件のゼロデイ"
title_ko: "Pwn2Own Berlin 2026: AI가 출품 목록을 뒤덮어 제로데이 47건"
title_de: "Pwn2Own Berlin 2026: 47 Zero-Days, während KI die Einsendeliste flutet"
title_fr: "Pwn2Own Berlin 2026 : 47 zero-days alors que l'IA submerge les candidatures"
title_es: "Pwn2Own Berlín 2026: 47 zero-days mientras la IA inunda la lista de inscripciones"
date: 2026-05-01
date_precision: month
date_raw: "2026-05"

kind: policy
type: [GOV]
severity: info
confidence: B
real_harm: null
ai_involvement: confirmed

region: [EU]

summary: |
  $1,298,250 in prize money; dozens of submissions were rejected, as AI-driven entry volume exceeded what the event could handle


summary_zh: |
  奖金 $1,298,250；数十份提交被拒，提交量因 AI 超出赛事承载能力

summary_ja: |
  賞金は129万8,250ドル。AIによる応募量がイベントの処理能力を超え、数十件の提出が拒否された

summary_ko: |
  상금 1,298,250달러. AI 기반 출품 물량이 대회가 감당할 수준을 넘어서면서 수십 건의 제출이 거부되었다

summary_de: |
  $1,298,250 an Preisgeldern; Dutzende Einsendungen wurden abgelehnt, da das KI-getriebene Einsendeaufkommen die Kapazität der Veranstaltung überstieg

summary_fr: |
  1 298 250 $ de primes ; des dizaines de soumissions ont été rejetées, le volume de candidatures pilotées par IA dépassant ce que l'événement pouvait traiter

summary_es: |
  $1,298,250 en premios; se rechazaron decenas de propuestas, ya que el volumen de inscripciones impulsado por IA superó lo que el evento podía gestionar

sources:
  - url: https://theori.io/ko/blog/2026-h1-hot-security-issue-case
    label: Theori

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

$1,298,250 in prize money; dozens of submissions were rejected, as AI-driven entry volume exceeded what the event could handle

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
| 1 | Theori | <https://theori.io/ko/blog/2026-h1-hot-security-issue-case> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-01` (raw: 2026-05, precision `month`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Europe](../../regions/eu.md) |
| Archive ID | `2026-05-01-pwn2own-berlin-ling-can-sai` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-04` [Five Eyes: agentic AI is not ready for rapid rollout](2026-05-04-five-eyes-agentic.md)<br>  <sub>Five Eyes: agentic AI is not ready for rapid rollout</sub>
- `2026-05-27` [Anthropic publishes "Zero Trust for AI agents"](2026-05-27-anthropic-zero-trust-agents.md)<br>  <sub>Anthropic publishes "Zero Trust for AI agents"</sub>
- `2026-04-07` [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](../2026-04/2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-01-pwn2own-berlin-ling-can-sai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
