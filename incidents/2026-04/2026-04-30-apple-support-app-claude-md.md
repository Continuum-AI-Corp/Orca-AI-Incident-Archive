---
id: 2026-04-30-apple-support-app-claude-md
title: "Apple Support app ships an internal CLAUDE.md by mistake"
title_zh: "Apple Support App 误发布内部 CLAUDE.md"
title_ja: "Apple Supportアプリが社内CLAUDE.mdを誤って出荷"
title_ko: "Apple 지원 앱, 실수로 내부 CLAUDE.md 포함"
title_de: "Apple-Support-App liefert versehentlich eine interne CLAUDE.md aus"
title_fr: "L'app Apple Support embarque par erreur un CLAUDE.md interne"
title_es: "La app de soporte de Apple publica por error un CLAUDE.md interno"
date: 2026-04-30
date_precision: day
date_raw: "2026-04-30"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  The v5.13 production build shipped an internal configuration file meant for Claude Code, leaking internal architecture decisions such as the "Juno AI" design, the Actor concurrency model and the UI component library. What leaked was **development standards and architecture decisions** rather than user data, but it handed attackers a map of the attack surface


summary_zh: |
  v5.13 生产构建中混入给 Claude Code 用的内部配置文件，泄露 "Juno AI" 设计、Actor 并发模型、UI 组件库等内部架构决策。暴露的是**开发标准与架构决策**而非用户数据，但给了攻击者攻击面地图

summary_ja: |
  v5.13の本番ビルドに、Claude Code向けの社内設定ファイルが含まれて出荷され、「Juno AI」の設計、Actor並行モデル、UIコンポーネントライブラリといった社内のアーキテクチャ決定が漏えいした。漏れたのはユーザーデータではなく**開発標準とアーキテクチャ決定**だったが、攻撃者に攻撃面の地図を渡すことになった

summary_ko: |
  v5.13 프로덕션 빌드에 Claude Code용 내부 설정 파일이 포함되어 "Juno AI" 설계, Actor 동시성 모델, UI 컴포넌트 라이브러리 같은 내부 아키텍처 결정이 유출되었다. 유출된 것은 사용자 데이터가 아니라 **개발 표준과 아키텍처 결정**이었지만, 공격자에게 공격 표면 지도를 쥐여준 셈이다

summary_de: |
  Der Produktions-Build v5.13 lieferte eine interne Konfigurationsdatei aus, die für Claude Code gedacht war, und gab interne Architekturentscheidungen preis, etwa das Design von „Juno AI“, das Actor-Nebenläufigkeitsmodell und die UI-Komponentenbibliothek. Preisgegeben wurden **Entwicklungsstandards und Architekturentscheidungen** und keine Nutzerdaten, doch Angreifer erhielten damit eine Karte der Angriffsfläche

summary_fr: |
  La build de production v5.13 a embarqué un fichier de configuration interne destiné à Claude Code, divulguant des décisions d'architecture interne comme la conception « Juno AI », le modèle de concurrence Actor et la bibliothèque de composants UI. Ce qui a fuité, ce sont **des normes de développement et des décisions d'architecture** plutôt que des données utilisateurs, mais cela a donné aux attaquants une carte de la surface d'attaque

summary_es: |
  La compilación de producción v5.13 incluyó un archivo de configuración interno destinado a Claude Code, filtrando decisiones de arquitectura internas como el diseño de "Juno AI", el modelo de concurrencia de Actor y la biblioteca de componentes de UI. Lo filtrado fueron **estándares de desarrollo y decisiones de arquitectura** y no datos de usuarios, pero entregó a los atacantes un mapa de la superficie de ataque

sources:
  - url: https://x.com/aaronp613/status/2049986504617820551
    label: Original post (X)
  - url: https://medium.com/vibe-coding/what-apples-leaked-claude-md-teaches-us-b8269e2ace51
    label: Medium analysis

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Apple Support app ships an internal CLAUDE.md by mistake

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

The v5.13 production build shipped an internal configuration file meant for Claude Code, leaking internal architecture decisions such as the "Juno AI" design, the Actor concurrency model and the UI component library. What leaked was **development standards and architecture decisions** rather than user data, but it handed attackers a map of the attack surface

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
| 1 | Original post (X) | <https://x.com/aaronp613/status/2049986504617820551> |
| 2 | Medium analysis | <https://medium.com/vibe-coding/what-apples-leaked-claude-md-teaches-us-b8269e2ace51> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-30` (raw: 2026-04-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-04-30-apple-support-app-claude-md` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-19` [Vercel OAuth supply-chain intrusion](2026-04-19-vercel-oauth-gong-ying-lian.md)<br>  <sub>Vercel OAuth supply-chain intrusion</sub>
- `2026-04-21` [Unauthorised access to Anthropic's "Mythos"](2026-04-21-anthropic-mythos-zao-shou-quan.md)<br>  <sub>Unauthorised access to Anthropic's "Mythos"</sub>
- `2026-04-17` [Meta AI support bot tricked into handing over an Instagram account](2026-04-17-meta-instagram-ke-fu-ji.md)<br>  <sub>Meta AI support bot tricked into handing over an Instagram account</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-30-apple-support-app-claude-md.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
