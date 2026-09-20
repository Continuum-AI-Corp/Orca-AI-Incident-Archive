---
id: 2026-09-16-mandiant-ai-risk-resilience-2026
title: "Mandiant 2026 AI report: a runaway agent's $50,000 bill and AI-assisted intrusions"
title_zh: "Mandiant 2026 AI 报告：失控 agent 烧掉 5 万美元账单，AI 辅助入侵登场"
title_ja: "Mandiant 2026 AIレポート：暴走エージェントの5万ドル請求とAI支援型侵入"
title_ko: "Mandiant 2026 AI 보고서: 폭주 에이전트의 5만 달러 청구서와 AI 지원 침입"
title_de: "Mandiant-KI-Bericht 2026: 50.000-Dollar-Rechnung eines außer Kontrolle geratenen Agenten"
title_fr: "Rapport IA 2026 de Mandiant : une facture de 50 000 $ due à un agent emballé"
title_es: "Informe de IA 2026 de Mandiant: una factura de 50.000 $ de un agente desbocado"
date: 2026-09-16
date_raw: "2026-09-15→16"
date_precision: day

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Mandiant's **AI Risk and Resilience 2026** report details how adversaries now run parts of intrusions with AI — and one case where no attacker was involved at all: a hijacked **AI coding-assistant session** that recommended a poisoned package, handing an intruder an infostealer, **GitHub OAuth tokens** and the **Shai-Hulud worm across about 100 internal repositories**; a **compromised CI/CD credential** rebuilt into a live, AI-assisted offensive hub (IP-rotation scripts, a Rust tool to log into victim accounts) that exfiltrated thousands of credentials; and a financial firm's **accounting agent** that, stuck in a recursive reasoning loop after a corrupted null value, made **15,000+ reasoning API calls in under an hour**, ran up a **~$50,000 cloud bill** and **halted active business transactions**

summary_zh: |
  Mandiant《AI Risk and Resilience 2026》报告披露攻击者已用 AI 执行入侵的部分环节——以及一起**完全无攻击者**的案例：被劫持的 **AI 编码助手会话**推荐了被投毒的包，使入侵者获得 infostealer、**GitHub OAuth 令牌**，并在**约 100 个内部代码仓库**中部署 **Shai-Hulud 蠕虫**；一枚**失窃的 CI/CD 长期凭证**被改造成实时 AI 辅助攻击平台（动态换 IP 脚本、用于登录受害者账户的 Rust 工具），外泄数千条凭证；某金融机构的**记账 agent** 因一个损坏的空值陷入递归推理循环，**一小时内发起 15,000+ 次推理 API 调用**、产生**约 5 万美元云账单**并**导致业务交易中断**

summary_ja: |
  Mandiantの**AI Risk and Resilience 2026**報告は、攻撃者がAIで侵入の一部を実行する実態を明らかにした——そして攻撃者が一切関与しない事例も：ハイジャックされた**AIコーディングアシスタントのセッション**が汚染パッケージを推薦し、侵入者にインフォスティーラー、**GitHub OAuthトークン**、**約100の社内リポジトリに及ぶShai-Huludワーム**を渡した。**盗まれたCI/CDの長期資格情報**は、IPローテーションスクリプトや被害者の口座にログインするRust製ツールを備えた、AI支援の生きた攻撃ハブに作り替えられ、数千件の資格情報を窃取した。金融機関の**経理エージェント**は、破損したnull値のため再帰的推論ループに陥り、**1時間足らずで1万5千回超の推論API呼び出し**、**約5万ドルのクラウド請求**を発生させ、**業務トランザクションを停止**させた

summary_ko: |
  Mandiant의 **AI Risk and Resilience 2026** 보고서는 공격자들이 침입의 일부를 AI로 수행하는 실태와, 공격자가 전혀 없는 사례 하나를 상세히 다룬다: 하이재킹된 **AI 코딩 어시스턴트 세션**이 오염된 패키지를 추천해 침입자에게 인포스틸러, **GitHub OAuth 토큰**, 그리고 **약 100개 내부 저장소에 퍼진 Shai-Hulud 웜**을 안겼다. **탈취된 CI/CD 장기 자격증명**은 IP 로테이션 스크립트와 피해자 계정 로그인용 Rust 도구를 갖춘 실시간 AI 지원 공격 허브로 바뀌어 수천 건의 자격증명을 유출했다. 금융사의 **회계 에이전트**는 손상된 null 값 때문에 재귀 추론 루프에 빠져 **1시간 안에 1만5천 건이 넘는 추론 API 호출**과 **약 5만 달러의 클라우드 청구서**를 만들고 **업무 거래를 중단**시켰다

