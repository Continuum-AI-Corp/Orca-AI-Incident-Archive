---
id: 2026-09-11-claude-scans-18m-android-apks
title: "Claude used to scan 1.8 million Android apps for secrets"
title_zh: "用 Claude 扫描 180 万个安卓 App 找密钥"
title_ja: "Claudeが180万件のAndroidアプリをスキャンしてシークレットを探索"
title_ko: "Claude, 180만 개 Android 앱에서 비밀 정보 스캔에 사용"
title_de: "Claude durchsucht 1.8 Millionen Android-Apps nach Secrets"
title_fr: "Claude utilisé pour scanner 1,8 million d'applications Android à la recherche de secrets"
title_es: "Se usó Claude para escanear 1.8 millones de apps de Android en busca de secretos"
date: 2026-09-11
date_precision: day
date_raw: "2026-09-11"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  One concrete case in Anthropic's September report: a suspected French-speaking **ShinyHunters** member (handle **`frkoo`**) deployed a credential-harvesting pipeline **across 10 AWS EC2 workers**, downloading from multiple app stores and **scanning 1.8 million Android APKs for secrets**. The account has been removed and guardrails adjusted


summary_zh: |
  Anthropic 九月报告中的一个具体案例：一名疑似法语系的 **ShinyHunters** 成员（handle **`frkoo`**）部署了一条凭据收割流水线，**横跨 10 台 AWS EC2 worker**，从多个应用商店下载并**扫描 180 万个安卓 APK 中的密钥**。账号已被移除、护栏已调整

summary_ja: |
  Anthropicの9月レポートの具体的な事例：フランス語話者とみられる**ShinyHunters**のメンバー（ハンドル**`frkoo`**）が**10台のAWS EC2ワーカーにわたる**認証情報収集パイプラインを展開し、複数のアプリストアからダウンロードして**180万件のAndroid APKをスキャンしてシークレットを探索**した。アカウントは削除され、ガードレールが調整された

summary_ko: |
  Anthropic 9월 보고서의 구체적 사례 하나: 프랑스어권 **ShinyHunters** 구성원으로 의심되는 인물(핸들 **`frkoo`**)이 **AWS EC2 워커 10대에 걸쳐** 자격 증명 수집 파이프라인을 배치하고 여러 앱 스토어에서 내려받아 **180만 개의 Android APK에서 비밀 정보를 스캔**했다. 해당 계정은 삭제되고 가드레일이 조정되었다

summary_de: |
  Ein konkreter Fall im September-Bericht von Anthropic: Ein mutmaßliches französischsprachiges **ShinyHunters**-Mitglied (Handle **`frkoo`**) setzte eine Pipeline zum Ernten von Zugangsdaten **auf 10 AWS-EC2-Workern** ein, lud aus mehreren App-Stores herunter und **durchsuchte 1.8 Millionen Android-APKs nach Secrets**. Das Konto wurde entfernt und die Guardrails angepasst

summary_fr: |
  Un cas concret du rapport de septembre d'Anthropic : un membre présumé de **ShinyHunters** francophone (pseudonyme **`frkoo`**) a déployé un pipeline de récolte d'identifiants **sur 10 workers AWS EC2**, téléchargeant depuis plusieurs magasins d'applications et **scannant 1,8 million d'APK Android à la recherche de secrets**. Le compte a été supprimé et les garde-fous ajustés

summary_es: |
  Un caso concreto del informe de septiembre de Anthropic: un presunto miembro de **ShinyHunters** de habla francesa (alias **`frkoo`**) desplegó una canalización de recolección de credenciales **en 10 workers de AWS EC2**, descargando de varias tiendas de aplicaciones y **escaneando 1.8 millones de APK de Android en busca de secretos**. La cuenta ha sido eliminada y los guardrails ajustados

sources:
  - url: https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/
    label: BleepingComputer
  - url: https://www.anthropic.com/threat-intelligence-report-september-2026
    label: Anthropic report

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Claude used to scan 1.8 million Android apps for secrets

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

One concrete case in Anthropic's September report: a suspected French-speaking **ShinyHunters** member (handle **`frkoo`**) deployed a credential-harvesting pipeline **across 10 AWS EC2 workers**, downloading from multiple app stores and **scanning 1.8 million Android APKs for secrets**. The account has been removed and guardrails adjusted

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/hackers-abused-claude-to-extract-secrets-from-18m-android-apps/> |
| 2 | Anthropic report | <https://www.anthropic.com/threat-intelligence-report-september-2026> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-11` (raw: 2026-09-11, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-11-claude-scans-18m-android-apks` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-10` [Anthropic September threat intelligence report](2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-09-15` [PaperCut AI agent swarm attack made public](2026-09-15-papercut-agent-swarm-disclosed.md)<br>  <sub>PaperCut AI agent swarm attack made public</sub>
- `2026-09-02` [Unit 42: AI agents compress two weeks of intrusion work into 10 hours](2026-09-02-unit-agent-liang-ru-qin.md)<br>  <sub>Unit 42: AI agents compress two weeks of intrusion work into 10 hours</sub>
- `2026-08-28` [PaperCut AI agent swarm campaign begins](../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-11-claude-scans-18m-android-apks.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
