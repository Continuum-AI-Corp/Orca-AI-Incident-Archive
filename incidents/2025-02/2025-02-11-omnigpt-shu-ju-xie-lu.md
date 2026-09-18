---
id: 2025-02-11-omnigpt-shu-ju-xie-lu
title: "OmniGPT data leak (claimed)"
title_zh: "OmniGPT 数据泄露（声称）"
title_ja: "OmniGPTのデータ漏えい（主張）"
title_ko: "OmniGPT 데이터 유출(주장)"
title_de: "OmniGPT-Datenleck (behauptet)"
title_fr: "Fuite de données chez OmniGPT (revendiquée)"
title_es: "Fuga de datos de OmniGPT (presunta)"
date: 2025-02-11
date_precision: day
date_raw: "2025-02-11"

kind: incident
type: [OTHER]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Someone using the handle "Gloomer" posted samples on BreachForums, claiming 30,000 users' emails/phones plus **34 million lines of chat logs** with API keys, credentials and billing data. OmniGPT is an intermediary that aggregates GPT-4o/Claude 3.5/Gemini. **The platform has not confirmed it**; strictly speaking this is an aggregator rather than an agent, a borderline entry


summary_zh: |
  化名 "Gloomer" 者在 BreachForums 挂出样本，称获 3 万用户邮箱/电话 + **3,400 万行聊天记录**，含 API key、凭据、账单。OmniGPT 是聚合 GPT-4o/Claude 3.5/Gemini 的中间商。**平台方未确认**；严格说属聚合器而非 agent，边界条目

summary_ja: |
  「Gloomer」を名乗る人物がBreachForumsにサンプルを投稿し、3万人分のユーザーのメールアドレス・電話番号に加え、APIキー、認証情報、請求データを含む**3,400万行のチャットログ**を主張した。OmniGPTはGPT-4o/Claude 3.5/Geminiを集約する仲介サービス。**プラットフォーム側は確認していない**。厳密にはエージェントではなくアグリゲーターであり、境界的なエントリ

summary_ko: |
  "Gloomer"라는 핸들을 쓰는 인물이 BreachForums에 샘플을 게시하며 사용자 3만 명의 이메일/전화번호와 API 키, 자격 증명, 결제 데이터가 포함된 **3,400만 줄의 채팅 로그**를 주장했다. OmniGPT는 GPT-4o/Claude 3.5/Gemini를 통합하는 중개 서비스다. **플랫폼은 이를 확인하지 않았다**. 엄밀히 말해 에이전트가 아닌 집계 서비스로, 경계선상의 항목이다

summary_de: |
  Jemand mit dem Handle „Gloomer“ veröffentlichte Proben auf BreachForums und behauptete, 30,000 E-Mails/Telefonnummern von Nutzern sowie **34 Millionen Zeilen Chatprotokolle** mit API-Schlüsseln, Zugangsdaten und Abrechnungsdaten zu haben. OmniGPT ist ein Vermittler, der GPT-4o/Claude 3.5/Gemini bündelt. **Die Plattform hat es nicht bestätigt**; streng genommen ist dies ein Aggregator und kein Agent, ein Grenzfall-Eintrag

summary_fr: |
  Une personne utilisant le pseudonyme « Gloomer » a publié des échantillons sur BreachForums, revendiquant les e-mails/téléphones de 30 000 utilisateurs ainsi que **34 millions de lignes de journaux de chat** contenant des clés API, des identifiants et des données de facturation. OmniGPT est un intermédiaire qui agrège GPT-4o/Claude 3.5/Gemini. **La plateforme n'a pas confirmé** ; à strictement parler, c'est un agrégateur et non un agent, une entrée limite

summary_es: |
  Alguien con el alias "Gloomer" publicó muestras en BreachForums, afirmando tener correos y teléfonos de 30,000 usuarios más **34 millones de líneas de registros de chat** con claves de API, credenciales y datos de facturación. OmniGPT es un intermediario que agrega GPT-4o/Claude 3.5/Gemini. **La plataforma no lo ha confirmado**; en rigor se trata de un agregador y no de un agente, una entrada limítrofe

sources:
  - url: https://siliconangle.com/2025/02/12/ai-aggregator-omnigpt-reportedly-breached-sensitive-user-data-leaked-online/
    label: SiliconANGLE
  - url: https://hackread.com/omnigpt-ai-chatbot-breach-hacker-leak-user-data-messages/
    label: HackRead

disputed: false
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# OmniGPT data leak (claimed)

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Someone using the handle "Gloomer" posted samples on BreachForums, claiming 30,000 users' emails/phones plus **34 million lines of chat logs** with API keys, credentials and billing data. OmniGPT is an intermediary that aggregates GPT-4o/Claude 3.5/Gemini. **The platform has not confirmed it**; strictly speaking this is an aggregator rather than an agent, a borderline entry

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | SiliconANGLE | <https://siliconangle.com/2025/02/12/ai-aggregator-omnigpt-reportedly-breached-sensitive-user-data-leaked-online/> |
| 2 | HackRead | <https://hackread.com/omnigpt-ai-chatbot-breach-hacker-leak-user-data-messages/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-11` (raw: 2025-02-11, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-02-11-omnigpt-shu-ju-xie-lu` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-11-omnigpt-shu-ju-xie-lu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
