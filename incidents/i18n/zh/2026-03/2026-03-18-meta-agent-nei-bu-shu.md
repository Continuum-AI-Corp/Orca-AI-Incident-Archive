---
id: 2026-03-18-meta-agent-nei-bu-shu
lang: zh
source: incidents/2026-03/2026-03-18-meta-agent-nei-bu-shu.md
title: "Meta 内部 AI agent 数据暴露"
summary: |
  agent 给出不安全的配置建议，导致敏感用户与公司数据内部暴露约 2 小时
---

# Meta 内部 AI agent 数据暴露

<sub>Meta internal AI agent data exposure</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## 概要

agent 给出不安全的配置建议，导致敏感用户与公司数据内部暴露约 2 小时

## 攻击链

```mermaid
flowchart LR
    E["用户交付的普通任务"]:::entry
    S0["agent 误判现状并自行升级动作"]:::step
    I["破坏性命令被执行"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | OWASP Q1'26 | <https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-03-18`（原文：2026-03-18，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`ROGUE`](../../../../taxonomy/types.md#rogue) agent 自主破坏 |
| 严重度 | **高** `high` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [美国](../../../../regions/us.md) |
| 档案编号 | `2026-03-18-meta-agent-nei-bu-shu` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[编码 agent 自主破坏](../../../../topics/rogue-agents.md)

**同类条目**：

- `2026-03-02` [⚠️ Amazon 因 AI 生成代码连续宕机](../../../2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md)<br>  <sub>Amazon hit by back-to-back outages from AI-generated code</sub>
- `2026-02-26` [Claude Code 用 terraform destroy 抹掉 DataTalks.Club 全部生产基础设施](../../../2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br>  <sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub>
- `2026-04-25` [Cursor + Claude Opus 4.6 九秒删光生产库与备份](../../../2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br>  <sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub>
- `2026-02-18` [Microsoft 365 Copilot 越权总结机密邮件](../../../2026-02/2026-02-18-microsoft-copilot-yue-quan-zong.md)<br>  <sub>Microsoft 365 Copilot summarises confidential mail it shouldn't see</sub>

---

[← English original](../../../2026-03/2026-03-18-meta-agent-nei-bu-shu.md) · [2026-03 index](../../../2026-03/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
