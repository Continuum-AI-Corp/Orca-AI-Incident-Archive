---
id: 2025-12-01-anthropic-git-mcp-server
title: "Three CVEs in Anthropic's Git MCP Server"
title_zh: "Anthropic Git MCP Server 三连 CVE"
title_ja: "AnthropicのGit MCP Serverに3件のCVE"
title_ko: "Anthropic Git MCP 서버의 CVE 3건"
title_de: "Drei CVEs in Anthropics Git MCP-Server"
title_fr: "Trois CVE dans le Git MCP Server d'Anthropic"
title_es: "Tres CVE en el Git MCP Server de Anthropic"
date: 2025-12-01
date_precision: month
date_raw: "fixed 2025-12 / disclosed 2026-01"

kind: vulnerability
type: [MCP]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Anthropic **accepted the report in 2025-09, shipped fixes in 2025-12, went public in 2026-01**. CVE-2025-68143: `git_init` accepts an arbitrary filesystem path without validation, turning any directory into a git repository; CVE-2025-68145: the `--repository` restriction is not validated on subsequent calls, allowing access to any repository on the system; CVE-2025-68144: `git_diff` / `git_checkout` pass user-controllable arguments straight to GitPython. Combined with a filesystem MCP server, this allows executing code, deleting arbitrary files and stuffing arbitrary files into the LLM context


summary_zh: |
  Anthropic **2025-09 接受报告、2025-12 发布修复、2026-01 公开**。CVE-2025-68143：`git_init` 接受任意文件系统路径且不校验，可把任何目录变成 git 仓库；CVE-2025-68145：`--repository` 限定在后续调用中未被校验，可越界访问系统上任意仓库；CVE-2025-68144：`git_diff` / `git_checkout` 把用户可控参数直接传给 GitPython。与 filesystem MCP server 并用时可执行代码、删除任意文件、把任意文件塞进 LLM 上下文

summary_ja: |
  Anthropicは**2025-09に報告を受理、2025-12に修正をリリース、2026-01に公表**。CVE-2025-68143：`git_init`が任意のファイルシステムパスを検証なしに受け入れ、あらゆるディレクトリをgitリポジトリにしてしまう。CVE-2025-68145：`--repository`制限が後続の呼び出しで検証されず、システム上の任意のリポジトリにアクセスできる。CVE-2025-68144：`git_diff`／`git_checkout`がユーザー制御可能な引数をそのままGitPythonに渡す。ファイルシステムMCPサーバーと組み合わせると、コード実行、任意ファイルの削除、LLMコンテキストへの任意ファイルの詰め込みが可能になる

summary_ko: |
  Anthropic은 **2025-09에 보고를 접수하고 2025-12에 수정을 배포했으며 2026-01에 공개했다**. CVE-2025-68143: `git_init`이 검증 없이 임의의 파일 시스템 경로를 받아 어떤 디렉터리든 git 저장소로 만든다. CVE-2025-68145: `--repository` 제한이 후속 호출에서 검증되지 않아 시스템의 모든 저장소에 접근할 수 있다. CVE-2025-68144: `git_diff` / `git_checkout`이 사용자가 제어하는 인자를 그대로 GitPython에 전달한다. 파일 시스템 MCP 서버와 결합하면 코드 실행, 임의 파일 삭제, 임의 파일을 LLM 컨텍스트에 밀어 넣기가 가능하다

summary_de: |
  Anthropic **akzeptierte den Bericht im 2025-09, lieferte Korrekturen im 2025-12 aus und ging im 2026-01 an die Öffentlichkeit**. CVE-2025-68143: `git_init` akzeptiert einen beliebigen Dateisystempfad ohne Validierung und macht jedes Verzeichnis zu einem Git-Repository; CVE-2025-68145: Die `--repository`-Beschränkung wird bei Folgeaufrufen nicht validiert, was Zugriff auf jedes Repository im System erlaubt; CVE-2025-68144: `git_diff` / `git_checkout` geben nutzerkontrollierte Argumente direkt an GitPython weiter. Zusammen mit einem Filesystem-MCP-Server erlaubt dies das Ausführen von Code, das Löschen beliebiger Dateien und das Einschleusen beliebiger Dateien in den LLM-Kontext

summary_fr: |
  Anthropic **a accepté le rapport en 2025-09, livré les correctifs en 2025-12, communiqué publiquement en 2026-01**. CVE-2025-68143 : `git_init` accepte un chemin de système de fichiers arbitraire sans validation, transformant n'importe quel répertoire en dépôt git ; CVE-2025-68145 : la restriction `--repository` n'est pas validée lors des appels suivants, permettant d'accéder à n'importe quel dépôt du système ; CVE-2025-68144 : `git_diff` / `git_checkout` transmettent des arguments contrôlables par l'utilisateur directement à GitPython. Combiné à un serveur MCP de système de fichiers, cela permet d'exécuter du code, de supprimer des fichiers arbitraires et d'injecter des fichiers arbitraires dans le contexte du LLM

summary_es: |
  Anthropic **aceptó el informe en 2025-09, publicó las correcciones en 2025-12 y lo hizo público en 2026-01**. CVE-2025-68143: `git_init` acepta una ruta arbitraria del sistema de archivos sin validación, convirtiendo cualquier directorio en un repositorio git; CVE-2025-68145: la restricción `--repository` no se valida en llamadas posteriores, permitiendo el acceso a cualquier repositorio del sistema; CVE-2025-68144: `git_diff` / `git_checkout` pasan argumentos controlables por el usuario directamente a GitPython. Combinado con un servidor MCP de sistema de archivos, esto permite ejecutar código, borrar archivos arbitrarios e introducir archivos arbitrarios en el contexto del LLM

sources:
  - url: https://www.theregister.com/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059
    label: The Register
  - url: https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html
    label: THN

disputed: true
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# Three CVEs in Anthropic's Git MCP Server

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

Anthropic **accepted the report in 2025-09, shipped fixes in 2025-12, went public in 2026-01**. CVE-2025-68143: `git_init` accepts an arbitrary filesystem path without validation, turning any directory into a git repository; CVE-2025-68145: the `--repository` restriction is not validated on subsequent calls, allowing access to any repository on the system; CVE-2025-68144: `git_diff` / `git_checkout` pass user-controllable arguments straight to GitPython. Combined with a filesystem MCP server, this allows executing code, deleting arbitrary files and stuffing arbitrary files into the LLM context

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    I["Unauthorized tool calls<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | The Register | <https://www.theregister.com/security/2026/01/20/anthropic-quietly-fixed-flaws-in-its-git-mcp-server/4676059> |
| 2 | THN | <https://thehackernews.com/2026/01/three-flaws-in-anthropic-mcp-git-server.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-01` (raw: fixed 2025-12 / disclosed 2026-01, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-01-anthropic-git-mcp-server` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-12-06` [IDEsaster](2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>
- `2025-12-01` [MCP TypeScript SDK DNS rebinding](2025-12-01-mcp-typescript-sdk-dns.md)<br>  <sub>MCP TypeScript SDK DNS rebinding</sub>
- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-01` [Framelink Figma MCP RCE](../2025-10/2025-10-01-framelink-figma-mcp-rce.md)<br>  <sub>Framelink Figma MCP RCE</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-01-anthropic-git-mcp-server.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
