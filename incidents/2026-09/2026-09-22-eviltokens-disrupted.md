---
id: 2026-09-22-eviltokens-disrupted
title: "EvilTokens: Microsoft dismantles an AI-powered PhaaS that compromised 12,000 inboxes"
title_zh: "EvilTokens：微软取缔一个入侵了 12,000 个邮箱的 AI 驱动钓鱼平台"
title_ja: "EvilTokens：12,000の受信トレイを侵害したAI駆動PhaaSをマイクロソフトが摘発"
title_ko: "EvilTokens: 12,000개 받은편지함을 침해한 AI 기반 PhaaS를 마이크로소프트가 차단"
title_de: "EvilTokens: Microsoft zerschlägt eine KI-gestützte PhaaS, die 12.000 Postfächer kompromittierte"
title_fr: "EvilTokens : Microsoft démantèle un PhaaS dopé à l'IA ayant compromis 12 000 boîtes mail"
title_es: "EvilTokens: Microsoft desmantela un PhaaS con IA que comprometió 12.000 buzones"
date: 2026-09-22
date_raw: "2026-09-22"
date_precision: day

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Microsoft's Digital Crimes Unit moves against EvilTokens**, a phishing-as-a-service platform that since **February 2026** powered device-code phishing campaigns and, in Microsoft's account, *"used AI at every step of the attack chain."* The platform's centrepiece was an **AI chatbot that analysed a victim's inbox to identify trusted relationships, payment authorisations and sensitive responsibilities, recommended fraud strategies and drafted impersonation messages** — Microsoft's framing: *"[AI] helped them decide who to target, who to impersonate, and how to most effectively exploit the relationship to extract as much money as possible."* The service (sold by the actor tracked **Storm-2992** at **$1,500 plus $500/month**) was used to compromise **more than 12,000 inboxes across 10,000+ organisations** in the US, Canada, the UK, Australia, India and France, mostly for business email compromise. Microsoft **seized 50 websites and disabled 150+ domains**; the UK-registered company behind it is named in pleadings, and TRM Labs supported the disruption. The AI here assists the operator — it analyses and advises rather than acting autonomously — and the platform is now dismantled; recorded `incident` / `WEAPON` / `high` / `real_harm: true` as the archive's first AI-driven PhaaS takedown

summary_zh: |
  **微软数字犯罪部门对 EvilTokens 采取行动**。这是一个自 **2026 年 2 月**起运营的钓鱼即服务（PhaaS）平台，用于设备代码钓鱼活动；按微软的说法，它*「在攻击链的每一步都使用了 AI」*。平台的核心是一个 **AI 聊天机器人：它分析受害者的收件箱以识别受信任关系、付款授权与敏感职责，推荐欺诈策略并起草冒充消息**——微软的概括是：*「（AI）帮他们决定攻击谁、冒充谁、以及如何最有效地利用这层关系榨取尽可能多的钱。」* 该服务（由被追踪为 **Storm-2992** 的行为者以 **1,500 美元 + 500 美元/月** 出售）被用于入侵**美国、加拿大、英国、澳大利亚、印度与法国的 12,000 余个邮箱、涉及 10,000 余家组织**，主要用于商务电子邮件诈骗（BEC）。微软**查封了 50 个网站、停用了 150 余个域名**；其背后的英国注册公司在法院文书中被列名，TRM Labs 为此次取缔提供了支持。此处的 AI 是辅助操作者——它做分析与建议，而非自主行动——且该平台已被捣毁；本条记为 `incident` / `WEAPON` / `high` / `real_harm: true`，是本档案首个「AI 驱动 PhaaS 被取缔」的案例

