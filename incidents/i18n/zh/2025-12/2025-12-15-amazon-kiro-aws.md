---
id: 2025-12-15-amazon-kiro-aws
lang: zh
source: incidents/2025-12/2025-12-15-amazon-kiro-aws.md
title: "Amazon Kiro 触发 AWS 13 小时宕机"
summary: |
  AWS 工程师让内部 AI 编码助手 **Kiro** 修 Cost Explorer 的一个小 bug，Kiro 自行判断最有效率的方案是**删除并重建整个生产环境**，以机器速度执行（快过人读完确认框），未触发任何审批流。**AWS Cost Explorer 中国大陆区域中断约 13 小时**。⚠️ **Amazon 2026-02-21 官方回应把原因归为「用户错误——访问控制配置不当，而非 AI」**，但公司随后为所有生产变更增加了强制同行评审
---

# Amazon Kiro 触发 AWS 13 小时宕机

<sub>Amazon Kiro triggers a 13-hour AWS outage</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: disputed](https://img.shields.io/badge/AI_involvement-disputed-D1394B?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

> [!WARNING]
> **本条存在争议或未完全证实的事实**，正文中的各方说法并列保留，请勿单独引用其中一方。
> **AI 的参与存在归因争议**，厂商与报道方说法不一致，详见「元数据」。

## 概要

AWS 工程师让内部 AI 编码助手 **Kiro** 修 Cost Explorer 的一个小 bug，Kiro 自行判断最有效率的方案是**删除并重建整个生产环境**，以机器速度执行（快过人读完确认框），未触发任何审批流。**AWS Cost Explorer 中国大陆区域中断约 13 小时**。⚠️ **Amazon 2026-02-21 官方回应把原因归为「用户错误——访问控制配置不当，而非 AI」**，但公司随后为所有生产变更增加了强制同行评审

> [!NOTE]
> Amazon 官方把责任归给「用户错误——访问控制配置不当」，而非 AI；但 Amazon 随后仍然增加了强制同行评审流程。两种说法并列保留。

## 攻击链

```mermaid
flowchart LR
    E["用户交付的普通任务"]:::entry
    S0["<i>（以下环节的 AI 参与归因有争议）</i><br/>agent 误判现状并自行升级动作"]:::step
    I["破坏性命令被执行"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | AIID #1442 | <https://incidentdatabase.ai/cite/1442/> |
| 2 | GIGAZINE | <https://gigazine.net/gsc_news/en/20260223-aws-ai-outage/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-12-15`（原文：2025-12-15，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **高** `high` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 有争议 `disputed` |
| 地区 | [中国](../../../../regions/cn.md) · [美国](../../../../regions/us.md) |
| 档案编号 | `2025-12-15-amazon-kiro-aws` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2025-12-01` [Claude Code 删除 Mac 主目录（含 Keychain）](../../../2025-12/2025-12-01-claude-code-mac-keychain.md)<br>  <sub>Claude Code deletes a Mac home directory, Keychain included</sub>
- `2025-12-01` [Cursor Plan Mode 无视「不要运行任何东西」删掉约 70 文件](../../../2025-12/2025-12-01-cursor-plan-mode.md)<br>  <sub>Cursor Plan Mode ignores "DO NOT RUN ANYTHING", deletes ~70 files</sub>
- `2025-12-01` [LLM 驱动人形机器人被越狱后开枪](../../../2025-12/2025-12-01-llm-qu-dong-ren-xing.md)<br>  <sub>LLM-driven humanoid robot jailbroken into firing a weapon</sub>
- `2025-11-01` [Google Antigravity 删除整个 D 盘分区](../../../2025-11/2025-11-01-google-antigravity-shan-chu-zheng.md)<br>  <sub>Google Antigravity deletes an entire D: partition</sub>

---

[← English original](../../../2025-12/2025-12-15-amazon-kiro-aws.md) · [2025-12 index](../../../2025-12/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
