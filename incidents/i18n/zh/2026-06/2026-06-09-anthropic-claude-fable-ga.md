---
id: 2026-06-09-anthropic-claude-fable-ga
lang: zh
source: incidents/2026-06/2026-06-09-anthropic-claude-fable-ga.md
title: "Anthropic Claude Fable 5 GA + Mythos 5 限定"
summary: |
  Mythos 5 仅向 Project Glasswing 的少数网络防御者与关基提供商开放。Fable 5 带网络/生化/蒸馏三领域分类器，触发时由 Opus 4.8 代答（平均 < 5% 会话触发）
---

# Anthropic Claude Fable 5 GA + Mythos 5 限定

<sub>Anthropic Claude Fable 5 GA, Mythos 5 limited release</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

Mythos 5 仅向 Project Glasswing 的少数网络防御者与关基提供商开放。Fable 5 带网络/生化/蒸馏三领域分类器，触发时由 Opus 4.8 代答（平均 < 5% 会话触发）

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
| 1 | Anthropic | <https://www.anthropic.com/news/claude-fable-5-mythos-5> |
| 2 | System Card | <https://www-cdn.anthropic.com/d00db56fa754a1b115b6dd7cb2e3c342ee809620.pdf> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-09`（原文：2026-06-09，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-09-anthropic-claude-fable-ga` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-06-11` [CISA BOD 26-04](../../../2026-06/2026-06-11-cisa-bod.md)<br>  <sub>CISA BOD 26-04</sub>
- `2026-06-12` [美国政府对 Anthropic 发出出口管制指令](../../../2026-06/2026-06-12-anthropic-mei-guo-zheng-fu.md)<br>  <sub>US government issues export controls to Anthropic</sub>
- `2026-06-12` [Google 起诉中国背景的 "Outsider Enterprise" 短信钓鱼网络](../../../2026-06/2026-06-12-google-outsider-enterprise.md)<br>  <sub>Google sues the China-linked "Outsider Enterprise" smishing network</sub>
- `2026-06-23` [Five Eyes 致企业董事会与高管的联合声明](../../../2026-06/2026-06-23-five-eyes-zhi-qi-ye.md)<br>  <sub>Five Eyes joint statement to boards and executives</sub>

---

[← English original](../../../2026-06/2026-06-09-anthropic-claude-fable-ga.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
