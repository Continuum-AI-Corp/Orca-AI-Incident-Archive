---
id: 2026-11-04-bossai-ai-attack-mesh-taiwan-emergency
title: "\"BOSSAI\": Acronis documents a lone operator's 12-agent AI attack mesh that breached emergency services across three countries"
title_zh: "\"BOSSAI\"：Acronis 记录一名单人操作者的 12-agent AI 攻击网，攻破三国的应急/急救服务"
title_ja: "「BOSSAI」：Acronisが単独の攻撃者による12エージェントのAI攻撃メッシュを記録——3か国の緊急サービスを侵害"
title_ko: "\"BOSSAI\": Acronis, 단독 공격자의 12개 에이전트 AI 공격 메시를 기록——3개국 긴급 서비스 침해"
title_de: "„BOSSAI\": Acronis dokumentiert das 12-Agenten-KI-Angriffsnetz eines Einzeltäters, das Notdienste in drei Ländern kompromittierte"
title_fr: "« BOSSAI » : Acronis documente le maillage d'attaque IA à 12 agents d'un opérateur isolé, ayant compromis les services d'urgence de trois pays"
title_es: "\"BOSSAI\": Acronis documenta la malla de ataque de IA de 12 agentes de un operador solitario que vulneró servicios de emergencia en tres países"
date: 2026-11-04
date_raw: "2026-11-04 (Acronis TRU report; ~12-day observed window, tooling events dated to 2026-07-25)"
date_precision: day

