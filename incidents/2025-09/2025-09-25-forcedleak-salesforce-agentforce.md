---
id: 2025-09-25-forcedleak-salesforce-agentforce
title: "ForcedLeak (Salesforce Agentforce)"
title_zh: "ForcedLeak（Salesforce Agentforce）"
title_ja: "ForcedLeak（Salesforce Agentforce）"
title_ko: "ForcedLeak (Salesforce Agentforce)"
title_de: "ForcedLeak (Salesforce Agentforce)"
title_fr: "ForcedLeak (Salesforce Agentforce)"
title_es: "ForcedLeak (Salesforce Agentforce)"
date: 2025-09-25
date_precision: day
date_raw: "2025-09-25"

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Noma Security, **CVSS 9.4**. All an attacker needs is a public Web-to-Lead form plus **$5** to buy up an **expired Salesforce CSP allow-listed domain**, and they can exfiltrate any Agentforce organization's CRM data with zero interaction


summary_zh: |
  Noma Security，**CVSS 9.4**。攻击者只需一个公开 Web-to-Lead 表单 + 花 **$5** 买下 Salesforce **已过期的 CSP 白名单域名**，即可零交互外带任意 Agentforce 组织的 CRM 数据

summary_ja: |
  Noma Security、**CVSS 9.4**。攻撃者に必要なのは公開のWeb-to-Leadフォームと、**期限切れのSalesforce CSP許可ドメイン**を買うための**5ドル**だけで、Agentforce組織のCRMデータをゼロ操作で外部送信できる

summary_ko: |
  Noma Security, **CVSS 9.4**. 공격자에게 필요한 것은 공개 Web-to-Lead 폼과 **만료된 Salesforce CSP 허용 목록 도메인**을 사들이는 **5달러**뿐이며, 상호작용 없이 어떤 Agentforce 조직의 CRM 데이터든 유출할 수 있다

summary_de: |
  Noma Security, **CVSS 9.4**. Ein Angreifer braucht nur ein öffentliches Web-to-Lead-Formular plus **$5**, um eine **abgelaufene, in der Salesforce-CSP-Positivliste geführte Domain** zu kaufen, und kann dann mit null Interaktion die CRM-Daten jeder Agentforce-Organisation exfiltrieren

summary_fr: |
  Noma Security, **CVSS 9.4**. Il suffit à un attaquant d'un formulaire Web-to-Lead public plus **5 $** pour racheter un **domaine CSP Salesforce expiré figurant en liste blanche**, et il peut exfiltrer les données CRM de n'importe quelle organisation Agentforce sans aucune interaction

summary_es: |
  Noma Security, **CVSS 9.4**. Todo lo que necesita un atacante es un formulario público Web-to-Lead más **$5** para comprar un **dominio vencido que esté en la lista de permitidos del CSP de Salesforce**, y puede exfiltrar los datos de CRM de cualquier organización Agentforce con cero interacción

sources:
  - url: https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce
    label: Noma Security

disputed: false
landmark: true
scan_month: 2025-09
scan_ref: "SCAN.md §5 2025-09"
---

# ForcedLeak (Salesforce Agentforce)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Noma Security, **CVSS 9.4**. All an attacker needs is a public Web-to-Lead form plus **$5** to buy up an **expired Salesforce CSP allow-listed domain**, and they can exfiltrate any Agentforce organization's CRM data with zero interaction

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Noma Security | <https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-09-25` (raw: 2025-09-25, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-09-25-forcedleak-salesforce-agentforce` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-09-18` [ShadowLeak](2025-09-18-shadowleak.md)<br>  <sub>ShadowLeak</sub>
- `2025-09-19` [Notion 3.0 agent hits the lethal trifecta](2025-09-19-notion-agent-zhi-ming-san.md)<br>  <sub>Notion 3.0 agent hits the lethal trifecta</sub>
- `2025-09-30` [Gemini "Trifecta"](2025-09-30-gemini-trifecta.md)<br>  <sub>Gemini "Trifecta"</sub>
- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>

---

[← 2025-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-09/2025-09-25-forcedleak-salesforce-agentforce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
