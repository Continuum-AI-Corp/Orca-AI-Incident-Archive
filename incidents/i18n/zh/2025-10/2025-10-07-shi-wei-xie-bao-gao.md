---
id: 2025-10-07-shi-wei-xie-bao-gao
lang: zh
source: incidents/2025-10/2025-10-07-shi-wei-xie-bao-gao.md
title: "OpenAI 十月威胁报告"
summary: |
  自 2024-02 起累计瓦解 **40+ 网络**；披露中国政府相关的社媒监控提案、柬埔寨/缅甸/尼日利亚诈骗网络。核心判断：**攻击者是把 AI 接到旧剧本上提速，而不是获得了新的攻击能力**
---

# OpenAI 十月威胁报告

<sub>OpenAI October threat report</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

自 2024-02 起累计瓦解 **40+ 网络**；披露中国政府相关的社媒监控提案、柬埔寨/缅甸/尼日利亚诈骗网络。核心判断：**攻击者是把 AI 接到旧剧本上提速，而不是获得了新的攻击能力**

## 攻击链

```mermaid
flowchart LR
    E["攻击者 + 越狱话术"]:::entry
    S0["LLM 编排器驱动子 agent 集群"]:::step
    S1["落到厂商与使用方头上"]:::step
    I["合规要求发生变化"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | OpenAI | <https://openai.com/global-affairs/disrupting-malicious-uses-of-ai-october-2025/> |
| 2 | PDF | <https://cdn.openai.com/threat-intelligence-reports/7d662b68-952f-4dfd-a2f2-fe55b041cc4a/disrupting-malicious-uses-of-ai-october-2025.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-10-07`（原文：2025-10-07，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 · [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-10-07-shi-wei-xie-bao-gao` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md) · [防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2025-10-21` [OpenAI Atlas 浏览器发布](../../../2025-10/2025-10-21-atlas-liu-lan-qi-fa.md)<br>  <sub>OpenAI launches the Atlas browser</sub>
- `2025-11-13` [GTG-1002：首起 AI 自主编排的网络间谍行动](../../../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub>
- `2025-09-02` [HexStrike-AI 被威胁方用于打 Citrix 0-day](../../../2025-09/2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager（Cyberspike）AI 渗透工具](../../../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>

---

[← English original](../../../2025-10/2025-10-07-shi-wei-xie-bao-gao.md) · [2025-10 index](../../../2025-10/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
