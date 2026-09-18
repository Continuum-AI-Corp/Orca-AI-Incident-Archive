---
id: 2025-12-01-claude-code-mac-keychain
title: "Claude Code deletes a Mac home directory, Keychain included"
title_zh: "Claude Code 删除 Mac 主目录（含 Keychain）"
title_ja: "Claude CodeがMacのホームディレクトリをKeychainごと削除"
title_ko: "Claude Code, Mac 홈 디렉터리와 Keychain까지 삭제"
title_de: "Claude Code löscht ein Mac-Home-Verzeichnis samt Keychain"
title_fr: "Claude Code supprime un répertoire home macOS, Keychain compris"
title_es: "Claude Code borra un directorio home de Mac, incluido el Keychain"
date: 2025-12-01
date_precision: month
date_raw: "2025-12"

kind: incident
type: [ROGUE]
severity: high
confidence: B
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  `rm -rf tests/ patches/ plan/ ~/`; TRIM had already zeroed the data, so recovery was impossible


summary_zh: |
  `rm -rf tests/ patches/ plan/ ~/`，TRIM 已清零，完全不可恢复

summary_ja: |
  `rm -rf tests/ patches/ plan/ ~/`。TRIMがすでにデータをゼロ化していたため、復旧は不可能だった

summary_ko: |
  `rm -rf tests/ patches/ plan/ ~/`; TRIM이 이미 데이터를 0으로 덮어써 복구가 불가능했다

summary_de: |
  `rm -rf tests/ patches/ plan/ ~/`; TRIM hatte die Daten bereits genullt, eine Wiederherstellung war unmöglich

summary_fr: |
  `rm -rf tests/ patches/ plan/ ~/` ; TRIM avait déjà mis les données à zéro, rendant toute récupération impossible

summary_es: |
  `rm -rf tests/ patches/ plan/ ~/`; TRIM ya había puesto a cero los datos, así que la recuperación fue imposible

sources:
  - url: https://adversa.ai/blog/ai-coding-agent-incidents/
    label: Adversa roundup

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# Claude Code deletes a Mac home directory, Keychain included

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

`rm -rf tests/ patches/ plan/ ~/`; TRIM had already zeroed the data, so recovery was impossible

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
| Date | `2025-12-01` (raw: 2025-12, precision `month`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-01-claude-code-mac-keychain` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-12-15` [Amazon Kiro triggers a 13-hour AWS outage](2025-12-15-amazon-kiro-aws.md)<br>  <sub>Amazon Kiro triggers a 13-hour AWS outage</sub>
- `2025-12-01` [Cursor Plan Mode ignores "DO NOT RUN ANYTHING", deletes ~70 files](2025-12-01-cursor-plan-mode.md)<br>  <sub>Cursor Plan Mode ignores "DO NOT RUN ANYTHING", deletes ~70 files</sub>
- `2025-12-01` [LLM-driven humanoid robot jailbroken into firing a weapon](2025-12-01-llm-qu-dong-ren-xing.md)<br>  <sub>LLM-driven humanoid robot jailbroken into firing a weapon</sub>
- `2025-11-01` [Google Antigravity deletes an entire D: partition](../2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md)<br>  <sub>Google Antigravity deletes an entire D: partition</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-01-claude-code-mac-keychain.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
