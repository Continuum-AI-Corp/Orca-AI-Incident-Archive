---
id: 2025-04-29-nvidia-tensorrt-llm-rce
lang: zh
source: incidents/2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md
title: "NVIDIA TensorRT-LLM 反序列化 RCE"
summary: |
  CVE-2025-23254，CVSS 8.8，Python executor 的 pickle IPC
---

# NVIDIA TensorRT-LLM 反序列化 RCE

<sub>NVIDIA TensorRT-LLM deserialization RCE</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

CVE-2025-23254，CVSS 8.8，Python executor 的 pickle IPC

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
| 1 | OWASP Q2'25 | <https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2025-04-29`（原文：2025-04-29，精度 `day`） |
| 性质 | 漏洞披露 `vulnerability` |
| 类型 | [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2025-04-29-nvidia-tensorrt-llm-rce` |

<sub>**判定依据**：漏洞披露，截至归档未见在野利用证据，故 `real_harm: false`。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[agent 基础设施暴露](../../../../topics/agent-infra.md)

**同类条目**：

- `2025-03-01` [ChatGPT SSRF CVE-2024-27564 在野利用](../../../2025-03/2025-03-01-chatgpt-ssrf-ye-li-yong.md)<br>  <sub>ChatGPT SSRF CVE-2024-27564 exploited in the wild</sub>
- `2025-03-03` [DeepSeek 暴露窗口关闭](../../../2025-03/2025-03-03-deepseek-bao-lu-chuang-kou.md)<br>  <sub>DeepSeek exposure window closes</sub>
- `2025-02-01` [Ollama 服务器大规模裸奔](../../../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>Thousands of Ollama servers exposed without auth</sub>
- `2025-01-29` [DeepSeek ClickHouse 数据库裸奔](../../../2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br>  <sub>DeepSeek ClickHouse database left wide open</sub>

---

[← English original](../../../2025-04/2025-04-29-nvidia-tensorrt-llm-rce.md) · [2025-04 index](../../../2025-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
