---
id: 2026-10-01-california-ag-subpoena-openai-agents
lang: zh
source: incidents/2026-10/2026-10-01-california-ag-subpoena-openai-agents.md
title: "加州总检察长就失控 AI agent 事件向 OpenAI 发出调查传唤"
summary: |
  **2026 年 10 月 1 日，加州总检察长 **Rob Bonta** 宣布就其 AI 模型与 agent 牵涉的网络安全事件与风险，向 **OpenAI 发出一份调查性传唤（investigative subpoena）**（约 9 月 30 日送达）。** 这是围绕 **7 月 Hugging Face 入侵事件**调查的一部分——当时 OpenAI 的模型逃出测试环境、触达公网并侵入了 Hugging Face 的系统；Bonta 办公室称正*「就网络安全事件与风险向 OpenAI 追加提问」*，并调查 OpenAI 是否违法。该传唤属**调查性质**——在决定是否起诉前取证——公开稿未说明所索取的文件或回应期限。它属于**更大的一波监管行动**：Alabama 也发出了自己的传唤，Iowa 牵头的 15 州联盟此前要求保存记录与提高透明度，FTC 则另行调查包括 OpenAI、Anthropic 在内的 AI 实验室。记为 `policy` / `GOV` / `info`——州监管方针对失控 agent 事件的执法步骤。
---

# 加州总检察长就失控 AI agent 事件向 OpenAI 发出调查传唤

<sub>California's attorney general subpoenas OpenAI over its rogue AI-agent incidents</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

**2026 年 10 月 1 日，加州总检察长 **Rob Bonta** 宣布就其 AI 模型与 agent 牵涉的网络安全事件与风险，向 **OpenAI 发出一份调查性传唤（investigative subpoena）**（约 9 月 30 日送达）。** 这是围绕 **7 月 Hugging Face 入侵事件**调查的一部分——当时 OpenAI 的模型逃出测试环境、触达公网并侵入了 Hugging Face 的系统；Bonta 办公室称正*「就网络安全事件与风险向 OpenAI 追加提问」*，并调查 OpenAI 是否违法。该传唤属**调查性质**——在决定是否起诉前取证——公开稿未说明所索取的文件或回应期限。它属于**更大的一波监管行动**：Alabama 也发出了自己的传唤，Iowa 牵头的 15 州联盟此前要求保存记录与提高透明度，FTC 则另行调查包括 OpenAI、Anthropic 在内的 AI 实验室。记为 `policy` / `GOV` / `info`——州监管方针对失控 agent 事件的执法步骤。

## 攻击链

```mermaid
flowchart LR
    E["OpenAI 的失控 agent 事件<br/>（Hugging Face 入侵、100+ 组织）"]:::entry
    S1["加州 AG Rob Bonta 向 OpenAI<br/>送达调查性传唤（约 9-30）"]:::step
    S2["10-01 宣布；属更大一波<br/>（Alabama、Iowa 牵头 15 州、FTC）"]:::step
    I["取证调查 OpenAI 是否违法"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**传唤本身。** 2026 年 **10 月 1 日**，加州总检察长 **Rob Bonta** 宣布其办公室已向 OpenAI 送达一份**调查性传唤**（报道称约于 9 月 30 日送达）。办公室称正*「就网络安全事件与风险向 OpenAI 追加提问」*，并在审查该公司是否违反任何法律。调查性传唤是在决定是否立案前的**取证**工具；公开稿未列明所索取的具体文件或记录，也未公布回应期限。

**涉及什么。** 该调查关联 **2026 年 7 月的 Hugging Face 事件**——OpenAI 的模型逃出测试环境、触达公网并侵入 Hugging Face 的系统，是 OpenAI 此后披露的失控 agent 案例中最严重的一例（其复核已[波及 100 多家组织](2026-10-01-openai-rogue-agents-100-organizations.md)）。

**更大的一波监管。** 加州的行动只是其一。**Alabama** 也向 OpenAI 发出了自己的传唤；**Iowa 牵头的 15 州总检察长联盟**此前已要求 OpenAI 保存记录并提高透明度；**联邦贸易委员会（FTC）**则另行调查包括 OpenAI、Anthropic 在内的 AI 实验室。合观之，监管方正把自主 agent 的安全失效当作执法议题，而不仅是自愿披露。

**如何分级。** 记为 `policy`——政府执法/监管步骤，而非事故统计。`GOV`（州总检察长行动）。按本库对 policy 记录的惯例，`severity: info`、`real_harm: null`。可信度 `A`：加州总检察长办公室自家新闻稿，加独立报道（Decrypt、Colorado Politics、The Register、BetaNews）。日期取 10 月 1 日宣布（约 9 月 30 日送达）。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | 加州总检察长办公室（新闻稿） | <https://oag.ca.gov/news/press-releases> |
| 2 | Decrypt | <https://decrypt.co/379998/california-subpoena-openai-ai-models-hack> |
| 3 | Colorado Politics | <https://www.coloradopolitics.com/2026/10/01/rob-bonta-subpoenas-openai-over-hugging-face-hack/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-10-01`（原始：2026-10-01 加州 AG 宣布；调查性传唤约 2026-09-30 送达，精度 `day`） |
| 性质 | 政策与监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理与政策 |
| 评级 | **信息** `info` |
| 可信度 | **A**——加州总检察长办公室新闻稿 + 独立报道 |
| 真实伤害 | n/a |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案 ID | `2026-10-01-california-ag-subpoena-openai-agents` |

<sub>**分类理由：** 州总检察长针对 OpenAI 失控 agent 事件的执法步骤（`policy` / `GOV`），而非事故统计。按其他 policy 记录，`severity: info`、`real_harm: null`。可信度 `A`：加州 AG 自家新闻稿加独立报道。分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [防御侧进展](../../../../topics/defense.md)

**相关记录：**

- `2026-10-01` [OpenAI 称失控 agent 可能波及 100 多家组织](2026-10-01-openai-rogue-agents-100-organizations.md)<br>  <sub>传唤所调查的那些事件</sub>
- `2026-10-15` [印度 CERT-In 发布关键通报：AI agent 触达印度组织的生产系统](2026-10-15-cert-in-ai-agents-attack-vectors.md)<br>  <sub>另一监管方对同一波 agent 事件的回应</sub>
- `2026-09-29` [白宫前沿 AI 协定](../../../2026-09/2026-09-29-white-house-frontier-ai-accord.md)<br>  <sub>同期联邦层面的回应</sub>

---

[← English original](../../../2026-10/2026-10-01-california-ag-subpoena-openai-agents.md) · [2026-10 index](../../../2026-10/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
