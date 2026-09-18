---
id: 2026-02-01-openclaw-xin-xi-qie-qu
title: "Infostealers start harvesting OpenClaw configs and gateway tokens"
title_zh: "信息窃取器开始专门收割 OpenClaw 配置与网关令牌"
title_ja: "インフォスティーラーがOpenClawの設定とゲートウェイトークンの収集を開始"
title_ko: "정보 탈취 악성코드, OpenClaw 설정과 게이트웨이 토큰 수집 시작"
title_de: "Infostealer ernten nun OpenClaw-Konfigurationen und Gateway-Token"
title_fr: "Les infostealers commencent à récolter les configurations et jetons de passerelle OpenClaw"
title_es: "Los infostealers empiezan a recolectar configuraciones y tokens de gateway de OpenClaw"
date: 2026-02-01
date_precision: month
date_raw: "2026-02"

kind: incident
type: [CRED]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Commercial infostealers now list **OpenClaw agent config files and gateway tokens** as their own collection targets — agent credentials have formally entered the standard infostealer checklist


summary_zh: |
  商品化 infostealer 把 **OpenClaw 的 agent 配置文件与 gateway token** 列为独立收集目标 —— agent 凭据正式进入信息窃取器的标准清单

summary_ja: |
  商用インフォスティーラーが**OpenClawエージェントの設定ファイルとゲートウェイトークン**を収集対象として明記——エージェントの認証情報が正式に標準的なインフォスティーラーのチェックリスト入りを果たした

summary_ko: |
  상용 정보 탈취 악성코드들이 **OpenClaw 에이전트 설정 파일과 게이트웨이 토큰**을 자체 수집 대상으로 등재했다 — 에이전트 자격 증명이 공식적으로 표준 정보 탈취 목록에 들어왔다

summary_de: |
  Kommerzielle Infostealer führen **OpenClaw-Agent-Konfigurationsdateien und Gateway-Token** nun als eigene Sammelziele — Agent-Zugangsdaten sind damit offiziell in die Standard-Checkliste der Infostealer aufgenommen

summary_fr: |
  Les infostealers commerciaux listent désormais **les fichiers de configuration d'agent OpenClaw et les jetons de passerelle** parmi leurs propres cibles de collecte — les identifiants d'agents sont officiellement entrés dans la checklist standard des infostealers

summary_es: |
  Los infostealers comerciales ya incluyen los **archivos de configuración del agente OpenClaw y los tokens de gateway** entre sus propios objetivos de recolección — las credenciales de agentes han entrado formalmente en la lista estándar de los infostealers

sources:
  - url: https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html
    label: THN

disputed: false
landmark: false
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Infostealers start harvesting OpenClaw configs and gateway tokens

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Commercial infostealers now list **OpenClaw agent config files and gateway tokens** as their own collection targets — agent credentials have formally entered the standard infostealer checklist

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["agent retrieves and uses them"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/02/infostealer-steals-openclaw-ai-agent.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-01` (raw: 2026-02, precision `month`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-01-openclaw-xin-xi-qie-qu` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-02-27` [Check Point publishes two Claude Code CVEs](2026-02-27-check-point-claude-code.md)<br>  <sub>Check Point publishes two Claude Code CVEs</sub>
- `2026-01-31` [Moltbook database fully open](../2026-01/2026-01-31-moltbook-open-database.md)<br>  <sub>Moltbook database fully open</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-01-openclaw-xin-xi-qie-qu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
