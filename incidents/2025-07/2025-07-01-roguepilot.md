---
id: 2025-07-01-roguepilot
title: "RoguePilot"
title_zh: "RoguePilot"
title_ja: "RoguePilot"
title_ko: "RoguePilot"
title_de: "RoguePilot"
title_fr: "RoguePilot"
title_es: "RoguePilot"
date: 2025-07-01
date_precision: month
date_raw: "2025-07"

kind: research
type: [CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Orca Security: a **passive** prompt injection in GitHub Codespaces was enough to make Copilot spill its token and let the attacker take over the repository


summary_zh: |
  Orca Security：GitHub Codespaces 中的**被动**提示注入即可让 Copilot 吐出 token 并接管仓库

summary_ja: |
  Orca Security：GitHub Codespacesにおける**受動的な**プロンプトインジェクションだけで、Copilotにトークンを漏らさせ、攻撃者がリポジトリを乗っ取ることができた

summary_ko: |
  Orca Security: GitHub Codespaces에서의 **수동적** 프롬프트 인젝션만으로 Copilot이 토큰을 흘리게 하고 공격자가 저장소를 장악할 수 있었다

summary_de: |
  Orca Security: Eine **passive** Prompt-Injection in GitHub Codespaces genügte, damit Copilot sein Token preisgab und der Angreifer das Repository übernehmen konnte

summary_fr: |
  Orca Security : une injection de prompt **passive** dans GitHub Codespaces a suffi à faire fuiter le jeton de Copilot et à permettre à l'attaquant de prendre le contrôle du dépôt

summary_es: |
  Orca Security: una inyección de prompt **pasiva** en GitHub Codespaces bastó para que Copilot filtrara su token y el atacante tomara el control del repositorio

sources:
  - url: https://orca.security/resources/blog/roguepilot-github-copilot-vulnerability/
    label: Orca Security

disputed: false
landmark: true
scan_month: 2025-07
scan_ref: "SCAN.md §5 2025-07"
---

# RoguePilot

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Orca Security: a **passive** prompt injection in GitHub Codespaces was enough to make Copilot spill its token and let the attacker take over the repository

## Attack chain

```mermaid
flowchart LR
    E["Credentials within the agent's reach"]:::entry
    S0["The agent retrieves and uses them"]:::step
    I["Credential abuse<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Orca Security | <https://orca.security/resources/blog/roguepilot-github-copilot-vulnerability/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-07-01` (raw: 2025-07, precision `month`) |
| Kind | Research demo `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-07-01-roguepilot` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2025-07-09` [McHire flaw goes public](2025-07-09-mchire-lou-dong-gong-kai.md)<br>  <sub>McHire flaw goes public</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>
- `2025-08-26` [Nx "s1ngularity"](../2025-08/2025-08-26-nx-s1ngularity.md)<br>  <sub>Nx "s1ngularity"</sub>
- `2025-06-30` [McDonald's McHire "Olivia" hiring bot](../2025-06/2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>

---

[← 2025-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-07/2025-07-01-roguepilot.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
