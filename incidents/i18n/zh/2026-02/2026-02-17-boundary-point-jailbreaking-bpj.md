---
id: 2026-02-17-boundary-point-jailbreaking-bpj
lang: zh
source: incidents/2026-02/2026-02-17-boundary-point-jailbreaking-bpj.md
title: "Boundary Point Jailbreaking (BPJ)"
summary: |
  全自动黑盒攻击，**仅靠「是否被拦」的二值反馈** + 课程学习优化对抗前缀，利用对微小变化敏感的「边界点」。**攻破了经受过数千小时红队的 Constitutional Classifiers 与 GPT-5 输入过滤器**，实现通用越狱。研究团队指出：因其会产生大量查询，**单次对话级防御不够，需要批次级监控**
---

# Boundary Point Jailbreaking (BPJ)

<sub>Boundary Point Jailbreaking (BPJ)</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## 概要

全自动黑盒攻击，**仅靠「是否被拦」的二值反馈** + 课程学习优化对抗前缀，利用对微小变化敏感的「边界点」。**攻破了经受过数千小时红队的 Constitutional Classifiers 与 GPT-5 输入过滤器**，实现通用越狱。研究团队指出：因其会产生大量查询，**单次对话级防御不够，需要批次级监控**

## 攻击链

```mermaid
flowchart LR
    E["起点"]:::entry
    S0["过程"]:::step
    I["结果<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | UK AISI | <https://www.aisi.gov.uk/blog/boundary-point-jailbreaking-a-new-way-to-break-the-strongest-ai-defences> |
| 2 | arXiv | <https://arxiv.org/abs/2602.15001v2> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-02-17`（原文：2026-02-17，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`OTHER`](../../../../taxonomy/types.md#other) 其他 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [英国](../../../../regions/uk.md) |
| 档案编号 | `2026-02-17-boundary-point-jailbreaking-bpj` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

---

[← English original](../../../2026-02/2026-02-17-boundary-point-jailbreaking-bpj.md) · [2026-02 index](../../../2026-02/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
