---
id: 2026-09-08-gtig-prompting-to-autonomy
title: "GTIG AI threat tracker: from prompting to autonomy"
title_zh: "GTIG AI 威胁追踪：从提示到自主"
title_ja: "GTIG AI脅威トラッカー：プロンプトから自律へ"
title_ko: "GTIG AI 위협 트래커: 프롬프팅에서 자율로"
title_de: "GTIG AI Threat Tracker: Vom Prompting zur Autonomie"
title_fr: "GTIG AI Threat Tracker : du prompting à l'autonomie"
title_es: "GTIG AI Threat Tracker: del prompting a la autonomía"
date: 2026-09-08
date_raw: "2026-09-08"
date_precision: day

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Google Threat Intelligence Group (GTIG)** publishes its Q2 2026 **AI Threat Tracker**, describing how *“forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation.”* The cases span the ladder. **UNC6780** compromises developer accounts to publish trojanised forks of legitimate MCP servers — such as `tiktoken_mcp` — to PyPI, and its **DUSTMAKER** stealer extracts OIDC tokens from GitHub Actions runners to publish backdoored packages *“with valid, cryptographically signed SLSA Build 3 attestations”* that *“will pass AI coding agent automated trust checks.”* A suspected financially motivated actor used an AI coding chatbot, a prompt and preconfigured markdown agent instructions to plan and run a **mass credential-harvesting campaign in under six hours** — thousands of credentials, stolen from victim cloud infrastructure, with autonomous scanning, troubleshooting and IP rotation. State-linked groups run throughout: PRC-nexus **UNC6508** targets proprietary AI research, DPRK's **MIDNIGHT NEPTUNE** and Iran's **CALANQUE ION** embed commercial LLMs across operations, and GTIG disrupted a China-based actor that used Gemini to design an automated penetration-testing framework. The tracker also records the year's **LLMJacking** market — stolen AI accounts and hijacked compute — and LLM refusal bait: DUSTMAKER loaders open with biological- and nuclear-weapons text *“likely intended to cause LLM security scanners to fail or skip analysis.”*

summary_zh: |
  **谷歌威胁情报小组（GTIG）**发布 2026 年第二季度 **AI 威胁追踪**报告，描述*「走在前面的攻击者正从基础提示转向 agent 化 AI 工作流与 AI 驱动的自动化」*。案例沿这条阶梯展开：**UNC6780** 攻陷开发者账号，把合法 MCP 服务器（如 `tiktoken_mcp`）的「投毒分叉」发布到 PyPI；其 **DUSTMAKER** 窃密程序会从 GitHub Actions 运行器进程内存中提取 OIDC 令牌，以合法身份发布带*「有效的、加密签名的 SLSA Build 3 证明」*的后门包——*「这些包会通过 AI 编程 agent 的自动信任检查」*。一个疑似经济动机的攻击者用 AI 编程聊天机器人、一段提示加预置的 markdown agent 指令，在**不到六小时**内策划并执行了一场大规模凭证收割行动：从受害者的云基础设施中窃得数千条凭证，扫描、排障与 IP 轮换全部自主完成。国家背景组织贯穿全篇：中国背景的 **UNC6508** 瞄准专有 AI 研究；朝鲜的 **MIDNIGHT NEPTUNE** 与伊朗的 **CALANQUE ION** 把商用 LLM 嵌进行动链条；GTIG 还处置了一个用 Gemini 设计自动化渗透测试框架的中国相关行为体。报告也记录了今年的 **LLMJacking** 市场——被盗 AI 账号与被劫持算力——以及针对 LLM 的「拒绝诱饵」：DUSTMAKER 的加载器以生物武器与核武器相关文本开头，*「很可能意在让 LLM 安全扫描器失败或跳过分析」*

