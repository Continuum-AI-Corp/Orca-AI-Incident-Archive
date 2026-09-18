---
id: 2026-06-15-searchleak
lang: zh
source: incidents/2026-06/2026-06-15-searchleak.md
title: "SearchLeak（CVE-2026-42824）"
summary: |
  Varonis 三段链：① 搜索 URL 的 `q` 参数被当指令 ② 无害化是**生成后的后处理**，流式渲染中的 `<img>` 已先发出请求 ③ CSP 允许 `*.bing.com`，**Bing 图片搜索在服务端抓取指定 URL，浏览器 CSP 管不着**。诱导域名是 microsoft.com，Copilot 以用户权限运行 —— 受害者**点一次链接**即泄露邮件、安全验证码、日历、SharePoint、OneDrive。微软已修复、用户无需操作；Varonis 称微软给了 critical，MSRC 页面基本值 6.5
---

# SearchLeak（CVE-2026-42824）

<sub>SearchLeak (CVE-2026-42824)</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

Varonis 三段链：① 搜索 URL 的 `q` 参数被当指令 ② 无害化是**生成后的后处理**，流式渲染中的 `<img>` 已先发出请求 ③ CSP 允许 `*.bing.com`，**Bing 图片搜索在服务端抓取指定 URL，浏览器 CSP 管不着**。诱导域名是 microsoft.com，Copilot 以用户权限运行 —— 受害者**点一次链接**即泄露邮件、安全验证码、日历、SharePoint、OneDrive。微软已修复、用户无需操作；Varonis 称微软给了 critical，MSRC 页面基本值 6.5

## 攻击链

```mermaid
flowchart LR
    E["外部内容<br/>邮件 · 文档 · Issue · 网页"]:::entry
    S0["agent 读取并当作指令执行"]:::step
    S1["经厂商可信域外带<br/>图片渲染 · API · 代理"]:::step
    I["数据落入攻击者手中<br/><i>（实验室演示 · 无真实受害方）</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Varonis | <https://www.varonis.com/blog/searchleak> |
| 2 | MSRC | <https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-42824> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-06-15`（原文：2026-06-15，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`IPI`](../../../../taxonomy/types.md#ipi) 间接提示注入 · [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **中** `medium` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-06-15-searchleak` |

<sub>**判定依据**：研究机构或厂商的受控演示，`real_harm: false`；收录是为了标记攻击面何时被公开。 判 `medium`：受控演示、中等缺陷，或单用户 / 单机范围的事故。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-06-01` [黑客直接「请求」Meta AI 客服机器人交出 Instagram 账号](../../../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-12` [Agentjacking：一个公开 DSN 就能劫持 AI 编码 agent](../../../2026-06/2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>
- `2026-06-24` [BioShocking：把 agent 先教傻，再让它交出密码](../../../2026-06/2026-06-24-bioshocking-agent-xian-jiao-sha.md)<br>  <sub>BioShocking: dumb the agent down first, then take the password</sub>
- `2026-06-08` [AgentForger：一条链接伪造出一个「AI 内鬼」](../../../2026-06/2026-06-08-agentforger-yi-tiao-lian-jie.md)<br>  <sub>AgentForger: one link forges an "AI insider"</sub>

---

[← English original](../../../2026-06/2026-06-15-searchleak.md) · [2026-06 index](../../../2026-06/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
