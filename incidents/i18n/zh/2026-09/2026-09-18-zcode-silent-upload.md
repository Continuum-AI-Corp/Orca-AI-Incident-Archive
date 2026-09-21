---
id: 2026-09-18-zcode-silent-upload
lang: zh
source: incidents/2026-09/2026-09-18-zcode-silent-upload.md
title: "智谱 ZCode 静默上传完整代码仓库，含 Git 历史"
summary: |
  用户发现**智谱 AI 编程 agent ZCode** 会静默打包**整个工作区并上传**：一位开发者的取证记录在隐藏目录 `~/.zcode` 中找到 **313MB 加密压缩包**，内含约 **4.2 万个文件、其中 86.6% 是 `.git` 历史**——已删除的密钥、配置与业务痕迹一并被打包带走；加密密钥由服务端下发、仅存于云端，**没有任何设置能关闭上传**。智谱当日致歉，将原因归于默认开启的**「代码库索引」**功能，称数据只为生成仓库 Wiki 而短暂存在、随后即销毁；客户**太原承明科技**对此提出异议，称修复后仍检测到上传行为，并要求智谱在 **10 月 10 日前**书面答复——包括数据是否出境。此后智谱已开源 ZCode，并称 v3.14.0 已完成整改
---

# 智谱 ZCode 静默上传完整代码仓库，含 Git 历史

<sub>Zhipu's ZCode agent silently uploaded whole repositories, Git history included</sub>

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## 概要

用户发现**智谱 AI 编程 agent ZCode** 会静默打包**整个工作区并上传**：一位开发者的取证记录在隐藏目录 `~/.zcode` 中找到 **313MB 加密压缩包**，内含约 **4.2 万个文件、其中 86.6% 是 `.git` 历史**——已删除的密钥、配置与业务痕迹一并被打包带走；加密密钥由服务端下发、仅存于云端，**没有任何设置能关闭上传**。智谱当日致歉，将原因归于默认开启的**「代码库索引」**功能，称数据只为生成仓库 Wiki 而短暂存在、随后即销毁；客户**太原承明科技**对此提出异议，称修复后仍检测到上传行为，并要求智谱在 **10 月 10 日前**书面答复——包括数据是否出境。此后智谱已开源 ZCode，并称 v3.14.0 已完成整改

## 攻击链

