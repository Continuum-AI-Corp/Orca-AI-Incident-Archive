---
id: 2026-05-22-google-disregard-bug
lang: zh
source: incidents/2026-05/2026-05-22-google-disregard-bug.md
title: "Google AI 搜索「disregard」bug"
summary: |
  搜 "disregard"/"ignore"/"skip" 时 Gemini 把用户输入当成系统指令。虽属功能性缺陷非恶意利用，但暴露了**把 LLM 塞进搜索框而不做指令/数据分离的结构性风险**
---

# Google AI 搜索「disregard」bug

<sub>Google AI Search "disregard" bug</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## 概要

搜 "disregard"/"ignore"/"skip" 时 Gemini 把用户输入当成系统指令。虽属功能性缺陷非恶意利用，但暴露了**把 LLM 塞进搜索框而不做指令/数据分离的结构性风险**

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    I["按攻击者意图越权行动<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | The Verge | <https://www.theverge.com/tech/936176/google-ai-overviews-search-disregard> |
| 2 | MacRumors | <https://www.macrumors.com/2026/05/22/google-search-disregard/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-05-22`（原文：2026-05-22，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-05-22-google-disregard-bug` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-05-04` [Grok / Bankrbot 摩尔斯电码提示注入](../../../2026-05/2026-05-04-grok-bankrbot-mo-er-si.md)<br>  <sub>Grok / Bankrbot Morse-code prompt injection</sub>
- `2026-05-12` [巴西劳动法院首次因提示注入处罚律师](../../../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>
- `2026-05-26` [Microsoft Copilot Cowork 文件外泄](../../../2026-05/2026-05-26-microsoft-copilot-cowork.md)<br>  <sub>Microsoft Copilot Cowork file exfiltration</sub>
- `2026-05-12` [ClaudeBleed：零权限扩展劫持 Claude for Chrome](../../../2026-05/2026-05-12-claudebleed-claude-chrome.md)<br>  <sub>ClaudeBleed: a zero-permission extension hijacks Claude for Chrome</sub>

---

[← English original](../../../2026-05/2026-05-22-google-disregard-bug.md) · [2026-05 index](../../../2026-05/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
