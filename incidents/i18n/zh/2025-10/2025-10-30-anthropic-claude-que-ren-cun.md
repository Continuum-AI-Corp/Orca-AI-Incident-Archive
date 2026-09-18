---
id: 2025-10-30-anthropic-claude-que-ren-cun
lang: zh
source: incidents/2025-10/2025-10-30-anthropic-claude-que-ren-cun.md
title: "Anthropic 确认 Claude 存在提示注入缺陷"
summary: |
  ⚠️ **本条是为 2026-01 Cowork 事件建立时间锚点**：该缺陷在 **Cowork 发布（2026-01-12）前三个月**就已被报告并获 Anthropic 确认，**发布时仍未修复**，随后被评为 **CVSS 10/10**。Anthropic 的书面立场是它「落在当前威胁模型之外」—— 与 2026-07 GhostApproval 事件中的回应用词一致
---

# Anthropic 确认 Claude 存在提示注入缺陷

<sub>Anthropic confirms a prompt-injection flaw in Claude</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## 概要

⚠️ **本条是为 2026-01 Cowork 事件建立时间锚点**：该缺陷在 **Cowork 发布（2026-01-12）前三个月**就已被报告并获 Anthropic 确认，**发布时仍未修复**，随后被评为 **CVSS 10/10**。Anthropic 的书面立场是它「落在当前威胁模型之外」—— 与 2026-07 GhostApproval 事件中的回应用词一致

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    I["按攻击者意图越权行动<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | GovInfoSecurity | <https://www.govinfosecurity.com/anthropics-cowork-shipped-known-vulnerability-a-30553> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-10-30`（原文：2025-10-30，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-10-30-anthropic-claude-que-ren-cun` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2025-10-02` [CometJacking](../../../2025-10/2025-10-02-cometjacking.md)<br>  <sub>CometJacking</sub>
- `2025-10-08` [CamoLeak（GitHub Copilot Chat）](../../../2025-10/2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>CamoLeak (GitHub Copilot Chat)</sub>
- `2025-10-31` [Agent Session Smuggling：A2A 协议上的 agent 互骗](../../../2025-10/2025-10-31-agent-session-smuggling-a2a.md)<br>  <sub>Agent Session Smuggling: agents deceiving agents over A2A</sub>
- `2025-10-21` [Brave 披露 Comet 截图型注入](../../../2025-10/2025-10-21-brave-comet-pi-lu-jie.md)<br>  <sub>Brave discloses screenshot-based injection in Comet</sub>

---

[← English original](../../../2025-10/2025-10-30-anthropic-claude-que-ren-cun.md) · [2025-10 index](../../../2025-10/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
