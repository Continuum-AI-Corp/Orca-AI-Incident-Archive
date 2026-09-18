---
id: 2025-09-15-anthropic-gtg-jian-ce-dao
title: "Anthropic detects GTG-1002"
title_zh: "Anthropic 检测到 GTG-1002"
title_ja: "AnthropicがGTG-1002を検知"
title_ko: "Anthropic, GTG-1002를 탐지"
title_de: "Anthropic entdeckt GTG-1002"
title_fr: "Anthropic détecte GTG-1002"
title_es: "Anthropic detecta GTG-1002"
date: 2025-09-15
date_precision: part
date_raw: "mid 2025-09"

kind: incident
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Anthropic detected the GTG-1002 campaign internally in mid-September, then spent 10 days investigating while banning accounts and notifying victims, and only went public on 11-13.


summary_zh: |
  Anthropic 在 9 月中旬内部检测到 GTG-1002 战役，随后 10 天边调查边封号、通知受害方，直到 11-13 才公开。

summary_ja: |
  Anthropicは9月中旬に社内でGTG-1002キャンペーンを検知し、その後10日間かけて調査しながらアカウント停止と被害者通知を行い、11-13まで公表しなかった。

summary_ko: |
  Anthropic은 9월 중순 내부에서 GTG-1002 작전을 탐지했고, 10일 동안 조사하면서 계정을 정지하고 피해자에게 통보했으며, 11-13에야 공개했다.

summary_de: |
  Anthropic entdeckte die GTG-1002-Kampagne Mitte September intern, verbrachte dann 10 Tage mit Untersuchungen, sperrte Konten und benachrichtigte Opfer und ging erst am 11-13 an die Öffentlichkeit.

summary_fr: |
  Anthropic a détecté la campagne GTG-1002 en interne à la mi-septembre, puis a passé 10 jours à enquêter tout en bannissant des comptes et en notifiant les victimes, et n'a communiqué publiquement que le 11-13.

summary_es: |
  Anthropic detectó internamente la campaña GTG-1002 a mediados de septiembre, luego dedicó 10 días a investigar mientras bloqueaba cuentas y notificaba a las víctimas, y solo lo hizo público el 11-13.

sources:
  - url: https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf
    label: Anthropic PDF

disputed: false
landmark: false
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Anthropic detects GTG-1002

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Anthropic detected the GTG-1002 campaign internally in mid-September, then spent 10 days investigating while banning accounts and notifying victims, and only went public on 11-13.

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
| 1 | Anthropic PDF | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-15` (raw: mid 2025-09, precision `part`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-15-anthropic-gtg-jian-ce-dao` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-09-02` [HexStrike-AI turned on a Citrix zero-day](2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager (Cyberspike) AI pentest tool](2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-08-26` [ESET finds PromptLock](../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-08-27` [Anthropic August threat report](../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
