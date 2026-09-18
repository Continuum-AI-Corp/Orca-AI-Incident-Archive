---
id: 2025-10-01-claude-code-gen-mu-lu
title: "Claude Code recursively deletes from the filesystem root"
title_zh: "Claude Code 从根目录递归删除"
title_ja: "Claude Codeがファイルシステムのルートから再帰的に削除"
title_ko: "Claude Code, 파일 시스템 루트에서 재귀 삭제"
title_de: "Claude Code löscht rekursiv ab der Dateisystemwurzel"
title_fr: "Claude Code supprime récursivement depuis la racine du système de fichiers"
title_es: "Claude Code borra recursivamente desde la raíz del sistema de archivos"
date: 2025-10-01
date_precision: month
date_raw: "2025-10"

kind: incident
type: [ROGUE]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Wiped all user files on Ubuntu/WSL2; the permission system did not recognize the dangerous expansion


summary_zh: |
  Ubuntu/WSL2 上删光所有用户文件，权限系统未识别危险展开

summary_ja: |
  Ubuntu/WSL2上でユーザーファイルをすべて消去。権限システムが危険な展開を認識できなかった

summary_ko: |
  Ubuntu/WSL2에서 사용자 파일 전체를 삭제했다. 권한 시스템이 위험한 확장을 인식하지 못했다

summary_de: |
  Löschte alle Nutzerdateien unter Ubuntu/WSL2; das Berechtigungssystem erkannte die gefährliche Expansion nicht

summary_fr: |
  Efface tous les fichiers utilisateur sous Ubuntu/WSL2 ; le système de permissions n'a pas reconnu l'expansion dangereuse

summary_es: |
  Borró todos los archivos de usuario en Ubuntu/WSL2; el sistema de permisos no reconoció la expansión peligrosa

sources:
  - url: https://adversa.ai/blog/ai-coding-agent-incidents/
    label: Adversa roundup

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# Claude Code recursively deletes from the filesystem root

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

Wiped all user files on Ubuntu/WSL2; the permission system did not recognize the dangerous expansion

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
| Date | `2025-10-01` (raw: 2025-10, precision `month`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-01-claude-code-gen-mu-lu` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-11-01` [Google Antigravity deletes an entire D: partition](../2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md)<br>  <sub>Google Antigravity deletes an entire D: partition</sub>
- `2025-11-01` [Gemini CLI destructive file move](../2025-11/2025-11-01-gemini-cli-po-huai-xing.md)<br>  <sub>Gemini CLI destructive file move</sub>
- `2025-12-15` [Amazon Kiro triggers a 13-hour AWS outage](../2025-12/2025-12-15-amazon-kiro-aws.md)<br>  <sub>Amazon Kiro triggers a 13-hour AWS outage</sub>
- `2025-12-01` [Claude Code deletes a Mac home directory, Keychain included](../2025-12/2025-12-01-claude-code-mac-keychain.md)<br>  <sub>Claude Code deletes a Mac home directory, Keychain included</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-01-claude-code-gen-mu-lu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
