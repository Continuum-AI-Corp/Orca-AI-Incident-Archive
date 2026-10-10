---
id: 2026-10-06-artex-ai-south-korea-banks
title: "An open-source agentic pen-test tool (ARTEX) is tied to breaches at seven South Korean banks"
title_zh: "一款开源 agentic 渗透测试工具（ARTEX）被关联到韩国七家银行的入侵"
title_ja: "オープンソースのagentic侵入テストツール（ARTEX）が韓国7行の侵害に関連づけられる"
title_ko: "오픈소스 agentic 침투테스트 도구(ARTEX)가 한국 7개 은행 침해와 연관됐다"
title_de: "Ein quelloffenes agentisches Pentest-Tool (ARTEX) wird mit Einbrüchen bei sieben südkoreanischen Banken in Verbindung gebracht"
title_fr: "Un outil de pentest agentique open-source (ARTEX) est lié à des intrusions chez sept banques sud-coréennes"
title_es: "Una herramienta agéntica de pentest de código abierto (ARTEX) se vincula a brechas en siete bancos surcoreanos"
date: 2026-10-06
date_raw: "campaign from 2026-09-28; public disclosure 2026-10-06"
date_precision: day

kind: incident
type: [WEAPON, EXFIL]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [KR]

summary: |
  **Between about 28 September and early October 2026, attackers breached at least **seven South Korean financial institutions** — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings, Welcome Savings and Hyundai Capital — exposing **roughly 66,000 individuals' records (reports range 65,000–68,000) plus ~2,200 corporate records**; investigators tracing the attack logs attribute the activity to **ARTEX, an open-source "autonomous penetration-testing" tool driven by multiple AI agents running on commercial models.**** South Korea's president publicly acknowledged on **6 October** that "signs have emerged of AI being used." The intruders hit **internet-facing auxiliary systems** — loan-agent lookup portals, employee mobile work-support and sales-support apps — and did **not** reach core banking, which stays physically network-separated under Korean regulation. The worst single losses: Shinhan ~25,000 customers (including 66 national ID numbers) and Yegaram Savings ~40,000 people. The Financial Security Institute's assessment is that the **AI "did not act independently without human involvement"** — a human-directed operation using an agentic tool. Attribution of the operator is uncertain (the tool is public and the IPs globally distributed), and **no regulator has formally confirmed the ARTEX link**, which rests on attack-log analysis. Regulators responded by **suspending a planned round of network-separation deregulation**. Recorded `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`.

summary_zh: |
  **2026 年约 9 月 28 日至 10 月初，攻击者攻破至少 **七家韩国金融机构**——新韩、KB 国民、Hana、BNK 釜山、Yegaram 储蓄、Welcome 储蓄与现代资本——泄露 **约 6.6 万人记录（各源 6.5 万–6.8 万）及约 2200 条企业记录**；调查者据攻击日志把活动关联到 **ARTEX——一款由多个 AI agent（跑在商用模型上）驱动的开源"自主渗透测试"工具。**** 韩国总统于 **10 月 6 日**公开表示"已出现使用 AI 的迹象"。入侵者打的是**面向互联网的外围系统**——贷款中介查询门户、员工移动办公支持与销售支持应用——并**未**触及核心银行（按韩国监管核心系统物理网络隔离）。单家损失最重：新韩约 2.5 万客户（含 66 个身份证号）、Yegaram 储蓄约 4 万人。金融安全院的研判是 **AI "并非在无人参与下独立行动"**——一次由人主导、使用 agentic 工具的行动。操作者归因不明（工具公开、IP 全球分散），且**没有监管机构正式确认 ARTEX 关联**，该关联基于攻击日志分析。监管方作出的反应是**暂停一轮原定的网络隔离放松**。记为 `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`。

