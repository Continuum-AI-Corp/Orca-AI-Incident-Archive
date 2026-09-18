---
id: 2026-07-27-jfrog-artifactory-fa-bu-jiu
title: "JFrog patches nine Artifactory CVEs"
title_zh: "JFrog 发布 Artifactory 九个 CVE 补丁"
title_ja: "JFrogがArtifactoryの9件のCVEを修正"
title_ko: "JFrog, Artifactory CVE 9건 패치"
title_de: "JFrog patcht neun Artifactory-CVEs"
title_fr: "JFrog corrige neuf CVE d'Artifactory"
title_es: "JFrog parchea nueve CVE de Artifactory"
date: 2026-07-27
date_precision: day
date_raw: "2026-07-27"

kind: policy
type: [INFRA]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Related to the OpenAI escape incident; the one disclosed is CVE-2026-65617 (High), and **neither JFrog nor OpenAI has said which zero-day was actually used in the evaluation**


summary_zh: |
  与 OpenAI 逃逸事件相关；公开的是 CVE-2026-65617（High），**评测中实际用到的是哪个零日，JFrog 与 OpenAI 均未说明**

summary_ja: |
  OpenAIの脱出インシデントに関連。公表されたのはCVE-2026-65617（High）で、**JFrogもOpenAIも、評価で実際に使われたゼロデイがどれかは明らかにしていない**

summary_ko: |
  OpenAI 탈출 사건과 관련이 있다. 공개된 것은 CVE-2026-65617(높음)이며, **JFrog도 OpenAI도 평가에서 실제로 어떤 제로데이가 사용되었는지는 밝히지 않았다**

summary_de: |
  Im Zusammenhang mit dem OpenAI-Escape-Vorfall; die offengelegte ist CVE-2026-65617 (High), und **weder JFrog noch OpenAI haben gesagt, welcher Zero-Day in der Evaluierung tatsächlich genutzt wurde**

summary_fr: |
  En lien avec l'incident d'évasion d'OpenAI ; celle divulguée est CVE-2026-65617 (High), et **ni JFrog ni OpenAI n'ont dit quel zero-day a réellement été utilisé dans l'évaluation**

summary_es: |
  Relacionado con el incidente de escape de OpenAI; el divulgado es CVE-2026-65617 (Alta), y **ni JFrog ni OpenAI han dicho qué zero-day se usó realmente en la evaluación**

sources:
  - url: https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/
    label: JFrog

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# JFrog patches nine Artifactory CVEs

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Related to the OpenAI escape incident; the one disclosed is CVE-2026-65617 (High), and **neither JFrog nor OpenAI has said which zero-day was actually used in the evaluation**

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | JFrog | <https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-27` (raw: 2026-07-27, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-27-jfrog-artifactory-fa-bu-jiu` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-07-30` [RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm](2026-07-30-rufroot-man-fen-zhao-huan.md)<br>  <sub>RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm</sub>
- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping](../2026-06/2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-27-jfrog-artifactory-fa-bu-jiu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