summary_ja: |
  **Google Threat Intelligence Group（GTIG）**は2026年第2四半期の**AI脅威トラッカー**を公表し、*「先を行く攻撃者が基礎的なプロンプトからエージェント型AIワークフローとAI駆動の自動化へ移行している」*と述べた。事例はその階段をなぞる。**UNC6780**は開発者アカウントを侵害し、正規MCPサーバー（`tiktoken_mcp`など）のトロイの木馬化フォークをPyPIに公開。その**DUSTMAKER**スティーラーはGitHub ActionsランナーのプロセスメモリからOIDCトークンを抽出し、*「有効で暗号署名されたSLSA Build 3アテステーション付き」*のバックドアパッケージを公開する——*「これらはAIコーディングエージェントの自動信頼チェックを通過する」*。金銭的動機とみられる攻撃者は、AIコーディングチャットボット、1つのプロンプト、事前設定されたmarkdownのエージェント指示を使い、**6時間未満**で大規模な資格情報収集キャンペーンを計画・実行し、被害者のクラウド基盤から数千件の資格情報を窃取した。スキャン、トラブルシューティング、IPローテーションはすべて自律的。国家背景のグループも随所に登場する。中国系**UNC6508**は独自AI研究を標的にし、北朝鮮の**MIDNIGHT NEPTUNE**とイランの**CALANQUE ION**は商用LLMを活動に組み込み、GTIGはGeminiで自動ペネトレーションテスト基盤を設計していた中国系アクターを無効化した。報告は今年の**LLMJacking**市場（盗まれたAIアカウントと乗っ取られた計算資源）や、DUSTMAKERローダーが生物・核兵器関連の文言で始まるLLMへの「拒否の囮」も記録している

summary_ko: |
  **Google Threat Intelligence Group(GTIG)**이 2026년 2분기 **AI 위협 트래커**를 발표하며 *"앞서가는 공격자들이 기초 프롬프팅에서 에이전트형 AI 워크플로와 AI 기반 자동화로 이동하고 있다"*고 밝혔다. 사례들은 그 사다리를 따른다. **UNC6780**은 개발자 계정을 탈취해 정상 MCP 서버(예: `tiktoken_mcp`)의 트로이목마 포크를 PyPI에 게시하고, 그 **DUSTMAKER** 스틸러는 GitHub Actions 러너 프로세스 메모리에서 OIDC 토큰을 추출해 *"유효하고 암호학적으로 서명된 SLSA Build 3 증명"*이 붙은 백도어 패키지를 게시한다. *"이 패키지들은 AI 코딩 에이전트의 자동 신뢰 검사를 통과한다."* 금전적 동기로 보이는 공격자는 AI 코딩 챗봇, 하나의 프롬프트, 사전 구성된 markdown 에이전트 지침으로 **6시간 이내**에 대규모 자격 증명 수집 캠페인을 계획·실행해 피해자 클라우드 인프라에서 수천 건의 자격 증명을 훔쳤다. 스캔, 트러블슈팅, IP 로테이션은 모두 자율적이었다. 국가 배후 조직도 곳곳에 등장한다. 중국 연계 **UNC6508**은 독점 AI 연구를 겨냥하고, 북한의 **MIDNIGHT NEPTUNE**과 이란의 **CALANQUE ION**은 상용 LLM을 작전에 통합했으며, GTIG는 Gemini로 자동 침투 테스트 프레임워크를 설계하던 중국 관련 행위자를 무력화했다. 보고서는 올해의 **LLMJacking** 시장(도난당한 AI 계정과 탈취된 컴퓨트)과 DUSTMAKER 로더가 생물·핵무기 관련 문구로 시작하는 LLM 대상 '거부 미끼'도 기록한다

