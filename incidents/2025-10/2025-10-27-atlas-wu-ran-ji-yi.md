---
id: 2025-10-27-atlas-wu-ran-ji-yi
title: "Atlas \"poisoned memory\""
title_zh: "Atlas「污染记忆」"
title_ja: "Atlasの「汚染されたメモリ」"
title_ko: "Atlas \"오염된 기억\""
title_de: "Atlas: „vergiftetes Gedächtnis“"
title_fr: "« Mémoire empoisonnée » d'Atlas"
title_es: "\"Memoria envenenada\" en Atlas"
date: 2025-10-27
date_precision: day
date_raw: "2025-10-27"

kind: research
type: [IPI]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  LayerX: via CSRF, malicious instructions are written into ChatGPT's persistent memory and **survive across sessions**


summary_zh: |
  LayerX：经 CSRF 向 ChatGPT 持久记忆写入恶意指令，**跨会话存活**

summary_ja: |
  LayerX：CSRF経由で悪意ある指示がChatGPTの永続メモリに書き込まれ、**セッションをまたいで生き残る**

summary_ko: |
  LayerX: CSRF를 통해 악성 지시가 ChatGPT의 영구 메모리에 기록되어 **세션을 넘어 지속된다**

summary_de: |
  LayerX: Über CSRF werden bösartige Anweisungen in das persistente Gedächtnis von ChatGPT geschrieben und **überleben über Sitzungen hinweg**

summary_fr: |
  LayerX : via CSRF, des instructions malveillantes sont écrites dans la mémoire persistante de ChatGPT et **survivent d'une session à l'autre**

summary_es: |
  LayerX: mediante CSRF, se escriben instrucciones maliciosas en la memoria persistente de ChatGPT y **sobreviven entre sesiones**

sources:
  - url: https://www.wiz.io/blog/agentic-browser-security-2025-year-end-review
    label: Wiz year-end review

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Atlas "poisoned memory"

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

LayerX: via CSRF, malicious instructions are written into ChatGPT's persistent memory and **survive across sessions**

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
| 1 | Wiz year-end review | <https://www.wiz.io/blog/agentic-browser-security-2025-year-end-review> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-27` (raw: 2025-10-27, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-27-atlas-wu-ran-ji-yi` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-27-atlas-wu-ran-ji-yi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
