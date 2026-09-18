---
id: 2025-08-28-transunion-jing-di-san-fang
title: "TransUnion leaks 4.4-4.5M people via a third-party app"
title_zh: "TransUnion 经第三方应用泄露 440–450 万人数据"
title_ja: "TransUnion、第三者アプリ経由で440万〜450万人分が漏えい"
title_ko: "TransUnion, 서드파티 앱을 통해 440만~450만 명 정보 유출"
title_de: "TransUnion: Daten von 4.4-4.5M Personen über eine Drittanbieter-App preisgegeben"
title_fr: "TransUnion expose les données de 4,4 à 4,5 millions de personnes via une application tierce"
title_es: "TransUnion filtra 4.4-4.5M de personas a través de una app de terceros"
date: 2025-08-28
date_precision: day
date_raw: "2025-08-28"

kind: incident
type: [CRED]
severity: high
confidence: B
real_harm: true
ai_involvement: not-applicable

region: [US]

summary: |
  The data was stolen from its **Salesforce account**, including names, billing addresses, phone numbers, emails, dates of birth and **unmasked Social Security numbers**.
  ⚠️ **v1 misrecorded it as a "follow-on to the Drift incident"**: the intrusion actually happened on **2025-07-28** (discovered two days later), **earlier than the Drift/UNC6395 campaign (08-08→18)**, and belongs to a separate Salesforce social-engineering chain. **It has no direct connection to AI agents; it is listed only to tell the two apart, and is not recommended for inclusion**


summary_zh: |
  数据从其 **Salesforce 账户**被窃，含姓名、账单地址、电话、邮箱、生日与**未脱敏社保号**。
  ⚠️ **v1 误记为「Drift 事件后续」**：入侵实际发生在 **2025-07-28**（两天后发现），**早于 Drift/UNC6395 战役（08-08→18）**，属另一条 Salesforce 社工链。**与 AI agent 无直接关系，列此仅供区分，建议不入库**

summary_ja: |
  データは同社の**Salesforceアカウント**から窃取され、氏名、請求先住所、電話番号、メール、生年月日、**マスクされていない社会保障番号**が含まれていた。
  ⚠️ **v1では「Driftインシデントの後続」と誤記録**：侵入は実際には**2025-07-28**（2日後に発見）に発生しており、**Drift/UNC6395キャンペーン（08-08→18）より前**で、別のSalesforceソーシャルエンジニアリング・チェーンに属する。**AIエージェントとは直接関係がなく、両者を区別するために掲載しているもので、収録は推奨しない**

summary_ko: |
  데이터는 **Salesforce 계정**에서 탈취되었으며 이름, 청구 주소, 전화번호, 이메일, 생년월일, **마스킹 해제된 사회보장번호**가 포함되었다.
  ⚠️ **v1에서는 "Drift 사건의 후속"으로 잘못 기록했다**: 실제 침해는 **2025-07-28**에 발생했고(이틀 뒤 발견) **Drift/UNC6395 작전(08-08→18)보다 이르며**, 별개의 Salesforce 소셜 엔지니어링 체인에 속한다. **AI 에이전트와 직접적 관련이 없고, 두 사건을 구분하기 위해 기재한 것으로 등재는 권장하지 않는다**

summary_de: |
  Die Daten wurden aus seinem **Salesforce-Konto** gestohlen, darunter Namen, Rechnungsadressen, Telefonnummern, E-Mails, Geburtsdaten und **unmaskierte Sozialversicherungsnummern**.
  ⚠️ **In v1 wurde es fälschlich als „Folge des Drift-Vorfalls“ erfasst**: Die Intrusion geschah tatsächlich am **2025-07-28** (zwei Tage später entdeckt), **früher als die Drift/UNC6395-Kampagne (08-08→18)**, und gehört zu einer separaten Salesforce-Social-Engineering-Kette. **Es besteht keine direkte Verbindung zu KI-Agenten; der Eintrag dient nur der Unterscheidung und wird nicht zur Aufnahme empfohlen**

summary_fr: |
  Les données ont été volées depuis son **compte Salesforce**, incluant noms, adresses de facturation, numéros de téléphone, e-mails, dates de naissance et **numéros de sécurité sociale non masqués**.
  ⚠️ **La v1 l'a consigné à tort comme une « suite de l'incident Drift »** : l'intrusion a en réalité eu lieu le **2025-07-28** (découverte deux jours plus tard), **plus tôt que la campagne Drift/UNC6395 (08-08→18)**, et relève d'une chaîne d'ingénierie sociale Salesforce distincte. **Elle n'a aucun lien direct avec les agents IA ; elle n'est répertoriée que pour distinguer les deux affaires, et son inclusion n'est pas recommandée**

summary_es: |
  Los datos se robaron de su **cuenta de Salesforce**, e incluían nombres, direcciones de facturación, teléfonos, correos, fechas de nacimiento y **números de Seguro Social sin enmascarar**.
  ⚠️ **La v1 lo registró erróneamente como un "seguimiento del incidente Drift"**: la intrusión en realidad ocurrió el **2025-07-28** (descubierta dos días después), **antes que la campaña Drift/UNC6395 (08-08→18)**, y pertenece a una cadena separada de ingeniería social contra Salesforce. **No tiene conexión directa con agentes de IA; se lista solo para distinguir ambas cosas, y no se recomienda incluirla**

sources:
  - url: https://www.bleepingcomputer.com/news/security/transunion-suffers-data-breach-impacting-over-44-million-people/
    label: BleepingComputer
  - url: https://www.theregister.com/2025/08/28/transunion_support_app_breach/
    label: The Register

disputed: true
landmark: false
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# TransUnion leaks 4.4-4.5M people via a third-party app

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: not-applicable](https://img.shields.io/badge/AI_involvement-not--applicable-9AA8AD?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully confirmed facts**; the claims of each party are kept side by side in the body, so do not cite any single one of them in isolation.

## Summary

The data was stolen from its **Salesforce account**, including names, billing addresses, phone numbers, emails, dates of birth and **unmasked Social Security numbers**.

⚠️ **v1 misrecorded it as a "follow-on to the Drift incident"**: the intrusion actually happened on **2025-07-28** (discovered two days later), **earlier than the Drift/UNC6395 campaign (08-08→18)**, and belongs to a separate Salesforce social-engineering chain. **It has no direct connection to AI agents; it is listed only to tell the two apart, and is not recommended for inclusion**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within the agent's reach"]:::entry
    S0["The agent retrieves and uses it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/transunion-suffers-data-breach-impacting-over-44-million-people/> |
| 2 | The Register | <https://www.theregister.com/2025/08/28/transunion_support_app_breach/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-28` (raw: 2025-08-28, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Not applicable `not-applicable` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-08-28-transunion-jing-di-san-fang` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-08-08` [Salesloft Drift OAuth token theft](2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-26` [Nx "s1ngularity"](2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>
- `2025-09-15` [Shai-Hulud npm worm v1](../2025-09/2025-09-15-shai-hulud-npm.md)<br>  <sub>Shai-Hulud npm worm v1</sub>
- `2025-07-01` [RoguePilot](../2025-07/2025-07-01-roguepilot.md)<br>  <sub>RoguePilot</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-28-transunion-jing-di-san-fang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
