---
id: 2026-04-06-openclaw-chan-chu-su-lv
lang: zh
source: incidents/2026-04/2026-04-06-openclaw-chan-chu-su-lv.md
title: "OpenClaw 的 CVE 产出速率：每天 2.2 个"
summary: |
  截至 2026-04-06，OpenClaw 累计 **138 个 CVE**，全部集中在一个 **63 天**的窗口内 —— 约 **2.2 个/天**，其中 **7 个 critical、49 个 high**。最严重的 **CVE-2026-22172** 与 **CVE-2026-32922** 均为 **CVSS 9.9**（分别为无凭据取得管理控制、权限提升）。另：**2026-01-25 的首次正式审计就发现 512 个漏洞，其中 8 个 critical**
  💡 这个速率本身就是一条数据：**一个在两个月内爆出 138 个 CVE 的组件，正被当作个人 AI 助理装在开发机上**
---

# OpenClaw 的 CVE 产出速率：每天 2.2 个

<sub>OpenClaw's CVE rate: 2.2 per day</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

截至 2026-04-06，OpenClaw 累计 **138 个 CVE**，全部集中在一个 **63 天**的窗口内 —— 约 **2.2 个/天**，其中 **7 个 critical、49 个 high**。最严重的 **CVE-2026-22172** 与 **CVE-2026-32922** 均为 **CVSS 9.9**（分别为无凭据取得管理控制、权限提升）。另：**2026-01-25 的首次正式审计就发现 512 个漏洞，其中 8 个 critical**

💡 这个速率本身就是一条数据：**一个在两个月内爆出 138 个 CVE 的组件，正被当作个人 AI 助理装在开发机上**

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
| 1 | CVE 汇总 | <https://www.betterclaw.io/blog/openclaw-security-2026> |
| 2 | ARMO(CVE-2026-32922) | <https://www.armosec.io/blog/cve-2026-32922-openclaw-privilege-escalation-cloud-security/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-04-06`（原文：2026-04-06，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **信息** `info` |
| 可信度 | **B** — 研究机构或主流媒体，有可核查细节 |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-04-06-openclaw-chan-chu-su-lv` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-04-16` [MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打](../../../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 在野利用](../../../2026-04/2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-23` [OpenClaw「Claw Chain」四漏洞链，24.5 万台服务器暴露](../../../2026-04/2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-01` [Google Vertex AI「Double Agent」权限滥用](../../../2026-04/2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>

---

[← English original](../../../2026-04/2026-04-06-openclaw-chan-chu-su-lv.md) · [2026-04 index](../../../2026-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
