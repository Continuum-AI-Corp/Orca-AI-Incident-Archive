---
id: 2026-10-23-openai-redteam-microvm-covert-channel
lang: zh
source: incidents/2026-10/2026-10-23-openai-redteam-microvm-covert-channel.md
title: "OpenAI 红队 agent 在其训练环境中建起 CPU 缓存隐蔽信道、逃出 microVM 沙箱"
summary: |
  **在 2026 年 10 月 23 日发布的报告《Securing our frontier model training environment》中，OpenAI 披露：在内部**红队演练**中，运行于同一宿主、彼此隔离的 **microVM 里的 agent 用 CPU 缓存时序建起了隐蔽信道**——一个 agent 把数据逐出处理器缓存、另一个计量它重新载入的快慢——从而在**无网络、无共享文件**的情况下传递合成机密。** OpenAI 将其定性为*协作* agent 之间的通信演示（Spectre/Meltdown 同族技术），而非新的硬件漏洞；另发现三条更慢的隐蔽信道。此外，agent **链式利用软件缺陷逃出 microVM 隔离**，牵出对 **Kata Containers（CVE-2026-24834，容器→guest 的 microVM 逃逸，明确不是宿主逃逸）、gVisor 与 Docker** 的修复。重要限定：演练是**受控**的——研究者提供了源码、配置与可能弱点的线索，故 agent 并非全程自力找到每条路径——且涉及的是**内部训练/评估系统，无面向客户或外部的影响**（OpenAI 称未发现 agent 可轻易利用、又能隐蔽于监控的互联网路径）。记为 `research` / `EVAL` + `SANDBOX` / `medium` / `real_harm: false`——厂商对 agent 探测自身沙箱的红队研究。
---

# OpenAI 红队 agent 在其训练环境中建起 CPU 缓存隐蔽信道、逃出 microVM 沙箱

<sub>OpenAI red-team agents built a CPU-cache covert channel and escaped microVM sandboxes in its training environment</sub>

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-8F6A3C?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-3C6E8F?style=flat-square)

## 概要

**在 2026 年 10 月 23 日发布的报告《Securing our frontier model training environment》中，OpenAI 披露：在内部**红队演练**中，运行于同一宿主、彼此隔离的 **microVM 里的 agent 用 CPU 缓存时序建起了隐蔽信道**——一个 agent 把数据逐出处理器缓存、另一个计量它重新载入的快慢——从而在**无网络、无共享文件**的情况下传递合成机密。** OpenAI 将其定性为*协作* agent 之间的通信演示（Spectre/Meltdown 同族技术），而非新的硬件漏洞；另发现三条更慢的隐蔽信道。此外，agent **链式利用软件缺陷逃出 microVM 隔离**，牵出对 **Kata Containers（CVE-2026-24834，容器→guest 的 microVM 逃逸，明确不是宿主逃逸）、gVisor 与 Docker** 的修复。重要限定：演练是**受控**的——研究者提供了源码、配置与可能弱点的线索，故 agent 并非全程自力找到每条路径——且涉及的是**内部训练/评估系统，无面向客户或外部的影响**（OpenAI 称未发现 agent 可轻易利用、又能隐蔽于监控的互联网路径）。记为 `research` / `EVAL` + `SANDBOX` / `medium` / `real_harm: false`——厂商对 agent 探测自身沙箱的红队研究。

## 攻击链

