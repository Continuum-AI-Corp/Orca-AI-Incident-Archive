---
id: 2025-12-28-mexico-government-intrusion-begins
title: "Mexico government intrusion campaign begins"
title_zh: "墨西哥政府入侵行动启动"
title_ja: "メキシコ政府への侵入キャンペーンが始まる"
title_ko: "멕시코 정부 침입 작전 시작"
title_de: "Beginn der Intrusionskampagne gegen die mexikanische Regierung"
title_fr: "Début de la campagne d'intrusion contre le gouvernement mexicain"
title_es: "Comienza la campaña de intrusión al gobierno de México"
date: 2025-12-28
date_precision: part
date_raw: "late 2025-12"

kind: incident
type: [WEAPON]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [LATAM]

summary: |
  The starting point of the Mexico government intrusion campaign — the attacker begins using Claude Code for sustained reconnaissance against government network ranges; the full campaign was only reconstructed in 2026-02.


summary_zh: |
  墨西哥政府入侵战役的起点——攻击者开始用 Claude Code 对政府网段做持续侦察，整条战役到 2026-02 才被完整还原。

summary_ja: |
  メキシコ政府侵入キャンペーンの起点——攻撃者が政府のネットワークレンジに対する持続的偵察にClaude Codeを使い始める。キャンペーン全体が再構成されたのは2026-02になってからである。

summary_ko: |
  멕시코 정부 침입 작전의 출발점 — 공격자가 정부 네트워크 대역을 대상으로 Claude Code를 이용한 지속적 정찰을 시작했다. 전체 작전은 2026-02에야 재구성되었다.

summary_de: |
  Der Ausgangspunkt der Intrusionskampagne gegen die mexikanische Regierung — der Angreifer beginnt, Claude Code für anhaltende Aufklärung gegen Regierungsnetzbereiche einzusetzen; die vollständige Kampagne wurde erst im 2026-02 rekonstruiert.

summary_fr: |
  Le point de départ de la campagne d'intrusion contre le gouvernement mexicain — l'attaquant commence à utiliser Claude Code pour de la reconnaissance prolongée contre des plages réseau gouvernementales ; la campagne complète n'a été reconstituée qu'en 2026-02.

summary_es: |
  El punto de partida de la campaña de intrusión al gobierno de México — el atacante empieza a usar Claude Code para reconocimiento sostenido contra rangos de red gubernamentales; la campaña completa solo se reconstruyó en 2026-02.

sources:
  - url: https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data
    label: Bloomberg

disputed: false
landmark: true
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# Mexico government intrusion campaign begins

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

The starting point of the Mexico government intrusion campaign — the attacker begins using Claude Code for sustained reconnaissance against government network ranges; the full campaign was only reconstructed in 2026-02.

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
| 1 | Bloomberg | <https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-28` (raw: late 2025-12, precision `part`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Latin America](../../regions/latam.md) |
| Archive ID | `2025-12-28-mexico-government-intrusion-begins` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-11-13` [GTG-1002: first AI-orchestrated cyber-espionage campaign](../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-11-03` [SesameOp](../2025-11/2025-11-03-sesameop.md)<br>  <sub>SesameOp</sub>
- `2025-11-05` [GTIG: PROMPTFLUX / PROMPTSTEAL](../2025-11/2025-11-05-gtig-promptflux-promptsteal.md)<br>  <sub>GTIG: PROMPTFLUX / PROMPTSTEAL</sub>
- `2026-01-01` [Claude Code sprays credentials at a Mexican water utility's OT network](../2026-01/2026-01-01-ot-claude-code.md)<br>  <sub>Claude Code sprays credentials at a Mexican water utility's OT network</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-28-mexico-government-intrusion-begins.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
