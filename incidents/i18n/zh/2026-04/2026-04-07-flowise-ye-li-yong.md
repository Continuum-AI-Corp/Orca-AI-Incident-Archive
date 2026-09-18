---
id: 2026-04-07-flowise-ye-li-yong
lang: zh
source: incidents/2026-04/2026-04-07-flowise-ye-li-yong.md
title: "Flowise CVE-2025-59528 在野利用"
summary: |
  1.2 万–1.5 万个暴露实例
---

# Flowise CVE-2025-59528 在野利用

<sub>Flowise CVE-2025-59528 exploited in the wild</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

1.2 万–1.5 万个暴露实例

## 攻击链

```mermaid
flowchart LR
    E["暴露在公网的 agent 基础设施"]:::entry
    S0["未认证访问"]:::step
    I["RCE / 数据泄露"]:::impact
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
| 日期 | `2026-04-07`（原文：2026-04-07，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-04-07-flowise-ye-li-yong` |

<sub>**判定依据**：漏洞披露，已确认在野利用，故 `real_harm: true`。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-04-16` [MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打](../../../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-23` [OpenClaw「Claw Chain」四漏洞链，24.5 万台服务器暴露](../../../2026-04/2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-01` [Google Vertex AI「Double Agent」权限滥用](../../../2026-04/2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>
- `2026-04-06` [OpenClaw 的 CVE 产出速率：每天 2.2 个](../../../2026-04/2026-04-06-openclaw-chan-chu-su-lv.md)<br>  <sub>OpenClaw's CVE rate: 2.2 per day</sub>

---

[← English original](../../../2026-04/2026-04-07-flowise-ye-li-yong.md) · [2026-04 index](../../../2026-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
