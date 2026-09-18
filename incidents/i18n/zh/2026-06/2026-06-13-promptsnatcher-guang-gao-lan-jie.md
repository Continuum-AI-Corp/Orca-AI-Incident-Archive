---
id: 2026-06-13-promptsnatcher-guang-gao-lan-jie
lang: zh
source: incidents/2026-06/2026-06-13-promptsnatcher-guang-gao-lan-jie.md
title: "PromptSnatcher：广告拦截扩展偷 AI 对话"
summary: |
  Smart Adblocker(约 8 万) + Adblock for Browser(约 1 万)，共享同一外带逻辑与 C2。注入 MAIN world 脚本替换 fetch/XHR/WebSocket，复制 **ChatGPT、Claude、Gemini、Copilot 等 8 个 AI 服务的完整对话**（其中 5 个还判定套餐等级）。**解析规则从 C2 运行时下发，无需更新商店版本即可扩大目标**；Firefox 版声明「不收集数据」却装了同款捕获引擎
---

# PromptSnatcher：广告拦截扩展偷 AI 对话

<sub>PromptSnatcher: ad-blocking extensions steal AI conversations</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

Smart Adblocker(约 8 万) + Adblock for Browser(约 1 万)，共享同一外带逻辑与 C2。注入 MAIN world 脚本替换 fetch/XHR/WebSocket，复制 **ChatGPT、Claude、Gemini、Copilot 等 8 个 AI 服务的完整对话**（其中 5 个还判定套餐等级）。**解析规则从 C2 运行时下发，无需更新商店版本即可扩大目标**；Firefox 版声明「不收集数据」却装了同款捕获引擎

## 攻击链

```mermaid
flowchart LR
    E["放在 agent 够得着的位置的凭据"]:::entry
    S0["agent 取用并调用"]:::step
    I["凭据被滥用"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | MalExt Sentry | <https://malext.io/reports/PromptSnatcher/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-13`（原文：2026-06-13，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-13-promptsnatcher-guang-gao-lan-jie` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**同类条目**：

- `2026-06-01` [Miasma 蠕虫](../../../2026-06/2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [黑客直接「请求」Meta AI 客服机器人交出 Instagram 账号](../../../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet 88 分钟投毒 Mastra AI 全 scope](../../../2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p 被非法分发](../../../2026-06/2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>

---

[← English original](../../../2026-06/2026-06-13-promptsnatcher-guang-gao-lan-jie.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
