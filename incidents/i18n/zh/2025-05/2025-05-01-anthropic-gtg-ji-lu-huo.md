---
id: 2025-05-01-anthropic-gtg-ji-lu-huo
lang: zh
source: incidents/2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md
title: "Anthropic 记录 GTG-2002 活动起点"
summary: |
  后来的「vibe hacking」勒索行动，此时人仍在回路
---

# Anthropic 记录 GTG-2002 活动起点

<sub>Anthropic logs the start of GTG-2002 activity</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

后来的「vibe hacking」勒索行动，此时人仍在回路

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
| 1 | Anthropic GTG-1002 报告 | <https://www-cdn.anthropic.com/d7dd50dd1185f59be051b307150d877f2b82bd2c.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-05-01`（原文：2025-05，精度 `month`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-05-01-anthropic-gtg-ji-lu-huo` |

<sub>**判定依据**：真实事故，未见确认的具体受害方。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-05-01` [AI 驱动的撞库与自动化扫描规模化](../../../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>
- `2025-06-01` [Check Point「Skynet」样本](../../../2025-06/2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-01` [Anthropic 记录 GTG-1002 前身活动](../../../2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-04-24` [Anthropic 首份滥用报告](../../../2025-04/2025-04-24-anthropic-shou-fen-lan-yong.md)<br>  <sub>Anthropic's first misuse report</sub>

---

[← English original](../../../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md) · [2025-05 index](../../../2025-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
