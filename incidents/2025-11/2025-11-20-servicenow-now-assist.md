---
id: 2025-11-20-servicenow-now-assist
title: "ServiceNow Now Assist second-order prompt injection"
title_zh: "ServiceNow Now Assist 二阶提示注入"
title_ja: "ServiceNow Now Assistの二次プロンプトインジェクション"
title_ko: "ServiceNow Now Assist 이차 프롬프트 인젝션"
title_de: "ServiceNow Now Assist: Prompt-Injection zweiter Ordnung"
title_fr: "Injection de prompt de second ordre dans ServiceNow Now Assist"
title_es: "Inyección de prompt de segundo orden en ServiceNow Now Assist"
date: 2025-11-20
date_precision: day
date_raw: "2025-11-20"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  AppOmni: agents send instructions to one another; a low-privilege agent can drive a high-privilege agent to modify records, send email and escalate privileges


summary_zh: |
  AppOmni：agent 之间互相发指令，低权限 agent 可驱使高权限 agent 改记录、发邮件、提权

summary_ja: |
  AppOmni：エージェント同士が指示を送り合うため、低権限のエージェントが高権限のエージェントを操作してレコードの変更、メール送信、権限昇格を行わせることができる

summary_ko: |
  AppOmni: 에이전트가 다른 에이전트에게 지시를 보내며, 낮은 권한의 에이전트가 높은 권한의 에이전트를 부려 레코드 수정, 이메일 발송, 권한 상승을 수행하게 할 수 있다

summary_de: |
  AppOmni: Agenten senden einander Anweisungen; ein Agent mit geringen Rechten kann einen Agenten mit hohen Rechten dazu bringen, Datensätze zu ändern, E-Mails zu senden und Rechte zu erweitern

summary_fr: |
  AppOmni : des agents s'envoient des instructions entre eux ; un agent à faibles privilèges peut pousser un agent à hauts privilèges à modifier des enregistrements, envoyer des e-mails et élever ses privilèges

summary_es: |
  AppOmni: los agentes se envían instrucciones entre sí; un agente con privilegios bajos puede llevar a un agente con privilegios altos a modificar registros, enviar correo y escalar privilegios

sources:
  - url: https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html
    label: THN

disputed: false
landmark: false
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# ServiceNow Now Assist second-order prompt injection

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

AppOmni: agents send instructions to one another; a low-privilege agent can drive a high-privilege agent to modify records, send email and escalate privileges

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2025/11/servicenow-ai-agents-can-be-tricked.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-20` (raw: 2025-11-20, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-20-servicenow-now-assist` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-10-02` [CometJacking](../2025-10/2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak (GitHub Copilot Chat)](../2025-10/2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling: agents deceiving agents over A2A](../2025-10/2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave discloses screenshot-based injection in Comet](../2025-10/2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-20-servicenow-now-assist.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
