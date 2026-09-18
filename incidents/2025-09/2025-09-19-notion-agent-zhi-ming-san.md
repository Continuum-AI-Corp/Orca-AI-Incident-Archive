---
id: 2025-09-19-notion-agent-zhi-ming-san
title: "Notion 3.0 agent hits the lethal trifecta"
title_zh: "Notion 3.0 agent「致命三元组」"
title_ja: "Notion 3.0エージェントがlethal trifectaに該当"
title_ko: "Notion 3.0 에이전트, 치명적 삼중주에 빠지다"
title_de: "Notion-3.0-Agent trifft die lethal trifecta"
title_fr: "L'agent de Notion 3.0 tombe dans la lethal trifecta"
title_es: "El agente de Notion 3.0 topa con la trifecta letal"
date: 2025-09-19
date_precision: day
date_raw: "2025-09-19"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CodeIntegrity: a PDF disguised as a customer-feedback report contained hidden white-on-white prompts that induced the agent to use the **URL parameter capability** of `functions.search()` (the tool accepts both search terms and URLs) to exfiltrate private Notion pages. **Any user tricked into "summarizing a seemingly harmless PDF" became a leak channel for the whole team's private data**


summary_zh: |
  CodeIntegrity：伪装成客户反馈报告的 PDF，内含白底白字的隐藏提示，诱导 agent 用 `functions.search()` 的 **URL 参数能力**（该工具同时支持搜索词和 URL）把私有 Notion 页面外带。**任何被骗去「总结一份看起来无害的 PDF」的用户，都成了整个团队私有数据的泄露通道**

summary_ja: |
  CodeIntegrity：顧客フィードバック報告書を装ったPDFに、白地に白の隠しプロンプトが含まれており、エージェントに`functions.search()`の**URLパラメータ機能**（このツールは検索語とURLの両方を受け付ける）を使わせて非公開のNotionページを外部送信させた。**「一見無害なPDFを要約させる」よう仕向けられたユーザーは誰でも、チーム全体の非公開データの漏えい経路となってしまう**

summary_ko: |
  CodeIntegrity: 고객 피드백 보고서로 위장한 PDF에 흰 배경에 흰 글씨로 숨겨진 프롬프트가 있어, 에이전트가 `functions.search()`의 **URL 매개변수 기능**(이 도구는 검색어와 URL을 모두 받는다)을 이용해 비공개 Notion 페이지를 유출하게 만들었다. **"무해해 보이는 PDF를 요약"하도록 속은 사용자는 누구든 팀 전체 비공개 데이터의 유출 통로가 되었다**

summary_de: |
  CodeIntegrity: Ein als Kundenfeedback-Bericht getarntes PDF enthielt versteckte weiß-auf-weiß geschriebene Prompts, die den Agenten dazu brachten, die **URL-Parameter-Funktion** von `functions.search()` zu nutzen (das Tool akzeptiert sowohl Suchbegriffe als auch URLs), um private Notion-Seiten zu exfiltrieren. **Jeder Nutzer, der dazu gebracht wurde, „ein scheinbar harmloses PDF zusammenzufassen“, wurde zum Leckkanal für die privaten Daten des gesamten Teams**

summary_fr: |
  CodeIntegrity : un PDF déguisé en rapport de retours clients contenait des prompts cachés en blanc sur blanc qui ont amené l'agent à utiliser la **capacité de paramètre d'URL** de `functions.search()` (l'outil accepte à la fois des termes de recherche et des URL) pour exfiltrer des pages Notion privées. **Tout utilisateur amené à « résumer un PDF apparemment inoffensif » devenait un canal de fuite pour les données privées de toute l'équipe**

summary_es: |
  CodeIntegrity: un PDF disfrazado de informe de comentarios de clientes contenía prompts ocultos en blanco sobre blanco que indujeron al agente a usar la **capacidad de parámetro URL** de `functions.search()` (la herramienta acepta tanto términos de búsqueda como URL) para exfiltrar páginas privadas de Notion. **Cualquier usuario engañado para "resumir un PDF aparentemente inofensivo" se convertía en un canal de fuga de los datos privados de todo el equipo**

sources:
  - url: https://www.codeintegrity.ai/blog/notion
    label: CodeIntegrity
  - url: https://simonwillison.net/2025/Sep/19/notion-lethal-trifecta/
    label: Simon Willison
  - url: https://www.schneier.com/blog/archives/2025/09/abusing-notions-ai-agent-for-data-theft.html
    label: Schneier

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# Notion 3.0 agent hits the lethal trifecta

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

CodeIntegrity: a PDF disguised as a customer-feedback report contained hidden white-on-white prompts that induced the agent to use the **URL parameter capability** of `functions.search()` (the tool accepts both search terms and URLs) to exfiltrate private Notion pages. **Any user tricked into "summarizing a seemingly harmless PDF" became a leak channel for the whole team's private data**

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
| 1 | CodeIntegrity | <https://www.codeintegrity.ai/blog/notion> |
| 2 | Simon Willison | <https://simonwillison.net/2025/Sep/19/notion-lethal-trifecta/> |
| 3 | Schneier | <https://www.schneier.com/blog/archives/2025/09/abusing-notions-ai-agent-for-data-theft.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-19` (raw: 2025-09-19, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-19-notion-agent-zhi-ming-san` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-09-18` [ShadowLeak](2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-25` [ForcedLeak (Salesforce Agentforce)](2025-09-25-forcedleak-salesforce-agentforce.md)<br>  <sub>ForcedLeak (Salesforce Agentforce)</sub>
- `2025-09-30` [Gemini "Trifecta"](2025-09-30-gemini-trifecta.md)<br>  <sub>Gemini "Trifecta"</sub>
- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-19-notion-agent-zhi-ming-san.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