```mermaid
flowchart LR
    E["开发者登录 ZCode agent"]:::entry
    S0["「代码库索引」默认开启；工作区在客户端被打包加密"]:::step
    I["源代码、.git 历史、密钥与个人信息离开本机<br/><i>（厂商称数据已销毁；客户对此有异议）</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## 详情

**取证发现了什么。** **9 月 18 日**，开发者 **ferstar** 发布取证记录：他在清理磁盘时，于 ZCode 的隐藏目录 `~/.zcode` 中发现一个 **313MB 的加密压缩包**，内含约 **4.2 万个文件、其中 86.6% 是 `.git` 历史**——也就是说，不只是当前源码，连版本控制记录也被打包，包括那些已从工作区删除的密钥、配置与业务痕迹。打包**在登录后自动进行**，无需用户操作、也无任何提示；用于加密的 RSA 公钥从服务端获取，私钥仅存于云端，用户无法查看究竟有什么离开了自己的机器。上传过滤器中 `.git` 目录的优先级更高，使其**绕过了客户端的密钥扫描与体积限制**；产品中两个隐私开关也都没能阻止上传。

**厂商的回应。** 智谱当晚通过官方社群致歉，将上传归因于**「代码库索引」功能**——**自上线起便默认开启**——并称数据只为在云端生成仓库 Wiki 页面而短暂存在，随后「立即销毁」，从未用于模型训练。公司承诺开源 ZCode、邀请第三方审查系统，并为全体用户额外提供一次周额度重置作为补偿。**9 月 21 日**，智谱宣布客户端 **v3.14.0** 已完成整改、ZCode 正式开源，并称已邀请中国信息通信研究院与绿盟科技开展安全审计——信通院的技术评测确认 `zcode-prod` 阿里云 OSS 存储桶目前为**零数据**。

**客户的质疑——以及为何重要。** **太原承明科技**走得更远：在独立取证后，其于 **9 月 19–20 日**公开发函，指出上传是自动、批量发生的，所涉数据包含完整源代码、系统架构、版本控制历史、**数据库口令、云服务凭证及员工个人信息**——远超 ZCode 隐私政策载明的范围；且**在客户端已于 16 日更新至 3.12.3 后，9 月 18 日凌晨仍检测到上传行为**。函件还追问：为何网络请求指向**新加坡主体**而签约主体在北京（数据出境问题）；要求智谱在 **10 月 10 日前**就十项事项书面答复（彻底删除、数据处理清单、私钥保管、访问日志、删除证明、不再上传承诺等），并保留索赔、投诉与诉讼的权利。无论结果如何，本案标志着**agentic 编程工具**的数据处理——它们如今会读取整个代码仓库、掌握超过以往任何桌面软件的访问权限——已成为使用它们的企业的首要合规问题。

## 来源

| # | 来源 | 链接 |
|---|---|---|
| 1 | Global Times | <https://www.secrss.com/articles/94149> |
| 2 | The Paper | <https://news.qq.com/rain/a/20260921A02ESY00> |
| 3 | TechWeb | <https://news.qq.com/rain/a/20260920A05HHD00> |
| 4 | FreeBuf | <https://www.freebuf.com/articles/501972.html> |
| 5 | OSChina | <https://www.oschina.net/news/502589> |

## 元数据

| 字段 | 值 |
|---|---|
| 日期 | `2026-09-18`（原文：2026-09-18→21，精度 `day`） |
| 性质 | 事件 `incident` |
| 类型 | [`EXFIL`](../../../../taxonomy/types.md#exfil) 数据外泄 |
| 严重度 | **高** `high` |
| 可信度 | **A** — 一手来源（厂商 / 受害方 / 执法 / 官方报告） |
| 真实伤害 | 有 |
| AI 参与 | 已确认 `confirmed` |
| 地区 | [中国](../../../../regions/cn.md) |
| 档案编号 | `2026-09-18-zcode-silent-upload` |

<sub>**判定依据**：真实事件且受害方明确——受影响的开发者与企业公布了取证结果，厂商也承认了上传行为；来源质量记为 `A`。各方对修复后的行为与数据留存仍有分歧，两种立场均已在上文并列。定级 `high`：源代码、Git 历史乃至凭据在未经同意的情况下离开用户机器，且有客户正式追责。 分级口径见 [taxonomy/severity.md](../../../../taxonomy/severity.md) 与 [taxonomy/confidence.md](../../../../taxonomy/confidence.md)。</sub>

## 相关

**所属专题**：[零点击数据外泄链](../../../../topics/zero-click-exfil.md)

**同类条目**：

- `2026-09-08` [ChatGPT 沙箱缺陷让受害者的 Gmail 数据流进攻击者账号](../../../2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md)<br>  <sub>ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account</sub>
- `2026-08-04` [CHAINDROP npm 蠕虫](../../../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-09-01` [GitSpawn：恶意 .git/config 让 7 款编码 agent 在联系模型之前就执行攻击者代码](../../../2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br>  <sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub>

---

[← English original](../../../2026-09/2026-09-18-zcode-silent-upload.md) · [2026-09 index](../../../2026-09/README.md) · [All records](../../../README.md) · [Home](../../../../README.md)

<sub>本条目属于 **Orca AI Incident Archive**，按 [CC BY 4.0](../../../../LICENSE) 授权。发现事实错误或缺少来源，请[提 issue 或 PR](../../../../CONTRIBUTING.md)——更正会写进条目的修订记录，不会静默覆盖。</sub>
