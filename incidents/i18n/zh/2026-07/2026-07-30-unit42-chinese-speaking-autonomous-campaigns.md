---
id: 2026-07-30-unit42-chinese-speaking-autonomous-campaigns
lang: zh
source: incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md
title: "Unit 42：中文使用者的自主攻击战役"
summary: |
  行为者位于**珠海**，化名 knaithe / KnYuan，运营自动化漏洞情报流水线 1DayNews。主执行器是 **Hermes Agent + DeepSeek**（Claude Code 仅用于连通性测试与代理验证，Codex 仅少量测试）。尝试 **460+ 个目标**、7 个 CVE。**自主部分多因前提条件不满足而失败**（Langflow 目标没开 auto_login、n8n 没有未认证公开表单）；**手动部分确实得手**：Citrix NetScaler CVE-2026-3055 从 **3 个组织**外带数据、Marimo **11 个实例**命令执行、Tomcat CVE-2026-34486 对 9 台服务器尝试反弹 shell。马来西亚政府机构被连续多日针对。Unit 42 判断：**成败之差很小，自主攻击循环在运营上已经成立**
---

# Unit 42：中文使用者的自主攻击战役

<sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

行为者位于**珠海**，化名 knaithe / KnYuan，运营自动化漏洞情报流水线 1DayNews。主执行器是 **Hermes Agent + DeepSeek**（Claude Code 仅用于连通性测试与代理验证，Codex 仅少量测试）。尝试 **460+ 个目标**、7 个 CVE。**自主部分多因前提条件不满足而失败**（Langflow 目标没开 auto_login、n8n 没有未认证公开表单）；**手动部分确实得手**：Citrix NetScaler CVE-2026-3055 从 **3 个组织**外带数据、Marimo **11 个实例**命令执行、Tomcat CVE-2026-34486 对 9 台服务器尝试反弹 shell。马来西亚政府机构被连续多日针对。Unit 42 判断：**成败之差很小，自主攻击循环在运营上已经成立**

## 攻击链

```mermaid
flowchart LR
    E["攻击者 + 越狱话术"]:::entry
    S0["LLM 编排器驱动子 agent 集群"]:::step
    I["目标系统被攻陷"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Unit 42 | <https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/> |
| 2 | Hunt.io 四国报告 | <https://hunt.io/blog/chinese-operators-claude-deepseek-government-intrusion> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-30`（原文：2026-07-30，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) · [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-30-unit42-chinese-speaking-autonomous-campaigns` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-07-01` [台湾核安会等政府机构被 agent 蜂群攻破](../../../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-01` [JADEPUFFER：首起 LLM 全程驱动的勒索攻击](../../../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI 的 agent 入侵 Hugging Face](../../../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Hermes Agent 无人值守模式攻击泰国财政部](../../../2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub>

---

[← English original](../../../2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md) · [2026-07 index](../../../2026-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
