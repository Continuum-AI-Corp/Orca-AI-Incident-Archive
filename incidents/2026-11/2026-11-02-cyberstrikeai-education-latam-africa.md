---
id: 2026-11-02-cyberstrikeai-education-latam-africa
title: "CyberStrikeAI in the wild: an LLM-orchestrated intrusion reaches domain admin at education targets in Latin America and Africa"
title_zh: "CyberStrikeAI 实战：LLM 编排的入侵在拉美与非洲教育目标处拿下域管理员"
title_ja: "CyberStrikeAIの実戦投入：LLMが編成する侵入がラテンアメリカとアフリカの教育機関でドメイン管理者を掌握"
title_ko: "실전의 CyberStrikeAI: LLM이 편성한 침입이 라틴아메리카·아프리카 교육 표적에서 도메인 관리자를 장악"
title_de: "CyberStrikeAI im Einsatz: ein LLM-orchestrierter Einbruch erlangt Domänen-Admin bei Bildungszielen in Lateinamerika und Afrika"
title_fr: "CyberStrikeAI en conditions réelles : une intrusion orchestrée par LLM atteint l'admin de domaine chez des cibles éducatives d'Amérique latine et d'Afrique"
title_es: "CyberStrikeAI en la práctica: una intrusión orquestada por LLM alcanza el administrador de dominio en objetivos educativos de América Latina y África"
date: 2026-11-02
date_raw: "2026-11-02 (Kaspersky press release / Securelist report; intrusions observed Sept–Oct 2026)"
date_precision: day

