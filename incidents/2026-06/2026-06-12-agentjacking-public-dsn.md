---
id: 2026-06-12-agentjacking-public-dsn
title: "Agentjacking: one public DSN hijacks AI coding agents"
title_zh: "Agentjacking：一个公开 DSN 就能劫持 AI 编码 agent"
title_ja: "Agentjacking：1つの公開DSNがAIコーディングエージェントをハイジャック"
title_ko: "Agentjacking: 공개 DSN 하나로 AI 코딩 에이전트 하이재킹"
title_de: "Agentjacking: Ein öffentlicher DSN übernimmt KI-Coding-Agenten"
title_fr: "Agentjacking : un DSN public détourne les agents de code IA"
title_es: "Agentjacking: un DSN público secuestra a los agentes de código con IA"
date: 2026-06-12
date_precision: day
date_raw: "2026-06-12"

kind: research
type: [MCP, IPI]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Tenet Security: an attacker needs only a **Sentry DSN** (a **public write-only credential that can be picked up from browser JavaScript or GitHub search**) plus any HTTP client to inject malicious instructions into Sentry error events. **After Claude Code, Cursor and Codex retrieve these events over MCP, they cannot tell them apart from real application errors**, and they execute the attacker's commands with the developer's own system privileges. Tenet identified **publicly exposed DSNs belonging to at least 2,388 organizations**. The attack can steal environment variables, `~/.aws/config`, npm tokens, Docker credentials, git credentials and private repository URLs


summary_zh: |
  Tenet Security：攻击者只需一个 **Sentry DSN**（一种**可从浏览器 JavaScript 或 GitHub 搜索里捡到的公开只写凭据**）加任意 HTTP 客户端，就能把恶意指令注入 Sentry 的错误事件。**Claude Code、Cursor、Codex 经 MCP 取回这些事件后，无法把它们与真实的应用错误区分开**，并以开发者本人的系统权限执行攻击者的命令。Tenet 识别出**至少 2,388 个组织的 DSN 公开暴露**。可窃取环境变量、`~/.aws/config`、npm token、Docker 凭据、git 凭据与私有仓库 URL

summary_ja: |
  Tenet Security：攻撃者に必要なのは**Sentry DSN**（**ブラウザのJavaScriptやGitHub検索から拾える公開・書き込み専用の認証情報**）と任意のHTTPクライアントだけで、Sentryのエラーイベントに悪意ある指示を注入できる。**Claude Code、Cursor、CodexがMCP経由でこれらのイベントを取得すると、実際のアプリケーションエラーと区別がつかず**、開発者自身のシステム権限で攻撃者のコマンドを実行してしまう。Tenetは**少なくとも2,388組織に属する公開DSN**を特定した。この攻撃は環境変数、`~/.aws/config`、npmトークン、Docker認証情報、git認証情報、非公開リポジトリのURLを窃取できる

summary_ko: |
  Tenet Security: 공격자에게는 **Sentry DSN**(**브라우저 JavaScript나 GitHub 검색으로 얻을 수 있는 공개 쓰기 전용 자격 증명**)과 아무 HTTP 클라이언트만 있으면 Sentry 오류 이벤트에 악성 지시를 주입할 수 있다. **Claude Code, Cursor, Codex가 MCP로 이 이벤트를 가져온 뒤에는 실제 애플리케이션 오류와 구분하지 못하고**, 개발자 자신의 시스템 권한으로 공격자 명령을 실행한다. Tenet는 **최소 2,388개 조직의 공개 노출된 DSN**을 확인했다. 이 공격으로 환경 변수, `~/.aws/config`, npm 토큰, Docker 자격 증명, git 자격 증명, 비공개 저장소 URL을 탈취할 수 있다

