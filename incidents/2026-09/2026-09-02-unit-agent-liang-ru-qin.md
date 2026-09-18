---
id: 2026-09-02-unit-agent-liang-ru-qin
title: "Unit 42: AI agents compress two weeks of intrusion work into 10 hours"
title_zh: "Unit 42：AI agent 把两周的入侵工作压到 10 小时内"
title_ja: "Unit 42：AIエージェントが2週間分の侵入作業を10時間に圧縮"
title_ko: "Unit 42: AI 에이전트가 2주 분량의 침입 작업을 10시간으로 압축"
title_de: "Unit 42: KI-Agenten verdichten zwei Wochen Intrusionsarbeit auf 10 Stunden"
title_fr: "Unit 42 : des agents IA compriment deux semaines de travail d'intrusion en 10 heures"
title_es: "Unit 42: los agentes de IA comprimen dos semanas de trabajo de intrusión en 10 horas"
date: 2026-09-02
date_precision: day
date_raw: "2026-09-02"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL, JP]

summary: |
  The intrusion was carried out with front-tier models + agent frameworks, using **known techniques across 50+ MITRE ATT&CK categories rather than zero-days** — the AI advantage is the efficiency of automating the standard attack workflow


summary_zh: |
  用前沿模型 + agent 框架实施入侵，利用的是 **50+ 个 MITRE ATT&CK 类别的已知手法而非零日** —— AI 的优势在于把标准攻击流程自动化的效率

summary_ja: |
  侵入はフロントティアのモデル＋エージェントフレームワークで実行され、**ゼロデイではなく50以上のMITRE ATT&CKカテゴリにわたる既知の技術**を使用した——AIの優位は、標準的な攻撃ワークフローを自動化する効率性にある

summary_ko: |
  이 침입은 최전선 모델 + 에이전트 프레임워크로 수행되었고 **제로데이가 아닌 50개 이상의 MITRE ATT&CK 범주에 걸친 알려진 기법**을 사용했다 — AI의 이점은 표준 공격 워크플로를 자동화하는 효율성이다

summary_de: |
  Die Intrusion wurde mit Frontier-Modellen + Agent-Frameworks durchgeführt und nutzte **bekannte Techniken aus über 50 MITRE-ATT&CK-Kategorien statt Zero-Days** — der KI-Vorteil liegt in der Effizienz der Automatisierung des Standard-Angriffsablaufs

summary_fr: |
  L'intrusion a été menée avec des modèles de première ligne + des frameworks d'agents, en utilisant **des techniques connues couvrant plus de 50 catégories MITRE ATT&CK plutôt que des zero-days** — l'avantage de l'IA réside dans l'efficacité de l'automatisation du flux d'attaque standard

summary_es: |
  La intrusión se llevó a cabo con modelos de primer nivel + marcos de agentes, usando **técnicas conocidas en más de 50 categorías de MITRE ATT&CK en lugar de zero-days** — la ventaja de la IA es la eficiencia de automatizar el flujo de ataque estándar

sources:
  - url: https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/
    label: Yasashii Cybersecurity (via Unit 42)

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Unit 42: AI agents compress two weeks of intrusion work into 10 hours

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

The intrusion was carried out with frontier models + agent frameworks, using **known techniques across 50+ MITRE ATT&CK categories rather than zero-days** — the AI advantage is the efficiency of automating the standard attack workflow

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Yasashii Cybersecurity (via Unit 42) | <https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-02` (raw: 2026-09-02, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) · [Japan](../../regions/jp.md) |
| Archive ID | `2026-09-02-unit-agent-liang-ru-qin` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-11` [Claude used to scan 1.8 million Android apps for secrets](2026-09-11-claude-scans-18m-android-apks.md)<br>  <sub>Claude used to scan 1.8 million Android apps for secrets</sub>
- `2026-09-10` [Anthropic September threat intelligence report](2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-09-15` [PaperCut AI agent swarm attack made public](2026-09-15-papercut-agent-swarm-disclosed.md)<br>  <sub>PaperCut AI agent swarm attack made public</sub>
- `2026-08-28` [PaperCut AI agent swarm campaign begins](../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-02-unit-agent-liang-ru-qin.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
