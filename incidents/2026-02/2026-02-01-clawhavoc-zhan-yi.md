---
id: 2026-02-01-clawhavoc-zhan-yi
title: "ClawHavoc campaign"
title_zh: "ClawHavoc 战役"
title_ja: "ClawHavocキャンペーン"
title_ko: "ClawHavoc 작전"
title_de: "ClawHavoc-Kampagne"
title_fr: "Campagne ClawHavoc"
title_es: "Campaña ClawHavoc"
date: 2026-02-01
date_precision: day
date_raw: "2026-02-01"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Koi Security audited **2,857 skills on ClawHub and found 341 malicious ones (about 12%)**, a figure later raised to **824**. The main payload is the macOS infostealer **AMOS (Atomic Stealer)**. Techniques: typosquatting, fake "prerequisite" requirements, reverse shells, reading `.env`; payloads hide inside password-protected archives and obfuscated shell scripts to evade static analysis. OpenClaw then partnered with VirusTotal to add automatic scanning (including LLM-based Code Insight) for every skill
  ⚠️ **Sources conflict on the malicious count: 341 / 824 / 1,184 / 1,200+, depending on when the audit was run and what it counted**


summary_zh: |
  Koi Security 审计 ClawHub 上 **2,857 个 skill，发现 341 个恶意（约 12%）**，后续统计升至 **824 个**。主载荷为 macOS 信息窃取器 **AMOS (Atomic Stealer)**。手法：typosquatting、伪造「前置条件」要求、反弹 shell、读 `.env`；载荷藏在密码保护压缩包与混淆 shell 脚本里以躲静态分析。OpenClaw 随后与 VirusTotal 合作，对所有 skill 接入自动扫描（含基于 LLM 的 Code Insight）
  ⚠️ **恶意数量来源冲突：341 / 824 / 1,184 / 1,200+，取决于审计时点与口径**

summary_ja: |
  Koi Securityが**ClawHubの2,857スキルを監査し、341件（約12%）が悪性**と判定、その後この数字は**824件**に引き上げられた。主なペイロードはmacOSのインフォスティーラー**AMOS（Atomic Stealer）**。手法：typosquatting、偽の「前提条件」要求、リバースシェル、`.env`の読み取り。ペイロードはパスワード保護されたアーカイブや難読化されたシェルスクリプトの中に隠れ、静的解析を回避する。OpenClawはその後VirusTotalと提携し、すべてのスキルに自動スキャン（LLMベースのCode Insightを含む）を追加した
  ⚠️ **悪性数の情報源は矛盾している：341／824／1,184／1,200以上——監査時期と集計方法により異なる**

summary_ko: |
  Koi Security는 **ClawHub의 스킬 2,857개를 감사해 341개(약 12%)가 악성**임을 발견했고, 이 수치는 이후 **824개**로 상향되었다. 주 페이로드는 macOS 정보 탈취 악성코드 **AMOS (Atomic Stealer)**다. 기법: 타이포스쿼팅, 가짜 "사전 요구사항", 리버스 셸, `.env` 읽기이며, 페이로드는 정적 분석을 피하려 암호로 보호된 압축 파일과 난독화된 셸 스크립트 안에 숨는다. 이후 OpenClaw는 VirusTotal과 협력해 모든 스킬에 자동 스캔(LLM 기반 Code Insight 포함)을 추가했다
  ⚠️ **악성 개수는 출처마다 엇갈린다: 341 / 824 / 1,184 / 1,200+, 감사 시점과 집계 기준에 따라 달라진다**

summary_de: |
  Koi Security prüfte **2,857 Skills auf ClawHub und fand 341 bösartige (etwa 12%)**, eine Zahl, die später auf **824** erhöht wurde. Die Hauptnutzlast ist der macOS-Infostealer **AMOS (Atomic Stealer)**. Techniken: Typosquatting, gefälschte „Voraussetzungen“, Reverse Shells, Auslesen von `.env`; die Nutzlasten verstecken sich in passwortgeschützten Archiven und obfuskierten Shell-Skripten, um statische Analyse zu umgehen. OpenClaw ging anschließend eine Partnerschaft mit VirusTotal ein, um für jeden Skill automatisches Scannen (einschließlich LLM-basiertem Code Insight) hinzuzufügen
  ⚠️ **Die Quellen widersprechen sich bei der Anzahl der bösartigen Einträge: 341 / 824 / 1,184 / 1,200+, je nachdem, wann die Prüfung lief und was gezählt wurde**

summary_fr: |
  Koi Security a audité **2 857 skills sur ClawHub et en a trouvé 341 malveillants (environ 12 %)**, un chiffre ensuite porté à **824**. La charge principale est l'infostealer macOS **AMOS (Atomic Stealer)**. Techniques : typosquatting, fausses exigences de « prérequis », reverse shells, lecture des `.env` ; les charges se cachent dans des archives protégées par mot de passe et des scripts shell obfusqués pour échapper à l'analyse statique. OpenClaw s'est ensuite associé à VirusTotal pour ajouter un scan automatique (y compris Code Insight basé sur un LLM) de chaque skill
  ⚠️ **Les sources divergent sur le nombre de malveillants : 341 / 824 / 1 184 / plus de 1 200, selon la date de l'audit et ce qui a été compté**

summary_es: |
  Koi Security auditó **2,857 skills en ClawHub y encontró 341 maliciosas (alrededor del 12%)**, una cifra que después se elevó a **824**. La carga útil principal es el infostealer de macOS **AMOS (Atomic Stealer)**. Técnicas: typosquatting, falsos requisitos de "prerequisite", reverse shells, lectura de `.env`; las cargas se esconden dentro de archivos protegidos con contraseña y scripts de shell ofuscados para evadir el análisis estático. OpenClaw luego se asoció con VirusTotal para añadir escaneo automático (incluido Code Insight basado en LLM) a cada skill
  ⚠️ **Las fuentes discrepan sobre el recuento de maliciosas: 341 / 824 / 1,184 / 1,200+, según cuándo se ejecutó la auditoría y qué contó**

sources:
  - url: https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting
    label: Koi Security
  - url: https://openclaw.ai/blog/virustotal-partnership
    label: OpenClaw advisory

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# ClawHavoc campaign

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Koi Security audited **2,857 skills on ClawHub and found 341 malicious ones (about 12%)**, a figure later raised to **824**. The main payload is the macOS infostealer **AMOS (Atomic Stealer)**. Techniques: typosquatting, fake "prerequisite" requirements, reverse shells, reading `.env`; payloads hide inside password-protected archives and obfuscated shell scripts to evade static analysis. OpenClaw then partnered with VirusTotal to add automatic scanning (including LLM-based Code Insight) for every skill

⚠️ **Sources conflict on the malicious count: 341 / 824 / 1,184 / 1,200+, depending on when the audit was run and what it counted**

## Attack chain

```mermaid
flowchart LR
    E["Poisoned packages / repositories / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Koi Security | <https://www.koi.ai/blog/clawhavoc-341-malicious-clawedbot-skills-found-by-the-bot-they-were-targeting> |
| 2 | OpenClaw advisory | <https://openclaw.ai/blog/virustotal-partnership> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-01` (raw: 2026-02-01, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-01-clawhavoc-zhan-yi` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-02-09` [Clinejection](2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-30` [Axios npm package compromised](../2026-03/2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-01-clawhavoc-zhan-yi.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
