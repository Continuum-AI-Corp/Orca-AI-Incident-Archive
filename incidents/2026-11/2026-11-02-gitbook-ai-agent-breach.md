---
id: 2026-11-02-gitbook-ai-agent-breach
title: "GitBook discloses a targeted breach it attributes to AI agents, exposing infrastructure and customer credentials"
title_zh: "GitBook 披露一起归因于 AI agents 的定向攻击，基础设施与客户凭证遭泄露"
title_ja: "GitBook、AIエージェントによるとする標的型侵害を公表——インフラと顧客の認証情報が流出"
title_ko: "GitBook, AI 에이전트 소행으로 지목한 표적 침해 공개——인프라·고객 자격 증명 유출"
title_de: "GitBook meldet einen gezielten Angriff, den es KI-Agenten zuschreibt — Infrastruktur- und Kunden-Credentials offengelegt"
title_fr: "GitBook révèle une attaque ciblée qu'elle attribue à des agents IA, exposant des identifiants d'infrastructure et de clients"
title_es: "GitBook revela un ataque dirigido que atribuye a agentes de IA, exponiendo credenciales de infraestructura y de clientes"
date: 2026-11-02
date_raw: "2026-11-02 (intrusion; disclosed 2026-11-03)"
date_precision: day

kind: incident
type: [CRED, INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: unverified

region: [GLOBAL]

summary: |
  **On 2 November 2026, documentation platform GitBook was breached in what it called "a sophisticated, highly targeted attack using AI agents"; it disclosed the incident on 3 November.** Per GitBook's own post-mortem, an attacker hijacked an account at a targeted customer at 12:27 UTC, reached staff sessions and source code by 16:32, and the production environment by 17:48; GitBook detected it at 18:10, fixed an SSO flaw at 19:58, and took itself offline at 20:32, restoring service ~16 hours later after rotating every secret. Potentially exposed: GitBook API tokens, integration and session-signing secrets, internal **source code**, infrastructure secrets, database credentials, Git Sync secrets, a **Cloudflare API key**, customer content, repo access each customer had granted, and **questions visitors asked the GitBook Assistant**; passwords, billing and IPs were not. GitBook forced customers to rotate all tokens and **re-authenticate the GitBook MCP server**. PancakeSwap moved its docs off GitBook. The "AI agents" attribution is GitBook's **inference from the attacker's "speed and precision"**, not a forensically confirmed finding — hence `ai_involvement: unverified`. Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

summary_zh: |
  **2026 年 11 月 2 日，文档平台 GitBook 遭入侵，官方称其为"一场使用 AI agents 的高度定向攻击"，并于 11 月 3 日披露。** 据 GitBook 自己的事后复盘：攻击者于 UTC 12:27 劫持了某目标客户的账号，16:32 拿到员工会话与源码，17:48 进入生产环境；GitBook 18:10 检测到、19:58 修复一处 SSO 缺陷、20:32 主动下线，轮换全部密钥后约 16 小时恢复。可能被泄露的包括：GitBook API token、集成与会话签名密钥、内部**源码**、基础设施密钥、数据库凭证、Git Sync secrets、一个 **Cloudflare API key**、客户内容、各客户授予的仓库访问权，以及**访客向 GitBook Assistant 提出的问题**；密码、账单、IP 未泄。GitBook 强制客户轮换全部 token 并**重新认证 GitBook MCP server**。PancakeSwap 把文档迁离 GitBook。"AI agents"的归因是 GitBook **从攻击者"速度与精度"推断**而来，并非取证确认——故 `ai_involvement: unverified`。记为 `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`。

summary_ja: |
  **2026年11月2日、ドキュメントプラットフォームGitBookが侵害され、同社は「AIエージェントを用いた高度に標的化された攻撃」と表現、11月3日に公表した。** GitBook自身の事後報告によれば、攻撃者はUTC 12:27に標的顧客のアカウントを乗っ取り、16:32までにスタッフセッションとソースコードへ、17:48までに本番環境へ到達。GitBookは18:10に検知、19:58にSSOの不具合を修正、20:32に自らをオフライン化し、全シークレットをローテーションして約16時間後に復旧した。流出の可能性があるもの：GitBook APIトークン、連携・セッション署名シークレット、内部**ソースコード**、インフラのシークレット、DB認証情報、Git Syncシークレット、**Cloudflare APIキー**、顧客コンテンツ、各顧客が許可したリポジトリアクセス、そして**訪問者がGitBook Assistantに尋ねた質問**。パスワード・請求情報・IPは対象外。GitBookは全トークンのローテーションと**GitBook MCPサーバーの再認証**を顧客に求めた。「AIエージェント」という帰属は攻撃者の「速度と精度」からの**推論**であり、フォレンジックで確認されたものではない——よって `ai_involvement: unverified`。`incident` / `CRED` + `INFRA` / `high` / `real_harm: true`。

summary_ko: |
  **2026년 11월 2일, 문서화 플랫폼 GitBook이 침해당했으며, 회사는 이를 "AI 에이전트를 사용한 정교하고 고도로 표적화된 공격"이라고 표현하고 11월 3일 공개했다.** GitBook 자체 사후 분석에 따르면, 공격자는 UTC 12:27에 표적 고객 계정을 탈취했고 16:32까지 직원 세션과 소스 코드에, 17:48까지 운영 환경에 도달했다. GitBook은 18:10에 탐지, 19:58에 SSO 결함 수정, 20:32에 자체 오프라인 전환했으며 모든 시크릿을 교체한 뒤 약 16시간 후 복구했다. 노출 가능 항목: GitBook API 토큰, 연동·세션 서명 시크릿, 내부 **소스 코드**, 인프라 시크릿, DB 자격 증명, Git Sync 시크릿, **Cloudflare API 키**, 고객 콘텐츠, 각 고객이 부여한 저장소 접근, 그리고 **방문자가 GitBook Assistant에 던진 질문**. 비밀번호·결제·IP는 제외. GitBook은 모든 토큰 교체와 **GitBook MCP 서버 재인증**을 고객에 요구했다. "AI 에이전트" 귀속은 공격자의 "속도와 정밀도"에서 나온 **추론**이며 포렌식으로 확인된 것이 아니다——따라서 `ai_involvement: unverified`. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

summary_de: |
  **Am 2. November 2026 wurde die Dokumentationsplattform GitBook bei einem von ihr als „ausgeklügelten, hochgradig gezielten Angriff unter Einsatz von KI-Agenten" bezeichneten Vorfall kompromittiert; die Offenlegung erfolgte am 3. November.** Laut GitBooks eigenem Post-mortem kaperte ein Angreifer um 12:27 UTC ein Konto bei einem gezielten Kunden, erreichte bis 16:32 Mitarbeitersitzungen und Quellcode und bis 17:48 die Produktionsumgebung; GitBook erkannte es um 18:10, behob um 19:58 einen SSO-Fehler und ging um 20:32 offline, um nach Rotation aller Secrets rund 16 Stunden später wiederherzustellen. Möglicherweise offengelegt: GitBook-API-Tokens, Integrations- und Sitzungssignatur-Secrets, interner **Quellcode**, Infrastruktur-Secrets, Datenbank-Anmeldedaten, Git-Sync-Secrets, ein **Cloudflare-API-Key**, Kundeninhalte, jeweils gewährte Repo-Zugriffe sowie **Fragen, die Besucher dem GitBook Assistant stellten**; Passwörter, Abrechnung und IPs nicht. GitBook zwang Kunden, alle Tokens zu rotieren und **den GitBook-MCP-Server neu zu authentifizieren**. PancakeSwap zog seine Docs von GitBook ab. Die Zuordnung zu „KI-Agenten" ist GitBooks **Rückschluss aus „Geschwindigkeit und Präzision"** des Angreifers, kein forensisch bestätigter Befund — daher `ai_involvement: unverified`. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

summary_fr: |
  **Le 2 novembre 2026, la plateforme de documentation GitBook a été compromise lors de ce qu'elle a qualifié d'« attaque sophistiquée et hautement ciblée utilisant des agents IA » ; elle l'a révélé le 3 novembre.** Selon le post-mortem de GitBook, un attaquant a détourné un compte chez un client ciblé à 12:27 UTC, atteint les sessions du personnel et le code source à 16:32, puis l'environnement de production à 17:48 ; GitBook l'a détecté à 18:10, corrigé une faille SSO à 19:58 et s'est mis hors ligne à 20:32, rétablissant le service ~16 heures plus tard après rotation de tous les secrets. Potentiellement exposés : jetons API GitBook, secrets d'intégration et de signature de session, **code source** interne, secrets d'infrastructure, identifiants de base de données, secrets Git Sync, une **clé API Cloudflare**, contenus clients, accès aux dépôts accordés par chaque client, et **questions posées par les visiteurs à GitBook Assistant** ; mots de passe, facturation et IP non concernés. GitBook a contraint les clients à faire tourner tous les jetons et à **ré-authentifier le serveur MCP GitBook**. PancakeSwap a déplacé ses docs hors de GitBook. L'attribution aux « agents IA » est une **inférence de GitBook à partir de la « vitesse et de la précision »** de l'attaquant, non un constat confirmé par forensique — d'où `ai_involvement: unverified`. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

summary_es: |
  **El 2 de noviembre de 2026, la plataforma de documentación GitBook fue vulnerada en lo que calificó como "un ataque sofisticado y altamente dirigido usando agentes de IA"; lo reveló el 3 de noviembre.** Según el post-mortem de la propia GitBook, un atacante secuestró una cuenta de un cliente objetivo a las 12:27 UTC, alcanzó sesiones del personal y código fuente a las 16:32, y el entorno de producción a las 17:48; GitBook lo detectó a las 18:10, corrigió una falla de SSO a las 19:58 y se puso fuera de línea a las 20:32, restaurando el servicio ~16 horas después tras rotar todos los secretos. Potencialmente expuestos: tokens de API de GitBook, secretos de integración y de firma de sesión, **código fuente** interno, secretos de infraestructura, credenciales de base de datos, secretos de Git Sync, una **clave API de Cloudflare**, contenido de clientes, accesos a repos concedidos por cada cliente, y **preguntas que los visitantes hicieron a GitBook Assistant**; contraseñas, facturación e IPs no. GitBook obligó a los clientes a rotar todos los tokens y a **re-autenticar el servidor MCP de GitBook**. PancakeSwap trasladó sus docs fuera de GitBook. La atribución a "agentes de IA" es una **inferencia de GitBook a partir de la "velocidad y precisión"** del atacante, no un hallazgo confirmado forensemente — de ahí `ai_involvement: unverified`. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

sources:
  - url: https://www.gitbook.com/status/security-incident-2026-11-03
    label: GitBook (official security incident disclosure & post-mortem)
  - url: https://decrypt.co/382465/crypto-docs-gitbook-ai-agent-security-breach
    label: Decrypt
  - url: https://forklog.com/en/hackers-breach-gitbook-using-ai-agents/
    label: ForkLog
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.36"
---

# GitBook discloses a targeted breach it attributes to AI agents, exposing infrastructure and customer credentials

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: unverified](https://img.shields.io/badge/AI_involvement-unverified-7A868C?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**On 2 November 2026, documentation platform GitBook was breached in what it called "a sophisticated, highly targeted attack using AI agents"; it disclosed the incident on 3 November.** Per GitBook's own post-mortem, an attacker hijacked an account at a targeted customer at 12:27 UTC, reached staff sessions and source code by 16:32, and the production environment by 17:48; GitBook detected it at 18:10, fixed an SSO flaw at 19:58, and took itself offline at 20:32, restoring service ~16 hours later after rotating every secret. Potentially exposed: GitBook API tokens, integration and session-signing secrets, internal source code, infrastructure secrets, database credentials, Git Sync secrets, a Cloudflare API key, customer content, repo access each customer had granted, and questions visitors asked the GitBook Assistant; passwords, billing and IPs were not. GitBook forced customers to rotate all tokens and re-authenticate the GitBook MCP server. PancakeSwap moved its docs off GitBook. The "AI agents" attribution is GitBook's inference from the attacker's "speed and precision", not a forensically confirmed finding — hence `ai_involvement: unverified`. Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Account hijack at a targeted customer<br/>(Nov 2, 12:27 UTC)"]:::entry
    S1["Staff sessions + source code (16:32)<br/>→ production environment (17:48)"]:::step
    S2["Detected 18:10 · SSO flaw fixed 19:58<br/>· offline 20:32 · all secrets rotated"]:::step
    I["Exposed: API tokens, session/integration secrets,<br/>source code, DB creds, Git Sync secrets, Cloudflare key,<br/>customer content, GitBook Assistant questions"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** GitBook — a documentation platform widely used by software and cryptocurrency projects — published a security disclosure on **3 November 2026** stating it "has been the target of a sophisticated, highly targeted attack using AI agents." Its post-mortem gives a minute-by-minute timeline (UTC) for **2 November**: **12:27** an account at the targeted customer is hijacked; **16:32** the attacker reaches staff sessions and then source code; **17:48** the attacker reaches the production environment; **18:10** an internal alert fires and investigation begins; **19:58** an SSO flaw is fixed; **20:32** compromised accounts are disabled and GitBook is taken offline. On **3 November**, GitBook redeployed with new secrets (**02:34**, invalidating pre-existing API tokens), completed rotating all secrets and came back online after ~16 hours of downtime (**11:56**), and later rotated the GitLab tokens used for Git Sync (**22:51**). GitBook says the attacker held production access for roughly 2h45m on the evening of 2 November and ~40 minutes early on 3 November.

**What was exposed.** Per GitBook, potentially accessed data includes GitBook API tokens; integration tokens and secrets; session signing secrets; documentation sites using authenticated access; the GitHub and GitLab access each customer had granted to GitBook (limited to those repositories); customer content such as docs, spaces and change requests; internal source code, infrastructure secrets, database credentials, Git Sync secrets, and a **Cloudflare API key**; and **"questions asked to GitBook Assistant by your site visitors."** GitBook states billing information, passwords and IP addresses were **not** compromised, and it found no evidence that other customers' content was modified.

**On the "AI agents" claim.** GitBook frames the AI-agent involvement as an **inference from the attacker's behaviour**, not a forensic finding: the post-mortem says the attacker "moved with a speed and precision that pointed to an attack driven largely by automation and AI." The entry vector GitBook describes is an **SSO flaw plus account hijack** at a targeted customer — not GitBook's own AI products. Because the AI attribution rests on observed speed rather than recovered tooling, this record uses `ai_involvement: unverified` (and does **not** claim GitBook's AI Assistant or MCP server was the vector — those appear only as *exposed surface*: Assistant questions were among the data potentially read, and customers must re-authenticate the MCP server).

**Remediation and customer action.** GitBook revoked all personal API tokens, rotated all production and GitBook-managed customer secrets (including Git Sync and GitLab keys), recycled staging/production nodes, reversed actions taken by the compromised service account, and closed the exploited paths. It instructs customers to create a new API token, rotate third-party tokens and integration secrets, regenerate the authenticated-access signing key, **re-authenticate the GitBook MCP server**, reconnect Git Sync/GitLab, and review environments for the attacker IPs `94.183.188.91`, `45.139.84.195`, and `198.251.83.217`. Downstream, **PancakeSwap** took its docs offline and later moved them off GitBook (saying its app was unaffected), and **TradeXYZ** warned users not to click links in its documentation during the investigation.

**How it is graded.** `incident` — a real, disclosed breach with first-party confirmation. `CRED` (the defining loss is credentials/secrets — API tokens, integration/session secrets, DB credentials, a Cloudflare key) + `INFRA` (GitBook is shared documentation infrastructure for many AI/dev/crypto projects, with an AI Assistant and MCP server in scope). `real_harm: true`: source code, infrastructure secrets and customer secrets were exposed, forcing fleet-wide rotation, and at least one large customer migrated away. Severity `high`, not critical: production access was contained to ~3 hours, GitBook found no content modification, and passwords/billing/IPs were not compromised. `ai_involvement: unverified`: GitBook attributes AI agents from attacker speed, not from recovered tooling. Confidence `A`: detailed first-party post-mortem, corroborated by Decrypt and ForkLog.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | GitBook (official security incident disclosure & post-mortem) | <https://www.gitbook.com/status/security-incident-2026-11-03> |
| 2 | Decrypt | <https://decrypt.co/382465/crypto-docs-gitbook-ai-agent-security-breach> |
| 3 | ForkLog | <https://forklog.com/en/hackers-breach-gitbook-using-ai-agents/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-02` (raw: 2026-11-02 intrusion; disclosed 2026-11-03, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **High** `high` |
| Confidence | **A** — first-party GitBook post-mortem + Decrypt + ForkLog |
| Real harm | Yes — source code, infrastructure secrets, a Cloudflare key and customer secrets exposed; fleet-wide rotation forced; PancakeSwap migrated away |
| AI involvement | Unverified `unverified` — GitBook infers AI agents from attacker speed/precision, not from recovered tooling |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-11-02-gitbook-ai-agent-breach` |

<sub>**Why this classification:** A first-party-confirmed breach of shared documentation infrastructure whose defining loss is credentials and secrets (`CRED` + `INFRA`). `real_harm: true` because source code, infrastructure secrets, a Cloudflare API key and customer secrets were exposed, forcing fleet-wide rotation and at least one customer migration. `high`, not critical: ~3h contained production access, no content modification, and passwords/billing/IPs safe. `ai_involvement: unverified` because GitBook's AI-agent attribution is an inference from attacker speed, not a forensic finding. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-30` ["Black October": a coordinated wave breached at least nine AI developer platforms to harvest AI-access credentials](../2026-10/2026-10-30-black-october-ai-developer-platform-breaches.md)<br>  <sub>Same month-long pattern of AI/dev-platform infrastructure breached for stored credentials</sub>
- `2026-10-27` [Warp discloses a third-party vendor breach that exposed AI-agent decision logs and user telemetry](../2026-10/2026-10-27-warp-vendor-breach-agent-logs.md)<br>  <sub>Another AI-tooling vendor breach disclosed in the same wave</sub>
- `2026-10-17` [OpenCode Console breach exposes users' stored AI-provider API keys](../2026-10/2026-10-17-opencode-console-breach-api-keys.md)<br>  <sub>Credential-harvesting breach of an AI developer platform</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-02-gitbook-ai-agent-breach.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
