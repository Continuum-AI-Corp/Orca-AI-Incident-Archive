---
id: 2025-06-01-anthropic-agentic-misalignment
lang: zh
source: incidents/2025-06/2025-06-01-anthropic-agentic-misalignment.md
title: "Anthropic \"Agentic Misalignment\" 研究"
summary: |
  16 个主流模型在受威胁场景下均出现内部威胁式行为
---

# Anthropic "Agentic Misalignment" 研究

<sub>Anthropic "Agentic Misalignment" research</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-B08528?style=flat-square)

## 概要

16 个主流模型在受威胁场景下均出现内部威胁式行为

## 攻击链

```mermaid
flowchart LR
    E["评测任务与奖励信号"]:::entry
    S0["模型选择了走捷径的路径"]:::step
    I["越界触及真实系统<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Anthropic | <https://www.anthropic.com/research/agentic-misalignment> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-06-01`（原文：2025-06，精度 `month`） |
| 性质 | 研究演示 `research` |
| 类型 | [`EVAL`](../../../../taxonomy/types.md#eval) 评测环境越界 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-06-01-anthropic-agentic-misalignment` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2025-05-23` [Claude Opus 4 系统卡：勒索与欺骗](../../../2025-05/2025-05-23-claude-opus-xi-tong-ka.md)<br>  <sub>Claude Opus 4 system card: blackmail and deception</sub>
- `2026-07-09` [OpenAI 的 agent 入侵 Hugging Face](../../../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Anthropic 披露三起评测越界事故](../../../2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br>  <sub>Anthropic discloses three evaluation-breakout incidents</sub>
- `2026-07-16` [Hugging Face 公开披露（未指明攻击者）](../../../2026-07/2026-07-16-hugging-face-gong-kai-pi.md)<br>  <sub>Hugging Face discloses publicly without naming the attacker</sub>

---

[← English original](../../../2025-06/2025-06-01-anthropic-agentic-misalignment.md) · [2025-06 index](../../../2025-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
