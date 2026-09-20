---
id: 2026-09-18-hacktron-claude-openai-hack
title: "Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain"
title_zh: "研究员用 Claude 在漏洞赏金中攻破 OpenAI 内部系统"
title_ja: "研究者がClaudeを使いバグバウンティでOpenAI内部システムを侵害"
title_ko: "연구진, Claude로 버그바운티에서 OpenAI 내부 시스템 침투"
title_de: "Forscher nutzten Claude, um in einer Bug-Bounty-Kette in OpenAIs interne Systeme einzudringen"
title_fr: "Des chercheurs ont utilisé Claude pour pirater les systèmes internes d'OpenAI via un bug bounty"
title_es: "Investigadores usaron Claude para hackear los sistemas internos de OpenAI en un bug bounty"
date: 2026-09-18
date_precision: day
date_raw: "2026-09-17→18"

kind: vulnerability
type: [WEAPON, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [US]

summary: |
  A three-person team at **Hacktron AI** used **Claude** (a cybersecurity build of Opus 4.8, then **Opus 5** the day it released) to chain two critical flaws in OpenAI's **bug-bounty program**: an image bug in **libheif** behind **Discourse**'s HEIF/HEIC pipeline — fixed upstream in **libheif 1.22.0 (May 2026)** and tracked as **CVE-2026-32882**, but still unpatched in the forum's Debian 12 image — gave server access, and a flaw in OpenAI's **shared sign-on** allowed **takeover of ChatGPT and Codex accounts, including OpenAI employees'** — one with Codex wired into OpenAI's GitHub org. OpenAI fixed the issues and paid **$6,500** on 1 September; the researchers published the chain


summary_zh: |
  **Hacktron AI** 三人民队用 **Claude**（面向安全研究者的 Opus 4.8 版本，**Opus 5 发布当天换用**）在 OpenAI 的**漏洞赏金项目**中串联两个严重缺陷：经由 **Discourse** 的 HEIF/HEIC 图片管线触发 **libheif 图片缺陷**——上游已于 2026 年 5 月在 **libheif 1.22.0** 修复并记作 **CVE-2026-32882**，但论坛所用的 Debian 12 镜像仍是未打补丁的旧版——获得服务器权限；再借 OpenAI **共用 SSO** 的缺陷**接管 ChatGPT 与 Codex 账号，包括 OpenAI 员工的账号**——其中一位员工的 Codex 接入了 OpenAI 的 GitHub 组织。OpenAI 已修复并于 **9 月 1 日**支付 **6,500 美元**赏金；研究者公开了完整攻击链

summary_ja: |
  **Hacktron AI**の3人チームが**Claude**（セキュリティ研究者向けOpus 4.8、**Opus 5公開当日に切替**）を使い、OpenAIの**バグバウンティ**で2つの重大欠陥を連鎖させた：**Discourse**のHEIF/HEIC画像処理を経由した**libheifの画像バグ**（上流では2026年5月に**libheif 1.22.0**で修正され**CVE-2026-32882**として追跡されているが、フォーラムのDebian 12イメージは未パッチの旧版のまま）でサーバー権限を取得し、続いてOpenAIの**共通SSO**の欠陥で**ChatGPTとCodexのアカウント（OpenAI従業員を含む）を乗っ取り**——1人はCodexがOpenAIのGitHub組織に接続されていた。OpenAIは修正し**9月1日**に**6,500ドル**を支払い、研究者は攻撃チェーンを公開した

summary_ko: |
  **Hacktron AI** 3인 팀이 **Claude**(보안 연구자용 Opus 4.8, **Opus 5 공개 당일 교체**)로 OpenAI **버그바운티**에서 두 개의 치명적 결함을 연쇄했다: **Discourse**의 HEIF/HEIC 이미지 파이프라인을 통해 도달한 **libheif 이미지 버그**——업스트림에서는 2026년 5월 **libheif 1.22.0**에서 수정돼 **CVE-2026-32882**로 추적되었지만, 포럼의 Debian 12 이미지는 여전히 패치되지 않은 구버전——으로 서버 권한을 얻고, 이어 OpenAI **공용 SSO** 결함으로 **ChatGPT·Codex 계정(OpenAI 직원 포함)을 탈취**했다 — 한 직원의 Codex는 OpenAI GitHub 조직에 연결돼 있었다. OpenAI는 수정 후 **9월 1일**에 **6,500달러**를 지급했고 연구진은 체인을 공개했다

summary_de: |
  Ein dreiköpfiges Team von **Hacktron AI** nutzte **Claude** (ein Cybersicherheits-Build von Opus 4.8, dann **Opus 5 am Erscheinungstag**) in OpenAIs **Bug-Bounty-Programm**, um zwei kritische Lücken zu verketten: ein Bildfehler in **libheif** hinter **Discourses** HEIF/HEIC-Pipeline — upstream im Mai 2026 in **libheif 1.22.0** behoben und als **CVE-2026-32882** geführt, aber im Debian-12-Image des Forums weiterhin ungepatcht — verschaffte Serverzugriff; eine Schwäche in OpenAIs **gemeinsamem SSO** erlaubte die **Übernahme von ChatGPT- und Codex-Konten, auch von OpenAI-Mitarbeitern** — bei einem war Codex mit der OpenAI-GitHub-Organisation verbunden. OpenAI behob die Probleme und zahlte am **1. September 6.500 US-Dollar**; die Forscher veröffentlichten die Kette

summary_fr: |
  Une équipe de trois personnes de **Hacktron AI** a utilisé **Claude** (une version cybersécurité d'Opus 4.8, puis **Opus 5 le jour de sa sortie**) dans le **programme de bug bounty** d'OpenAI pour enchaîner deux failles critiques : un bug d'image dans **libheif**, derrière la chaîne HEIF/HEIC de **Discourse** — corrigé en amont en mai 2026 dans **libheif 1.22.0** et suivi comme **CVE-2026-32882**, mais toujours non corrigé dans l'image Debian 12 du forum — a donné accès au serveur ; une faille dans le **SSO partagé** d'OpenAI a permis de **prendre le contrôle de comptes ChatGPT et Codex, y compris d'employés d'OpenAI** — l'un ayant Codex relié à l'organisation GitHub d'OpenAI. OpenAI a corrigé et versé **6 500 $** le **1er septembre** ; les chercheurs ont publié la chaîne

summary_es: |
  Un equipo de tres personas de **Hacktron AI** usó **Claude** (una versión de ciberseguridad de Opus 4.8 y, el día de su lanzamiento, **Opus 5**) en el **programa de bug bounty** de OpenAI para encadenar dos fallos críticos: un fallo de imagen en **libheif**, tras la tubería HEIF/HEIC de **Discourse** — corregido aguas arriba en mayo de 2026 en **libheif 1.22.0** y registrado como **CVE-2026-32882**, pero aún sin parche en la imagen Debian 12 del foro — dio acceso al servidor; un fallo en el **SSO compartido** de OpenAI permitió **tomar el control de cuentas de ChatGPT y Codex, incluidas las de empleados de OpenAI** — uno con Codex conectado a la organización de GitHub de OpenAI. OpenAI lo corrigió y pagó **6.500 $** el **1 de septiembre**; los investigadores publicaron la cadena

sources:
  - url: https://www.hacktron.ai/blog/hacking-openai
    label: Hacktron AI
  - url: https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html
    label: The Hacker News
  - url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
    label: TechCrunch
  - url: https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883
    label: WSJ
  - url: https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335
    label: Discourse advisory
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-32882
    label: NVD

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A three-person team at **Hacktron AI** used **Claude** (a cybersecurity build of Opus 4.8, then **Opus 5** the day it released) to chain two critical flaws in OpenAI's **bug-bounty program**: an image bug in **libheif** behind **Discourse**'s HEIF/HEIC pipeline — fixed upstream in **libheif 1.22.0 (May 2026)** and tracked as **CVE-2026-32882**, but still unpatched in the forum's Debian 12 image — gave server access, and a flaw in OpenAI's **shared sign-on** allowed **takeover of ChatGPT and Codex accounts, including OpenAI employees'** — one with Codex wired into OpenAI's GitHub org. OpenAI fixed the issues and paid **$6,500** on 1 September; the researchers published the chain

## Attack chain

```mermaid
flowchart LR
    E["iPhone HEIC upload to OpenAI's community forum"]:::entry
    S0["Discourse → ImageMagick → libheif image bug → RCE (CVE-2026-32882) → server hijack"]:::step
    S1["Second flaw takes over ChatGPT/Codex accounts, incl. employees"]:::step
    I["Codex linked to OpenAI's GitHub org; reported, fixed, $6,500 bounty"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The chain.** Hacktron found the path into OpenAI on **25 July** through **Discourse**, the community-forum software. The entry point was an image upload: HEIF/HEIC files (iPhone default) were passed through ImageMagick to a **libheif** decoder, where a crafted file triggered a memory bug — **Discourse's advisory rates the result as remote code execution (CVSS 8.8) and tracks it as CVE-2026-32882**, while libheif's own record describes an **out-of-bounds read** that leaks memory and helps defeat ASLR; the researchers say they **combined several libheif memory bugs, with the AI's help, to turn the crash into working code execution**. Upstream had **fixed the flaw in libheif 1.22.0 in May 2026** — months before the test — but the forum's **Debian 12 image still shipped the unpatched libheif 1.19.7**, so the fix and its CVE were public without reaching the running server. From there, a flaw in **OpenAI's shared sign-on** (the forum's "Sign in with OpenAI" is the same SSO staff use elsewhere) allowed **takeover of users' ChatGPT and Codex accounts, including OpenAI employees'** — one employee's Codex was **connected to OpenAI's GitHub organisation**, reaching internal code repositories. The team proved access with a **single harmless pull request**, read no source code, merged nothing and touched no customer data; Hacktron alerted OpenAI and Discourse, and Discourse fixed on **27 July**.

**The Claude timeline.** A special cybersecurity build of **Opus 4.8 "struggled across several sessions to produce a working exploit"** with ASLR enabled; Anthropic released **Opus 5 on the evening of 24 July**, and "within hours of Opus 5's release, we gave it the same problem and it succeeded." The model's safeguards against writing exploit code for real targets were worked around by pointing it at the team's own server disguised as a **CTF practice target** — and the researchers stress the work was **not hands-off**: skilled human direction still mattered.

**Responses and context.** OpenAI resolved the issues and paid a **$6,500** bounty on **1 September**, saying the award "recognizes the OpenAI-side finding, not the actions against Discourse" (the forum itself is outside its bounty programme). There is **no sign the flaw was used against anyone in the real world**. Commentators framed the case as a watershed — "For $200 a month, anyone can use these tools and hack into a company like OpenAI" (Matt Fredrikson, Gray Swan) — and it also highlights **Opus 5's absence of export restrictions** despite its offensive capability, unlike the locked-down Mythos 5. The OpenAI work was part of a wider Hacktron project ("HEIF Heist") that the team says found similar image-decoding bugs in software used by Slack, Meta, GitHub Enterprise and Next.js; the Next.js bug and a Meta exploit are independently confirmed, while the **wider code-execution claims are not**.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Hacktron AI | <https://www.hacktron.ai/blog/hacking-openai> |
| 2 | The Hacker News | <https://thehackernews.com/2026/09/claude-opus-5-helped-researchers-take.html> |
| 3 | TechCrunch | <https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/> |
| 4 | WSJ | <https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883> |
| 5 | Discourse advisory | <https://github.com/discourse/discourse/security/advisories/GHSA-vhm9-85gw-x335> |
| 6 | NVD | <https://nvd.nist.gov/vuln/detail/CVE-2026-32882> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-18` (raw: 2026-09-17→18, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | no |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-09-18-hacktron-claude-openai-hack` |

<sub>**Why this classification:** Vulnerability disclosure handled under a bug-bounty program; the flaws were fixed with no evidence of malicious exploitation, so `real_harm: false`. Rated `high`: critical flaws chained through to employee-account takeover and access to internal repositories. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-17` [Plugin4Shell: a zero-click RCE chain hits four AI coding agents](2026-09-17-plugin4shell-coding-agents.md)<br>  <sub>Plugin4Shell: a zero-click RCE chain hits four AI coding agents</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-09-16` [OpenAI discloses six misalignment incidents and a reporting framework](2026-09-16-openai-misalignment-reports.md)<br>  <sub>OpenAI discloses six misalignment incidents and a reporting framework</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-18-hacktron-claude-openai-hack.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
