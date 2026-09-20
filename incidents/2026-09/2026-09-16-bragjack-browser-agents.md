---
id: 2026-09-16-bragjack-browser-agents
title: "BragJack: one browser extension hijacks the AI agents in five major browsers"
title_zh: "BragJack：一个浏览器扩展即可劫持五款主流浏览器的内置 AI agent"
title_ja: "BragJack：拡張機能1つで5大ブラウザの内蔵AIエージェントを乗っ取り"
title_ko: "BragJack: 확장 프로그램 하나로 5개 브라우저 내장 AI 에이전트 탈취"
title_de: "BragJack: Eine Browser-Erweiterung entführt die KI-Agenten in fünf Browsern"
title_fr: "BragJack : une seule extension détourne les agents IA de cinq navigateurs"
title_es: "BragJack: una sola extensión secuestra los agentes de IA de cinco navegadores"
date: 2026-09-16
date_raw: "2026-09-16"
date_precision: day

kind: vulnerability
type: [SUPPLY, IPI]
severity: high
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Forever Security's **Gal Weizman** discloses **BragJack**, a technique in which **one ordinary browser extension** — using nothing but normal content-script and **declarativeNetRequest** permissions — hijacks the built-in AI agents of **five Chromium browsers**: **Gemini Live in Chrome, Copilot in Edge, Opera Neon, Perplexity Comet and Claude in Chrome**. Instead of hiding instructions in content, the extension **takes over the trusted prompt channel** between the vendor's site and the in-browser agent — the researchers call it **"prompt forcing"** — so model-level safety filters never get a chance to matter. Google fixed it as **CVE-2026-0628** (CVSS 8.8, Chrome 143.0.7499.192/.193) and Microsoft as **CVE-2026-55945** (medium, Edge before 150.0.4078.48); Comet saw the broadest impact, and Anthropic paid a bounty for the Claude in Chrome case. It is a proof of concept — **no in-the-wild attacks** — but a malicious extension must merely be installed first, not clicked

summary_zh: |
  Forever Security 研究员 **Gal Weizman** 披露 **BragJack**：**一个普通浏览器扩展**——仅使用正常的 content script 与 **declarativeNetRequest** 权限——即可劫持**五款 Chromium 浏览器的内置 AI agent**：**Chrome 的 Gemini Live、Edge 的 Copilot、Opera Neon、Perplexity Comet 与 Claude in Chrome**。它不在内容里藏指令，而是**夺取厂商站点与浏览器内 agent 之间的可信指令通道**——研究者称之为**「prompt forcing」（提示强塞）**——使模型层的安全过滤根本来不及起作用。Google 记为 **CVE-2026-0628**（CVSS 8.8，Chrome 143.0.7499.192/.193 修复）、微软记为 **CVE-2026-55945**（中危，Edge 150.0.4078.48 之前版本）；Comet 受影响面最广，Anthropic 也为 Claude in Chrome 一案支付赏金。该攻击为概念验证、**无在野利用**——但恶意扩展只需被安装、无需点击

summary_ja: |
  Forever Securityの**Gal Weizman**氏は、**ごく普通のブラウザ拡張機能1つ**——通常のcontent scriptと**declarativeNetRequest**権限だけで——が**5つのChromium系ブラウザの内蔵AIエージェント**（**ChromeのGemini、EdgeのCopilot、Opera Neon、Perplexity Comet、Claude in Chrome**）を乗っ取る「**BragJack**」を公表した。コンテンツに指示を隠すのではなく、ベンダーサイトとブラウザ内エージェントの間の**信頼されたプロンプト経路そのものを奪う**——研究チームはこれを**「プロンプト・フォーシング」**と呼ぶ——ため、モデル側の安全フィルタは意味を持たない。Googleは**CVE-2026-0628**（CVSS 8.8、Chrome 143.0.7499.192/.193で修正）、Microsoftは**CVE-2026-55945**（中、Edge 150.0.4078.48未満）として修正。影響が最も広かったのはCometで、AnthropicはClaude in Chromeの件に報奨金を支払った。概念実証であり**実被害はない**が、悪意ある拡張は「インストールされていれば」よく、クリックは不要

summary_ko: |
  Forever Security의 **Gal Weizman**이 **BragJack**을 공개했다: **평범한 브라우저 확장 프로그램 하나**가 — 일반적인 content script와 **declarativeNetRequest** 권한만으로 — **5개 Chromium 브라우저의 내장 AI 에이전트**(**Chrome의 Gemini, Edge의 Copilot, Opera Neon, Perplexity Comet, Claude in Chrome**)를 탈취한다. 콘텐츠에 지시를 숨기는 대신 **벤더 사이트와 브라우저 내 에이전트 사이의 신뢰된 프롬프트 채널 자체를 장악**한다 — 연구진은 이를 **"프롬프트 포싱"**이라 부른다 — 따라서 모델 수준 안전 필터는 작동할 기회조차 없다. Google은 **CVE-2026-0628**(CVSS 8.8, Chrome 143.0.7499.192/.193에서 수정), 마이크로소프트는 **CVE-2026-55945**(중간, Edge 150.0.4078.48 이전)로 수정했다. 영향 범위가 가장 넓은 것은 Comet이었고, Anthropic은 Claude in Chrome 사례에 포상금을 지급했다. 개념 증명이며 **실제 악용은 없지만**, 악성 확장이 설치만 되어 있으면 되고 클릭은 필요 없다

