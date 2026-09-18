---
id: 2025-01-27-deepseek-zao-gui-mo-gong
lang: zh
source: incidents/2025-01/2025-01-27-deepseek-zao-gui-mo-gong.md
title: "DeepSeek 遭大规模攻击，限制注册"
summary: |
  奇安信 XLab 记录反射攻击、HTTP 代理攻击、DDoS、僵尸网络多轮
---

# DeepSeek 遭大规模攻击，限制注册

<sub>DeepSeek hit by large-scale attacks, halts signups</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## 概要

奇安信 XLab 记录反射攻击、HTTP 代理攻击、DDoS、僵尸网络多轮

## 攻击链

```mermaid
flowchart LR
    E["起点"]:::entry
    S0["过程"]:::step
    I["结果"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | 安全内参 | <https://www.secrss.com/articles/86614> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-01-27`（原文：2025-01-27，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`OTHER`](../../../../taxonomy/types.md#other) 其他 |
| 严重度 | **中** `medium` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) |
| 档案编号 | `2025-01-27-deepseek-zao-gui-mo-gong` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

---

[← English original](../../../2025-01/2025-01-27-deepseek-zao-gui-mo-gong.md) · [2025-01 index](../../../2025-01/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
