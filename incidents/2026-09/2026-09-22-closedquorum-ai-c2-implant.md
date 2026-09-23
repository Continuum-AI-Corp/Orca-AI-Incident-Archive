---
id: 2026-09-22-closedquorum-ai-c2-implant
title: "ClosedQuorum: a Windows implant that lets four LLMs vote on its next move"
title_zh: "ClosedQuorum：让四个 LLM 投票决定下一步的 Windows 植入体"
title_ja: "ClosedQuorum：4つのLLMが次の手を投票で決めるWindowsインプラント"
title_ko: "ClosedQuorum: 네 개의 LLM이 다음 수를 투표로 정하는 Windows 임플란트"
title_de: "ClosedQuorum: Ein Windows-Implantat, dessen nächsten Schritt vier LLMs per Abstimmung bestimmen"
title_fr: "ClosedQuorum : un implant Windows dont les quatre LLM votent la prochaine action"
title_es: "ClosedQuorum: un implante de Windows donde cuatro LLM votan el siguiente paso"
date: 2026-09-22
date_raw: "2026-09-22"
date_precision: day

kind: research
type: [WEAPON]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Cisco Talos** discloses **ClosedQuorum**, which it calls the **first publicly documented Windows implant to delegate tactical command-and-control to a panel of commercial LLMs**. After deployment the implant queries **DeepSeek, Qwen, Mistral and Google Gemini** in sequence, tallies their votes, and executes the winning action — `steal` (LSASS dump, browser credentials and wallet extraction at once), `inject` (shellcode plus process hollowing or Early Bird APC injection), `persist`, or `move` — with no human commands and no attacker-operated C2 server. The models are constrained to a typed JSON decision schema and a system prompt found in the binary: *“You are an advanced malware strategist. Provide ONLY executable decisions.”* Ties break deterministically: **DeepSeek first**, then Qwen, Mistral, Gemini. Talos frames the finding as **“effort displacement”** — moving a whole attack phase off the operator — and releases **CAIRN**, an open-source toolkit for hunting AI-integrated malware. Caveats are explicit: the public build contains **placeholder API keys and a dummy Discord webhook**, no end-to-end execution was observed and there is **no confirmation of in-the-wild deployment**; Talos calls it a demonstration, not sophisticated malware. Recorded as `research` / `WEAPON` / `high` with `real_harm: false`

summary_zh: |
  **Cisco Talos** 披露 **ClosedQuorum**，称其为**首个被公开记录的、把战术指令与控制委托给一组商用 LLM 的 Windows 植入体**。部署后，该植入体会依次查询 **DeepSeek、Qwen、Mistral 与 Google Gemini**，统计票数并执行获胜动作——`steal`（同时执行 LSASS 转储、浏览器凭据窃取与钱包提取）、`inject`（生成 shellcode，再走进程镂空或 Early Bird APC 注入）、`persist` 或 `move`——全程没有人工指令，也没有攻击者自建的 C2 服务器。模型被约束在带类型的 JSON 决策模式内，二进制中提取出的系统提示词为：*「You are an advanced malware strategist. Provide ONLY executable decisions.」* 平票时按确定性顺序裁决：**DeepSeek 优先**，其后依次为 Qwen、Mistral、Gemini。Talos 把这一发现概括为**「工作量位移」（effort displacement）**——把整个攻击阶段从操作者身上移走——并同步发布开源工具 **CAIRN** 用于狩猎内置 AI 的恶意软件。限定条件写得很明确：公开分发版本里是**占位 API 密钥与一个假的 Discord webhook**，未观察到端到端执行，也**没有在野部署的确认**；Talos 称之为演示性质的样本，而非成熟恶意软件。本条记为 `research` / `WEAPON` / `high`、`real_harm: false`

