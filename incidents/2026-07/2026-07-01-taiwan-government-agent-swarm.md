---
id: 2026-07-01-taiwan-government-agent-swarm
title: "Taiwan's nuclear safety commission and other agencies breached by an agent swarm"
title_zh: "台湾核安会等政府机构被 agent 蜂群攻破"
title_ja: "台湾の原子力安全委員会などがエージェント群集に侵害される"
title_ko: "대만 원자력안전위원회 등 기관, 에이전트 군집에 침해"
title_de: "Taiwans Atomaufsichtsbehörde und weitere Stellen von einem Agentenschwarm kompromittiert"
title_fr: "La commission de sûreté nucléaire taïwanaise et d'autres agences compromises par un essaim d'agents"
title_es: "La comisión de seguridad nuclear de Taiwán y otras agencias vulneradas por un enjambre de agentes"
date: 2026-07-01
date_end: 2026-07-04
date_precision: day
date_raw: "2026-07-01→04"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [TW]

summary: |
  See the expansion below. ⚠️ **v1 badly underrated this one (originally a one-line grade-C entry)**


summary_zh: |
  见下方展开。⚠️ **v1 严重低估了这条（原列为 C 级单行）**

summary_ja: |
  後述の詳細を参照。⚠️ **v1ではこれが著しく過小評価されていた（当初は1行のグレードC項目）**

summary_ko: |
  아래 확장 참조. ⚠️ **v1에서는 이 사건을 크게 과소평가했다(원래 한 줄짜리 C등급 항목이었다)**

summary_de: |
  Siehe die Erweiterung unten. ⚠️ **v1 bewertete diesen Fall deutlich zu niedrig (ursprünglich ein einzeiliger Eintrag der Stufe C)**

summary_fr: |
  Voir le développement ci-dessous. ⚠️ **La v1 a fortement sous-estimé cet incident (à l'origine une entrée d'une ligne de grade C)**

summary_es: |
  Ver la ampliación a continuación. ⚠️ **La v1 subestimó gravemente esta entrada (originalmente una entrada de una línea y grado C)**

sources:
  - url: https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055
    label: The Register
  - url: https://www.cnn.com/2026/08/13/tech/china-taiwan-ai-agent-cyberattack-intl-hnk
    label: CNN
  - url: https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/
    label: CyberScoop

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Taiwan's nuclear safety commission and other agencies breached by an agent swarm

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

See the expansion below. ⚠️ **v1 badly underrated this one (originally a one-line grade-C entry)**

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
| Disclosed by | Israel's **Dream** (research published 2026-08-12). Dream initially said only "government entities in Asia"; **the Financial Times named Taiwan** |
| Targets | Taiwanese government systems, the **nuclear safety regulator**, IT supply-chain vendors, government email systems, and **more than 7 energy companies** |
| Attribution | Suspected China-linked operators. Dream says the operational documents "point to a Chinese-speaking operator", **but does not attribute it to the Chinese government or a specific group** |
| Frameworks | Open-source **Hermes** + **OpenClaw** |
| Scale | Up to **8 sub-agents**, **12 waves of attacks** over four days, **85 government accounts** compromised, **2,500+ personnel records** taken, leaving a **160MB / 1,395-file** operations archive |
| Guardrail bypass | Hermes and OpenClaw both have safety checks meant to block offensive use — the operators **framed the whole campaign as an "authorised penetration test"** and walked straight past them |
| Autonomy | Dream calls it "**near-autonomous**" rather than fully autonomous: the framework has a "learning loop", the model searches vulnerability databases and GitHub on its own for usable techniques, and can self-correct. But researchers told CyberScoop that **reaching this level takes far more work than "running a model"** |

## Sources

| # | Source | Link |
|---|---|---|
| 1 | The Register | <https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055> |
| 2 | CNN | <https://www.cnn.com/2026/08/13/tech/china-taiwan-ai-agent-cyberattack-intl-hnk> |
| 3 | CyberScoop | <https://cyberscoop.com/near-autonomous-ai-attack-government-target-taiwan/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-01` → `2026-07-04` (raw: 2026-07-01→04, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Taiwan](../../regions/tw.md) |
| Archive ID | `2026-07-01-taiwan-government-agent-swarm` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Hermes Agent attacks Thailand's Ministry of Finance unattended](2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub>
- `2026-07-30` [Unit 42: autonomous campaigns run by Chinese-speaking operators](2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br>  <sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-01-taiwan-government-agent-swarm.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
