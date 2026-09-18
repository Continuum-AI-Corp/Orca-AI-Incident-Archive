---
id: 2026-09-15-papercut-agent-swarm-disclosed
title: "PaperCut AI agent swarm attack made public"
title_zh: "PaperCut AI agent 蜂群攻击公开"
title_ja: "PaperCutへのAIエージェント群集攻撃が公表される"
title_ko: "PaperCut AI 에이전트 군집 공격 공개"
title_de: "PaperCut-Angriff eines KI-Agentenschwarms veröffentlicht"
title_fr: "L'attaque par essaim d'agents IA contre PaperCut rendue publique"
title_es: "Se hace público el ataque del enjambre de agentes de IA contra PaperCut"
date: 2026-09-15
date_precision: part
date_raw: "mid 2026-09"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The agent-swarm campaign against PaperCut made public: 395 organizations in 48 countries affected, with as little as 7 minutes from first contact to domain administrator; the attacker's target list excluded 28 countries.


summary_zh: |
  针对 PaperCut 的 agent 蜂群战役被公开：48 个国家 395 个组织受影响，从首次接触到域管理员最短 7 分钟；攻击者的目标清单排除了 28 个国家。

summary_ja: |
  PaperCutに対するエージェント群集キャンペーンが公表された：48か国・395組織が影響を受け、最初の接触からドメイン管理者まで最短7分。攻撃者の標的リストは28か国を除外していた。

summary_ko: |
  PaperCut을 겨냥한 에이전트 군집 작전이 공개되었다. 48개국 395개 조직이 영향을 받았고, 최초 접촉에서 도메인 관리자까지 최단 7분이 걸렸으며 공격자의 표적 목록에서는 28개국이 제외되어 있었다.

summary_de: |
  Die Agentenschwarm-Kampagne gegen PaperCut wurde öffentlich: 395 Organisationen in 48 Ländern betroffen, mit nur 7 Minuten vom Erstkontakt bis zum Domänenadministrator; die Zielliste des Angreifers schloss 28 Länder aus.

summary_fr: |
  La campagne d'essaim d'agents contre PaperCut rendue publique : 395 organisations dans 48 pays touchées, avec à peine 7 minutes entre le premier contact et l'administrateur de domaine ; la liste de cibles de l'attaquant excluait 28 pays.

summary_es: |
  La campaña del enjambre de agentes contra PaperCut se hace pública: 395 organizaciones en 48 países afectadas, con tan solo 7 minutos desde el primer contacto hasta administrador de dominio; la lista de objetivos del atacante excluía 28 países.

sources:
  - url: https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html
    label: THN
  - url: https://www.darkreading.com/cyberattacks-data-breaches/papercut-ai-swarm-attack-cyber-kill-chain
    label: Dark Reading

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# PaperCut AI agent swarm attack made public

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

The agent-swarm campaign against PaperCut made public: 395 organizations in 48 countries affected, with as little as 7 minutes from first contact to domain administrator; the attacker's target list excluded 28 countries.

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

## Details

| Item | Data |
|---|---|
| Reported by | **Blackpoint Cyber** and **GreyNoise** (independent intelligence firms); **Arctic Wolf** also tracked related activity |
| Actor | Russian-speaking; assessed from tradecraft as an **initial access broker** |
| Time | GreyNoise has tracked malicious IP activity since **early 2026-07**; the earliest records recovered from the attacker's workspace show that **vulnerability research began 08-31** |
| Method | Trained **hundreds of AI agents** into a swarm in a lab environment, autonomously scanning PaperCut NG/MF print-management servers and opportunistically attempting Windows AD environments |
| Tech stack | **OpenAI Codex orchestration framework + DeepSeek models** (the latter chosen for weaker content-safety restrictions), plus **Hindsight** (persistent memory for AI agents) and **AionUi** (a unified graphical workspace for concurrent multi-agent work) |
| Vulnerabilities | **CVE-2026-81578** (web admin interface **authentication bypass**, CVSS 8.8) + **CVE-2026-82078** (**unsafe dynamic class loading**, CVSS 9.4), **both in-the-wild zero-days**, with exploit code developed by AI. PaperCut first shipped an emergency patch, then replaced it with a formal fix |
| Impact | **440+ instances**, **395 victim organizations**, **48 countries**, of which **12 organizations had domain administrator privileges obtained** |
| Speed | From vulnerability research to a multithreaded validation tool: hours; **under 4 hours to first RCE against a real victim**; once the swarm was in full operation, **11 organizations compromised within 26 seconds**; in one US high-school case, **only 7 minutes from initial access to domain administrator** |
| Target distribution | Mainly the **US education sector**, plus the UK, France, Spain, Canada, Belgium, Portugal, Australia, Germany and Switzerland; Arctic Wolf observed everything from K-12 to large comprehensive universities<br>⚠️ **The breakdown "204 of the 395 are educational institutions" appears only in second-hand roundups; first-hand reporting does not give that figure, so it is downgraded to unverified** |
| Attacker's exclusion list | **28 countries actively excluded, including Russia, China, Iran, Venezuela, Pakistan and Bangladesh** — an important attribution signal |
| Significance | Dark Reading: **once set up, the AI agents carried out scanning, exploit development and initial post-compromise actions with almost no human direction** |

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html> |
| 2 | Dark Reading | <https://www.darkreading.com/cyberattacks-data-breaches/papercut-ai-swarm-attack-cyber-kill-chain> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-15` (raw: mid 2026-09, precision `part`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-15-papercut-agent-swarm-disclosed` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-11` [Claude used to scan 1.8 million Android apps for secrets](2026-09-11-claude-scans-18m-android-apks.md)<br>  <sub>Claude used to scan 1.8 million Android apps for secrets</sub>
- `2026-09-10` [Anthropic September threat intelligence report](2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-09-02` [Unit 42: AI agents compress two weeks of intrusion work into 10 hours](2026-09-02-unit-agent-liang-ru-qin.md)<br>  <sub>Unit 42: AI agents compress two weeks of intrusion work into 10 hours</sub>
- `2026-08-28` [PaperCut AI agent swarm campaign begins](../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
