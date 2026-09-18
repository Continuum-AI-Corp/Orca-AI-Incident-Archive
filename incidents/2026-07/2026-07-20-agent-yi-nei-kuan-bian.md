---
id: 2026-07-20-agent-yi-nei-kuan-bian
title: "Six sandbox escapes across four coding agents in one week"
title_zh: "一周内 4 款编码 agent 爆 6 个沙箱逃逸"
title_ja: "1週間で4つのコーディングエージェントに6件のサンドボックス脱出"
title_ko: "일주일 만에 코딩 에이전트 4종에서 샌드박스 탈출 6건"
title_de: "Sechs Sandbox-Escapes über vier Coding-Agenten in einer Woche"
title_fr: "Six évasions de bac à sable sur quatre agents de code en une semaine"
title_es: "Seis escapes de sandbox en cuatro agentes de código en una semana"
date: 2026-07-20
date_precision: day
date_raw: "2026-07-20"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Pillar Security: Cursor, OpenAI Codex CLI, Google Gemini CLI and Google Antigravity. The common pattern: **the agent dutifully stays inside its limits, but rewrites files the host will later trust and execute** — the Docker socket (shared by three vendors, GHSA-v4xv-rqh3-w9mc), Cursor's virtualenv interpreter (GHSA-p9g2-cr55-cw9c), Git fsmonitor, the workspace `.claude` hook configuration (CVE-2026-48124), Codex CLI's allowlist that trusts command names without checking arguments, and Antigravity's macOS Seatbelt denylist bypass plus a `.vscode` task-configuration bypass of safe mode. Fixed in Cursor 3.0.0 / Codex CLI v0.95.0; Google treats them as ordinary vulnerabilities but argues they require social engineering or a trusted-repository precondition. **No in-the-wild exploitation reported**


summary_zh: |
  Pillar Security：Cursor、OpenAI Codex CLI、Google Gemini CLI、Google Antigravity。共同模式：**agent 自己老实待在限制内，但改写了宿主之后会信任并执行的文件** —— Docker socket（三家共有，GHSA-v4xv-rqh3-w9mc）、Cursor 的 virtualenv 解释器（GHSA-p9g2-cr55-cw9c）、Git fsmonitor、工作区 `.claude` hook 配置（CVE-2026-48124）、Codex CLI 只信命令名不查参数的白名单、Antigravity 的 macOS Seatbelt 拒绝列表绕过与 `.vscode` 任务配置绕过安全模式。Cursor 3.0.0 / Codex CLI v0.95.0 修复；Google 视为普通漏洞但认为需社工或仓库信任前提。**无在野利用报告**

summary_ja: |
  Pillar Security：Cursor、OpenAI Codex CLI、Google Gemini CLI、Google Antigravity。共通パターン：**エージェントは律儀に制限内にとどまるが、ホストが後で信頼して実行するファイルを書き換えてしまう**——Dockerソケット（3ベンダーが共有、GHSA-v4xv-rqh3-w9mc）、Cursorのvirtualenvインタープリター（GHSA-p9g2-cr55-cw9c）、Git fsmonitor、ワークスペースの`.claude`フック設定（CVE-2026-48124）、引数を検証せずコマンド名を信頼するCodex CLIの許可リスト、AntigravityのmacOS Seatbelt拒否リストのバイパスと`.vscode`タスク設定によるセーフモードのバイパス。Cursor 3.0.0／Codex CLI v0.95.0で修正。Googleは通常の脆弱性として扱うが、ソーシャルエンジニアリングか信頼されたリポジトリという前提条件が必要だと主張している。**実悪用の報告はなし**

summary_ko: |
  Pillar Security: Cursor, OpenAI Codex CLI, Google Gemini CLI, Google Antigravity. 공통 패턴: **에이전트는 한계 안에 얌전히 머무르지만, 호스트가 나중에 신뢰해 실행할 파일을 재작성한다** — Docker 소켓(세 벤더가 공유, GHSA-v4xv-rqh3-w9mc), Cursor의 virtualenv 인터프리터(GHSA-p9g2-cr55-cw9c), Git fsmonitor, 워크스페이스 `.claude` 훅 설정(CVE-2026-48124), 인자를 확인하지 않고 명령 이름만 신뢰하는 Codex CLI의 허용 목록, Antigravity의 macOS Seatbelt 거부 목록 우회와 `.vscode` 작업 설정을 통한 안전 모드 우회가 포함된다. Cursor 3.0.0 / Codex CLI v0.95.0에서 수정되었고, Google은 이를 일반 취약점으로 취급하면서도 소셜 엔지니어링이나 신뢰된 저장소 전제 조건이 필요하다고 주장한다. **실제 악용 보고는 없다**

