---
id: 2026-06-04-claude-oceanus-fei-fa-fen
title: "Claude Oceanus-v1-p illegally redistributed"
title_zh: "Claude Oceanus-v1-p 被非法分发"
title_ja: "Claude Oceanus-v1-pが不正に再配布される"
title_ko: "Claude Oceanus-v1-p 불법 재배포"
title_de: "Claude Oceanus-v1-p unrechtmäßig weiterverbreitet"
title_fr: "Redistribution illégale de Claude Oceanus-v1-p"
title_es: "Redistribución ilegal de Claude Oceanus-v1-p"
date: 2026-06-04
date_precision: day
date_raw: "2026-06-04"

kind: vulnerability
type: [CRED]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL, CN]

summary: |
  A next-generation model released only to a handful of red teams was abused through distribution channels as soon as evaluation began, with **API access resold illegally via China-based proxy services**. Anthropic paused red-team access and opened an internal investigation


summary_zh: |
  仅对少数红队开放的下一代模型，评测刚开始就被滥用分发渠道，**经中国的代理服务非法转售 API 访问**。Anthropic 暂停红队访问并内部调查

summary_ja: |
  一握りのレッドチームにのみ提供された次世代モデルが、評価開始と同時に流通チャネルを通じて悪用され、**APIアクセスが中国拠点のプロキシサービス経由で不正に転売された**。Anthropicはレッドチームへの提供を一時停止し、社内調査を開始した

summary_ko: |
  소수의 레드팀에만 공개된 차세대 모델이 평가가 시작되자마자 유통 경로를 통해 악용되었고, **중국 기반 프록시 서비스로 API 접근이 불법 재판매**되었다. Anthropic은 레드팀 접근을 중단하고 내부 조사에 착수했다

summary_de: |
  Ein Modell der nächsten Generation, das nur an eine Handvoll Red Teams ausgegeben wurde, wurde über Vertriebskanäle missbraucht, sobald die Evaluierung begann, wobei **API-Zugang über Proxy-Dienste mit Sitz in China illegal weiterverkauft wurde**. Anthropic setzte den Red-Team-Zugang aus und eröffnete eine interne Untersuchung

summary_fr: |
  Un modèle de nouvelle génération distribué seulement à une poignée d'équipes de red-team a été détourné par les canaux de distribution dès le début de l'évaluation, avec **un accès API revendu illégalement via des services proxy basés en Chine**. Anthropic a suspendu l'accès red-team et ouvert une enquête interne

summary_es: |
  Un modelo de nueva generación entregado solo a un puñado de equipos de red-team fue abusado a través de canales de distribución en cuanto comenzó la evaluación, con **acceso a la API revendido ilegalmente mediante servicios proxy con base en China**. Anthropic pausó el acceso de los red-teams y abrió una investigación interna

sources:
  - url: https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/
    label: CybersecurityNews

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Claude Oceanus-v1-p illegally redistributed

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A next-generation model released only to a handful of red teams was abused through distribution channels as soon as evaluation began, with **API access resold illegally via China-based proxy services**. Anthropic paused red-team access and opened an internal investigation

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
| 1 | CybersecurityNews | <https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-04` (raw: 2026-06-04, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) · [China](../../regions/cn.md) |
| Archive ID | `2026-06-04-claude-oceanus-fei-fa-fen` |

<sub>**Why this classification:** Vulnerability disclosure; in-the-wild exploitation is confirmed, so `real_harm: true`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-13` [PromptSnatcher: ad-blocking extensions steal AI conversations](2026-06-13-promptsnatcher-guang-gao-lan-jie.md)<br>  <sub>PromptSnatcher: ad-blocking extensions steal AI conversations</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-04-claude-oceanus-fei-fa-fen.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
