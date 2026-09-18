---
id: 2026-04-15-shareleak-pipeleak
title: "ShareLeak (CVE-2026-21520) and PipeLeak"
title_zh: "ShareLeak（CVE-2026-21520）+ PipeLeak"
title_ja: "ShareLeak（CVE-2026-21520）とPipeLeak"
title_ko: "ShareLeak (CVE-2026-21520)과 PipeLeak"
title_de: "ShareLeak (CVE-2026-21520) und PipeLeak"
title_fr: "ShareLeak (CVE-2026-21520) et PipeLeak"
title_es: "ShareLeak (CVE-2026-21520) y PipeLeak"
date: 2026-04-15
date_precision: day
date_raw: "2026-04-15"

kind: vulnerability
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Found by **Capsule Security** (**v1 mistakenly recorded this as Zenity and placed it in 2026-08**). ShareLeak: Copilot Studio concatenated SharePoint form submissions with the agent's system instructions **without any sanitisation**, so an injected fake system-role message directed the agent to query connected SharePoint lists for PII/leads/CRM data and send it through Outlook to a chosen address. CVSS 7.5, **patch deployed 2026-01-15**. PipeLeak: the same class of problem in Salesforce Agentforce, where **Salesforce assigned no CVE and issued no advisory**. VentureBeat notes: **even when security mechanisms flagged the attack, the data was still taken**


summary_zh: |
  **Capsule Security** 发现（**v1 误记为 Zenity、误置于 2026-08**）。ShareLeak：Copilot Studio 把 SharePoint 表单提交内容**未经任何净化**直接与 agent 系统指令拼接，注入的伪 system 角色消息指挥 agent 查询已连接的 SharePoint 列表取 PII/线索/CRM 数据，经 Outlook 发到指定地址。CVSS 7.5，**补丁 2026-01-15 部署**。PipeLeak：Salesforce Agentforce 的同类问题，**Salesforce 未分配 CVE、未发公告**。VentureBeat 指出：**即使安全机制标记了攻击，数据仍然被带走了**

summary_ja: |
  **Capsule Security**が発見（**v1では誤ってZenityと記録し、2026-08に配置していた**）。ShareLeak：Copilot StudioがSharePointのフォーム送信内容とエージェントのシステム指示を**一切サニタイズせずに**連結していたため、偽のsystemロールメッセージを注入して、エージェントに接続済みのSharePointリストからPII／リード／CRMデータを照会させ、Outlook経由で指定のアドレスへ送信させた。CVSS 7.5、**パッチは2026-01-15に適用**。PipeLeak：Salesforce Agentforceにおける同種の問題で、**SalesforceはCVEの割り当てもアドバイザリの発行も行わなかった**。VentureBeatは指摘する：**セキュリティ機構が攻撃を検知した場合でも、データは依然として持ち出された**

summary_ko: |
  **Capsule Security**가 발견했다(**v1에서는 Zenity로 잘못 기록하고 2026-08에 배치했다**). ShareLeak: Copilot Studio가 SharePoint 폼 제출 내용을 에이전트의 시스템 지시와 **아무 정제 없이** 이어 붙였고, 주입된 가짜 system 역할 메시지가 에이전트에게 연결된 SharePoint 목록에서 PII/리드/CRM 데이터를 조회해 Outlook으로 지정된 주소에 보내라고 지시했다. CVSS 7.5, **2026-01-15 패치 배포**. PipeLeak: Salesforce Agentforce의 같은 종류의 문제로, **Salesforce는 CVE를 부여하지도 권고를 발행하지도 않았다**. VentureBeat 지적: **보안 메커니즘이 공격을 감지했는데도 데이터는 빠져나갔다**

summary_de: |
  Gefunden von **Capsule Security** (**in v1 fälschlich als Zenity erfasst und in den 2026-08 einsortiert**). ShareLeak: Copilot Studio verknüpfte SharePoint-Formulareinsendungen mit den Systemanweisungen des Agenten **ohne jegliche Bereinigung**, sodass eine injizierte gefälschte System-Rollen-Nachricht den Agenten dazu brachte, verbundene SharePoint-Listen nach PII/Leads/CRM-Daten abzufragen und sie über Outlook an eine gewählte Adresse zu senden. CVSS 7.5, **Patch am 2026-01-15 ausgerollt**. PipeLeak: dieselbe Problemklasse in Salesforce Agentforce, wobei **Salesforce weder eine CVE vergab noch eine Meldung herausgab**. VentureBeat merkt an: **Selbst als Sicherheitsmechanismen den Angriff meldeten, wurden die Daten trotzdem abgegriffen**

