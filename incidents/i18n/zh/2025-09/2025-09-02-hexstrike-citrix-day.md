---
id: 2025-09-02-hexstrike-citrix-day
lang: zh
source: incidents/2025-09/2025-09-02-hexstrike-citrix-day.md
title: "HexStrike-AI 被威胁方用于打 Citrix 0-day"
summary: |
  Check Point：开源 AI 攻防框架发布后数小时，暗网即出现用其批量利用 NetScaler 漏洞（含零日 **CVE-2025-7775**）的讨论。**150 个自主 agent，10 分钟内完成利用**，并有人立即倒卖已控设备
---

# HexStrike-AI 被威胁方用于打 Citrix 0-day

<sub>HexStrike-AI turned on a Citrix zero-day</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

Check Point：开源 AI 攻防框架发布后数小时，暗网即出现用其批量利用 NetScaler 漏洞（含零日 **CVE-2025-7775**）的讨论。**150 个自主 agent，10 分钟内完成利用**，并有人立即倒卖已控设备

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
| 1 | Check Point | <https://blog.checkpoint.com/executive-insights/hexstrike-ai-when-llms-meet-zero-day-exploitation/> |
| 2 | THN | <https://thehackernews.com/2025/09/threat-actors-weaponize-hexstrike-ai-to.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-09-02`（原文：2025-09-02，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-09-02-hexstrike-citrix-day` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-09-01` [Villager（Cyberspike）AI 渗透工具](../../../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>Villager (Cyberspike) AI pentest tool</sub>
- `2025-09-15` [Anthropic 检测到 GTG-1002](../../../2025-09/2025-09-15-anthropic-gtg-jian-ce-dao.md)<br>  <sub>Anthropic detects GTG-1002</sub>
- `2025-08-26` [ESET 发现 PromptLock](../../../2025-08/2025-08-26-eset-promptlock-fa-xian.md)<br>  <sub>ESET finds PromptLock</sub>
- `2025-08-27` [Anthropic 八月威胁报告](../../../2025-08/2025-08-27-anthropic-ba-wei-xie-bao.md)<br>  <sub>Anthropic August threat report</sub>

---

[← English original](../../../2025-09/2025-09-02-hexstrike-citrix-day.md) · [2025-09 index](../../../2025-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
