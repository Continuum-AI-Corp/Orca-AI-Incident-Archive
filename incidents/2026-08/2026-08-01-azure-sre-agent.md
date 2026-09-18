---
id: 2026-08-01-azure-sre-agent
title: "Azure SRE Agent privilege escalation (CVE-2026-62830)"
title_zh: "Azure SRE Agent 越权（CVE-2026-62830）"
title_ja: "Azure SRE Agentの権限昇格（CVE-2026-62830）"
title_ko: "Azure SRE Agent 권한 상승 (CVE-2026-62830)"
title_de: "Azure SRE Agent: Rechteerweiterung (CVE-2026-62830)"
title_fr: "Élévation de privilèges dans Azure SRE Agent (CVE-2026-62830)"
title_es: "Escalada de privilegios en Azure SRE Agent (CVE-2026-62830)"
date: 2026-08-01
date_precision: month
date_raw: "2026-08"

kind: vulnerability
type: [INFRA, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVSS 9.9**, missing authorization. Exploiting **a failure in the Scope-Changed OBO (on-behalf-of) flow**, an attacker can **inherit the agent's managed identity** and then modify runbooks, telemetry and infrastructure. The blast radius is not just the agent itself but **every infrastructure resource its managed identity can reach** — runbooks, telemetry, incident-handling tools and all the Azure resources they involve. Microsoft's fix is **server-side (customers need to patch nothing)**, and it recommends auditing managed identity assignments, reviewing RBAC, and monitoring for anomalous privilege escalation


summary_zh: |
  **CVSS 9.9**，授权缺失。利用 **Scope-Changed OBO（代表用户）流程的失效**，攻击者可**继承该 agent 的托管身份**，进而修改 runbook、遥测与基础设施。爆炸半径不止 agent 本身，而是**其托管身份能触达的每一个基础设施资源** —— runbook、遥测、事件处理工具及其涉及的全部 Azure 资源。微软做的是**服务端修复（客户无需打补丁）**，并建议审计托管身份分配、复查 RBAC、监控异常提权

summary_ja: |
  **CVSS 9.9**、認可の欠如。**Scope-Changed OBO（on-behalf-of）フローの不具合**を悪用し、攻撃者は**エージェントのマネージドIDを継承**して、ランブック、テレメトリ、インフラを改変できる。影響範囲はエージェント自体にとどまらず、**そのマネージドIDが到達できるすべてのインフラリソース**——ランブック、テレメトリ、インシデント対応ツール、およびそれらが関与するすべてのAzureリソースに及ぶ。Microsoftの修正は**サーバー側（顧客側のパッチ適用は不要）**で、マネージドIDの割り当ての監査、RBACの見直し、異常な権限昇格の監視を推奨している

summary_ko: |
  **CVSS 9.9**, 권한 부여 누락. **범위 변경 OBO(on-behalf-of) 흐름의 결함**을 악용해 공격자가 **에이전트의 관리 ID를 상속**한 뒤 런북, 텔레메트리, 인프라를 변경할 수 있다. 영향 범위는 에이전트 자체뿐 아니라 **그 관리 ID가 도달할 수 있는 모든 인프라 리소스** — 런북, 텔레메트리, 사고 대응 도구와 관련된 모든 Azure 리소스다. 마이크로소프트의 수정은 **서버 측**(고객이 패치할 필요 없음)이며, 관리 ID 할당 감사, RBAC 검토, 비정상 권한 상승 모니터링을 권고한다

summary_de: |
  **CVSS 9.9**, fehlende Autorisierung. Durch Ausnutzung **eines Fehlers im Scope-Changed-OBO-Flow (On-Behalf-Of)** kann ein Angreifer **die Managed Identity des Agenten übernehmen** und anschließend Runbooks, Telemetrie und Infrastruktur ändern. Der Wirkungsradius ist nicht nur der Agent selbst, sondern **jede Infrastrukturressource, die seine Managed Identity erreichen kann** — Runbooks, Telemetrie, Werkzeuge zur Incident-Bearbeitung und alle beteiligten Azure-Ressourcen. Microsofts Korrektur erfolgt **serverseitig (für Kunden ist kein Patch nötig)**, und es empfiehlt, Zuweisungen von Managed Identities zu prüfen, RBAC zu überprüfen und auf anomale Rechteerweiterungen zu überwachen

summary_fr: |
  **CVSS 9.9**, autorisation manquante. En exploitant **une défaillance du flux OBO (on-behalf-of) à changement de portée**, un attaquant peut **hériter de l'identité managée de l'agent** puis modifier les runbooks, la télémétrie et l'infrastructure. Le rayon d'impact ne se limite pas à l'agent lui-même mais à **toutes les ressources d'infrastructure que son identité managée peut atteindre** — runbooks, télémétrie, outils de traitement d'incidents et toutes les ressources Azure qu'ils impliquent. Le correctif de Microsoft est **côté serveur (rien à patcher pour les clients)**, et il recommande d'auditer les attributions d'identités managées, de revoir les RBAC et de surveiller toute élévation de privilèges anormale

summary_es: |
  **CVSS 9.9**, autorización ausente. Al explotar **un fallo en el flujo OBO (on-behalf-of) con Scope-Changed**, un atacante puede **heredar la identidad administrada del agente** y luego modificar runbooks, telemetría e infraestructura. El radio de impacto no es solo el agente en sí, sino **todos los recursos de infraestructura que su identidad administrada puede alcanzar** — runbooks, telemetría, herramientas de gestión de incidentes y todos los recursos de Azure que implican. La corrección de Microsoft es **del lado del servidor (los clientes no tienen que parchear nada)**, y recomienda auditar las asignaciones de identidad administrada, revisar el RBAC y monitorear la escalada de privilegios anómala

sources:
  - url: https://app.opencve.io/cve/CVE-2026-62830
    label: MSRC/OpenCVE
  - url: https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/
    label: Talos Patch Tuesday

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Azure SRE Agent privilege escalation (CVE-2026-62830)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**CVSS 9.9**, missing authorization. Exploiting **a failure in the Scope-Changed OBO (on-behalf-of) flow**, an attacker can **inherit the agent's managed identity** and then modify runbooks, telemetry and infrastructure. The blast radius is not just the agent itself but **every infrastructure resource its managed identity can reach** — runbooks, telemetry, incident-handling tools and all the Azure resources they involve. Microsoft's fix is **server-side (customers need to patch nothing)**, and it recommends auditing managed identity assignments, reviewing RBAC, and monitoring for anomalous privilege escalation

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | MSRC/OpenCVE | <https://app.opencve.io/cve/CVE-2026-62830> |
| 2 | Talos Patch Tuesday | <https://blog.talosintelligence.com/microsoft-patch-tuesday-for-august-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-01` (raw: 2026-08, precision `month`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-01-azure-sre-agent` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-08-25` [NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template](2026-08-25-nemoclaw-dns-zhong-bang-ding.md)<br>  <sub>NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template</sub>
- `2026-08-17` [AI finds a flaw AI helped write: Snowflake's Jira token](2026-08-17-snowflake-jira-zhao-dao-can.md)<br>  <sub>AI finds a flaw AI helped write: Snowflake's Jira token</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-01-azure-sre-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
