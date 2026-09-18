---
id: 2026-07-27-jfrog-artifactory-fa-bu-jiu
lang: zh
source: incidents/2026-07/2026-07-27-jfrog-artifactory-fa-bu-jiu.md
title: "JFrog 发布 Artifactory 九个 CVE 补丁"
summary: |
  与 OpenAI 逃逸事件相关；公开的是 CVE-2026-65617（High），**评测中实际用到的是哪个零日，JFrog 与 OpenAI 均未说明**
---

# JFrog 发布 Artifactory 九个 CVE 补丁

<sub>JFrog patches nine Artifactory CVEs</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

与 OpenAI 逃逸事件相关；公开的是 CVE-2026-65617（High），**评测中实际用到的是哪个零日，JFrog 与 OpenAI 均未说明**

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
| 1 | JFrog | <https://jfrog.com/blog/jfrog-and-openai-collaboration-on-zero-day-security-findings/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-27`（原文：2026-07-27，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-27-jfrog-artifactory-fa-bu-jiu` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-07-30` [RufRoot（CVE-2026-59726）：CVSS 满分，可召唤流氓 AI 蜂群](../../../2026-07/2026-07-30-rufroot-man-fen-zhao-huan.md)<br>  <sub>RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm</sub>
- `2026-08-06` [Langflow 未认证 RCE 进 CISA KEV](../../../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-06-08` [LiteLLM CVE-2026-42271 MCP 端点接管](../../../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap：4 个漏洞让 100 万+ AI 应用被跨租户窃听](../../../2026-06/2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>

---

[← English original](../../../2026-07/2026-07-27-jfrog-artifactory-fa-bu-jiu.md) · [2026-07 index](../../../2026-07/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
