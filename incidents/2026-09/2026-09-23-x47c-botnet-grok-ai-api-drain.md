---
id: 2026-09-23-x47c-botnet-grok-ai-api-drain
title: "x47.c: a Windows botnet-for-sale that drains AI API credit and uses Grok to choose how it hides"
title_zh: "x47.c：一款在售的 Windows 僵尸网络，抽干 AI API 额度，并用 Grok 决定如何隐藏"
title_ja: "x47.c：AI APIのクレジットを枯渇させ、Grokを使って隠れ方を選ぶ、販売中のWindowsボットネット"
title_ko: "x47.c: AI API 크레딧을 소진시키고 Grok으로 은신 방법을 고르는, 판매 중인 Windows 봇넷"
title_de: "x47.c: ein zum Verkauf stehendes Windows-Botnetz, das AI-API-Guthaben leert und mit Grok wählt, wie es sich versteckt"
title_fr: "x47.c : un botnet Windows en vente qui vide le crédit d'API d'IA et se sert de Grok pour choisir comment se cacher"
title_es: "x47.c: un botnet de Windows a la venta que agota el crédito de API de IA y usa Grok para elegir cómo esconderse"
date: 2026-09-23
date_raw: "2026-09-23 (Qrator)"
date_precision: day

kind: incident
type: [WEAPON, CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Qrator Research Labs documents x47.c, a Windows botnet advertised for sale (base $200, full package $950) by a threat actor called WraithTools, whose command panel offers 18 DDoS methods, credential theft, SOCKS5 proxying — and two AI-driven features.** The first is an *"AI API drain"* (a denial-of-wallet attack): the operator supplies a valid OpenAI, xAI or compatible API key and the botnet sends *"repeated billable requests straight to the provider,"* so — as Qrator notes — *"the victim's website can stay up while the AI features behind it run out of credit,"* and filtering the site's own traffic does not stop it. The second is an *"AI Stealth"* module that *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions,"* reporting Defender exclusions and persistence repair, with local fallbacks when the model call fails. The stealer also lifts browser passwords, cookies, Discord and AI-site tokens. Qrator's findings are drawn from the seller's **advertisement, technical documentation and panel screenshots** (an ad dated 3 August), not from an observed deployment. Recorded `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — unlike [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), where an LLM panel is the autonomous command-and-control brain, here the model is an *optional* module (action selection and wallet-draining), so the AI role is assistive rather than the core.

summary_zh: |
  **Qrator 研究实验室记录了 x47.c——一款由名为 WraithTools 的威胁行为者公开兜售（基础版 200 美元、全包 950 美元）的 Windows 僵尸网络，其控制面板提供 18 种 DDoS 手法、凭据窃取、SOCKS5 代理，以及两项由 AI 驱动的功能。** 其一是*「AI API 抽血」*（一种"钱包耗尽"攻击）：操作者填入一个有效的 OpenAI、xAI 或兼容 API 密钥，僵尸网络便*「向服务商直接发送反复计费的请求」*，于是——如 Qrator 所述——*「受害者网站可以照常运行，而其背后的 AI 功能却把额度耗光」*，在网站侧过滤流量也拦不住。其二是*「AI 隐身」*模块，它*「用 xAI 的 Grok 评估被感染主机，并从预定义的持久化与隐藏动作中做选择」*，会回报 Defender 排除项与持久化修复，模型调用失败时有本地兜底。窃取器还会取走浏览器口令、cookie、Discord 与 AI 站点令牌。Qrator 的结论取自卖家的**广告、技术文档与面板截图**（一则广告日期为 8 月 3 日），而非观测到的实际部署。本条记为 `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false`——与 [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md)（LLM 面板是自主的指挥控制大脑）不同，这里模型是一个*可选*模块（动作选择与钱包抽血），AI 角色是辅助而非核心。

summary_ja: |
  **Qrator Research Labsは、x47.cを記録した。WraithToolsと名乗る脅威アクターが販売する（基本200ドル、フルパッケージ950ドル）Windowsボットネットで、そのコマンドパネルは18のDDoS手法、認証情報窃取、SOCKS5プロキシ、そして2つのAI駆動機能を備える。** 1つ目は*「AI API drain」*（デニアル・オブ・ウォレット攻撃）で、運用者が有効なOpenAI・xAI・互換APIキーを入力すると、ボットネットが*「課金対象のリクエストをプロバイダーへ直接繰り返し送る」*。Qratorいわく*「被害者のサイトは動いたままでも、その背後のAI機能がクレジットを使い果たす」*ため、サイト側のトラフィック遮断では止められない。2つ目は*「AI Stealth」*モジュールで、*「xAIのGrokを使って感染ホストを評価し、事前定義された永続化・隠蔽アクションから選ぶ」*。窃取器はブラウザのパスワード、Cookie、Discordトークン、AIサイトのトークンも奪う。Qratorの分析は、観測された展開ではなく、売り手の**広告・技術文書・パネルのスクリーンショット**（8月3日付の広告）に基づく。`incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false`——LLMパネルが自律的なC2の頭脳である[ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md)とは異なり、ここではモデルは*任意の*モジュール（アクション選択とウォレット枯渇）であり、AIの役割は中核ではなく補助である

summary_ko: |
  **Qrator Research Labs가 x47.c를 기록했다. WraithTools라는 위협 행위자가 판매하는(기본 200달러, 풀패키지 950달러) Windows 봇넷으로, 명령 패널은 18가지 DDoS 기법, 자격증명 절취, SOCKS5 프록시, 그리고 두 가지 AI 기반 기능을 제공한다.** 첫째는 *"AI API drain"*(월렛 소진 공격)으로, 운영자가 유효한 OpenAI·xAI·호환 API 키를 넣으면 봇넷이 *"과금되는 요청을 공급자에게 직접 반복 전송"*한다. Qrator에 따르면 *"피해자의 사이트는 계속 동작하는데 그 뒤의 AI 기능이 크레딧을 소진"*하므로 사이트 측 트래픽 필터링으로는 막을 수 없다. 둘째는 *"AI Stealth"* 모듈로, *"xAI의 Grok을 사용해 감염 호스트를 평가하고 사전 정의된 지속·은닉 동작 중에서 선택"*한다. 스틸러는 브라우저 비밀번호·쿠키·Discord·AI 사이트 토큰도 가져간다. Qrator의 분석은 관측된 배포가 아니라 판매자의 **광고·기술 문서·패널 스크린샷**(8월 3일자 광고)에 근거한다. `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — LLM 패널이 자율 C2 두뇌인 [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md)와 달리, 여기서 모델은 *선택적* 모듈(동작 선택과 월렛 소진)이라 AI 역할이 핵심이 아니라 보조다

summary_de: |
  **Qrator Research Labs dokumentiert x47.c, ein zum Verkauf angebotenes Windows-Botnetz (Basis 200 $, Vollpaket 950 $) eines Akteurs namens WraithTools, dessen Steuerpanel 18 DDoS-Methoden, Diebstahl von Zugangsdaten, SOCKS5-Proxying und zwei KI-gesteuerte Funktionen bietet.** Die erste ist ein *"AI API drain"* (Denial-of-Wallet): Der Betreiber hinterlegt einen gültigen OpenAI-, xAI- oder kompatiblen API-Schlüssel, und das Botnetz sendet *"repeated billable requests straight to the provider"*, sodass laut Qrator *"the victim's website can stay up while the AI features behind it run out of credit"* — Filtern am Website-Verkehr hilft nicht. Die zweite ist ein *"AI Stealth"*-Modul, das *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions."* Der Stealer greift auch Browser-Passwörter, Cookies sowie Discord- und AI-Site-Token ab. Qrators Erkenntnisse stammen aus **Werbung, technischer Dokumentation und Panel-Screenshots** des Verkäufers (Anzeige vom 3. August), nicht aus einer beobachteten Bereitstellung. Verzeichnet als `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — anders als bei [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), wo ein LLM-Panel das autonome C2-Gehirn ist, ist das Modell hier ein *optionales* Modul, die KI-Rolle also unterstützend statt zentral

summary_fr: |
  **Qrator Research Labs documente x47.c, un botnet Windows mis en vente (base 200 $, pack complet 950 $) par un acteur nommé WraithTools, dont le panneau de commande offre 18 méthodes de DDoS, du vol d'identifiants, du proxy SOCKS5 et deux fonctions pilotées par IA.** La première est un *"AI API drain"* (déni de portefeuille) : l'opérateur fournit une clé d'API OpenAI, xAI ou compatible valide, et le botnet envoie *"repeated billable requests straight to the provider"*, si bien que, selon Qrator, *"the victim's website can stay up while the AI features behind it run out of credit"* — filtrer le trafic du site n'y change rien. La seconde est un module *"AI Stealth"* qui *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions."* Le voleur récupère aussi mots de passe de navigateur, cookies, jetons Discord et de sites d'IA. Les conclusions de Qrator proviennent de **l'annonce, de la documentation technique et de captures du panneau** du vendeur (annonce datée du 3 août), non d'un déploiement observé. Enregistré `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — contrairement à [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), où un panel de LLM est le cerveau C2 autonome, le modèle n'est ici qu'un module *optionnel*, le rôle de l'IA étant accessoire et non central

summary_es: |
  **Qrator Research Labs documenta x47.c, un botnet de Windows puesto a la venta (base 200 $, paquete completo 950 $) por un actor llamado WraithTools, cuyo panel de mando ofrece 18 métodos de DDoS, robo de credenciales, proxy SOCKS5 y dos funciones impulsadas por IA.** La primera es un *"AI API drain"* (denegación de cartera): el operador aporta una clave de API válida de OpenAI, xAI o compatible y el botnet envía *"repeated billable requests straight to the provider"*, de modo que, según Qrator, *"the victim's website can stay up while the AI features behind it run out of credit"* — filtrar el tráfico del propio sitio no lo detiene. La segunda es un módulo *"AI Stealth"* que *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions."* El ladrón también toma contraseñas de navegador, cookies y tokens de Discord y de sitios de IA. Los hallazgos de Qrator provienen del **anuncio, la documentación técnica y capturas del panel** del vendedor (un anuncio del 3 de agosto), no de un despliegue observado. Registrado `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — a diferencia de [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), donde un panel de LLM es el cerebro autónomo de C2, aquí el modelo es un módulo *opcional*, por lo que el papel de la IA es auxiliar y no central

sources:
  - url: https://qrator.net/blog/details/x47.c-botnet
    label: Qrator Research Labs
  - url: https://www.securityweek.com/new-x47-c-windows-botnet-weaponizes-xai-grok-ai-api-draining/
    label: SecurityWeek
  - url: https://www.infosecurity-magazine.com/news/x47c-botnet-ai-api-draining-18/
    label: Infosecurity Magazine
disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.21"
---

# x47.c: a Windows botnet-for-sale that drains AI API credit and uses Grok to choose how it hides

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**Qrator Research Labs documents x47.c, a Windows botnet advertised for sale (base $200, full package $950) by a threat actor called WraithTools, whose command panel offers 18 DDoS methods, credential theft, SOCKS5 proxying — and two AI-driven features.** The first is an *"AI API drain"* (a denial-of-wallet attack): the operator supplies a valid OpenAI, xAI or compatible API key and the botnet sends *"repeated billable requests straight to the provider,"* so — as Qrator notes — *"the victim's website can stay up while the AI features behind it run out of credit,"* and filtering the site's own traffic does not stop it. The second is an *"AI Stealth"* module that *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions,"* reporting Defender exclusions and persistence repair, with local fallbacks when the model call fails. The stealer also lifts browser passwords, cookies, Discord and AI-site tokens. Qrator's findings are drawn from the seller's **advertisement, technical documentation and panel screenshots** (an ad dated 3 August), not from an observed deployment. Recorded `incident` / `WEAPON` + `CRED` / `medium` / `real_harm: false` — unlike [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), where an LLM panel is the autonomous command-and-control brain, here the model is an *optional* module (action selection and wallet-draining), so the AI role is assistive rather than the core.

## Attack chain

```mermaid
flowchart LR
    E["WraithTools sells x47.c ($200-$950);<br/>operator runs a C&C panel"]:::entry
    S1["AI API drain: operator's stolen/valid OpenAI/xAI key<br/>-> repeated billable calls to the provider (denial-of-wallet)"]:::step
    S2["AI Stealth: Grok assesses the host and picks<br/>predefined persistence / Defender-exclusion actions"]:::step
    I["Victim AI credit drained; browser, Discord and<br/>AI-site credentials stolen; hosts relayed via SOCKS5"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What it is.** In a report published on **23 September 2026**, Qrator Research Labs describes **x47.c**, a Windows botnet offered for sale by an actor using the handle **WraithTools**. The command-and-control panel bundles bot management, fast-flux configuration, infostealer logs, proxies and DDoS. Qrator's analysis is *"drawn from the seller's advertisement, technical documentation, panel screenshots and follow-up messages"* — an August 3 advertisement priced it from **$200 to $950**, the top package adding credential theft, proxying and AI-assisted persistence.

**The AI API drain (denial-of-wallet).** The panel's *"AI API drain"* mode takes a valid API key for **OpenAI, xAI or a compatible chat API** and *"sends repeated billable requests straight to the provider,"* which OWASP calls **denial of wallet (DoW)**. Because the requests bypass the victim's own application, *"the victim's website can stay up while the AI features behind it run out of credit,"* and filtering traffic at the website will not stop them. The seller pitched it against chatbots, AI-connected CMSes, trading bots and scanners — *"including as a service to use against competitors"* — and pointed to automatic top-ups as a way to keep charges accruing. Qrator notes the botnet's stealer lists AI-site tokens among its targets, though the documentation does not show them being converted into keys for the drain command.

**The Grok-driven stealth module.** An *"AI Stealth"* module *"uses xAI's Grok to assess the infected host and choose from predefined persistence and concealment actions,"* with seller-provided status messages describing persistence repair and Windows Defender exclusions and *"local fallbacks when model calls fail."* Beyond the AI features, the stealer targets browser passwords, cookies and Discord tokens, a SOCKS5 module turns hosts into relays, and an advertised rootkit removes rival malware. Qrator *"found no test results supporting the advertised protection-bypass modes."*

**Why it is here, and where the line is.** The archive records this on the offensive-AI-evolution thread: it is another commodity-crime datapoint where a large language model is wired into malware, and where **AI systems are themselves the target** (draining a victim's provider credit, stealing AI-site tokens). But the AI role is deliberately bounded in the grading: unlike **ClosedQuorum** (`2026-09-22`), in which a panel of LLMs *is* the autonomous command-and-control decision loop, x47.c uses a model as an **optional module** — Grok picks from a *predefined* list of persistence actions, and the drain mode is scripted request-spamming that *"anyone holding a valid key could"* run. `real_harm: false` and `medium`: Qrator documented the tool from seller materials, not from an observed deployment, so there is no confirmed victim; the grade reflects a real, in-market capability rather than a demonstrated intrusion.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Qrator Research Labs — "x47.c botnet" (23 Sep 2026) | <https://qrator.net/blog/details/x47.c-botnet> |
| 2 | SecurityWeek | <https://www.securityweek.com/new-x47-c-windows-botnet-weaponizes-xai-grok-ai-api-draining/> |
| 3 | Infosecurity Magazine | <https://www.infosecurity-magazine.com/news/x47c-botnet-ai-api-draining-18/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-23` (raw: Qrator 2026-09-23, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **Medium** `medium` |
| Confidence | **A** — Qrator's research report plus two independent outlets |
| Real harm | No — documented from seller materials; no confirmed victim |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-23-x47c-botnet-grok-ai-api-drain` |

<sub>**Why this classification:** a criminal wires an LLM into a for-sale botnet (`WEAPON`) that steals browser, Discord and AI-site credentials and drains victims' AI API credit (`CRED`). `real_harm: false` because Qrator documented it from the seller's advertisement and documentation, not an observed deployment with a confirmed victim; `medium` because the AI is an optional module (Grok picking predefined persistence actions; scripted wallet-draining) rather than the autonomous core — which is the line against [ClosedQuorum](2026-09-22-closedquorum-ai-c2-implant.md), graded `high` as the first LLM-panel autonomous C2. Dated to Qrator's report (23 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution (WEAPON)](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-22` [ClosedQuorum: the first autonomous AI C2 implant](2026-09-22-closedquorum-ai-c2-implant.md)<br>  <sub>The contrast — there the LLM panel is the autonomous C2 brain; here the model is an optional module</sub>
- `2026-09-22` [CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys](2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>Another commodity botnet whose priority loot is AI API keys</sub>
- `2026-09-22` [Gambit: three AI harnesses stole 600,000 card records from online retailers](2026-09-22-gambit-ai-agent-retail-card-theft.md)<br>  <sub>The higher-autonomy end of the same offensive-AI commodity-crime thread</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-23-x47c-botnet-grok-ai-api-drain.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