summary_fr: |
  Trouvés par **Capsule Security** (**la v1 les a consignés par erreur comme étant de Zenity et placés en 2026-08**). ShareLeak : Copilot Studio concaténait les soumissions de formulaires SharePoint avec les instructions système de l'agent **sans aucune sanitisation**, si bien qu'un faux message injecté au rôle système dirigeait l'agent vers les listes SharePoint connectées pour y chercher des PII/pistes/données CRM et les envoyer via Outlook à une adresse choisie. CVSS 7.5, **correctif déployé le 2026-01-15**. PipeLeak : la même classe de problème dans Salesforce Agentforce, où **Salesforce n'a attribué aucun CVE et publié aucun avis**. VentureBeat note : **même lorsque les mécanismes de sécurité signalaient l'attaque, les données ont quand même été prises**

summary_es: |
  Encontrado por **Capsule Security** (**la v1 lo registró por error como Zenity y lo situó en 2026-08**). ShareLeak: Copilot Studio concatenaba los envíos de formularios de SharePoint con las instrucciones de sistema del agente **sin ninguna sanitización**, así que un mensaje inyectado con el rol de sistema falso dirigía al agente a consultar listas de SharePoint conectadas en busca de PII/leads/datos de CRM y enviarlos por Outlook a una dirección elegida. CVSS 7.5, **parche desplegado el 2026-01-15**. PipeLeak: el mismo tipo de problema en Salesforce Agentforce, donde **Salesforce no asignó ningún CVE y no emitió ningún aviso**. VentureBeat señala: **incluso cuando los mecanismos de seguridad marcaban el ataque, los datos igualmente fueron tomados**

sources:
  - url: https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook
    label: VentureBeat
  - url: https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520
    label: Capsule Security
  - url: https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws
    label: Dark Reading

disputed: true
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# ShareLeak (CVE-2026-21520) and PipeLeak

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully verified facts**; the accounts of the parties are kept side by side in the body — do not quote one side alone.

## Summary

Found by **Capsule Security** (**v1 mistakenly recorded this as Zenity and placed it in 2026-08**). ShareLeak: Copilot Studio concatenated SharePoint form submissions with the agent's system instructions **without any sanitisation**, so an injected fake system-role message directed the agent to query connected SharePoint lists for PII/leads/CRM data and send it through Outlook to a chosen address. CVSS 7.5, **patch deployed 2026-01-15**. PipeLeak: the same class of problem in Salesforce Agentforce, where **Salesforce assigned no CVE and issued no advisory**. VentureBeat notes: **even when security mechanisms flagged the attack, the data was still taken**

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
| 1 | VentureBeat | <https://venturebeat.com/security/microsoft-salesforce-copilot-agentforce-prompt-injection-cve-agent-remediation-playbook> |
| 2 | Capsule Security | <https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520> |
| 3 | Dark Reading | <https://www.darkreading.com/cloud-security/microsoft-salesforce-patch-ai-agent-data-leak-flaws> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-15` (raw: 2026-04-15, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-15-shareleak-pipeleak` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-17` [Meta AI support bot tricked into handing over an Instagram account](2026-04-17-meta-instagram-ke-fu-ji.md)<br>  <sub>Meta AI support bot tricked into handing over an Instagram account</sub>
- `2026-04-07` [GrafanaGhost indirect prompt injection](2026-04-07-grafanaghost-jian-jie-ti-shi.md)<br>  <sub>GrafanaGhost indirect prompt injection</sub>
- `2026-03-01` [Claudy Day: a three-flaw chain in claude.ai](../2026-03/2026-03-01-claudy-day-claude-ai.md)<br>  <sub>Claudy Day: a three-flaw chain in claude.ai</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-15-shareleak-pipeleak.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
