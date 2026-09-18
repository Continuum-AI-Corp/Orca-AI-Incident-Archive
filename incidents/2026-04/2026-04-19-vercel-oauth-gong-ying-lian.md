---
id: 2026-04-19-vercel-oauth-gong-ying-lian
title: "Vercel OAuth supply-chain intrusion"
title_zh: "Vercel OAuth 供应链入侵"
title_ja: "VercelのOAuthサプライチェーン侵入"
title_ko: "Vercel OAuth 공급망 침입"
title_de: "Vercel: OAuth-Supply-Chain-Intrusion"
title_fr: "Intrusion dans la chaîne d'approvisionnement OAuth de Vercel"
title_es: "Intrusión en la cadena de suministro por OAuth de Vercel"
date: 2026-04-19
date_precision: day
date_raw: "2026-04-19"

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A Context.ai employee was hit by **Lumma Stealer** → the attacker stole the **Google Workspace OAuth token** a Vercel employee had granted Context.ai → pivoting to obtain Vercel's API keys and database connection strings. **The upstream of the AI ecosystem was breached, affecting a downstream deployment platform**; the over-broad scope of the OAuth token was the main reason it spread


summary_zh: |
  Context.ai 员工中招 **Lumma Stealer** → 攻击者盗走 Vercel 员工授予 Context.ai 的 **Google Workspace OAuth token** → 横移取得 Vercel 的 API key 与数据库连接串。**AI 生态上游被打穿，波及下游部署平台**；OAuth 令牌权限范围过宽是扩大化主因

summary_ja: |
  Context.aiの従業員が**Lumma Stealer**に感染→攻撃者はVercelの従業員がContext.aiに付与していた**Google WorkspaceのOAuthトークン**を窃取→横展開してVercelのAPIキーとデータベース接続文字列を取得。**AIエコシステムの上流が侵害され、下流のデプロイプラットフォームに影響した**。OAuthトークンの過大なスコープが被害拡大の主因だった

summary_ko: |
  Context.ai 직원이 **Lumma Stealer**에 감염되었다 → 공격자는 Vercel 직원이 Context.ai에 부여한 **Google Workspace OAuth 토큰**을 탈취했다 → 이를 발판으로 Vercel의 API 키와 데이터베이스 연결 문자열을 획득했다. **AI 생태계의 상류가 침해되어 하류 배포 플랫폼에 영향을 주었으며**, OAuth 토큰의 과도하게 넓은 범위가 확산의 주된 원인이었다

summary_de: |
  Ein Mitarbeiter von Context.ai wurde von **Lumma Stealer** getroffen → der Angreifer stahl das **Google-Workspace-OAuth-Token**, das ein Vercel-Mitarbeiter Context.ai gewährt hatte → über diesen Pivot gelangte er an Vercels API-Schlüssel und Datenbank-Verbindungszeichenfolgen. **Das Upstream des KI-Ökosystems wurde kompromittiert, was eine nachgelagerte Deployment-Plattform betraf**; der zu weit gefasste Geltungsbereich des OAuth-Tokens war der Hauptgrund für die Ausbreitung

summary_fr: |
  Un employé de Context.ai a été touché par **Lumma Stealer** → l'attaquant a volé le **jeton OAuth Google Workspace** qu'un employé de Vercel avait accordé à Context.ai → pivot pour obtenir les clés API et chaînes de connexion aux bases de Vercel. **L'amont de l'écosystème IA a été compromis, touchant une plateforme de déploiement en aval** ; la portée excessive du jeton OAuth est la principale raison de la propagation

summary_es: |
  Un empleado de Context.ai fue golpeado por **Lumma Stealer** → el atacante robó el **token OAuth de Google Workspace** que un empleado de Vercel había concedido a Context.ai → pivotando para obtener las claves de API y las cadenas de conexión de bases de datos de Vercel. **Se comprometió el upstream del ecosistema de IA, afectando a una plataforma de despliegue posterior**; el alcance demasiado amplio del token OAuth fue la razón principal de su propagación

sources:
  - url: https://vercel.com/kb/bulletin/vercel-april-2026-security-incident
    label: Vercel official
  - url: https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html
    label: Trend Micro

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Vercel OAuth supply-chain intrusion

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A Context.ai employee was hit by **Lumma Stealer** → the attacker stole the **Google Workspace OAuth token** a Vercel employee had granted Context.ai → pivoting to obtain Vercel's API keys and database connection strings. **The upstream of the AI ecosystem was breached, affecting a downstream deployment platform**; the over-broad scope of the OAuth token was the main reason it spread

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Vercel official | <https://vercel.com/kb/bulletin/vercel-april-2026-security-incident> |
| 2 | Trend Micro | <https://www.trendmicro.com/en_us/research/26/d/vercel-breach-oauth-supply-chain.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-19` (raw: 2026-04-19, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-19-vercel-oauth-gong-ying-lian` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-21` [Unauthorised access to Anthropic's "Mythos"](2026-04-21-anthropic-mythos-zao-shou-quan.md)<br>  <sub>Unauthorised access to Anthropic's "Mythos"</sub>
- `2026-04-24` [Gemini CLI CVSS 10.0: one pull request compromises CI](2026-04-24-gemini-cli-pr-ci.md)<br>  <sub>Gemini CLI CVSS 10.0: one pull request compromises CI</sub>
- `2026-04-30` [Apple Support app ships an internal CLAUDE.md by mistake](2026-04-30-apple-support-app-claude-md.md)<br>  <sub>Apple Support app ships an internal CLAUDE.md by mistake</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-19-vercel-oauth-gong-ying-lian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
