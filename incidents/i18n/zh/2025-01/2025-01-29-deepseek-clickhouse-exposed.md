---
id: 2025-01-29-deepseek-clickhouse-exposed
lang: zh
source: incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md
title: "DeepSeek ClickHouse 数据库裸奔"
summary: |
  Wiz 发现无认证公网 ClickHouse（`oauth2callback.deepseek.com:9000`、`dev.deepseek.com:9000`），经 `/play` 路径可直接跑任意 SQL。`log_stream` 表 **100 万+ 条日志**（最早 2025-01-06），含明文聊天记录、API 密钥、后端细节。DeepSeek 接报后迅速关闭
---

# DeepSeek ClickHouse 数据库裸奔

<sub>DeepSeek ClickHouse database left wide open</sub>

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

Wiz 发现无认证公网 ClickHouse（`oauth2callback.deepseek.com:9000`、`dev.deepseek.com:9000`），经 `/play` 路径可直接跑任意 SQL。`log_stream` 表 **100 万+ 条日志**（最早 2025-01-06），含明文聊天记录、API 密钥、后端细节。DeepSeek 接报后迅速关闭

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
| 1 | Wiz | <https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak> |
| 2 | THN | <https://thehackernews.com/2025/01/deepseek-ai-database-exposed-over-1.html> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-01-29`（原文：2025-01-29，精度 `day`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **严重** `critical` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) |
| 档案编号 | `2025-01-29-deepseek-clickhouse-exposed` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `critical`：确认的真实损害达到多组织 / 政府 / 关键基础设施 / 供应链蠕虫级别，或属首次出现且有真实受害方的能力里程碑。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2025-02-01` [Ollama 服务器大规模裸奔](../../../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>Thousands of Ollama servers exposed without auth</sub>
- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 在野利用](../../../2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-03-03` [DeepSeek 暴露窗口关闭](../../../2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-04-29` [NVIDIA TensorRT-LLM 反序列化 RCE](../../../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md)<br>  <sub>NVIDIA TensorRT-LLM deserialization RCE</sub>

---

[← English original](../../../2025-01/2025-01-29-deepseek-clickhouse-exposed.md) · [2025-01 index](../../../2025-01/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
