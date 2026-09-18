---
id: 2025-07-28-gemini-cli-jing-mo-dai
title: "Gemini CLI silent code execution"
title_zh: "Gemini CLI 静默代码执行"
title_ja: "Gemini CLIのサイレントなコード実行"
title_ko: "Gemini CLI 무음 코드 실행"
title_de: "Gemini CLI: stilles Ausführen von Code"
title_fr: "Exécution de code silencieuse dans Gemini CLI"
title_es: "Ejecución silenciosa de código en Gemini CLI"
date: 2025-07-28
date_precision: day
date_raw: "2025-07-28"

kind: research
type: [SANDBOX]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Tracebit: a whitelisted-command validation flaw plus misleading UI could execute arbitrary commands without the user's knowledge


summary_zh: |
  Tracebit：白名单命令校验缺陷 + UI 误导，可在用户不知情下执行任意命令

summary_ja: |
  Tracebit：ホワイトリストコマンドの検証不備と誤解を招くUIにより、ユーザーに気づかれずに任意のコマンドを実行できた

summary_ko: |
  Tracebit: 허용 목록 명령 검증 결함과 오해를 유발하는 UI가 결합해 사용자가 모르는 사이에 임의 명령을 실행할 수 있었다

summary_de: |
  Tracebit: Ein Validierungsfehler bei der Positivliste von Befehlen plus eine irreführende UI konnten beliebige Befehle ohne Wissen des Nutzers ausführen

summary_fr: |
  Tracebit : une faille de validation des commandes en liste blanche, combinée à une interface trompeuse, permettait d'exécuter des commandes arbitraires à l'insu de l'utilisateur

summary_es: |
  Tracebit: un fallo de validación de comandos en la lista blanca más una interfaz engañosa podían ejecutar comandos arbitrarios sin conocimiento del usuario

sources:
  - url: https://rafter.so/blog/incidents/ai-agent-security-timeline-2025-2026
    label: Rafter timeline

disputed: false
landmark: false
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# Gemini CLI silent code execution

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Tracebit: a whitelisted-command validation flaw plus misleading UI could execute arbitrary commands without the user's knowledge

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
| 1 | Rafter timeline | <https://rafter.so/blog/incidents/ai-agent-security-timeline-2025-2026> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-07-28` (raw: 2025-07-28, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-07-28-gemini-cli-jing-mo-dai` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-07-21` [Claude Code hooks RCE](2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-08-01` [Cursor CurXecute (CVE-2025-54135)](../2025-08/2025-08-01-cursor-curxecute.md)<br>  <sub>Cursor CurXecute (CVE-2025-54135)</sub>
- `2025-08-07` [OpenAI Codex CLI config hijack](../2025-08/2025-08-07-codex-cli-pei-zhi-jie.md)<br>  <sub>OpenAI Codex CLI config hijack</sub>
- `2025-03-01` [Manus AI leaks in-sandbox prompts and runtime code](../2025-03/2025-03-01-manus-sha-xiang-nei-ti.md)<br>  <sub>Manus AI leaks in-sandbox prompts and runtime code</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
