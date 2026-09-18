---
id: 2026-04-21-anthropic-mythos-zao-shou-quan
title: "Unauthorised access to Anthropic's \"Mythos\""
title_zh: "Anthropic \"Mythos\" 遭未授权访问"
title_ja: "Anthropicの「Mythos」への不正アクセス"
title_ko: "Anthropic \"Mythos\" 무단 접근"
title_de: "Unbefugter Zugriff auf Anthropics „Mythos“"
title_fr: "Accès non autorisé au « Mythos » d'Anthropic"
title_es: "Acceso no autorizado al \"Mythos\" de Anthropic"
date: 2026-04-21
date_precision: day
date_raw: "2026-04-21"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Accessed by unauthorised users through a third-party vendor's environment. The model has advanced reasoning and vulnerability-identification capabilities, a "step change" capability that cuts both ways for offence and defence


summary_zh: |
  经第三方供应商环境被未授权用户访问。该模型具备高级推理与漏洞识别能力，属攻防双向可转用的「阶跃」能力

summary_ja: |
  サードパーティベンダーの環境を通じて不正ユーザーにアクセスされた。このモデルは高度な推論と脆弱性特定能力を持ち、攻撃と防御の両面に作用する「段階的飛躍」の能力である

summary_ko: |
  제3자 벤더 환경을 통해 무단 사용자들이 접근했다. 이 모델은 고도화된 추론과 취약점 식별 능력을 갖추고 있으며, 공격과 방어 모두에 영향을 주는 "능력의 도약"이다

summary_de: |
  Über die Umgebung eines Drittanbieters von unbefugten Nutzern zugegriffen. Das Modell verfügt über fortgeschrittene Argumentations- und Schwachstellenerkennungsfähigkeiten, eine „Step-Change“-Fähigkeit, die für Offensive und Defensive gleichermaßen wirkt

summary_fr: |
  Accès par des utilisateurs non autorisés via l'environnement d'un fournisseur tiers. Le modèle possède des capacités avancées de raisonnement et d'identification de vulnérabilités, une capacité « de saut » à double tranchant pour l'offensive et la défensive

summary_es: |
  Accedido por usuarios no autorizados a través del entorno de un proveedor externo. El modelo tiene capacidades avanzadas de razonamiento e identificación de vulnerabilidades, una capacidad de "salto de nivel" que corta en ambos sentidos, para la ofensiva y la defensa

sources:
  - url: https://www.bloomberg.com/news/articles/2026-04-21/anthropic-s-mythos-model-is-being-accessed-by-unauthorized-users
    label: Bloomberg
  - url: https://www.reuters.com/technology/anthropics-mythos-model-accessed-by-unauthorized-users-bloomberg-news-reports-2026-04-21/
    label: Reuters

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Unauthorised access to Anthropic's "Mythos"

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Accessed by unauthorised users through a third-party vendor's environment. The model has advanced reasoning and vulnerability-identification capabilities, a "step change" capability that cuts both ways for offence and defence

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Bloomberg | <https://www.bloomberg.com/news/articles/2026-04-21/anthropic-s-mythos-model-is-being-accessed-by-unauthorized-users> |
| 2 | Reuters | <https://www.reuters.com/technology/anthropics-mythos-model-accessed-by-unauthorized-users-bloomberg-news-reports-2026-04-21/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-21` (raw: 2026-04-21, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-21-anthropic-mythos-zao-shou-quan` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-19` [Vercel OAuth supply-chain intrusion](2026-04-19-vercel-oauth-gong-ying-lian.md)<br>  <sub>Vercel OAuth supply-chain intrusion</sub>
- `2026-04-30` [Apple Support app ships an internal CLAUDE.md by mistake](2026-04-30-apple-support-app-claude-md.md)<br>  <sub>Apple Support app ships an internal CLAUDE.md by mistake</sub>
- `2026-04-17` [Meta AI support bot tricked into handing over an Instagram account](2026-04-17-meta-instagram-ke-fu-ji.md)<br>  <sub>Meta AI support bot tricked into handing over an Instagram account</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-21-anthropic-mythos-zao-shou-quan.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
