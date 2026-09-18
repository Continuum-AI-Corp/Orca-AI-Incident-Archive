---
id: 2025-11-01-gemini-cli-po-huai-xing
title: "Gemini CLI destructive file move"
title_zh: "Gemini CLI 破坏性文件移动"
title_ja: "Gemini CLIの破壊的なファイル移動"
title_ko: "Gemini CLI의 파괴적 파일 이동"
title_de: "Gemini CLI: destruktives Verschieben von Dateien"
title_fr: "Déplacement de fichiers destructif dans Gemini CLI"
title_es: "Movimiento destructivo de archivos en Gemini CLI"
date: 2025-11-01
date_precision: month
date_raw: "2025-11"

kind: incident
type: [ROGUE]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Took a failed directory creation for success; files overwrote one another until only one survived


summary_zh: |
  误把失败的目录创建当成功，逐个文件互相覆盖，仅一个文件幸存

summary_ja: |
  ディレクトリ作成の失敗を成功と誤認し、ファイルが互いに上書きを繰り返して1つだけが残った

summary_ko: |
  실패한 디렉터리 생성을 성공으로 착각했고, 파일들이 서로 덮어써 마지막 하나만 남았다

summary_de: |
  Hielt eine fehlgeschlagene Verzeichniserstellung für einen Erfolg; Dateien überschrieben einander, bis nur eine übrig blieb

summary_fr: |
  A pris un échec de création de répertoire pour un succès ; les fichiers se sont écrasés les uns les autres jusqu'à ce qu'un seul survive

summary_es: |
  Tomó una creación de directorio fallida como exitosa; los archivos se sobrescribieron entre sí hasta que solo sobrevivió uno

sources:
  - url: https://adversa.ai/blog/ai-coding-agent-incidents/
    label: Adversa roundup

disputed: false
landmark: false
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# Gemini CLI destructive file move

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

Took a failed directory creation for success; files overwrote one another until only one survived

## Attack chain

```mermaid
flowchart LR
    E["An ordinary task handed to the agent"]:::entry
    S0["The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Adversa roundup | <https://adversa.ai/blog/ai-coding-agent-incidents/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-11-01` (raw: 2025-11, precision `month`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-01-gemini-cli-po-huai-xing` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-11-01` [Google Antigravity deletes an entire D: partition](2025-11-01-google-antigravity-shan-chu-zheng.md)<br>  <sub>Google Antigravity deletes an entire D: partition</sub>
- `2025-10-01` [Claude Code recursively deletes from the filesystem root](../2025-10/2025-10-01-claude-code-gen-mu-lu.md)<br>  <sub>Claude Code recursively deletes from the filesystem root</sub>
- `2025-12-15` [Amazon Kiro triggers a 13-hour AWS outage](../2025-12/2025-12-15-amazon-kiro-aws.md)<br>  <sub>Amazon Kiro triggers a 13-hour AWS outage</sub>
- `2025-12-01` [Claude Code deletes a Mac home directory, Keychain included](../2025-12/2025-12-01-claude-code-mac-keychain.md)<br>  <sub>Claude Code deletes a Mac home directory, Keychain included</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-01-gemini-cli-po-huai-xing.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
