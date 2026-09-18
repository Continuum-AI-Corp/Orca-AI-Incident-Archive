---
id: 2026-03-09-lilli-mai-ken-xi-shi
title: "McKinsey Lilli incident goes public"
title_zh: "麦肯锡 Lilli 事件公开"
title_ja: "マッキンゼーLilliインシデントが公表される"
title_ko: "맥킨지 Lilli 사건 공개"
title_de: "McKinsey: Lilli-Vorfall wird öffentlich"
title_fr: "L'incident McKinsey Lilli devient public"
title_es: "El incidente de Lilli de McKinsey se hace público"
date: 2026-03-09
date_precision: day
date_raw: "2026-03-09"

kind: incident
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [US]

summary: |
  See 2026-02-28


summary_zh: |
  见 2026-02-28

summary_ja: |
  2026-02-28を参照

summary_ko: |
  2026-02-28 항목 참조

summary_de: |
  Siehe 2026-02-28

summary_fr: |
  Voir 2026-02-28

summary_es: |
  Ver 2026-02-28

sources:
  - url: https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform
    label: CodeWall

disputed: false
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# McKinsey Lilli incident goes public

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

See 2026-02-28

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
| 1 | CodeWall | <https://codewall.ai/blog/how-we-hacked-mckinseys-ai-platform> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-09` (raw: 2026-03-09, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-03-09-lilli-mai-ken-xi-shi` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-03-27` [Langflow path traversal enables arbitrary file write](2026-03-27-langflow-lu-jing-chuan-yue.md)<br>  <sub>Langflow path traversal enables arbitrary file write</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-02-10` [15,200 OpenClaw control panels exposed](../2026-02/2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-09-lilli-mai-ken-xi-shi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
