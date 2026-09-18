---
id: 2025-10-07-shi-wei-xie-bao-gao
title: "OpenAI October threat report"
title_zh: "OpenAI 十月威胁报告"
title_ja: "OpenAIの10月脅威レポート"
title_ko: "OpenAI 10월 위협 보고서"
title_de: "OpenAI-Bedrohungsbericht Oktober"
title_fr: "Rapport de menace d'octobre d'OpenAI"
title_es: "Informe de amenazas de OpenAI de octubre"
date: 2025-10-07
date_precision: day
date_raw: "2025-10-07"

kind: report
type: [WEAPON, GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Has cumulatively disrupted **40+ networks** since 2024-02; discloses a China-government-related social media monitoring proposal and scam networks in Cambodia/Myanmar/Nigeria. Core judgment: **attackers are speeding up old playbooks by plugging in AI, not gaining new attack capabilities**


summary_zh: |
  自 2024-02 起累计瓦解 **40+ 网络**；披露中国政府相关的社媒监控提案、柬埔寨/缅甸/尼日利亚诈骗网络。核心判断：**攻击者是把 AI 接到旧剧本上提速，而不是获得了新的攻击能力**

summary_ja: |
  2024-02以降、累計で**40以上のネットワーク**を妨害。中国政府関連のSNS監視の提案や、カンボジア／ミャンマー／ナイジェリアの詐欺ネットワークを公表。中核的な判断：**攻撃者はAIを組み込んで従来の手口を高速化しているのであり、新たな攻撃能力を得ているわけではない**

summary_ko: |
  2024-02 이후 누적 **40개 이상의 네트워크**를 차단했다. 중국 정부 관련 소셜 미디어 감시 제안과 캄보디아/미얀마/나이지리아의 사기 네트워크도 공개했다. 핵심 판단: **공격자들은 AI를 끼워 넣어 기존 공격 방식을 가속하고 있을 뿐, 새로운 공격 능력을 얻은 것은 아니다**

summary_de: |
  Hat seit 2024-02 kumulativ **40+ Netzwerke** gestört; legt einen Vorschlag zur Social-Media-Überwachung mit Verbindung zur chinesischen Regierung offen sowie Betrugsnetzwerke in Kambodscha/Myanmar/Nigeria. Kernurteil: **Angreifer beschleunigen alte Vorgehensweisen durch den Einsatz von KI, gewinnen aber keine neuen Angriffsfähigkeiten**

summary_fr: |
  A perturbé cumulativement **plus de 40 réseaux** depuis 2024-02 ; divulgue une proposition de surveillance des réseaux sociaux liée au gouvernement chinois et des réseaux d'arnaque au Cambodge/Myanmar/Nigeria. Jugement central : **les attaquants accélèrent d'anciens modes opératoires en y branchant de l'IA, sans acquérir de nouvelles capacités d'attaque**

summary_es: |
  Ha perturbado acumulativamente **más de 40 redes** desde 2024-02; divulga una propuesta de monitoreo de redes sociales vinculada al gobierno chino y redes de estafa en Camboya/Myanmar/Nigeria. Juicio central: **los atacantes están acelerando manuales antiguos conectando IA, no obteniendo nuevas capacidades de ataque**

sources:
  - url: https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/
    label: OpenAI
  - url: https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf
    label: PDF

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# OpenAI October threat report

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Has cumulatively disrupted **40+ networks** since 2024-02; discloses a China-government-related social media monitoring proposal and scam networks in Cambodia/Myanmar/Nigeria. Core judgment: **attackers are speeding up old playbooks by plugging in AI, not gaining new attack capabilities**

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    S1["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenAI | <https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/> |
| 2 | PDF | <https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-07` (raw: 2025-10-07, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon · [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-07-shi-wei-xie-bao-gao` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md) · [Defense & governance](../../topics/defense.md)

**Related records:**

- `2025-10-21` [OpenAI launches the Atlas browser](2025-10-21-atlas-liu-lan-qi-fa.md)<br>  <sub>OpenAI launches the Atlas browser</sub>
- `2025-11-13` [GTG-1002: first AI-orchestrated cyber-espionage campaign](../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-09-02` [HexStrike-AI turned on a Citrix zero-day](../2025-09/2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager (Cyberspike) AI pentest tool](../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-07-shi-wei-xie-bao-gao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
