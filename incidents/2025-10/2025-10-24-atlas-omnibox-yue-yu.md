---
id: 2025-10-24-atlas-omnibox-yue-yu
title: "Atlas omnibox jailbreak"
title_zh: "Atlas omnibox 越狱"
title_ja: "Atlasのオムニボックス・ジェイルブレイク"
title_ko: "Atlas 옴니박스 탈옥"
title_de: "Atlas: Omnibox-Jailbreak"
title_fr: "Jailbreak de l'omnibox d'Atlas"
title_es: "Jailbreak de la omnibox de Atlas"
date: 2025-10-24
date_precision: day
date_raw: "2025-10-24"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  NeuralTrust: input disguised as a URL is executed as a high-trust instruction


summary_zh: |
  NeuralTrust：伪装成 URL 的输入被当成高信任指令执行

summary_ja: |
  NeuralTrust：URLを装った入力が信頼度の高い指示として実行される

summary_ko: |
  NeuralTrust: URL로 위장한 입력이 높은 신뢰도의 지시로 실행된다

summary_de: |
  NeuralTrust: Als URL getarnte Eingaben werden als hoch vertrauenswürdige Anweisung ausgeführt

summary_fr: |
  NeuralTrust : une entrée déguisée en URL est exécutée comme une instruction de haute confiance

summary_es: |
  NeuralTrust: una entrada disfrazada de URL se ejecuta como una instrucción de alta confianza

sources:
  - url: https://neuraltrust.ai/blog/openai-atlas-omnibox-prompt-injection
    label: NeuralTrust

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Atlas omnibox jailbreak

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

NeuralTrust: input disguised as a URL is executed as a high-trust instruction

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | NeuralTrust | <https://neuraltrust.ai/blog/openai-atlas-omnibox-prompt-injection> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-24` (raw: 2025-10-24, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-24-atlas-omnibox-yue-yu` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-24-atlas-omnibox-yue-yu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
