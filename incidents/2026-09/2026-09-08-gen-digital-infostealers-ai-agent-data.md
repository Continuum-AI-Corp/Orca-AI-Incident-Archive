---
id: 2026-09-08-gen-digital-infostealers-ai-agent-data
title: "Infostealers turn to AI-agent data: collection rules now target Claude, Cursor and Codex"
title_zh: "窃密软件转向 AI agent 数据：采集规则开始针对 Claude、Cursor 与 Codex"
title_ja: "インフォスティーラーがAIエージェントのデータへ：収集ルールがClaude、Cursor、Codexを標的に"
title_ko: "인포스틸러가 AI 에이전트 데이터로: 수집 규칙이 Claude·Cursor·Codex를 겨냥하다"
title_de: "Infostealer entdecken Agentendaten: Sammlungsregeln zielen jetzt auf Claude, Cursor und Codex"
title_fr: "Les infostealers s'attaquent aux données des agents : les règles de collecte ciblent désormais Claude, Cursor et Codex"
title_es: "Los infostealers apuntan a los datos de agentes: las reglas de recolección ya cazan Claude, Cursor y Codex"
date: 2026-09-08
date_raw: "2026-09-08"
date_precision: day

kind: research
type: [CRED, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Gen Digital** publishes an analysis of recent information-stealer collection rules and finds a new target list: local data belonging to AI coding agents and developer tools — **Claude, Cline, Codex, Continue, Cursor, OpenCode** and others. The targeting is not experimental. Over a three-month window, its telemetry recorded **Amatera** (Cline, Continue) and **Remus** (Claude, Cursor, OpenCode) detections among tens of thousands of protected users; **CallbackBeaver** has added Cursor and Claude to its collection scope with more than **5,000 samples in 30 days**, and BeeStealer, STG, HydraStealer, APEX and Otter show the behaviour spreading, with **Djinn** doing the same on macOS. What is collected is not preferences but **access and context**: access and refresh **tokens**, credentials stored in **MCP configurations**, prompt histories, conversation databases and traces of the projects a developer worked on. The following day, **Okta's threat-intelligence team** showed the same market from the buyer's side — a free 7 GB log dump from **5,871 infected machines** contained **555 tokens tied to AI services** among 44,791 JWTs, and 24 still-valid AI API keys

summary_zh: |
  **Gen Digital** 对近期窃密软件的采集规则做了分析，发现了一份新的目标清单：属于 AI 编程 agent 与开发工具的本地数据——**Claude、Cline、Codex、Continue、Cursor、OpenCode** 等。这种针对并非实验性质：在三个月的窗口里，其遥测在数万名受保护用户中记录了 **Amatera**（针对 Cline、Continue）与 **Remus**（针对 Claude、Cursor、OpenCode）的检出；**CallbackBeaver** 已把 Cursor 和 Claude 列入采集范围，30 天内出现 **5000 多个样本**；BeeStealer、STG、HydraStealer、APEX、Otter 等家族显示该行为正在扩散，macOS 上的 **Djinn** 也在做同样的事。被采集的不是偏好设置，而是**访问权与上下文**：访问与刷新**令牌**、存放在 **MCP 配置**里的凭据、提示历史、会话数据库，以及开发者做过的项目踪迹。次日，**Okta 威胁情报团队**从买家一侧展示了同一个市场——一份来自 **5,871 台受感染机器**的免费 7GB 日志包，在 44,791 个 JWT 中检出 **555 个与 AI 服务相关的令牌**，以及 24 个仍然有效的 AI API 密钥

summary_ja: |
  **Gen Digital**が最近のインフォスティーラーの収集ルールを分析し、新たな標的リストを明らかにした。AIコーディングエージェントや開発者ツールのローカルデータ——**Claude、Cline、Codex、Continue、Cursor、OpenCode**など——である。これは実験的なものではない。3か月の観測期間で、同社のテレメトリは**Amatera**（Cline、Continue）と**Remus**（Claude、Cursor、OpenCode）の検出を数万人の保護ユーザー間で記録した。**CallbackBeaver**はCursorとClaudeを収集対象に追加し、30日間で**5,000件超のサンプル**が観測され、BeeStealer、STG、HydraStealer、APEX、Otterにも広がり、macOSでは**Djinn**が同様の動きを見せる。収集されるのは設定ではなく**アクセスと文脈**だ。アクセス／リフレッシュ**トークン**、**MCP設定**に保存された資格情報、プロンプト履歴、会話データベース、開発者が触れたプロジェクトの痕跡。翌日、**Oktaの脅威インテリジェンスチーム**が買い手側から同じ市場を示した——**5,871台**の感染端末からの無料7GBログには、44,791件のJWTのうち**AIサービスに関連する555件のトークン**と、24件の有効なAI APIキーが含まれていた

summary_ko: |
  **Gen Digital**이 최근 인포스틸러 수집 규칙을 분석해 새로운 표적 목록을 찾아냈다. AI 코딩 에이전트와 개발 도구의 로컬 데이터 — **Claude, Cline, Codex, Continue, Cursor, OpenCode** 등이다. 이는 실험이 아니다. 3개월 동안 자사 텔레메트리는 **Amatera**(Cline, Continue)와 **Remus**(Claude, Cursor, OpenCode) 탐지를 수만 명의 보호 사용자 사이에서 기록했다. **CallbackBeaver**는 Cursor와 Claude를 수집 범위에 추가했고 30일간 **5,000개 이상의 샘플**이 관측됐으며, BeeStealer, STG, HydraStealer, APEX, Otter로 확산되고 macOS에서는 **Djinn**이 같은 행동을 보인다. 수집되는 것은 환경설정이 아니라 **접근 권한과 맥락**이다. 액세스·리프레시 **토큰**, **MCP 설정**에 저장된 자격 증명, 프롬프트 기록, 대화 데이터베이스, 개발자가 다룬 프로젝트 흔적. 다음 날 **Okta 위협 인텔리전스 팀**은 구매자 쪽에서 같은 시장을 보여줬다. **5,871대**의 감염 단말에서 나온 무료 7GB 로그에 44,791개 JWT 중 **AI 서비스 관련 토큰 555개**와 유효한 AI API 키 24개가 들어 있었다

summary_de: |
  **Gen Digital** analysiert aktuelle Sammlungsregeln von Infostealern und findet eine neue Zielliste: lokale Daten von KI-Coding-Agenten und Entwicklerwerkzeugen – **Claude, Cline, Codex, Continue, Cursor, OpenCode** und weitere. Das ist kein Experiment: Über drei Monate verzeichnete die Telemetrie **Amatera**- (Cline, Continue) und **Remus**-Erkennungen (Claude, Cursor, OpenCode) bei Zehntausenden geschützten Nutzern; **CallbackBeaver** hat Cursor und Claude in seinen Sammlungsumfang aufgenommen, mit über **5.000 Proben in 30 Tagen**, und BeeStealer, STG, HydraStealer, APEX und Otter zeigen, wie sich das Verhalten ausbreitet – auf macOS tut **Djinn** dasselbe. Gesammelt werden nicht Einstellungen, sondern **Zugang und Kontext**: Access- und Refresh-**Token**, in **MCP-Konfigurationen** gespeicherte Zugangsdaten, Prompt-Verläufe, Gesprächsdatenbanken und Spuren der Projekte eines Entwicklers. Am Folgetag zeigte **Oktas Threat-Intelligence-Team** denselben Markt von der Käuferseite: Ein kostenloser 7-GB-Log-Dump von **5.871 infizierten Rechnern** enthielt unter 44.791 JWTs **555 Token mit Bezug zu KI-Diensten** und 24 noch gültige KI-API-Schlüssel

summary_fr: |
  **Gen Digital** analyse les règles de collecte récentes des infostealers et découvre une nouvelle liste de cibles : les données locales des agents de codage et outils de développement — **Claude, Cline, Codex, Continue, Cursor, OpenCode** et d'autres. Ce n'est pas une expérience : sur trois mois, sa télémétrie a relevé des détections **Amatera** (Cline, Continue) et **Remus** (Claude, Cursor, OpenCode) chez des dizaines de milliers d'utilisateurs protégés ; **CallbackBeaver** a ajouté Cursor et Claude à son périmètre, avec plus de **5 000 échantillons en 30 jours**, et BeeStealer, STG, HydraStealer, APEX et Otter montrent la diffusion de ce comportement, **Djinn** faisant de même sur macOS. Ce qui est collecté n'est pas un réglage mais **l'accès et le contexte** : **jetons** d'accès et de rafraîchissement, identifiants stockés dans les **configurations MCP**, historiques de prompts, bases de conversations et traces des projets d'un développeur. Le lendemain, l'équipe **threat intelligence d'Okta** a montré ce marché côté acheteur : un dump gratuit de 7 Go issu de **5 871 machines infectées** contenait **555 jetons liés à des services d'IA** parmi 44 791 JWT, et 24 clés d'API d'IA encore valides

summary_es: |
  **Gen Digital** analiza las recientes reglas de recolección de los infostealers y encuentra una nueva lista de objetivos: datos locales de agentes de programación y herramientas de desarrollo — **Claude, Cline, Codex, Continue, Cursor, OpenCode** y otros. No es un experimento: en tres meses, su telemetría registró detecciones de **Amatera** (Cline, Continue) y **Remus** (Claude, Cursor, OpenCode) entre decenas de miles de usuarios protegidos; **CallbackBeaver** sumó Cursor y Claude a su alcance con más de **5.000 muestras en 30 días**, y BeeStealer, STG, HydraStealer, APEX y Otter muestran la expansión, con **Djinn** haciendo lo mismo en macOS. Lo recolectado no son preferencias, sino **acceso y contexto**: **tokens** de acceso y refresco, credenciales guardadas en **configuraciones MCP**, historiales de prompts, bases de conversaciones y rastros de los proyectos de un desarrollador. Al día siguiente, el equipo de **threat intelligence de Okta** mostró ese mercado desde el lado del comprador: un volcado gratuito de 7 GB de **5.871 máquinas infectadas** contenía **555 tokens ligados a servicios de IA** entre 44.791 JWT, y 24 claves de API de IA aún válidas

sources:
  - url: https://www.gendigital.com/blog/insights/research/infostealers-your-ai-agent
    label: Gen Digital
  - url: https://www.okta.com/blog/threat-intelligence/signing_in_without_actually_signing_in/
    label: Okta Threat Intelligence
  - url: https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html
    label: The Hacker News
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-infostealer-ai-token-replay-20260911-csa-s/
    label: Cloud Security Alliance

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Infostealers turn to AI-agent data: collection rules now target Claude, Cursor and Codex

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

**Gen Digital** publishes an analysis of recent information-stealer collection rules and finds a new target list: local data belonging to AI coding agents and developer tools — **Claude, Cline, Codex, Continue, Cursor, OpenCode** and others. The targeting is not experimental. Over a three-month window, its telemetry recorded **Amatera** (Cline, Continue) and **Remus** (Claude, Cursor, OpenCode) detections among tens of thousands of protected users; **CallbackBeaver** has added Cursor and Claude to its collection scope with more than **5,000 samples in 30 days**, and BeeStealer, STG, HydraStealer, APEX and Otter show the behaviour spreading, with **Djinn** doing the same on macOS. What is collected is not preferences but **access and context**: access and refresh **tokens**, credentials stored in **MCP configurations**, prompt histories, conversation databases and traces of the projects a developer worked on. The following day, **Okta's threat-intelligence team** showed the same market from the buyer's side — a free 7 GB log dump from **5,871 infected machines** contained **555 tokens tied to AI services** among 44,791 JWTs, and 24 still-valid AI API keys

## Attack chain

```mermaid
flowchart LR
    E["An infostealer runs on a developer's machine"]:::entry
    S0["Its remotely updated collection rules include the agent's local paths: tokens, MCP configs, prompt histories"]:::step
    I["Account access and working context leave in one archive<br/><i>(Okta's August dump: 555 AI-service tokens among 44,791 JWTs)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The collection rules changed.** Gen Digital's starting observation is simple: alongside the familiar browser, wallet and credential targets, stealers' rule sets now include *“local data associated with Claude, Cline, Codex, Continue, Cursor, OpenCode, and other AI-assisted development tools.”* The evidence is spread across families and platforms. Amatera collects Cline and Continue data; Remus collects Claude, Cursor and OpenCode; CallbackBeaver, a fast-emerging stealer, added Cursor and Claude and was seen in more than 5,000 samples in a 30-day window; lower-prevalence families (BeeStealer, STG Stealer, HydraStealer, APEX Stealer, Otter Stealer) show the behaviour is not one group's specialty; and on macOS, Djinn collects from Claude, Codex, Gemini, Cline, OpenCode and Kilo. Gen Digital's summary of the pace: *“AI agent data appearing in the collection rules of another stealer almost every day.”* The scale context: in the first half of 2026 its telemetry recorded infostealer detections among more than **3.3 million** unique protected users, with monthly figures consistently above **500,000** — figures that describe detections of all stealers, not infections caused by these rules.

**Access and context in the same archive.** What an agent's local directory holds differs by product, but the material falls into two categories. The first is **account access**: cached access tokens that work until they expire, refresh tokens that can extend the window, and credentials embedded in MCP configuration files — endpoints, headers, environment variables, API keys. The second is **context**: prompts and transcripts that may contain proprietary source code, internal hostnames, pasted secrets, or the shape of unfinished work, plus the account details and file histories that profile the user. Gen Digital's framing: *“a browser cookie can open a door, but an AI-agent archive may also tell the attacker whose door it is, which projects are behind it, and which connected systems may be reachable from the same workspace.”* The caveats are stated: a stolen token's value depends on scope, lifetime and the service's controls, and short-lived credentials or OS-protected storage limit what a stolen configuration unlocks. The cost of expansion is trivial — most stealers take remotely managed collection rules, so adding a new agent's path needs no new malware build, only a configuration update.

**The following day, from the buyer's side.** On 9 September, Okta's threat-intelligence team (Jeremy Kirk) published an analysis of a 7 GB infostealer log dump released for free on Telegram on 2 August, covering 5,871 folders — each an infected machine — across 162 countries. Using pattern matching and the secret-scanner TruffleHog, it counted **44,791 unique JWTs**, of which **555 were tied to authentication for AI services**; the dataset also held **24 still-valid API keys** spanning Google Gemini, OpenAI, Groq and OpenRouter. Newer stealers, Okta writes, *“have added explicit regex or glob rules for Anthropic or OpenAI style API keys and known AI-tool config paths.”* The motive is direct: *“a stolen LLM API key is easy to monetize, allowing a buyer to run inference on someone else's tab.”* Okta is precise about what its data does and does not show — it describes tokens present in a criminal dump and their replayability, not observed account takeovers, and the financial-loss figures it cites (about $1 million, $25,000 and $600,000 in unauthorized usage) come from separately reported incidents.

**How this record reads it.** Nothing here is a new way to compromise a machine — the stealer is already running; what changed is that AI-agent credentials became predictable, valuable local files, and the criminal market adjusted in weeks. Both vendors state their limits, and this record keeps them: `real_harm: false` because the compile concerns a capability trend rather than a named victim of the AI-agent rules, `medium` severity because the underlying data — reusable tokens and MCP credentials — is genuinely sensitive, and the trend is one-way.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Gen Digital | <https://www.gendigital.com/blog/insights/research/infostealers-your-ai-agent> |
| 2 | Okta Threat Intelligence | <https://www.okta.com/blog/threat-intelligence/signing_in_without_actually_signing_in/> |
| 3 | The Hacker News | <https://thehackernews.com/2026/09/infostealer-logs-expose-replayable-ai.html> |
| 4 | Cloud Security Alliance | <https://labs.cloudsecurityalliance.org/research/csa-research-note-infostealer-ai-token-replay-20260911-csa-s/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-08` (raw: 2026-09-08, precision `day`) |
| Kind | Research demo `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary sources: Gen Digital's own telemetry analysis and Okta's own log-dump analysis, with an independent CSA review |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-08-gen-digital-infostealers-ai-agent-data` |

<sub>**Why this classification:** Both primary sources are first-hand vendor analyses of their own telemetry; the behaviour is real and measured, but no specific victim of the new AI-agent collection rules is named, so `real_harm: false` with `medium` severity. Okta's cross-dump evidence is folded in here rather than recorded separately — it measures the same week's market with data (a passing remark about AI-tool config paths is not a record on its own). Dated to Gen Digital's post (8 September 2026); Okta followed on 9 September. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-05-13` [OpenAI staff devices compromised via the TanStack incident](../2026-05/2026-05-13-tanstack-yuan-gong-she-bei.md)<br>  <sub>When a developer machine's stolen credentials travelled into an AI organisation</sub>
- `2026-06-24` [Operation Endgame (Europol) takes down StealC and Amadey](../2026-06/2026-06-24-operation-endgame-europol-stealc.md)<br>  <sub>The takedown wave this commodity market rebuilt after</sub>
- `2026-08-19` [Grok "cryptographic context injection": encrypted instructions, plaintext data](../2026-08/2026-08-19-grok-mi-ma-xue-wen.md)<br>  <sub>Another path from a developer's local context to credential exposure</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-08-gen-digital-infostealers-ai-agent-data.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
