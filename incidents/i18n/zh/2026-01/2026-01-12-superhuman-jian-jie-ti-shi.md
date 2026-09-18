---
id: 2026-01-12-superhuman-jian-jie-ti-shi
lang: zh
source: incidents/2026-01/2026-01-12-superhuman-jian-jie-ti-shi.md
title: "Superhuman AI 间接提示注入"
summary: |
  PromptArmor：零交互外带收件箱数据，经 **Google 表单预填链接** + Markdown 图片自动渲染绕过 CSP。Superhuman 安全团队快速修复（含 Superhuman Go）
---

# Superhuman AI 间接提示注入

<sub>Superhuman AI indirect prompt injection</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

PromptArmor：零交互外带收件箱数据，经 **Google 表单预填链接** + Markdown 图片自动渲染绕过 CSP。Superhuman 安全团队快速修复（含 Superhuman Go）

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | PromptArmor | <https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-01-12`（原文：2026-01-12，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-01-12-superhuman-jian-jie-ti-shi` |

<sub>**判定依据**：真实事故，未见确认的具体受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-01-12` [Claude Cowork 带着已知漏洞发布](../../../2026-01/2026-01-12-claude-cowork-dai-zhe-zhi.md)<br>  <sub>Claude Cowork ships with known vulnerabilities</sub>
- `2026-01-14` [Microsoft Copilot Personal「Reprompt」](../../../2026-01/2026-01-14-microsoft-copilot-personal-reprompt.md)<br>  <sub>Microsoft Copilot Personal "Reprompt"</sub>
- `2026-01-07` [九天内四款生产力工具「致命三元组」集中披露](../../../2026-01/2026-01-07-lethal-trifecta-four-tools.md)<br>  <sub>Four productivity tools hit the lethal trifecta in nine days</sub>
- `2026-02-09` [Clinejection](../../../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← English original](../../../2026-01/2026-01-12-superhuman-jian-jie-ti-shi.md) · [2026-01 index](../../../2026-01/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