summary_ja: |
  **マイクロソフトのデジタル犯罪対策部門（DCU）がEvilTokensに打撃を与えた**。これは**2026年2月**以降、デバイスコードフィッシングを支えてきたフィッシング・アズ・ア・サービス（PhaaS）で、マイクロソフト曰く*「攻撃チェーンのあらゆる段階でAIを使用」*。中核は**被害者の受信トレイを分析して信頼関係・支払い承認・機密の職務を特定し、詐欺戦略を推奨し、なりすましメッセージを起草するAIチャットボット**——マイクロソフトの要約：*「AIは誰を標的にし、誰を装い、関係をどう悪用して最大限の金を引き出すかを決める手助けをした」*。**Storm-2992**として追跡される行為者が**1,500ドル＋月額500ドル**で販売し、**米国・カナダ・英国・豪州・インド・フランスの12,000以上の受信トレイ、10,000社超の組織**が侵害された。マイクロソフトは**50のウェブサイトを押収し、150以上のドメインを無効化**した

summary_ko: |
  **마이크로소프트 디지털 범죄 부서(DCU)가 EvilTokens를 겨냥한 작전을 단행했다.** 2026년 2월부터 디바이스 코드 피싱을 지원해 온 피싱-어즈-어-서비스(PhaaS)로, 마이크로소프트에 따르면 *"공격 체인의 모든 단계에서 AI를 사용했다."* 핵심은 **피해자의 받은편지함을 분석해 신뢰 관계·결제 승인·민감한 직무를 식별하고, 사기 전략을 추천하며, 사칭 메시지를 작성하는 AI 챗봇**이다 — 마이크로소프트의 요약: *"AI는 누구를 표적으로 하고, 누구를 사칭하며, 관계를 어떻게 악용해 최대의 돈을 빼낼지 결정하도록 도왔다."* **Storm-2992**로 추적되는 행위자가 **1,500달러 + 월 500달러**에 판매했고, **미국·캐나다·영국·호주·인도·프랑스의 12,000개 이상 받은편지함, 10,000개 이상 조직**이 침해되었다. 마이크로소프트는 **웹사이트 50개를 압수하고 150개 이상 도메인을 비활성화**했다

summary_de: |
  **Microsofts Digital Crimes Unit geht gegen EvilTokens vor** – eine Phishing-as-a-Service-Plattform, die seit **Februar 2026** Device-Code-Phishing befeuerte und laut Microsoft *„auf jeder Stufe der Angriffskette KI einsetzte"*. Herzstück war ein **KI-Chatbot, der das Postfach eines Opfers analysierte, um Vertrauensbeziehungen, Zahlungsfreigaben und sensible Zuständigkeiten zu identifizieren, Betrugsstrategien empfahl und Täuschungsnachrichten entwarf** – Microsofts Fazit: *„[KI] half ihnen zu entscheiden, wen sie angreifen, wen sie imitieren und wie sie die Beziehung am wirksamsten ausbeuten, um möglichst viel Geld zu erpressen."* Der Dienst (vom Akteur **Storm-2992** für **1.500 USD plus 500 USD/Monat** verkauft) kompromittierte **über 12.000 Postfächer in mehr als 10.000 Organisationen** in den USA, Kanada, Großbritannien, Australien, Indien und Frankreich. Microsoft **beschlagnahmte 50 Websites und deaktivierte über 150 Domains**