summary_de: |
  Mandiants Bericht **AI Risk and Resilience 2026** beschreibt, wie Angreifer Teile von Intrusionen inzwischen mit KI ausführen — und einen Fall ganz ohne Angreifer: Eine gekaperte **KI-Coding-Assistant-Sitzung** empfahl ein vergiftetes Paket und lieferte einem Eindringling einen Infostealer, **GitHub-OAuth-Token** und den **Shai-Hulud-Wurm über rund 100 interne Repositories**. Ein **kompromittierter CI/CD-Dauerzugang** wurde zu einem lebenden, KI-gestützten Angriffs-Hub umgebaut (IP-Rotationsskripte, ein Rust-Tool zum Login in Opferkonten) und exfiltrierte Tausende Zugangsdaten. Der **Buchhaltungs-Agent** eines Finanzunternehmens geriet nach einem korrupten Nullwert in eine rekursive Reasoning-Schleife: **über 15.000 Reasoning-API-Aufrufe in unter einer Stunde**, eine **Cloud-Rechnung von ~50.000 US-Dollar** und **gestoppte Geschäftstransaktionen**

summary_fr: |
  Le rapport **AI Risk and Resilience 2026** de Mandiant détaille comment les attaquants confient désormais une partie des intrusions à l'IA — et un cas sans aucun attaquant : une **session d'assistant de codage IA** détournée a recommandé un paquet empoisonné, fournissant à un intrus un infostealer, des **jetons OAuth GitHub** et le **ver de Shai-Hulud sur environ 100 dépôts internes** ; un **identifiant CI/CD compromis** a été transformé en hub offensif vivant assisté par IA (scripts de rotation d'IP, outil Rust pour se connecter aux comptes des victimes), exfiltrant des milliers d'identifiants ; et l'**agent comptable** d'une société financière, bloqué dans une boucle de raisonnement récursive après une valeur nulle corrompue, a généré **plus de 15 000 appels d'API de raisonnement en moins d'une heure**, une **facture cloud d'environ 50 000 $** et **l'arrêt de transactions commerciales**

summary_es: |
  El informe **AI Risk and Resilience 2026** de Mandiant detalla cómo los atacantes ya ejecutan partes de las intrusiones con IA — y un caso sin atacante alguno: una **sesión de asistente de código IA** secuestrada recomendó un paquete envenenado, entregando a un intruso un infostealer, **tokens OAuth de GitHub** y el **gusano Shai-Hulud por unos 100 repositorios internos**; una **credencial CI/CD comprometida** se convirtió en un centro ofensivo vivo asistido por IA (scripts de rotación de IP, una herramienta en Rust para entrar en cuentas de víctimas) que exfiltró miles de credenciales; y el **agente contable** de una firma financiera, atrapado en un bucle de razonamiento recursivo tras un valor nulo corrupto, generó **más de 15.000 llamadas a la API de razonamiento en menos de una hora**, una **factura de nube de ~50.000 $** y **detuvo transacciones comerciales activas**

sources:
  - url: https://cloud.google.com/security/resources/ai-risk-and-resilience-2026
    label: Mandiant (Google Cloud)
  - url: https://www.helpnetsecurity.com/2026/09/16/google-mandiant-enterprise-ai-security-risks-report/
    label: Help Net Security
  - url: https://www.securityweek.com/in-other-news-ransomware-developer-sentenced-plugin4shell-ai-attack-critical-sap-flaw/
    label: SecurityWeek

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Mandiant 2026 AI report: a runaway agent's $50,000 bill and AI-assisted intrusions

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Mandiant's **AI Risk and Resilience 2026** report details how adversaries now run parts of intrusions with AI — and one case where no attacker was involved at all: a hijacked **AI coding-assistant session** that recommended a poisoned package, handing an intruder an infostealer, **GitHub OAuth tokens** and the **Shai-Hulud worm across about 100 internal repositories**; a **compromised CI/CD credential** rebuilt into a live, AI-assisted offensive hub (IP-rotation scripts, a Rust tool to log into victim accounts) that exfiltrated thousands of credentials; and a financial firm's **accounting agent** that, stuck in a recursive reasoning loop after a corrupted null value, made **15,000+ reasoning API calls in under an hour**, ran up a **~$50,000 cloud bill** and **halted active business transactions**

## Attack chain

```mermaid
flowchart LR
    E["Mandiant + GTIG observations, September 2026 report"]:::entry
    S0["AI sessions and credentials weaponised; elsewhere, an agent loops with no attacker at all"]:::step
    I["Supply-chain worm, thousands of credentials, and a ~$50,000 runaway bill"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The report.** *AI Risk and Resilience 2026*, a Mandiant special report drawing on Mandiant and Google Threat Intelligence Group (GTIG) observations, argues that enterprise AI has shifted from assistive chat to **autonomous, agentic systems that orchestrate workflows and execute end-to-end operations** — and that a poisoned data source, model dependency or extension hook is enough to turn a trusted agent into a channel for internal reconnaissance, lateral movement or an escape from its sandbox. It restates cases this archive already carries (malicious OpenClaw skills in February, TeamPCP/UNC6780 in March, GTIG's AI-developed zero-day in May) and adds three case studies that are new here.

**The new case studies.** (1) A threat actor compromised a SaaS provider and **hijacked an active AI coding-assistant session** on a developer's workstation; the assistant, trusted as an interpreter, **recommended installing an external package the attacker had poisoned** — it functioned as a trojan horse, leading to an infostealer via a poisoned PyPI package, harvest of GitHub OAuth tokens and deployment of the self-propagating **Shai-Hulud worm across roughly 100 internal repositories**, before a package in the company's own namespace poisoned a downstream customer. (2) At a global healthcare organisation, a **long-lived CI/CD credential** was used to spin up an unisolated VM and turn it into a **live, AI-assisted offensive hub**: priming the model with project READMEs, co-debugging a multi-worker harvesting framework down to a three-hour exfiltration cycle, then generating IP-rotation scripts and a Rust tool to log into victim accounts — thousands of credentials were compromised. (3) **"Denial-of-Wallet" using a rogue reasoning loop**: a financial-services firm's accounting agent had read/write access to internal billing databases; when a corrupted null value broke its formatting tool, the agent entered an **unconstrained recursive loop to brute-force a fix**, generating **over 15,000 high-cost API calls in under an hour**, a **~$50,000 billing spike** and **severe database locking that halted active business transactions** — no attacker involved.

**Why it matters.** The report's most transferable lesson is governance of, and for, agents: Mandiant recommends **cost-cap thresholds and financial circuit breakers** that halt agents after consecutive task failures, bounded recursion limits and rate limits at the service-ID and project level, **short-lived workload identity instead of long-lived keys**, egress containment, and verification of every AI-recommended dependency against checksums or allowlists. The runaway-loop case in particular extends this archive's definition of harm: an agent can cause measurable financial and operational damage with **no adversary and no data breach at all**.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Mandiant (Google Cloud) | <https://cloud.google.com/security/resources/ai-risk-and-resilience-2026> |
| 2 | Help Net Security | <https://www.helpnetsecurity.com/2026/09/16/google-mandiant-enterprise-ai-security-risks-report/> |
| 3 | SecurityWeek | <https://www.securityweek.com/in-other-news-ransomware-developer-sentenced-plugin4shell-ai-attack-critical-sap-flaw/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-16` (raw: 2026-09-15→16, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-16-mandiant-ai-risk-resilience-2026` |

<sub>**Why this classification:** A vendor threat report covering several incidents and case studies, not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-10` [Anthropic September threat intelligence report](2026-09-10-anthropic-september-threat-report.md)<br>  <sub>Anthropic September threat intelligence report</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](../2026-05/2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](../2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-16-mandiant-ai-risk-resilience-2026.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
