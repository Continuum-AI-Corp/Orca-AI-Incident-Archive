---
id: 2025-10-08-camoleak-github-copilot-chat
title: "CamoLeak (GitHub Copilot Chat)"
title_zh: "CamoLeak（GitHub Copilot Chat）"
title_ja: "CamoLeak（GitHub Copilot Chat）"
title_ko: "CamoLeak (GitHub Copilot Chat)"
title_de: "CamoLeak (GitHub Copilot Chat)"
title_fr: "CamoLeak (GitHub Copilot Chat)"
title_es: "CamoLeak (GitHub Copilot Chat)"
date: 2025-10-08
date_precision: day
date_raw: "2025-10-08"

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Legit Security (Omer Mayraz), **CVSS 9.6**. A **hidden HTML comment** in a PR description lures Copilot into exfiltrating private repository source code, API keys and undisclosed vulnerabilities character by character through **GitHub's own Camo image proxy**. Found in 2025-06; GitHub mitigated it by **disabling image rendering in Copilot Chat on 08-14**, disclosed in October


summary_zh: |
  Legit Security（Omer Mayraz），**CVSS 9.6**。PR 描述里的**隐藏 HTML 注释**诱导 Copilot，经 **GitHub 自家的 Camo 图片代理**逐字符编码外带私有仓库源码、API key、未披露漏洞。2025-06 发现，GitHub **08-14 通过关闭 Copilot Chat 的图片渲染**缓解，10 月公开

summary_ja: |
  Legit Security（Omer Mayraz氏）、**CVSS 9.6**。PR説明文に**隠されたHTMLコメント**がCopilotを誘導し、非公開リポジトリのソースコード、APIキー、未公開の脆弱性を**GitHub自身のCamo画像プロキシ**経由で1文字ずつ外部送信させる。2025-06に発見。GitHubは**08-14にCopilot Chatでの画像レンダリングを無効化**して緩和し、10月に公表

summary_ko: |
  Legit Security(Omer Mayraz), **CVSS 9.6**. PR 설명에 있는 **숨겨진 HTML 주석**이 Copilot을 유인해 **GitHub 자체의 Camo 이미지 프록시**를 통해 비공개 저장소 소스 코드, API 키, 미공개 취약점을 한 글자씩 유출하게 만들었다. 2025-06에 발견되었고 GitHub은 **08-14 Copilot Chat의 이미지 렌더링을 비활성화**해 완화했으며, 10월에 공개했다

summary_de: |
  Legit Security (Omer Mayraz), **CVSS 9.6**. Ein **versteckter HTML-Kommentar** in einer PR-Beschreibung verleitet Copilot dazu, privaten Repository-Quellcode, API-Schlüssel und nicht offengelegte Schwachstellen Zeichen für Zeichen über **GitHubs eigenen Camo-Bildproxy** zu exfiltrieren. Gefunden im 2025-06; GitHub entschärfte es, indem **am 08-14 das Bild-Rendering in Copilot Chat deaktiviert wurde**; offengelegt im Oktober

summary_fr: |
  Legit Security (Omer Mayraz), **CVSS 9.6**. Un **commentaire HTML caché** dans la description d'une PR incite Copilot à exfiltrer le code source privé d'un dépôt, des clés API et des vulnérabilités non divulguées, caractère par caractère, via **le proxy d'images Camo de GitHub lui-même**. Découvert en 2025-06 ; GitHub l'a atténué en **désactivant le rendu d'images dans Copilot Chat le 08-14**, divulgué en octobre

summary_es: |
  Legit Security (Omer Mayraz), **CVSS 9.6**. Un **comentario HTML oculto** en la descripción de un PR atrae a Copilot para que exfiltre código fuente de repositorios privados, claves de API y vulnerabilidades no divulgadas carácter por carácter a través del **propio proxy de imágenes Camo de GitHub**. Encontrado en 2025-06; GitHub lo mitigó **desactivando el renderizado de imágenes en Copilot Chat el 08-14**, divulgado en octubre

sources:
  - url: https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code
    label: Legit Security

disputed: false
landmark: true
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# CamoLeak (GitHub Copilot Chat)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Legit Security (Omer Mayraz), **CVSS 9.6**. A **hidden HTML comment** in a PR description lures Copilot into exfiltrating private repository source code, API keys and undisclosed vulnerabilities character by character through **GitHub's own Camo image proxy**. Found in 2025-06; GitHub mitigated it by **disabling image rendering in Copilot Chat on 08-14**, disclosed in October

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Legit Security | <https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-08` (raw: 2025-10-08, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-08-camoleak-github-copilot-chat` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>Shadow Escape: first zero-click agent attack over MCP</sub>
- `2025-10-02` [CometJacking](2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-08-camoleak-github-copilot-chat.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
