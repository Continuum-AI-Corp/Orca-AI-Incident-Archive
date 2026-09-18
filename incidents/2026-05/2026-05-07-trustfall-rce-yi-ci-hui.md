---
id: 2026-05-07-trustfall-rce-yi-ci-hui
title: "TrustFall: RCE on a single keypress"
title_zh: "TrustFall：一次回车即 RCE"
title_ja: "TrustFall：キー1回の押下でRCE"
title_ko: "TrustFall: 키 한 번 누르면 RCE"
title_de: "TrustFall: RCE mit einem einzigen Tastendruck"
title_fr: "TrustFall : un RCE en une seule frappe"
title_es: "TrustFall: RCE con una sola pulsación de tecla"
date: 2026-05-07
date_precision: day
date_raw: "2026-05-07"

kind: research
type: [SANDBOX, MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Adversa AI: a systemic architectural flaw affecting four agentic CLIs — **Claude Code, Gemini CLI, Cursor CLI and GitHub Copilot**. After the developer accepts the "folder trust" prompt, a malicious repository config **auto-starts a project-level MCP server** — one Enter press in a developer environment runs the attacker's code with the developer's own privileges, and **in headless CI workflows there is not even a prompt**. Key points: `enableAllProjectMcpServers` **is not banned in project scope the way `bypassPermissions` is**; and **Claude Code v2.1+ removed the earlier MCP warning from its dialog**


summary_zh: |
  Adversa AI：影响 **Claude Code、Gemini CLI、Cursor CLI、GitHub Copilot** 四款 agentic CLI 的系统性架构缺陷。恶意仓库配置在开发者接受「文件夹信任」提示后**自动启动项目级 MCP server** —— 开发者环境里一次回车就以本人权限跑起攻击者的代码，**headless CI 工作流里连提示都没有**。关键点：`enableAllProjectMcpServers` **没有像 `bypassPermissions` 那样被禁止在项目作用域设置**；且 **Claude Code v2.1+ 的对话框去掉了早先的 MCP 警告**

summary_ja: |
  Adversa AI：4つのエージェント型CLIに影響する体系的なアーキテクチャ欠陥——**Claude Code、Gemini CLI、Cursor CLI、GitHub Copilot**。開発者が「フォルダの信頼」プロンプトを承認すると、悪性リポジトリの設定が**プロジェクトレベルのMCPサーバーを自動起動する**——開発者環境でEnterを1回押すだけで、開発者自身の権限で攻撃者のコードが実行され、**ヘッドレスCIワークフローではプロンプトすら表示されない**。要点：`enableAllProjectMcpServers`は**`bypassPermissions`のようにプロジェクトスコープで禁止されていない**。そして**Claude Code v2.1以降は、以前あったMCP警告をダイアログから削除した**

summary_ko: |
  Adversa AI: **Claude Code, Gemini CLI, Cursor CLI, GitHub Copilot** 네 가지 에이전틱 CLI에 영향을 주는 구조적 설계 결함이다. 개발자가 "폴더 신뢰" 프롬프트를 수락하면 악성 저장소 설정이 **프로젝트 수준 MCP 서버를 자동 시작**한다 — 개발 환경에서 Enter를 한 번 누르면 공격자 코드가 개발자 자신의 권한으로 실행되며, **헤드리스 CI 워크플로에서는 프롬프트조차 없다**. 핵심: `enableAllProjectMcpServers`는 **`bypassPermissions`처럼 프로젝트 범위에서 금지되지 않는다**. 그리고 **Claude Code v2.1+는 대화상자에서 이전의 MCP 경고를 제거했다**

summary_de: |
  Adversa AI: Ein systemischer Architekturfehler betrifft vier agentische CLIs — **Claude Code, Gemini CLI, Cursor CLI und GitHub Copilot**. Nachdem der Entwickler den „Ordner vertrauen“-Dialog akzeptiert hat, **startet eine bösartige Repository-Konfiguration automatisch einen projektweiten MCP-Server** — ein Enter-Druck in einer Entwicklungsumgebung führt den Code des Angreifers mit den Rechten des Entwicklers selbst aus, und **in Headless-CI-Workflows gibt es nicht einmal einen Dialog**. Kernpunkte: `enableAllProjectMcpServers` **ist im Projektkontext nicht verboten, anders als `bypassPermissions`**; und **Claude Code v2.1+ hat die frühere MCP-Warnung aus seinem Dialog entfernt**

summary_fr: |
  Adversa AI : un défaut d'architecture systémique touchant quatre CLI agentiques — **Claude Code, Gemini CLI, Cursor CLI et GitHub Copilot**. Après que le développeur accepte l'invite de « confiance dans le dossier », une configuration de dépôt malveillante **démarre automatiquement un serveur MCP au niveau du projet** — une pression sur Entrée dans un environnement de développement exécute le code de l'attaquant avec les propres privilèges du développeur, et **dans les workflows de CI headless il n'y a même pas d'invite**. Points clés : `enableAllProjectMcpServers` **n'est pas banni au niveau du projet comme l'est `bypassPermissions`** ; et **Claude Code v2.1+ a retiré l'avertissement MCP de sa boîte de dialogue**

summary_es: |
  Adversa AI: un fallo arquitectónico sistémico que afecta a cuatro CLI agénticas — **Claude Code, Gemini CLI, Cursor CLI y GitHub Copilot**. Después de que el desarrollador acepta el aviso de "confianza en la carpeta", una configuración maliciosa del repositorio **inicia automáticamente un servidor MCP a nivel de proyecto** — una pulsación de Enter en un entorno de desarrollo ejecuta el código del atacante con los propios privilegios del desarrollador, y **en flujos de CI headless ni siquiera hay un aviso**. Puntos clave: `enableAllProjectMcpServers` **no está prohibido en el ámbito de proyecto como sí lo está `bypassPermissions`**; y **Claude Code v2.1+ eliminó la advertencia sobre MCP que antes aparecía en su diálogo**

sources:
  - url: https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/
    label: Adversa
  - url: https://www.darkreading.com/application-security/trustfall-exposes-claude-code-execution-risk
    label: Dark Reading

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# TrustFall: RCE on a single keypress

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Adversa AI: a systemic architectural flaw affecting four agentic CLIs — **Claude Code, Gemini CLI, Cursor CLI and GitHub Copilot**. After the developer accepts the "folder trust" prompt, a malicious repository config **auto-starts a project-level MCP server** — one Enter press in a developer environment runs the attacker's code with the developer's own privileges, and **in headless CI workflows there is not even a prompt**. Key points: `enableAllProjectMcpServers` **is not banned in project scope the way `bypassPermissions` is**; and **Claude Code v2.1+ removed the earlier MCP warning from its dialog**

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    S1["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Adversa | <https://adversa.ai/blog/trustfall-coding-agent-security-flaw-rce-claude-cursor-gemini-cli-copilot/> |
| 2 | Dark Reading | <https://www.darkreading.com/application-security/trustfall-exposes-claude-code-execution-risk> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-07` (raw: 2026-05-07, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape · [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-07-trustfall-rce-yi-ci-hui` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md) · [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-08` [Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)](2026-05-08-cline-kanban-websocket.md)<br>  <sub>Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)</sub>
- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](../2026-04/2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](../2026-04/2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-07-trustfall-rce-yi-ci-hui.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
