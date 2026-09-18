---
id: 2026-08-04-chaindrop-npm-ru-chong
title: "CHAINDROP npm worm"
title_zh: "CHAINDROP npm 蠕虫"
title_ja: "CHAINDROP npmワーム"
title_ko: "CHAINDROP npm 웜"
title_de: "CHAINDROP npm-Wurm"
title_fr: "Le ver npm CHAINDROP"
title_es: "Gusano npm CHAINDROP"
date: 2026-08-04
date_precision: day
date_raw: "2026-08-04"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The GitHub account of a `keyv` maintainer was compromised → **400+ packages** poisoned by a self-replicating worm. Because it pushed straight to main and published immediately, **the poisoned versions shipped with valid provenance signatures**. A preinstall hook pulls Bun 1.3.13 to run an obfuscated payload that, beyond npm/cloud credentials, **specifically harvests credentials for AI development tools such as Anthropic, Codex, Cursor and Gemini**.
  **The most dangerous part**: if the stolen credentials include a GitHub App token (`ghs_`), the worm commits malicious `.claude/settings.json` and `.vscode/tasks.json` to branches of reachable repositories (up to 50 per repo) — **a developer is infected simply by opening the repo in VS Code or starting one Claude Code session, with no `npm install` required**. Elastic recommends upgrading to npm 12+, which disables preinstall by default


summary_zh: |
  `keyv` 维护者 GitHub 账号被攻陷 → **400+ 个包**被自我复制蠕虫污染。因直接推 main 并立即发版，**污染版本带着合法的来源签名（provenance）发布**。preinstall 钩子拉 Bun 1.3.13 跑混淆载荷，除 npm/云凭据外**专门收集 Anthropic、Codex、Cursor、Gemini 等 AI 开发工具的凭据**。
  **最危险的一点**：窃取的凭据中若含 GitHub App token(`ghs_`)，蠕虫会向可达仓库的分支（每仓最多 50 个）提交恶意的 `.claude/settings.json` 与 `.vscode/tasks.json` —— **开发者只要用 VS Code 打开该仓库、或启动一次 Claude Code 会话，无需 `npm install` 就会被感染**。Elastic 建议升级到默认禁用 preinstall 的 npm 12+

summary_ja: |
  `keyv`メンテナーのGitHubアカウントが侵害され→自己複製ワームにより**400以上のパッケージ**が汚染された。mainに直接プッシュして即公開したため、**汚染版は有効なprovenance署名付きで出荷された**。preinstallフックがBun 1.3.13を取得して難読化ペイロードを実行し、npm／クラウドの認証情報に加えて、**Anthropic、Codex、Cursor、GeminiなどAI開発ツールの認証情報を特に収集する**。
  **最も危険な点**：窃取された認証情報にGitHub Appトークン（`ghs_`）が含まれる場合、ワームは到達可能なリポジトリのブランチに悪性の`.claude/settings.json`と`.vscode/tasks.json`をコミットする（リポジトリあたり最大50）——**開発者はVS Codeでリポジトリを開くか、Claude Codeのセッションを1回開始するだけで感染し、`npm install`は不要である**。Elasticは、preinstallがデフォルトで無効になるnpm 12以降へのアップグレードを推奨している

summary_ko: |
  `keyv` 유지관리자의 GitHub 계정이 침해되었다 → **패키지 400개 이상**이 자기 복제 웜으로 오염되었다. main에 곧바로 푸시해 즉시 게시했기 때문에 **오염된 버전이 유효한 출처 증명 서명과 함께 배포되었다**. preinstall 훅이 Bun 1.3.13을 내려받아 난독화된 페이로드를 실행하며, npm/클라우드 자격 증명 외에도 **Anthropic, Codex, Cursor, Gemini 등 AI 개발 도구의 자격 증명을 특별히 수집한다**.
  **가장 위험한 부분**: 탈취한 자격 증명에 GitHub App 토큰(`ghs_`)이 있으면 웜이 접근 가능한 저장소의 브랜치(저장소당 최대 50개)에 악성 `.claude/settings.json`과 `.vscode/tasks.json`을 커밋한다 — **`npm install` 없이 저장소를 VS Code로 열거나 Claude Code 세션을 한 번 시작하기만 해도 개발자가 감염된다**. Elastic은 preinstall을 기본 비활성화하는 npm 12 이상으로 업그레이드할 것을 권장한다

