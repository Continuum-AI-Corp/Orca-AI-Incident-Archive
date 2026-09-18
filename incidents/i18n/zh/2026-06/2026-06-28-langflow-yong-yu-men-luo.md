---
id: 2026-06-28-langflow-yong-yu-men-luo
lang: zh
source: incidents/2026-06/2026-06-28-langflow-yong-yu-men-luo.md
title: "Langflow CVE-2026-33017 被用于门罗币挖矿"
summary: |
  Trend Micro：未认证 RCE → `isp.sh` → Go 语言 `lambsys`（置于 `/var/tmp/.xlamb`），**遍历私钥、known_hosts、ssh-agent 密钥蠕虫式扩散**，停掉竞争矿工，禁用 AppArmor/SELinux/防火墙/阿里云监控代理，cron + 常驻脚本持久化，部署改版 XMRig。**单个 IoC 追踪到 19 天的持续利用**
---

# Langflow CVE-2026-33017 被用于门罗币挖矿

<sub>Langflow CVE-2026-33017 used for Monero mining</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

Trend Micro：未认证 RCE → `isp.sh` → Go 语言 `lambsys`（置于 `/var/tmp/.xlamb`），**遍历私钥、known_hosts、ssh-agent 密钥蠕虫式扩散**，停掉竞争矿工，禁用 AppArmor/SELinux/防火墙/阿里云监控代理，cron + 常驻脚本持久化，部署改版 XMRig。**单个 IoC 追踪到 19 天的持续利用**

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
| 1 | Trend Micro | <https://www.trendmicro.com/en_us/research/26/f/from-langflow-to-monero-inside-cve-2026-33017-cryptominer.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-28`（原文：2026-06-28，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-28-langflow-yong-yu-men-luo` |

<sub>**判定依据**：漏洞披露，已确认在野利用，故 `real_harm: true`。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP 端点接管](../../../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>LiteLLM CVE-2026-42271 MCP endpoint takeover</sub>
- `2026-06-29` [DifyTap：4 个漏洞让 100 万+ AI 应用被跨租户窃听](../../../2026-06/2026-06-29-difytap-lou-dong-rang-wan.md)<br>  <sub>DifyTap: four flaws leave 1M+ AI apps open to cross-tenant eavesdropping</sub>
- `2026-06-17` [Vertex AI SDK 存储桶抢占 → 跨租户 RCE](../../../2026-06/2026-06-17-vertex-sdk-rce.md)<br>  <sub>Vertex AI SDK bucket takeover leads to cross-tenant RCE</sub>
- `2026-06-18` [AutoJack：AutoGen Studio 一个网页打穿宿主](../../../2026-06/2026-06-18-autojack-autogen-studio.md)<br>  <sub>AutoJack: one web page from AutoGen Studio to the host</sub>

---

[← English original](../../../2026-06/2026-06-28-langflow-yong-yu-men-luo.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
