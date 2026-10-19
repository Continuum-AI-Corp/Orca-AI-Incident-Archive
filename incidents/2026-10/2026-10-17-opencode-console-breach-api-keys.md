---
id: 2026-10-17-opencode-console-breach-api-keys
title: "OpenCode Console breach exposes users' stored AI-provider API keys"
title_zh: "OpenCode Console 被攻破，泄露用户存储的 AI 提供方 API 密钥"
title_ja: "OpenCode Consoleが侵害され、ユーザー保存のAIプロバイダーAPIキーが流出"
title_ko: "OpenCode Console 침해로 사용자가 저장한 AI 제공업체 API 키 유출"
title_de: "OpenCode-Console-Einbruch legt gespeicherte KI-Anbieter-API-Schlüssel der Nutzer offen"
title_fr: "Une brèche dans OpenCode Console expose les clés API de fournisseurs d'IA stockées par les utilisateurs"
title_es: "Una brecha en OpenCode Console expone las claves API de proveedores de IA almacenadas por los usuarios"
date: 2026-10-17
date_raw: "2026-10-17 (OpenCode disclosure); intrusion overnight 2026-10-16 to 2026-10-17"
date_precision: day

kind: incident
type: [CRED, INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **OpenCode — an open-source AI coding agent — disclosed on 17 October 2026 that an unauthorized party reached a **legacy Console system it was decommissioning** and exposed the third-party **AI-provider API keys (OpenAI, Anthropic, Google)** that the Console had stored in users' workspaces.** OpenCode called it a *"large-scale distillation attack"* and said it affected about **1.4% of Console users** — the subset who had external providers linked. The stolen keys were **actively abused**: named users reported unauthorized charges, including **$281 (OpenAI) + $168 (Anthropic)**, **over $700**, and **$1,700**, as attackers ran queries against high-end models on the victims' accounts. OpenCode notified affected users by email, said it is working with all three providers, and urged users to **revoke and rotate** their keys. The company has not published a total loss figure or a post-mortem. Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true` — a credential breach of an agent platform with confirmed financial harm.

summary_zh: |
  **开源 AI 编码 agent **OpenCode** 于 2026 年 10 月 17 日披露：一名未授权方入侵了其**正在退役的遗留 Console 系统**，泄露了 Console 存放在用户工作区中的**第三方 AI 提供方 API 密钥（OpenAI、Anthropic、Google）**。** OpenCode 称其为一次*"大规模蒸馏攻击（distillation attack）"*，影响约 **1.4% 的 Console 用户**——即那些关联了外部提供方的用户。被盗密钥**已被实际滥用**：多名具名用户报告了未授权扣费，包括 **$281（OpenAI）+ $168（Anthropic）**、**700 多美元**、**$1,700**——攻击者用受害者账户去跑高端模型。OpenCode 已邮件通知受影响用户，称正与三家提供方协作处置，并敦促用户**吊销并轮换**密钥。公司尚未公布总损失或事后分析。记为 `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`——一次 agent 平台的凭据泄露，且有确认的财务损失。

summary_ja: |
  **オープンソースのAIコーディングエージェント **OpenCode** は2026年10月17日、未承認の第三者が**廃止作業中のレガシーConsoleシステム**に侵入し、Consoleがユーザーのワークスペースに保存していた**第三者AIプロバイダーのAPIキー（OpenAI、Anthropic、Google）**を流出させたと公表した。** OpenCodeはこれを*「大規模なディスティレーション攻撃」*と呼び、**Consoleユーザーの約1.4%**（外部プロバイダーを連携していた層）に影響したとした。盗まれたキーは**実際に悪用**され、具名のユーザーが**$281（OpenAI）+$168（Anthropic）**、**700ドル超**、**$1,700**の不正請求を報告した。攻撃者が被害者のアカウントで高性能モデルにクエリを実行したためである。OpenCodeは影響を受けたユーザーにメールで通知し、3社と協力して対応中とし、キーの**失効と再発行**を促した。総損失額や事後分析は未公表。`incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_ko: |
  **오픈소스 AI 코딩 에이전트 **OpenCode**는 2026년 10월 17일, 무단 침입자가 **폐기 작업 중이던 레거시 Console 시스템**에 접근해 Console이 사용자 워크스페이스에 저장해 둔 **제3자 AI 제공업체 API 키(OpenAI, Anthropic, Google)**를 유출시켰다고 공개했다.** OpenCode는 이를 *"대규모 디스틸레이션 공격"*이라 부르며 **Console 사용자 약 1.4%**(외부 제공업체를 연결한 사용자)가 영향을 받았다고 밝혔다. 탈취된 키는 **실제로 악용**되어, 실명 사용자들이 **$281(OpenAI)+$168(Anthropic)**, **700달러 이상**, **$1,700**의 무단 청구를 보고했다. 공격자가 피해자 계정으로 고성능 모델에 쿼리를 실행했기 때문이다. OpenCode는 영향받은 사용자에게 이메일로 통지했고 세 제공업체와 협력 중이라며 키 **폐기 및 교체**를 권고했다. 총 손실액이나 사후 분석은 미공개. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_de: |
  **OpenCode — ein quelloffener KI-Coding-Agent — teilte am 17. Oktober 2026 mit, dass ein Unbefugter auf ein **außer Betrieb genommenes Legacy-Console-System** zugriff und die **API-Schlüssel von KI-Drittanbietern (OpenAI, Anthropic, Google)** offenlegte, die die Console in den Workspaces der Nutzer gespeichert hatte.** OpenCode nannte es einen *"groß angelegten Distillation-Angriff"* und erklärte, es seien etwa **1,4% der Console-Nutzer** betroffen — jene mit verknüpften externen Anbietern. Die gestohlenen Schlüssel wurden **aktiv missbraucht**: namentlich genannte Nutzer meldeten unbefugte Abbuchungen, darunter **281 $ (OpenAI) + 168 $ (Anthropic)**, **über 700 $** und **1.700 $**, da Angreifer über die Konten der Opfer Anfragen an Hochleistungsmodelle stellten. OpenCode benachrichtigte Betroffene per E-Mail, arbeitet mit allen drei Anbietern zusammen und forderte zum **Widerrufen und Rotieren** der Schlüssel auf. Eine Gesamtschadenssumme oder Nachanalyse wurde nicht veröffentlicht. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_fr: |
  **OpenCode — un agent de codage IA open source — a révélé le 17 octobre 2026 qu'un tiers non autorisé a atteint un **ancien système Console en cours de mise hors service** et exposé les **clés API de fournisseurs d'IA tiers (OpenAI, Anthropic, Google)** que la Console stockait dans les espaces de travail des utilisateurs.** OpenCode a parlé d'une *« attaque de distillation à grande échelle »* et dit qu'environ **1,4 % des utilisateurs de Console** étaient touchés — ceux ayant lié des fournisseurs externes. Les clés volées ont été **activement exploitées** : des utilisateurs nommés ont signalé des frais non autorisés, dont **281 $ (OpenAI) + 168 $ (Anthropic)**, **plus de 700 $** et **1 700 $**, les attaquants exécutant des requêtes sur des modèles haut de gamme via les comptes des victimes. OpenCode a prévenu les utilisateurs concernés par e-mail, dit travailler avec les trois fournisseurs et exhorté à **révoquer et faire tourner** les clés. Aucun montant total ni post-mortem n'a été publié. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_es: |
  **OpenCode —un agente de codificación de IA de código abierto— reveló el 17 de octubre de 2026 que un tercero no autorizado accedió a un **sistema Console heredado que estaba dando de baja** y expuso las **claves API de proveedores de IA externos (OpenAI, Anthropic, Google)** que la Console almacenaba en los espacios de trabajo de los usuarios.** OpenCode lo llamó un *"ataque de destilación a gran escala"* y dijo que afectó a cerca del **1,4 % de los usuarios de Console** —los que tenían proveedores externos vinculados—. Las claves robadas fueron **activamente abusadas**: usuarios con nombre reportaron cargos no autorizados, incluidos **$281 (OpenAI) + $168 (Anthropic)**, **más de $700** y **$1,700**, al ejecutar los atacantes consultas contra modelos de gama alta en las cuentas de las víctimas. OpenCode notificó por correo a los afectados, dijo estar trabajando con los tres proveedores e instó a **revocar y rotar** las claves. No ha publicado una cifra total de pérdidas ni un análisis posterior. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

sources:
  - url: https://dealroom.co/news/163473-opencode-breach-drains-users-ai-keys-as-platforms-holding-customer-crede/
    label: Dealroom (quotes OpenCode's X post + customer email)
  - url: https://cryptobriefing.com/opencode-distillation-attack-api-key-breach/
    label: Crypto Briefing
  - url: https://startupfortune.com/opencode-breach-exposes-stored-openai-and-anthropic-keys-prompts-urgent-key-rotation/
    label: Startup Fortune
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.31"
---

# OpenCode Console breach exposes users' stored AI-provider API keys

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**OpenCode — an open-source AI coding agent — disclosed on 17 October 2026 that an unauthorized party reached a legacy Console system it was decommissioning and exposed the third-party AI-provider API keys (OpenAI, Anthropic, Google) that the Console had stored in users' workspaces.** OpenCode called it a *"large-scale distillation attack"* and said it affected about **1.4% of Console users** — the subset who had external providers linked. The stolen keys were **actively abused**: named users reported unauthorized charges, including **$281 (OpenAI) + $168 (Anthropic)**, **over $700**, and **$1,700**, as attackers ran queries against high-end models on the victims' accounts. OpenCode notified affected users by email, said it is working with all three providers, and urged users to **revoke and rotate** their keys. The company has not published a total loss figure or a post-mortem. Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true` — a credential breach of an agent platform with confirmed financial harm.

## Attack chain

```mermaid
flowchart LR
    E["Unauthorized access to OpenCode's legacy<br/>Console (being decommissioned)"]:::entry
    S1["Provider API keys (OpenAI/Anthropic/Google)<br/>stored in user workspaces exposed"]:::step
    S2["Keys abused to run queries against high-end<br/>models (the 'distillation attack')"]:::step
    I["~1.4% of Console users; named victims<br/>billed $168–$1,700"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **17 October 2026** OpenCode — an open-source AI coding agent whose cloud Console lets users link external model providers — disclosed (via its X account and an email to affected users) that an unauthorized party had gained access to a **legacy Console system that was in the process of being decommissioned**. The intrusion happened overnight from **16 to 17 October**. The provider **API keys stored in users' workspaces** — covering OpenAI, Anthropic and Google — were exposed. OpenCode characterised the event as a *"large-scale distillation attack."*

**Scope and harm.** OpenCode said about **1.4% of Console users** were affected — specifically those who had external providers linked — and that it notified each by email (users who were not emailed were not affected). The stolen keys were **used**: individual users publicly reported unauthorized charges on their provider bills, including **$281 on OpenAI plus $168 on Anthropic** (Colin Parsons), **over $700** of OpenAI usage (Francisco Giancarelli), and **$1,700** (Preston Zeller). The pattern — running many queries against expensive frontier models on someone else's key — is the "distillation" framing. OpenCode has **not** published a total number of affected accounts beyond the percentage, a total loss figure, an indicator list, or a post-mortem; it says it is working with OpenAI, Anthropic and Google on remediation.

**How it is graded.** Recorded `incident` — a real breach, not a disclosed-but-unused flaw. `CRED` (what is lost is the **keys** — users' stored provider API credentials) and `INFRA` (the compromised asset is the agent platform's own Console service). `real_harm: true`: unlike a demo, this exposed live keys that were abused for real, with named users reporting real financial charges. Severity `high` rather than `critical`: there is confirmed harm but the scope is bounded (≈1.4% of one product's Console users; billing abuse rather than deeper system compromise), and no provider-account takeover beyond API billing is reported. Confidence `A`: the disclosure is OpenCode's own (X post + customer email), corroborated by multiple independent outlets and by named victims posting their charges — though note no tier-1 security outlet had covered it at the time of recording and OpenCode has not released a full post-mortem.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Dealroom (quotes OpenCode's X post + customer email) | <https://dealroom.co/news/163473-opencode-breach-drains-users-ai-keys-as-platforms-holding-customer-crede/> |
| 2 | Crypto Briefing | <https://cryptobriefing.com/opencode-distillation-attack-api-key-breach/> |
| 3 | Startup Fortune | <https://startupfortune.com/opencode-breach-exposes-stored-openai-and-anthropic-keys-prompts-urgent-key-rotation/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-17` (raw: 2026-10-17 OpenCode disclosure; intrusion overnight 2026-10-16 to 2026-10-17, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **High** `high` |
| Confidence | **A** — OpenCode's own disclosure (X + customer email) + independent reporting + named victims |
| Real harm | Yes — provider API keys exposed and abused; named users reported $168–$1,700 in unauthorized charges |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-17-opencode-console-breach-api-keys` |

<sub>**Why this classification:** A breach of the OpenCode coding-agent Console that exposed users' stored AI-provider API keys (`CRED` — the loss is the keys; `INFRA` — the agent platform's own Console was the compromised asset). `incident` with `real_harm: true` because the keys were abused and named users reported real charges. `high` not `critical`: confirmed harm but bounded scope (≈1.4% of Console users, billing abuse). Confidence `A` on OpenCode's own disclosure plus independent reporting and named victims. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-08` [AgentCorruption — one prompt takes over an AWS Bedrock AgentCore account](2026-10-08-agentcorruption-aws-bedrock-agentcore.md)<br>  <sub>Another agent-platform compromise exposing stored credentials</sub>
- `2026-10-08` [Tensorlake npm SDK compromise harvests agent config and credentials](2026-10-08-tensorlake-npm-sdk-compromise.md)<br>  <sub>Same week — stealing agent provider keys and config</sub>
- `2026-10-02` [Loom for AWS agent-control-plane auth bypass (CVE-2026-103956)](2026-10-02-loom-aws-agent-control-plane-cve-2026-103956.md)<br>  <sub>Another agent platform exposing stored integration credentials</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-17-opencode-console-breach-api-keys.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
