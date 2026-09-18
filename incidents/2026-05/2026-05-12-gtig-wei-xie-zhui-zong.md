---
id: 2026-05-12-gtig-wei-xie-zhui-zong
title: "GTIG AI threat tracker, 2026 edition"
title_zh: "GTIG AI 威胁追踪（2026 版）"
title_ja: "GTIG AI脅威トラッカー2026年版"
title_ko: "GTIG AI 위협 추적 보고서 2026년판"
title_de: "GTIG-KI-Bedrohungstracker, Ausgabe 2026"
title_fr: "Le tracker de menaces IA de GTIG, édition 2026"
title_es: "Rastreador de amenazas de IA de GTIG, edición 2026"
date: 2026-05-12
date_precision: day
date_raw: "2026-05-12"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  See [§7.5](#75-offensive-ai-capability-evolutionweapon) for the full breakdown. New: **PROMPTSPY** (a backdoor that calls the Gemini API to operate an Android UI autonomously), AI-usage profiles for China-nexus actors such as UNC2814 / APT45 / APT27 / UNC6201 / UNC5673, and the LLM-access obfuscation industry (CLIProxyAPI, Claude-Relay-Service and others)


summary_zh: |
  见 [§7.5](#75-攻击方使用-ai-的能力演进weapon) 完整拆解。新增 **PROMPTSPY**（调 Gemini API 自主操作安卓 UI 的后门）、UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 等中国系行为者的 AI 使用画像、LLM 访问混淆产业（CLIProxyAPI、Claude-Relay-Service 等）

summary_ja: |
  完全な内訳は[§7.5](#75-offensive-ai-capability-evolutionweapon)を参照。新規：**PROMPTSPY**（Gemini APIを呼び出してAndroid UIを自律操作するバックドア）、UNC2814／APT45／APT27／UNC6201／UNC5673など中国関連アクターのAI利用プロファイル、LLMアクセスの難読化産業（CLIProxyAPI、Claude-Relay-Serviceなど）

summary_ko: |
  전체 분석은 [§7.5](#75-offensive-ai-capability-evolutionweapon) 참조. 새로운 내용: **PROMPTSPY**(Gemini API를 호출해 Android UI를 자율 조작하는 백도어), UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 등 중국 연계 행위자의 AI 활용 프로파일, LLM 접근 난독화 산업(CLIProxyAPI, Claude-Relay-Service 등)

summary_de: |
  Die vollständige Aufschlüsselung findet sich in [§7.5](#75-offensive-ai-capability-evolutionweapon). Neu: **PROMPTSPY** (eine Backdoor, die die Gemini-API aufruft, um eine Android-UI autonom zu bedienen), Nutzungsprofile von KI für Akteure mit China-Bezug wie UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 sowie die Industrie zur Verschleierung des LLM-Zugriffs (CLIProxyAPI, Claude-Relay-Service und andere)

summary_fr: |
  Voir [§7.5](#75-offensive-ai-capability-evolutionweapon) pour l'analyse complète. Nouveautés : **PROMPTSPY** (une backdoor qui appelle l'API Gemini pour piloter de façon autonome une UI Android), des profils d'usage de l'IA pour des acteurs liés à la Chine comme UNC2814 / APT45 / APT27 / UNC6201 / UNC5673, et l'industrie de l'obfuscation d'accès aux LLM (CLIProxyAPI, Claude-Relay-Service et autres)

summary_es: |
  Ver [§7.5](#75-offensive-ai-capability-evolutionweapon) para el desglose completo. Novedades: **PROMPTSPY** (una puerta trasera que llama a la API de Gemini para operar de forma autónoma una interfaz de Android), perfiles de uso de IA de actores vinculados a China como UNC2814 / APT45 / APT27 / UNC6201 / UNC5673, y la industria de ofuscación de acceso a LLM (CLIProxyAPI, Claude-Relay-Service y otros)

sources:
  - url: https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access
    label: GTIG

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# GTIG AI threat tracker, 2026 edition

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

See [§7.5](#75-offensive-ai-capability-evolutionweapon) for the full breakdown. New: **PROMPTSPY** (a backdoor that calls the Gemini API to operate an Android UI autonomously), AI-usage profiles for China-nexus actors such as UNC2814 / APT45 / APT27 / UNC6201 / UNC5673, and the LLM-access obfuscation industry (CLIProxyAPI, Claude-Relay-Service and others)

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
| 1 | GTIG | <https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-12` (raw: 2026-05-12, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-12-gtig-wei-xie-zhui-zong` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-05-10` [First in-the-wild LLM agent running the full post-exploitation chain](2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br>  <sub>First in-the-wild LLM agent running the full post-exploitation chain</sub>
- `2026-04-08` [Aurora ransomware operators use Cursor Agent in live intrusions](../2026-04/2026-04-08-aurora-cursor-agent.md)<br>  <sub>Aurora ransomware operators use Cursor Agent in live intrusions</sub>
- `2026-06-15` [UNC6508 breaches North American research institutions via REDCap](../2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)<br>  <sub>UNC6508 breaches North American research institutions via REDCap</sub>
- `2026-06-02` [CleverHans Lab adaptive AI worm PoC](../2026-06/2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
