---
id: 2026-05-12-claudebleed-claude-chrome
title: "ClaudeBleed: a zero-permission extension hijacks Claude for Chrome"
title_zh: "ClaudeBleed：零权限扩展劫持 Claude for Chrome"
title_ja: "ClaudeBleed：権限ゼロの拡張機能がClaude for Chromeをハイジャック"
title_ko: "ClaudeBleed: 권한 없는 확장 프로그램이 Claude for Chrome을 하이재킹"
title_de: "ClaudeBleed: Eine Erweiterung ohne Berechtigungen übernimmt Claude for Chrome"
title_fr: "ClaudeBleed : une extension sans permission détourne Claude for Chrome"
title_es: "ClaudeBleed: una extensión sin permisos secuestra Claude for Chrome"
date: 2026-05-12
date_precision: day
date_raw: "2026-05-12"

kind: research
type: [IPI, CRED]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The extension's code lets **any script on the same origin** communicate with the Claude LLM without validating the caller


summary_zh: |
  扩展代码允许**同源内任意脚本**与 Claude LLM 通信而不校验调用方

summary_ja: |
  拡張機能のコードが、呼び出し元を検証せずに**同一オリジン上のあらゆるスクリプト**をClaude LLMと通信させる

summary_ko: |
  확장 프로그램의 코드가 **같은 출처의 어떤 스크립트든** 호출자를 검증하지 않고 Claude LLM과 통신하게 허용했다

summary_de: |
  Der Code der Erweiterung erlaubt **jedem Skript derselben Origin**, mit dem Claude-LLM zu kommunizieren, ohne den Aufrufer zu validieren

summary_fr: |
  Le code de l'extension permet à **tout script de la même origine** de communiquer avec le LLM Claude sans valider l'appelant

summary_es: |
  El código de la extensión permite que **cualquier script del mismo origen** se comunique con el LLM de Claude sin validar al llamador

sources:
  - url: https://cyberscoop.com/claude-chrome-extension-allows-plugins-to-hijack-ai/
    label: CyberScoop

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# ClaudeBleed: a zero-permission extension hijacks Claude for Chrome

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

The extension's code lets **any script on the same origin** communicate with the Claude LLM without validating the caller

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credentials are abused<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CyberScoop | <https://cyberscoop.com/claude-chrome-extension-allows-plugins-to-hijack-ai/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-12` (raw: 2026-05-12, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-12-claudebleed-claude-chrome` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-12-claudebleed-claude-chrome.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
