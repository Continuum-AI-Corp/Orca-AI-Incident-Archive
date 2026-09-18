---
id: 2025-06-01-anthropic-gtg-ji-lu-shen
title: "Anthropic logs the precursor to GTG-1002"
title_zh: "Anthropic 记录 GTG-1002 前身活动"
title_ja: "AnthropicがGTG-1002の前兆を記録"
title_ko: "Anthropic, GTG-1002의 전조를 기록"
title_de: "Anthropic verzeichnet den Vorläufer von GTG-1002"
title_fr: "Anthropic consigne le précurseur de GTG-1002"
title_es: "Anthropic registra el precursor de GTG-1002"
date: 2025-06-01
date_precision: month
date_raw: "2025-06"

kind: incident
type: [WEAPON]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  "Vibe hacking": the attacker got in through a compromised VPN, with a human still in the loop


summary_zh: |
  「vibe hacking」：攻击者用受损 VPN 入场，人仍在回路

summary_ja: |
  「Vibe hacking」：攻撃者は侵害されたVPNから侵入し、この時点ではまだ人間が介在していた

summary_ko: |
  "바이브 해킹": 공격자는 침해된 VPN을 통해 침입했으며 아직 사람이 개입하고 있었다

summary_de: |
  „Vibe Hacking“: Der Angreifer gelangte über ein kompromittiertes VPN hinein, ein Mensch war noch im Loop

summary_fr: |
  « Vibe hacking » : l'attaquant est entré via un VPN compromis, avec un humain encore dans la boucle

summary_es: |
  "Vibe hacking": el atacante entró mediante una VPN comprometida, todavía con un humano en el circuito

sources:
  - url: https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf
    label: "Anthropic GTG-1002 report"

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Anthropic logs the precursor to GTG-1002

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

"Vibe hacking": the attacker got in through a compromised VPN, with a human still in the loop

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
| 1 | Anthropic GTG-1002 report | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-01` (raw: 2025-06, precision `month`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-01-anthropic-gtg-ji-lu-shen` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-06-01` [Check Point's "Skynet" sample](2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-05` [OpenAI June threat report](2025-06-05-liu-wei-xie-bao-gao.md)<br>  <sub>OpenAI June threat report</sub>
- `2025-05-01` [Anthropic logs the start of GTG-2002 activity](../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI-driven credential stuffing and scanning goes to scale](../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
