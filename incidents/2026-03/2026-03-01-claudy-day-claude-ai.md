---
id: 2026-03-01-claudy-day-claude-ai
title: "Claudy Day: a three-flaw chain in claude.ai"
title_zh: "Claudy Day：claude.ai 三漏洞链"
title_ja: "Claudy Day：claude.aiにおける3つの欠陥の連鎖"
title_ko: "Claudy Day: claude.ai의 세 가지 결함 연쇄"
title_de: "Claudy Day: eine Kette aus drei Schwachstellen in claude.ai"
title_fr: "Claudy Day : une chaîne de trois failles dans claude.ai"
title_es: "Claudy Day: una cadena de tres fallos en claude.ai"
date: 2026-03-01
date_precision: month
date_raw: "2026-03"

kind: incident
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The full attack pipeline disclosed by Oasis Security, chained from three flaws: (1) invisible prompt injection on claude.ai via a **URL parameter**, (2) a data exfiltration channel through the **Anthropic Files API**, and (3) an **open redirect** on claude.ai.
  Delivery was by **buying Google ads** — the ads showed a trusted claude.com link but took users to a poisoned redirect point and then into a crafted `claude.ai/new?q=` URL that silently exfiltrated sensitive data from the user's conversation history.
  ⚠️ **The most notable point: no integration, tool or MCP server is required — this hits the out-of-the-box default claude.ai session**. The prompt injection part has been fixed; the rest is being handled
  ⚠️ v2 was mistakenly placed on 2026-05-27; v3 corrects it to the Oasis disclosure date


summary_zh: |
  Oasis Security 披露的完整攻击流水线，由三个漏洞串成：① claude.ai 上经 **URL 参数**的隐形提示注入 ② 经 **Anthropic Files API** 的数据外带通道 ③ claude.ai 上的**开放重定向**。
  投递方式是**买 Google 广告** —— 广告显示的是可信的 claude.com 链接，实际把用户导到被投毒的跳转点，再送进特制的 `claude.ai/new?q=` URL，静默外带用户对话历史中的敏感数据。
  ⚠️ **最值得注意的一点：不需要任何集成、工具或 MCP server —— 打的是开箱即用的默认 claude.ai 会话**。提示注入部分已修复，其余在处理中
  ⚠️ v2 曾误置于 2026-05-27，v3 已按 Oasis 披露时间更正

summary_ja: |
  Oasis Securityが公表した攻撃パイプライン全体で、3つの欠陥を連鎖させた：(1) **URLパラメータ**経由のclaude.aiへの不可視プロンプトインジェクション、(2) **Anthropic Files API**を通じたデータ外部送信チャネル、(3) claude.aiの**オープンリダイレクト**。
  配信は**Google広告の購入**による——広告は信頼できるclaude.comのリンクを表示しながら、ユーザーを汚染されたリダイレクト地点へ導き、細工された`claude.ai/new?q=` URLへ送り込み、ユーザーの会話履歴から機密データを静かに外部送信させた。
  ⚠️ **最も注目すべき点：連携もツールもMCPサーバーも不要——初期状態のデフォルトのclaude.aiセッションで成立する**。プロンプトインジェクション部分は修正済み、残りは対応中。
  ⚠️ v2は誤って2026-05-27に配置されていた。v3でOasisの公表日へ修正

summary_ko: |
  Oasis Security가 공개한 전체 공격 파이프라인으로, 세 결함이 연쇄된다: (1) **URL 매개변수**를 통한 claude.ai의 보이지 않는 프롬프트 인젝션, (2) **Anthropic Files API**를 통한 데이터 유출 채널, (3) claude.ai의 **오픈 리다이렉트**.
  전달 수단은 **구글 광고 구매**였다 — 광고는 신뢰할 만한 claude.com 링크를 보여주지만 사용자를 오염된 리다이렉트 지점으로 보낸 뒤 조작된 `claude.ai/new?q=` URL로 유도해 대화 기록의 민감 데이터를 조용히 유출했다.
  ⚠️ **가장 주목할 점: 통합, 도구, MCP 서버가 전혀 필요 없다 — 기본 설정 그대로의 claude.ai 세션을 노린다**. 프롬프트 인젝션 부분은 수정되었고 나머지는 처리 중이다
  ⚠️ v2에서 2026-05-27로 잘못 배치했고, v3에서 Oasis 공개일로 바로잡았다

