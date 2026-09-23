---
id: 2026-07-31-exposed-by-design-mcp-servers
lang: zh
source: incidents/2026-07/2026-07-31-exposed-by-design-mcp-servers.md
title: "《Exposed by Design》：对 414 个公网 MCP 服务器的动态审计发现 68 个漏洞"
summary: |
  **Nicolás Padilla** 在 arXiv 发布《**Exposed by Design**》（2608.00150），作者称这是首个针对公网 **MCP 服务器**的动态行为安全评估。研究先从 GitHub、npm、PyPI、Smithery、Hugging Face、Shodan、Censys、FOFA 等十一个来源发现服务器，再用自研框架 **Corvus**（34 个测试模块，覆盖 10 类 MCP 特有漏洞）做实时测试。在 2026 年 7 月的四轮测量中，研究确认了 **640 个生产环境服务器**，对其中 **414 个**做了动态审计，发现 **68 个可报告的漏洞**，包括 SQL 注入、针对云元数据服务的 SSRF、提示模板注入和路径遍历。**受审计服务器中 91.8% 没有 OAuth 认证**，**687 个工具实例在没有访问控制的情况下暴露 shell 执行能力**，**41.6% 的已确认服务器在两轮测量之间的三天内就已消失**。Corvus 已开源；论文未声称存在在野利用
---

# 《Exposed by Design》：对 414 个公网 MCP 服务器的动态审计发现 68 个漏洞

<sub>Exposed by Design: a dynamic audit of 414 internet-facing MCP servers finds 68 vulnerabilities</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## 概要

**Nicolás Padilla** 在 arXiv 发布《**Exposed by Design**》（2608.00150），作者称这是首个针对公网 **MCP 服务器**的动态行为安全评估。研究先从 GitHub、npm、PyPI、Smithery、Hugging Face、Shodan、Censys、FOFA 等十一个来源发现服务器，再用自研框架 **Corvus**（34 个测试模块，覆盖 10 类 MCP 特有漏洞）做实时测试。在 2026 年 7 月的四轮测量中，研究确认了 **640 个生产环境服务器**，对其中 **414 个**做了动态审计，发现 **68 个可报告的漏洞**，包括 SQL 注入、针对云元数据服务的 SSRF、提示模板注入和路径遍历。**受审计服务器中 91.8% 没有 OAuth 认证**，**687 个工具实例在没有访问控制的情况下暴露 shell 执行能力**，**41.6% 的已确认服务器在两轮测量之间的三天内就已消失**。Corvus 已开源；论文未声称存在在野利用

## 攻击链

```mermaid
flowchart LR
    E["一个部署在公网上的 MCP 服务器"]:::entry
    S0["没有 OAuth，工具在无访问控制的情况下暴露 shell 执行"]:::step
    I["SQL 注入、打向云元数据的 SSRF、路径遍历<br/><i>（测量研究，未声称在野利用）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**测的是行为，不是清单。** 论文的出发点是：MCP 自 2024 年 11 月推出以来，公网上可探测到的服务器实例已超过 21,000 个；研究要测的是这些服务器运行起来之后实际会做什么——作者因此称之为动态行为评估。方法分两半。被动发现从十一个数据源收集候选服务器，既有软件包仓库（npm、PyPI）和 MCP 目录（Smithery），也有全网扫描器（Shodan、Censys、FOFA）。主动测试则运行 **Corvus**——作者为这项研究自建并已开源的框架，含 34 个测试模块，覆盖 10 类 MCP 特有漏洞。2026 年 7 月的四轮测量确认了 640 个生产环境服务器，其中 414 个做了动态审计，得到 68 个可报告的漏洞：SQL 注入、针对云元数据服务的 SSRF、提示模板注入，以及借游标操纵实现的路径遍历。

**值得记住的三个数字。** 第一，**受动态审计的服务器中 91.8% 没有 OAuth 认证**——而这正是 MCP 规范为这种部署形态提供的控制手段。第二，**已确认服务器上有 687 个工具实例在没有访问控制的情况下暴露 shell 执行能力**：任何能连上服务器的远端，都可以让它执行命令。第三，**41.6% 的已确认服务器在相邻两轮测量之间的三天内就已消失**，作者把这解读为缺乏安全审查的快速部署周期。对防守方来说，最后这个数字和前两个同样重要：暴露在外的 MCP 服务器清单几天就会过时，一次性扫描会低估任一时刻实际可触达的范围。

**怎么读这篇论文。** 这是一篇单作者预印本，尚未经过同行评审，68 项发现都没有 CVE 编号或厂商公告；论文报告了相应的负责任披露流程，但没有在野利用。本档案收录它，是因为它所测量的暴露面在档案其他条目里并非假设：2026 年 4 月，nginx-ui 暴露在外的 MCP 端点遭到在野攻击；9 月，LiteLLM MCP 端点的认证绕过进入了 CISA 的已知被利用漏洞目录。由此得出的建议并不新鲜——给每一个能从公网访问的 MCP 服务器加上认证，不要把能执行 shell 的工具暴露给无法识别身份的调用方。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | arXiv 2608.00150 | <https://arxiv.org/abs/2608.00150> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-07-31`（原文：2026-07-31，精度 `day`） |
| 性质 | 研究演示 `research` |
| 类型 | [`MCP`](../../../../taxonomy/types.md#mcp) MCP / 工具链 · [`INFRA`](../../../../taxonomy/types.md#infra) agent 基础设施暴露 |
| 严重度 | **中** `medium` |
| 可信度 | **B** —— 单作者学术预印本，方法可核查、工具已开源，但没有 CVE 或厂商公告可作锚点 |
| 真实伤害 | 否 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案编号 | `2026-07-31-exposed-by-design-mcp-servers` |

<sub>**判定依据：** 带实时测试的测量研究，`real_harm: false`；本条记录的是这一暴露面何时被量化。判 `medium`：是对大规模暴露的受控测量，而非已证实的入侵。判 `B`：预印本未经同行评审，且其发现均无 CVE 或厂商公告作锚点。日期取 arXiv v1 提交日（2026 年 7 月 31 日）。分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题：** [agent 供应链投毒](../../../../topics/agent-supply-chain.md) · [agent 基础设施暴露](../../../../topics/agent-infra.md)

**相关条目：**

- `2026-04-16` [MCPwn（CVE-2026-33032）：nginx-ui 的 MCP 端点在野被打](../../../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>一个真的遭到攻击的暴露 MCP 端点</sub>
- `2026-09-02` [任意 Bearer 令牌即可打开 LiteLLM 的 MCP 端点：CVE-2026-59822 进入 CISA KEV](../../../2026-09/2026-09-02-litellm-mcp-auth-bypass-kev.md)<br>  <sub>进入 CISA KEV 的 MCP 认证缺陷</sub>
- `2025-06-13` [MCP Inspector 未认证 RCE](../../../2025-06/2025-06-13-mcp-inspector-rce.md)<br>  <sub>一年前，MCP 工具链同样缺认证</sub>
- `2026-08-10` [Deadbugz：一个在第三次工具调用后翻脸的 MCP 服务器](../../../2026-08/2026-08-10-deadbugz-mcp-supply-chain.md)<br>  <sub>为什么对 MCP 服务器只审一次不够</sub>

---

[← 2026-07 索引](../../../2026-07/README.md) · [← 全库索引](../../../../README.md) · [English](../../../2026-07/2026-07-31-exposed-by-design-mcp-servers.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
