---
id: 2026-04-30-tui-chu-gao-ji-zhang
lang: zh
source: incidents/2026-04/2026-04-30-tui-chu-gao-ji-zhang.md
title: "OpenAI 推出「高级账户安全」"
summary: |
  强制 passkey/FIDO 硬件密钥、取消邮件/短信找回、缩短会话、会话可视化；**启用后自动排除模型训练**。与 Yubico 合作
---

# OpenAI 推出「高级账户安全」

<sub>OpenAI launches Advanced Account Security</sub>

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## 概要

强制 passkey/FIDO 硬件密钥、取消邮件/短信找回、缩短会话、会话可视化；**启用后自动排除模型训练**。与 Yubico 合作

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
| 1 | OpenAI | <https://openai.com/ja-JP/index/advanced-account-security/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-04-30`（原文：2026-04-30，精度 `day`） |
| 性质 | 政策 / 监管 `policy` |
| 类型 | [`GOV`](../../../../taxonomy/types.md#gov) 治理 / 监管 |
| 严重度 | **信息** `info` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 不适用 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-04-30-tui-chu-gao-ji-zhang` |

<sub>**判定依据**：政策 / 监管动作，不计入事故统计，`severity` 记为 `info`。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[防御与治理](../../../../topics/defense.md)

**同类条目**：

- `2026-04-07` [Claude Mythos Preview 网络能力披露 + Project Glasswing 成立](../../../2026-04/2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>
- `2026-04-13` [UK AISI 独立评估 Claude Mythos Preview](../../../2026-04/2026-04-13-uk-aisi-claude-mythos.md)<br>  <sub>UK AISI independently evaluates Claude Mythos Preview</sub>
- `2026-04-14` [Vidoc：用公开模型复现了 Mythos 的发现](../../../2026-04/2026-04-14-vidoc-mythos-yong-gong-kai.md)<br>  <sub>Vidoc reproduces Mythos's findings with public models</sub>
- `2026-05-12` [巴西劳动法院首次因提示注入处罚律师](../../../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>

---

[← English original](../../../2026-04/2026-04-30-tui-chu-gao-ji-zhang.md) · [2026-04 index](../../../2026-04/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