summary_de: |
  **Google Threat Intelligence Group (GTIG)** veröffentlicht den **AI Threat Tracker** für Q2 2026: *„Vorausschauende Angreifer wechseln vom einfachen Prompting zu agentischen KI-Workflows und KI-gestützter Automatisierung.“* Die Fälle folgen dieser Leiter. **UNC6780** kompromittiert Entwicklerkonten, um trojanisierte Forks legitimer MCP-Server – etwa `tiktoken_mcp` – auf PyPI zu veröffentlichen; sein **DUSTMAKER**-Stealer extrahiert OIDC-Token aus dem Prozessspeicher von GitHub-Actions-Runnern und veröffentlicht Backdoor-Pakete *„mit gültigen, kryptografisch signierten SLSA-Build-3-Attestierungen“*, die *„die automatischen Vertrauensprüfungen von KI-Coding-Agenten bestehen.“* Ein vermutlich finanziell motivierter Akteur nutzte einen KI-Coding-Chatbot, einen Prompt und vorkonfigurierte Markdown-Agentenanweisungen, um in **unter sechs Stunden** eine massenhafte Credential-Harvesting-Kampagne zu planen und auszuführen – Tausende Zugangsdaten aus der Cloud-Infrastruktur der Opfer, mit autonomen Scans, Troubleshooting und IP-Rotation. Staatlich verankerte Gruppen ziehen sich durch: Das PRC-nahe **UNC6508** zielt auf proprietäre KI-Forschung, Nordkoreas **MIDNIGHT NEPTUNE** und Irans **CALANQUE ION** betten kommerzielle LLMs in Operationen ein, und GTIG störte einen China-nahen Akteur, der Gemini zum Entwurf eines automatisierten Pentest-Frameworks nutzte. Der Tracker erfasst auch den **LLMJacking**-Markt – gestohlene KI-Konten und gekaperte Rechenleistung – sowie LLM-Köder: DUSTMAKER-Loader beginnen mit Bio- und Nuklearwaffen-Texten, *„wahrscheinlich um LLM-Sicherheitsscanner scheitern zu lassen oder die Analyse zu überspringen.“*

summary_fr: |
  **Google Threat Intelligence Group (GTIG)** publie son **AI Threat Tracker** du T2 2026 : *« des adversaires à l'avant-garde passent du prompting de base à des workflows d'agents et à l'automatisation par l'IA. »* Les cas suivent cette échelle. **UNC6780** compromet des comptes de développeurs pour publier sur PyPI des forks trojanisés de serveurs MCP légitimes — comme `tiktoken_mcp` — et son stealer **DUSTMAKER** extrait des jetons OIDC de la mémoire des runners GitHub Actions pour publier des paquets piégés *« avec des attestations SLSA Build 3 valides et signées cryptographiquement »* qui *« passeront les contrôles de confiance automatiques des agents de codage. »* Un acteur probablement motivé financièrement a utilisé un chatbot de codage, un prompt et des instructions d'agent prédéfinies en markdown pour planifier et exécuter une **campagne de collecte massive d'identifiants en moins de six heures** — des milliers d'identifiants, avec scan, dépannage et rotation d'IP autonomes. Les groupes étatiques traversent le rapport : **UNC6508** (Chine) cible la recherche IA propriétaire, **MIDNIGHT NEPTUNE** (Corée du Nord) et **CALANQUE ION** (Iran) intègrent des LLM commerciaux dans leurs opérations, et GTIG a neutralisé un acteur lié à la Chine utilisant Gemini pour concevoir un framework de pentest automatisé. Le rapport consigne aussi le marché du **LLMJacking** — comptes IA volés, calcul détourné — et les leurres à refus : les chargeurs DUSTMAKER s'ouvrent sur des textes d'armes biologiques et nucléaires *« probablement destinés à faire échouer ou à faire sauter l'analyse des scanners LLM. »*

summary_es: |
  **Google Threat Intelligence Group (GTIG)** publica su **AI Threat Tracker** del segundo trimestre de 2026: *«los adversarios más avanzados pasan del prompting básico a flujos de trabajo con agentes y automatización impulsada por IA.»* Los casos siguen esa escalera. **UNC6780** compromete cuentas de desarrolladores para publicar en PyPI forks troyanizados de servidores MCP legítimos —como `tiktoken_mcp`— y su stealer **DUSTMAKER** extrae tokens OIDC de la memoria de los runners de GitHub Actions para publicar paquetes con puerta trasera *«con atestaciones SLSA Build 3 válidas y firmadas criptográficamente»* que *«pasarán las comprobaciones automáticas de confianza de los agentes de programación.»* Un actor presuntamente motivado por dinero usó un chatbot de programación, un prompt e instrucciones de agente preconfiguradas en markdown para planificar y ejecutar una **campaña masiva de recolección de credenciales en menos de seis horas** —miles de credenciales, con escaneo, resolución de problemas y rotación de IP autónomos—. Los grupos estatales recorren todo el informe: **UNC6508** (China) ataca investigación propietaria de IA; **MIDNIGHT NEPTUNE** (Corea del Norte) y **CALANQUE ION** (Irán) integran LLM comerciales en sus operaciones, y GTIG neutralizó a un actor vinculado a China que usaba Gemini para diseñar un framework de pentest automatizado. El informe registra además el mercado del **LLMJacking** —cuentas de IA robadas y cómputo secuestrado— y los señuelos de rechazo: los cargadores DUSTMAKER abren con textos de armas biológicas y nucleares *«probablemente para hacer fallar o saltar el análisis de los escáneres LLM».*

