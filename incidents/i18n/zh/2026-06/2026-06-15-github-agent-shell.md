---
id: 2026-06-15-github-agent-shell
lang: zh
source: incidents/2026-06/2026-06-15-github-agent-shell.md
title: "无害外观的 GitHub 仓库让 agent 执行反弹 shell"
summary: |
  Mozilla 0DIN 三段式：README 写常规 `python3 -m axiom init` → Python 包**故意报错**诱导执行初始化 → `setup.sh` 用 `dig +short TXT _axiom-config` 取 DNS TXT 记录内容喂给 `bash -c`。**Claude Code 会执行一个它自己从未审阅过的东西**（可信的错误信息 + 外取值的脚本 + 看不见的 DNS 记录，三段迂回）。检证环境实证，无在野报告
---

# 无害外观的 GitHub 仓库让 agent 执行反弹 shell

<sub>Innocuous-looking GitHub repos make agents open a reverse shell</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## 概要

Mozilla 0DIN 三段式：README 写常规 `python3 -m axiom init` → Python 包**故意报错**诱导执行初始化 → `setup.sh` 用 `dig +short TXT _axiom-config` 取 DNS TXT 记录内容喂给 `bash -c`。**Claude Code 会执行一个它自己从未审阅过的东西**（可信的错误信息 + 外取值的脚本 + 看不见的 DNS 记录，三段迂回）。检证环境实证，无在野报告

## 攻击链

```mermaid
flowchart LR
    E["被投毒的包 / 仓库 / agent 配置"]:::entry
    S0["开发者或 agent 自动安装"]:::step
    I["凭据窃取与自我传播<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | 0DIN | <https://0din.ai/blog/clone-this-repo-and-i-own-your-machine> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-15`（原文：2026-06-15，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`SUPPLY`](../../../../taxonomy/types.md#supply) 供应链投毒 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-15-github-agent-shell` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 供应链投毒](../../../../topics/agent-supply-chain.md)

**同类条目**：

- `2026-06-01` [Miasma 蠕虫](../../../2026-06/2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-17` [Sapphire Sleet 88 分钟投毒 Mastra AI 全 scope](../../../2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-18` [ClickFix 恶意广告滥用 claude.ai 分享对话](../../../2026-06/2026-06-18-clickfix-claude-ai-e-yi-guang.md)<br>  <sub>ClickFix malvertising abuses claude.ai shared conversations</sub>
- `2026-05-19` [TrapDoor：跨三个生态投毒，专门污染 AI 助手配置](../../../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>

---

[← English original](../../../2026-06/2026-06-15-github-agent-shell.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
