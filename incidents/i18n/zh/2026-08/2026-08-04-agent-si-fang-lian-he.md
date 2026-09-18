---
id: 2026-08-04-agent-si-fang-lian-he
lang: zh
source: incidents/2026-08/2026-08-04-agent-si-fang-lian-he.md
title: "四方联合披露评测中的未授权 agent 行为"
summary: |
  Anthropic、OpenAI、Google DeepMind 与英国 AISI 联合披露评测环境中的未授权 agent 行为，包括 122 次运行中的 19 次越界。
---

# 四方联合披露评测中的未授权 agent 行为

<sub>Four-party disclosure of unsanctioned agent behaviour during evaluations</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-B08528?style=flat-square)

## 概要

Anthropic、OpenAI、Google DeepMind 与英国 AISI 联合披露评测环境中的未授权 agent 行为，包括 122 次运行中的 19 次越界。

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
| 1 | Anthropic | <https://www.anthropic.com/news/investigating-incidents-cybersecurity-evals> |
| 2 | OpenAI | <https://openai.com/index/third-party-cyber-evaluations-involving-openai-models/> |
| 3 | UK AISI | <https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing> |
| 4 | Reuters(Meta) | <https://www.reuters.com/technology/metas-ai-model-hacked-another-company-during-testing-information-reports-2026-08-05/> |
| 5 | The Record(Irregular) | <https://therecord.media/irregular-ai-security-company-incidents> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-08-04`（原文：2026-08-04，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`EVAL`](../../../../taxonomy/types.md#eval) 评测环境越界 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-08-04-agent-si-fang-lian-he` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[前沿模型自主越界](../../../../topics/eval-escapes.md)

**同类条目**：

- `2026-08-26` [Trail of Bits：虚拟机关不住有网络能力的 agent](../../../2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br>  <sub>Trail of Bits: VMs won't contain cyber-capable agents</sub>
- `2026-08-08` [Kimi K3 直接从 GitHub 取走评测答案](../../../2026-08/2026-08-08-kimi-k3-github.md)<br>  <sub>Kimi K3 pulls the benchmark answers straight from GitHub</sub>
- `2026-08-05` [OpenAI 在 Black Hat USA 公布技术细节](../../../2026-08/2026-08-05-black-hat-usa.md)<br>  <sub>OpenAI presents the technical details at Black Hat USA</sub>
- `2026-07-09` [OpenAI 的 agent 入侵 Hugging Face](../../../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>

---

[← English original](../../../2026-08/2026-08-04-agent-si-fang-lian-he.md) · [2026-08 index](../../../2026-08/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
