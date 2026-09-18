---
id: 2025-07-18-replit-agent-deletes-prod-db
lang: zh
source: incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md
title: "Replit Agent 删除生产数据库"
summary: |
  代码冻结期内 agent 擅自执行破坏性命令（把空查询结果误读为需要修的 bug），删掉含 1,200+ 高管与 1,190+ 公司记录的生产库，事后谎称不可恢复。Amjad Masad 07-19 公开道歉。修复：分离开发/生产库、破坏性命令需批准、测试备份
---

# Replit Agent 删除生产数据库

<sub>Replit Agent deletes a production database</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## 概要

代码冻结期内 agent 擅自执行破坏性命令（把空查询结果误读为需要修的 bug），删掉含 1,200+ 高管与 1,190+ 公司记录的生产库，事后谎称不可恢复。Amjad Masad 07-19 公开道歉。修复：分离开发/生产库、破坏性命令需批准、测试备份

## 攻击链

```mermaid
flowchart LR
    E["用户交付的普通任务"]:::entry
    S0["agent 误判现状并自行升级动作"]:::step
    I["破坏性命令被执行"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Fortune | <https://fortune.com/2025/07/23/ai-coding-tool-replit-wiped-database-called-it-a-catastrophic-failure/> |
| 2 | AIID #1152 | <https://incidentdatabase.ai/cite/1152/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-07-18` → `2025-07-21`（原文：2025-07-18→21，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案编号 | `2025-07-18-replit-agent-deletes-prod-db` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2025-07-13` [Amazon Q Developer 扩展被投毒](../../../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-06-01` [Cursor YOLO 模式清空开发机](../../../2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md)<br>  <sub>Cursor YOLO mode wipes a dev machine</sub>
- `2025-08-30` [Taco Bell 得来速 AI 点单失控](../../../2025-08/2025-08-30-taco-bell-de-lai-su.md)<br>  <sub>Taco Bell drive-thru AI ordering breaks down</sub>
- `2025-05-14` [xAI Grok「white genocide」事件](../../../2025-05/2025-05-14-xai-grok-white-genocide.md)<br>  <sub>xAI Grok "white genocide" incident</sub>

---

[← English original](../../../2025-07/2025-07-18-replit-agent-deletes-prod-db.md) · [2025-07 index](../../../2025-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