summary_de: |
  Pillar Security: Cursor, OpenAI Codex CLI, Google Gemini CLI und Google Antigravity. Das gemeinsame Muster: **Der Agent bleibt brav innerhalb seiner Grenzen, schreibt aber Dateien um, denen der Host später vertraut und die er ausführt** — der Docker-Socket (von drei Anbietern geteilt, GHSA-v4xv-rqh3-w9mc), Cursors virtualenv-Interpreter (GHSA-p9g2-cr55-cw9c), Git fsmonitor, die `.claude`-Hook-Konfiguration im Workspace (CVE-2026-48124), die Positivliste der Codex CLI, die Befehlsnamen vertraut, ohne Argumente zu prüfen, und bei Antigravity die Umgehung der macOS-Seatbelt-Denylist plus die Umgehung des sicheren Modus über eine `.vscode`-Taskkonfiguration. Behoben in Cursor 3.0.0 / Codex CLI v0.95.0; Google behandelt sie als gewöhnliche Schwachstellen, argumentiert aber, sie erforderten Social Engineering oder ein vertrauenswürdiges Repository als Vorbedingung. **Keine Ausnutzung in freier Wildbahn gemeldet**

summary_fr: |
  Pillar Security : Cursor, OpenAI Codex CLI, Google Gemini CLI et Google Antigravity. Le schéma commun : **l'agent reste sagement dans ses limites, mais réécrit des fichiers que l'hôte fera ensuite confiance et exécutera** — le socket Docker (partagé par trois fournisseurs, GHSA-v4xv-rqh3-w9mc), l'interpréteur virtualenv de Cursor (GHSA-p9g2-cr55-cw9c), Git fsmonitor, la configuration de hook `.claude` de l'espace de travail (CVE-2026-48124), la liste blanche de Codex CLI qui fait confiance aux noms de commandes sans vérifier les arguments, et le contournement de la liste de refus Seatbelt de macOS d'Antigravity plus un contournement du mode sûr via la configuration de tâches `.vscode`. Corrigés dans Cursor 3.0.0 / Codex CLI v0.95.0 ; Google les traite comme des vulnérabilités ordinaires mais argue qu'elles exigent de l'ingénierie sociale ou une précondition de dépôt de confiance. **Aucune exploitation en conditions réelles signalée**

summary_es: |
  Pillar Security: Cursor, OpenAI Codex CLI, Google Gemini CLI y Google Antigravity. El patrón común: **el agente se mantiene obedientemente dentro de sus límites, pero reescribe archivos en los que el host confiará y ejecutará más tarde** — el socket de Docker (compartido por tres proveedores, GHSA-v4xv-rqh3-w9mc), el intérprete de virtualenv de Cursor (GHSA-p9g2-cr55-cw9c), Git fsmonitor, la configuración de hooks `.claude` del espacio de trabajo (CVE-2026-48124), la lista de permitidos de Codex CLI que confía en los nombres de comando sin comprobar los argumentos, y la elusión de la lista de denegación del Seatbelt de macOS de Antigravity más una elusión del modo seguro mediante la configuración de tareas de `.vscode`. Corregidos en Cursor 3.0.0 / Codex CLI v0.95.0; Google los trata como vulnerabilidades ordinarias pero sostiene que requieren ingeniería social o la precondición de un repositorio de confianza. **No se han reportado explotaciones en entornos reales**

sources:
  - url: https://www.pillar.security/blog/the-week-of-sandbox-escapes
    label: Pillar Security
  - url: https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/
    label: BleepingComputer

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Six sandbox escapes across four coding agents in one week

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Pillar Security: Cursor, OpenAI Codex CLI, Google Gemini CLI and Google Antigravity. The common pattern: **the agent dutifully stays inside its limits, but rewrites files the host will later trust and execute** — the Docker socket (shared by three vendors, GHSA-v4xv-rqh3-w9mc), Cursor's virtualenv interpreter (GHSA-p9g2-cr55-cw9c), Git fsmonitor, the workspace `.claude` hook configuration (CVE-2026-48124), Codex CLI's allowlist that trusts command names without checking arguments, and Antigravity's macOS Seatbelt denylist bypass plus a `.vscode` task-configuration bypass of safe mode. Fixed in Cursor 3.0.0 / Codex CLI v0.95.0; Google treats them as ordinary vulnerabilities but argues they require social engineering or a trusted-repository precondition. **No in-the-wild exploitation reported**

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
| 1 | Pillar Security | <https://www.pillar.security/blog/the-week-of-sandbox-escapes> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/cursor-codex-gemini-cli-antigravity-hit-by-sandbox-escapes/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-20` (raw: 2026-07-20, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-20-agent-yi-nei-kuan-bian` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-22` [SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host](2026-07-22-sharedroot-claude-cowork-linux.md)<br>  <sub>SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-20-agent-yi-nei-kuan-bian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