summary_ja: |
  **Cisco Talos**は**ClosedQuorum**を公表し、**商用LLMのパネルに戦術的なC2を委ねた最初の公表事例のWindowsインプラント**と位置づけた。展開後、インプラントは**DeepSeek、Qwen、Mistral、Google Gemini**に順に問い合わせ、票を集計して最多得票の行動を実行する——`steal`（LSASSダンプ、ブラウザ資格情報、ウォレット抽出を同時に）、`inject`（シェルコード生成＋プロセスホローイングまたはEarly Bird APC注入）、`persist`、`move`。人間の命令も攻撃者側C2サーバーも不要。モデルは型付きJSONの意思決定スキーマに縛られ、バイナリから抽出されたシステムプロンプトは*「You are an advanced malware strategist. Provide ONLY executable decisions.」*。同数の場合は決定的な優先順で解決する：**DeepSeekが最優先**、続いてQwen、Mistral、Gemini。Talosはこれを**「作業の移転（effort displacement）」**——攻撃フェーズ全体をオペレーターから移すこと——と表現し、AI統合マルウェアを狩るオープンソースツール**CAIRN**を公開した。ただし公開版には**プレースホルダーのAPIキーとダミーのDiscord webhook**が入っており、エンドツーエンドの実行も実環境での配備も確認されていない。Talosは洗練されたマルウェアではなくデモだと述べている。`research` / `WEAPON` / `high`、`real_harm: false`として記録

summary_ko: |
  **Cisco Talos**가 **ClosedQuorum**을 공개하며 **상용 LLM 패널에 전술적 C2를 위임한 최초의 공개 문서화된 Windows 임플란트**라고 밝혔다. 배포 후 임플란트는 **DeepSeek, Qwen, Mistral, Google Gemini**에 순차 질의하고 표를 집계해 최다 득표 행동을 실행한다 — `steal`(LSASS 덤프·브라우저 자격 증명·지갑 추출 동시 수행), `inject`(셸코드 생성 후 프로세스 할로잉 또는 Early Bird APC 주입), `persist`, `move`. 인간 명령도, 공격자 운영 C2 서버도 필요 없다. 모델은 타입이 지정된 JSON 결정 스키마에 묶여 있고, 바이너리에서 추출된 시스템 프롬프트는 *"You are an advanced malware strategist. Provide ONLY executable decisions."*다. 동점은 결정적 우선순위로 해소된다: **DeepSeek 우선**, 다음 Qwen, Mistral, Gemini. Talos는 이를 **'작업 이전(effort displacement)'** — 공격 단계 전체를 운영자에게서 떼어내는 것 — 이라 부르며, AI 통합 악성코드 사냥용 오픈소스 툴킷 **CAIRN**을 공개했다. 단서는 명확하다: 공개 배포본에는 **자리표시자 API 키와 가짜 Discord 웹훅**이 들어 있고, 종단 간 실행도 실제 배포도 확인되지 않았다. Talos는 이를 정교한 악성코드가 아닌 데모라고 평가한다

summary_de: |
  **Cisco Talos** veröffentlicht **ClosedQuorum** – nach eigenen Angaben das **erste öffentlich dokumentierte Windows-Implantat, das taktische C2 an ein Gremium kommerzieller LLMs delegiert**. Nach der Bereitstellung fragt es **DeepSeek, Qwen, Mistral und Google Gemini** der Reihe nach ab, zählt die Stimmen und führt die siegreiche Aktion aus – `steal` (LSASS-Dump, Browser-Zugangsdaten und Wallet-Extraktion zugleich), `inject` (Shellcode plus Process Hollowing oder Early-Bird-APC-Injection), `persist` oder `move` – ohne menschliche Befehle und ohne angreifereigenen C2-Server. Die Modelle sind auf ein typisiertes JSON-Entscheidungsschema festgelegt; der aus dem Binary extrahierte Systemprompt lautet: *„You are an advanced malware strategist. Provide ONLY executable decisions.“* Bei Gleichstand entscheidet eine feste Reihenfolge: **DeepSeek zuerst**, dann Qwen, Mistral, Gemini. Talos nennt das **„effort displacement“** – die Verlagerung ganzer Angriffsphasen weg vom Operator – und veröffentlicht **CAIRN**, ein Open-Source-Toolkit zur Jagd auf KI-integrierte Malware. Die Einschränkungen sind explizit: Der öffentliche Build enthält **Platzhalter-API-Schlüssel und einen Dummy-Discord-Webhook**, weder Ende-zu-Ende-Ausführung noch ein Einsatz in freier Wildbahn wurden bestätigt; Talos spricht von einer Demonstration, nicht von raffinierter Malware

