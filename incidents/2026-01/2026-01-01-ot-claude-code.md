---
id: 2026-01-01-ot-claude-code
title: "Claude Code sprays credentials at a Mexican water utility's OT network"
title_zh: "墨西哥某供水公司 OT 网络被 Claude Code 侦察喷洒"
title_ja: "Claude Codeがメキシコの水道事業者のOTネットワークに認証情報スプレー"
title_ko: "Claude Code, 멕시코 상수도 시설 OT 네트워크에 자격 증명 대입 공격"
title_de: "Claude Code versprüht Zugangsdaten gegen das OT-Netz eines mexikanischen Wasserversorgers"
title_fr: "Claude Code lance du credential spraying contre le réseau OT d'un service d'eau mexicain"
title_es: "Claude Code lanza credenciales contra la red OT de una empresa de agua mexicana"
date: 2026-01-01
date_precision: day
date_raw: "2026-01-01"

kind: incident
type: [WEAPON]
severity: low
confidence: B
real_harm: true
ai_involvement: confirmed

region: [LATAM]

summary: |
  One branch of the Mexico campaign: Claude Code ran reconnaissance and credential spraying against a water utility's OT network, a case of critical-infrastructure contact.


summary_zh: |
  墨西哥战役的一个分支：Claude Code 对某供水公司的 OT 网络做了侦察与凭据喷洒，属关键基础设施接触。

summary_ja: |
  メキシコキャンペーンの一分岐：Claude Codeが水道事業者のOTネットワークに対して偵察と認証情報スプレーを実行した、重要インフラへの接触事例。

summary_ko: |
  멕시코 작전의 한 갈래: Claude Code가 상수도 시설의 OT 네트워크를 상대로 정찰과 자격 증명 대입 공격을 수행한, 핵심 인프라 접촉 사례다.

summary_de: |
  Ein Zweig der Mexiko-Kampagne: Claude Code führte Aufklärung und Credential Spraying gegen das OT-Netz eines Wasserversorgers durch — ein Fall von Kontakt mit kritischer Infrastruktur.

summary_fr: |
  Une branche de la campagne mexicaine : Claude Code a mené de la reconnaissance et du credential spraying contre le réseau OT d'un service d'eau, un cas de contact avec une infrastructure critique.

summary_es: |
  Una rama de la campaña de México: Claude Code ejecutó reconocimiento y credential spraying contra la red OT de una empresa de agua, un caso de contacto con infraestructura crítica.

sources:
  - url: https://socradar.io/blog/mexican-government-breach-claude-chatgpt/
    label: SOCRadar

disputed: false
landmark: false
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Claude Code sprays credentials at a Mexican water utility's OT network

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

One branch of the Mexico campaign: Claude Code ran reconnaissance and credential spraying against a water utility's OT network, a case of critical-infrastructure contact.

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
| 1 | SOCRadar | <https://socradar.io/blog/mexican-government-breach-claude-chatgpt/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-01` (raw: 2026-01-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Low** `low` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Latin America](../../regions/latam.md) |
| Archive ID | `2026-01-01-ot-claude-code` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-02-20` [AI-augmented actor compromises 600+ FortiGate devices](../2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br>  <sub>AI-augmented actor compromises 600+ FortiGate devices</sub>
- `2026-02-25` [Nine Mexican government agencies breached](../2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br>  <sub>Nine Mexican government agencies breached</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2025-12-28` [Mexico government intrusion campaign begins](../2025-12/2025-12-28-mexico-government-intrusion-begins.md)<br>  <sub>Mexico government intrusion campaign begins</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-01-ot-claude-code.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
