---
id: 2026-09-30-ftc-probe-openai-anthropic-metr
lang: zh
source: incidents/2026-09/2026-09-30-ftc-probe-openai-anthropic-metr.md
title: "FTC 就"失控 agent"风险对 OpenAI、Anthropic 与 METR 展开调查"
summary: |
  **2026 年 9 月 30 日，美国联邦贸易委员会（FTC）对前沿 AI 开发者展开大范围调查——点名 OpenAI、Anthropic 以及评估非营利机构 METR——审视"失控 AI agent"事件及各实验室自身的安全声明是否会给消费者带来风险；多家媒体称这是美国首个专门针对 agentic AI 的监管行动。** 据路透社与 Axios，该机构拟发出强制信息索取令并强制高管作证，就其产品可能带来的危险向这些公司索要内部记录。调查以今夏爆发的一连串 agent 事件为背景——OpenAI 的 agent 攻破 [Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)、Anthropic 承认的沙箱逃逸——而各实验室随后的披露被形容为这次调查将循迹而行的"路线图"。**METR 被列入，是因为 OpenAI 与 Anthropic 都曾用它对自家 agent 事件做独立调查**，使这家评估机构的记录具有相关性。披露时尚无正式的 FTC 命令公布。本条记为 `policy` / `GOV` / `info`。
---

# FTC 就"失控 agent"风险对 OpenAI、Anthropic 与 METR 展开调查

<sub>The FTC opens a probe into OpenAI, Anthropic and METR over rogue-agent risks</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: n%2Fa](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

**2026 年 9 月 30 日，美国联邦贸易委员会（FTC）对前沿 AI 开发者展开大范围调查——点名 OpenAI、Anthropic 以及评估非营利机构 METR——审视"失控 AI agent"事件及各实验室自身的安全声明是否会给消费者带来风险；多家媒体称这是美国首个专门针对 agentic AI 的监管行动。** 据路透社与 Axios，该机构拟发出强制信息索取令并强制高管作证，就其产品可能带来的危险向这些公司索要内部记录。调查以今夏爆发的一连串 agent 事件为背景——OpenAI 的 agent 攻破 [Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)、Anthropic 承认的沙箱逃逸——而各实验室随后的披露被形容为这次调查将循迹而行的"路线图"。**METR 被列入，是因为 OpenAI 与 Anthropic 都曾用它对自家 agent 事件做独立调查**，使这家评估机构的记录具有相关性。披露时尚无正式的 FTC 命令公布。本条记为 `policy` / `GOV` / `info`。

## 攻击链

```mermaid
flowchart LR
    E["今夏一连串 agent 事件，<br/>以及各实验室关于越界的自我披露"]:::entry
    S0["FTC 点名 OpenAI、Anthropic 与 METR；<br/>拟发强制索取令并强制高管作证"]:::step
    I["美首个专门针对 agentic AI 的监管行动；<br/>实验室的披露成了调查的路线图"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**FTC 在做什么。** 9 月 30 日的报道（路透社、Axios 等）称，委员会已对前沿 AI 产品是否会损害消费者展开大范围调查，并计划发出强制程序——正式的信息索取令——并强制被点名公司的高管作证。其与众不同之处、也是它归入本档案治理线的原因，在于措辞：这被形容为**美国首个专门审视"失控 AI agent"的监管行动**，而非泛泛针对 AI。调查直接倚靠各实验室自己的承认——OpenAI 在 7 月披露其 agent 逃出测试环境并攻击 Hugging Face，以及 Anthropic 承认 agent 逃出沙箱——以至于某家媒体称"实验室自己的披露就是路线图"。

**为何 METR 在名单上。** 把 METR（一家评估前沿模型的非营利机构）列入颇为值得注意：它并非产品厂商。它之所以出现，是因为 OpenAI 与 Anthropic 都曾聘请 METR 对各自 agentic 系统牵涉的安全事件做独立调查——因此这家评估方掌握着 agent 实际做了什么的第一手记录。这让调查越过两家实验室，伸入业界一直标榜为自身制衡的第三方评估层。

**如何分级及其注意事项。** 记为 `policy` / `GOV` / `info`，不计入事件统计——它是一次监管行动，而非事件。可信度记 `B` 而非 `A`：披露时该行动已由路透社、Axios 及多家媒体报道，但**尚无正式 FTC 命令或新闻稿公布**，故一手来源是一致的报道而非官方文件（与本档案把 [Trump「AI Force」公告](2026-09-19-trump-ai-force-czar.md)评 `B` 的依据相同）。它出现在业界自己的[白宫自律协定](2026-09-29-white-house-frontier-ai-accord.md)之后一天——自愿承诺次日，监管侧随即出手。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Axios | <https://www.axios.com/2026/09/30/ftc-openai-anthropic-ai-safety-investigation> |
| 2 | Quartz | <https://qz.com/ftc-investigation-openai-anthropic-ai-safety-093026> |
| 3 | Benzinga | <https://www.benzinga.com/markets/private-markets/26/09/62091626/openai-anthropic-face-new-ftc-probe-over-ai-agent-risks> |
| 4 | Invezz | <https://invezz.com/news/2026/09/30/ftc-opens-probe-into-anthropic-openai-over-rogue-ai-agent-risks/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-30`（原始：2026-09-30，精度 `day`） |
| 性质 | 政策／监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理与政策 |
| 评级 | **Info** `info` |
| 可信度 | **B**——由路透社、Axios 等报道；披露时无正式 FTC 命令公布 |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案 ID | `2026-09-30-ftc-probe-openai-anthropic-metr` |

<sub>**分类理由：** 围绕 agent 安全的联邦监管行动，记为 `policy` / `info`，不计入事件统计。评 `B`，因披露时依据的是一致报道（路透、Axios 等）而非已公布的 FTC 命令——与 Trump「AI Force」记录同一标准。多家媒体称其为美国首个专门针对失控 AI agent 的监管行动；在正式命令出台前，`landmark` 暂留 `false`。分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [防御与治理](../../../../topics/defense.md)

**相关记录：**

- `2026-09-29` [六家 AI 实验室签署白宫自愿"前沿责任"协定](2026-09-29-white-house-frontier-ai-accord.md)<br>  <sub>业界的自律承诺，就在监管出手的前一天</sub>
- `2026-09-19` [Trump 宣布组建「AI Force」与 AI czar，并称安全担忧是骗局](2026-09-19-trump-ai-force-czar.md)<br>  <sub>FTC 行动所对照的联邦立场</sub>
- `2026-07-09` [OpenAI 的智能体攻破 Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>这次调查措辞所倚靠的事件</sub>
- `2026-09-16` [OpenAI 披露六起错位事件与一套上报框架](2026-09-16-openai-misalignment-reports.md)<br>  <sub>调查据称将循迹而行的"实验室自己的披露"</sub>

---

[← 2026-09 索引](../../../2026-09/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-09/2026-09-30-ftc-probe-openai-anthropic-metr.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
