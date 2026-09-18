---
id: 2025-06-01-cursor-yolo-mo-shi-qing
title: "Cursor YOLO mode wipes a dev machine"
title_zh: "Cursor YOLO 模式清空开发机"
title_ja: "CursorのYOLOモードが開発マシンを消去"
title_ko: "Cursor YOLO 모드, 개발자 머신을 초기화"
title_de: "Cursor YOLO-Modus löscht einen Entwicklerrechner"
title_fr: "Le mode YOLO de Cursor efface une machine de développement"
title_es: "El modo YOLO de Cursor borra una máquina de desarrollo"
date: 2025-06-01
date_precision: month
date_raw: "2025-06"

kind: incident
type: [ROGUE]
severity: medium
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  An Express→Next.js migration deleted an entire machine; only partial recovery from a cloud backup


summary_zh: |
  Express→Next.js 迁移中删掉整台机器，仅云备份部分恢复

summary_ja: |
  Express→Next.jsの移行作業でマシン全体が削除され、クラウドバックアップから一部のみ復旧

summary_ko: |
  Express→Next.js 마이그레이션 중 머신 전체가 삭제되었다. 클라우드 백업에서 일부만 복구했다

summary_de: |
  Eine Express→Next.js-Migration löschte einen ganzen Rechner; nur teilweise Wiederherstellung aus einem Cloud-Backup

summary_fr: |
  Une migration Express→Next.js a supprimé une machine entière ; récupération partielle uniquement depuis une sauvegarde cloud

summary_es: |
  Una migración de Express→Next.js borró una máquina entera; solo se recuperó parcialmente desde una copia de seguridad en la nube

sources:
  - url: https://adversa.ai/blog/ai-coding-agent-incidents/
    label: Adversa roundup

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# Cursor YOLO mode wipes a dev machine

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

An Express→Next.js migration deleted an entire machine; only partial recovery from a cloud backup

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
| Date | `2025-06-01` (raw: 2025-06, precision `month`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **Medium** `medium` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-01-cursor-yolo-mo-shi-qing` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-07-18` [Replit Agent deletes a production database](../2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br>  <sub>Replit Agent deletes a production database</sub>
- `2025-05-14` [xAI Grok "white genocide" incident](../2025-05/2025-05-14-xai-grok-white-genocide.md)<br>  <sub>xAI Grok "white genocide" incident</sub>
- `2025-08-30` [Taco Bell drive-thru AI ordering breaks down](../2025-08/2025-08-30-taco-bell-de-lai-su.md)<br>  <sub>Taco Bell drive-thru AI ordering breaks down</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
