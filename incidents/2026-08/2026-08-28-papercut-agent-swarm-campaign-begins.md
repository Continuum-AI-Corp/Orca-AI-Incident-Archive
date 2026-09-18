---
id: 2026-08-28-papercut-agent-swarm-campaign-begins
title: "PaperCut AI agent swarm campaign begins"
title_zh: "PaperCut AI agent 蜂群战役启动"
title_ja: "PaperCut AIエージェント群集キャンペーンが始まる"
title_ko: "PaperCut AI 에이전트 군집 작전 시작"
title_de: "PaperCut-Kampagne eines KI-Agentenschwarms beginnt"
title_fr: "Début de la campagne d'essaim d'agents IA contre PaperCut"
title_es: "Comienza la campaña del enjambre de agentes de IA contra PaperCut"
date: 2026-08-28
date_precision: part
date_raw: "late 2026-08"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The launch point of the PaperCut campaign — agent-driven scanning and exploitation of PaperCut NG/MF was already under way in late August, and was only reconstructed publicly in mid-September.


summary_zh: |
  PaperCut 战役的启动点——8 月末已出现针对 PaperCut NG/MF 的 agent 驱动扫描与利用，9 月中旬才被公开还原。

summary_ja: |
  PaperCutキャンペーンの起点——PaperCut NG/MFに対するエージェント駆動のスキャンと悪用は8月下旬にすでに進行しており、公に再構成されたのは9月中旬だった。

summary_ko: |
  PaperCut 작전의 출발점 — 에이전트가 주도하는 PaperCut NG/MF 스캔과 악용이 8월 말에 이미 진행 중이었고, 9월 중순에야 공개적으로 재구성되었다.

summary_de: |
  Der Startpunkt der PaperCut-Kampagne — das agentengesteuerte Scannen und Ausnutzen von PaperCut NG/MF lief bereits Ende August, wurde öffentlich aber erst Mitte September rekonstruiert.

summary_fr: |
  Le point de départ de la campagne PaperCut — le scan et l'exploitation pilotés par agents de PaperCut NG/MF étaient déjà en cours fin août et n'ont été reconstitués publiquement qu'à la mi-septembre.

summary_es: |
  El punto de lanzamiento de la campaña PaperCut — el escaneo y la explotación dirigidos por agentes contra PaperCut NG/MF ya estaban en marcha a finales de agosto, y solo se reconstruyeron públicamente a mediados de septiembre.

sources:
  - url: https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html
    label: THN

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# PaperCut AI agent swarm campaign begins

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

The launch point of the PaperCut campaign — agent-driven scanning and exploitation of PaperCut NG/MF was already under way in late August, and was only reconstructed publicly in mid-September.

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
| 1 | THN | <https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-28` (raw: late 2026-08, precision `part`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-28-papercut-agent-swarm-campaign-begins` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-08-12` [Taiwan agent-swarm intrusion made public](2026-08-12-agent-tai-wan-feng-qun.md)<br>  <sub>Taiwan agent-swarm intrusion made public</sub>
- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