summary_ja: |
  **2026年9月28日頃から10月初旬にかけて、攻撃者は少なくとも**韓国の7金融機関**——新韓、KB国民、ハナ、BNK釜山、Yegaram貯蓄、Welcome貯蓄、現代キャピタル——を侵害し、**約6万6千人分の記録（各報道で6.5万〜6.8万）と約2,200件の法人記録**を露出させた。攻撃ログを追った調査は、この活動を**ARTEX——商用モデル上で動く複数のAIエージェントによって駆動されるオープンソースの「自律的侵入テスト」ツール**に帰属させている。** 韓国大統領は**10月6日**に「AIが使われた兆候が出ている」と公に認めた。侵入者が突いたのは**インターネットに面した補助系統**——ローン仲介照会ポータル、従業員モバイル支援・営業支援アプリ——で、韓国規制下で物理的にネットワーク分離されたコア банキングには**到達していない**。最大の被害：新韓 約2.5万人（国民登録番号66件を含む）、Yegaram貯蓄 約4万人。金融保安院の評価は、**AIが「人の関与なしに独立して行動したわけではない」**——agenticツールを用いた人間主導の作戦だ。実行者の帰属は不確か（ツールは公開、IPは世界各地）で、**ARTEXとの関連を正式に確認した規制当局はない**（攻撃ログ解析に基づく）。規制側は**予定していたネットワーク分離の規制緩和の一巡を停止**した。`incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`

summary_ko: |
  **2026년 9월 28일경부터 10월 초 사이, 공격자가 최소 **한국 7개 금융기관**——신한, KB국민, 하나, BNK부산, 예가람저축, 웰컴저축, 현대캐피탈——을 침해해 **약 6만 6천 명의 기록(보도별 6.5만~6.8만)과 약 2,200건의 법인 기록**을 노출시켰다. 공격 로그를 추적한 조사는 이 활동을 **ARTEX——상용 모델 위에서 동작하는 다수 AI 에이전트로 구동되는 오픈소스 "자율 침투테스트" 도구**에 연결한다.** 한국 대통령은 **10월 6일** "AI가 사용된 정황이 나타났다"고 공개적으로 인정했다. 침입자는 **인터넷에 노출된 보조 시스템**——대출모집인 조회 포털, 임직원 모바일 업무지원·영업지원 앱——을 공략했고, 한국 규제상 물리적으로 망분리된 코어뱅킹에는 **도달하지 못했다**. 최대 피해: 신한 약 2.5만 고객(주민등록번호 66건 포함), 예가람저축 약 4만 명. 금융보안원의 판단은 **AI가 "사람의 개입 없이 독립적으로 행동하지 않았다"**——agentic 도구를 사용한 인간 주도 작전이다. 공격자 귀속은 불확실하며(도구가 공개돼 있고 IP가 전 세계 분산), **ARTEX 연관을 공식 확인한 규제기관은 없다**(공격 로그 분석에 근거). 규제 당국은 **예정됐던 망분리 규제완화 한 차례를 중단**했다. `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`

summary_de: |
  **Zwischen etwa dem 28. September und Anfang Oktober 2026 kompromittierten Angreifer mindestens **sieben südkoreanische Finanzinstitute** — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings, Welcome Savings und Hyundai Capital — und legten **rund 66.000 Personendatensätze (Berichte nennen 65.000–68.000) sowie ~2.200 Unternehmensdatensätze** offen; Ermittler führen die Aktivität anhand der Angriffsprotokolle auf **ARTEX zurück, ein quelloffenes „autonomes Penetrationstest"-Tool, das von mehreren KI-Agenten auf kommerziellen Modellen angetrieben wird.**** Südkoreas Präsident räumte am **6. Oktober** öffentlich ein, es gebe „Anzeichen für den Einsatz von KI". Die Eindringlinge trafen **internetseitige Hilfssysteme** — Kreditvermittler-Portale, Mitarbeiter-Mobil- und Vertriebsunterstützung — und erreichten **nicht** das Kernbankensystem, das in Korea physisch netzgetrennt bleibt. Größte Einzelverluste: Shinhan ~25.000 Kunden (inkl. 66 nationale ID-Nummern), Yegaram Savings ~40.000 Personen. Die Einschätzung des Financial Security Institute: Die **KI habe „nicht ohne menschliche Beteiligung eigenständig gehandelt"** — eine menschengesteuerte Operation mit einem agentischen Werkzeug. Die Zuordnung des Täters ist unsicher (öffentliches Tool, global verteilte IPs), und **keine Behörde hat die ARTEX-Verbindung formell bestätigt** (sie beruht auf Log-Analyse). Die Regulierer **setzten eine geplante Runde der Netztrennungs-Deregulierung aus**. `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`

