---
id: 2026-05-22-google-disregard-bug
title: "Google AI Search \"disregard\" bug"
title_zh: "Google AI 搜索「disregard」bug"
title_ja: "Google AI検索の「disregard」バグ"
title_ko: "구글 AI 검색 \"disregard\" 버그"
title_de: "Google AI Search: der „Disregard“-Bug"
title_fr: "Le bug « disregard » de Google AI Search"
title_es: "El fallo \"disregard\" de la Búsqueda con IA de Google"
date: 2026-05-22
date_precision: day
date_raw: "2026-05-22"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Searching for "disregard"/"ignore"/"skip" made Gemini treat user input as system instructions. It is a functional defect rather than malicious exploitation, but it exposed **the structural risk of putting an LLM in a search box without separating instructions from data**


summary_zh: |
  搜 "disregard"/"ignore"/"skip" 时 Gemini 把用户输入当成系统指令。虽属功能性缺陷非恶意利用，但暴露了**把 LLM 塞进搜索框而不做指令/数据分离的结构性风险**

summary_ja: |
  「disregard」「ignore」「skip」を検索すると、Geminiがユーザー入力をシステム指示として扱った。悪意ある悪用ではなく機能上の欠陥だが、**指示とデータを分離せずにLLMを検索ボックスに置くことの構造的リスク**を露呈した

summary_ko: |
  "disregard"/"ignore"/"skip"을 검색하면 Gemini가 사용자 입력을 시스템 지시로 취급했다. 악의적 악용이 아닌 기능 결함이지만, **지시와 데이터를 분리하지 않고 LLM을 검색창에 넣는 구조적 위험**을 드러냈다

summary_de: |
  Die Suche nach „disregard“/„ignore“/„skip“ brachte Gemini dazu, Nutzereingaben als Systemanweisungen zu behandeln. Es ist ein funktionaler Defekt und keine bösartige Ausnutzung, doch er legte **das strukturelle Risiko offen, ein LLM ohne Trennung von Anweisungen und Daten in ein Suchfeld zu setzen**

summary_fr: |
  Chercher « disregard »/« ignore »/« skip » faisait que Gemini traitait l'entrée utilisateur comme des instructions système. C'est un défaut fonctionnel plutôt qu'une exploitation malveillante, mais il a exposé **le risque structurel de mettre un LLM dans une zone de recherche sans séparer les instructions des données**

summary_es: |
  Buscar "disregard"/"ignore"/"skip" hacía que Gemini tratara la entrada del usuario como instrucciones de sistema. Es un defecto funcional y no una explotación maliciosa, pero expuso **el riesgo estructural de poner un LLM en un cuadro de búsqueda sin separar las instrucciones de los datos**

sources:
  - url: https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard
    label: The Verge
  - url: https://www.macrumors.com/2026/05/22/google-search-disregard/
    label: MacRumors

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Google AI Search "disregard" bug

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Searching for "disregard"/"ignore"/"skip" made Gemini treat user input as system instructions. It is a functional defect rather than malicious exploitation, but it exposed **the structural risk of putting an LLM in a search box without separating instructions from data**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Unauthorized actions serving the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | The Verge | <https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard> |
| 2 | MacRumors | <https://www.macrumors.com/2026/05/22/google-search-disregard/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-22` (raw: 2026-05-22, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-22-google-disregard-bug` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-05-04` [Grok / Bankrbot Morse-code prompt injection](2026-05-04-grok-bankrbot-mo-er-si.md)<br>  <sub>Grok / Bankrbot Morse-code prompt injection</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-26` [Microsoft Copilot Cowork file exfiltration](2026-05-26-microsoft-copilot-cowork.md)<br>  <sub>Microsoft Copilot Cowork file exfiltration</sub>
- `2026-05-12` [ClaudeBleed: a zero-permission extension hijacks Claude for Chrome](2026-05-12-claudebleed-claude-chrome.md)<br>  <sub>ClaudeBleed: a zero-permission extension hijacks Claude for Chrome</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-22-google-disregard-bug.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
