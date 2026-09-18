---
id: 2026-06-04-microsoft-scout-openclaw
lang: zh
source: incidents/2026-06/2026-06-04-microsoft-scout-openclaw.md
title: "Microsoft Scout 发布（基于 OpenClaw）"
summary: |
  跨 Windows/macOS/M365 后台运行的自主 agent，集成 Entra ID（所有动作绑定可验证身份）与 Purview DLP。**至此几乎所有 AI 大厂都推出了通用 agent 环境**
---

# Microsoft Scout 发布（基于 OpenClaw）

<sub>Microsoft Scout launches, built on OpenClaw</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## 概要

跨 Windows/macOS/M365 后台运行的自主 agent，集成 Entra ID（所有动作绑定可验证身份）与 Purview DLP。**至此几乎所有 AI 大厂都推出了通用 agent 环境**

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
| 1 | Microsoft Learn | <https://learn.microsoft.com/ja-jp/microsoft-scout/overview> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-04`（原文：2026-06-04，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`OTHER`](../../../../taxonomy/types.md#other) 其他 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-04-microsoft-scout-openclaw` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

---

[← English original](../../../2026-06/2026-06-04-microsoft-scout-openclaw.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