summary_fr: |
  **Entre le 28 septembre environ et début octobre 2026, des attaquants ont compromis au moins **sept institutions financières sud-coréennes** — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings, Welcome Savings et Hyundai Capital — exposant **environ 66 000 dossiers de particuliers (les sources citent 65 000 à 68 000) plus ~2 200 dossiers d'entreprises** ; en remontant les journaux d'attaque, les enquêteurs attribuent l'activité à **ARTEX, un outil open-source de « test d'intrusion autonome » animé par plusieurs agents IA tournant sur des modèles commerciaux.**** Le président sud-coréen a reconnu publiquement le **6 octobre** que « des signes d'utilisation de l'IA sont apparus ». Les intrus ont visé des **systèmes auxiliaires exposés à internet** — portails de courtiers en prêts, applications de support mobile des employés et de support des ventes — et n'ont **pas** atteint le cœur bancaire, qui reste physiquement isolé du réseau selon la réglementation coréenne. Pertes individuelles les plus lourdes : Shinhan ~25 000 clients (dont 66 numéros d'identité nationale), Yegaram Savings ~40 000 personnes. L'évaluation du Financial Security Institute : l'**IA « n'a pas agi de façon indépendante sans intervention humaine »** — une opération dirigée par un humain au moyen d'un outil agentique. L'attribution de l'opérateur est incertaine (outil public, IP réparties mondialement), et **aucun régulateur n'a formellement confirmé le lien avec ARTEX** (il repose sur l'analyse des journaux). Les régulateurs ont réagi en **suspendant une série prévue de déréglementation de la séparation des réseaux**. `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`

summary_es: |
  **Entre aproximadamente el 28 de septiembre y principios de octubre de 2026, atacantes vulneraron al menos **siete instituciones financieras surcoreanas** — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings, Welcome Savings e Hyundai Capital — exponiendo **unos 66 000 registros de personas (las fuentes citan 65 000–68 000) más ~2 200 registros corporativos**; al rastrear los registros del ataque, los investigadores atribuyen la actividad a **ARTEX, una herramienta de código abierto de "pruebas de penetración autónomas" impulsada por múltiples agentes de IA que corren sobre modelos comerciales.**** El presidente de Corea del Sur reconoció públicamente el **6 de octubre** que "han surgido indicios del uso de IA". Los intrusos golpearon **sistemas auxiliares expuestos a internet** — portales de corredores de préstamos, apps de soporte móvil de empleados y de soporte de ventas — y **no** alcanzaron la banca central, que permanece físicamente separada de la red por regulación coreana. Las mayores pérdidas individuales: Shinhan ~25 000 clientes (incluidos 66 números de identidad nacional), Yegaram Savings ~40 000 personas. La evaluación del Financial Security Institute: la **IA "no actuó de forma independiente sin intervención humana"** — una operación dirigida por humanos con una herramienta agéntica. La atribución del operador es incierta (herramienta pública, IP distribuidas globalmente), y **ningún regulador ha confirmado formalmente el vínculo con ARTEX** (se basa en el análisis de registros). Los reguladores respondieron **suspendiendo una ronda prevista de desregulación de la separación de redes**. `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`

sources:
  - url: https://www.americanbanker.com/news/ai-linked-hacks-hit-korean-banks-through-loan-agent-sites
    label: American Banker
  - url: https://mbiz.heraldcorp.com/article/10892497
    label: The Herald Business (exclusive)
  - url: https://www.techtimes.com/articles/328541/20261005/open-source-ai-agent-hacked-seven-south-korean-banks-exposing-65000-records.htm
    label: Tech Times
  - url: https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/
    label: CrowdStrike (9 October follow-up)
  - url: https://securityaffairs.com/200661/hacking/ai-driven-tool-artex-used-in-attacks-against-south-korean-banks.html
    label: Security Affairs
  - url: https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html
    label: The Hacker News (developer response)
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.27"
---

