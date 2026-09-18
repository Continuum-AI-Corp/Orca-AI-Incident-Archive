---
id: 2025-08-25-anthropic-claude-chrome
lang: zh
source: incidents/2025-08/2025-08-25-anthropic-claude-chrome.md
title: "Anthropic 启动 Claude for Chrome 试点"
summary: |
  仅 1,000 名 Max 用户。自述：**无缓解时提示注入攻击成功率 23.6%，加入缓解后降至 11.2%**
---

# Anthropic 启动 Claude for Chrome 试点

<sub>Anthropic starts the Claude for Chrome pilot</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

仅 1,000 名 Max 用户。自述：**无缓解时提示注入攻击成功率 23.6%，加入缓解后降至 11.2%**

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
| 1 | Anthropic | <https://claude.com/blog/claude-for-chrome> |
| 2 | VentureBeat | <https://venturebeat.com/infrastructure/anthropic-launches-claude-for-chrome-in-limited-beta-but-prompt-injection-attacks-remain-a-major-concern> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-08-25`（原文：2025-08-25，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-08-25-anthropic-claude-chrome` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2025-06-16` [Simon Willison 提出「致命三元组」](../../../2025-06/2025-06-16-simon-willison-ti-chu-zhi.md)<br>  <sub>Simon Willison names the "lethal trifecta"</sub>
- `2025-10-07` [OpenAI 十月威胁报告](../../../2025-10/2025-10-07-shi-wei-xie-bao-gao.md)<br>  <sub>OpenAI October threat report</sub>
- `2025-10-21` [OpenAI Atlas 浏览器发布](../../../2025-10/2025-10-21-atlas-liu-lan-qi-fa.md)<br>  <sub>OpenAI launches the Atlas browser</sub>
- `2025-11-19` [欧盟「数字综合法案(Digital Omnibus)」提议推迟 AI Act](../../../2025-11/2025-11-19-digital-omnibus-act.md)<br>  <sub>EU "Digital Omnibus" proposes delaying the AI Act</sub>

---

[← English original](../../../2025-08/2025-08-25-anthropic-claude-chrome.md) · [2025-08 index](../../../2025-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
