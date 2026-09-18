---
id: 2025-10-22-shadow-escape-mcp-agent
title: "Shadow Escape: first zero-click agent attack over MCP"
title_zh: "Shadow Escape：首个经 MCP 的零点击 agent 攻击"
title_ja: "Shadow Escape：MCP経由の初のゼロクリックエージェント攻撃"
title_ko: "Shadow Escape: MCP를 통한 최초의 제로클릭 에이전트 공격"
title_de: "Shadow Escape: erster Zero-Click-Agentenangriff über MCP"
title_fr: "Shadow Escape : première attaque d'agent zero-click via MCP"
title_es: "Shadow Escape: el primer ataque zero-click a un agente a través de MCP"
date: 2025-10-22
date_precision: day
date_raw: "2025-10-22"

kind: research
type: [MCP, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Disclosed by Operant AI. **No user mistake, phishing or malicious extension required** — it exploits the trust an agent already holds through legitimate MCP connections to invisibly exfiltrate data across major platforms including ChatGPT, Claude and Gemini, including Social Security and medical record numbers


summary_zh: |
  Operant AI 披露。**不需要用户失误、钓鱼或恶意扩展** —— 直接利用 agent 经合法 MCP 连接已获得的信任，跨 ChatGPT、Claude、Gemini 等主流平台隐形外带数据，包括社保号与病历号

summary_ja: |
  Operant AIが公表。**ユーザーのミスも、フィッシングも、悪性拡張機能も不要**——正規のMCP接続を通じてエージェントがすでに持つ信頼を悪用し、ChatGPT、Claude、Geminiを含む主要プラットフォームをまたいで、社会保障番号や医療記録番号を含むデータを目に見えない形で外部送信する

summary_ko: |
  Operant AI가 공개했다. **사용자 실수, 피싱, 악성 확장 프로그램이 모두 필요 없다** — 에이전트가 정상적인 MCP 연결을 통해 이미 보유한 신뢰를 악용해 ChatGPT, Claude, Gemini 등 주요 플랫폼 전반에서 사회보장번호와 의료 기록 번호를 포함한 데이터를 보이지 않게 유출한다

summary_de: |
  Offengelegt von Operant AI. **Kein Nutzerfehler, kein Phishing und keine bösartige Erweiterung nötig** — es nutzt das Vertrauen aus, das ein Agent über legitime MCP-Verbindungen bereits besitzt, um Daten über große Plattformen wie ChatGPT, Claude und Gemini hinweg unsichtbar zu exfiltrieren, darunter Sozialversicherungs- und Krankenaktennummern

summary_fr: |
  Divulguée par Operant AI. **Aucune erreur de l'utilisateur, phishing ou extension malveillante nécessaire** — elle exploite la confiance dont un agent dispose déjà via des connexions MCP légitimes pour exfiltrer invisiblement des données sur les principales plateformes, dont ChatGPT, Claude et Gemini, y compris des numéros de sécurité sociale et de dossier médical

summary_es: |
  Divulgado por Operant AI. **No requiere ningún error del usuario, phishing ni extensión maliciosa** — explota la confianza que un agente ya tiene mediante conexiones MCP legítimas para exfiltrar datos de forma invisible en las principales plataformas, incluidas ChatGPT, Claude y Gemini, como números de Seguro Social y de historiales médicos

sources:
  - url: https://www.operant.ai/art-kubed/shadow-escape
    label: Operant AI
  - url: https://www.globenewswire.com/news-release/2025/10/22/3171164/0/en/Operant-AI-Discovers-Shadow-Escape-The-First-Zero-Click-Agentic-Attack-via-MCP.html
    label: GlobeNewswire

disputed: false
landmark: true
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Shadow Escape: first zero-click agent attack over MCP

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Disclosed by Operant AI. **No user mistake, phishing or malicious extension required** — it exploits the trust an agent already holds through legitimate MCP connections to invisibly exfiltrate data across major platforms including ChatGPT, Claude and Gemini, including Social Security and medical record numbers

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
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
| 1 | Operant AI | <https://www.operant.ai/art-kubed/shadow-escape> |
| 2 | GlobeNewswire | <https://www.globenewswire.com/news-release/2025/10/22/3171164/0/en/Operant-AI-Discovers-Shadow-Escape-The-First-Zero-Click-Agentic-Attack-via-MCP.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-22` (raw: 2025-10-22, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-22-shadow-escape-mcp-agent` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-01` [Framelink Figma MCP RCE](2025-10-01-framelink-figma-mcp-rce.md)<br>  <sub>Framelink Figma MCP RCE</sub>
- `2025-09-03` [Claude Code MCP auto-enable bypass](../2025-09/2025-09-03-claude-code-mcp.md)<br>  <sub>Claude Code MCP auto-enable bypass</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-22-shadow-escape-mcp-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
