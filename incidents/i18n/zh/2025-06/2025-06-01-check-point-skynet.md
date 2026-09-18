---
id: 2025-06-01-check-point-skynet
lang: zh
source: incidents/2025-06/2025-06-01-check-point-skynet.md
title: "Check Point「Skynet」样本"
summary: |
  恶意软件内嵌提示注入串，诱导 AI 分析引擎输出「NO MALWARE DETECTED」—— **首个针对 AI 分析器的规避样本**
---

# Check Point「Skynet」样本

<sub>Check Point's "Skynet" sample</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## 概要

恶意软件内嵌提示注入串，诱导 AI 分析引擎输出「NO MALWARE DETECTED」—— **首个针对 AI 分析器的规避样本**

## 攻击链

```mermaid
flowchart LR
    E["攻击者 + 越狱话术"]:::entry
    S0["LLM 编排器驱动子 agent 集群"]:::step
    I["目标系统被攻陷<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Check Point Research | <https://research.checkpoint.com/2025/ai-evasion-prompt-injection/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-06-01`（原文：2025-06，精度 `month`） |
| 性质 | 研究演示 `research` |
| 类型 | [`WEAPON`](../../../../taxonomy/types.md#weapon) agent 被用作攻击工具 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-06-01-check-point-skynet` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[攻击方 AI 能力演进](../../../../topics/offensive-ai.md)

**同类条目**：

- `2025-06-01` [Anthropic 记录 GTG-1002 前身活动](../../../2025-06/2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-06-05` [OpenAI 六月威胁报告](../../../2025-06/2025-06-05-liu-wei-xie-bao-gao.md)<br>  <sub>OpenAI June threat report</sub>
- `2025-05-01` [Anthropic 记录 GTG-2002 活动起点](../../../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI 驱动的撞库与自动化扫描规模化](../../../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>

---

[← English original](../../../2025-06/2025-06-01-check-point-skynet.md) · [2025-06 index](../../../2025-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
