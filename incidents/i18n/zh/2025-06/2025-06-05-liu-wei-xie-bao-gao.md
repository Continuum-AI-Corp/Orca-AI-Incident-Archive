---
id: 2025-06-05-liu-wei-xie-bao-gao
lang: zh
source: incidents/2025-06/2025-06-05-liu-wei-xie-bao-gao.md
title: "OpenAI 六月威胁报告"
summary: |
  披露来自 6 个国家的 10 起行动，含 **ScopeCreep**（俄语系行为者用 ChatGPT 编写并调试 Windows 恶意软件，连 Telegram 告警功能都让 AI 排错）、Sneer Review、Uncle Spam、VAGue Focus、Helgoland Bite、Wrong Number
---

# OpenAI 六月威胁报告

<sub>OpenAI June threat report</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

披露来自 6 个国家的 10 起行动，含 **ScopeCreep**（俄语系行为者用 ChatGPT 编写并调试 Windows 恶意软件，连 Telegram 告警功能都让 AI 排错）、Sneer Review、Uncle Spam、VAGue Focus、Helgoland Bite、Wrong Number

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
| 1 | OpenAI PDF | <https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-06-05`（原文：2025-06-05，精度 `day`） |
| 性质 | 威胁情报报告 `report` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-06-05-liu-wei-xie-bao-gao` |

<sub>**判定依据**：威胁情报报告，汇总多起事件，本身不作为单一事故计数，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-06-01` [Check Point「Skynet」样本](../../../2025-06/2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-01` [Anthropic 记录 GTG-1002 前身活动](../../../2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-05-01` [Anthropic 记录 GTG-2002 活动起点](../../../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI 驱动的撞库与自动化扫描规模化](../../../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>

---

[← English original](../../../2025-06/2025-06-05-liu-wei-xie-bao-gao.md) · [2025-06 index](../../../2025-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