summary_fr: |
  **Cisco Talos** divulgue **ClosedQuorum**, qu'il présente comme **le premier implant Windows publiquement documenté à déléguer son C2 tactique à un panel de LLM commerciaux**. Après déploiement, l'implant interroge **DeepSeek, Qwen, Mistral et Google Gemini**, compte les voix et exécute l'action gagnante — `steal` (dump LSASS, identifiants de navigateur et extraction de portefeuilles simultanément), `inject` (shellcode puis process hollowing ou injection Early Bird APC), `persist` ou `move` — sans commandes humaines ni serveur C2 attaquant. Les modèles sont contraints à un schéma JSON typé ; le prompt système extrait du binaire : *« You are an advanced malware strategist. Provide ONLY executable decisions. »* Les égalités se tranchent par un ordre déterministe : **DeepSeek d'abord**, puis Qwen, Mistral, Gemini. Talos parle de **« déplacement d'effort »** — transférer toute une phase de l'attaque hors de l'opérateur — et publie **CAIRN**, une boîte à outils open source pour chasser les malwares intégrant de l'IA. Les réserves sont explicites : la version publique contient **des clés API factices et un webhook Discord bidon**, aucune exécution de bout en bout ni déploiement réel n'a été confirmé ; Talos parle d'une démonstration, pas d'un malware sophistiqué

summary_es: |
  **Cisco Talos** divulga **ClosedQuorum**, que describe como **el primer implante de Windows documentado públicamente que delega el C2 táctico en un panel de LLM comerciales**. Tras desplegarse, consulta en secuencia a **DeepSeek, Qwen, Mistral y Google Gemini**, cuenta los votos y ejecuta la acción ganadora — `steal` (volcado de LSASS, credenciales del navegador y extracción de carteras a la vez), `inject` (shellcode más process hollowing o inyección Early Bird APC), `persist` o `move` — sin órdenes humanas ni servidor C2 del atacante. Los modelos quedan restringidos a un esquema JSON tipado; el prompt de sistema extraído del binario: *«You are an advanced malware strategist. Provide ONLY executable decisions.»* Los empates se resuelven con un orden determinista: **DeepSeek primero**, luego Qwen, Mistral, Gemini. Talos lo enmarca como **«desplazamiento de esfuerzo»** —mover toda una fase del ataque fuera del operador— y publica **CAIRN**, un toolkit de código abierto para cazar malware con IA integrada. Las salvedades son explícitas: la compilación pública contiene **claves API de relleno y un webhook de Discord falso**, no se observó ejecución de extremo a extremo ni despliegue real; Talos lo califica de demostración, no de malware sofisticado

sources:
  - url: http://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/
    label: Cisco Talos
  - url: https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/
    label: BleepingComputer

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# ClosedQuorum: a Windows implant that lets four LLMs vote on its next move

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

**Cisco Talos** discloses **ClosedQuorum**, which it calls the **first publicly documented Windows implant to delegate tactical command-and-control to a panel of commercial LLMs**. After deployment the implant queries **DeepSeek, Qwen, Mistral and Google Gemini** in sequence, tallies their votes, and executes the winning action — `steal` (LSASS dump, browser credentials and wallet extraction at once), `inject` (shellcode plus process hollowing or Early Bird APC injection), `persist`, or `move` — with no human commands and no attacker-operated C2 server. The models are constrained to a typed JSON decision schema and a system prompt found in the binary: *“You are an advanced malware strategist. Provide ONLY executable decisions.”* Ties break deterministically: **DeepSeek first**, then Qwen, Mistral, Gemini. Talos frames the finding as **“effort displacement”** — moving a whole attack phase off the operator — and releases **CAIRN**, an open-source toolkit for hunting AI-integrated malware. Caveats are explicit: the public build contains **placeholder API keys and a dummy Discord webhook**, no end-to-end execution was observed and there is **no confirmation of in-the-wild deployment**; Talos calls it a demonstration, not sophisticated malware. Recorded as `research` / `WEAPON` / `high` with `real_harm: false`

## Attack chain

