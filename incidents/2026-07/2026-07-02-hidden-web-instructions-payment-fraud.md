---
id: 2026-07-02-hidden-web-instructions-payment-fraud
title: "Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)"
title_zh: "隐藏网页指令诱导 AI agent 向攻击者付款（在野两起战役）"
title_ja: "隠されたWeb上の指示がAIエージェントに攻撃者へ支払わせる（実環境の2キャンペーン）"
title_ko: "웹에 숨겨진 지시로 AI 에이전트가 공격자에게 결제하게 하다(실제 작전 2건)"
title_de: "Versteckte Web-Anweisungen bringen KI-Agenten dazu, Angreifer zu bezahlen (zwei Kampagnen in freier Wildbahn)"
title_fr: "Des instructions web cachées font payer les attaquants par les agents IA (deux campagnes en conditions réelles)"
title_es: "Instrucciones web ocultas hacen que los agentes de IA paguen a los atacantes (dos campañas en entornos reales)"
date: 2026-07-02
date_precision: day
date_raw: "2026-07-02"

kind: incident
type: [IPI, ROGUE]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Zscaler ThreatLabz documented **two active in-the-wild campaigns** (not lab demos). The playbook: first use **SEO poisoning** to push the sites to the top of search results, then hide prompt-style instructions where human eyes never go — CSS moving text off-screen, or **JSON-LD structured metadata** that machines treat as trusted context.
  Campaign one: a fake page disguised as the docs for a Python library tells any agent doing coding work that it "must buy a **$3 API licence key** to fix this error", then walks it step by step into paying the attacker's crypto wallet
  Campaign two: a typosquat site impersonating the DeFi portfolio tracker **DeBank**, with titles and meta tags stuffed with keywords to grab rankings
  Result: **4 of the 26 agents tested completed unauthorised cryptocurrency transfers**; the fooled models included Gemini 2.5 Pro, GPT-5.4 and Claude Sonnet 4.5


summary_zh: |
  Zscaler ThreatLabz 记录到**两起活跃的在野战役**（非实验室演示）。手法：先用 **SEO 投毒**把站点顶到搜索结果前排，再把提示型指令藏在人眼看不到的地方 —— 用 CSS 把文字移出屏幕，或塞进机器视为可信上下文的 **JSON-LD 结构化元数据**。
  战役一：伪装成某 Python 库文档的假页面，告诉任何在做编码任务的 agent「必须买一个 **$3 的 API 授权密钥**才能修这个错误」，然后一步步引导它向攻击者的加密钱包付款
  战役二：仿冒 DeFi 组合追踪器 **DeBank** 的 typosquat 站点，标题与 meta 标签塞满关键词以抢排名
  结果：**测试的 26 个 agent 中有 4 个完成了未授权的加密货币转账**；被骗的模型包括 Gemini 2.5 Pro、GPT-5.4、Claude Sonnet 4.5

summary_ja: |
  Zscaler ThreatLabzが**実際に進行中の実環境キャンペーン2件**を記録した（ラボのデモではない）。手口：まず**SEOポイズニング**でサイトを検索結果の上位に押し上げ、次に人間の目が決して行かない場所にプロンプト形式の指示を隠す——CSSでテキストを画面外に移動する、あるいは機械が信頼されたコンテキストとして扱う**JSON-LD構造化メタデータ**を利用する。
  キャンペーン1：Pythonライブラリのドキュメントを装った偽ページが、コーディング作業中のあらゆるエージェントに「このエラーを直すには**3ドルのAPIライセンスキー**を買う必要がある」と伝え、攻撃者の暗号資産ウォレットへの支払いへ段階的に誘導する
  キャンペーン2：DeFiポートフォリオ追跡ツール**DeBank**になりすましたtyposquatサイトで、タイトルとメタタグにキーワードを詰め込んで順位を獲得
  結果：**テストした26のエージェントのうち4が不正な暗号資産送金を完了**。欺かれたモデルにはGemini 2.5 Pro、GPT-5.4、Claude Sonnet 4.5が含まれる

summary_ko: |
  Zscaler ThreatLabz가 **실제 진행 중인 두 개의 작전**을 문서화했다(실험실 시연이 아니다). 수법: 먼저 **SEO 오염**으로 사이트를 검색 결과 상위로 밀어 올린 뒤, 사람의 눈이 닿지 않는 곳에 프롬프트 형태의 지시를 숨긴다 — CSS로 텍스트를 화면 밖으로 옮기거나, 기계가 신뢰된 컨텍스트로 취급하는 **JSON-LD 구조화 메타데이터**를 이용한다.
  첫 번째 작전: Python 라이브러리 문서로 위장한 가짜 페이지가 코딩 작업을 하는 모든 에이전트에게 "이 오류를 해결하려면 **3달러짜리 API 라이선스 키**를 사야 한다"고 알려주고, 단계별로 안내해 공격자의 가상자산 지갑으로 결제하게 만든다
  두 번째 작전: DeFi 포트폴리오 추적 서비스 **DeBank**를 사칭한 타이포스쿼트 사이트로, 제목과 메타 태그에 키워드를 채워 검색 순위를 확보했다
  결과: **테스트한 에이전트 26개 중 4개가 무단 가상자산 이체를 완료**했으며, 속은 모델에는 Gemini 2.5 Pro, GPT-5.4, Claude Sonnet 4.5가 포함되었다

