---
id: 2025-10-31-agent-session-smuggling-a2a
title: "Agent Session Smuggling: agents deceiving agents over A2A"
title_zh: "Agent Session Smuggling：A2A 协议上的 agent 互骗"
title_ja: "Agent Session Smuggling：A2Aでエージェントがエージェントを欺く"
title_ko: "Agent Session Smuggling: A2A에서 에이전트가 에이전트를 속이다"
title_de: "Agent Session Smuggling: Agenten täuschen Agenten über A2A"
title_fr: "Agent Session Smuggling : des agents trompent d'autres agents via A2A"
title_es: "Agent Session Smuggling: agentes que engañan a agentes a través de A2A"
date: 2025-10-31
date_precision: day
date_raw: "2025-10-31"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Unit 42: a malicious AI agent uses an **already-established cross-agent session** to deliver covert instructions to a victim agent. The attack surface comes from the **stateful design of the A2A protocol** — agents remember recent interactions to keep a coherent conversation, so malicious instructions hide among a string of seemingly normal client requests and server responses. PoC: a rogue research-assistant agent, through a finance-assistant agent, **extracts confidential information and executes unauthorized stock trades**


summary_zh: |
  Unit 42：恶意 AI agent 利用**已建立的跨 agent 会话**向受害 agent 投送隐蔽指令。攻击面来自 **A2A 协议的有状态设计** —— agent 会记住近期交互以维持连贯对话，恶意指令就藏在一连串看似正常的客户端请求与服务端响应之间。PoC：一个流氓研究助理 agent 通过金融助理 agent **提取机密信息并执行未授权股票交易**

summary_ja: |
  Unit 42：悪性AIエージェントが**すでに確立されたエージェント間セッション**を利用して、被害エージェントに隠れた指示を届ける。攻撃面は**A2Aプロトコルのステートフルな設計**に由来する——エージェントは一貫した会話を保つために直近のやり取りを記憶するため、悪意ある指示が一連の正常に見えるクライアント要求とサーバー応答の中に隠れる。PoC：悪意あるリサーチアシスタントエージェントが、財務アシスタントエージェントを通じて**機密情報を引き出し、無断で株式取引を実行**する

summary_ko: |
  Unit 42: 악성 AI 에이전트가 **이미 수립된 에이전트 간 세션**을 이용해 피해 에이전트에 은밀한 지시를 전달한다. 공격 표면은 **A2A 프로토콜의 상태 유지 설계**에서 비롯된다 — 에이전트는 일관된 대화를 위해 최근 상호작용을 기억하므로, 악성 지시가 정상으로 보이는 일련의 클라이언트 요청과 서버 응답 사이에 숨는다. PoC: 악성 연구 지원 에이전트가 금융 지원 에이전트를 통해 **기밀 정보를 빼내고 무단 주식 거래를 실행**했다

summary_de: |
  Unit 42: Ein bösartiger KI-Agent nutzt eine **bereits aufgebaute Agenten-übergreifende Sitzung**, um einem Opfer-Agenten verdeckte Anweisungen zu übermitteln. Die Angriffsfläche entsteht durch das **zustandsbehaftete Design des A2A-Protokolls** — Agenten merken sich frühere Interaktionen, um eine kohärente Unterhaltung zu führen, sodass sich bösartige Anweisungen in einer Reihe scheinbar normaler Client-Anfragen und Server-Antworten verstecken. PoC: Ein rogue Research-Assistant-Agent **extrahiert über einen Finance-Assistant-Agenten vertrauliche Informationen und führt unautorisierte Aktiengeschäfte aus**

summary_fr: |
  Unit 42 : un agent IA malveillant utilise une **session inter-agents déjà établie** pour transmettre des instructions dissimulées à un agent victime. La surface d'attaque vient de la **conception avec état du protocole A2A** — les agents mémorisent les interactions récentes pour garder une conversation cohérente, si bien que les instructions malveillantes se dissimulent parmi une série de requêtes client et de réponses serveur apparemment normales. PoC : un agent assistant de recherche rogue, via un agent assistant financier, **extrait des informations confidentielles et exécute des transactions boursières non autorisées**

summary_es: |
  Unit 42: un agente de IA malicioso usa una **sesión entre agentes ya establecida** para entregar instrucciones encubiertas a un agente víctima. La superficie de ataque proviene del **diseño con estado del protocolo A2A** — los agentes recuerdan interacciones recientes para mantener una conversación coherente, así que las instrucciones maliciosas se esconden entre una serie de solicitudes de cliente y respuestas de servidor aparentemente normales. PoC: un agente malicioso de asistente de investigación, a través de un agente de asistente financiero, **extrae información confidencial y ejecuta operaciones bursátiles no autorizadas**

sources:
  - url: https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/
    label: Unit 42

disputed: false
landmark: true
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Agent Session Smuggling: agents deceiving agents over A2A

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Unit 42: a malicious AI agent uses an **already-established cross-agent session** to deliver covert instructions to a victim agent. The attack surface comes from the **stateful design of the A2A protocol** — agents remember recent interactions to keep a coherent conversation, so malicious instructions hide among a string of seemingly normal client requests and server responses. PoC: a rogue research-assistant agent, through a finance-assistant agent, **extracts confidential information and executes unauthorized stock trades**

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
| 1 | Unit 42 | <https://unit42.paloaltonetworks.com/agent-session-smuggling-in-agent2agent-systems/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-31` (raw: 2025-10-31, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-31-agent-session-smuggling-a2a` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>
- `2025-10-24` [Atlas omnibox jailbreak](2025-10-24-atlas-omnibox-yue-yu.md)<br>  <sub>Atlas omnibox jailbreak</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-31-agent-session-smuggling-a2a.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
