---
id: 2026-03-27-langflow-lu-jing-chuan-yue
lang: zh
source: incidents/2026-03/2026-03-27-langflow-lu-jing-chuan-yue.md
title: "Langflow 路径穿越任意文件写"
summary: |
  Tenable：CVE-2026-5027（CWE-22），`POST /api/v2/files` 不校验 filename。VulnCheck 指出可导致 RCE，且 Langflow **默认开启未认证自动登录**，公网可达实例约 **7,000 个**，已观测到在野利用尝试。v1.9.0 修复
---

# Langflow 路径穿越任意文件写

<sub>Langflow path traversal enables arbitrary file write</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

Tenable：CVE-2026-5027（CWE-22），`POST /api/v2/files` 不校验 filename。VulnCheck 指出可导致 RCE，且 Langflow **默认开启未认证自动登录**，公网可达实例约 **7,000 个**，已观测到在野利用尝试。v1.9.0 修复

## 攻击链

```mermaid
flowchart LR
    E["暴露在公网的 agent 基础设施"]:::entry
    S0["未认证访问"]:::step
    I["RCE / 数据泄露<br/><i>（漏洞已披露 · 未见在野利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Tenable | <https://www.tenable.com/security/research/tra-2026-26> |
| 2 | SecurityWeek | <https://www.securityweek.com/hackers-exploit-langflow-vulnerability-for-remote-code-execution/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-03-27`（原文：2026-03-27，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-03-27-langflow-lu-jing-chuan-yue` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-03-09` [麦肯锡 Lilli 事件公开](../../../2026-03/2026-03-09-lilli-mai-ken-xi-shi.md)<br>  <sub>McKinsey Lilli incident goes public</sub>
- `2026-02-28` [CodeWall 攻破麦肯锡 "Lilli" 内部 AI 平台](../../../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>
- `2026-04-16` [MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打](../../../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-02-10` [15,200 个 OpenClaw 控制面板裸奔](../../../2026-02/2026-02-10-openclaw-kong-zhi-mian-ban.md)<br>  <sub>15,200 OpenClaw control panels exposed</sub>

---

[← English original](../../../2026-03/2026-03-27-langflow-lu-jing-chuan-yue.md) · [2026-03 index](../../../2026-03/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
