---
id: 2025-08-01-man-prompt-liu-lan-qi
title: "\"Man in the Prompt\" browser-extension attack"
title_zh: "\"Man in the Prompt\" 浏览器扩展攻击"
title_ja: "「Man in the Prompt」ブラウザ拡張機能攻撃"
title_ko: "\"Man in the Prompt\" 브라우저 확장 공격"
title_de: "Browser-Erweiterungsangriff „Man in the Prompt“"
title_fr: "L'attaque « Man in the Prompt » par extension de navigateur"
title_es: "Ataque de extensión de navegador \"Man in the Prompt\""
date: 2025-08-01
date_precision: month
date_raw: "2025-08"

kind: research
type: [IPI]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  LayerX: a **least-privilege extension** is enough to manipulate the ChatGPT / Gemini prompt box in the browser DOM to inject instructions, hide its traces, and read confidential content including Google Workspace data


summary_zh: |
  LayerX：**最低权限的扩展**即可操纵浏览器 DOM 中 ChatGPT / Gemini 的提示框注入指令、隐藏痕迹、读取包括 Google Workspace 在内的机密内容

summary_ja: |
  LayerX：**最小権限の拡張機能**だけで、ブラウザDOM上のChatGPT／Geminiのプロンプトボックスを操作して指示を注入し、痕跡を隠し、Google Workspaceのデータを含む機密コンテンツを読み取ることができる

summary_ko: |
  LayerX: **최소 권한 확장 프로그램**만으로 브라우저 DOM에서 ChatGPT / Gemini 프롬프트 입력창을 조작해 지시를 주입하고 흔적을 숨기며 Google Workspace 데이터를 포함한 기밀 콘텐츠를 읽을 수 있었다

summary_de: |
  LayerX: Eine **Erweiterung mit minimalen Rechten** genügt, um das Prompt-Feld von ChatGPT / Gemini im Browser-DOM zu manipulieren, Anweisungen einzuschleusen, Spuren zu verwischen und vertrauliche Inhalte einschließlich Google-Workspace-Daten zu lesen

summary_fr: |
  LayerX : une **extension à privilèges minimaux** suffit à manipuler la zone de prompt de ChatGPT / Gemini dans le DOM du navigateur pour injecter des instructions, masquer ses traces et lire du contenu confidentiel, y compris des données Google Workspace

summary_es: |
  LayerX: **una extensión con privilegios mínimos** basta para manipular el cuadro de prompt de ChatGPT / Gemini en el DOM del navegador, inyectar instrucciones, ocultar sus rastros y leer contenido confidencial, incluidos datos de Google Workspace

sources:
  - url: https://techriskguru.com/p/techrisk-133-man-in-the-prompt-attack
    label: LayerX (via TechRisk)

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# "Man in the Prompt" browser-extension attack

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

LayerX: a **least-privilege extension** is enough to manipulate the ChatGPT / Gemini prompt box in the browser DOM to inject instructions, hide its traces, and read confidential content including Google Workspace data

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Takes unauthorized actions as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | LayerX (via TechRisk) | <https://techriskguru.com/p/techrisk-133-man-in-the-prompt-attack> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-01` (raw: 2025-08, precision `month`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-01-man-prompt-liu-lan-qi` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>
- `2025-08-06` [SafeBreach "Invitation Is All You Need"](2025-08-06-safebreach-invitation-is-all.md)<br>  <sub>SafeBreach "Invitation Is All You Need"</sub>
- `2025-09-18` [ShadowLeak](../2025-09/2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](../2025-09/2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-01-man-prompt-liu-lan-qi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