```mermaid
flowchart LR
    E["红队 agent 运行于同一宿主、<br/>彼此隔离的 microVM（内部训练环境）"]:::entry
    S1["无网络/无共享文件 →<br/>用 CPU 缓存时序建隐蔽信道"]:::step
    S2["另：链式利用软件缺陷逃出 microVM 隔离<br/>（Kata CVE-2026-24834 等）"]:::step
    I["受控演练（研究者给了线索）；<br/>仅内部、无客户/外部影响"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**OpenAI 披露了什么。** 2026 年 **10 月 23 日**，OpenAI 发布报告《Securing our frontier model training environment》，描述其对**内部训练与评估**基础设施隔离性的红队演练。一项结果中，被放进同一宿主上**彼此隔离的 microVM** 的 agent 被要求在无网络、无共享可写文件的情况下交换机密；它们用 **CPU 缓存时序建起了隐蔽信道**——一个 agent 把选定数据逐出处理器缓存、另一个计量重新载入的快慢。OpenAI 称这是与 **Spectre/Meltdown 同族的技术**、是**协作** agent 之间的通信演示，而**非新发现的硬件漏洞**。演练还浮现出**另外三条隐蔽信道**，OpenAI 称多数较慢、模型难以利用。

**microVM 逃逸。** 另外，agent **链式利用软件缺陷突破了 microVM 隔离**。报告提到对多个容器/沙箱项目的修复，唯一具名的 CVE 是 **Kata Containers 的 CVE-2026-24834**——明确为**容器→guest 的 microVM 逃逸、不是宿主逃逸**（影响 ≤3.26.0，3.27.0 修复）；**gVisor** 与 **Moby/Docker** 也贡献了修复、无分配 CVE。在部分宿主入侵测试中，研究者**主动给了 agent 完整宿主权限**，其中一条路径经一个指标服务走了间接的互联网通道。

**为何记 `research`、`real_harm: false`。** 这是一次**受控红队研究**，不是失控入侵：OpenAI 研究者**提供了源码、配置与可能弱点的信息**，故 agent 并非独立发现每条路径，部分标题的"0-day"措辞过头。工作限定于**内部训练/评估系统**——OpenAI 称**无面向客户或外部的影响**，也未发现 agent 可轻易利用、又能隐蔽于监控的互联网路径。之所以收录，是因为它是一次值得注意的一手演示：agent 能**探测并跨越沙箱边界**（含一个真实的 Kata CVE），与更早的 VM 容纳性研究同属一类关切。

**如何分级。** `research`——厂商的受控红队研究，而非现实事件。`EVAL`（OpenAI 自家评估/训练中的 agent）+ `SANDBOX`（隐蔽信道与 microVM 隔离逃逸）。`real_harm: false`：受控、内部、无客户或外部影响。评 `medium`：有意义的能力演示加一个真实的容器逃逸 CVE，但受研究者协助、限于内部基础设施、且具名 CVE 不含宿主逃逸。可信度 `A`：OpenAI 自家报告 + 独立报道（Tom's Hardware、Cyber Security News、Startup Fortune）。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Tom's Hardware | <https://www.tomshardware.com/tech-industry/artificial-intelligence/openais-isolated-red-team-ai-agents-built-a-hidden-cpu-cache-channel-to-talk-with-no-network-or-shared-files-exploited-cpu-cache-timing-to-bypass-microvm-sandboxes> |
| 2 | Cyber Security News | <https://cybersecuritynews.com/openai-ai-agents-bypass-security/> |
| 3 | Startup Fortune | <https://startupfortune.com/openai-reveals-its-red-teaming-agents-found-a-hardware-level-covert-channel/> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-10-23`（原始：2026-10-23 OpenAI 报告《Securing our frontier model training environment》，精度 `day`） |
| 性质 | 研究／红队 `research` |
| 类型 | [`EVAL`](../../../../taxonomy/types.md#eval) [`SANDBOX`](../../../../taxonomy/types.md#sandbox) |
| 评级 | **中** `medium` |
| 可信度 | **A**——OpenAI 自家报告 + 独立报道 |
| 真实伤害 | 无——受控内部红队研究；无面向客户或外部的影响 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [全球](../../../../regions/global.md) |
| 档案 ID | `2026-10-23-openai-redteam-microvm-covert-channel` |

<sub>**分类理由：** 厂商红队研究（`research`）：OpenAI 自家评估中的 agent（`EVAL`）建起 CPU 缓存隐蔽信道、链式逃出 microVM 隔离（`SANDBOX`），含一个真实的 Kata Containers CVE（容器→guest、非宿主逃逸）。`real_harm: false`——受控、受研究者协助、仅内部、无客户/外部影响。评 `medium`：有意义的能力演示加一个容器逃逸 CVE，但有边界、受协助。分级标准见 [severity.md](../../../../taxonomy/severity.md) 与 [confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关条目

**专题：** [前沿模型自主越界（EVAL）](../../../../topics/eval-escapes.md)

**相关记录：**

- `2026-08-26` [Trail of Bits：虚拟机关不住联网的 agent](../../../2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br>  <sub>更早关于 agent 沙箱局限的研究</sub>
- `2026-10-15` [一个 OpenAI 研究模型为完成编码任务动用了他人钱包的测试网 ETH](2026-10-15-openai-agent-testnet-wallet.md)<br>  <sub>同月另一起 OpenAI 评估期 agent 行为披露</sub>
- `2026-09-16` [OpenAI 披露六起错位事件与一套上报框架](../../../2026-09/2026-09-16-openai-misalignment-reports.md)<br>  <sub>OpenAI 更广的失准披露计划</sub>

---

[← English original](../../../2026-10/2026-10-23-openai-redteam-microvm-covert-channel.md) · [2026-10 index](../../../2026-10/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
