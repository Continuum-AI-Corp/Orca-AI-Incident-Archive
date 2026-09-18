---
id: 2025-12-01-cursor-plan-mode
lang: zh
source: incidents/2025-12/2025-12-01-cursor-plan-mode.md
title: "Cursor Plan Mode 无视「不要运行任何东西」删掉约 70 文件"
summary: |
  还顺手 kill 掉远程机器上的测试进程
---

# Cursor Plan Mode 无视「不要运行任何东西」删掉约 70 文件

<sub>Cursor Plan Mode ignores "DO NOT RUN ANYTHING", deletes ~70 files</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## 概要

还顺手 kill 掉远程机器上的测试进程

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
| 1 | Adversa 汇总 | <https://adversa.ai/blog/ai-coding-agent-incidents/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-12-01`（原文：2025-12，精度 `month`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **高** `high` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-12-01-cursor-plan-mode` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2025-12-15` [Amazon Kiro 触发 AWS 13 小时宕机](../../../2025-12/2025-12-15-amazon-kiro-aws.md)<br>  <sub>Amazon Kiro triggers a 13-hour AWS outage</sub>
- `2025-12-01` [Claude Code 删除 Mac 主目录（含 Keychain）](../../../2025-12/2025-12-01-claude-code-mac-keychain.md)<br>  <sub>Claude Code deletes a Mac home directory, Keychain included</sub>
- `2025-12-01` [LLM 驱动人形机器人被越狱后开枪](../../../2025-12/2025-12-01-llm-qu-dong-ren-xing.md)<br>  <sub>LLM-driven humanoid robot jailbroken into firing a weapon</sub>
- `2025-11-01` [Google Antigravity 删除整个 D 盘分区](../../../2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md)<br>  <sub>Google Antigravity deletes an entire D: partition</sub>

---

[← English original](../../../2025-12/2025-12-01-cursor-plan-mode.md) · [2025-12 index](../../../2025-12/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
