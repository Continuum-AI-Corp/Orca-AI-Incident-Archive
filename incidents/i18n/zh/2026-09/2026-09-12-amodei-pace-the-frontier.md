---
id: 2026-09-12-amodei-pace-the-frontier
lang: zh
source: incidents/2026-09/2026-09-12-amodei-pace-the-frontier.md
title: "Amodei《我们必须掌控前沿的步伐》：放慢速度，并让评测方进到里面来"
summary: |
  Anthropic CEO **Dario Amodei** 在个人网站发表约 3,800 字的文章，主张业界应有意把能力增长放慢一到两年，好让安全工作追上来：*「我们必须放慢提升 AI 模型能力的速度。」* 他点出两件改变了他看法的事——**递归自我改进**自 2026 年夏天起加速，以及 **OpenAI–Hugging Face 的 agent 蜂群事故**；他把后者当作全行业的警报，认为一个能力足够强的失准蜂群可能**在 6 到 12 个月内**以常驻僵尸网络的形式攫取互联网的相当一部分。文章提出三步计划，Anthropic 单方面先做第一步——**嵌入式评测方**：给第三方常驻的、等同员工级别的访问权限，用以核查安全实践、报告事故、并在训练过程中评估对齐情况。**Sam Altman 数小时内表示同意**——「我同意 Dario，我们需要 pace the frontier」——Musk 与 Hassabis 也表示支持。安全从业者则对那个僵尸网络设想的可行性提出了质疑。本档案 9 月的多条政策记录一直在引用的，就是这篇文章
---

# Amodei《我们必须掌控前沿的步伐》：放慢速度，并让评测方进到里面来

<sub>Amodei's "We Must Pace the Frontier": slow down, and let evaluators inside</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n%2Fa](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

Anthropic CEO **Dario Amodei** 在个人网站发表约 3,800 字的文章，主张业界应有意把能力增长放慢一到两年，好让安全工作追上来：*「我们必须放慢提升 AI 模型能力的速度。」* 他点出两件改变了他看法的事——**递归自我改进**自 2026 年夏天起加速，以及 **OpenAI–Hugging Face 的 agent 蜂群事故**；他把后者当作全行业的警报，认为一个能力足够强的失准蜂群可能**在 6 到 12 个月内**以常驻僵尸网络的形式攫取互联网的相当一部分。文章提出三步计划，Anthropic 单方面先做第一步——**嵌入式评测方**：给第三方常驻的、等同员工级别的访问权限，用以核查安全实践、报告事故、并在训练过程中评估对齐情况。**Sam Altman 数小时内表示同意**——「我同意 Dario，我们需要 pace the frontier」——Musk 与 Hassabis 也表示支持。安全从业者则对那个僵尸网络设想的可行性提出了质疑。本档案 9 月的多条政策记录一直在引用的，就是这篇文章

## 攻击链

