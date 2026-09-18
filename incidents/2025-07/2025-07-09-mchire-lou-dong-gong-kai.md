---
id: 2025-07-09-mchire-lou-dong-gong-kai
title: "McHire flaw goes public"
title_zh: "McHire 漏洞公开"
title_ja: "McHireの欠陥が公表される"
title_ko: "McHire 취약점 공개"
title_de: "McHire-Schwachstelle wird öffentlich"
title_fr: "La faille McHire devient publique"
title_es: "El fallo de McHire se hace público"
date: 2025-07-09
date_precision: day
date_raw: "2025-07-09"

kind: incident
type: [CRED]
severity: low
confidence: A
real_harm: false
ai_involvement: confirmed

region: [US]

summary: |
  See 2025-06-30


summary_zh: |
  见 2025-06-30

summary_ja: |
  2025-06-30の項目を参照

summary_ko: |
  2025-06-30 항목 참조

summary_de: |
  Siehe 2025-06-30

summary_fr: |
  Voir 2025-06-30

summary_es: |
  Ver 2025-06-30

sources:
  - url: https://incidentdatabase.ai/cite/1179/
    label: "AIID #1179"

disputed: false
landmark: false
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# McHire flaw goes public

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

See 2025-06-30

## Attack chain

```mermaid
flowchart LR
    E["Credentials within the agent's reach"]:::entry
    S0["The agent retrieves and uses them"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | AIID #1179 | <https://incidentdatabase.ai/cite/1179/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-07-09` (raw: 2025-07-09, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Low** `low` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-07-09-mchire-lou-dong-gong-kai` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-07-01` [RoguePilot](2025-07-01-roguepilot.md)<br>  <sub>RoguePilot</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-26` [Nx "s1ngularity"](../2025-08/2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>
- `2025-06-30` [McDonald's McHire "Olivia" hiring bot](../2025-06/2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-09-mchire-lou-dong-gong-kai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