sources:
  - url: https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai
    label: Google Threat Intelligence Group
  - url: https://www.threatops.tech/threat-pulse/gtig-adversarial-ai-agent-enabled-operations-september-2026
    label: ThreatOps

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# GTIG AI threat tracker: from prompting to autonomy

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

**Google Threat Intelligence Group (GTIG)** publishes its Q2 2026 **AI Threat Tracker**, describing how *“forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation.”* The cases span the ladder. **UNC6780** compromises developer accounts to publish trojanised forks of legitimate MCP servers — such as `tiktoken_mcp` — to PyPI, and its **DUSTMAKER** stealer extracts OIDC tokens from GitHub Actions runners to publish backdoored packages *“with valid, cryptographically signed SLSA Build 3 attestations”* that *“will pass AI coding agent automated trust checks.”* A suspected financially motivated actor used an AI coding chatbot, a prompt and preconfigured markdown agent instructions to plan and run a **mass credential-harvesting campaign in under six hours** — thousands of credentials, stolen from victim cloud infrastructure, with autonomous scanning, troubleshooting and IP rotation. State-linked groups run throughout: PRC-nexus **UNC6508** targets proprietary AI research, DPRK's **MIDNIGHT NEPTUNE** and Iran's **CALANQUE ION** embed commercial LLMs across operations, and GTIG disrupted a China-based actor that used Gemini to design an automated penetration-testing framework. The tracker also records the year's **LLMJacking** market — stolen AI accounts and hijacked compute — and LLM refusal bait: DUSTMAKER loaders open with biological- and nuclear-weapons text *“likely intended to cause LLM security scanners to fail or skip analysis.”*

## Attack chain

