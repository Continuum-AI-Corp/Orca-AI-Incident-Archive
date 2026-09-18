---
id: 2026-04-01-claude-code-github-action
title: "Three CVEs in the Claude Code GitHub Action: a PR title steals your API key"
title_zh: "Claude Code GitHub Action 三 CVE：一个 PR 标题偷走 API key"
title_ja: "Claude Code GitHub Actionの3件のCVE：PRタイトルでAPIキーが窃取される"
title_ko: "Claude Code GitHub Action의 CVE 3건: PR 제목 하나로 API 키 탈취"
title_de: "Drei CVEs in der Claude Code GitHub Action: ein PR-Titel stiehlt den API-Schlüssel"
title_fr: "Trois CVE dans la Claude Code GitHub Action : un titre de PR vole votre clé API"
title_es: "Tres CVE en la GitHub Action de Claude Code: el título de un PR roba tu clave de API"
date: 2026-04-01
date_precision: month
date_raw: "2026-04"

kind: vulnerability
type: [IPI, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. A carefully crafted PR title alone can prompt-inject the Claude Code agent running in GitHub Actions and exfiltrate `ANTHROPIC_API_KEY` to an attacker endpoint. **No authentication and no repository permissions needed — opening a PR is enough**. Confirmed exfiltratable: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **The same injection vector reproduced successfully on Claude Code, Gemini CLI and GitHub Copilot Agent**. Anthropic fixed it in **Claude Code 2.1.128 on 2026-05-05** with five layers of control (tool-scope allowlist, read-only GITHUB_TOKEN, OIDC secret routing, actor filtering, script loop cap)


summary_zh: |
  **CVE-2026-35020 / 35021 / 35022，CVSS 9.4**。精心构造的 PR 标题即可对跑在 GitHub Actions 里的 Claude Code agent 做提示注入，把 `ANTHROPIC_API_KEY` 外带到攻击者端点。**无需认证、无需仓库权限 —— 开个 PR 就够了**。已确认可外带：`ANTHROPIC_API_KEY`、`GITHUB_TOKEN`、`GEMINI_API_KEY`、`GITHUB_COPILOT_API_TOKEN`、`GITHUB_PERSONAL_ACCESS_TOKEN`。**同一注入向量在 Claude Code、Gemini CLI 与 GitHub Copilot Agent 上均复现成功**。Anthropic 于 **2026-05-05 的 Claude Code 2.1.128** 修复，采用五层控制（工具范围白名单、只读 GITHUB_TOKEN、OIDC 密钥路由、actor 过滤、脚本循环上限）

summary_ja: |
  **CVE-2026-35020 / 35021 / 35022、CVSS 9.4**。巧妙に細工されたPRタイトルだけで、GitHub Actionsで動作するClaude Codeエージェントにプロンプトインジェクションし、`ANTHROPIC_API_KEY`を攻撃者のエンドポイントへ外部送信させられる。**認証もリポジトリ権限も不要——PRを開くだけで成立する**。外部送信可能と確認されたのは`ANTHROPIC_API_KEY`、`GITHUB_TOKEN`、`GEMINI_API_KEY`、`GITHUB_COPILOT_API_TOKEN`、`GITHUB_PERSONAL_ACCESS_TOKEN`。**同じインジェクションベクターはClaude Code、Gemini CLI、GitHub Copilot Agentでも再現に成功した**。Anthropicは**2026-05-05のClaude Code 2.1.128**で5層の制御（ツールスコープの許可リスト、読み取り専用GITHUB_TOKEN、OIDCシークレットルーティング、アクターフィルタリング、スクリプトループ上限）とともに修正した

summary_ko: |
  **CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. 정교하게 만든 PR 제목 하나로 GitHub Actions에서 실행되는 Claude Code 에이전트에 프롬프트 인젝션을 걸어 `ANTHROPIC_API_KEY`를 공격자 엔드포인트로 유출할 수 있다. **인증도 저장소 권한도 필요 없다 — PR을 열기만 하면 된다**. 유출이 확인된 항목: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **같은 주입 벡터가 Claude Code, Gemini CLI, GitHub Copilot Agent에서 모두 재현되었다**. Anthropic은 **2026-05-05 Claude Code 2.1.128**에서 5중 통제(도구 범위 허용 목록, 읽기 전용 GITHUB_TOKEN, OIDC 시크릿 라우팅, 행위자 필터링, 스크립트 루프 상한)로 수정했다

summary_de: |
  **CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. Allein ein sorgfältig gestalteter PR-Titel kann den in GitHub Actions laufenden Claude-Code-Agenten per Prompt-Injection dazu bringen, `ANTHROPIC_API_KEY` an einen Endpunkt des Angreifers zu exfiltrieren. **Keine Authentifizierung und keine Repository-Berechtigungen nötig — einen PR zu öffnen genügt**. Als exfiltrierbar bestätigt: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **Derselbe Injektionsvektor ließ sich erfolgreich auf Claude Code, Gemini CLI und GitHub Copilot Agent reproduzieren**. Anthropic behob es in **Claude Code 2.1.128 am 2026-05-05** mit fünf Kontrollebenen (Positivliste für Tool-Geltungsbereiche, schreibgeschütztes GITHUB_TOKEN, OIDC-Secret-Routing, Akteurfilterung, Obergrenze für Skriptschleifen)

summary_fr: |
  **CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. Un titre de PR soigneusement conçu suffit à injecter un prompt dans l'agent Claude Code exécuté dans GitHub Actions et à exfiltrer `ANTHROPIC_API_KEY` vers un point de terminaison d'attaquant. **Aucune authentification ni permission de dépôt nécessaire — ouvrir une PR suffit**. Confirmés exfiltrables : `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **Le même vecteur d'injection reproduit avec succès sur Claude Code, Gemini CLI et GitHub Copilot Agent**. Anthropic l'a corrigé dans **Claude Code 2.1.128 le 2026-05-05** avec cinq couches de contrôle (liste blanche de périmètre d'outils, GITHUB_TOKEN en lecture seule, routage de secrets par OIDC, filtrage des acteurs, plafond de boucles de scripts)

summary_es: |
  **CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. Solo con un título de PR cuidadosamente elaborado se puede inyectar un prompt en el agente Claude Code que se ejecuta en GitHub Actions y exfiltrar `ANTHROPIC_API_KEY` a un endpoint del atacante. **No se necesitan autenticación ni permisos de repositorio — basta con abrir un PR**. Confirmados como exfiltrables: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **El mismo vector de inyección se reprodujo con éxito en Claude Code, Gemini CLI y GitHub Copilot Agent**. Anthropic lo corrigió en **Claude Code 2.1.128 el 2026-05-05** con cinco capas de control (lista de permitidos de alcance de herramientas, GITHUB_TOKEN de solo lectura, enrutamiento de secretos por OIDC, filtrado de actores, límite de bucles de scripts)

sources:
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/
    label: CSA
  - url: https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/
    label: reproduction analysis

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Three CVEs in the Claude Code GitHub Action: a PR title steals your API key

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**CVE-2026-35020 / 35021 / 35022, CVSS 9.4**. A carefully crafted PR title alone can prompt-inject the Claude Code agent running in GitHub Actions and exfiltrate `ANTHROPIC_API_KEY` to an attacker endpoint. **No authentication and no repository permissions needed — opening a PR is enough**. Confirmed exfiltratable: `ANTHROPIC_API_KEY`, `GITHUB_TOKEN`, `GEMINI_API_KEY`, `GITHUB_COPILOT_API_TOKEN`, `GITHUB_PERSONAL_ACCESS_TOKEN`. **The same injection vector reproduced successfully on Claude Code, Gemini CLI and GitHub Copilot Agent**. Anthropic fixed it in **Claude Code 2.1.128 on 2026-05-05** with five layers of control (tool-scope allowlist, read-only GITHUB_TOKEN, OIDC secret routing, actor filtering, script loop cap)

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-code-github-action-prompt-injection/> |
| 2 | reproduction analysis | <https://oddguan.com/blog/comment-and-control-prompt-injection-credential-theft-claude-code-gemini-cli-github-copilot/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-01` (raw: 2026-04, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-01-claude-code-github-action` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-04-15` [ShareLeak (CVE-2026-21520) and PipeLeak](2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>
- `2026-04-19` [Vercel OAuth supply-chain intrusion](2026-04-19-vercel-oauth-gong-ying-lian.md)<br>  <sub>Vercel OAuth supply-chain intrusion</sub>
- `2026-04-21` [Unauthorised access to Anthropic's "Mythos"](2026-04-21-anthropic-mythos-zao-shou-quan.md)<br>  <sub>Unauthorised access to Anthropic's "Mythos"</sub>
- `2026-04-30` [Apple Support app ships an internal CLAUDE.md by mistake](2026-04-30-apple-support-app-claude-md.md)<br>  <sub>Apple Support app ships an internal CLAUDE.md by mistake</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-01-claude-code-github-action.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