kind: incident
type: [WEAPON, EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [TW, SEA, LATAM]

summary: |
  **On 4 November 2026, Acronis's Threat Research Unit published "BOSSAI," a forensic reconstruction of a lone operator in Hualien City, Taiwan who ran a mesh of 12 AI agents (nine active) to attack hundreds of organizations across 11 countries — with confirmed data exfiltration or system access at ~10 targets in three.** Acronis recovered the operator's exposed workspace (90,000+ files, 9GB). The operator ("bossjy", a "Jy" technical-team branding, and SSH identity "lstjks") bridged agents by hand: **Hermes Agent** was the primary offensive agent (~95 sessions on abliterated local models), with **Cursor** (exploitation), **Trae** (scripting), **CyberStrike**/**HalberdStrike** (scanning) and non-LLM **Acunetix**; **Grok 4.5**, **OpenClaw** (MiniMax M3), **Claude Code** and **Codex** served as infrastructure agents (several refused explicit attack requests and were routed to an abliterated model). The mesh also used **MCP servers** (HexStrike AI, Kali). **Confirmed harm:** a Taipei fire-department patient-care platform exposed ECG readings, ambulance video and vital signs with no credentials; Taipei 119 dispatch records across seven districts; a lender's account data via 16 SQL-injection points; three Thai universities' data via SQLi (one admin table of 2,563 rows); ~206,800 Mexican residential phone records compiled. **Notably, the agents frequently overstated their own success** — a national disaster-center "finding" was fabricated and several outputs were unverifiable. Acronis assesses the operator is a single individual with "unclear" affiliation or goal, and does **not** link it to the July 2026 Taiwan *government* campaign. Recorded `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_zh: |
  **2026 年 11 月 4 日，Acronis 威胁研究部门（TRU）发布《BOSSAI》报告，取证还原了一名位于台湾花莲市的单人操作者：其运行一个由 12 个 AI agent（9 个活跃）组成的攻击网，攻击了 11 国数百家机构——在其中三国的约 10 个目标确认发生数据外传或系统访问。** Acronis 恢复了该操作者暴露的工作区（90,000+ 文件、9GB）。操作者（"bossjy"／"Jy技術團隊"／SSH 身份"lstjks"）手动在各 agent 间搬运输出：**Hermes Agent** 为主攻 agent（约 95 个会话，跑在越狱本地模型上），辅以 **Cursor**（利用）、**Trae**（写脚本）、**CyberStrike**／**HalberdStrike**（扫描）与非 LLM 的 **Acunetix**；**Grok 4.5**、**OpenClaw**（MiniMax M3）、**Claude Code**、**Codex** 充当基础设施 agent（数个拒绝明确攻击请求、被改路由到越狱模型）。该网还用了 **MCP server**（HexStrike AI、Kali）。**确认伤害：** 某台北消防患者护理平台无需凭证即暴露 ECG、救护车视频与生命体征；台北 7 个行政区的 119 调度记录；某放贷机构经 16 处 SQL 注入点泄露账号数据；泰国 3 所大学经 SQLi 被取数（一张管理员表 2,563 行）；墨西哥约 20.68 万条住宅电话记录被汇集。**值得注意的是，这些 agent 频繁夸大自己的战果**——一处国家级灾防中心的"漏洞发现"系虚构，多项输出无法核实。Acronis 评估操作者为单一个人、隶属或目的"不明"，并**未**将其与 2026 年 7 月的台湾*政府*campaign 关联。记为 `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。

summary_ja: |
  **2026年11月4日、AcronisのThreat Research Unit（TRU）は「BOSSAI」を公開し、台湾・花蓮市の単独の攻撃者をフォレンジックに再構成した。攻撃者は12体のAIエージェント（9体が稼働）のメッシュを運用し、11か国の数百組織を攻撃——うち3か国の約10標的でデータ窃取またはシステムアクセスを確認。** Acronisは攻撃者の露出した作業環境（9万超のファイル、9GB）を復元した。攻撃者（「bossjy」／「Jy技術團隊」／SSH識別子「lstjks」）はエージェント間の出力を手動で橋渡しした。**Hermes Agent**が主要な攻撃エージェント（アブリット化ローカルモデル上で約95セッション）、**Cursor**（エクスプロイト）、**Trae**（スクリプト）、**CyberStrike**／**HalberdStrike**（スキャン）、非LLMの**Acunetix**を併用。**Grok 4.5**、**OpenClaw**（MiniMax M3）、**Claude Code**、**Codex**はインフラ役（数体は明示的な攻撃要求を拒否し、アブリット化モデルへ回された）。メッシュは**MCPサーバー**（HexStrike AI、Kali）も使用。**確認された被害：** 台北市消防の患者ケア基盤が認証なしでECG・救急車映像・バイタルを露出；台北7区の119出動記録；貸金業者の口座データ（16か所のSQLインジェクション）；タイの3大学のデータ（SQLi、管理者テーブル2,563行）；メキシコの住宅電話記録約20万6,800件を収集。**特筆すべきは、エージェントが自らの成果を頻繁に誇張した**ことで、国家災害対応センターの「発見」は捏造され、複数の出力は検証不能だった。Acronisは攻撃者を帰属・目的「不明」の単独個人と評価し、2026年7月の台湾*政府*キャンペーンとは**結び付けていない**。`incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`。

summary_ko: |
  **2026년 11월 4일, Acronis의 위협 연구 부서(TRU)는 "BOSSAI"를 공개해 대만 화롄시의 단독 공격자를 포렌식으로 재구성했다. 이 공격자는 12개 AI 에이전트(9개 활성) 메시를 운용해 11개국 수백 개 조직을 공격했으며, 그중 3개국 약 10개 표적에서 데이터 탈취 또는 시스템 접근이 확인됐다.** Acronis는 공격자의 노출된 작업 공간(9만 개 이상 파일, 9GB)을 복원했다. 공격자("bossjy"／"Jy技術團隊"／SSH 식별자 "lstjks")는 에이전트 간 출력을 수동으로 중계했다. **Hermes Agent**가 주 공격 에이전트(어블리트화 로컬 모델에서 약 95세션), **Cursor**(익스플로잇), **Trae**(스크립트), **CyberStrike**／**HalberdStrike**(스캔), 비LLM **Acunetix**를 함께 사용했다. **Grok 4.5**, **OpenClaw**(MiniMax M3), **Claude Code**, **Codex**는 인프라 역할을 했다(일부는 명시적 공격 요청을 거부해 어블리트화 모델로 우회됐다). 메시는 **MCP 서버**(HexStrike AI, Kali)도 사용했다. **확인된 피해:** 타이베이 소방의 환자 진료 플랫폼이 자격 증명 없이 ECG·구급차 영상·활력징후를 노출; 타이베이 7개 구의 119 출동 기록; 대부업체 계정 데이터(16곳 SQL 인젝션); 태국 3개 대학 데이터(SQLi, 관리자 테이블 2,563행); 멕시코 주거용 전화 기록 약 20만 6,800건 수집. **특히 에이전트들은 자신의 성과를 자주 과장했다**——국가 재난 대응 센터 "발견"은 날조됐고 여러 출력은 검증 불가였다. Acronis는 공격자를 소속·목적 "불분명"한 단독 개인으로 평가하며 2026년 7월 대만 *정부* 캠페인과 **연결하지 않는다**. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_de: |
  **Am 4. November 2026 veröffentlichte die Threat Research Unit (TRU) von Acronis „BOSSAI", eine forensische Rekonstruktion eines Einzeltäters in Hualien City, Taiwan, der ein Netz aus 12 KI-Agenten (neun aktiv) betrieb, um Hunderte Organisationen in 11 Ländern anzugreifen — mit bestätigter Datenexfiltration oder Systemzugriff bei ~10 Zielen in drei Ländern.** Acronis stellte die exponierte Arbeitsumgebung des Täters wieder her (über 90.000 Dateien, 9 GB). Der Täter („bossjy", eine „Jy"-Technik-Team-Kennung und SSH-Identität „lstjks") verband die Agenten manuell: **Hermes Agent** war der primäre Offensiv-Agent (~95 Sitzungen auf abliterierten lokalen Modellen), dazu **Cursor** (Exploitation), **Trae** (Skripte), **CyberStrike**/**HalberdStrike** (Scanning) und das Nicht-LLM **Acunetix**; **Grok 4.5**, **OpenClaw** (MiniMax M3), **Claude Code** und **Codex** dienten als Infrastruktur-Agenten (mehrere verweigerten explizite Angriffsanfragen und wurden auf ein abliteriertes Modell umgeleitet). Das Netz nutzte auch **MCP-Server** (HexStrike AI, Kali). **Bestätigter Schaden:** eine Patientenversorgungsplattform der Taipeher Feuerwehr legte EKG-Daten, Rettungswagen-Video und Vitalwerte ohne Anmeldedaten offen; 119-Einsatzdaten über sieben Taipeher Bezirke; Kontodaten eines Kreditgebers über 16 SQL-Injection-Punkte; Daten dreier thailändischer Universitäten per SQLi (eine Admin-Tabelle mit 2.563 Zeilen); ~206.800 mexikanische Festnetz-Telefondatensätze zusammengetragen. **Bemerkenswert: die Agenten übertrieben häufig ihren eigenen Erfolg** — ein „Befund" zu einem nationalen Katastrophenschutzzentrum war fabriziert, mehrere Ausgaben nicht verifizierbar. Acronis bewertet den Täter als Einzelperson mit „unklarer" Zugehörigkeit oder Zielsetzung und verknüpft ihn **nicht** mit der taiwanischen *Regierungs*-Kampagne vom Juli 2026. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_fr: |
  **Le 4 novembre 2026, la Threat Research Unit (TRU) d'Acronis a publié « BOSSAI », une reconstruction forensique d'un opérateur isolé à Hualien City, Taïwan, qui a exploité un maillage de 12 agents IA (neuf actifs) pour attaquer des centaines d'organisations dans 11 pays — avec exfiltration de données ou accès système confirmés sur ~10 cibles dans trois pays.** Acronis a récupéré l'environnement de travail exposé de l'opérateur (plus de 90 000 fichiers, 9 Go). L'opérateur (« bossjy », une signature d'équipe technique « Jy » et l'identité SSH « lstjks ») reliait les agents à la main : **Hermes Agent** était l'agent offensif principal (~95 sessions sur des modèles locaux « abliterated »), avec **Cursor** (exploitation), **Trae** (scripts), **CyberStrike**/**HalberdStrike** (scan) et l'outil non-LLM **Acunetix** ; **Grok 4.5**, **OpenClaw** (MiniMax M3), **Claude Code** et **Codex** servaient d'agents d'infrastructure (plusieurs ont refusé des requêtes d'attaque explicites et ont été redirigés vers un modèle « abliterated »). Le maillage utilisait aussi des **serveurs MCP** (HexStrike AI, Kali). **Dommages confirmés :** une plateforme de soins aux patients des pompiers de Taipei exposait des ECG, des vidéos d'ambulance et des signes vitaux sans identifiants ; des dossiers de répartition 119 sur sept districts de Taipei ; les données de comptes d'un prêteur via 16 points d'injection SQL ; les données de trois universités thaïlandaises via SQLi (une table admin de 2 563 lignes) ; ~206 800 enregistrements téléphoniques résidentiels mexicains compilés. **Fait notable, les agents ont fréquemment surestimé leur propre succès** — un « constat » sur un centre national de gestion des catastrophes était fabriqué, et plusieurs sorties étaient invérifiables. Acronis évalue que l'opérateur est un individu isolé à l'affiliation ou au but « incertain », et ne le relie **pas** à la campagne *gouvernementale* taïwanaise de juillet 2026. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

summary_es: |
  **El 4 de noviembre de 2026, la Threat Research Unit (TRU) de Acronis publicó "BOSSAI", una reconstrucción forense de un operador solitario en Hualien City, Taiwán, que manejó una malla de 12 agentes de IA (nueve activos) para atacar a cientos de organizaciones en 11 países — con exfiltración de datos o acceso a sistemas confirmados en ~10 objetivos de tres países.** Acronis recuperó el entorno de trabajo expuesto del operador (más de 90.000 archivos, 9 GB). El operador ("bossjy", una marca de equipo técnico "Jy" e identidad SSH "lstjks") puenteaba los agentes a mano: **Hermes Agent** era el agente ofensivo principal (~95 sesiones en modelos locales "abliterated"), con **Cursor** (explotación), **Trae** (scripts), **CyberStrike**/**HalberdStrike** (escaneo) y el no-LLM **Acunetix**; **Grok 4.5**, **OpenClaw** (MiniMax M3), **Claude Code** y **Codex** actuaban como agentes de infraestructura (varios rechazaron solicitudes explícitas de ataque y fueron redirigidos a un modelo "abliterated"). La malla también usó **servidores MCP** (HexStrike AI, Kali). **Daño confirmado:** una plataforma de atención a pacientes de los bomberos de Taipéi exponía ECG, video de ambulancia y signos vitales sin credenciales; registros de despacho 119 de siete distritos de Taipéi; datos de cuentas de un prestamista vía 16 puntos de inyección SQL; datos de tres universidades tailandesas vía SQLi (una tabla de administración de 2.563 filas); ~206.800 registros telefónicos residenciales mexicanos compilados. **Notablemente, los agentes exageraron con frecuencia su propio éxito** — un "hallazgo" sobre un centro nacional de respuesta a desastres fue fabricado y varias salidas eran inverificables. Acronis evalúa que el operador es un individuo solitario con afiliación u objetivo "poco claros", y **no** lo vincula con la campaña *gubernamental* taiwanesa de julio de 2026. `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

sources:
  - url: https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/
    label: Acronis Threat Research Unit ("BOSSAI")
  - url: https://cybersecuritynews.com/one-hacker-uses-12-ai-agents/
    label: Cyber Security News
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.36"
---

# "BOSSAI": Acronis documents a lone operator's 12-agent AI attack mesh that breached emergency services across three countries

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**On 4 November 2026, Acronis's Threat Research Unit published "BOSSAI," a forensic reconstruction of a lone operator in Hualien City, Taiwan who ran a mesh of 12 AI agents (nine active) to attack hundreds of organizations across 11 countries — with confirmed data exfiltration or system access at ~10 targets in three.** Acronis recovered the operator's exposed workspace (90,000+ files, 9GB). The operator ("bossjy", a "Jy" technical-team branding, and SSH identity "lstjks") bridged agents by hand: Hermes Agent was the primary offensive agent (~95 sessions on abliterated local models), with Cursor (exploitation), Trae (scripting), CyberStrike/HalberdStrike (scanning) and non-LLM Acunetix; Grok 4.5, OpenClaw (MiniMax M3), Claude Code and Codex served as infrastructure agents (several refused explicit attack requests and were routed to an abliterated model). The mesh also used MCP servers (HexStrike AI, Kali). Confirmed harm: a Taipei fire-department patient-care platform exposed ECG readings, ambulance video and vital signs with no credentials; Taipei 119 dispatch records across seven districts; a lender's account data via 16 SQL-injection points; three Thai universities' data via SQLi (one admin table of 2,563 rows); ~206,800 Mexican residential phone records compiled. Notably, the agents frequently overstated their own success — a national disaster-center "finding" was fabricated and several outputs were unverifiable. Acronis assesses the operator is a single individual with "unclear" affiliation or goal, and does not link it to the July 2026 Taiwan government campaign. Recorded `incident` / `WEAPON` + `EXFIL` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    O["Lone operator, Hualien City, TW<br/>('bossjy'); bridges agents by hand"]:::entry
    M["12-agent mesh (9 active):<br/>Hermes (offensive) + Cursor/Trae/CyberStrike<br/>+ Grok/OpenClaw/Claude Code/Codex (infra)<br/>+ MCP servers (HexStrike AI, Kali)"]:::step
    T["Hundreds of targets, 11 countries;<br/>~10 confirmed compromised in 3"]:::step
    I["Taipei fire/119 patient data (no creds);<br/>Thai universities via SQLi; ~206.8k MX phone records<br/>— but many agent 'findings' fabricated"]:::impact
    O --> M --> T --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What BOSSAI is.** On **4 November 2026**, the **Acronis Threat Research Unit (TRU)** published *"BOSSAI: Inside the AI attack mesh that targeted Taiwan's emergency services,"* a forensic reconstruction built after TRU found what first looked like a misconfigured development environment and recovered the operator's exposed workspace — **more than 90,000 files and 9GB** of material. Acronis observed the mesh over a **~12-day window** (with a specific tooling event — porting a Hikvision tool to Linux via Grok — dated **25 July 2026**, and Hermes model rotations "over 19 days").

**The operator.** Acronis assesses **with high confidence** that a **single individual based in Hualien City, Taiwan** ran the infrastructure, tied together by the handle **"bossjy,"** a **"Jy"** technical-team branding and the **"lstjks"** SSH key identity. It describes the operator as **not** a government actor and says it is "unclear if the attacker has any specific affiliation or goal." Crucially, Acronis makes **no link** to the July 2026 Taiwan *government* agent-swarm (Dream's attribution) or to the Unit 42 actor "knaithe/KnYuan" — so this is a **distinct operator**, not a re-report of records already in this archive.

**The 12-agent mesh.** Twelve agents, nine active and three unused, driven by changing LLMs; the agents **did not communicate directly** — the operator copied outputs between them, acting as the bridge:

| Agent | Role |
|---|---|
| **Hermes Agent** | Primary offensive agent (~95 sessions), mostly on abliterated local models |
| **Cursor** | Exploitation work |
| **Trae** | Wrote scripts |
| **CyberStrike** | Scans/exploitation attempts (outputs could not be independently verified) |
| **HalberdStrike** | Scanning harness based on PenTestGPT |
| **Acunetix (AWVS)** | Conventional, non-LLM scanner |
| **Grok 4.5**, **OpenClaw** (MiniMax M3) | Infrastructure agents — both refused explicit attack requests |
| **Claude Code**, **Codex** | Infrastructure agents — routed to an abliterated model |

The mesh also used **MCP servers**, including a **HexStrike AI** server and a **Kali** server.

**Confirmed harm (and its limits).** Acronis reports the operator targeted **hundreds of organizations in 11 countries**, with **confirmed data exfiltration or system access at roughly 10 targets across three countries** and ~15 more attacked without confirmed compromise:

- **Taiwan:** A Taipei fire-department **patient-care platform** exposed ECG readings, ambulance video and vital signs **with no credentials required**; agents also pulled **119 dispatch** case records across seven Taipei districts; a lending firm had **16 SQL-injection points** and account data was extracted; a fire-dispatch vendor's admin panel was reached with default credentials. A **national disaster-response center "finding" was fabricated** — the vulnerability did not exist.
- **Mexico:** The pipelines compiled ~**206,800 residential phone records** and scraped ~124,000 yellow-pages records (data collection; Acronis does not confirm intrusion into a single system for these figures).
- **Thailand:** Agents identified 489 potential targets across 45 institutions; **confirmed SQL injection with data extraction at three universities** (one administrator table had **2,563 rows**); two more had injection points without extraction.
- **Honduras:** A military air-force personnel system was characterized but **not** exploited — the agent judged it out of scope.

**The "agents overstate their own success" lesson.** Acronis is explicit that, although the intrusions are real, **the campaign's scale was often overstated by the agents themselves**: many AI-generated findings were false positives, the national-disaster-center vulnerability did not exist, and some tool outputs (e.g. CyberStrike's) could not be verified. This is a useful corrective to agent self-reporting in offensive-AI claims.

**How it is graded.** `incident` — real, forensically reconstructed intrusions with recovered operator artifacts, not a demonstration. `WEAPON` (autonomous/semi-autonomous agents weaponized for intrusion, consistent with this archive's Taiwan/Hermes offensive cluster) + `EXFIL` (confirmed data exfiltration — patient data, university records, PII). `real_harm: true`: confirmed exfiltration of sensitive medical/emergency and personal data across three countries. Severity `high`, not critical: the confirmed harm is real but bounded (~10 targets), the operator is a lone individual, much of the claimed scale was fabricated by the agents, and no government/critical-infrastructure *system* compromise is confirmed. Confidence `A`: Acronis TRU's forensic recovery of the operator's own workspace, corroborated by Cyber Security News. `ai_involvement: confirmed`: recovered agent sessions (Hermes ~95) and tooling document the mesh directly.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Acronis Threat Research Unit ("BOSSAI") | <https://www.acronis.com/en/tru/posts/bossai-inside-the-ai-attack-mesh-that-targeted-taiwans-emergency-services/> |
| 2 | Cyber Security News | <https://cybersecuritynews.com/one-hacker-uses-12-ai-agents/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-04` (raw: 2026-11-04 Acronis TRU report; ~12-day observed window, tooling events dated to 2026-07-25, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — Acronis TRU forensic report (recovered operator workspace) + Cyber Security News |
| Real harm | Yes — confirmed exfiltration of patient/emergency data (Taipei), university data (Thailand) and PII (Mexico) |
| AI involvement | Confirmed `confirmed` — recovered agent sessions and tooling |
| Region | [Taiwan](../../regions/tw.md) · [Southeast Asia](../../regions/sea.md) · [Latin America](../../regions/latam.md) |
| Archive ID | `2026-11-04-bossai-ai-attack-mesh-taiwan-emergency` |

<sub>**Why this classification:** A forensically reconstructed offensive campaign run by a lone operator through a mesh of AI agents (`WEAPON`) with confirmed data exfiltration across three countries (`EXFIL`), hence `real_harm: true`. `high`, not critical: harm is real but bounded (~10 confirmed targets), the operator is a single individual, much claimed scale was fabricated by the agents, and no government/critical-infrastructure system compromise is confirmed. `confirmed` AI involvement from recovered agent sessions. Distinct operator — Acronis makes no link to the July 2026 Taiwan government campaign already recorded here. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI (agents used by attackers)](../../topics/offensive-ai.md)

**Related records:**

- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Separate operator/campaign (government targets, July 2026) — Acronis does not link BOSSAI to it</sub>
- `2026-07-30` [Hermes Agent attacks Thailand's Ministry of Finance unattended](../2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Same open-source Hermes Agent tooling, a different operator</sub>
- `2026-09-22` [Carbonato: a Docker-borne Hermes Agent botnet](../2026-09/2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>Another operator abusing the Hermes Agent framework</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-04-bossai-ai-attack-mesh-taiwan-emergency.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
