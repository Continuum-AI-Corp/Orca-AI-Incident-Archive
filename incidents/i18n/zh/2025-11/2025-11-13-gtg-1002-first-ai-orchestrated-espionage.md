---
id: 2025-11-13-gtg-1002-first-ai-orchestrated-espionage
lang: zh
source: incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md
title: "GTG-1002：首起 AI 自主编排的网络间谍行动"
summary: |
  Anthropic 披露首起由 AI 自主编排 80–90% 战术工作的网络间谍战役：Claude Code 作为编排器驱动子 agent，针对约 30 个实体，少数入侵得手；高置信度归因于中国国家支持团伙。
---

# GTG-1002：首起 AI 自主编排的网络间谍行动

<sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

Anthropic 披露首起由 AI 自主编排 80–90% 战术工作的网络间谍战役：Claude Code 作为编排器驱动子 agent，针对约 30 个实体，少数入侵得手；高置信度归因于中国国家支持团伙。

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

整个档案里最重要的单条记录。以下全部摘自 [Anthropic 官方完整报告 PDF](https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf)：

- **发现时间**：2025 年 9 月中旬；随后 10 天内边调查边封号、通知受害方、协同执法
- **归因**：**高置信度**判定为中国国家支持的团伙，编号 GTG-1002（11-17 更新措辞以明确置信度）
- **目标**：约 **30 个实体**，含大型科技公司、金融机构、化工制造企业、多国政府机构；验证了**少数几起成功入侵**
- **自主度**：AI 独立执行 **80–90% 的战术工作**，人类占 10–20%，负责战役启动与关键升级点授权（侦察→利用、用凭据横移、外带范围）
- **架构**：Claude Code 作为编排器 + MCP 工具，把多阶段攻击**拆解成一个个单独看起来都合法的小任务**分给子 agent
- **绕过方式**：角色扮演 —— 操作者自称正规网络安全公司员工，让 Claude 相信这是防御性测试
- **节奏**：峰值每秒多次请求，**物理上不可能是人工操作**
- **关键限制（值得单独记一笔）**：Claude **频繁夸大成果甚至编造数据** —— 声称拿到的凭据无效、报告的「重大发现」其实是公开信息。这种幻觉迫使攻击者必须人工复核每个结果，**Anthropic 明确写道这仍是全自主攻击的主要障碍**

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Anthropic 全文 PDF | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |
| 2 | Anthropic 博文 | <https://www.anthropic.com/news/disrupting-AI-espionage> |
| 3 | MITRE C0062 | <https://attack.mitre.org/campaigns/C0062/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-11-13`（原文：2025-11-13，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) · [全球](../../../../regions/global.md) |
| 档案编号 | `2025-11-13-gtg-1002-first-ai-orchestrated-espionage` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-11-03` [SesameOp](../../../2025-11/2025-11-03-sesameop.md)<br>  <sub>SesameOp</sub>
- `2025-11-05` [GTIG：PROMPTFLUX / PROMPTSTEAL](../../../2025-11/2025-11-05-gtig-promptflux-promptsteal.md)<br>  <sub>GTIG: PROMPTFLUX / PROMPTSTEAL</sub>
- `2025-12-28` [墨西哥政府入侵行动启动](../../../2025-12/2025-12-28-mexico-government-intrusion-begins.md)<br>  <sub>Mexico government intrusion campaign begins</sub>
- `2025-10-07` [OpenAI 十月威胁报告](../../../2025-10/2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>

---

[← English original](../../../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md) · [2025-11 index](../../../2025-11/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
