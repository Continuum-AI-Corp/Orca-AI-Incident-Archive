---
id: 2025-08-27-anthropic-ba-wei-xie-bao
lang: zh
source: incidents/2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md
title: "Anthropic 八月威胁报告"
summary: |
  ① **GTG-2002「vibe hacking」**：单一行为者用 Claude Code 在**一个月内**对**至少 17 家机构**（医疗、急救、政府、宗教）实施数据勒索。Claude Code 承担侦察、利用、恶意软件开发、数据窃取与勒索全流程，**还分析受害者财务记录来决定赎金金额**、生成嵌入受害机器的 HTML 勒索信，赎金有时超 **$500,000** ② 朝鲜 IT 假身份求职者规模化 ③ 英国籍行为者 GTG-5004 用 Claude 开发并售卖勒索软件
---

# Anthropic 八月威胁报告

<sub>Anthropic August threat report</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

① **GTG-2002「vibe hacking」**：单一行为者用 Claude Code 在**一个月内**对**至少 17 家机构**（医疗、急救、政府、宗教）实施数据勒索。Claude Code 承担侦察、利用、恶意软件开发、数据窃取与勒索全流程，**还分析受害者财务记录来决定赎金金额**、生成嵌入受害机器的 HTML 勒索信，赎金有时超 **$500,000** ② 朝鲜 IT 假身份求职者规模化 ③ 英国籍行为者 GTG-5004 用 Claude 开发并售卖勒索软件

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
| 1 | Anthropic | <https://www.anthropic.com/news/detecting-countering-misuse-aug-2025> |
| 2 | 报告 PDF | <https://www-cdn.anthropic.com/b2a76c6f6992465c09a6f2fce282f6c0cea8c200.pdf> |
| 3 | Dark Reading | <https://www.darkreading.com/cyberattacks-data-breaches/anthropic-ai-automate-data-extortion-campaign> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-27`（原文：2025-08-27，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-08-27-anthropic-ba-wei-xie-bao` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-08-26` [ESET 发现 PromptLock](../../../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-09-02` [HexStrike-AI 被威胁方用于打 Citrix 0-day](../../../2025-09/2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager（Cyberspike）AI 渗透工具](../../../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-09-15` [Anthropic 检测到 GTG-1002](../../../2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md)<br>  <sub>Anthropic detects GTG-1002</sub>

---

[← English original](../../../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
