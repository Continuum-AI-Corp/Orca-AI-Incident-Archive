---
id: 2025-08-07-codex-cli-pei-zhi-jie
title: "OpenAI Codex CLI config hijack"
title_zh: "OpenAI Codex CLI 配置劫持"
title_ja: "OpenAI Codex CLIの設定ハイジャック"
title_ko: "OpenAI Codex CLI 설정 하이재킹"
title_de: "OpenAI Codex CLI: Konfigurations-Hijacking"
title_fr: "Détournement de configuration de la CLI OpenAI Codex"
title_es: "Secuestro de configuración en OpenAI Codex CLI"
date: 2025-08-07
date_precision: day
date_raw: "2025-08-07"

kind: vulnerability
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2025-61260, CVSS 9.8. Codex automatically loads project-local `.env` and `.codex/config.toml` without user confirmation, so they can embed arbitrary commands that execute immediately. Affects ≤ v0.23.0, fixed 08-20


summary_zh: |
  CVE-2025-61260，CVSS 9.8。Codex 自动加载项目本地 `.env` 与 `.codex/config.toml` 而不需用户确认，可嵌入立即执行的任意命令。影响 ≤ v0.23.0，08-20 修复

summary_ja: |
  CVE-2025-61260、CVSS 9.8。Codexはユーザーの確認なしにプロジェクト内の`.env`と`.codex/config.toml`を自動読み込みするため、任意のコマンドを埋め込むと即座に実行される。v0.23.0以下が対象、08-20に修正

summary_ko: |
  CVE-2025-61260, CVSS 9.8. Codex는 사용자 확인 없이 프로젝트 로컬 `.env`와 `.codex/config.toml`을 자동으로 로드하므로, 여기에 즉시 실행되는 임의 명령을 넣을 수 있었다. v0.23.0 이하 영향, 08-20 수정

summary_de: |
  CVE-2025-61260, CVSS 9.8. Codex lädt projektlokale `.env` und `.codex/config.toml` ohne Nutzerbestätigung automatisch, sodass beliebige Befehle eingebettet werden können, die sofort ausgeführt werden. Betrifft ≤ v0.23.0, behoben am 08-20

summary_fr: |
  CVE-2025-61260, CVSS 9.8. Codex charge automatiquement les fichiers projet `.env` et `.codex/config.toml` sans confirmation de l'utilisateur, qui peuvent donc contenir des commandes arbitraires exécutées immédiatement. Affecte ≤ v0.23.0, corrigé le 08-20

summary_es: |
  CVE-2025-61260, CVSS 9.8. Codex carga automáticamente `.env` y `.codex/config.toml` locales del proyecto sin confirmación del usuario, por lo que pueden incrustar comandos arbitrarios que se ejecutan de inmediato. Afecta a ≤ v0.23.0, corregido el 08-20

sources:
  - url: https://github.com/advisories/GHSA-xrxf-jgv3-qmrm
    label: "GHSA-xrxf-jgv3-qmrm"

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# OpenAI Codex CLI config hijack

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

CVE-2025-61260, CVSS 9.8. Codex automatically loads project-local `.env` and `.codex/config.toml` without user confirmation, so they can embed arbitrary commands that execute immediately. Affects ≤ v0.23.0, fixed 08-20

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GHSA-xrxf-jgv3-qmrm | <https://github.com/advisories/GHSA-xrxf-jgv3-qmrm> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-07` (raw: 2025-08-07, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-07-codex-cli-pei-zhi-jie` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-08-01` [Cursor CurXecute (CVE-2025-54135)](2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>
- `2025-07-21` [Claude Code hooks RCE](../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI silent code execution](../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-12-06` [IDEsaster](../2025-12/2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-07-codex-cli-pei-zhi-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
