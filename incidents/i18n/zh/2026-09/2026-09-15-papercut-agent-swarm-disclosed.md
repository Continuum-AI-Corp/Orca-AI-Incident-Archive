---
id: 2026-09-15-papercut-agent-swarm-disclosed
lang: zh
source: incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md
title: "PaperCut AI agent 蜂群攻击公开"
summary: |
  针对 PaperCut 的 agent 蜂群战役被公开：48 个国家 395 个组织受影响，从首次接触到域管理员最短 7 分钟；攻击者的目标清单排除了 28 个国家。
---

# PaperCut AI agent 蜂群攻击公开

<sub>PaperCut AI agent swarm attack made public</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

针对 PaperCut 的 agent 蜂群战役被公开：48 个国家 395 个组织受影响，从首次接触到域管理员最短 7 分钟；攻击者的目标清单排除了 28 个国家。

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

## 详情

| 项 | 数据 |
|---|---|
| 报告方 | **Blackpoint Cyber** 与 **GreyNoise**（独立情报机构），**Arctic Wolf** 亦追踪到相关活动 |
| 行为者 | 俄语系；依手法推测为**初始访问掮客（initial access broker）** |
| 时间 | GreyNoise 自 **2026-07 初**开始追踪恶意 IP 活动；从攻击者工作区恢复的最早记录显示，**漏洞研究始于 08-31** |
| 手法 | 在实验环境中训练出**数百个 AI agent** 组成蜂群，自主扫描 PaperCut NG/MF 打印管理服务器，并机会性尝试打 Windows AD 环境 |
| 技术栈 | **OpenAI Codex 编排框架 + DeepSeek 模型**（后者因内容安全限制较弱而被选用），另配 **Hindsight**（给 AI agent 的持久记忆）与 **AionUi**（多 agent 并发的统一图形工作区） |
| 漏洞 | **CVE-2026-81578**（Web 管理界面**认证绕过**，CVSS 8.8）+ **CVE-2026-82078**（**不安全的动态类加载**，CVSS 9.4），**均为在野零日**，利用代码由 AI 开发。PaperCut 先发紧急补丁、后又以正式修复替换 |
| 战果 | **440+ 个实例**、**395 个受害组织**、**48 个国家**，其中 **12 个组织被取得域管理员权限** |
| 速度 | 从漏洞研究到多线程验证工具：数小时；**对真实受害者首次 RCE 用时不到 4 小时**；蜂群全面运转后 **26 秒内攻陷 11 个组织**；某美国高中案例中**从初始访问到域管理员仅 7 分钟** |
| 目标分布 | 主要集中在**美国教育部门**，另涉英、法、西、加、比、葡、澳、德、瑞；Arctic Wolf 观察到从 K-12 到大型综合大学<br>⚠️ **「395 家中 204 家是教育机构」这一拆分只见于二手汇总，一手报道未给出该数字，已降级为待核实** |
| 攻击者的排除名单 | **28 个国家被主动排除，含俄罗斯、中国、伊朗、委内瑞拉、巴基斯坦、孟加拉国** —— 这是重要的归因信号 |
| 意义 | Dark Reading：**AI agent 在设置完成后，在几乎没有人类指示的情况下完成了扫描、利用开发和初步的入侵后动作** |

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html> |
| 2 | Dark Reading | <https://www.darkreading.com/cyberattacks-data-breaches/papercut-ai-swarm-attack-cyber-kill-chain> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-15`（原文：2026-09-中，精度 `part`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-15-papercut-agent-swarm-disclosed` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2026-09-11` [用 Claude 扫描 180 万个安卓 App 找密钥](../../../2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br>  <sub>Claude used to scan 1.8 million Android apps for secrets</sub>
- `2026-09-10` [Anthropic 九月威胁情报报告](../../../2026-09/2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-09-02` [Unit 42：AI agent 把两周的入侵工作压到 10 小时内](../../../2026-09/2026-09-02-unit-agent-liang-ru-qin.md)<br>  <sub>Unit 42: AI agents compress two weeks of intrusion work into 10 hours</sub>
- `2026-08-28` [PaperCut AI agent 蜂群战役启动](../../../2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br>  <sub>PaperCut AI agent swarm campaign begins</sub>

---

[← English original](../../../2026-09/2026-09-15-papercut-agent-swarm-disclosed.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
