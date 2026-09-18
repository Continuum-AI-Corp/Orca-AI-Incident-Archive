---
id: 2025-02-01-ollama-fu-wu-qi-gui
lang: zh
source: incidents/2025-02/2025-02-01-ollama-fu-wu-qi-gui.md
title: "Ollama 服务器大规模裸奔"
summary: |
  奇安信鹰图：全球 **8,971** 台 Ollama 服务器中 **6,449 台活跃**，其中 **88.9% 无有效安全防护**；8,971 台中 **5,669 台在中国**。默认无身份验证（11434 端口），可窃取模型、投喂虚假信息、盗用推理资源，甚至删除已部署的 DeepSeek/Qwen 模型文件。CNVD-2025-04094
---

# Ollama 服务器大规模裸奔

<sub>Thousands of Ollama servers exposed without auth</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

> [!WARNING]
> **本条存在争议或未完全证实的事实**，正文中的各方说法并列保留，请勿单独引用其中一方。

## 概要

奇安信鹰图：全球 **8,971** 台 Ollama 服务器中 **6,449 台活跃**，其中 **88.9% 无有效安全防护**；8,971 台中 **5,669 台在中国**。默认无身份验证（11434 端口），可窃取模型、投喂虚假信息、盗用推理资源，甚至删除已部署的 DeepSeek/Qwen 模型文件。CNVD-2025-04094

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
| 1 | 奇安信 | <https://www.qianxin.com/news/detail?news_id=13062> |
| 2 | CNCERT 公告 | <https://www.secrss.com/articles/76168> |
| 3 | 绿盟 | <https://blog.nsfocus.net/cnvd-2025-04094/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-02-01`（原文：2025-02，精度 `month`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) · [全球](../../../../regions/global.md) |
| 档案编号 | `2025-02-01-ollama-fu-wu-qi-gui` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2025-01-29` [DeepSeek ClickHouse 数据库裸奔](../../../2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br>  <sub>DeepSeek ClickHouse database left wide open</sub>
- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 在野利用](../../../2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-03-03` [DeepSeek 暴露窗口关闭](../../../2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM 反序列化 RCE](../../../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>

---

[← English original](../../../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md) · [2025-02 index](../../../2025-02/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
