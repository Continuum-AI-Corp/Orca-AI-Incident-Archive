---
id: 2025-07-21-claude-code-hooks-rce
title: "Claude Code hooks RCE"
title_zh: "Claude Code hooks RCE"
title_ja: "Claude Code hooksのRCE"
title_ko: "Claude Code hooks RCE"
title_de: "Claude Code Hooks: RCE"
title_fr: "RCE via les hooks de Claude Code"
title_es: "RCE en los hooks de Claude Code"
date: 2025-07-21
date_precision: day
date_raw: "2025-07-21"

kind: vulnerability
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A malicious `.claude/settings.json` runs shell on SessionStart — **cloning a repository is enough**. GHSA-ph6w-f82w-28w6, affects < 1.0.87, fixed 08-26


summary_zh: |
  恶意 `.claude/settings.json` 在 SessionStart 执行 shell —— **clone 一个仓库就中招**。GHSA-ph6w-f82w-28w6，影响 < 1.0.87，08-26 修复

summary_ja: |
  悪性の`.claude/settings.json`がSessionStartでシェルを実行する——**リポジトリをcloneするだけで成立**。GHSA-ph6w-f82w-28w6、1.0.87未満が対象、08-26に修正

summary_ko: |
  악성 `.claude/settings.json`은 SessionStart에서 셸을 실행한다 — **저장소를 클론하기만 하면 된다**. GHSA-ph6w-f82w-28w6, 1.0.87 미만 영향, 08-26 수정

summary_de: |
  Eine bösartige `.claude/settings.json` führt bei SessionStart eine Shell aus — **das Klonen eines Repositorys genügt**. GHSA-ph6w-f82w-28w6, betrifft < 1.0.87, behoben am 08-26

summary_fr: |
  Un `.claude/settings.json` malveillant exécute un shell au SessionStart — **cloner un dépôt suffit**. GHSA-ph6w-f82w-28w6, affecte les versions < 1.0.87, corrigé le 08-26

summary_es: |
  Un `.claude/settings.json` malicioso ejecuta shell en SessionStart — **basta con clonar un repositorio**. GHSA-ph6w-f82w-28w6, afecta a < 1.0.87, corregido el 08-26

sources:
  - url: https://github.com/advisories/GHSA-4fgq-fpq9-mr3g
    label: "GHSA-4fgq-fpq9-mr3g"
  - url: https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/
    label: Check Point

disputed: false
landmark: false
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# Claude Code hooks RCE

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

A malicious `.claude/settings.json` runs shell on SessionStart — **cloning a repository is enough**. GHSA-ph6w-f82w-28w6, affects < 1.0.87, fixed 08-26

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
| 1 | GHSA-4fgq-fpq9-mr3g | <https://github.com/advisories/GHSA-4fgq-fpq9-mr3g> |
| 2 | Check Point | <https://research.checkpoint.com/2026/rce-and-api-token-exfiltration-through-claude-code-project-files-cve-2025-59536/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-07-21` (raw: 2025-07-21, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-07-21-claude-code-hooks-rce` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-07-28` [Gemini CLI silent code execution](2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-08-01` [Cursor CurXecute (CVE-2025-54135)](../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>
- `2025-08-07` [OpenAI Codex CLI config hijack](../2025-08/2025-08-07-codex-cli-pei-zhi-jie.md)<br>  <sub>OpenAI Codex CLI config hijack</sub>
- `2025-03-01` [Manus AI leaks in-sandbox prompts and runtime code](../2025-03/2025-03-01-manus-sha-xiang-nei-ti.md)<br>  <sub>Manus AI leaks in-sandbox prompts and runtime code</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-21-claude-code-hooks-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
