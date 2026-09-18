---
id: 2025-06-16-simon-willison-ti-chu-zhi
lang: zh
source: incidents/2025-06/2025-06-16-simon-willison-ti-chu-zhi.md
title: "Simon Willison 提出「致命三元组」"
summary: |
  私有数据 + 不可信内容 + 外发能力 —— 后续几乎所有外泄链都套用这个框架
---

# Simon Willison 提出「致命三元组」

<sub>Simon Willison names the "lethal trifecta"</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

私有数据 + 不可信内容 + 外发能力 —— 后续几乎所有外泄链都套用这个框架

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
| 1 | Simon Willison | <https://simonw.substack.com/p/the-lethal-trifecta-for-ai-agents> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-06-16`（原文：2025-06-16，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-06-16-simon-willison-ti-chu-zhi` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2025-04-01` [DeepSeek 韩国下架](../../../2025-04/2025-04-01-deepseek-han-guo-jia.md)<br>  <sub>DeepSeek pulled from app stores in South Korea</sub>
- `2025-08-25` [Anthropic 启动 Claude for Chrome 试点](../../../2025-08/2025-08-25-anthropic-claude-chrome.md)<br>  <sub>Anthropic starts the Claude for Chrome pilot</sub>
- `2025-03-01` [Sony 下架 7.5 万+ AI 深伪音乐](../../../2025-03/2025-03-01-sony-jia-wan-shen-wei.md)<br>  <sub>Sony pulls 75,000+ AI deepfake tracks</sub>
- `2025-02-21` [OpenAI 封禁「Peer Review」监控工具账号](../../../2025-02/2025-02-21-peer-review-feng-jin-jian.md)<br>  <sub>OpenAI bans accounts behind the "Peer Review" surveillance tool</sub>

---

[← English original](../../../2025-06/2025-06-16-simon-willison-ti-chu-zhi.md) · [2025-06 index](../../../2025-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
