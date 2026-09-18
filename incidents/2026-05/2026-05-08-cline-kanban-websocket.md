---
id: 2026-05-08-cline-kanban-websocket
title: "Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)"
title_zh: "Cline Kanban 跨源 WebSocket 劫持（CVE-2026-44211）"
title_ja: "Cline KanbanのクロスオリジンWebSocketハイジャック（CVE-2026-44211）"
title_ko: "Cline Kanban 교차 출처 WebSocket 하이재킹 (CVE-2026-44211)"
title_de: "Cline Kanban: Cross-Origin-WebSocket-Hijacking (CVE-2026-44211)"
title_fr: "Détournement de WebSocket cross-origin de Cline Kanban (CVE-2026-44211)"
title_es: "Secuestro de WebSocket de origen cruzado en Cline Kanban (CVE-2026-44211)"
date: 2026-05-08
date_precision: day
date_raw: "2026-05-08"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVSS 9.7**, affecting ≤ 2.13.0. The `kanban` npm package used by the cline CLI started a WebSocket service on `127.0.0.1:3484` that **does not validate the Origin header** — **any website the developer visits can connect silently**, steal data in real time and **inject arbitrary prompts into the agent's input, hijacking the running AI agent's terminal** to achieve RCE. **No public patch at disclosure**


summary_zh: |
  **CVSS 9.7**，影响 ≤ 2.13.0。cline CLI 用的 `kanban` npm 包在 `127.0.0.1:3484` 起了一个 **不校验 Origin 头**的 WebSocket 服务 —— **开发者访问的任何网站都能静默连上去**，实时窃取数据，并**向 agent 的输入注入任意提示、劫持正在运行的 AI agent 终端**，达成 RCE。**披露时无公开补丁**

summary_ja: |
  **CVSS 9.7**、2.13.0以下が対象。cline CLIが使用する`kanban` npmパッケージは`127.0.0.1:3484`でWebSocketサービスを起動するが、**Originヘッダーを検証しない**——**開発者が訪れるあらゆるWebサイトが無言で接続でき**、リアルタイムでデータを窃取し、**エージェントの入力に任意のプロンプトを注入して、実行中のAIエージェントのターミナルをハイジャック**しRCEを達成できる。**公表時点で公開パッチなし**

summary_ko: |
  **CVSS 9.7**, 2.13.0 이하 영향. cline CLI가 사용하는 `kanban` npm 패키지가 `127.0.0.1:3484`에 WebSocket 서비스를 열었는데 **Origin 헤더를 검증하지 않는다** — **개발자가 방문하는 어떤 웹사이트든 조용히 접속**해 데이터를 실시간으로 탈취하고 **에이전트 입력에 임의 프롬프트를 주입해 실행 중인 AI 에이전트의 터미널을 하이재킹**하여 RCE에 이를 수 있었다. **공개 시점에 공개 패치는 없었다**

summary_de: |
  **CVSS 9.7**, betrifft ≤ 2.13.0. Das von der cline CLI genutzte npm-Paket `kanban` startete einen WebSocket-Dienst auf `127.0.0.1:3484`, der **den Origin-Header nicht validiert** — **jede Website, die der Entwickler besucht, kann sich still verbinden**, Daten in Echtzeit stehlen und **beliebige Prompts in die Eingabe des Agenten einschleusen und so das Terminal des laufenden KI-Agenten übernehmen**, um RCE zu erreichen. **Zum Zeitpunkt der Offenlegung kein öffentlicher Patch**

summary_fr: |
  **CVSS 9.7**, affecte ≤ 2.13.0. Le paquet npm `kanban` utilisé par la CLI cline démarrait un service WebSocket sur `127.0.0.1:3484` qui **ne valide pas l'en-tête Origin** — **tout site web que le développeur visite peut s'y connecter silencieusement**, voler des données en temps réel et **injecter des prompts arbitraires dans l'entrée de l'agent, détournant le terminal de l'agent IA en cours** pour obtenir un RCE. **Aucun correctif public au moment de la divulgation**

summary_es: |
  **CVSS 9.7**, afecta a ≤ 2.13.0. El paquete npm `kanban` que usa la CLI de cline iniciaba un servicio WebSocket en `127.0.0.1:3484` que **no valida la cabecera Origin** — **cualquier sitio web que visite el desarrollador puede conectarse en silencio**, robar datos en tiempo real e **inyectar prompts arbitrarios en la entrada del agente, secuestrando la terminal del agente de IA en ejecución** para lograr RCE. **Sin parche público en el momento de la divulgación**

sources:
  - url: https://advisories.gitlab.com/npm/cline/CVE-2026-44211/
    label: GHSA / GitLab Advisory
  - url: https://cybersecuritynews.com/cline-ai-agent-vulnerability/
    label: CybersecurityNews

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

**CVSS 9.7**, affecting ≤ 2.13.0. The `kanban` npm package used by the cline CLI started a WebSocket service on `127.0.0.1:3484` that **does not validate the Origin header** — **any website the developer visits can connect silently**, steal data in real time and **inject arbitrary prompts into the agent's input, hijacking the running AI agent's terminal** to achieve RCE. **No public patch at disclosure**

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GHSA / GitLab Advisory | <https://advisories.gitlab.com/npm/cline/CVE-2026-44211/> |
| 2 | CybersecurityNews | <https://cybersecuritynews.com/cline-ai-agent-vulnerability/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-08` (raw: 2026-05-08, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-08-cline-kanban-websocket` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-05-07` [TrustFall: RCE on a single keypress](2026-05-07-trustfall-rce-yi-ci-hui.md)<br>  <sub>TrustFall: RCE on a single keypress</sub>
- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](../2026-04/2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](../2026-04/2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>
- `2026-06-30` [GuardFall: 10 of 11 open-source agents can be pushed past their shell boundary](../2026-06/2026-06-30-guardfall-agent-shell.md)<br>  <sub>GuardFall: 10 of 11 open-source agents can be pushed past their shell boundary</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-08-cline-kanban-websocket.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
