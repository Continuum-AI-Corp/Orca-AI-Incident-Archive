---
id: 2025-10-02-cometjacking
title: "CometJacking"
title_zh: "CometJacking"
title_ja: "CometJacking"
title_ko: "CometJacking"
title_de: "CometJacking"
title_fr: "CometJacking"
title_es: "CometJacking"
date: 2025-10-02
date_precision: day
date_raw: "2025-10-02"

kind: research
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  LayerX: the `collection` parameter in a URL alone can carry instructions, making Perplexity Comet look up **memories and connected services** (Gmail, Calendar) and exfiltrate them, **with no credentials or user interaction**. Reported to Perplexity on 2025-08-27/28; its first response was "no security impact"


summary_zh: |
  LayerX：URL 的 `collection` 参数即可携带指令，让 Perplexity Comet 去查**记忆和已连接服务**（Gmail、日历）并外带，**无需凭据或用户交互**。2025-08-27/28 报告 Perplexity，初次回应「无安全影响」

summary_ja: |
  LayerX：URL内の`collection`パラメータだけで指示を運ぶことができ、Perplexity Cometに**メモリと連携サービス**（Gmail、カレンダー）を検索させて外部送信させる——**認証情報もユーザー操作も不要**。2025-08-27/28にPerplexityへ報告。最初の回答は「セキュリティ上の影響はない」だった

summary_ko: |
  LayerX: URL의 `collection` 매개변수만으로 지시를 전달할 수 있어, Perplexity Comet이 **메모리와 연결된 서비스**(Gmail, Calendar)를 조회해 유출하게 만들 수 있다. **자격 증명도 사용자 상호작용도 필요 없다**. 2025-08-27/28 Perplexity에 신고했고, 첫 응답은 "보안 영향 없음"이었다

summary_de: |
  LayerX: Allein der `collection`-Parameter in einer URL kann Anweisungen transportieren, wodurch Perplexity Comet **Erinnerungen und verbundene Dienste** (Gmail, Kalender) nachschlägt und sie exfiltriert — **ohne Zugangsdaten oder Nutzerinteraktion**. Am 2025-08-27/28 an Perplexity gemeldet; die erste Antwort lautete „keine Sicherheitsauswirkung“

summary_fr: |
  LayerX : le paramètre `collection` d'une URL suffit à transporter des instructions, amenant Perplexity Comet à consulter les **mémoires et services connectés** (Gmail, Calendar) et à les exfiltrer, **sans identifiants ni interaction de l'utilisateur**. Signalé à Perplexity les 2025-08-27/28 ; sa première réponse a été « aucun impact de sécurité »

summary_es: |
  LayerX: el parámetro `collection` de una URL por sí solo puede transportar instrucciones, haciendo que Perplexity Comet busque **recuerdos y servicios conectados** (Gmail, Calendar) y los exfiltre, **sin credenciales ni interacción del usuario**. Reportado a Perplexity el 2025-08-27/28; su primera respuesta fue "sin impacto de seguridad"

sources:
  - url: https://ppc.land/comet-browser-faces-multiple-security-vulnerabilities-from-prompt-injection/
    label: PPC Land roundup

disputed: false
landmark: true
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# CometJacking

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

LayerX: the `collection` parameter in a URL alone can carry instructions, making Perplexity Comet look up **memories and connected services** (Gmail, Calendar) and exfiltrate them, **with no credentials or user interaction**. Reported to Perplexity on 2025-08-27/28; its first response was "no security impact"

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | PPC Land roundup | <https://ppc.land/comet-browser-faces-multiple-security-vulnerabilities-from-prompt-injection/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-02` (raw: 2025-10-02, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-02-cometjacking` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-02-cometjacking.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