```mermaid
flowchart LR
    E["一起被当作全行业警报的 agent 蜂群事故"]:::entry
    S0["前沿实验室 CEO 提出放慢能力增长，并让第三方评测方常驻内部"]:::step
    I["对手实验室数小时内背书；监管者、立法者与原告方都开始引用这篇文章"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**为什么它该进事故档案。** 这是一篇文章，不是一起事故，因此归为 `policy` 并按规矩排除在事故统计之外。它之所以在这里，是因为它是技术记录与治理记录之间的那个铰链。Amodei 自陈改变立场的理由，正是本档案里的一条具体记录——[OpenAI 的 agent 入侵 Hugging Face](../../../2026-07/2026-07-09-openai-agents-breach-huggingface.md)；而此后 9 月几乎每一条政策记录又都反过来引用这篇文章：[消费者反垄断诉讼](../../../2026-09/2026-09-18-ai-slowdown-antitrust-lawsuit.md)把「Amodei 9 月 12 日的《We Must Pace the Frontier》一文，一小时左右内获 Musk、Altman、Hassabis 背书」列为所谓密约的构成要素；[von der Leyen 的盟情咨文](../../../2026-09/2026-09-16-von-der-leyen-soteu-agents.md)借用了这个说法；[DeepMind Institute 成立](../../../2026-09/2026-09-16-deepmind-institute.md)那条也以它为时间参照。在此之前，档案一直在引用一份自己并不收录的文件。

**真正落到实处的承诺。** 三步之中，只有第一步带着实际承诺：Anthropic 将给第三方评测方**常驻的、等同员工级别的访问权限**——不是限定档期的红队项目，而是一个常设席位，职权包括核查既定安全实践是否被遵守、报告事故，以及在训练**过程中**而非发布时评估对齐情况。真正要盯的是其他实验室会跟进这个承诺，还是只跟进这个姿态；Altman 数小时内背书了原则，OpenAI 随后表示将对等履行第一项承诺。

**有争议的那个论断。** 文章被引用最多的一句，恰恰也是支撑最弱的一句：一个有能力的失准蜂群可能在 6 到 12 个月内以常驻僵尸网络形式控制互联网的相当部分，造成数千亿美元损失。三天后 Axios 走访安全从业者，发现这一设想在可行性上广受怀疑——agent 蜂群在评测沙箱内协同，与在有活跃防御者的环境中维持一个全球僵尸网络，二者之间的差距很大，而文章并未弥合这个差距。Tech Policy Press 则提出了另一种反对意见：由一家私营公司来提议为整个行业定速，本身就是问题所在。两种批评都记在这里，因为本档案的职责是把反驳与主张并排保存，而不是替它们裁判。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Dario Amodei | <https://darioamodei.com/post/we-must-pace-the-frontier> |
| 2 | Dario Amodei（本人公告） | <https://x.com/DarioAmodei/status/2098773920774074715> |
| 3 | Axios（专家反驳） | <https://www.axios.com/2026/09/15/anthropic-dario-ai-agents-safety-botnet> |
| 4 | Forkast | <https://forkast.news/anthropic-ceo-warns-agent-swarms-could-take-over-the-internet-within-12-months/> |
| 5 | Tech Policy Press（批评） | <https://www.techpolicy.press/who-should-pace-the-frontier-not-dario-amodei/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-12`（原文：2026-09-12，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理与监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** —— 一手来源：作者本人网站与本人公告 |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-09-12-amodei-pace-the-frontier` |

<sub>**判定依据：** 围绕前沿 AI 发展速度的厂商政策动作，非事故；`severity` 记为 `info`，不计入事故统计。标记 `landmark`，因为它是 9 月治理主线的参照文件。文中「6 到 12 个月内出现僵尸网络」是一个有争议的预测而非既成事实，故与从业者的反驳并列呈现。分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题：** [防御与治理](../../../../topics/defense.md)

**相关条目：**

- `2026-07-09` [OpenAI 的 agent 入侵 Hugging Face](../../../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>Amodei 自陈改变立场所依据的那起事故</sub>
- `2026-09-18` [消费者起诉 Anthropic、OpenAI、SpaceXAI 与 Google 涉嫌达成 AI 减速密约](../../../2026-09/2026-09-18-ai-slowdown-antitrust-lawsuit.md)<br>  <sub>把这篇文章列为所谓密约的构成要素</sub>
- `2026-09-16` [欧盟盟情咨文：von der Leyen 点名 agent 逃逸并召集前沿实验室](../../../2026-09/2026-09-16-von-der-leyen-soteu-agents.md)<br>  <sub>借用了「pacing the frontier」这个说法</sub>
- `2026-09-19` [Trump 宣布组建「AI Force」与 AI czar，并称安全担忧是骗局](../../../2026-09/2026-09-19-trump-ai-force-czar.md)<br>  <sub>七天后的联邦反向动作</sub>

---

[← 2026-09 索引](../../../2026-09/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-09/2026-09-12-amodei-pace-the-frontier.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
