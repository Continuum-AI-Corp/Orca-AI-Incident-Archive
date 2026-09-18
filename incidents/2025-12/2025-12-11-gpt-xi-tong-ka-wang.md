---
id: 2025-12-11-gpt-xi-tong-ka-wang
title: "GPT-5.2 system card updates cyber capability"
title_zh: "GPT-5.2 系统卡网络安全更新"
title_ja: "GPT-5.2システムカードがサイバー能力を更新"
title_ko: "GPT-5.2 시스템 카드, 사이버 능력 등급 상향"
title_de: "GPT-5.2 System Card aktualisiert die Cyber-Fähigkeiten"
title_fr: "La system card de GPT-5.2 met à jour la capacité cyber"
title_es: "El system card de GPT-5.2 actualiza la capacidad ciber"
date: 2025-12-11
date_precision: day
date_raw: "2025-12-11"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  In the GPT-5.2 system card, OpenAI updates its cyber capability assessment and for the first time classifies "could assist real intrusions" as a capability level requiring mitigation.


summary_zh: |
  OpenAI 在 GPT-5.2 系统卡中更新网络安全能力评估，首次把「可协助真实入侵」列为需要缓解的能力等级。

summary_ja: |
  GPT-5.2のシステムカードで、OpenAIはサイバー能力評価を更新し、「実際の侵入を支援し得る」を初めて緩和策を要する能力レベルとして分類した。

summary_ko: |
  GPT-5.2 시스템 카드에서 OpenAI는 사이버 능력 평가를 갱신하고 "실제 침입을 도울 수 있음"을 처음으로 완화 조치가 필요한 능력 등급으로 분류했다.

summary_de: |
  In der GPT-5.2 System Card aktualisiert OpenAI seine Bewertung der Cyber-Fähigkeiten und stuft erstmals „könnte echte Intrusionen unterstützen“ als Fähigkeitsstufe ein, die Gegenmaßnahmen erfordert.

summary_fr: |
  Dans la system card de GPT-5.2, OpenAI met à jour son évaluation de capacité cyber et classe pour la première fois « pourrait aider à de vraies intrusions » comme un niveau de capacité nécessitant des mesures d'atténuation.

summary_es: |
  En el system card de GPT-5.2, OpenAI actualiza su evaluación de capacidad ciber y por primera vez clasifica "podría facilitar intrusiones reales" como un nivel de capacidad que exige mitigación.

sources:
  - url: https://deploymentsafety.openai.com/gpt-5-2/cybersecurity
    label: OpenAI Deployment Safety

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# GPT-5.2 system card updates cyber capability

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

In the GPT-5.2 system card, OpenAI updates its cyber capability assessment and for the first time classifies "could assist real intrusions" as a capability level requiring mitigation.

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
| 1 | OpenAI Deployment Safety | <https://deploymentsafety.openai.com/gpt-5-2/cybersecurity> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-11` (raw: 2025-12-11, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-11-gpt-xi-tong-ka-wang` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-12-09` [OWASP Top 10 for Agentic Applications 2026](2025-12-09-owasp-top-agentic-applications.md)<br>  <sub>OWASP Top 10 for Agentic Applications 2026</sub>
- `2025-12-22` [OpenAI: browser prompt injection "may never be fully solved"](2025-12-22-liu-lan-qi-ti-shi.md)<br>  <sub>OpenAI: browser prompt injection "may never be fully solved"</sub>
- `2025-11-19` [EU "Digital Omnibus" proposes delaying the AI Act](../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>
- `2026-01-30` [Anthropic ships Constitutional Classifiers++](../2026-01/2026-01-30-anthropic-constitutional-classifiers.md)<br>  <sub>Anthropic ships Constitutional Classifiers++</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-11-gpt-xi-tong-ka-wang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