```mermaid
flowchart LR
    E["An adversary moves past prompting into agentic workflows"]:::entry
    S0["AI coding chatbot + a prompt + markdown agent instructions: scanning, harvesting, IP rotation"]:::step
    I["Thousands of credentials harvested in under six hours<br/><i>(report-level finding; no single victim named)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The framing: prompting is over.** GTIG's baseline is its own May 2026 report on adversarial AI misuse; this tracker reports what changed since. *“Since the release of our May 2026 report… GTIG has observed forward leaning adversaries transition from basic prompting to agentic AI workflows and AI-enabled automation.”* The headline consequence is speed: agents compress the traditional window defenders have to respond, and the report's Q2 trend list reads as a map of where that shows up — accelerating software supply-chain risk around AI coding tooling, direct targeting of proprietary AI assets (“model weights to cloud compute quotas”), agentic automation of attack stages, and AI as a force multiplier across the lifecycle. The report is explicit about the limit: *“GTIG has not yet observed threat actors deploying fully autonomous pipelines against targets in the wild,”* describing instead *“a gradual maturation of tradecraft and layering of AI capabilities.”*

**The supply chain: UNC6780 and DUSTMAKER.** UNC6780's play is *“multiple tactics to trick AI coding assistants and large language model (LLM) security scanners”*: it compromises legitimate developer accounts and publishes trojanised forks of real MCP servers (the report names `tiktoken_mcp`) to PyPI, with malicious workspace hooks that are auto-ingested *“whenever the assets were downloaded or cloned.”* Its DUSTMAKER credential stealer detects when it is running in CI/CD, extracts OIDC tokens from the process memory of GitHub Actions runners, and uses them to authorise itself as a trusted publisher — publishing compromised packages *“with valid, cryptographically signed SLSA Build 3 attestations”* that *“will pass AI coding agent automated trust checks.”* The same malware carries LLM refusal bait: DUSTMAKER's JavaScript loaders open with biological- and nuclear-weapons text *“likely intended to cause LLM security scanners to fail or skip analysis”* — the tactic ESET would name GuardBreaker in the same week.

**The six-hour campaign and the "Recon" C2.** The report's most-quoted case: a suspected financially motivated actor compromised an organisation's cloud infrastructure and deployed an autonomous, multi-agent attack framework, then used *“an AI coding chatbot, a prompt, and a set of agent instructions to plan, build, and execute a mass credential harvesting campaign in less than six hours.”* With preconfigured markdown instruction sets as playbooks, the agent ran automated scanning and credential harvesting — *“compromising thousands of third-party credentials”* — while handling real-time troubleshooting and IP-rotation logic *“without manual intervention, significantly reducing the human-in-the-loop latency,”* and routing attack traffic through the victim's own legitimate IP range. A related find: an exposed C2 server hosting an automated recon and credential-management framework dubbed “Recon,” with directory listings full of agentic configuration files (`AGENTS.md`, `KNOWLEDGE.md`, `agentic_vuln_research.md`). One caveat this record keeps: the six-hour campaign may be the same intrusion described as one of the case studies in the archive's **Mandiant** record of 16 September — both concern a cloud compromise turned into an AI-assisted credential-harvesting hub — but neither report cites the other, so the overlap cannot be confirmed.

**Targets, actors, and the market.** GTIG attributes across the map: PRC-nexus **UNC6508** targets proprietary AI research at academic, medical and military institutions, and has compromised cloud environments to deploy local, open-weight LLM infrastructure; DPRK cluster **MIDNIGHT NEPTUNE** uses commercial LLMs and open-weight models for social engineering and automated backdoor development in cryptocurrency theft; Iran's **CALANQUE ION** (formerly APT42) uses Gemini for reconnaissance and pretexting. GTIG separately disrupted a PRC-nexus group using Gemini to design a dynamic, automated penetration-testing framework, and — *“the first time Google has pursued legal action over Gemini misuse”* — disrupted “Outsider Enterprise,” a China-based phishing-kit service whose operators used Gemini to generate code at scale. On the criminal side, the tracker documents a maturing **LLMJacking** market: stolen developer credentials, purchased AI accounts, and hijacked enterprise cloud infrastructure used to run unauthorised high-performance compute, with DPRK IT-worker clusters bulk-registering API accounts. Recorded as a `report` at `info` severity: no single victim or incident is the subject — it is the state-of-the-art survey that this archive's other records of the period sit inside.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Google Threat Intelligence Group | <https://cloud.google.com/blog/topics/threat-intelligence/from-prompting-to-autonomy-the-evolution-of-adversarial-ai> |
| 2 | ThreatOps | <https://www.threatops.tech/threat-pulse/gtig-adversarial-ai-agent-enabled-operations-september-2026> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-08` (raw: 2026-09-08, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source: the report itself, from Google's own threat-intelligence group |
| Real harm | Not applicable |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-08-gtig-prompting-to-autonomy` |

<sub>**Why this classification:** A vendor threat report, not a single incident — `info` severity with no `real_harm` assessment, consistent with the archive's treatment of the May GTIG tracker and the CrowdStrike and Mandiant reports. Date follows Google's RSS timestamp in GMT (8 September 2026, 14:00 UTC); the post page renders 9 September in some timezones. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-08-27` [GuardBreaker: a Russia-aligned group plants a nuclear-weapon request in its malware to derail AI analysis](../2026-08/2026-08-27-guardbreaker-uac-0099.md)<br>  <sub>The refusal-bait tactic this report documents in DUSTMAKER, used in the wild the same quarter</sub>
- `2026-09-16` [Mandiant 2026 AI report: a runaway agent's $50,000 bill and AI-assisted intrusions](2026-09-16-mandiant-ai-risk-resilience-2026.md)<br>  <sub>Its case study may be the same intrusion as the six-hour campaign</sub>
- `2026-05-12` [GTIG AI threat tracker, 2026 edition](../2026-05/2026-05-12-gtig-wei-xie-zhui-zong.md)<br>  <sub>The May baseline this tracker updates</sub>
- `2025-11-13` [GTG-1002: first AI-orchestrated cyber-espionage campaign](../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>Where Google first documented agent autonomy in state operations</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-08-gtig-prompting-to-autonomy.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