# An open-source agentic pen-test tool (ARTEX) is tied to breaches at seven South Korean banks

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**Between about 28 September and early October 2026, attackers breached at least seven South Korean financial institutions — Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings, Welcome Savings and Hyundai Capital — exposing roughly 66,000 individuals' records (reports range 65,000–68,000) plus ~2,200 corporate records; investigators tracing the attack logs attribute the activity to ARTEX, an open-source "autonomous penetration-testing" tool driven by multiple AI agents running on commercial models.** South Korea's president publicly acknowledged on **6 October** that "signs have emerged of AI being used." The intruders hit **internet-facing auxiliary systems** — loan-agent lookup portals, employee mobile work-support and sales-support apps — and did **not** reach core banking, which stays physically network-separated under Korean regulation. The worst single losses: Shinhan ~25,000 customers (including 66 national ID numbers) and Yegaram Savings ~40,000 people. The Financial Security Institute's assessment is that the **AI "did not act independently without human involvement"** — a human-directed operation using an agentic tool. Attribution of the operator is uncertain (the tool is public and the IPs globally distributed), and **no regulator has formally confirmed the ARTEX link**, which rests on attack-log analysis. Regulators responded by **suspending a planned round of network-separation deregulation**. Recorded `incident` / `WEAPON` + `EXFIL` / `critical` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Operator points an open-source agentic<br/>pen-test tool (ARTEX) at Korean lenders"]:::entry
    S1["Agents hit internet-facing auxiliary systems:<br/>loan-agent portals, employee / sales support"]:::step
    S2["Credential abuse + record extraction;<br/>30–43h dwell before detection"]:::step
    I["7 institutions, ~66,000 people + ~2,200 firms;<br/>core banking (network-separated) untouched"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** Over roughly a week beginning **28 September 2026**, at least **seven South Korean financial institutions** were breached: Shinhan, KB Kookmin, Hana, BNK Busan, Yegaram Savings Bank, Welcome Savings Bank and Hyundai Capital. Reported totals cluster around **66,000 individuals (65,000–68,000 across outlets) and about 2,200 corporate records**. The heaviest single hits were **Shinhan (~25,000 customers, including 66 resident-registration/national ID numbers)** and **Yegaram Savings Bank (~40,000 people)**; other banks lost far smaller sets (tens to low hundreds of records). The attackers reached **internet-facing auxiliary systems** — a loan-recruiter lookup service, an employee mobile work-support system, and sales-support applications — and, critically, did **not** breach the banks' **core banking systems, which remain physically network-separated** under Korean regulation. Dwell times before detection ran to roughly **30–43 hours**.

**The AI angle, stated carefully.** Investigators tracing attack IPs and server logs — Shinhan was the first to report — found evidence pointing to **ARTEX**, an **open-source "autonomous penetration-testing" tool that describes itself as driven by multiple AI agents running on commercial models (Anthropic or OpenAI)**. Two cautions belong on this record: (1) **the ARTEX link is suspected from log analysis, not formally confirmed by any regulator** — American Banker notes "no regulator has publicly confirmed" it; and (2) the operator is **unattributed**, precisely because the tool is public and the source IPs are globally distributed. South Korea's **Financial Security Institute** said the **AI "did not act independently without human involvement"** — i.e. a human-directed operation using an agentic tool, which is why this is `WEAPON` rather than `ROGUE`. South Korea's president acknowledged on **6 October** that "signs have emerged of AI being used."

**Why it is recorded, and how graded.** This is a **confirmed real-world breach of seven financial institutions** with tens of thousands of customers' personal data (including national ID numbers) taken — `real_harm: true`, and `critical` under the archive's multi-organisation-damage trigger. `WEAPON` (a human wielding an agentic pen-test tool as an attack weapon) + `EXFIL` (customer records extracted). Confidence `A` for the incident itself — acknowledged by the president and the Financial Security Institute and reported across major outlets — while the **ARTEX attribution is held as "traced/suspected, not formally confirmed"** in the text. The regulatory aftermath is notable: authorities **suspended a planned round of network-separation deregulation**, crediting the physical separation of core banking for limiting the damage.

**Update (9 October 2026) — CrowdStrike analyses the operator's own working files.** CrowdStrike published a follow-up built on **open directories left exposed on attacker-controlled servers**, which it says provide *"direct insight into the threat actor's operational methodology and tooling."* Exposed on those servers were **Claude Code session histories, ARTEX configuration files and Claude memory files**; one directory held a `CLAUDE.md` at `38.244.50[.]120:18899/.claude/CLAUDE.md` containing *"a Chinese-language pentesting prompt that specified how the LLM should conduct pentesting activities."* The sessions show a **two-server setup** (a Hong Kong address as the operator's main infrastructure; `38.244.50[.]120` running the ARTEX instance behind the Korean attacks), with **DeepSeek v4.1-flash as the main model and GLM-5.3 (Zhipu AI) and Grok 4.6 used for additional sessions**, likely reached through a reseller (`xcai[.]pro`), plus nine proxy IPs listed in the report. CrowdStrike **does not link the activity to a specific group** and assesses with moderate confidence that the operator is **Chinese-speaking and financially motivated**; industry reporting still has not confirmed how many organisations were hit. The operator also queried the model about where stolen Korean data is typically sold and how to find Korean data-sale channels on Telegram; the session dumps surfaced what may be operator personal details, which are omitted here per Security Affairs' own caution. Separately, ARTEX's developer (Autumn-27) has **closed the source code and stopped updates**, saying the tool was built for learning and research and that these attacks are unrelated to the project. This update enriches the record with the same incident's follow-up primary analysis; the attribution stance is unchanged — tool use traced/suspected, operator assessed (not formally attributed).

## Sources

| # | Source | Link |
|---|---|---|
| 1 | American Banker | <https://www.americanbanker.com/news/ai-linked-hacks-hit-korean-banks-through-loan-agent-sites> |
| 2 | The Herald Business (exclusive) | <https://mbiz.heraldcorp.com/article/10892497> |
| 3 | Tech Times | <https://www.techtimes.com/articles/328541/20261005/open-source-ai-agent-hacked-seven-south-korean-banks-exposing-65000-records.htm> |
| 4 | CrowdStrike — "Unknown threat actor uses ARTEX to target South Korean finance" (9 October follow-up) | <https://www.crowdstrike.com/en-us/blog/unknown-threat-actor-uses-artex-to-target-south-korean-finance/> |
| 5 | Security Affairs | <https://securityaffairs.com/200661/hacking/ai-driven-tool-artex-used-in-attacks-against-south-korean-banks.html> |
| 6 | The Hacker News — ARTEX developer response | <https://thehackernews.com/2026/10/artex-ai-pentesting-tool-used-in-data.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-06` (raw: campaign from 2026-09-28; public disclosure 2026-10-06, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **Critical** `critical` |
| Confidence | **A** — the breach is acknowledged by the president and the Financial Security Institute and widely reported; the ARTEX attribution is traced, not formally confirmed |
| Real harm | Yes — ~66,000 people's records (incl. national IDs) taken from seven financial institutions |
| AI involvement | Confirmed `confirmed` |
| Region | [South Korea](../../regions/kr.md) |
| Archive ID | `2026-10-06-artex-ai-south-korea-banks` |

<sub>**Why this classification:** A human-directed operation that used an open-source agentic pen-test tool against seven banks (`WEAPON`) and extracted customer records (`EXFIL`). `critical` under the multi-organisation confirmed-damage trigger — seven financial institutions, ~66,000 people's data including national IDs. `real_harm: true`. Confidence `A` for the breach (presidential and Financial Security Institute acknowledgement plus major-outlet reporting); the **ARTEX tool attribution is explicitly held as log-traced/suspected rather than formally confirmed**, and the operator is unattributed. Dated to the 6 October public disclosure; the campaign ran from ~28 September (kept in `date_raw`). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md). Enriched on 10 October 2026 with CrowdStrike's 9 October follow-up analysis of the operator's exposed working files (see Details).</sub>

## Related

**Topic:** [Offensive AI capability evolution (WEAPON)](../../topics/offensive-ai.md)

**Related records:**

- `2025-11-13` [GTG-1002: the first AI-orchestrated espionage campaign](../2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br>  <sub>The reference point for a human operator driving an agent through most of an intrusion</sub>
- `2025-09-01` [Villager / CyberSpike: a weaponised autonomous pen-test framework](../2025-09/2025-09-01-villager-cyberspike-shen-tou-gong.md)<br>  <sub>An offensive pen-test agent turned attack tool — the same tool class as ARTEX</sub>
- `2026-09-22` [Gambit: an AI agent steals retail payment-card data](../2026-09/2026-09-22-gambit-ai-agent-retail-card-theft.md)<br>  <sub>Another financially-motivated agent-driven data theft, weeks earlier</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-06-artex-ai-south-korea-banks.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