kind: incident
type: [WEAPON, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 2 November 2026, Kaspersky (press release + a Securelist report, "CyberStrikeAI in the wild") documented real-world intrusions at education-sector organizations across several countries in Latin America and Africa, in which an LLM orchestrator drove the post-exploitation.** CyberStrikeAI is an open-source, Go-based AI penetration-testing framework; in these attacks the **LLM ran on the attacker's C2 server** (selecting tools, writing commands, reading results) while the on-host **implant carried no AI and simply executed tasks**. Kaspersky reconstructed one case: a human operator first breached a likely-exposed **Microsoft SQL Server** (`sqlservr.exe` 16.0.1000) over ~24h, **paused ~2 weeks**, then deployed the CyberStrikeAI beacon — which set **persistence** (a `SystemUpdate` scheduled task) within **~2 minutes**, ran LDAP **domain recon** (~5h), moved laterally over SMB/WMI, dumped registry hives and **lsass via comsvcs.dll**, and ran **DCSync + Golden Ticket** with a renamed Mimikatz. **Domain controllers were compromised within 3–4 days of implant deployment**; the final stage was data collection (database records from the SQL server, files from network resources). Kaspersky does **not** attribute the activity to a known group and cannot confirm a single operator across infrastructure; Chinese-language script comments, use of Chinese services (DNSLog.cn) and UTC+8 restart timing **suggest** a Chinese-speaking operator. Recorded `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

summary_zh: |
  **2026 年 11 月 2 日，Kaspersky（新闻稿 + Securelist 报告《CyberStrikeAI in the wild》）记录了拉美与非洲数国教育行业机构遭遇的真实入侵——其后利用阶段由一个 LLM 编排器驱动。** CyberStrikeAI 是一款基于 Go 的开源 AI 渗透测试框架；在这些攻击中，**LLM 跑在攻击者的 C2 服务器上**（选择工具、编写命令、解析结果），而落地主机上的**植入体不含 AI、只负责执行任务**。Kaspersky 还原了其中一例：人工操作者先在约 24 小时内攻破一台很可能暴露在外的 **Microsoft SQL Server**（`sqlservr.exe` 16.0.1000），**停歇约 2 周**，随后投放 CyberStrikeAI beacon——该 beacon 在 **约 2 分钟** 内建立**持久化**（一个名为 `SystemUpdate` 的计划任务）、做 LDAP **域侦察**（约 5 小时）、经 SMB/WMI 横向移动、转储注册表 hive 并**用 comsvcs.dll 掏 lsass**、再以改名的 Mimikatz 执行 **DCSync + Golden Ticket**。**在植入体部署后 3–4 天内域控被攻陷**；最后阶段是数据采集（从 SQL server 取库记录、从网络资源取文件）。Kaspersky **未**将该活动归于任何已知团伙，也无法确认各基础设施背后是同一操作者；脚本中的中文注释、对中文服务（DNSLog.cn）的使用、以及 UTC+8 的重启时间**暗示**是一名中文使用者。记为 `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`。

summary_ja: |
  **2026年11月2日、Kaspersky（プレスリリース＋Securelistレポート「CyberStrikeAI in the wild」）は、ラテンアメリカとアフリカの複数国の教育機関で起きた実世界の侵入を記録した。ポストエクスプロイトはLLMオーケストレーターが駆動した。** CyberStrikeAIはGo製のオープンソースAIペネトレーションテスト基盤で、これらの攻撃では**LLMが攻撃者のC2サーバー上で動作**（ツール選択・コマンド生成・結果解析）し、ホスト上の**インプラントはAIを持たず単にタスクを実行**した。Kasperskyは一例を再構成した——人のオペレーターがまず露出していたとみられる**Microsoft SQL Server**（`sqlservr.exe` 16.0.1000）を約24時間で侵害し、**約2週間休止**した後にCyberStrikeAIビーコンを投下。ビーコンは**約2分**で**永続化**（`SystemUpdate`というスケジュールタスク）を設定し、LDAPで**ドメイン偵察**（約5時間）、SMB/WMIで横移動、レジストリハイブのダンプと**comsvcs.dll経由のlsass**抽出、改名したMimikatzで**DCSync＋Golden Ticket**を実行した。**インプラント展開から3〜4日でドメインコントローラーが侵害**され、最終段はデータ収集（SQLサーバーからのDBレコード、ネットワーク資源からのファイル）だった。Kasperskyは活動を既知グループに**帰属せず**、インフラ全体で単一オペレーターとも断定できないとする。スクリプトの中国語コメント、中国系サービス（DNSLog.cn）の利用、UTC+8の再起動タイミングは中国語話者を**示唆**する。`incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`。

summary_ko: |
  **2026년 11월 2일, Kaspersky(보도자료 + Securelist 보고서 "CyberStrikeAI in the wild")는 라틴아메리카와 아프리카 여러 나라의 교육 부문 기관에서 벌어진 실제 침입을 기록했다. 사후 공격 단계는 LLM 오케스트레이터가 주도했다.** CyberStrikeAI는 Go 기반의 오픈소스 AI 침투 테스트 하네스로, 이 공격들에서 **LLM은 공격자의 C2 서버에서 동작**(도구 선택·명령 생성·결과 분석)했고 호스트의 **임플란트는 AI가 없이 단지 작업을 실행**했다. Kaspersky는 한 사례를 재구성했다——사람 운영자가 먼저 노출되었을 가능성이 큰 **Microsoft SQL Server**(`sqlservr.exe` 16.0.1000)를 약 24시간에 걸쳐 침해하고 **약 2주 쉰 뒤** CyberStrikeAI 비컨을 투입했다. 비컨은 **약 2분** 만에 **지속성**(`SystemUpdate` 예약 작업)을 설정하고 LDAP로 **도메인 정찰**(약 5시간), SMB/WMI 측면 이동, 레지스트리 하이브 덤프와 **comsvcs.dll을 통한 lsass** 추출, 이름을 바꾼 Mimikatz로 **DCSync + Golden Ticket**을 실행했다. **임플란트 배포 후 3~4일 내 도메인 컨트롤러가 침해**됐고, 마지막 단계는 데이터 수집(SQL 서버의 DB 레코드, 네트워크 자원의 파일)이었다. Kaspersky는 활동을 알려진 그룹에 **귀속하지 않으며** 인프라 전반의 단일 운영자도 확신할 수 없다고 한다. 스크립트의 중국어 주석, 중국계 서비스(DNSLog.cn) 사용, UTC+8 재시작 타이밍은 중국어 사용자를 **시사**한다. `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

summary_de: |
  **Am 2. November 2026 dokumentierte Kaspersky (Pressemitteilung + ein Securelist-Bericht, „CyberStrikeAI in the wild") reale Einbrüche bei Bildungseinrichtungen in mehreren Ländern Lateinamerikas und Afrikas, bei denen ein LLM-Orchestrator die Post-Exploitation steuerte.** CyberStrikeAI ist ein quelloffenes, in Go geschriebenes KI-Pentesting-Gerüst; bei diesen Angriffen **lief das LLM auf dem C2-Server des Angreifers** (Toolauswahl, Befehlserzeugung, Ergebnisanalyse), während der **Implantat** auf dem Host **keine KI enthielt und nur Aufgaben ausführte**. Kaspersky rekonstruierte einen Fall: Ein menschlicher Operator kompromittierte zunächst über ~24 h einen vermutlich exponierten **Microsoft SQL Server** (`sqlservr.exe` 16.0.1000), **pausierte ~2 Wochen** und setzte dann das CyberStrikeAI-Beacon ein — das binnen **~2 Minuten** **Persistenz** (eine geplante Aufgabe `SystemUpdate`) einrichtete, per LDAP **Domänen-Aufklärung** (~5 h) betrieb, sich über SMB/WMI seitlich bewegte, Registry-Hives und **lsass via comsvcs.dll** auslas und mit einem umbenannten Mimikatz **DCSync + Golden Ticket** ausführte. **Domänencontroller wurden binnen 3–4 Tagen nach Implantat-Einsatz kompromittiert**; die letzte Phase war Datensammlung (Datenbankdatensätze vom SQL-Server, Dateien aus Netzwerkressourcen). Kaspersky **ordnet** die Aktivität keiner bekannten Gruppe zu und kann keinen einzelnen Operator über die Infrastruktur hinweg bestätigen; chinesischsprachige Skriptkommentare, die Nutzung chinesischer Dienste (DNSLog.cn) und UTC+8-Neustartzeiten **deuten** auf einen chinesischsprachigen Operator hin. `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

summary_fr: |
  **Le 2 novembre 2026, Kaspersky (communiqué + un rapport Securelist, « CyberStrikeAI in the wild ») a documenté des intrusions réelles chez des établissements du secteur éducatif dans plusieurs pays d'Amérique latine et d'Afrique, où un orchestrateur LLM pilotait la post-exploitation.** CyberStrikeAI est un harnais open source de test d'intrusion assisté par IA, écrit en Go ; dans ces attaques, **le LLM tournait sur le serveur C2 de l'attaquant** (choix des outils, génération de commandes, analyse des résultats) tandis que l'**implant** sur l'hôte **ne contenait aucune IA et se contentait d'exécuter les tâches**. Kaspersky a reconstitué un cas : un opérateur humain a d'abord compromis en ~24 h un **Microsoft SQL Server** probablement exposé (`sqlservr.exe` 16.0.1000), a **marqué une pause de ~2 semaines**, puis a déployé la balise CyberStrikeAI — qui a établi la **persistance** (une tâche planifiée `SystemUpdate`) en **~2 minutes**, mené une **reconnaissance de domaine** LDAP (~5 h), s'est déplacée latéralement via SMB/WMI, a extrait les ruches de registre et **lsass via comsvcs.dll**, puis exécuté **DCSync + Golden Ticket** avec un Mimikatz renommé. **Les contrôleurs de domaine ont été compromis en 3–4 jours après le déploiement de l'implant** ; la dernière étape a été la collecte de données (enregistrements de base de données depuis le serveur SQL, fichiers depuis les ressources réseau). Kaspersky **n'attribue pas** l'activité à un groupe connu et ne peut confirmer un opérateur unique sur l'ensemble de l'infrastructure ; les commentaires de script en chinois, l'usage de services chinois (DNSLog.cn) et les horaires de redémarrage en UTC+8 **suggèrent** un opérateur sinophone. `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

summary_es: |
  **El 2 de noviembre de 2026, Kaspersky (nota de prensa + un informe de Securelist, "CyberStrikeAI in the wild") documentó intrusiones reales en organizaciones del sector educativo de varios países de América Latina y África, en las que un orquestador LLM impulsó la post-explotación.** CyberStrikeAI es un marco de código abierto, escrito en Go, para pruebas de penetración con IA; en estos ataques **el LLM se ejecutaba en el servidor C2 del atacante** (selección de herramientas, generación de comandos, análisis de resultados), mientras que el **implante** en el host **no contenía IA y solo ejecutaba tareas**. Kaspersky reconstruyó un caso: un operador humano comprometió primero, en ~24 h, un **Microsoft SQL Server** probablemente expuesto (`sqlservr.exe` 16.0.1000), **hizo una pausa de ~2 semanas** y luego desplegó la baliza de CyberStrikeAI — que estableció **persistencia** (una tarea programada `SystemUpdate`) en **~2 minutos**, realizó **reconocimiento de dominio** por LDAP (~5 h), se movió lateralmente por SMB/WMI, volcó las colmenas del registro y **lsass mediante comsvcs.dll**, y ejecutó **DCSync + Golden Ticket** con un Mimikatz renombrado. **Los controladores de dominio fueron comprometidos en 3–4 días tras el despliegue del implante**; la etapa final fue la recolección de datos (registros de base de datos del servidor SQL, archivos de recursos de red). Kaspersky **no atribuye** la actividad a un grupo conocido ni puede confirmar un único operador en toda la infraestructura; los comentarios de script en chino, el uso de servicios chinos (DNSLog.cn) y los horarios de reinicio en UTC+8 **sugieren** un operador sinohablante. `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

sources:
  - url: https://securelist.com/cyberstrikeai-attacks/121715/
    label: Securelist / Kaspersky ("CyberStrikeAI in the wild")
  - url: https://www.kaspersky.com/about/press-releases/kaspersky-uncovers-ai-driven-attacks-on-educational-organizations-in-latin-america-and-africa
    label: Kaspersky press release
  - url: https://securityonline.info/cyberstrikeai-framework-attacks
    label: Security Online
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.37"
---

# CyberStrikeAI in the wild: an LLM-orchestrated intrusion reaches domain admin at education targets in Latin America and Africa

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 2 November 2026, Kaspersky (press release + a Securelist report, "CyberStrikeAI in the wild") documented real-world intrusions at education-sector organizations across several countries in Latin America and Africa, in which an LLM orchestrator drove the post-exploitation.** CyberStrikeAI is an open-source, Go-based AI penetration-testing framework; in these attacks the LLM ran on the attacker's C2 server (selecting tools, writing commands, reading results) while the on-host implant carried no AI and simply executed tasks. Kaspersky reconstructed one case: a human operator first breached a likely-exposed Microsoft SQL Server (`sqlservr.exe` 16.0.1000) over ~24h, paused ~2 weeks, then deployed the CyberStrikeAI beacon — which set persistence (a `SystemUpdate` scheduled task) within ~2 minutes, ran LDAP domain recon (~5h), moved laterally over SMB/WMI, dumped registry hives and lsass via comsvcs.dll, and ran DCSync + Golden Ticket with a renamed Mimikatz. Domain controllers were compromised within 3–4 days of implant deployment; the final stage was data collection (database records from the SQL server, files from network resources). Kaspersky does not attribute the activity to a known group and cannot confirm a single operator across infrastructure; Chinese-language script comments, use of Chinese services (DNSLog.cn) and UTC+8 restart timing suggest a Chinese-speaking operator. Recorded `incident` / `WEAPON` + `CRED` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Likely-exposed Microsoft SQL Server<br/>breached manually (~24h), then ~2-week pause"]:::entry
    S1["CyberStrikeAI beacon deployed;<br/>LLM on C2 selects tools / writes commands;<br/>persistence (SystemUpdate task) in ~2 min"]:::step
    S2["LDAP domain recon (~5h) · SMB/WMI lateral<br/>· lsass via comsvcs.dll · DCSync + Golden Ticket"]:::step
    I["Domain controllers compromised in 3–4 days;<br/>database + network files collected"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What Kaspersky reported.** On **2 November 2026**, Kaspersky issued a press release and a Securelist report, *"CyberStrikeAI in the wild: the use of AI in real-world attacks on organizations,"* describing intrusions at **education-sector organizations in several countries across Latin America and Africa** (no specific organizations or countries are named). **CyberStrikeAI** is an open-source, Go-based (Apache-2.0) AI penetration-testing framework whose maintainers describe it as built for authorized assessments; here it was abused in real attacks.

**The architecture.** The design keeps the model off the victim: an **LLM orchestrator runs on the attacker's C2 server** — it selects tools, writes the commands and analyses the returned output — while the **implant on the compromised host carries no AI functionality** and simply executes the tasks it is handed. A human operator sets the objectives; Kaspersky notes human involvement at goal-setting but does not quantify ongoing oversight.

**The reconstructed intrusion.** In one reconstructed case:

1. **Initial access (manual, ~24h).** The first malicious commands ran from `sqlservr.exe` (version 16.0.1000) — Kaspersky calls a likely-exposed Microsoft SQL Server the "likely initial access vector." The operator collected basic system data and deployed local utilities (e.g. RogueWinRM, GodPotato).
2. **Pause (~2 weeks).** Operations went quiet.
3. **Beacon + autonomy.** The operator deployed the **CyberStrikeAI beacon**, which received tasks from the LLM on the C2. Within **~2 minutes** it established **persistence** via a scheduled task named **`SystemUpdate`**.
4. **Domain recon (~5h).** LDAP queries enumerated user accounts, subnets and Azure credentials.
5. **Lateral movement + credential theft.** Over SMB administrative shares and WMI; registry hives dumped with `reg.exe`; credentials extracted from `lsass.exe` via `comsvcs.dll`. With domain-admin credentials it ran **DCSync** and **Golden Ticket** attacks using a **renamed Mimikatz**.
6. **Outcome.** **Domain controllers were compromised within 3–4 days** of implant deployment, giving full domain-administrative control. The **final stage was data collection** — database records queried from the education organization's SQL server, and files collected from network resources. (Kaspersky describes *collection*; it does not detail external exfiltration to a specific destination, and it names no student/staff record counts.)

**Attribution — stated carefully.** Kaspersky says the evidence **does not link** the activity to any known group and that it cannot be certain the same operator is behind related campaigns. Chinese-language comments in PowerShell scripts, the use of Chinese services (e.g. DNSLog.cn) and UTC+8 business-hours restart timing **"suggest a connection"** to a Chinese-speaking operator — a suggestion, not an attribution. CyberStrikeAI has prior documented abuse (earlier FortiGate-focused and Japan-focused reporting); this education-sector campaign in Latin America and Africa is a distinct Kaspersky-documented case.

**How it is graded.** `incident` — real, forensically reconstructed intrusions, not a demonstration. `WEAPON` (an AI framework orchestrating offensive operations end-to-end) + `CRED` (what is confirmed is **credential theft and full domain-controller takeover** — lsass dumping, DCSync, Golden Ticket; data "collection" is described but external exfiltration of named records is not confirmed, so this is `CRED`, not `EXFIL`). `real_harm: true`: the **domain-controller compromise and credential theft are confirmed** at real education organizations. Severity `high`, not critical: the compromise is real but Kaspersky names no victims, quantifies no data loss, and reports no critical-infrastructure impact. Confidence `A`: Kaspersky's own Securelist forensic report and press release, with independent reporting. `ai_involvement: confirmed`: the LLM-on-C2 orchestration is the documented core of the technique.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Securelist / Kaspersky ("CyberStrikeAI in the wild") | <https://securelist.com/cyberstrikeai-attacks/121715/> |
| 2 | Kaspersky press release | <https://www.kaspersky.com/about/press-releases/kaspersky-uncovers-ai-driven-attacks-on-educational-organizations-in-latin-america-and-africa> |
| 3 | Security Online | <https://securityonline.info/cyberstrikeai-framework-attacks> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-02` (raw: 2026-11-02 Kaspersky press release / Securelist report; intrusions observed Sept–Oct 2026, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — Kaspersky's own Securelist forensic report + press release, with independent reporting |
| Real harm | Yes — confirmed domain-controller compromise and credential theft at real education organizations |
| AI involvement | Confirmed `confirmed` — LLM-on-C2 orchestration is the core technique |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-11-02-cyberstrikeai-education-latam-africa` |

<sub>**Why this classification:** A forensically reconstructed, real intrusion in which an AI framework (CyberStrikeAI) orchestrated the attack end-to-end (`WEAPON`) and achieved domain-controller takeover via credential theft (`CRED` — lsass/DCSync/Golden Ticket; external exfiltration of named records is not confirmed, so not `EXFIL`), hence `real_harm: true`. `high` not critical: the compromise is confirmed but no victims are named, no data-loss figures are given, and no critical-infrastructure impact is reported. Region `GLOBAL` — targets span Latin America and Africa with no named countries (the taxonomy has no Africa code). `confirmed` AI involvement from the LLM-on-C2 design. Attribution to a Chinese-speaking operator is "suggested," not established. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI (agents used by attackers)](../../topics/offensive-ai.md)

**Related records:**

- `2026-11-05` ["Hacking on Autopilot": Check Point's ARTEX cybercrime forensics](2026-11-05-artex-hacking-on-autopilot-cybercrime.md)<br>  <sub>Another open-source AI pentest harness abused for autonomous-leaning crime</sub>
- `2026-11-04` ["BOSSAI": a lone operator's 12-agent AI attack mesh](2026-11-04-bossai-ai-attack-mesh-taiwan-emergency.md)<br>  <sub>Another LLM-orchestrated real-world intrusion campaign</sub>
- `2026-09-22` [Carbonato: a Docker-borne Hermes Agent botnet](../2026-09/2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>Another offensive-AI framework operated at scale</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-02-cyberstrikeai-education-latam-africa.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
