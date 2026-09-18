---
id: 2026-01-14-cursor-bai-ming-dan-rao
title: "Cursor allowlist bypass CVE-2026-22708"
title_zh: "Cursor 白名单绕过 CVE-2026-22708"
title_ja: "Cursorの許可リストバイパス CVE-2026-22708"
title_ko: "Cursor 허용 목록 우회 CVE-2026-22708"
title_de: "Cursor: Umgehung der Positivliste CVE-2026-22708"
title_fr: "Contournement de liste blanche dans Cursor (CVE-2026-22708)"
title_es: "Omisión de la lista de permitidos en Cursor, CVE-2026-22708"
date: 2026-01-14
date_precision: day
date_raw: "2026-01-14"

kind: research
type: [SANDBOX]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Pillar Security: in Auto-Run + Allowlist mode, **shell built-ins (`export`, `typeset`, `unset`, `set`, etc.) bypass allowlist validation entirely** — external commands are validated, but built-ins are let through because they are not standalone executables, **even when the user's allowlist is empty**. An attacker poisons the shell environment via direct or indirect prompt injection (setting / modifying / deleting environment variables that affect trusted commands), achieving both zero-click and one-click RCE. **Fixed in Cursor 2.3**, which now requires explicit approval for commands the server-side parser cannot classify


summary_zh: |
  Pillar Security：Auto-Run + Allowlist 模式下，**shell 内建命令（`export`、`typeset`、`unset`、`set` 等）完全绕过白名单校验** —— 外部命令会被校验，内建命令因为不是独立可执行文件而直接放行，**即使用户的白名单是空的**。攻击者经直接或间接提示注入投毒 shell 环境（设置/修改/删除影响可信命令的环境变量），达成零点击与一点击两种 RCE。**Cursor 2.3 修复**，现要求服务端解析器无法分类的命令必须显式批准

summary_ja: |
  Pillar Security：Auto-Run＋Allowlistモードでは、**シェルビルトイン（`export`、`typeset`、`unset`、`set`など）が許可リスト検証を完全にバイパスする**——外部コマンドは検証されるが、ビルトインは単体の実行ファイルではないため、**ユーザーの許可リストが空であっても**通ってしまう。攻撃者は直接または間接のプロンプトインジェクションでシェル環境を汚染し（信頼されたコマンドに影響する環境変数の設定／変更／削除）、ゼロクリックとワンクリックの両方のRCEを成立させる。**Cursor 2.3で修正**され、サーバー側パーサーが分類できないコマンドには明示的な承認が必要になった

summary_ko: |
  Pillar Security: Auto-Run + 허용 목록 모드에서 **셸 내장 명령(`export`, `typeset`, `unset`, `set` 등)이 허용 목록 검증을 완전히 우회한다** — 외부 명령은 검증되지만, 내장 명령은 독립 실행 파일이 아니라는 이유로 통과된다. **사용자의 허용 목록이 비어 있어도 마찬가지다**. 공격자는 직접 또는 간접 프롬프트 인젝션으로 셸 환경을 오염시켜(신뢰된 명령에 영향을 주는 환경 변수를 설정/수정/삭제) 제로클릭과 원클릭 RCE를 모두 달성한다. **Cursor 2.3에서 수정**되었으며, 이제 서버 측 파서가 분류할 수 없는 명령은 명시적 승인을 요구한다

summary_de: |
  Pillar Security: Im Modus Auto-Run + Allowlist **umgehen Shell-Built-ins (`export`, `typeset`, `unset`, `set` usw.) die Validierung der Positivliste vollständig** — externe Befehle werden validiert, Built-ins aber durchgelassen, weil sie keine eigenständigen Executables sind, **selbst wenn die Positivliste des Nutzers leer ist**. Ein Angreifer vergiftet die Shell-Umgebung per direkter oder indirekter Prompt-Injection (Setzen / Ändern / Löschen von Umgebungsvariablen, die vertrauenswürdige Befehle beeinflussen) und erreicht damit sowohl Zero-Click- als auch One-Click-RCE. **Behoben in Cursor 2.3**, das nun für Befehle, die der serverseitige Parser nicht klassifizieren kann, eine ausdrückliche Genehmigung verlangt

summary_fr: |
  Pillar Security : en mode Auto-Run + Allowlist, **les commandes internes du shell (`export`, `typeset`, `unset`, `set`, etc.) contournent entièrement la validation de liste blanche** — les commandes externes sont validées, mais les commandes internes passent car ce ne sont pas des exécutables autonomes, **même quand la liste blanche de l'utilisateur est vide**. Un attaquant empoisonne l'environnement du shell via une injection de prompt directe ou indirecte (définir / modifier / supprimer des variables d'environnement qui influent sur des commandes de confiance), obtenant un RCE zero-click et one-click. **Corrigé dans Cursor 2.3**, qui exige désormais une approbation explicite pour les commandes que l'analyseur côté serveur ne peut pas classer

summary_es: |
  Pillar Security: en el modo Auto-Run + Allowlist, **los comandos internos del shell (`export`, `typeset`, `unset`, `set`, etc.) omiten por completo la validación de la lista de permitidos** — los comandos externos se validan, pero los internos se dejan pasar porque no son ejecutables independientes, **incluso cuando la lista de permitidos del usuario está vacía**. Un atacante envenena el entorno del shell mediante inyección de prompt directa o indirecta (estableciendo / modificando / eliminando variables de entorno que afectan a comandos de confianza), logrando RCE tanto con cero clics como con un clic. **Corregido en Cursor 2.3**, que ahora exige aprobación explícita para los comandos que el analizador del lado del servidor no puede clasificar

sources:
  - url: https://www.pillar.security/blog/the-agent-security-paradox-when-trusted-commands-in-cursor-become-attack-vectors
    label: Pillar Security
  - url: https://www.scworld.com/news/cursor-vulnerability-enables-stealthy-rce-via-indirect-prompt-injection
    label: SC Media

disputed: false
landmark: false
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# Cursor allowlist bypass CVE-2026-22708

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Pillar Security: in Auto-Run + Allowlist mode, **shell built-ins (`export`, `typeset`, `unset`, `set`, etc.) bypass allowlist validation entirely** — external commands are validated, but built-ins are let through because they are not standalone executables, **even when the user's allowlist is empty**. An attacker poisons the shell environment via direct or indirect prompt injection (setting / modifying / deleting environment variables that affect trusted commands), achieving both zero-click and one-click RCE. **Fixed in Cursor 2.3**, which now requires explicit approval for commands the server-side parser cannot classify

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["A leftover egress path"]:::step
    I["Escape into the real system<br/><i>(lab demo · no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Pillar Security | <https://www.pillar.security/blog/the-agent-security-paradox-when-trusted-commands-in-cursor-become-attack-vectors> |
| 2 | SC Media | <https://www.scworld.com/news/cursor-vulnerability-enables-stealthy-rce-via-indirect-prompt-injection> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-14` (raw: 2026-01-14, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-14-cursor-bai-ming-dan-rao` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-02-27` [Check Point publishes two Claude Code CVEs](../2026-02/2026-02-27-check-point-claude-code.md)<br>  <sub>Check Point publishes two Claude Code CVEs</sub>
- `2025-12-06` [IDEsaster](../2025-12/2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>
- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](../2026-04/2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](../2026-04/2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-14-cursor-bai-ming-dan-rao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
