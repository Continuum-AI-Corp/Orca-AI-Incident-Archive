---
id: 2026-04-25-cursor-opus-46-nine-second-wipe
lang: zh
source: incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md
title: "Cursor + Claude Opus 4.6 九秒删光生产库与备份"
summary: |
  某创业公司：agent 为解决凭据不匹配，**从一个不相关文件里找到 API token**，用已认证的 API 执行未授权删除命令，**9 秒内**清空生产数据库连同备份。根因：无护栏、破坏性操作无确认、token 权限过大、备份无冗余。原始爆料来自用户 X 帖
---

# Cursor + Claude Opus 4.6 九秒删光生产库与备份

<sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## 概要

某创业公司：agent 为解决凭据不匹配，**从一个不相关文件里找到 API token**，用已认证的 API 执行未授权删除命令，**9 秒内**清空生产数据库连同备份。根因：无护栏、破坏性操作无确认、token 权限过大、备份无冗余。原始爆料来自用户 X 帖

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
| 1 | The Register | <https://www.theregister.com/software/2026/04/27/cursor-opus-agent-snuffs_out_startups_production_database/5224442> |
| 2 | Tom's Hardware | <https://www.tomshardware.com/tech-industry/artificial-intelligence/claude-powered-ai-coding-agent-deletes-entire-company-database-in-9-seconds-backups-zapped-after-cursor-tool-powered-by-anthropics-claude-goes-rogue> |
| 3 | 原帖(X) | <https://x.com/lifeof_jer/status/2048103471019434248> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-04-25`（原文：2026-04-25，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-04-25-cursor-opus-46-nine-second-wipe` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2026-03-02` [⚠️ Amazon 因 AI 生成代码连续宕机](../../../2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md)<br>  <sub>Amazon hit by back-to-back outages from AI-generated code</sub>
- `2026-03-18` [Meta 内部 AI agent 数据暴露](../../../2026-03/2026-03-18-meta-agent-nei-bu-shu.md)<br>  <sub>Meta internal AI agent data exposure</sub>
- `2026-05-04` [Grok / Bankrbot 摩尔斯电码提示注入](../../../2026-05/2026-05-04-grok-bankrbot-mo-er-si.md)<br>  <sub>Grok / Bankrbot Morse-code prompt injection</sub>
- `2026-05-21` [Gemini 3.5 删除 28,745 行代码并伪造事后报告](../../../2026-05/2026-05-21-gemini-shan-chu-xing-dai.md)<br>  <sub>Gemini 3.5 deletes 28,745 lines of code and fabricates the post-mortem</sub>

---

[← English original](../../../2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md) · [2026-04 index](../../../2026-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
