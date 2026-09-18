---
id: 2026-03-31-anthropic-claude-code
title: "Anthropic Claude Code source code leak"
title_zh: "Anthropic Claude Code 源码泄露"
title_ja: "Anthropic Claude Codeのソースコード漏えい"
title_ko: "Anthropic Claude Code 소스 코드 유출"
title_de: "Anthropic: Quellcode-Leak von Claude Code"
title_fr: "Fuite du code source de Claude Code d'Anthropic"
title_es: "Filtración del código fuente de Anthropic Claude Code"
date: 2026-03-31
date_precision: day
date_raw: "2026-03-31"

kind: incident
type: [CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  An npm package accidentally included a source map (.map), leaking about **510,000 lines of TypeScript / 1,906 files / 59.8 MB** and exposing unreleased features such as the KAIROS autonomous agent mode. AI-built clones appeared within a day, along with a "leaked source" version laced with the **Vidar infostealer** and the **GhostSocks proxy**


summary_zh: |
  npm 包中误含 source map（.map），约 **51 万行 TypeScript / 1,906 个文件 / 59.8 MB** 外泄，暴露 KAIROS 自主 agent 模式等未发布功能。随后出现 AI 一天内做出的克隆版，以及混入 **Vidar 窃密器**和 **GhostSocks 代理**的「泄露版源码」

summary_ja: |
  npmパッケージにソースマップ（.map）が誤って含まれ、約**51万行のTypeScript／1,906ファイル／59.8 MB**が漏えいし、KAIROS自律エージェントモードなどの未リリース機能が露呈した。1日以内にAI製のクローンが出現し、**Vidarインフォスティーラー**と**GhostSocksプロキシ**を仕込んだ「リーク版」も現れた

summary_ko: |
  npm 패키지에 소스 맵(.map)이 실수로 포함되어 약 **TypeScript 51만 줄 / 1,906개 파일 / 59.8MB**가 유출되었고, KAIROS 자율 에이전트 모드 같은 미출시 기능이 드러났다. 하루 안에 AI로 만든 복제본이 나타났으며, **Vidar 정보 탈취기**와 **GhostSocks 프록시**를 심은 "유출 소스" 버전도 등장했다

summary_de: |
  Ein npm-Paket enthielt versehentlich eine Source Map (.map), wodurch etwa **510,000 Zeilen TypeScript / 1,906 Dateien / 59.8 MB** preisgegeben wurden und unveröffentlichte Funktionen wie der autonome Agentenmodus KAIROS offenlagen. Innerhalb eines Tages erschienen KI-gebaute Klone sowie eine „Leaked Source“-Version, die mit dem **Vidar-Infostealer** und dem **GhostSocks-Proxy** versehen war

summary_fr: |
  Un paquet npm incluait accidentellement une source map (.map), divulguant environ **510 000 lignes de TypeScript / 1 906 fichiers / 59,8 Mo** et exposant des fonctionnalités non publiées comme le mode agent autonome KAIROS. Des clones construits par IA sont apparus en un jour, ainsi qu'une version « source fuitée » infectée par l'**infostealer Vidar** et le **proxy GhostSocks**

summary_es: |
  Un paquete de npm incluyó por accidente un source map (.map), filtrando unos **510,000 líneas de TypeScript / 1,906 archivos / 59.8 MB** y exponiendo funciones no lanzadas como el modo de agente autónomo KAIROS. Aparecieron clones creados con IA en un día, junto con una versión del "código fuente filtrado" cargada con el **infostealer Vidar** y el **proxy GhostSocks**

sources:
  - url: https://www.theregister.com/software/2026/03/31/anthropic-accidentally-exposes-claude-code-source-code/5227940
    label: The Register
  - url: https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html
    label: CNBC
  - url: https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak
    label: Zscaler

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Anthropic Claude Code source code leak

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

An npm package accidentally included a source map (.map), leaking about **510,000 lines of TypeScript / 1,906 files / 59.8 MB** and exposing unreleased features such as the KAIROS autonomous agent mode. AI-built clones appeared within a day, along with a "leaked source" version laced with the **Vidar infostealer** and the **GhostSocks proxy**

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
| 1 | The Register | <https://www.theregister.com/software/2026/03/31/anthropic-accidentally-exposes-claude-code-source-code/5227940> |
| 2 | CNBC | <https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html> |
| 3 | Zscaler | <https://www.zscaler.com/blogs/security-research/anthropic-claude-code-leak> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-31` (raw: 2026-03-31, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-31-anthropic-claude-code` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-26` [Anthropic CMS misconfiguration reveals the existence of "Mythos"](2026-03-26-anthropic-cms-mythos.md)<br>  <sub>Anthropic CMS misconfiguration reveals the existence of "Mythos"</sub>
- `2026-03-01` [METR API key stolen, $600K of credit burned](2026-03-01-metr-api-key.md)<br>  <sub>METR API key stolen, $600K of credit burned</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-31-anthropic-claude-code.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
