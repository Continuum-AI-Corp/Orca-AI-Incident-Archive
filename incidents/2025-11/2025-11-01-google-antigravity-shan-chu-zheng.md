---
id: 2025-11-01-google-antigravity-shan-chu-zheng
title: "Google Antigravity deletes an entire D: partition"
title_zh: "Google Antigravity 删除整个 D 盘分区"
title_ja: "Google AntigravityがD:パーティション全体を削除"
title_ko: "Google Antigravity, D: 파티션 전체 삭제"
title_de: "Google Antigravity löscht eine gesamte D:-Partition"
title_fr: "Google Antigravity supprime une partition D: entière"
title_es: "Google Antigravity borra toda una partición D:"
date: 2025-11-01
date_precision: month
date_raw: "2025-11"

kind: incident
type: [ROGUE]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  An unquoted path containing a space led it to execute `rmdir /s /q d:\`; prompted Google to add "Secure Mode"


summary_zh: |
  路径含空格未加引号，执行 `rmdir /s /q d:\`；促使 Google 加入 "Secure Mode"

summary_ja: |
  スペースを含むパスを引用符で囲まなかったため`rmdir /s /q d:\`を実行。Googleが「Secure Mode」を追加するきっかけとなった

summary_ko: |
  공백이 포함된 경로를 따옴표로 감싸지 않아 `rmdir /s /q d:\`를 실행했다. 이로 인해 구글이 "보안 모드"를 추가하게 되었다

summary_de: |
  Ein nicht in Anführungszeichen gesetzter Pfad mit Leerzeichen führte dazu, dass es `rmdir /s /q d:\` ausführte; Google fügte daraufhin einen „Secure Mode“ hinzu

summary_fr: |
  Un chemin non mis entre guillemets contenant un espace l'a amené à exécuter `rmdir /s /q d:\` ; ce qui a poussé Google à ajouter un « Secure Mode »

summary_es: |
  Una ruta sin comillas que contenía un espacio lo llevó a ejecutar `rmdir /s /q d:\`; impulsó a Google a añadir el "Secure Mode"

sources:
  - url: https://adversa.ai/blog/ai-coding-agent-incidents/
    label: Adversa roundup

disputed: false
landmark: false
scan_month: 2025-11
scan_ref: "SCAN.md §5 2025-11"
---

# Google Antigravity deletes an entire D: partition

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

An unquoted path containing a space led it to execute `rmdir /s /q d:\`; prompted Google to add "Secure Mode"

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
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-11-01-google-antigravity-shan-chu-zheng` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-11-01` [Gemini CLI destructive file move](2025-11-01-gemini-cli-po-huai-xing.md)<br>  <sub>Gemini CLI destructive file move</sub>
- `2025-10-01` [Claude Code recursively deletes from the filesystem root](../2025-10/2025-10-01-claude-code-gen-mu-lu.md)<br>  <sub>Claude Code recursively deletes from the filesystem root</sub>
- `2025-12-15` [Amazon Kiro triggers a 13-hour AWS outage](../2025-12/2025-12-15-amazon-kiro-aws.md)<br>  <sub>Amazon Kiro triggers a 13-hour AWS outage</sub>
- `2025-12-01` [Claude Code deletes a Mac home directory, Keychain included](../2025-12/2025-12-01-claude-code-mac-keychain.md)<br>  <sub>Claude Code deletes a Mac home directory, Keychain included</sub>

---

[← 2025-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
