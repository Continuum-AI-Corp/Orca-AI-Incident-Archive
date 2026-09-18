---
id: 2025-08-01-cursor-curxecute
title: "Cursor CurXecute (CVE-2025-54135)"
title_zh: "Cursor CurXecute（CVE-2025-54135）"
title_ja: "Cursor CurXecute（CVE-2025-54135）"
title_ko: "Cursor CurXecute (CVE-2025-54135)"
title_de: "Cursor CurXecute (CVE-2025-54135)"
title_fr: "Cursor CurXecute (CVE-2025-54135)"
title_es: "Cursor CurXecute (CVE-2025-54135)"
date: 2025-08-01
date_precision: day
date_raw: "2025-08-01"

kind: vulnerability
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Disclosed by Aim Security (v1 misattributed it to Check Point)**. Cursor runs with developer privileges; combined with an MCP server that pulls untrusted external data, poisoned data is enough to gain full RCE under the user's privileges


summary_zh: |
  **由 Aim Security 披露（v1 误记为 Check Point）**。Cursor 以开发者权限运行，配合会拉取不可信外部数据的 MCP server，投毒数据即可取得用户权限下的完整 RCE

summary_ja: |
  **Aim Securityが公表（v1では誤ってCheck Pointに帰属）**。Cursorは開発者権限で動作するため、信頼できない外部データを取り込むMCPサーバーと組み合わせると、汚染されたデータだけでユーザー権限での完全なRCEが成立する

summary_ko: |
  **Aim Security가 공개했다(v1에서는 Check Point로 잘못 귀속했다)**. Cursor는 개발자 권한으로 실행되므로, 신뢰할 수 없는 외부 데이터를 가져오는 MCP 서버와 결합하면 오염된 데이터만으로 사용자 권한의 완전한 RCE를 얻을 수 있다

summary_de: |
  **Offengelegt von Aim Security (in v1 fälschlich Check Point zugeschrieben)**. Cursor läuft mit Entwicklerrechten; zusammen mit einem MCP-Server, der nicht vertrauenswürdige externe Daten bezieht, genügen vergiftete Daten, um vollständige RCE unter den Rechten des Nutzers zu erlangen

summary_fr: |
  **Divulguée par Aim Security (la v1 l'attribuait à tort à Check Point)**. Cursor s'exécute avec les privilèges du développeur ; combiné à un serveur MCP qui récupère des données externes non fiables, des données empoisonnées suffisent à obtenir un RCE complet sous les privilèges de l'utilisateur

summary_es: |
  **Divulgado por Aim Security (la v1 lo atribuyó erróneamente a Check Point)**. Cursor se ejecuta con privilegios de desarrollador; combinado con un servidor MCP que extrae datos externos no confiables, datos envenenados bastan para obtener RCE total con los privilegios del usuario

sources:
  - url: https://www.tenable.com/blog/faq-cve-2025-54135-cve-2025-54136-vulnerabilities-in-cursor-curxecute-mcpoison
    label: Tenable FAQ

disputed: true
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Cursor CurXecute (CVE-2025-54135)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

**Disclosed by Aim Security (v1 misattributed it to Check Point)**. Cursor runs with developer privileges; combined with an MCP server that pulls untrusted external data, poisoned data is enough to gain full RCE under the user's privileges

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
| 1 | Tenable FAQ | <https://www.tenable.com/blog/faq-cve-2025-54135-cve-2025-54136-vulnerabilities-in-cursor-curxecute-mcpoison> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-01` (raw: 2025-08-01, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-08-01-cursor-curxecute` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2025-08-07` [OpenAI Codex CLI config hijack](2025-08-07-codex-cli-pei-zhi-jie.md)<br>  <sub>OpenAI Codex CLI config hijack</sub>
- `2025-07-21` [Claude Code hooks RCE](../2025-07/2025-07-21-claude-code-hooks-rce.md)<br>  <sub>Claude Code hooks RCE</sub>
- `2025-07-28` [Gemini CLI silent code execution](../2025-07/2025-07-28-gemini-cli-jing-mo-dai.md)<br>  <sub>Gemini CLI silent code execution</sub>
- `2025-12-06` [IDEsaster](../2025-12/2025-12-06-idesaster.md)<br>  <sub>IDEsaster</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-01-cursor-curxecute.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
