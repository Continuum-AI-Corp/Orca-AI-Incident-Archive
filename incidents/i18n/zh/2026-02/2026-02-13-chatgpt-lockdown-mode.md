---
id: 2026-02-13-chatgpt-lockdown-mode
lang: zh
source: incidents/2026-02/2026-02-13-chatgpt-lockdown-mode.md
title: "ChatGPT 推出 Lockdown Mode"
summary: |
  限制外发网络请求，关闭 Deep Research / agent 模式；同时给高风险功能统一贴「elevated risk」标签
---

# ChatGPT 推出 Lockdown Mode

<sub>ChatGPT introduces Lockdown Mode</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

限制外发网络请求，关闭 Deep Research / agent 模式；同时给高风险功能统一贴「elevated risk」标签

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
| 1 | OpenAI | <https://openai.com/ja-JP/index/introducing-lockdown-mode-and-elevated-risk-labels-in-chatgpt/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-02-13`（原文：2026-02-13，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-02-13-chatgpt-lockdown-mode` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-02-05` [GPT-5.3-Codex 被评为网络安全 "High"](../../../2026-02/2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-05` [Claude Opus 4.6 在开源项目中发现 500+ 零日](../../../2026-02/2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-18` [Anthropic《Measuring AI agent autonomy in practice》](../../../2026-02/2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>
- `2026-02-19` [微软：不要在普通办公机上运行 OpenClaw](../../../2026-02/2026-02-19-openclaw-wei-ruan-pu-tong.md)<br>  <sub>Microsoft: don't run OpenClaw on ordinary work machines</sub>

---

[← English original](../../../2026-02/2026-02-13-chatgpt-lockdown-mode.md) · [2026-02 index](../../../2026-02/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
