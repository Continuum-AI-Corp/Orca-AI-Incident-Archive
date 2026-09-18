---
id: 2026-05-04-braintrust-aws-zhang-hao-gong
title: "Braintrust's AWS account compromised, all customers told to rotate AI keys"
title_zh: "Braintrust 的 AWS 账号被攻陷，要求全体客户轮换 AI 密钥"
title_ja: "BraintrustのAWSアカウントが侵害され、全顧客にAIキーのローテーションを要求"
title_ko: "Braintrust AWS 계정 침해, 전 고객에 AI 키 교체 통보"
title_de: "Braintrusts AWS-Konto kompromittiert, alle Kunden zur Rotation der KI-Schlüssel aufgefordert"
title_fr: "Le compte AWS de Braintrust compromis, tous les clients invités à renouveler leurs clés IA"
title_es: "Comprometen la cuenta de AWS de Braintrust y piden a todos los clientes rotar las claves de IA"
date: 2026-05-04
date_precision: day
date_raw: "2026-05-04"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  AI **evaluation** platform Braintrust confirmed unauthorized access to one AWS account after spotting suspicious activity, **most likely exposing the organization-level AI provider API keys stored in Braintrust** (customers use them to reach cloud models). On 05-05 it told all customers to rotate. SecurityWeek: 1 customer confirmed affected, while 3 others reported **anomalous spikes in AI provider usage**


summary_zh: |
  AI **评测**平台 Braintrust 发现可疑活动后确认一个 AWS 账号被未授权访问，**很可能暴露了存放在 Braintrust 中的组织级 AI 提供方 API key**（客户用它连接云端模型）。05-05 通知全部客户轮换。SecurityWeek：已确认 1 家客户受影响，另有 3 家报告 **AI 提供方用量异常飙升**

summary_ja: |
  AI**評価**プラットフォームのBraintrustは、不審な活動を察知した後、1つのAWSアカウントへの不正アクセスを確認した。**Braintrustに保存されていた組織レベルのAIプロバイダーAPIキーが露出した可能性が高い**（顧客がクラウドモデルへのアクセスに使用）。05-05に全顧客へローテーションを指示。SecurityWeek：1社が影響を確認し、他3社が**AIプロバイダー使用量の異常な急増**を報告した

summary_ko: |
  AI **평가** 플랫폼 Braintrust는 의심스러운 활동을 발견한 뒤 AWS 계정 하나에 대한 무단 접근을 확인했고, **Braintrust에 저장된 조직 수준의 AI 제공자 API 키가 노출되었을 가능성이 크다**(고객이 클라우드 모델에 접근하는 데 사용한다). 05-05 전 고객에게 교체를 통보했다. SecurityWeek: 피해가 확인된 고객 1곳, **AI 제공자 사용량의 이상 급증**을 보고한 고객 3곳

summary_de: |
  Die KI-**Evaluierungs**plattform Braintrust bestätigte nach dem Entdecken verdächtiger Aktivitäten einen unbefugten Zugriff auf ein AWS-Konto und **legte dabei höchstwahrscheinlich die in Braintrust gespeicherten API-Schlüssel der KI-Anbieter auf Organisationsebene offen** (Kunden nutzen sie für den Zugriff auf Cloud-Modelle). Am 05-05 forderte sie alle Kunden zur Rotation auf. SecurityWeek: 1 Kunde bestätigte eine Betroffenheit, während 3 weitere **anomale Spitzen in der Nutzung von KI-Anbietern** meldeten

summary_fr: |
  La plateforme d'**évaluation** IA Braintrust a confirmé un accès non autorisé à un compte AWS après avoir repéré une activité suspecte, **exposant très probablement les clés API de fournisseurs d'IA au niveau organisation stockées dans Braintrust** (les clients les utilisent pour accéder aux modèles cloud). Le 05-05, elle a demandé à tous ses clients de les renouveler. SecurityWeek : 1 client a confirmé avoir été touché, tandis que 3 autres ont signalé **des pics anormaux d'usage de fournisseurs d'IA**

summary_es: |
  La plataforma de **evaluación** de IA Braintrust confirmó un acceso no autorizado a una cuenta de AWS tras detectar actividad sospechosa, **exponiendo muy probablemente las claves de API de proveedores de IA a nivel de organización almacenadas en Braintrust** (los clientes las usan para acceder a modelos en la nube). El 05-05 pidió a todos los clientes que las rotaran. SecurityWeek: 1 cliente confirmó verse afectado, mientras que otros 3 informaron de **picos anómalos en el uso de proveedores de IA**

sources:
  - url: https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/
    label: TechCrunch
  - url: https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/
    label: SecurityWeek

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Braintrust's AWS account compromised, all customers told to rotate AI keys

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

AI **evaluation** platform Braintrust confirmed unauthorized access to one AWS account after spotting suspicious activity, **most likely exposing the organization-level AI provider API keys stored in Braintrust** (customers use them to reach cloud models). On 05-05 it told all customers to rotate. SecurityWeek: 1 customer confirmed affected, while 3 others reported **anomalous spikes in AI provider usage**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | TechCrunch | <https://techcrunch.com/2026/05/06/ai-evaluation-startup-braintrust-confirms-breach-tells-every-customer-to-rotate-sensitive-keys/> |
| 2 | SecurityWeek | <https://www.securityweek.com/ai-firm-braintrust-prompts-api-key-rotation-after-data-breach/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-04` (raw: 2026-05-04, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-04-braintrust-aws-zhang-hao-gong` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-04-braintrust-aws-zhang-hao-gong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
