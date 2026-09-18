---
id: 2026-01-29-openclaw-control-ui-websocket
title: "OpenClaw Control UI WebSocket hijack RCE"
title_zh: "OpenClaw Control UI WebSocket 劫持 RCE"
title_ja: "OpenClaw Control UIのWebSocketハイジャックRCE"
title_ko: "OpenClaw Control UI WebSocket 하이재킹 RCE"
title_de: "OpenClaw Control UI: WebSocket-Hijacking mit RCE"
title_fr: "Détournement de WebSocket de la Control UI d'OpenClaw (RCE)"
title_es: "Secuestro de WebSocket con RCE en la Control UI de OpenClaw"
date: 2026-01-29
date_precision: day
date_raw: "2026-01-29"

kind: incident
type: [INFRA]
severity: high
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Early discovery ahead of CVE-2026-25253


summary_zh: |
  CVE-2026-25253 的前期发现

summary_ja: |
  CVE-2026-25253に先立つ早期の発見

summary_ko: |
  CVE-2026-25253에 앞선 조기 발견

summary_de: |
  Frühe Entdeckung vor CVE-2026-25253

summary_fr: |
  Découverte précoce, avant le CVE-2026-25253

summary_es: |
  Descubrimiento temprano anterior a CVE-2026-25253

sources:
  - url: https://www.permissionprotocol.com/agent-incident-tracker
    label: Permission Protocol tracker

disputed: false
landmark: false
scan_month: 2026-01
scan_ref: "SCAN.md §6 2026-01"
---

# OpenClaw Control UI WebSocket hijack RCE

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Early discovery ahead of CVE-2026-25253

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
| 1 | Permission Protocol tracker | <https://www.permissionprotocol.com/agent-incident-tracker> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-01-29` (raw: 2026-01-29, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-01-29-openclaw-control-ui-websocket` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-01-26` [Clawdbot gateways exposed at scale](2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-02-10` [15,200 OpenClaw control panels exposed](../2026-02/2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>
- `2026-02-25` [OpenClaw ClawJacked (CVE-2026-25253)](../2026-02/2026-02-25-openclaw-clawjacked.md)<br>  <sub>OpenClaw ClawJacked (CVE-2026-25253)</sub>

---

[← 2026-01 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-01/2026-01-29-openclaw-control-ui-websocket.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
