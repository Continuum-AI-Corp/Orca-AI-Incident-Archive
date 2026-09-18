---
id: 2026-04-07-flowise-ye-li-yong
title: "Flowise CVE-2025-59528 exploited in the wild"
title_zh: "Flowise CVE-2025-59528 在野利用"
title_ja: "Flowise CVE-2025-59528が実悪用される"
title_ko: "Flowise CVE-2025-59528 실제 악용"
title_de: "Flowise CVE-2025-59528 in freier Wildbahn ausgenutzt"
title_fr: "CVE-2025-59528 de Flowise exploité en conditions réelles"
title_es: "CVE-2025-59528 de Flowise explotado en entornos reales"
date: 2026-04-07
date_precision: day
date_raw: "2026-04-07"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  12,000–15,000 exposed instances


summary_zh: |
  1.2 万–1.5 万个暴露实例

summary_ja: |
  12,000〜15,000のインスタンスが露出

summary_ko: |
  노출된 인스턴스 12,000~15,000개

summary_de: |
  12,000–15,000 exponierte Instanzen

summary_fr: |
  12 000 à 15 000 instances exposées

summary_es: |
  12,000–15,000 instancias expuestas

sources:
  - url: https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/
    label: "OWASP Q1'26"

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Flowise CVE-2025-59528 exploited in the wild

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

12,000–15,000 exposed instances

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak"]:::impact
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
| Date | `2026-04-07` (raw: 2026-04-07, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-07-flowise-ye-li-yong` |

<sub>**Why this classification:** Vulnerability disclosure with confirmed in-the-wild exploitation, so `real_harm: true`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-23` [OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed](2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-01` [Google Vertex AI "Double Agent" permission abuse](2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>
- `2026-04-06` [OpenClaw's CVE rate: 2.2 per day](2026-04-06-openclaw-chan-chu-su-lv.md)<br>  <sub>OpenClaw's CVE rate: 2.2 per day</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-07-flowise-ye-li-yong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
