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
  A three-person team at **Hacktron AI** used **Claude** (a cybersecurity build of Opus 4.8, then **Opus 5** the day it released) to chain two critical flaws in OpenAI's **bug-bounty program**: a memory bug in **libheif** reached through **Discourse**'s HEIF/HEIC image pipeline (already fixed upstream but **never assigned a CVE**, so the forum still ran the vulnerable version) gave server access, and a second flaw allowed **takeover of ChatGPT and Codex accounts, including OpenAI employees'** — one with Codex wired into OpenAI's GitHub org. OpenAI fixed the issues and paid **$6,500**; the researchers published the chain


summary_zh: |
  **Hacktron AI** 三人民队用 **Claude**（面向安全研究者的 Opus 4.8 版本，**Opus 5 发布当天换用**）在 OpenAI 的**漏洞赏金项目**中串联两个严重缺陷：经由 **Discourse** 的 HEIF/HEIC 图片管线触发 **libheif 内存缺陷**（上游早已修复但**从未分配 CVE**，论坛仍在跑有漏洞的版本）获得服务器权限；第二个缺陷使其**接管 ChatGPT 与 Codex 账号，包括 OpenAI 员工的账号**——其中一位员工的 Codex 接入了 OpenAI 的 GitHub 组织。OpenAI 已修复并支付 **6,500 美元**赏金；研究者公开了完整攻击链

summary_ja: |
  **Hacktron AI**の3人チームが**Claude**（セキュリティ研究者向けOpus 4.8、**Opus 5公開当日に切替**）を使い、OpenAIの**バグバウンティ**で2つの重大欠陥を連鎖させた：**Discourse**のHEIF/HEIC画像処理を経由した**libheifのメモリバグ**（上流では修正済みだが**CVE未採番**のためフォーラムは脆弱版のまま）でサーバー権限を取得し、2つ目の欠陥で**ChatGPTとCodexのアカウント（OpenAI従業員を含む）を乗っ取り**——1人はCodexがOpenAIのGitHub組織に接続されていた。OpenAIは修正し**6,500ドル**を支払い、研究者は攻撃チェーンを公開した

summary_ko: |
  **Hacktron AI** 3인 팀이 **Claude**(보안 연구자용 Opus 4.8, **Opus 5 공개 당일 교체**)로 OpenAI **버그바운티**에서 두 개의 치명적 결함을 연쇄했다: **Discourse**의 HEIF/HEIC 이미지 파이프라인을 통해 도달한 **libheif 메모리 버그**(업스트림에서 이미 수정됐지만 **CVE 미부여**로 포럼은 취약 버전 실행)로 서버 권한을 얻고, 두 번째 결함으로 **ChatGPT·Codex 계정(OpenAI 직원 포함)을 탈취**했다 — 한 직원의 Codex는 OpenAI GitHub 조직에 연결돼 있었다. OpenAI는 수정 후 **6,500달러**를 지급했고 연구진은 체인을 공개했다

summary_de: |
  Ein dreiköpfiges Team von **Hacktron AI** nutzte **Claude** (ein Cybersicherheits-Build von Opus 4.8, dann **Opus 5 am Erscheinungstag**) in OpenAIs **Bug-Bounty-Programm**, um zwei kritische Lücken zu verketten: ein Speicherfehler in **libheif**, erreichbar über **Discourses** HEIF/HEIC-Bildpipeline (upstream längst gefixt, aber **nie mit CVE versehen**, daher lief das Forum noch verwundbar), verschaffte Serverzugriff; eine zweite Lücke erlaubte die **Übernahme von ChatGPT- und Codex-Konten, auch von OpenAI-Mitarbeitern** — bei einem war Codex mit der OpenAI-GitHub-Organisation verbunden. OpenAI behob die Probleme und zahlte **6.500 US-Dollar**; die Forscher veröffentlichten die Kette

summary_fr: |
  Une équipe de trois personnes de **Hacktron AI** a utilisé **Claude** (une version cybersécurité d'Opus 4.8, puis **Opus 5 le jour de sa sortie**) dans le **programme de bug bounty** d'OpenAI pour enchaîner deux failles critiques : un bug mémoire dans **libheif**, atteint via la chaîne d'images HEIF/HEIC de **Discourse** (corrigé en amont mais **jamais doté d'un CVE**, le forum exécutait donc la version vulnérable), a donné accès au serveur ; une seconde faille a permis de **prendre le contrôle de comptes ChatGPT et Codex, y compris d'employés d'OpenAI** — l'un ayant Codex relié à l'organisation GitHub d'OpenAI. OpenAI a corrigé et versé **6 500 $** ; les chercheurs ont publié la chaîne

