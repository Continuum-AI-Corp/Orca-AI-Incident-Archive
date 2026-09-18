---
id: 2026-06-03-anthropic-llm-att-ck
title: "Anthropic, \"LLM ATT&CK Navigator\""
title_zh: "Anthropic《LLM ATT&CK Navigator》"
title_ja: "Anthropic「LLM ATT&CK Navigator」"
title_ko: "Anthropic, \"LLM ATT&CK Navigator\""
title_de: "Anthropic: „LLM ATT&CK Navigator“"
title_fr: "Anthropic : « LLM ATT&CK Navigator »"
title_es: "Anthropic, \"LLM ATT&CK Navigator\""
date: 2026-06-03
date_precision: day
date_raw: "2026-06-03"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Examines **832 abuse accounts** from 2025-03 → 2026-03. Key finding: attackers' use of AI shifted from the "preparation phase" (writing malware) toward the **"post-compromise phase"** (lateral movement, credential theft); the share of medium-to-high-risk actors rose from **33% to 56%** within a year, driven mainly by agents chaining attack stages autonomously. Conclusion: MITRE ATT&CK cannot capture these autonomous behaviors, and risk assessment needs to move from "number of skills / techniques" to **"orchestration capability"**


summary_zh: |
  分析 2025-03 → 2026-03 的 **832 个滥用账号**。关键发现：攻击者用 AI 的重心从「准备阶段」（写恶意软件）转向**「入侵后阶段」**（横移、窃凭据）；中高风险行为者占比一年内从 **33% 升到 56%**，主因是 agent 对攻击阶段的自主串联。结论：MITRE ATT&CK 捕捉不了这些自主行为，风险评估需从「技能/手法数量」转向**「编排能力」**

summary_ja: |
  2025-03 → 2026-03の**832の悪用アカウント**を調査。重要な発見：攻撃者のAI利用は「準備段階」（マルウェア作成）から**「侵害後段階」**（横展開、認証情報窃取）へ移行し、中〜高リスクのアクターの割合は1年で**33%から56%**に上昇、主因はエージェントが攻撃段階を自律的に連鎖させること。結論：MITRE ATT&CKはこれらの自律的行動を捉えられず、リスク評価は「スキル／技術の数」から**「オーケストレーション能力」**へ移る必要がある

summary_ko: |
  2025-03 → 2026-03 기간의 **악용 계정 832개**를 분석했다. 핵심 발견: 공격자의 AI 활용이 "준비 단계"(악성코드 작성)에서 **"침해 이후 단계"**(측면 이동, 자격 증명 탈취)로 이동했고, 중·고위험 행위자의 비중이 1년 만에 **33%에서 56%로** 상승했으며 주된 요인은 에이전트가 공격 단계를 자율적으로 연쇄하는 것이다. 결론: MITRE ATT&CK은 이런 자율 행동을 포착하지 못하며, 위험 평가는 "기술/기법의 개수"에서 **"오케스트레이션 능력"**으로 옮겨가야 한다

summary_de: |
  Untersucht **832 Missbrauchskonten** von 2025-03 → 2026-03. Zentrales Ergebnis: Die Nutzung von KI durch Angreifer verlagerte sich von der „Vorbereitungsphase“ (Schreiben von Malware) zur **„Post-Compromise-Phase“** (laterale Bewegung, Zugangsdatendiebstahl); der Anteil mittel- bis hochriskanten Akteure stieg innerhalb eines Jahres von **33% auf 56%**, vor allem getrieben durch Agenten, die Angriffsphasen autonom verketten. Fazit: MITRE ATT&CK kann diese autonomen Verhaltensweisen nicht erfassen, und die Risikobewertung muss von der „Anzahl der Fähigkeiten / Techniken“ zur **„Orchestrierungsfähigkeit“** übergehen

summary_fr: |
  Examine **832 comptes abusifs** de 2025-03 → 2026-03. Constat clé : l'usage de l'IA par les attaquants est passé de la « phase de préparation » (écrire des malwares) vers la **« phase post-compromission »** (mouvement latéral, vol d'identifiants) ; la part d'acteurs à risque moyen à élevé est passée de **33 % à 56 %** en un an, principalement parce que les agents enchaînent les étapes d'attaque de façon autonome. Conclusion : MITRE ATT&CK ne peut pas capturer ces comportements autonomes, et l'évaluation des risques doit passer du « nombre de compétences / techniques » à la **« capacité d'orchestration »**

summary_es: |
  Examina **832 cuentas de abuso** de 2025-03 → 2026-03. Hallazgo clave: el uso de la IA por parte de los atacantes pasó de la "fase de preparación" (escribir malware) hacia la **"fase posterior al compromiso"** (movimiento lateral, robo de credenciales); la proporción de actores de riesgo medio-alto subió del **33% al 56%** en un año, impulsada principalmente por agentes que encadenan etapas de ataque de forma autónoma. Conclusión: MITRE ATT&CK no puede capturar estos comportamientos autónomos, y la evaluación de riesgos debe pasar del "número de habilidades / técnicas" a la **"capacidad de orquestación"**

sources:
  - url: https://red.anthropic.com/2026/attack-navigator/
    label: red.anthropic.com
  - url: https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack
    label: Anthropic

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Anthropic, "LLM ATT&CK Navigator"

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Examines **832 abuse accounts** from 2025-03 → 2026-03. Key finding: attackers' use of AI shifted from the "preparation phase" (writing malware) toward the **"post-compromise phase"** (lateral movement, credential theft); the share of medium-to-high-risk actors rose from **33% to 56%** within a year, driven mainly by agents chaining attack stages autonomously. Conclusion: MITRE ATT&CK cannot capture these autonomous behaviors, and risk assessment needs to move from "number of skills / techniques" to **"orchestration capability"**

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
| 1 | red.anthropic.com | <https://red.anthropic.com/2026/attack-navigator/> |
| 2 | Anthropic | <https://www.anthropic.com/news/AI-enabled-cyber-threats-mitre-attack> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-03` (raw: 2026-06-03, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-03-anthropic-llm-att-ck` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-06-15` [UNC6508 breaches North American research institutions via REDCap](2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab adaptive AI worm PoC](2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight: malware prompt-injects the AI analyst](2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-09` [Anthropic: N-day is really "N-hour"](2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-03-anthropic-llm-att-ck.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