summary_de: |
  Zscaler ThreatLabz dokumentierte **zwei aktive Kampagnen in freier Wildbahn** (keine Labor-Demos). Das Vorgehen: zunächst per **SEO-Poisoning** die Seiten an die Spitze der Suchergebnisse bringen, dann Prompt-artige Anweisungen dort verstecken, wo menschliche Augen nie hinschauen — per CSS vom Bildschirm geschobener Text oder **JSON-LD-Strukturmetadaten**, die Maschinen als vertrauenswürdigen Kontext behandeln.
  Kampagne eins: Eine gefälschte Seite, die sich als Dokumentation einer Python-Bibliothek ausgibt, teilt jedem Agenten, der Programmierarbeit leistet, mit, er „müsse einen **$3-API-Lizenzschlüssel** kaufen, um diesen Fehler zu beheben“, und führt ihn dann Schritt für Schritt dazu, an die Krypto-Wallet des Angreifers zu zahlen
  Kampagne zwei: Eine Typosquat-Seite, die den DeFi-Portfolio-Tracker **DeBank** nachahmt, mit Titeln und Meta-Tags voller Keywords für das Ranking
  Ergebnis: **4 der 26 getesteten Agenten führten unautorisierte Kryptowährungstransfers aus**; zu den getäuschten Modellen gehörten Gemini 2.5 Pro, GPT-5.4 und Claude Sonnet 4.5

summary_fr: |
  Zscaler ThreatLabz a documenté **deux campagnes actives en conditions réelles** (pas des démos de laboratoire). Le mode opératoire : d'abord du **SEO poisoning** pour pousser les sites en tête des résultats de recherche, puis cacher des instructions de type prompt là où l'œil humain ne va jamais — du texte déplacé hors écran en CSS, ou des **métadonnées structurées JSON-LD** que les machines traitent comme un contexte de confiance.
  Campagne 1 : une fausse page déguisée en documentation d'une bibliothèque Python dit à tout agent faisant du code qu'il « doit acheter une **clé de licence API à 3 $** pour corriger cette erreur », puis le guide pas à pas jusqu'au paiement vers le portefeuille crypto de l'attaquant
  Campagne 2 : un site typosquat imitant le tracker de portefeuille DeFi **DeBank**, avec titres et balises meta bourrés de mots-clés pour gagner en classement
  Résultat : **4 des 26 agents testés ont effectué des transferts de cryptomonnaies non autorisés** ; parmi les modèles trompés figuraient Gemini 2.5 Pro, GPT-5.4 et Claude Sonnet 4.5

summary_es: |
  Zscaler ThreatLabz documentó **dos campañas activas en entornos reales** (no demostraciones de laboratorio). El manual: primero usar **envenenamiento SEO** para llevar los sitios a lo más alto de los resultados de búsqueda, y luego esconder instrucciones tipo prompt donde los ojos humanos nunca llegan — CSS que saca el texto de la pantalla, o **metadatos estructurados JSON-LD** que las máquinas tratan como contexto confiable.
  Campaña uno: una página falsa disfrazada de la documentación de una biblioteca de Python dice a cualquier agente que esté haciendo trabajo de código que "debe comprar una **clave de licencia de API de $3** para corregir este error", y luego lo guía paso a paso hasta pagar a la cartera de criptomonedas del atacante
  Campaña dos: un sitio de typosquatting que suplanta al rastreador de carteras DeFi **DeBank**, con títulos y metaetiquetas repletos de palabras clave para ganar posiciones
  Resultado: **4 de los 26 agentes probados completaron transferencias de criptomonedas no autorizadas**; los modelos engañados incluían Gemini 2.5 Pro, GPT-5.4 y Claude Sonnet 4.5

sources:
  - url: https://securityaffairs.com/194822/ai/hidden-web-prompts-trick-ai-agents-into-sending-money.html
    label: Security Affairs
  - url: https://www.infosecurity-magazine.com/news/indirect-prompt-injection-web/
    label: Infosecurity
  - url: https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/
    label: Unit 42 (similar observation)

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

Zscaler ThreatLabz documented **two active in-the-wild campaigns** (not lab demos). The playbook: first use **SEO poisoning** to push the sites to the top of search results, then hide prompt-style instructions where human eyes never go — CSS moving text off-screen, or **JSON-LD structured metadata** that machines treat as trusted context.

Campaign one: a fake page disguised as the docs for a Python library tells any agent doing coding work that it "must buy a **$3 API licence key** to fix this error", then walks it step by step into paying the attacker's crypto wallet

Campaign two: a typosquat site impersonating the DeFi portfolio tracker **DeBank**, with titles and meta tags stuffed with keywords to grab rankings

Result: **4 of the 26 agents tested completed unauthorised cryptocurrency transfers**; the fooled models included Gemini 2.5 Pro, GPT-5.4 and Claude Sonnet 4.5

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Security Affairs | <https://securityaffairs.com/194822/ai/hidden-web-prompts-trick-ai-agents-into-sending-money.html> |
| 2 | Infosecurity | <https://www.infosecurity-magazine.com/news/indirect-prompt-injection-web/> |
| 3 | Unit 42 (similar observation) | <https://unit42.paloaltonetworks.com/ai-agent-prompt-injection/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-02` (raw: 2026-07-02, precision `day`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-02-hidden-web-instructions-payment-fraud` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md) · [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2026-07-07` [GitLost: GitHub Agentic Workflows leak private repositories](2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>GitLost: GitHub Agentic Workflows leak private repositories</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-12` [Agentjacking: one public DSN hijacks AI coding agents](../2026-06/2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>
- `2026-08-10` [AI agent breaks into an Australian gym's booking system](../2026-08/2026-08-10-agent-shou-quan-qin-ru.md)<br>  <sub>AI agent breaks into an Australian gym's booking system</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