summary_de: |
  Forever Securitys **Gal Weizman** veröffentlicht **BragJack**: **eine gewöhnliche Browser-Erweiterung** — allein mit normalen Content-Script- und **declarativeNetRequest**-Rechten — entführt die integrierten KI-Agenten von **fünf Chromium-Browsern**: **Gemini in Chrome, Copilot in Edge, Opera Neon, Perplexity Comet und Claude in Chrome**. Statt Anweisungen in Inhalten zu verstecken, **übernimmt die Erweiterung den vertrauenswürdigen Prompt-Kanal** zwischen der Herstellerseite und dem Agenten im Browser — die Forscher nennen das **„Prompt Forcing"** —, sodass Sicherheitsfilter auf Modellebene gar nicht erst greifen. Google behebt es als **CVE-2026-0628** (CVSS 8.8, Chrome 143.0.7499.192/.193), Microsoft als **CVE-2026-55945** (mittel, Edge vor 150.0.4078.48); Comet war am breitesten betroffen, und Anthropic zahlte ein Kopfgeld für den Claude-in-Chrome-Fall. Ein Proof of Concept — **keine Ausnutzung in freier Wildbahn** — bei dem die schädliche Erweiterung lediglich installiert sein muss, ohne Klick

summary_fr: |
  **Gal Weizman**, de Forever Security, divulgue **BragJack** : **une simple extension de navigateur** — avec de banales autorisations de content script et de **declarativeNetRequest** — détourne les agents IA intégrés de **cinq navigateurs Chromium** : **Gemini dans Chrome, Copilot dans Edge, Opera Neon, Perplexity Comet et Claude in Chrome**. Plutôt que de cacher des instructions dans le contenu, l'extension **s'empare du canal de prompt de confiance** entre le site de l'éditeur et l'agent du navigateur — les chercheurs parlent de **« prompt forcing »** — si bien que les filtres de sécurité du modèle n'entrent jamais en jeu. Google l'a corrigé sous **CVE-2026-0628** (CVSS 8.8, Chrome 143.0.7499.192/.193), Microsoft sous **CVE-2026-55945** (moyen, Edge avant 150.0.4078.48) ; Comet a été le plus touché et Anthropic a versé une prime pour le cas Claude in Chrome. Une preuve de concept — **aucune exploitation observée** — où l'extension malveillante doit simplement être installée, sans clic

summary_es: |
  **Gal Weizman**, de Forever Security, divulga **BragJack**: **una extensión de navegador corriente** — solo con permisos normales de content script y **declarativeNetRequest** — secuestra los agentes de IA integrados de **cinco navegadores Chromium**: **Gemini en Chrome, Copilot en Edge, Opera Neon, Perplexity Comet y Claude in Chrome**. En vez de esconder instrucciones en el contenido, la extensión **toma el canal de prompts de confianza** entre el sitio del fabricante y el agente del navegador — los investigadores lo llaman **«prompt forcing»** —, de modo que los filtros de seguridad del modelo nunca llegan a actuar. Google lo corrigió como **CVE-2026-0628** (CVSS 8.8, Chrome 143.0.7499.192/.193) y Microsoft como **CVE-2026-55945** (medio, Edge anterior a 150.0.4078.48); Comet fue el más afectado y Anthropic pagó una recompensa por el caso de Claude in Chrome. Es una prueba de concepto — **sin explotación real** — y a la extensión maliciosa le basta con estar instalada, sin clics

sources:
  - url: https://forever.security/blog/bragjack-hijacking-5-browsers-via-built-in-ai-assistants
    label: Forever Security
  - url: https://forever.security/blog/bragjack-attack-hijacks-every-browser-agent
    label: Forever Security (technical)
  - url: https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/
    label: BleepingComputer
  - url: https://cybersecuritynews.com/bragjack-ai-agent-hijacking/
    label: Cybersecurity News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# BragJack: one browser extension hijacks the AI agents in five major browsers

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Forever Security's **Gal Weizman** discloses **BragJack**, a technique in which **one ordinary browser extension** — using nothing but normal content-script and **declarativeNetRequest** permissions — hijacks the built-in AI agents of **five Chromium browsers**: **Gemini Live in Chrome, Copilot in Edge, Opera Neon, Perplexity Comet and Claude in Chrome**. Instead of hiding instructions in content, the extension **takes over the trusted prompt channel** between the vendor's site and the in-browser agent — the researchers call it **"prompt forcing"** — so model-level safety filters never get a chance to matter. Google fixed it as **CVE-2026-0628** (CVSS 8.8, Chrome 143.0.7499.192/.193) and Microsoft as **CVE-2026-55945** (medium, Edge before 150.0.4078.48); Comet saw the broadest impact, and Anthropic paid a bounty for the Claude in Chrome case. It is a proof of concept — **no in-the-wild attacks** — but a malicious extension must merely be installed first, not clicked

