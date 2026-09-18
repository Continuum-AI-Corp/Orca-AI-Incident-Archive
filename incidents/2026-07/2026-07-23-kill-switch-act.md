---
id: 2026-07-23-kill-switch-act
title: "US representatives introduce the AI Kill Switch Act"
title_zh: "美国众议员提出「AI Kill Switch Act」"
title_ja: "米下院議員がAI Kill Switch Actを提出"
title_ko: "미국 하원 의원, AI 킬 스위치 법안 발의"
title_de: "US-Abgeordnete bringen den AI Kill Switch Act ein"
title_fr: "Des représentants américains présentent l'AI Kill Switch Act"
title_es: "Representantes de Estados Unidos presentan la Ley del Interruptor de Apagado de la IA"
date: 2026-07-23
date_precision: day
date_raw: "2026-07-23"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [US]

summary: |
  Ted Lieu / Nathaniel Moran: would require developers to retain kill-switch capability and report incidents


summary_zh: |
  Ted Lieu / Nathaniel Moran：要求开发者保有关停能力并上报事故

summary_ja: |
  Ted Lieu氏／Nathaniel Moran氏：開発者にキルスイッチ能力の保持とインシデントの報告を義務付ける内容

summary_ko: |
  Ted Lieu / Nathaniel Moran: 개발자에게 킬 스위치 능력 유지와 사고 보고를 의무화하는 법안

summary_de: |
  Ted Lieu / Nathaniel Moran: würde Entwickler verpflichten, eine Kill-Switch-Fähigkeit vorzuhalten und Vorfälle zu melden

summary_fr: |
  Ted Lieu / Nathaniel Moran : imposerait aux développeurs de conserver une capacité d'arrêt d'urgence et de déclarer les incidents

summary_es: |
  Ted Lieu / Nathaniel Moran: exigiría a los desarrolladores conservar la capacidad de interruptor de apagado y notificar incidentes

sources:
  - url: https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks
    label: Wikipedia

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# US representatives introduce the AI Kill Switch Act

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Ted Lieu / Nathaniel Moran: would require developers to retain kill-switch capability and report incidents

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
| 1 | Wikipedia | <https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` (raw: 2026-07-23, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-07-23-kill-switch-act` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-07-17` [Anthropic, "A CISO's guide to agentic AI"](2026-07-17-anthropic-ciso-guide-agentic.md)<br>  <sub>Anthropic, "A CISO's guide to agentic AI"</sub>
- `2026-07-27` [NVIDIA convenes the Open Secure AI Alliance](2026-07-27-nvidia-open-secure-alliance.md)<br>  <sub>NVIDIA convenes the Open Secure AI Alliance</sub>
- `2026-07-28` ["Pacing the Frontier" open letter](2026-07-28-pacing-frontier-gong-kai-xin.md)<br>  <sub>"Pacing the Frontier" open letter</sub>
- `2026-07-29` [Perplexity open-sources Numbat for agent behaviour monitoring](2026-07-29-perplexity-agent-numbat.md)<br>  <sub>Perplexity open-sources Numbat for agent behaviour monitoring</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-23-kill-switch-act.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
