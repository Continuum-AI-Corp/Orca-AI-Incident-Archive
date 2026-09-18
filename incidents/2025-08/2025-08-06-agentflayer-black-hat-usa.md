---
id: 2025-08-06-agentflayer-black-hat-usa
title: "AgentFlayer zero-click attack set (Black Hat USA)"
title_zh: "AgentFlayer 零点击攻击集（Black Hat USA）"
title_ja: "AgentFlayerのゼロクリック攻撃群（Black Hat USA）"
title_ko: "AgentFlayer 제로클릭 공격 세트(Black Hat USA)"
title_de: "AgentFlayer: Zero-Click-Angriffsset (Black Hat USA)"
title_fr: "Série d'attaques zero-click AgentFlayer (Black Hat USA)"
title_es: "Conjunto de ataques zero-click AgentFlayer (Black Hat USA)"
date: 2025-08-06
date_precision: day
date_raw: "2025-08-06"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Zenity Labs (Tamir Ishay Sharbat) broke through **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira and Gemini** in one sweep. Typical technique: share a document containing about 300 words of 1px white text; the user says "summarize this", and the agent goes off to search Google Drive / SharePoint for API keys and exfiltrates them to the attacker's Azure Blob through an image-rendering URL


summary_zh: |
  Zenity Labs（Tamir Ishay Sharbat）一次性打穿 **ChatGPT Connectors、Copilot Studio、Salesforce Einstein、Cursor+Jira、Gemini**。典型手法：共享一个含约 300 词 1px 白字的文档，用户说一句「总结一下」，agent 就去 Google Drive / SharePoint 搜 API key 并经图片渲染 URL 外带到攻击者 Azure Blob

summary_ja: |
  Zenity Labs（Tamir Ishay Sharbat氏）が**ChatGPT Connectors、Copilot Studio、Salesforce Einstein、Cursor＋Jira、Gemini**を一挙に突破した。典型的な手法：約300語の1px白文字を含む文書を共有し、ユーザーが「これを要約して」と言うと、エージェントがGoogle Drive／SharePointを検索してAPIキーを探し、画像レンダリングURL経由で攻撃者のAzure Blobへ外部送信する

summary_ko: |
  Zenity Labs(Tamir Ishay Sharbat)는 **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira, Gemini**를 한 번에 뚫었다. 대표 기법: 약 300단어 분량의 1px 흰색 텍스트가 담긴 문서를 공유하고 사용자가 "이거 요약해줘"라고 말하면, 에이전트가 Google Drive / SharePoint에서 API 키를 찾아 이미지 렌더링 URL을 통해 공격자의 Azure Blob으로 유출한다

summary_de: |
  Zenity Labs (Tamir Ishay Sharbat) durchbrach in einem Zug **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira und Gemini**. Typische Technik: ein geteiltes Dokument mit etwa 300 Wörtern in 1px weißem Text; der Nutzer sagt „fasse das zusammen“, und der Agent macht sich auf, Google Drive / SharePoint nach API-Schlüsseln zu durchsuchen, und exfiltriert sie über eine Bild-Rendering-URL zum Azure Blob des Angreifers

summary_fr: |
  Zenity Labs (Tamir Ishay Sharbat) a franchi les défenses de **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira et Gemini** d'un seul coup. Technique typique : partager un document contenant environ 300 mots en texte blanc de 1 px ; l'utilisateur dit « résume ceci », et l'agent part chercher des clés API dans Google Drive / SharePoint et les exfiltre vers l'Azure Blob de l'attaquant via une URL de rendu d'image

summary_es: |
  Zenity Labs (Tamir Ishay Sharbat) burló de una sola vez **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira y Gemini**. Técnica típica: compartir un documento con unas 300 palabras de texto blanco de 1px; el usuario dice "resume esto" y el agente va a buscar claves de API en Google Drive / SharePoint y las exfiltra al Azure Blob del atacante mediante una URL de renderizado de imágenes

sources:
  - url: https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41
    label: Zenity Labs
  - url: https://hackread.com/agentflayer-0-click-exploit-chatgpt-connectors-steal-data/
    label: HackRead

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# AgentFlayer zero-click attack set (Black Hat USA)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Zenity Labs (Tamir Ishay Sharbat) broke through **ChatGPT Connectors, Copilot Studio, Salesforce Einstein, Cursor+Jira and Gemini** in one sweep. Typical technique: share a document containing about 300 words of 1px white text; the user says "summarize this", and the agent goes off to search Google Drive / SharePoint for API keys and exfiltrates them to the attacker's Azure Blob through an image-rendering URL

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Zenity Labs | <https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41> |
| 2 | HackRead | <https://hackread.com/agentflayer-0-click-exploit-chatgpt-connectors-steal-data/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-06` (raw: 2025-08-06, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-06-agentflayer-black-hat-usa` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-08-06` [SafeBreach "Invitation Is All You Need"](2025-08-06-safebreach-invitation-is-all.md)<br>  <sub>SafeBreach "Invitation Is All You Need"</sub>
- `2025-08-01` ["Man in the Prompt" browser-extension attack](2025-08-01-man-prompt-liu-lan-qi.md)<br>  <sub>"Man in the Prompt" browser-extension attack</sub>
- `2025-09-18` [ShadowLeak](../2025-09/2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](../2025-09/2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-06-agentflayer-black-hat-usa.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