summary_de: |
  Tenet Security: Ein Angreifer braucht nur einen **Sentry-DSN** (ein **öffentliches, nur schreibendes Credential, das aus Browser-JavaScript oder über die GitHub-Suche aufgespürt werden kann**) plus einen beliebigen HTTP-Client, um bösartige Anweisungen in Sentry-Fehlerereignisse einzuschleusen. **Nachdem Claude Code, Cursor und Codex diese Ereignisse über MCP abgerufen haben, können sie sie nicht von echten Anwendungsfehlern unterscheiden**, und sie führen die Befehle des Angreifers mit den Systemrechten des Entwicklers aus. Tenet identifizierte **öffentlich exponierte DSNs von mindestens 2,388 Organisationen**. Der Angriff kann Umgebungsvariablen, `~/.aws/config`, npm-Token, Docker-Zugangsdaten, git-Zugangsdaten und private Repository-URLs stehlen

summary_fr: |
  Tenet Security : il suffit à un attaquant d'un **DSN Sentry** (un **identifiant public en écriture seule, récupérable depuis le JavaScript d'un navigateur ou une recherche GitHub**) plus de n'importe quel client HTTP pour injecter des instructions malveillantes dans les événements d'erreur Sentry. **Après que Claude Code, Cursor et Codex ont récupéré ces événements via MCP, ils ne peuvent pas les distinguer de vraies erreurs applicatives**, et ils exécutent les commandes de l'attaquant avec les privilèges système du développeur. Tenet a identifié **des DSN publiquement exposés appartenant à au moins 2 388 organisations**. L'attaque peut voler des variables d'environnement, `~/.aws/config`, des jetons npm, des identifiants Docker, des identifiants git et des URL de dépôts privés

summary_es: |
  Tenet Security: un atacante solo necesita un **DSN de Sentry** (una **credencial pública de solo escritura que puede obtenerse del JavaScript del navegador o de una búsqueda en GitHub**) más cualquier cliente HTTP para inyectar instrucciones maliciosas en los eventos de error de Sentry. **Después de que Claude Code, Cursor y Codex recuperan estos eventos por MCP, no pueden distinguirlos de errores reales de la aplicación**, y ejecutan los comandos del atacante con los privilegios del propio sistema del desarrollador. Tenet identificó **DSN expuestos públicamente pertenecientes a al menos 2,388 organizaciones**. El ataque puede robar variables de entorno, `~/.aws/config`, tokens de npm, credenciales de Docker, credenciales de git y URL de repositorios privados

sources:
  - url: https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/
    label: Tenet Security
  - url: https://thenewstack.io/agentjacking-sentry-mcp-attack/
    label: The New Stack

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Agentjacking: one public DSN hijacks AI coding agents

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Tenet Security: an attacker needs only a **Sentry DSN** (a **public write-only credential that can be picked up from browser JavaScript or GitHub search**) plus any HTTP client to inject malicious instructions into Sentry error events. **After Claude Code, Cursor and Codex retrieve these events over MCP, they cannot tell them apart from real application errors**, and they execute the attacker's commands with the developer's own system privileges. Tenet identified **publicly exposed DSNs belonging to at least 2,388 organizations**. The attack can steal environment variables, `~/.aws/config`, npm tokens, Docker credentials, git credentials and private repository URLs

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Tenet Security | <https://tenetsecurity.ai/blog/agentjacking-coding-agents-with-fake-sentry-errors/> |
| 2 | The New Stack | <https://thenewstack.io/agentjacking-sentry-mcp-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-12` (raw: 2026-06-12, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-12-agentjacking-public-dsn` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-15` [SearchLeak (CVE-2026-42824)](2026-06-15-searchleak.md)<br>  <sub>SearchLeak (CVE-2026-42824)</sub>
- `2026-06-24` [BioShocking: dumb the agent down first, then take the password](2026-06-24-bioshocking-agent-xian-jiao-sha.md)<br>  <sub>BioShocking: dumb the agent down first, then take the password</sub>
- `2026-06-08` [AgentForger: one link forges an "AI insider"](2026-06-08-agentforger-yi-tiao-lian-jie.md)<br>  <sub>AgentForger: one link forges an "AI insider"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-12-agentjacking-public-dsn.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
