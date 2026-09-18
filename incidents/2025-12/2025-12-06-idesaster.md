---
id: 2025-12-06-idesaster
title: "IDEsaster"
title_zh: "IDEsaster"
title_ja: "IDEsaster"
title_ko: "IDEsaster"
title_de: "IDEsaster"
title_fr: "IDEsaster"
title_es: "IDEsaster"
date: 2025-12-06
date_precision: day
date_raw: "2025-12-06"

kind: research
type: [SANDBOX, MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Researcher **Ari Marzouk (MaccariTA)**, a six-month investigation, 30+ vulnerabilities: **100% of the AI IDEs and coding assistants tested were affected**, at least **24 CVEs** plus an additional AWS advisory. Covers GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI and Claude Code. The common pattern: place payloads in files the AI reads (repository config, code comments, issue descriptions, MCP tool responses) and direct the AI to **weaponize the IDE's legitimate features**


summary_zh: |
  研究者 **Ari Marzouk（MaccariTA）** 六个月调查，30+ 漏洞，**受测的 AI IDE 与编码助手 100% 存在问题**，至少 **24 个 CVE** + AWS 额外公告。覆盖 GitHub Copilot、Cursor、Windsurf、Kiro.dev、Zed.dev、Roo Code、Junie、Cline、Gemini CLI、Claude Code。统一模式：把载荷放进 AI 会读的文件（仓库配置、代码注释、issue 描述、MCP 工具响应），指挥 AI **把 IDE 的合法功能武器化**

summary_ja: |
  研究者**Ari Marzouk氏（MaccariTA）**による6か月の調査、30以上の脆弱性：**テストされたAI IDEとコーディングアシスタントの100%が影響を受けた**。少なくとも**24件のCVE**に加え、AWSの追加アドバイザリも存在する。GitHub Copilot、Cursor、Windsurf、Kiro.dev、Zed.dev、Roo Code、Junie、Cline、Gemini CLI、Claude Codeが対象。共通パターン：AIが読むファイル（リポジトリ設定、コードコメント、イシュー説明、MCPツール応答）にペイロードを置き、AIに**IDEの正規機能を兵器化させる**よう誘導する

summary_ko: |
  연구자 **Ari Marzouk (MaccariTA)**의 6개월 조사, 취약점 30건 이상: **테스트한 AI IDE와 코딩 어시스턴트 전부(100%)가 영향을 받았고**, 최소 **CVE 24건**과 추가 AWS 권고가 있었다. GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI, Claude Code가 포함된다. 공통 패턴: AI가 읽는 파일(저장소 설정, 코드 주석, 이슈 설명, MCP 도구 응답)에 페이로드를 넣고 AI가 **IDE의 정상 기능을 무기화**하도록 유도한다

summary_de: |
  Forscher **Ari Marzouk (MaccariTA)**, eine sechsmonatige Untersuchung, 30+ Schwachstellen: **100% der getesteten KI-IDEs und Coding-Assistenten waren betroffen**, mindestens **24 CVEs** plus eine zusätzliche AWS-Meldung. Abgedeckt sind GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI und Claude Code. Das gemeinsame Muster: Nutzlasten in Dateien platzieren, die die KI liest (Repository-Konfiguration, Codekommentare, Issue-Beschreibungen, MCP-Tool-Antworten), und die KI dazu bringen, **die legitimen Funktionen der IDE als Waffe einzusetzen**

summary_fr: |
  Le chercheur **Ari Marzouk (MaccariTA)**, six mois d'enquête, plus de 30 vulnérabilités : **100 % des IDE d'IA et assistants de code testés étaient affectés**, au moins **24 CVE** plus un avis AWS supplémentaire. Couvre GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI et Claude Code. Le schéma commun : placer des charges utiles dans des fichiers que l'IA lit (configuration de dépôt, commentaires de code, descriptions d'issues, réponses d'outils MCP) et amener l'IA à **weaponiser les fonctionnalités légitimes de l'IDE**

summary_es: |
  El investigador **Ari Marzouk (MaccariTA)**, una investigación de seis meses, más de 30 vulnerabilidades: **el 100% de los IDE de IA y asistentes de código probados se vieron afectados**, al menos **24 CVE** más un aviso adicional de AWS. Abarca GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI y Claude Code. El patrón común: colocar cargas útiles en archivos que la IA lee (configuración del repositorio, comentarios de código, descripciones de issues, respuestas de herramientas MCP) y dirigir a la IA a **convertir en armas las funciones legítimas del IDE**

sources:
  - url: https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html
    label: THN
  - url: https://www.tomshardware.com/tech-industry/cyber-security/researchers-uncover-critical-ai-ide-flaws-exposing-developers-to-data-theft-and-rce
    label: "Tom's Hardware"

disputed: false
landmark: true
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# IDEsaster

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

## Summary

Researcher **Ari Marzouk (MaccariTA)**, a six-month investigation, 30+ vulnerabilities: **100% of the AI IDEs and coding assistants tested were affected**, at least **24 CVEs** plus an additional AWS advisory. Covers GitHub Copilot, Cursor, Windsurf, Kiro.dev, Zed.dev, Roo Code, Junie, Cline, Gemini CLI and Claude Code. The common pattern: place payloads in files the AI reads (repository config, code comments, issue descriptions, MCP tool responses) and direct the AI to **weaponize the IDE's legitimate features**

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
| 1 | THN | <https://thehackernews.com/2025/12/researchers-uncover-30-flaws-in-ai.html> |
| 2 | Tom's Hardware | <https://www.tomshardware.com/tech-industry/cyber-security/researchers-uncover-critical-ai-ide-flaws-exposing-developers-to-data-theft-and-rce> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-06` (raw: 2025-12-06, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape · [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-06-idesaster` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md) · [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-12-01` [MCP TypeScript SDK DNS rebinding](2025-12-01-mcp-typescript-sdk-dns.md)<br>  <sub>MCP TypeScript SDK DNS rebinding</sub>
- `2025-12-01` [Three CVEs in Anthropic's Git MCP Server](2025-12-01-anthropic-git-mcp-server.md)<br>  <sub>Three CVEs in Anthropic's Git MCP Server</sub>
- `2026-01-14` [Cursor allowlist bypass CVE-2026-22708](../2026-01/2026-01-14-cursor-bai-ming-dan-rao.md)<br>  <sub>Cursor allowlist bypass CVE-2026-22708</sub>
- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-06-idesaster.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