summary_de: |
  Die vollständige, von Oasis Security offengelegte Angriffskette aus drei Schwachstellen: (1) unsichtbare Prompt-Injection auf claude.ai über einen **URL-Parameter**, (2) ein Datenexfiltrationskanal über die **Anthropic Files API** und (3) ein **Open Redirect** auf claude.ai.
  Die Zustellung erfolgte durch **den Kauf von Google-Anzeigen** — die Anzeigen zeigten einen vertrauenswürdigen claude.com-Link, brachten Nutzer aber zu einem vergifteten Redirect-Punkt und dann in eine präparierte `claude.ai/new?q=`-URL, die still sensible Daten aus dem Unterhaltungsverlauf des Nutzers exfiltrierte.
  ⚠️ **Bemerkenswert ist vor allem: Es sind keine Integration, kein Tool und kein MCP-Server nötig — dies trifft die standardmäßige claude.ai-Sitzung ab Werk**. Der Prompt-Injection-Teil wurde behoben; der Rest wird bearbeitet
  ⚠️ v2 wurde fälschlich auf den 2026-05-27 gesetzt; v3 korrigiert dies auf das Offenlegungsdatum von Oasis

summary_fr: |
  Le pipeline d'attaque complet divulgué par Oasis Security, enchaîné à partir de trois failles : (1) une injection de prompt invisible sur claude.ai via un **paramètre d'URL**, (2) un canal d'exfiltration de données via l'**API Anthropic Files**, et (3) une **redirection ouverte** sur claude.ai.
  La livraison passait par **l'achat de publicités Google** — les annonces affichaient un lien claude.com de confiance mais emmenaient les utilisateurs vers un point de redirection empoisonné, puis vers une URL `claude.ai/new?q=` fabriquée qui exfiltrait silencieusement des données sensibles de l'historique de conversation de l'utilisateur.
  ⚠️ **Le point le plus notable : aucune intégration, outil ou serveur MCP n'est nécessaire — cela frappe la session claude.ai par défaut, prête à l'emploi**. La partie injection de prompt a été corrigée ; le reste est en cours de traitement
  ⚠️ La v2 avait été placée par erreur au 2026-05-27 ; la v3 la corrige à la date de divulgation d'Oasis

summary_es: |
  La canalización de ataque completa divulgada por Oasis Security, encadenada a partir de tres fallos: (1) inyección de prompt invisible en claude.ai mediante un **parámetro de URL**, (2) un canal de exfiltración de datos a través de la **Files API de Anthropic**, y (3) un **open redirect** en claude.ai.
  La entrega fue mediante **la compra de anuncios de Google** — los anuncios mostraban un enlace confiable de claude.com pero llevaban a los usuarios a un punto de redirección envenenado y luego a una URL `claude.ai/new?q=` diseñada que exfiltraba silenciosamente datos sensibles del historial de conversaciones del usuario.
  ⚠️ **Lo más notable: no se necesita ninguna integración, herramienta ni servidor MCP — esto golpea la sesión predeterminada de claude.ai recién salida de la caja**. La parte de inyección de prompt ya se corrigió; el resto está en proceso
  ⚠️ La v2 se colocó por error el 2026-05-27; la v3 la corrige a la fecha de divulgación de Oasis

sources:
  - url: https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability
    label: Oasis Security
  - url: https://www.oasis.security/resources/reports/claude-ai-prompt-injection-vulnerability-technical-report
    label: technical report
  - url: https://www.darkreading.com/vulnerabilities-threats/claudy-day-trio-flaws-claude-users-data-theft
    label: Dark Reading

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Claudy Day: a three-flaw chain in claude.ai

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

The full attack pipeline disclosed by Oasis Security, chained from three flaws: (1) invisible prompt injection on claude.ai via a **URL parameter**, (2) a data exfiltration channel through the **Anthropic Files API**, and (3) an **open redirect** on claude.ai.

Delivery was by **buying Google ads** — the ads showed a trusted claude.com link but took users to a poisoned redirect point and then into a crafted `claude.ai/new?q=` URL that silently exfiltrated sensitive data from the user's conversation history.

⚠️ **The most notable point: no integration, tool or MCP server is required — this hits the out-of-the-box default claude.ai session**. The prompt injection part has been fixed; the rest is being handled

⚠️ v2 was mistakenly placed on 2026-05-27; v3 corrects it to the Oasis disclosure date

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Oasis Security | <https://www.oasis.security/blog/claude-ai-prompt-injection-data-exfiltration-vulnerability> |
| 2 | technical report | <https://www.oasis.security/resources/reports/claude-ai-prompt-injection-vulnerability-technical-report> |
| 3 | Dark Reading | <https://www.darkreading.com/vulnerabilities-threats/claudy-day-trio-flaws-claude-users-data-theft> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-01` (raw: 2026-03, precision `month`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-01-claudy-day-claude-ai` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-03-16` [CellShock: data exfiltration through an AI spreadsheet tool](2026-03-16-cellshock-biao-ge-gong-ju.md)<br>  <sub>CellShock: data exfiltration through an AI spreadsheet tool</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](../2026-04/2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-15` [ShareLeak (CVE-2026-21520) and PipeLeak](../2026-04/2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-01-claudy-day-claude-ai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
