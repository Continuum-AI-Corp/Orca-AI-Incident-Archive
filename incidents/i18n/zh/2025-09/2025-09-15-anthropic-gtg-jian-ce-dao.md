---
id: 2025-09-15-anthropic-gtg-jian-ce-dao
lang: zh
source: incidents/2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md
title: "Anthropic 检测到 GTG-1002"
summary: |
  Anthropic 在 9 月中旬内部检测到 GTG-1002 战役，随后 10 天边调查边封号、通知受害方，直到 11-13 才公开。
---

# Anthropic 检测到 GTG-1002

<sub>Anthropic detects GTG-1002</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

Anthropic 在 9 月中旬内部检测到 GTG-1002 战役，随后 10 天边调查边封号、通知受害方，直到 11-13 才公开。

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
| 1 | Anthropic PDF | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-09-15`（原文：2025-09-中，精度 `part`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-09-15-anthropic-gtg-jian-ce-dao` |

<sub>**判定依据**：真实事故，未见确认的具体受害方。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-09-02` [HexStrike-AI 被威胁方用于打 Citrix 0-day](../../../2025-09/2025-09-02-hexstrike-citrix-day.md)<br>  <sub>HexStrike-AI turned on a Citrix zero-day</sub>
- `2025-09-01` [Villager（Cyberspike）AI 渗透工具](../../../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-08-26` [ESET 发现 PromptLock](../../../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-08-27` [Anthropic 八月威胁报告](../../../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>

---

[← English original](../../../2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md) · [2025-09 index](../../../2025-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