summary_es: |
  Un equipo de tres personas de **Hacktron AI** usó **Claude** (una versión de ciberseguridad de Opus 4.8 y, el día de su lanzamiento, **Opus 5**) en el **programa de bug bounty** de OpenAI para encadenar dos fallos críticos: un error de memoria en **libheif**, alcanzado por la tubería de imágenes HEIF/HEIC de **Discourse** (corregido aguas arriba pero **sin CVE asignado**, así que el foro seguía ejecutando la versión vulnerable), dio acceso al servidor; un segundo fallo permitió **tomar el control de cuentas de ChatGPT y Codex, incluidas las de empleados de OpenAI** — uno con Codex conectado a la organización de GitHub de OpenAI. OpenAI lo corrigió y pagó **6.500 $**; los investigadores publicaron la cadena

sources:
  - url: https://www.hacktron.ai/blog/hacking-openai
    label: Hacktron AI
  - url: https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/
    label: TechCrunch
  - url: https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883
    label: WSJ

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Researchers used Claude to hack OpenAI's internal systems in a bug-bounty chain

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

A three-person team at **Hacktron AI** used **Claude** (a cybersecurity build of Opus 4.8, then **Opus 5** the day it released) to chain two critical flaws in OpenAI's **bug-bounty program**: a memory bug in **libheif** reached through **Discourse**'s HEIF/HEIC image pipeline (already fixed upstream but **never assigned a CVE**, so the forum still ran the vulnerable version) gave server access, and a second flaw allowed **takeover of ChatGPT and Codex accounts, including OpenAI employees'** — one with Codex wired into OpenAI's GitHub org. OpenAI fixed the issues and paid **$6,500**; the researchers published the chain

## Attack chain

```mermaid
flowchart LR
    E["iPhone HEIC upload to OpenAI's community forum"]:::entry
    S0["Discourse → ImageMagick → libheif memory bug (no CVE) → server hijack"]:::step
    S1["Second flaw takes over ChatGPT/Codex accounts, incl. employees"]:::step
    I["Codex linked to OpenAI's GitHub org; reported, fixed, $6,500 bounty"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The chain.** Hacktron found the path into OpenAI on **25 July** through **Discourse**, the community-forum software. The entry point was an image upload: HEIF/HEIC files (iPhone default) were passed through ImageMagick to a **libheif** decoder, where a memory bug miscalculated image positioning and allowed a crafted file to **hijack the server**. Notably, libheif had **already fixed** the bug months earlier, but the fix was **never formally flagged as a vulnerability and never got a CVE**, which Hacktron suggests is why Discourse's software still ran the vulnerable version. From the server, a second flaw allowed **takeover of users' ChatGPT and Codex accounts, including OpenAI employees'** — one employee's Codex was **connected to OpenAI's GitHub organisation**, exposing internal code repositories. Hacktron alerted OpenAI and Discourse; Discourse fixed on **27 July**.

**The Claude timeline.** A special cybersecurity build of **Opus 4.8 "struggled across several sessions to produce a working exploit"**; "within hours of **Opus 5's** release, we gave it the same problem and it succeeded," the researchers wrote — a concrete data point for how model upgrades collapsed an exploit-development task that had resisted the prior version.

**Responses and context.** OpenAI resolved the issues and paid a **$6,500** bounty. Security commentators framed it as a watershed: "For $200 a month, anyone can use these tools and hack into a company like OpenAI" (Matt Fredrikson, Gray Swan); and "if these three guys can pull this off, what can a nation state do" (Andrew Curran). The case sits between two other September threads — OpenAI's own agents breaching Hugging Face in July, and the Claude Opus 5 model's absence of export restrictions despite its offensive capability (unlike the locked-down Mythos 5).

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Hacktron AI | <https://www.hacktron.ai/blog/hacking-openai> |
| 2 | TechCrunch | <https://techcrunch.com/2026/09/18/researchers-used-anthropics-claude-to-hack-into-openai/> |
| 3 | WSJ | <https://www.wsj.com/tech/ai/hackers-used-anthropics-claude-to-break-into-openai-b40ba883> |

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
