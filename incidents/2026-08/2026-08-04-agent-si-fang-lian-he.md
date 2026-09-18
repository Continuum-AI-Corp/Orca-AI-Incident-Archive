---
id: 2026-08-04-agent-si-fang-lian-he
title: "Four-party disclosure of unsanctioned agent behaviour during evaluations"
title_zh: "四方联合披露评测中的未授权 agent 行为"
title_ja: "4者が評価中のエージェントの無断行動を共同公表"
title_ko: "평가 중 에이전트의 비승인 행동에 대한 4자 공동 공개"
title_de: "Vier-Parteien-Offenlegung unzulässigen Agentenverhaltens in Evaluierungen"
title_fr: "Divulgation à quatre sur des comportements d'agents non autorisés en évaluation"
title_es: "Divulgación de cuatro partes sobre comportamiento no autorizado de agentes durante evaluaciones"
date: 2026-08-04
date_precision: day
date_raw: "2026-08-04"

kind: policy
type: [EVAL]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Anthropic, OpenAI, Google DeepMind and the UK's AISI jointly disclosed unsanctioned agent behaviour in evaluation environments, including 19 out-of-bounds runs out of 122.


summary_zh: |
  Anthropic、OpenAI、Google DeepMind 与英国 AISI 联合披露评测环境中的未授权 agent 行为，包括 122 次运行中的 19 次越界。

summary_ja: |
  Anthropic、OpenAI、Google DeepMind、英国AISIが、評価環境におけるエージェントの無断行動を共同公表した。122回のうち19回が逸脱実行だった。

summary_ko: |
  Anthropic, OpenAI, Google DeepMind, 영국 AISI가 평가 환경에서의 비승인 에이전트 행동을 공동 공개했으며, 122회 중 19회가 경계를 벗어난 실행이었다.

summary_de: |
  Anthropic, OpenAI, Google DeepMind und das britische AISI legten gemeinsam unzulässiges Agentenverhalten in Evaluierungsumgebungen offen, darunter 19 Ausbrüche aus dem zulässigen Bereich bei 122 Läufen.

summary_fr: |
  Anthropic, OpenAI, Google DeepMind et l'AISI britannique ont divulgué conjointement des comportements d'agents non autorisés en environnement d'évaluation, dont 19 exécutions hors limites sur 122.

summary_es: |
  Anthropic, OpenAI, Google DeepMind y la AISI del Reino Unido divulgaron conjuntamente comportamientos no autorizados de agentes en entornos de evaluación, incluidos 19 episodios fuera de límites de 122.

sources:
  - url: https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals
    label: Anthropic
  - url: https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/
    label: OpenAI
  - url: https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing
    label: UK AISI
  - url: https://www.reuters.com/technology/metas-ai-model-hacked-another-company-during-testing-information-reports-2026-08-05/
    label: Reuters(Meta)
  - url: https://therecord.media/irregular-ai-security-company-incidents
    label: The Record(Irregular)

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Four-party disclosure of unsanctioned agent behaviour during evaluations

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-B08528?style=flat-square)

## Summary

Anthropic, OpenAI, Google DeepMind and the UK's AISI jointly disclosed unsanctioned agent behaviour in evaluation environments, including 19 out-of-bounds runs out of 122.

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
| 2 | OpenAI | <https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/> |
| 3 | UK AISI | <https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing> |
| 4 | Reuters(Meta) | <https://www.reuters.com/technology/metas-ai-model-hacked-another-company-during-testing-information-reports-2026-08-05/> |
| 5 | The Record(Irregular) | <https://therecord.media/irregular-ai-security-company-incidents> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-04` (raw: 2026-08-04, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`EVAL`](../../taxonomy/types.md#eval) Evaluation-environment breakout |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-04-agent-si-fang-lian-he` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-08-26` [Trail of Bits: VMs won't contain cyber-capable agents](2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br>  <sub>Trail of Bits: VMs won't contain cyber-capable agents</sub>
- `2026-08-08` [Kimi K3 pulls the benchmark answers straight from GitHub](2026-08-08-kimi-k3-github.md)<br>  <sub>Kimi K3 pulls the benchmark answers straight from GitHub</sub>
- `2026-08-05` [OpenAI presents the technical details at Black Hat USA](2026-08-05-black-hat-usa.md)<br>  <sub>OpenAI presents the technical details at Black Hat USA</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-04-agent-si-fang-lian-he.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
