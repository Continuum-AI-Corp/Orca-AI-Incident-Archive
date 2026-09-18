---
id: 2026-03-01-metr-api-key
title: "METR API key stolen, $600K of credit burned"
title_zh: "METR API key 被盗，$60 万额度被消耗"
title_ja: "METRのAPIキーが窃取され、60万ドル分のクレジットが消費される"
title_ko: "METR API 키 탈취, 60만 달러 상당 크레딧 소진"
title_de: "METR-API-Schlüssel gestohlen, $600K Guthaben verbraucht"
title_fr: "Clé API de METR volée, 600 000 $ de crédit consumés"
title_es: "Roban la clave de API de METR y se consumen $600K de crédito"
date: 2026-03-01
date_precision: month
date_raw: "2026-03"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  A researcher ran an agent on a **personal EC2** instance protected by Google authentication, but the vibe-coded app **held an API key for METR's public model account**, and a **fail-open flaw** in the authentication silently disabled it for several days. The attacker **induced the agent to hand over the model provider's API key** and added an SSH key for persistence, then burned roughly **$600,000** worth of credit over three weeks (supplied free by the model vendor, so it is commercial value rather than a direct loss). Because METR itself runs large-scale evaluations and its token consumption is naturally enormous and uncapped, it went unnoticed for a long time. Disclosed 2026-08-31


summary_zh: |
  研究员在**个人 EC2** 上跑 agent，用 Google 认证保护，但该 vibe-coded 应用**持有 METR 公共模型账号的 API key**，且认证存在 **fail-open 缺陷**静默失效数日。攻击者**诱导 agent 吐出模型提供方 API key**并加了 SSH 密钥持久化，随后三周消耗价值约 **$600,000** 的额度（由模型厂商免费提供，故为商业价值非直接损失）。因 METR 本身跑大规模评测、token 消耗天然巨大且无上限，故长期未被发现。2026-08-31 披露

summary_ja: |
  研究者がGoogle認証で保護された**個人のEC2**上でエージェントを実行したが、そのバイブコーディング製アプリは**METRの公開モデルアカウントのAPIキーを保持**しており、認証の**フェイルオープン欠陥**により数日間それが静かに無効化されていた。攻撃者は**エージェントを誘導してモデルプロバイダーのAPIキーを渡させ**、永続化のためにSSHキーを追加。3週間で約**60万ドル**相当のクレジットを消費した（モデルベンダーが無償提供したもので、直接的損失ではなく商業的価値）。METR自体が大規模評価を実行しており、トークン消費が元々膨大で上限もないため、長期間気づかれなかった。2026-08-31に公表

summary_ko: |
  한 연구자가 Google 인증으로 보호되는 **개인 EC2** 인스턴스에서 에이전트를 실행했는데, 바이브 코딩한 앱이 **METR 공개 모델 계정의 API 키를 보유**하고 있었고 인증의 **페일 오픈 결함**으로 며칠간 조용히 비활성화되어 있었다. 공격자는 **에이전트를 유도해 모델 제공자의 API 키를 넘겨받고** 지속성을 위해 SSH 키를 추가한 뒤, 3주에 걸쳐 약 **60만 달러** 상당의 크레딧을 소진했다(모델 벤더가 무료 제공한 것으로 직접 손실이 아닌 상업적 가치다). METR 자체가 대규모 평가를 수행해 토큰 소비가 원래 막대하고 상한이 없어 오랫동안 발견되지 않았다. 2026-08-31 공개

summary_de: |
  Ein Forscher betrieb einen Agenten auf einer **persönlichen EC2**-Instanz, die durch Google-Authentifizierung geschützt war, doch die per Vibe Coding erstellte App **besaß einen API-Schlüssel für METRs öffentliches Modellkonto**, und ein **Fail-Open-Fehler** in der Authentifizierung deaktivierte sie mehrere Tage lang stillschweigend. Der Angreifer **brachte den Agenten dazu, den API-Schlüssel des Modellanbieters herauszugeben**, fügte für die Persistenz einen SSH-Schlüssel hinzu und verbrauchte dann über drei Wochen Guthaben im Wert von rund **$600,000** (vom Modellanbieter kostenlos bereitgestellt, also kommerzieller Wert und kein direkter Verlust). Da METR selbst groß angelegte Evaluierungen durchführt und sein Tokenverbrauch naturgemäß enorm und ungedeckelt ist, blieb es lange unbemerkt. Offengelegt am 2026-08-31

summary_fr: |
  Un chercheur a fait tourner un agent sur une **EC2 personnelle** protégée par authentification Google, mais l'application vibe-codée **détenait une clé API du compte de modèles public de METR**, et **une faille fail-open** de l'authentification l'a silencieusement désactivée pendant plusieurs jours. L'attaquant **a amené l'agent à remettre la clé API du fournisseur de modèles** et a ajouté une clé SSH pour la persistance, puis a consumé environ **600 000 $** de crédit en trois semaines (fourni gratuitement par le fournisseur de modèles, donc une valeur commerciale plutôt qu'une perte directe). Comme METR mène elle-même de grandes campagnes d'évaluation et que sa consommation de tokens est naturellement énorme et non plafonnée, le tout est passé inaperçu longtemps. Divulgué le 2026-08-31

summary_es: |
  Un investigador ejecutó un agente en una instancia **EC2 personal** protegida por autenticación de Google, pero la aplicación hecha a base de vibes **contenía una clave de API de la cuenta pública de modelos de METR**, y un **fallo fail-open** en la autenticación la desactivó silenciosamente durante varios días. El atacante **indujo al agente a entregar la clave de API del proveedor de modelos** y añadió una clave SSH para persistencia, y luego consumió unos **$600,000** de crédito en tres semanas (suministrado gratis por el proveedor de modelos, así que es valor comercial y no una pérdida directa). Como METR realiza evaluaciones a gran escala y su consumo de tokens es naturalmente enorme y sin límite, pasó desapercibido mucho tiempo. Divulgado el 2026-08-31

sources:
  - url: https://metr.org/blog/2026-08-31-security-update/
    label: METR official
  - url: https://www.theregister.com/security/2026/09/01/attacker-stole-a-metr-api-key-used-600k-worth-of-credits-and-no-one-noticed-for-weeks/5293730
    label: The Register

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# METR API key stolen, $600K of credit burned

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A researcher ran an agent on a **personal EC2** instance protected by Google authentication, but the vibe-coded app **held an API key for METR's public model account**, and a **fail-open flaw** in the authentication silently disabled it for several days. The attacker **induced the agent to hand over the model provider's API key** and added an SSH key for persistence, then burned roughly **$600,000** worth of credit over three weeks (supplied free by the model vendor, so it is commercial value rather than a direct loss). Because METR itself runs large-scale evaluations and its token consumption is naturally enormous and uncapped, it went unnoticed for a long time. Disclosed 2026-08-31

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | METR official | <https://metr.org/blog/2026-08-31-security-update/> |
| 2 | The Register | <https://www.theregister.com/security/2026/09/01/attacker-stole-a-metr-api-key-used-600k-worth-of-credits-and-no-one-noticed-for-weeks/5293730> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-01` (raw: 2026-03, precision `month`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-03-01-metr-api-key` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-26` [Anthropic CMS misconfiguration reveals the existence of "Mythos"](2026-03-26-anthropic-cms-mythos.md)<br>  <sub>Anthropic CMS misconfiguration reveals the existence of "Mythos"</sub>
- `2026-03-31` [Anthropic Claude Code source code leak](2026-03-31-anthropic-claude-code.md)<br>  <sub>Anthropic Claude Code source code leak</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-01-metr-api-key.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
