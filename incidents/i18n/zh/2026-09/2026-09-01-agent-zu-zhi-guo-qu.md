---
id: 2026-09-01-agent-zu-zhi-guo-qu
lang: zh
source: incidents/2026-09/2026-09-01-agent-zu-zhi-guo-qu.md
title: "「88% 的组织在过去一年遭遇确认或疑似 AI agent 安全事故」"
summary: |
  但只有 **6%** 的安全预算用于 AI agent 安全。⚠️ **与另一份「65%」的调查冲突**，两份调研的样本与口径均不明
---

# 「88% 的组织在过去一年遭遇确认或疑似 AI agent 安全事故」

<sub>"88% of organisations hit a confirmed or suspected AI agent security incident this year"</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: C](https://img.shields.io/badge/confidence-C-9A6008?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

> [!WARNING]
> **可信度 C** —— 无一手来源，仅见于二手转述。

## 概要

但只有 **6%** 的安全预算用于 AI agent 安全。⚠️ **与另一份「65%」的调查冲突**，两份调研的样本与口径均不明

## 攻击链

```mermaid
flowchart LR
    E["监管或政策动作"]:::entry
    S0["落到厂商与使用方头上"]:::step
    I["合规要求发生变化"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Beam.ai 汇总 | <https://beam.ai/agentic-insights/ai-agent-security-breaches-2026-lessons> |
| 2 | Kiteworks(65%) | <https://www.kiteworks.com/cybersecurity-risk-management/ai-agent-security-incidents-2026/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-01`（原文：2026-09，精度 `month`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **C** — 仅二手转述，无一手来源 |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-01-agent-zu-zhi-guo-qu` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-09-03` [美参议员提出「Ban Artificial Superintelligence Act」](../../../2026-09/2026-09-03-ban-artificial-superintelligence-act.md)<br>  <sub>US senators introduce the Ban Artificial Superintelligence Act</sub>
- `2026-09-05` [OpenAI 正式承认「wiki 事件」并承诺制定披露框架](../../../2026-09/2026-09-05-wiki-zheng-shi-cheng-ren.md)<br>  <sub>OpenAI formally acknowledges the "wiki incident", promises a disclosure framework</sub>
- `2026-09-07` [日本 IPA 发布《AI セキュリティ短信》2026 年 8 月号](../../../2026-09/2026-09-07-ipa-fa-bu-duan-xin.md)<br>  <sub>Japan's IPA publishes the August 2026 AI Security Bulletin</sub>
- `2026-08-03` [CrowdStrike 2026 威胁狩猎报告](../../../2026-08/2026-08-03-crowdstrike-wei-xie-shou-lie.md)<br>  <sub>CrowdStrike 2026 threat hunting report</sub>

---

[← English original](../../../2026-09/2026-09-01-agent-zu-zhi-guo-qu.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