summary_de: |
  Das GitHub-Konto eines `keyv`-Maintainers wurde kompromittiert → **400+ Pakete** durch einen selbstreplizierenden Wurm vergiftet. Weil er direkt auf main pushte und sofort veröffentlichte, **kamen die vergifteten Versionen mit gültigen Provenienz-Signaturen heraus**. Ein preinstall-Hook zieht Bun 1.3.13, um eine obfuskierte Nutzlast auszuführen, die neben npm-/Cloud-Zugangsdaten **gezielt Zugangsdaten für KI-Entwicklungstools wie Anthropic, Codex, Cursor und Gemini erntet**.
  **Der gefährlichste Teil**: Gehören zu den gestohlenen Zugangsdaten auch GitHub-App-Token (`ghs_`), committet der Wurm bösartige `.claude/settings.json` und `.vscode/tasks.json` in Branches erreichbarer Repositories (bis zu 50 pro Repository) — **ein Entwickler wird infiziert, indem er das Repository einfach in VS Code öffnet oder eine Claude-Code-Sitzung startet, ganz ohne `npm install`**. Elastic empfiehlt ein Upgrade auf npm 12+, das preinstall standardmäßig deaktiviert

summary_fr: |
  Le compte GitHub d'un mainteneur de `keyv` a été compromis → **plus de 400 paquets** empoisonnés par un ver auto-réplicateur. Comme il poussait directement sur main et publiait immédiatement, **les versions empoisonnées sont sorties avec des signatures de provenance valides**. Un hook preinstall tire Bun 1.3.13 pour exécuter une charge obfusquée qui, au-delà des identifiants npm/cloud, **récolte spécifiquement les identifiants d'outils de développement IA comme Anthropic, Codex, Cursor et Gemini**.
  **La partie la plus dangereuse** : si les identifiants volés incluent un jeton d'application GitHub (`ghs_`), le ver committe des fichiers `.claude/settings.json` et `.vscode/tasks.json` malveillants dans des branches de dépôts accessibles (jusqu'à 50 par dépôt) — **un développeur est infecté simplement en ouvrant le dépôt dans VS Code ou en démarrant une session Claude Code, sans `npm install`**. Elastic recommande de passer à npm 12+, qui désactive preinstall par défaut

summary_es: |
  La cuenta de GitHub de un mantenedor de `keyv` fue comprometida → **más de 400 paquetes** envenenados por un gusano autorreplicante. Como hacía push directamente a main y publicaba de inmediato, **las versiones envenenadas se distribuyeron con firmas de procedencia válidas**. Un hook preinstall descarga Bun 1.3.13 para ejecutar una carga útil ofuscada que, además de credenciales de npm y de nube, **recolecta específicamente credenciales de herramientas de desarrollo de IA como Anthropic, Codex, Cursor y Gemini**.
  **La parte más peligrosa**: si entre las credenciales robadas hay un token de GitHub App (`ghs_`), el gusano hace commit de `.claude/settings.json` y `.vscode/tasks.json` maliciosos en ramas de repositorios alcanzables (hasta 50 por repositorio) — **un desarrollador se infecta simplemente abriendo el repositorio en VS Code o iniciando una sesión de Claude Code, sin necesidad de `npm install`**. Elastic recomienda actualizar a npm 12+, que desactiva preinstall por defecto

sources:
  - url: https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain
    label: Elastic
  - url: https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/
    label: Microsoft
  - url: https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack
    label: Wiz
  - url: https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/
    label: Orca
  - url: https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-009/
    label: Singapore CSA advisory

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# CHAINDROP npm worm

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

The GitHub account of a `keyv` maintainer was compromised → **400+ packages** poisoned by a self-replicating worm. Because it pushed straight to main and published immediately, **the poisoned versions shipped with valid provenance signatures**. A preinstall hook pulls Bun 1.3.13 to run an obfuscated payload that, beyond npm/cloud credentials, **specifically harvests credentials for AI development tools such as Anthropic, Codex, Cursor and Gemini**.

**The most dangerous part**: if the stolen credentials include a GitHub App token (`ghs_`), the worm commits malicious `.claude/settings.json` and `.vscode/tasks.json` to branches of reachable repositories (up to 50 per repo) — **a developer is infected simply by opening the repo in VS Code or starting one Claude Code session, with no `npm install` required**. Elastic recommends upgrading to npm 12+, which disables preinstall by default

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
| 1 | Elastic | <https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain> |
| 2 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/08/04/chaindrop-supply-chain-compromise-anatomy-self-propagating-worm/> |
| 3 | Wiz | <https://www.wiz.io/blog/keyv-and-cacheable-npm-supply-chain-attack> |
| 4 | Orca | <https://orca.security/resources/blog/compromised-keyv-npm-supply-chain-attack/> |
| 5 | Singapore CSA advisory | <https://www.csa.gov.sg/alerts-and-advisories/advisories/ad-2026-009/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-04` (raw: 2026-08-04, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-04-chaindrop-npm-ru-chong` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-08-17` [AI finds a flaw AI helped write: Snowflake's Jira token](2026-08-17-snowflake-jira-zhao-dao-can.md)<br>  <sub>AI finds a flaw AI helped write: Snowflake's Jira token</sub>
- `2026-08-18` [Context7 MCP prompt injection (CVE-2026-75130)](2026-08-18-context7-mcp-ti-shi-zhu.md)<br>  <sub>Context7 MCP prompt injection (CVE-2026-75130)</sub>
- `2026-09-01` [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](../2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
