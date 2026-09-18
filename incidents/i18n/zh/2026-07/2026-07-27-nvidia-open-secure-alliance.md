---
id: 2026-07-27-nvidia-open-secure-alliance
lang: zh
source: incidents/2026-07/2026-07-27-nvidia-open-secure-alliance.md
title: "NVIDIA 牵头成立 Open Secure AI Alliance"
summary: |
  值得注意的论点：NVIDIA 举例称**闭源 AI 无法区分攻击方与防御方、阻碍取证分析**，Hugging Face 只能改用开源权重的 **GLM 5.2** 自建来解析 1.7 万+ 操作，因此呼吁政策当局把开放模型与工具当作防御资产、不要一刀切限制
---

# NVIDIA 牵头成立 Open Secure AI Alliance

<sub>NVIDIA convenes the Open Secure AI Alliance</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

值得注意的论点：NVIDIA 举例称**闭源 AI 无法区分攻击方与防御方、阻碍取证分析**，Hugging Face 只能改用开源权重的 **GLM 5.2** 自建来解析 1.7 万+ 操作，因此呼吁政策当局把开放模型与工具当作防御资产、不要一刀切限制

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
| 1 | NVIDIA | <https://blogs.nvidia.com/blog/open-secure-ai-alliance/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-27`（原文：2026-07-27，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-27-nvidia-open-secure-alliance` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-07-17` [Anthropic《a CISO's guide to agentic AI》](../../../2026-07/2026-07-17-anthropic-ciso-guide-agentic.md)<br>  <sub>Anthropic, "A CISO's guide to agentic AI"</sub>
- `2026-07-23` [美国众议员提出「AI Kill Switch Act」](../../../2026-07/2026-07-23-kill-switch-act.md)<br>  <sub>US representatives introduce the AI Kill Switch Act</sub>
- `2026-07-28` [「Pacing the Frontier」公开信](../../../2026-07/2026-07-28-pacing-frontier-gong-kai-xin.md)<br>  <sub>"Pacing the Frontier" open letter</sub>
- `2026-07-29` [Perplexity 开源 agent 行为监控 Numbat](../../../2026-07/2026-07-29-perplexity-agent-numbat.md)<br>  <sub>Perplexity open-sources Numbat for agent behaviour monitoring</sub>

---

[← English original](../../../2026-07/2026-07-27-nvidia-open-secure-alliance.md) · [2026-07 index](../../../2026-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
