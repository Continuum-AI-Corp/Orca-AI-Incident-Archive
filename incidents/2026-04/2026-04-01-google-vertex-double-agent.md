---
id: 2026-04-01-google-vertex-double-agent
title: "Google Vertex AI \"Double Agent\" permission abuse"
title_zh: "Google Vertex AI「Double Agent」权限滥用"
title_ja: "Google Vertex AI「Double Agent」の権限悪用"
title_ko: "Google Vertex AI \"Double Agent\" 권한 악용"
title_de: "Google Vertex AI: Rechtemissbrauch durch „Double Agent“"
title_fr: "Abus de permissions « Double Agent » dans Google Vertex AI"
title_es: "Abuso de permisos del \"Double Agent\" de Google Vertex AI"
date: 2026-04-01
date_precision: day
date_raw: "2026-04-01"

kind: research
type: [INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Unit 42: an over-privileged service agent can reach producer project resources, internal artifacts and consumer data


summary_zh: |
  Unit 42：过度授权的服务 agent 可访问 producer 项目资源、内部构件与 consumer 数据

summary_ja: |
  Unit 42：過剰な権限を持つサービスエージェントが、プロデューサープロジェクトのリソース、内部アーティファクト、コンシューマーデータに到達できる

summary_ko: |
  Unit 42: 과도한 권한을 가진 서비스 에이전트가 프로듀서 프로젝트 리소스, 내부 아티팩트, 소비자 데이터에 접근할 수 있다

summary_de: |
  Unit 42: Ein überprivilegierter Service-Agent kann auf Ressourcen des Produzentenprojekts, interne Artefakte und Verbraucherdaten zugreifen

summary_fr: |
  Unit 42 : un agent de service sur-privilégié peut atteindre les ressources du projet producteur, des artefacts internes et les données des consommateurs

summary_es: |
  Unit 42: un agente de servicio con privilegios excesivos puede alcanzar recursos del proyecto productor, artefactos internos y datos de consumidores

sources:
  - url: https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
    label: "OWASP Q1'26"

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Google Vertex AI "Double Agent" permission abuse

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Unit 42: an over-privileged service agent can reach producer project resources, internal artifacts and consumer data

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OWASP Q1'26 | <https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-01` (raw: 2026-04-01, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-01-google-vertex-double-agent` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 exploited in the wild](2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-23` [OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed](2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-06` [OpenClaw's CVE rate: 2.2 per day](2026-04-06-openclaw-chan-chu-su-lv.md)<br>  <sub>OpenClaw's CVE rate: 2.2 per day</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-01-google-vertex-double-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
