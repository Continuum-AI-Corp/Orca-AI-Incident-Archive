---
id: 2026-04-15-windsurf-mcp-rce
title: "Windsurf zero-click MCP RCE (CVE-2026-30615)"
title_zh: "Windsurf 零点击 MCP RCE（CVE-2026-30615）"
title_ja: "WindsurfのゼロクリックMCP RCE（CVE-2026-30615）"
title_ko: "Windsurf 제로클릭 MCP RCE (CVE-2026-30615)"
title_de: "Windsurf: Zero-Click-MCP-RCE (CVE-2026-30615)"
title_fr: "RCE MCP zero-click dans Windsurf (CVE-2026-30615)"
title_es: "RCE zero-click por MCP en Windsurf (CVE-2026-30615)"
date: 2026-04-15
date_precision: day
date_raw: "2026-04-15"

kind: vulnerability
type: [SANDBOX, MCP]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Windsurf 1.9544.26: a prompt injection in malicious HTML content can, **with no user interaction at all** (simply opening the attacker's content in the IDE), modify the local MCP configuration and **auto-register a malicious MCP STDIO server**, leading to command execution. Delivery surfaces include web pages browsed in the IDE, a malicious README in a cloned repository, **or a poisoned tool description returned by a remote server**


summary_zh: |
  Windsurf 1.9544.26：恶意 HTML 内容中的提示注入**未经任何用户交互**（IDE 打开攻击者内容即可）就能修改本地 MCP 配置、**自动注册一个恶意 MCP STDIO server**，进而命令执行。投递面包括 IDE 浏览的网页、克隆仓库里的恶意 README、**或远程 server 返回的被投毒工具描述**

summary_ja: |
  Windsurf 1.9544.26：悪性HTMLコンテンツ内のプロンプトインジェクションにより、**ユーザー操作が一切なくても**（IDEで攻撃者のコンテンツを開くだけで）、ローカルのMCP設定が書き換えられ、**悪性のMCP STDIOサーバーが自動登録**され、コマンド実行に至る。配信経路にはIDE内で閲覧したWebページ、クローンしたリポジトリ内の悪性README、**あるいはリモートサーバーが返す汚染されたツール説明文**が含まれる

summary_ko: |
  Windsurf 1.9544.26: 악성 HTML 콘텐츠의 프롬프트 인젝션으로 **사용자 상호작용이 전혀 없이**(IDE에서 공격자의 콘텐츠를 열기만 하면) 로컬 MCP 설정을 변경하고 **악성 MCP STDIO 서버를 자동 등록**해 명령 실행에 이르게 할 수 있다. 전달 경로에는 IDE에서 열람한 웹 페이지, 클론한 저장소의 악성 README, **또는 원격 서버가 반환한 오염된 도구 설명**이 포함된다

summary_de: |
  Windsurf 1.9544.26: Eine Prompt-Injection in bösartigem HTML-Inhalt kann **ganz ohne Nutzerinteraktion** (das bloße Öffnen des Inhalts des Angreifers in der IDE) die lokale MCP-Konfiguration ändern und **automatisch einen bösartigen MCP-STDIO-Server registrieren**, was zur Befehlsausführung führt. Zu den Verteilungswegen gehören in der IDE aufgerufene Webseiten, eine bösartige README in einem geklonten Repository **oder eine vergiftete Tool-Beschreibung, die ein Remote-Server zurückgibt**

summary_fr: |
  Windsurf 1.9544.26 : une injection de prompt dans du contenu HTML malveillant peut, **sans aucune interaction de l'utilisateur** (il suffit d'ouvrir le contenu de l'attaquant dans l'IDE), modifier la configuration MCP locale et **auto-enregistrer un serveur MCP STDIO malveillant**, menant à l'exécution de commandes. Vecteurs de livraison : pages web consultées dans l'IDE, README malveillant d'un dépôt cloné, **ou description d'outil empoisonnée renvoyée par un serveur distant**

summary_es: |
  Windsurf 1.9544.26: una inyección de prompt en contenido HTML malicioso puede, **sin ninguna interacción del usuario** (simplemente abrir el contenido del atacante en el IDE), modificar la configuración local de MCP y **registrar automáticamente un servidor MCP STDIO malicioso**, lo que lleva a la ejecución de comandos. Las superficies de entrega incluyen páginas web navegadas en el IDE, un README malicioso en un repositorio clonado, **o una descripción de herramienta envenenada devuelta por un servidor remoto**

sources:
  - url: https://github.com/advisories/GHSA-wj2m-jvpr-64cq
    label: GHSA
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-30615
    label: NVD

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Windsurf zero-click MCP RCE (CVE-2026-30615)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Windsurf 1.9544.26: a prompt injection in malicious HTML content can, **with no user interaction at all** (simply opening the attacker's content in the IDE), modify the local MCP configuration and **auto-register a malicious MCP STDIO server**, leading to command execution. Delivery surfaces include web pages browsed in the IDE, a malicious README in a cloned repository, **or a poisoned tool description returned by a remote server**

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    S1["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GHSA | <https://github.com/advisories/GHSA-wj2m-jvpr-64cq> |
| 2 | NVD | <https://nvd.nist.gov/vuln/detail/CVE-2026-30615> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-15` (raw: 2026-04-15, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape · [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-15-windsurf-mcp-rce` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md) · [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>
- `2026-04-28` [OpenAI Codex sandbox-escape zero-day](2026-04-28-codex-sha-xiang-rao-guo.md)<br>  <sub>OpenAI Codex sandbox-escape zero-day</sub>
- `2026-05-08` [Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)](../2026-05/2026-05-08-cline-kanban-websocket.md)<br>  <sub>Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-15-windsurf-mcp-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
