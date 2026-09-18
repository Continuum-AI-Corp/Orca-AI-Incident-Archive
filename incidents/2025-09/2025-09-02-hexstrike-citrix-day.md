---
id: 2025-09-02-hexstrike-citrix-day
title: "HexStrike-AI turned on a Citrix zero-day"
title_zh: "HexStrike-AI 被威胁方用于打 Citrix 0-day"
title_ja: "HexStrike-AIがCitrixのゼロデイを起動"
title_ko: "HexStrike-AI, Citrix 제로데이를 켜다"
title_de: "HexStrike-AI nutzte einen Citrix-Zero-Day"
title_fr: "HexStrike-AI exploite un zero-day Citrix"
title_es: "HexStrike-AI activó un zero-day de Citrix"
date: 2025-09-02
date_precision: day
date_raw: "2025-09-02"

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Check Point: within hours of the open-source AI attack framework's release, dark-web discussions appeared about using it to mass-exploit NetScaler vulnerabilities (including the zero-day **CVE-2025-7775**). **150 autonomous agents finished the exploitation within 10 minutes**, and some immediately resold the compromised devices


summary_zh: |
  Check Point：开源 AI 攻防框架发布后数小时，暗网即出现用其批量利用 NetScaler 漏洞（含零日 **CVE-2025-7775**）的讨论。**150 个自主 agent，10 分钟内完成利用**，并有人立即倒卖已控设备

summary_ja: |
  Check Point：オープンソースのAI攻撃フレームワークの公開から数時間以内に、NetScalerの脆弱性（ゼロデイ**CVE-2025-7775**を含む）を大量悪用するためのダークウェブ上の議論が現れた。**150の自律エージェントが10分以内に悪用を完了**し、一部は侵害したデバイスを即座に転売した

summary_ko: |
  Check Point: 오픈소스 AI 공격 프레임워크가 공개된 지 몇 시간 만에 이를 이용해 NetScaler 취약점(제로데이 **CVE-2025-7775** 포함)을 대량 악용하자는 다크웹 논의가 나타났다. **자율 에이전트 150개가 10분 안에 익스플로잇을 끝냈고**, 일부는 침해된 기기를 즉시 재판매했다

summary_de: |
  Check Point: Innerhalb von Stunden nach der Veröffentlichung des Open-Source-KI-Angriffsframeworks gab es Darknet-Diskussionen darüber, es zum massenhaften Ausnutzen von NetScaler-Schwachstellen einzusetzen (einschließlich des Zero-Day **CVE-2025-7775**). **150 autonome Agenten schlossen die Ausnutzung innerhalb von 10 Minuten ab**, und einige verkauften die kompromittierten Geräte sofort weiter

summary_fr: |
  Check Point : quelques heures après la sortie du framework d'attaque IA open source, des discussions sur le dark web sont apparues autour de son utilisation pour exploiter massivement des vulnérabilités NetScaler (dont le zero-day **CVE-2025-7775**). **150 agents autonomes ont terminé l'exploitation en 10 minutes**, et certains ont immédiatement revendu les appareils compromis

summary_es: |
  Check Point: a las pocas horas del lanzamiento del marco de ataque con IA de código abierto, aparecieron debates en la dark web sobre usarlo para explotar masivamente vulnerabilidades de NetScaler (incluido el zero-day **CVE-2025-7775**). **150 agentes autónomos completaron la explotación en 10 minutos**, y algunos revendieron de inmediato los dispositivos comprometidos

sources:
  - url: https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/
    label: Check Point
  - url: https://thehackernews.com/2025/09/threat-actors-weaponize-hexstrike-ai-to.html
    label: THN

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# HexStrike-AI turned on a Citrix zero-day

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Check Point: within hours of the open-source AI attack framework's release, dark-web discussions appeared about using it to mass-exploit NetScaler vulnerabilities (including the zero-day **CVE-2025-7775**). **150 autonomous agents finished the exploitation within 10 minutes**, and some immediately resold the compromised devices

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak prompts"]:::entry
    S0["An LLM orchestrator drives a cluster of sub-agents"]:::step
    I["The target system is compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Check Point | <https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/> |
| 2 | THN | <https://thehackernews.com/2025/09/threat-actors-weaponize-hexstrike-ai-to.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-02` (raw: 2025-09-02, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-02-hexstrike-citrix-day` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-09-01` [Villager (Cyberspike) AI pentest tool](2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-09-15` [Anthropic detects GTG-1002](2025-09-15-anthropic-gtg-jian-ce-dao.md)<br>  <sub>Anthropic detects GTG-1002</sub>
- `2025-08-26` [ESET finds PromptLock](../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-08-27` [Anthropic August threat report](../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-02-hexstrike-citrix-day.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
