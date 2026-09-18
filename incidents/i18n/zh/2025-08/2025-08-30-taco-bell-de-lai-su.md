---
id: 2025-08-30-taco-bell-de-lai-su
lang: zh
source: incidents/2025-08/2025-08-30-taco-bell-de-lai-su.md
title: "Taco Bell 得来速 AI 点单失控"
summary: |
  2023 年起在 500+ 家店铺部署语音 AI。顾客用「18,000 杯水」等荒谬订单**故意把 AI 逼到转人工**；AI 反而拉长排队、员工几乎每单都要盯着随时接管。CDTO Dane Mathews 对 WSJ 表示「未必所有得来速都该只用 AI」，公司改为繁忙门店转人工
---

# Taco Bell 得来速 AI 点单失控

<sub>Taco Bell drive-thru AI ordering breaks down</sub>

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## 概要

2023 年起在 500+ 家店铺部署语音 AI。顾客用「18,000 杯水」等荒谬订单**故意把 AI 逼到转人工**；AI 反而拉长排队、员工几乎每单都要盯着随时接管。CDTO Dane Mathews 对 WSJ 表示「未必所有得来速都该只用 AI」，公司改为繁忙门店转人工

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
| 1 | TechCrunch | <https://techcrunch.com/2025/08/30/taco-bell-is-having-second-thoughts-about-relying-on-ai-at-the-drive-through/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-30`（原文：2025-08-30，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **低** `low` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案编号 | `2025-08-30-taco-bell-de-lai-su` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `low`：背景性条目，保留用于时间线连续性。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2025-07-13` [Amazon Q Developer 扩展被投毒](../../../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-07-18` [Replit Agent 删除生产数据库](../../../2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br>  <sub>Replit Agent deletes a production database</sub>
- `2025-10-01` [Claude Code 从根目录递归删除](../../../2025-10/2025-10-01-claude-code-gen-mu-lu.md)<br>  <sub>Claude Code recursively deletes from the filesystem root</sub>
- `2025-06-01` [Cursor YOLO 模式清空开发机](../../../2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md)<br>  <sub>Cursor YOLO mode wipes a dev machine</sub>

---

[← English original](../../../2025-08/2025-08-30-taco-bell-de-lai-su.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
