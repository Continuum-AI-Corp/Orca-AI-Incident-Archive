---
id: 2024-12-01-storm-azure-llmjacking
lang: zh
source: incidents/2024-12/2024-12-01-storm-azure-llmjacking.md
title: "Storm-2139 Azure OpenAI LLMjacking"
summary: |
  微软 DCU 2024-12 在弗吉尼亚东区起诉 10 名「John Doe」；盗取凭据接管 Azure OpenAI，用越狱技术绕过安全防护并**转售服务**。2025-02-27 公开被告身份
---

# Storm-2139 Azure OpenAI LLMjacking

<sub>Storm-2139 Azure OpenAI LLMjacking</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## 概要

微软 DCU 2024-12 在弗吉尼亚东区起诉 10 名「John Doe」；盗取凭据接管 Azure OpenAI，用越狱技术绕过安全防护并**转售服务**。2025-02-27 公开被告身份

## 攻击链

```mermaid
flowchart LR
    E["放在 agent 够得着的位置的凭据"]:::entry
    S0["agent 取用并调用"]:::step
    I["凭据被滥用"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Microsoft | <https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2024-12-01` → `2025-02-01`（原文：2024-12→2025-02，精度 `month`） |
| 性质 | 真实事故 `incident` |
| 类型 | [`CRED`](../../../../taxonomy/types.md#cred) 凭据滥用 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 是 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2024-12-01-storm-azure-llmjacking` |

<sub>**判定依据**：真实事故，有确认的受害方。 判 `high`：真实损害范围有限，或属 CVSS 9+ 的严重缺陷，或是有重要意义的能力实证。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**同类条目**：

- `2025-06-30` [McDonald's McHire「Olivia」招聘机器人](../../../2025-06/2025-06-30-mcdonald-mchire-olivia.md)<br>  <sub>McDonald's McHire "Olivia" hiring bot</sub>
- `2025-06-13` [Smithery.ai 路径穿越](../../../2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md)<br>  <sub>Smithery.ai path traversal</sub>
- `2025-07-01` [RoguePilot](../../../2025-07/2025-07-01-roguepilot.md)<br>  <sub>RoguePilot</sub>
- `2025-07-09` [McHire 漏洞公开](../../../2025-07/2025-07-09-mchire-lou-dong-gong-kai.md)<br>  <sub>McHire flaw goes public</sub>

---

[← English original](../../../2024-12/2024-12-01-storm-azure-llmjacking.md) · [2024-12 index](../../../2024-12/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
