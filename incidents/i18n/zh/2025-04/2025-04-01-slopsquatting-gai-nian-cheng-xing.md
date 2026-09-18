---
id: 2025-04-01-slopsquatting-gai-nian-cheng-xing
lang: zh
source: incidents/2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md
title: "\"Slopsquatting\" 概念成型"
summary: |
  术语由 Python 软件基金会驻场开发者 **Seth Larson** 提出：把 typosquatting 里的「人类打字错误」换成「AI 幻觉」—— 模型自信地推荐一个从不存在的包名，攻击者抢先注册。规模由 USENIX Security 2025 论文《We Have a Package for You!》量化：16 个代码模型生成 223 万个样本，**19.7% 的推荐包根本不存在**（20.5 万个不同的幻觉包名），开源模型幻觉率均值 **21.7%**、商用 **5.2%**；**58% 的幻觉包在 10 次运行中重复出现** —— 即可预测、可抢注
---

# "Slopsquatting" 概念成型

<sub>"Slopsquatting" gets its name</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## 概要

术语由 Python 软件基金会驻场开发者 **Seth Larson** 提出：把 typosquatting 里的「人类打字错误」换成「AI 幻觉」—— 模型自信地推荐一个从不存在的包名，攻击者抢先注册。规模由 USENIX Security 2025 论文《We Have a Package for You!》量化：16 个代码模型生成 223 万个样本，**19.7% 的推荐包根本不存在**（20.5 万个不同的幻觉包名），开源模型幻觉率均值 **21.7%**、商用 **5.2%**；**58% 的幻觉包在 10 次运行中重复出现** —— 即可预测、可抢注

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
| 1 | Wikipedia | <https://en.wikipedia.org/wiki/Slopsquatting> |
| 2 | Socket | <https://socket.dev/blog/slopsquatting-how-ai-hallucinations-are-fueling-a-new-class-of-supply-chain-attacks> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-04-01`（原文：2025-04，精度 `month`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-04-01-slopsquatting-gai-nian-cheng-xing` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2025-03-18` [Cursor / Copilot「Rules File Backdoor」](../../../2025-03/2025-03-18-cursor-copilot-rules-file.md)<br>  <sub>Cursor / Copilot "Rules File Backdoor"</sub>
- `2025-02-06` [Hugging Face "nullifAI" 恶意模型](../../../2025-02/2025-02-06-hugging-face-nullifai.md)<br>  <sub>Hugging Face "nullifAI" malicious models</sub>
- `2025-07-13` [Amazon Q Developer 扩展被投毒](../../../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-08-08` [Salesloft Drift OAuth 令牌窃取](../../../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← English original](../../../2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md) · [2025-04 index](../../../2025-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