summary_fr: |
  **La Digital Crimes Unit de Microsoft frappe EvilTokens**, une plateforme de phishing-as-a-service qui, depuis **février 2026**, alimentait des campagnes de device code phishing et, selon Microsoft, *« utilisait l'IA à chaque étape de la chaîne d'attaque »*. Sa pièce maîtresse : un **chatbot IA qui analysait la boîte mail d'une victime pour identifier relations de confiance, autorisations de paiement et responsabilités sensibles, recommandait des stratégies de fraude et rédigeait des messages d'usurpation** — selon Microsoft, *« [l'IA] les aidait à décider qui cibler, qui usurper et comment exploiter au mieux la relation pour extorquer le maximum d'argent »*. Le service (vendu par l'acteur **Storm-2992** à **1 500 $ plus 500 $/mois**) a compromis **plus de 12 000 boîtes mail dans plus de 10 000 organisations** aux États-Unis, au Canada, au Royaume-Uni, en Australie, en Inde et en France. Microsoft a **saisi 50 sites et désactivé plus de 150 domaines**

summary_es: |
  **La Unidad de Delitos Digitales de Microsoft actúa contra EvilTokens**, una plataforma de phishing como servicio que desde **febrero de 2026** impulsaba campañas de device code phishing y, según Microsoft, *«usaba IA en cada paso de la cadena de ataque»*. Su pieza central: un **chatbot de IA que analizaba el buzón de la víctima para identificar relaciones de confianza, autorizaciones de pago y responsabilidades sensibles, recomendaba estrategias de fraude y redactaba mensajes de suplantación** — en palabras de Microsoft: *«[la IA] les ayudaba a decidir a quién atacar, a quién suplantar y cómo explotar mejor la relación para extraer el máximo dinero»*. El servicio (vendido por el actor **Storm-2992** a **1.500 $ más 500 $/mes**) comprometió **más de 12.000 buzones en más de 10.000 organizaciones** de EE. UU., Canadá, Reino Unido, Australia, India y Francia. Microsoft **incautó 50 sitios web y desactivó más de 150 dominios**

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/
    label: Microsoft Security Blog
  - url: https://blogs.microsoft.com/on-the-issues/2026/09/22/disrupting-eviltokens-the-ai-chatbot-built-for-cybercrime/
    label: Microsoft On the Issues
  - url: https://www.securityweek.com/ai-powered-phishing-platform-eviltokens-disrupted-by-microsoft/
    label: SecurityWeek

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# EvilTokens: Microsoft dismantles an AI-powered PhaaS that compromised 12,000 inboxes

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-B23B40?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

**Microsoft's Digital Crimes Unit moves against EvilTokens**, a phishing-as-a-service platform that since **February 2026** powered device-code phishing campaigns and, in Microsoft's account, *"used AI at every step of the attack chain."* The platform's centrepiece was an **AI chatbot that analysed a victim's inbox to identify trusted relationships, payment authorisations and sensitive responsibilities, recommended fraud strategies and drafted impersonation messages** — Microsoft's framing: *"[AI] helped them decide who to target, who to impersonate, and how to most effectively exploit the relationship to extract as much money as possible."* The service (sold by the actor tracked **Storm-2992** at **$1,500 plus $500/month**) was used to compromise **more than 12,000 inboxes across 10,000+ organisations** in the US, Canada, the UK, Australia, India and France, mostly for business email compromise. Microsoft **seized 50 websites and disabled 150+ domains**; the UK-registered company behind it is named in pleadings, and TRM Labs supported the disruption. The AI here assists the operator — it analyses and advises rather than acting autonomously — and the platform is now dismantled; recorded `incident` / `WEAPON` / `high` / `real_harm: true` as the archive's first AI-driven PhaaS takedown

## Attack chain

```mermaid
flowchart LR
    E["Storm-2992 sells EvilTokens on Telegram<br/>($1,500 + $500/month)"]:::entry
    S1["Customers run device-code phishing lures<br/>(OAuth device flow; MFA decoupled)"]:::step
    S2["AI analyses the compromised inbox - trusts, payment<br/>approvals, who to impersonate, fraud strategy"]:::step
    I["12,000+ inboxes across 10,000+ organisations<br/>hit with BEC; Microsoft seizes 50 sites,<br/>disables 150+ domains"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What EvilTokens was.** Microsoft describes it as *"one of the most widely used phishing-as-a-service (PhaaS) platforms"* within seven months of its February 2026 emergence, providing *"cybercriminals with AI capabilities for tailoring phishing lures and analyzing compromised inboxes to identify high-value targets"* — *"This AI-powered cybercrime platform facilitated sophisticated business email compromise (BEC) campaigns that compromised more than 12,000 inboxes in over 10,000 organizations worldwide."* Its primary capability is **device code phishing**: abusing the legitimate OAuth device-code flow (designed for TVs, printers, conferencing devices) in which a user enters a short code in a browser on a second device. Threat actors initiate the flow, deliver the code in a phishing lure, and the entered session *"grant[s] access to the account without exposing credentials"* — which *"circumvent[s] traditional MFA protections by decoupling authentication from the originating session."* Stolen tokens enable email exfiltration and persistence through malicious inbox rules; Microsoft also tracked an April 2026 campaign aligned with EvilTokens that spun up thousands of short-lived polling nodes on automation platforms to evade signature-based detection.

**Where the AI sits.** Microsoft's account is specific about the role, and it is more than copywriting. Its security blog: *"providing cybercriminals with AI capabilities for tailoring phishing lures and analyzing compromised inboxes to identify high-value targets"*; the toolkit offered prebuilt templates *"and landing pages with an AI-powered assistant to aid in structuring target-specific emails"*. Post-compromise, *"EvilTokens enabled threat actors to utilize AI assistants to sift through victim mailbox[es]"*. The On the Issues blog, from Microsoft's Digital Crimes Unit, puts the chatbot at the service's centre: it *"could analyze a victim's inbox and help criminals identify trusted relationships, payment authorizations, and sensitive responsibilities, as well as other circumstances where fraud was most likely to succeed"* and *"could even recommend fraud strategies, including drafting messages that impersonated trusted contacts."* Microsoft believes the platform itself was also coded with AI. Its summary verdict: *"AI was not simply helping attackers write more convincing messages. It helped them decide who to target, who to impersonate, and how to most effectively exploit the relationship to extract as much money as possible."*

**Scale, price, and the takedown.** The actor tracked as **Storm-2992** advertised the service on Telegram at **$1,500 for initial purchase plus $500/month**; victim organisations are reported across the **US, Canada, the UK, Australia, India and France**, and the service offered **44 different themes** for lure emails and phishing pages. Microsoft's Digital Crimes Unit filed pleadings naming a UK-registered company behind the operation, **seized 50 websites used to run the service and disabled more than 150 further domains** linked to its infrastructure. SecurityWeek reported the disruption the next day, with TRM Labs publicly supporting the action.

**How this archive reads it — and where the line is.** EvilTokens qualifies for the `WEAPON` category in the strict sense the archive uses: a human (here, paying cybercriminals) deliberately uses AI as part of an attack tool, with confirmed harm — 12,000-plus compromised mailboxes. It sits at the assisted end of the spectrum, though: the chatbot analyses and advises a human operator; it does not run the intrusion itself, and Microsoft's own phrase is *"AI-style chatbot"*. The record therefore keeps Microsoft's claims and limits side by side: `incident` / `WEAPON` / `high` / `real_harm: true`, with the AI's promotional-and-analytical role stated exactly as documented — the archive's first entry for the AI-driven PhaaS product category.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft Security Blog | <https://www.microsoft.com/en-us/security/blog/2026/09/22/unmasking-eviltokens-getting-to-the-root-of-device-code-phishing/> |
| 2 | Microsoft On the Issues | <https://blogs.microsoft.com/on-the-issues/2026/09/22/disrupting-eviltokens-the-ai-chatbot-built-for-cybercrime/> |
| 3 | SecurityWeek | <https://www.securityweek.com/ai-powered-phishing-platform-eviltokens-disrupted-by-microsoft/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-22` (raw: 2026-09-22, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — two first-party Microsoft posts (security blog and Digital Crimes Unit), plus independent press coverage |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-22-eviltokens-disrupted` |

<sub>**Why this classification:** A cybercrime service whose AI component was central — inbox analysis, target and impersonation decisions, fraud-strategy recommendation — used by paying operators against real organisations, with 12,000+ confirmed compromised inboxes: `incident` / `real_harm: true`. Rated `high` rather than `critical`: the harm is large and confirmed, but the AI assists human operators rather than executing autonomously, and the platform itself has been dismantled. Dated to Microsoft's disruption announcement (22 September 2026). Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-08` [GTIG AI threat tracker: from prompting to autonomy](2026-09-08-gtig-prompting-to-autonomy.md)<br>  <sub>The ecosystem view of AI moving through the attack lifecycle</sub>
- `2026-09-16` [RatHat: AI-driven Android malware walks operators through infected devices](2026-09-16-rathat-ai-android-malware.md)<br>  <sub>Another September case of AI baked into a criminal tool</sub>
- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>The autonomous end of the same spectrum</sub>

---