## Attack chain

```mermaid
flowchart LR
    E["An ordinary extension: content scripts + DNR rules"]:::entry
    S0["It replaces the trusted channel between the vendor site and the in-browser agent"]:::step
    I["The agent executes attacker prompts: local files, screenshots, mic/camera, actions on logged-in sites"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The technique.** BragJack exploits the architecture that connects an AI agent's "brain" — a model hosted on a **vendor-controlled website** — to its "body" inside the browser, which can read pages and operate sites. Every browser agent trusts certain origins to deliver instructions; the extension does not need to defeat the model's guardrails, it only has to **speak through a channel the agent already trusts**. Using content scripts plus **declarativeNetRequest** rules — permissions ad blockers request every day — Weizman replaced or injected resources on those trusted origins, then issued his own prompts, complete with timing and follow-ups. He calls the result **"prompt forcing"**, and the distinction matters: with **prompt injection** the attacker hides instructions in content the model reads, while here the attacker **controls the prompt itself**, abusing authorization and message-channel trust before the model evaluates intent — so model-level safety filters cannot correct the isolation failure.

**What each browser allowed.** In **Chrome**, Google blocked content-script injection into Gemini's embedded web app — but the DNR rules still intercepted resources loaded inside the privileged WebView, and by replacing a legitimate JavaScript resource the researchers ran code in Gemini's trusted context: local file reads, screenshots, profile information and **camera and microphone access** (Google: **CVE-2026-0628**, 8.8, fixed in **Chrome 143.0.7499.192/.193**). **Perplexity Comet** had the broadest impact: its agent trusted several Perplexity origins, including an unprotected testing domain, enabling **browsing-history access, screenshots, profile leaks, local-file reads and autonomous actions on authenticated websites** — Weizman demonstrated forcing the agent to summarise a victim's emails and send the results to another address. On **Opera Neon**, code on opera.com could send arbitrary agent prompts. **Microsoft Edge** needed a more complex chain — a marketing page that could place prompts into Copilot, plus a race condition between its "Think" and "Do" modes (**CVE-2026-55945**, medium, fixed before **150.0.4078.48**). **Claude in Chrome** was an extension-on-extension case: a Claude marketing page permitted to pass prompts to the side panel, plus click-through debugger privileges let one extension drive another; Anthropic acknowledged the report and paid a bounty.

**Status and why it matters.** The attack is a proof of concept: **no in-the-wild exploitation** was reported, the vendors paid **more than $20,000** in combined bounties (individual awards ranged from $600 to $7,000), and the malicious extension must be **installed first** — "zero-click" describes what happens afterwards, not an internet-only compromise. But BragJack is the first systematic demonstration that the **command-and-control channel of in-browser agents** is itself an attack surface: any extension with the permissions users grant without a second thought can usurp the vendor's authority over its agent. The practical guidance is extension hygiene — allowlists, tighter host and DNR permissions, scrutiny of debugger access, removing what is not needed, and treating agent activity as its own telemetry stream, correlated with file, microphone, camera and account access.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Forever Security | <https://forever.security/blog/bragjack-hijacking-5-browsers-via-built-in-ai-assistants> |
| 2 | Forever Security (technical) | <https://forever.security/blog/bragjack-attack-hijacks-every-browser-agent> |
| 3 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/bragjack-attacks-hijack-ai-browser-agents-through-malicious-extensions/> |
| 4 | Cybersecurity News | <https://cybersecuritynews.com/bragjack-ai-agent-hijacking/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-16` (raw: 2026-09-16, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **High** `high` |
| Confidence | **B** — research organisation or mainstream media, with checkable detail |
| Real harm | no |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-16-bragjack-browser-agents` |

<sub>**Why this classification:** Coordinated disclosure by a research firm; no exploitation in the wild and no real-world harm, so `real_harm: false`. Rated `high`: a capability demonstration of significance — agent hijack across five browsers using ordinary extension permissions, with CVSS 8.8 on the Chrome flaw. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-09-17` [Plugin4Shell: a zero-click RCE chain hits four AI coding agents](2026-09-17-plugin4shell-coding-agents.md)<br>  <sub>Plugin4Shell: a zero-click RCE chain hits four AI coding agents</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-16-bragjack-browser-agents.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
