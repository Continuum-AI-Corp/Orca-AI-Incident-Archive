---
id: 2026-04-17-meta-instagram-ke-fu-ji
title: "Meta AI support bot tricked into handing over an Instagram account"
title_zh: "Meta AI 客服机器人被骗交出 Instagram 账号"
title_ja: "MetaのAIサポートボットが騙されてInstagramアカウントを引き渡す"
title_ko: "Meta AI 지원 봇, 속아서 Instagram 계정을 넘겨주다"
title_de: "Meta-KI-Support-Bot dazu gebracht, ein Instagram-Konto herauszugeben"
title_fr: "Le bot de support IA de Meta piégé pour céder un compte Instagram"
title_es: "Engañan al bot de soporte de Meta AI para que entregue una cuenta de Instagram"
date: 2026-04-17
date_end: 2026-05-31
date_precision: day
date_raw: "2026-04-17→05-31"

kind: incident
type: [IPI, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  See the expanded entry in 2026-06


summary_zh: |
  见 2026-06 展开

summary_ja: |
  2026-06の詳細な項目を参照

summary_ko: |
  2026-06의 확장 항목 참조

summary_de: |
  Siehe den erweiterten Eintrag im 2026-06

summary_fr: |
  Voir la fiche développée en 2026-06

summary_es: |
  Ver la entrada ampliada en 2026-06

sources:
  - url: https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/
    label: Krebs

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Meta AI support bot tricked into handing over an Instagram account

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

See the expanded entry in 2026-06

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Krebs | <https://krebsonsecurity.com/2026/06/hackers-used-metas-ai-support-bot-to-seize-instagram-accounts/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-17` → `2026-05-31` (raw: 2026-04-17→05-31, precision `day`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-17-meta-instagram-ke-fu-ji` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-15` [ShareLeak (CVE-2026-21520) and PipeLeak](2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>
- `2026-04-19` [Vercel OAuth supply-chain intrusion](2026-04-19-vercel-oauth-gong-ying-lian.md)<br>  <sub>Vercel OAuth supply-chain intrusion</sub>
- `2026-04-21` [Unauthorised access to Anthropic's "Mythos"](2026-04-21-anthropic-mythos-zao-shou-quan.md)<br>  <sub>Unauthorised access to Anthropic's "Mythos"</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-17-meta-instagram-ke-fu-ji.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
