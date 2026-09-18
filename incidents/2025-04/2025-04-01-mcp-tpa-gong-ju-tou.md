---
id: 2025-04-01-mcp-tpa-gong-ju-tou
title: "First systematic disclosure of MCP tool-poisoning attacks"
title_zh: "MCP 工具投毒攻击（TPA）首次系统披露"
title_ja: "MCPツール汚染攻撃の初の体系的公表"
title_ko: "MCP 도구 오염 공격의 최초 체계적 공개"
title_de: "Erste systematische Offenlegung von MCP-Tool-Poisoning-Angriffen"
title_fr: "Première divulgation systématique d'attaques par empoisonnement d'outils MCP"
title_es: "Primera divulgación sistemática de ataques de envenenamiento de herramientas MCP"
date: 2025-04-01
date_precision: day
date_raw: "2025-04-01"

kind: research
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Invariant Labs: a malicious MCP server hid instructions inside its **tool description** (descriptions enter the agent context as trusted content). Demo: the description of a "guessing game" MCP server instructed the legitimate whatsapp-mcp on the same agent to **steal the entire WhatsApp chat history**. They also introduced the "rug pull" (the tool description is changed after the fact)


summary_zh: |
  Invariant Labs：恶意 MCP server 把指令藏在 **tool description** 里（描述会作为可信内容进入 agent 上下文）。演示：一个「猜谜游戏」MCP server 的描述指挥同一 agent 上的合法 whatsapp-mcp **窃取全部 WhatsApp 聊天记录**。同时提出 "rug pull"（工具描述事后被改）

summary_ja: |
  Invariant Labs：悪性MCPサーバーが**ツール説明文**の中に指示を隠した（説明文は信頼されたコンテンツとしてエージェントのコンテキストに入る）。デモでは、「数当てゲーム」MCPサーバーの説明文が、同じエージェント上の正規のwhatsapp-mcpに**WhatsAppのチャット履歴全体を窃取**するよう指示した。同社は「rug pull」（後からツール説明文を書き換える手法）も紹介した

summary_ko: |
  Invariant Labs: 악성 MCP 서버가 **도구 설명** 안에 지시를 숨겼다(설명은 신뢰할 수 있는 콘텐츠로 에이전트 컨텍스트에 들어간다). 시연: "숫자 맞히기 게임" MCP 서버의 설명이 같은 에이전트의 정상적인 whatsapp-mcp에게 **WhatsApp 채팅 기록 전체를 탈취**하라고 지시했다. 이들은 사후에 도구 설명을 바꿔치기하는 "러그 풀(rug pull)"도 소개했다

summary_de: |
  Invariant Labs: Ein bösartiger MCP-Server versteckte Anweisungen in seiner **Tool-Beschreibung** (Beschreibungen gelangen als vertrauenswürdiger Inhalt in den Agentenkontext). Demo: Die Beschreibung eines „Rate-Spiel“-MCP-Servers wies das legitime whatsapp-mcp auf demselben Agenten an, **den gesamten WhatsApp-Chatverlauf zu stehlen**. Sie führten außerdem den „Rug Pull“ ein (die Tool-Beschreibung wird nachträglich geändert)

summary_fr: |
  Invariant Labs : un serveur MCP malveillant a caché des instructions dans sa **description d'outil** (les descriptions entrent dans le contexte de l'agent comme du contenu de confiance). Démo : la description d'un serveur MCP de « jeu de devinettes » demandait au serveur whatsapp-mcp légitime du même agent de **voler tout l'historique de conversations WhatsApp**. Ils ont aussi introduit le « rug pull » (la description de l'outil est modifiée après coup)

summary_es: |
  Invariant Labs: un servidor MCP malicioso ocultó instrucciones dentro de su **descripción de herramienta** (las descripciones entran en el contexto del agente como contenido confiable). Demostración: la descripción de un servidor MCP de "juego de adivinanzas" instruyó al whatsapp-mcp legítimo del mismo agente a **robar todo el historial de chat de WhatsApp**. También introdujeron el "rug pull" (la descripción de la herramienta se cambia a posteriori)

sources:
  - url: https://github.com/invariantlabs-ai/mcp-injection-experiments
    label: Reproduction code
  - url: https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/
    label: Docker retrospective

disputed: false
landmark: true
scan_month: 2025-04
scan_ref: "SCAN.md §5 2025-04"
---

# First systematic disclosure of MCP tool-poisoning attacks

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Invariant Labs: a malicious MCP server hid instructions inside its **tool description** (descriptions enter the agent context as trusted content). Demo: the description of a "guessing game" MCP server instructed the legitimate whatsapp-mcp on the same agent to **steal the entire WhatsApp chat history**. They also introduced the "rug pull" (the tool description is changed after the fact)

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Reproduction code | <https://github.com/invariantlabs-ai/mcp-injection-experiments> |
| 2 | Docker retrospective | <https://www.docker.com/blog/mcp-horror-stories-whatsapp-data-exfiltration-issue/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-04-01` (raw: 2025-04-01, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-04-01-mcp-tpa-gong-ju-tou` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-04-01` [GPT-4.1 jailbroken through a poisoned MCP tool](2025-04-01-gpt-mcp-jing-gong-ju.md)<br>  <sub>GPT-4.1 jailbroken through a poisoned MCP tool</sub>
- `2025-05-26` [GitHub MCP "Toxic Agent Flow"](../2025-05/2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>
- `2025-06-13` [MCP Inspector unauthenticated RCE](../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>MCP Inspector unauthenticated RCE</sub>
- `2025-06-04` [Asana MCP server cross-tenant data exposure](../2025-06/2025-06-04-asana-mcp-server.md)<br>  <sub>Asana MCP server cross-tenant data exposure</sub>

---

[← 2025-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-04/2025-04-01-mcp-tpa-gong-ju-tou.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