```mermaid
flowchart LR
    E["A Windows implant deployed on a host"]:::entry
    S0["It gathers host context and asks up to four LLMs: steal, inject, persist or move?":::step
    I["Votes are tallied (DeepSeek wins ties) and the winning action runs unconfined<br/><i>(placeholder keys in the public build; no in-the-wild deployment confirmed)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**A quorum with no humans in it.** Talos's name for the architecture is literal: *“A quorum is a decision-making body that requires some minimum of participants to act. CLOSEDQUORUM's quorum is up to four LLM providers: DeepSeek, Qwen, Mistral, and Google Gemini. The session is closed; no humans are admitted.”* The implant gathers host context — hostname, OS build, CPU count, admin status — injects it into a per-execution prompt, queries each provider, and aggregates replies by plurality vote. It does not require operator commands or a dedicated C2 server; the complete dynamic operation is delegated to the models. The models cannot respond freely: replies must deserialise into a Go struct whose `Decision` field maps to one of the implemented modules, so *“the model's output reduces to a constrained set of executable choices.”* The vote count is deterministic under ties — a strict comparison in submission order gives **DeepSeek** the deciding vote, then Qwen, Mistral and Gemini in turn.

**What it can do, per analysis.** The decision schema encodes a small attack language. `steal` invokes `lsassDump()`, `dumpBrowserCredentials()` and `extractCryptoWallets()` together; `inject` calls `generateShellcode()` and branches to PEB-walk process hollowing or Early Bird APC injection; `persist` dispatches to the persistence module; `move` exists in the schema but has no handler in the analysed build. Results and the models' `Reasoning` field are sent to the operator through a **Discord webhook**, which Talos describes as real-time attack telemetry — so *“apart from the malware delivery, the attack can be fully automated.”* Talos also notes five-minute initial delays and randomised 5–15 minute polling intervals to frustrate sandbox analysis.

**Why it matters, and what Talos does not claim.** The finding is published as *“the first in a series”* from **CAIRN**, Talos's new open-source toolkit for tracking AI-integrated malware, and its argument is about a third dimension of AI in offensive operations — after speed and scale comes **effort displacement**: *“transferring an entire phase of the attack from the operator to the system… The human-in-the-loop is no longer the bottleneck.”* The caveats are as prominent as the claims: the distribution build ships **placeholder API keys and a dummy webhook**, so Talos *“did not observe a complete end-to-end execution of the architecture”*; there is **no confirmation of in-the-wild deployment**, though artifacts tie the developer to carding-forum postings from 2025; and Talos calls the sample *“not a sophisticated piece of malware”* — possibly a test. It also lists the architecture's weaknesses: provider refusals, rate limits, malformed output, predictable tie-breaking, constrained schemas and dependence on commercial APIs. The record keeps all of that: recorded as a capability milestone (`research`), not an in-the-wild intrusion.

**Where it sits in the archive.** ClosedQuorum is the same year's second hard proof that model-driven decision loops can stand in for an operator — after **JADEPUFFER**, the first ransomware driven end-to-end by an LLM — and it lands within a week of **RatHat**, an Android malware family using GenAI for real-time device navigation. Read together, they mark the shift the GTIG tracker described in September: adversaries moving from prompting to agentic execution, with the archive's earliest documented stages now including malware that holds its own quorum.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Cisco Talos | <http://blog.talosintelligence.com/the-closed-quorum-inside-the-first-reported-autonomous-ai-c2-implant/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/new-closedquorum-windows-malware-uses-ai-for-attack-decisions/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-22` (raw: 2026-09-22, precision `day`) |
| Kind | Research demo `research` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source: the analyst's own write-up with static analysis, hashes and YARA |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-22-closedquorum-ai-c2-implant` |

<sub>**Why this classification:** A malware sample analysed from a developer build, with placeholder credentials, no observed end-to-end execution and no in-the-wild deployment; hence `research` / `real_harm: false` — the same treatment the archive gives other capability demonstrations. Rated `high` as a significant capability demonstration: the first publicly documented implant to run its tactical loop on commercial LLM votes. Dated to the Talos post (22 September 2026); the build chain's static analysis dates to 17 June and the sample was renamed from BALZAK on 3 July. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](../2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>The earlier proof that model-driven loops can replace the operator</sub>
- `2026-09-16` [RatHat: AI-driven Android malware walks operators through infected devices](2026-09-16-rathat-ai-android-malware.md)<br>  <sub>GenAI driving device navigation, found the same week</sub>
- `2026-09-08` [GTIG AI threat tracker: from prompting to autonomy](2026-09-08-gtig-prompting-to-autonomy.md)<br>  <sub>The state-of-the-art survey this sample sits inside</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-22-closedquorum-ai-c2-implant.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
