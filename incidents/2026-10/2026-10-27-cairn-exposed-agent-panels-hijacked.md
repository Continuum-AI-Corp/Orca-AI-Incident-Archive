---
id: 2026-10-27-cairn-exposed-agent-panels-hijacked
title: "Attackers hijack exposed Cairn AI-agent panels in the wild to plant SSH keys, a Poseidon implant, and steal API keys"
title_zh: "攻击者在野劫持暴露的 Cairn AI-agent 面板，植入 SSH 密钥、Poseidon 植入体并窃取 API 密钥"
title_ja: "攻撃者が露出したCairnのAIエージェント・パネルを実環境で乗っ取り、SSHキーとPoseidonインプラントを仕込みAPIキーを窃取"
title_ko: "공격자들이 노출된 Cairn AI 에이전트 패널을 실제 환경에서 탈취해 SSH 키·Poseidon 임플란트를 심고 API 키를 탈취"
title_de: "Angreifer kapern exponierte Cairn-KI-Agenten-Panels in freier Wildbahn, platzieren SSH-Schlüssel und ein Poseidon-Implantat und stehlen API-Schlüssel"
title_fr: "Des attaquants détournent dans la nature des panneaux d'agents IA Cairn exposés pour planter des clés SSH, un implant Poseidon et voler des clés API"
title_es: "Atacantes secuestran en entornos reales paneles de agentes de IA Cairn expuestos para plantar claves SSH, un implante Poseidon y robar claves API"
date: 2026-10-27
date_raw: "2026-10-27 (NorForge report, via Cyber Security News / GBHackers); activity from ~2026-10-20"
date_precision: day

kind: incident
type: [INFRA, WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Security firm **NorForge** reported (27 October 2026) that attackers are hijacking **internet-exposed, login-less panels of Cairn** — an open platform where you give an AI agent a goal and it works autonomously, posting findings to a web panel — and injecting tasks that weaponise the agents.** Across **at least 17 exposed panels** (some red-team / CTF environments), observed activity from around **20 October** included a task that had the agent **add an attacker SSH key** to the kali account's `authorized_keys`; a 21 October "Local worker maintenance" task that delivered a base64 script fetching a **Poseidon implant** (a Go-based Mythic C2 payload, via Bunny.net CDN); and recon tasks hunting secrets such as `API_KEY` and `ANTHROPIC_AUTH_TOKEN`, with **AI-model API keys reported stolen**. NorForge tracks two separate clusters — **AIA0009** (persistence + malware, "cairnscan" tag) and **AIA0010** (credential theft + finding more panels). Entry was **unauthenticated administrative access to exposed panels, not a new software CVE**. NorForge observed passively and **could not confirm the campaigns ran fully autonomously** — synchronized activity suggests scripting, and it believes humans stepped in at key points (a pause before malware, and the C2/download-server setup). Recorded `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`.

summary_zh: |
  **安全公司 **NorForge** 报告（2026 年 10 月 27 日）：攻击者正在野劫持**暴露在公网、无需登录的 Cairn 面板**——Cairn 是一个开放平台，你给 AI agent 下一个目标、它便自主执行并把发现贴到 web 面板——并注入任务把这些 agent 武器化。** 在**至少 17 个暴露面板**（部分是红队/CTF 环境）上，自约 **10 月 20 日**起观察到的活动包括：一个任务让 agent **把攻击者 SSH 密钥**加进 kali 账户的 `authorized_keys`；10 月 21 日一个名为"Local worker maintenance"的任务投放 base64 脚本去拉取 **Poseidon 植入体**（基于 Go 的 Mythic C2 载荷，经 Bunny.net CDN）；以及搜寻 `API_KEY`、`ANTHROPIC_AUTH_TOKEN` 等机密的侦察任务，**据报 AI 模型 API 密钥被窃**。NorForge 跟踪两个独立簇——**AIA0009**（持久化 + 恶意软件、"cairnscan"标签）与 **AIA0010**（窃凭据 + 搜寻更多面板）。入口是**对暴露面板的未授权管理访问，而非新的软件 CVE**。NorForge 系被动观察，**无法确认这些行动完全自主**——同步活动暗示有脚本化，并认为关键节点有人工介入（投毒前的暂停、C2/下载服务器搭建）。记为 `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`。

summary_ja: |
  **セキュリティ企業 **NorForge** は（2026年10月27日）、攻撃者が**インターネットに露出しログイン不要のCairnパネル**——Cairnは、AIエージェントに目標を与えると自律的に作業し発見をwebパネルに投稿する公開プラットフォーム——を実環境で乗っ取り、エージェントを兵器化するタスクを注入していると報告した。** **少なくとも17の露出パネル**（一部はレッドチーム/CTF環境）で、約**10月20日**以降に観測された活動には、エージェントにkaliアカウントの`authorized_keys`へ**攻撃者のSSHキーを追加**させるタスク、10月21日の「Local worker maintenance」というタスクがbase64スクリプトで**Poseidonインプラント**（GoベースのMythic C2ペイロード、Bunny.net CDN経由）を取得すること、`API_KEY`や`ANTHROPIC_AUTH_TOKEN`などの秘密を探す偵察タスクが含まれ、**AIモデルのAPIキーが窃取されたと報告**された。NorForgeは2つの別クラスタ——**AIA0009**（永続化＋マルウェア、「cairnscan」タグ）と**AIA0010**（認証情報窃取＋さらなるパネル探索）——を追跡。侵入口は**露出パネルへの未認証の管理アクセスであり、新規のソフトウェアCVEではない**。NorForgeは受動的に観測し、**これらが完全に自律的に実行されたとは確認できなかった**——同期した活動はスクリプト化を示唆し、重要な局面で人間が関与したとみている（マルウェア投入前の一時停止、C2/ダウンロードサーバーの設定）。`incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_ko: |
  **보안 업체 **NorForge**는(2026년 10월 27일) 공격자들이 **인터넷에 노출되고 로그인 없는 Cairn 패널**——Cairn은 AI 에이전트에 목표를 주면 자율적으로 작업하고 발견을 웹 패널에 게시하는 공개 플랫폼——을 실제 환경에서 탈취해 에이전트를 무기화하는 작업을 주입하고 있다고 보고했다.** **최소 17개 노출 패널**(일부는 레드팀/CTF 환경)에서 약 **10월 20일**부터 관측된 활동에는 에이전트가 kali 계정의 `authorized_keys`에 **공격자 SSH 키를 추가**하게 한 작업, 10월 21일 "Local worker maintenance" 작업이 base64 스크립트로 **Poseidon 임플란트**(Go 기반 Mythic C2 페이로드, Bunny.net CDN 경유)를 가져온 것, `API_KEY`·`ANTHROPIC_AUTH_TOKEN` 같은 비밀을 찾는 정찰 작업이 포함됐고 **AI 모델 API 키가 탈취된 것으로 보고**됐다. NorForge는 두 별개 클러스터——**AIA0009**(지속성+멀웨어, "cairnscan" 태그)와 **AIA0010**(자격 증명 탈취+추가 패널 탐색)——를 추적한다. 진입점은 **노출 패널에 대한 미인증 관리 접근이며 새로운 소프트웨어 CVE가 아니다**. NorForge는 수동적으로 관측했고 **이 캠페인이 완전 자율로 실행됐다고 확인하지 못했다**——동기화된 활동은 스크립트화를 시사하며 핵심 지점에서 사람이 개입한 것으로 본다(멀웨어 투입 전 일시정지, C2/다운로드 서버 설정). `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_de: |
  **Die Sicherheitsfirma **NorForge** berichtete (27. Oktober 2026), dass Angreifer **im Internet exponierte, login-lose Cairn-Panels** — Cairn ist eine offene Plattform, auf der man einem KI-Agenten ein Ziel gibt und er autonom arbeitet und Ergebnisse in ein Web-Panel postet — in freier Wildbahn kapern und Aufgaben einschleusen, die die Agenten bewaffnen.** Über **mindestens 17 exponierte Panels** (teils Red-Team-/CTF-Umgebungen) umfasste die ab etwa **20. Oktober** beobachtete Aktivität: eine Aufgabe, die den Agenten einen **Angreifer-SSH-Schlüssel** in die `authorized_keys` des kali-Kontos eintragen ließ; eine Aufgabe „Local worker maintenance" vom 21. Oktober, die per Base64-Skript ein **Poseidon-Implantat** (eine Go-basierte Mythic-C2-Payload, über Bunny.net-CDN) nachlud; und Recon-Aufgaben, die nach Geheimnissen wie `API_KEY` und `ANTHROPIC_AUTH_TOKEN` suchten, wobei **KI-Modell-API-Schlüssel als gestohlen gemeldet** wurden. NorForge verfolgt zwei getrennte Cluster — **AIA0009** (Persistenz + Malware, „cairnscan"-Tag) und **AIA0010** (Diebstahl von Anmeldedaten + Auffinden weiterer Panels). Der Einstieg war **unauthentifizierter administrativer Zugriff auf exponierte Panels, kein neues Software-CVE**. NorForge beobachtete passiv und **konnte nicht bestätigen, dass die Kampagnen vollständig autonom liefen** — synchronisierte Aktivität deutet auf Skripting hin, und man vermutet menschliches Eingreifen an Schlüsselstellen (eine Pause vor dem Malware-Einsatz und das Einrichten der C2-/Download-Server). `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_fr: |
  **La société de sécurité **NorForge** a rapporté (27 octobre 2026) que des attaquants détournent dans la nature des **panneaux Cairn exposés sur Internet et sans authentification** — Cairn est une plateforme ouverte où l'on donne un objectif à un agent IA, qui travaille de façon autonome et publie ses trouvailles sur un panneau web — et y injectent des tâches qui militarisent les agents.** Sur **au moins 17 panneaux exposés** (certains environnements red team / CTF), l'activité observée depuis le **20 octobre** environ comprenait : une tâche faisant **ajouter par l'agent une clé SSH de l'attaquant** aux `authorized_keys` du compte kali ; une tâche « Local worker maintenance » du 21 octobre livrant un script base64 qui récupérait un **implant Poseidon** (charge Mythic C2 en Go, via le CDN Bunny.net) ; et des tâches de reconnaissance cherchant des secrets tels que `API_KEY` et `ANTHROPIC_AUTH_TOKEN`, avec des **clés API de modèles d'IA signalées volées**. NorForge suit deux clusters distincts — **AIA0009** (persistance + malware, étiquette « cairnscan ») et **AIA0010** (vol d'identifiants + recherche d'autres panneaux). L'entrée se faisait par **accès administratif non authentifié à des panneaux exposés, et non via une nouvelle CVE logicielle**. NorForge a observé passivement et **n'a pas pu confirmer que les campagnes étaient entièrement autonomes** — l'activité synchronisée suggère du scripting, et elle pense que des humains sont intervenus à des moments clés (une pause avant le déploiement du malware et la mise en place des serveurs C2/de téléchargement). `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_es: |
  **La firma de seguridad **NorForge** informó (27 de octubre de 2026) que atacantes están secuestrando en entornos reales **paneles de Cairn expuestos a Internet y sin inicio de sesión** —Cairn es una plataforma abierta donde se da un objetivo a un agente de IA y este trabaja de forma autónoma, publicando hallazgos en un panel web— e inyectan tareas que militarizan a los agentes.** En **al menos 17 paneles expuestos** (algunos entornos red team / CTF), la actividad observada desde alrededor del **20 de octubre** incluyó: una tarea que hacía que el agente **añadiera una clave SSH del atacante** a `authorized_keys` de la cuenta kali; una tarea "Local worker maintenance" del 21 de octubre que entregaba un script base64 que descargaba un **implante Poseidon** (carga Mythic C2 en Go, vía CDN de Bunny.net); y tareas de reconocimiento que buscaban secretos como `API_KEY` y `ANTHROPIC_AUTH_TOKEN`, con **claves API de modelos de IA reportadas como robadas**. NorForge rastrea dos clústeres distintos — **AIA0009** (persistencia + malware, etiqueta "cairnscan") y **AIA0010** (robo de credenciales + búsqueda de más paneles). La entrada fue **acceso administrativo no autenticado a paneles expuestos, no una nueva CVE de software**. NorForge observó de forma pasiva y **no pudo confirmar que las campañas fueran totalmente autónomas** — la actividad sincronizada sugiere scripting, y cree que hubo intervención humana en puntos clave (una pausa antes del despliegue del malware y la configuración de los servidores C2/de descarga). `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

sources:
  - url: https://cybersecuritynews.com/ai-pentesting-agents/
    label: Cyber Security News (NorForge research)
  - url: https://gbhackers.com/ai-pentesting-panels/
    label: GBHackers (NorForge research)
  - url: https://vibeincidents.com/incidents/cairn-exposed-panels-ai-intrusions/
    label: Vibe Incidents
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.34"
---

# Attackers hijack exposed Cairn AI-agent panels in the wild to plant SSH keys, a Poseidon implant, and steal API keys

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-8F6A3C?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-3C6E8F?style=flat-square)

## Summary

**Security firm NorForge reported (27 October 2026) that attackers are hijacking internet-exposed, login-less panels of Cairn — an open platform where you give an AI agent a goal and it works autonomously, posting findings to a web panel — and injecting tasks that weaponise the agents.** Across at least 17 exposed panels (some red-team / CTF environments), observed activity from around 20 October included a task that had the agent add an attacker SSH key to the kali account's `authorized_keys`; a 21 October "Local worker maintenance" task that delivered a base64 script fetching a Poseidon implant (a Go-based Mythic C2 payload, via Bunny.net CDN); and recon tasks hunting secrets such as `API_KEY` and `ANTHROPIC_AUTH_TOKEN`, with AI-model API keys reported stolen. NorForge tracks two separate clusters — AIA0009 (persistence + malware, "cairnscan" tag) and AIA0010 (credential theft + finding more panels). Entry was unauthenticated administrative access to exposed panels, not a new software CVE. NorForge observed passively and could not confirm the campaigns ran fully autonomously — synchronized activity suggests scripting, and it believes humans stepped in at key points (a pause before malware, and the C2/download-server setup). Recorded `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Cairn AI-agent panels exposed to the<br/>internet with no login"]:::entry
    S1["Attackers inject tasks via the panel<br/>(unauthenticated admin access, no CVE)"]:::step
    S2["Agent adds attacker SSH key; fetches a<br/>Poseidon implant; hunts API_KEY / tokens"]:::step
    I["≥17 panels; SSH persistence, Mythic C2 RAT,<br/>AI API keys reported stolen (human-assisted)"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What Cairn is, and what happened.** **Cairn** is an open platform for running AI agents: a user defines a goal and a starting point, and the agent works on its own, posting findings as "facts" to a web panel. Anyone who can reach the panel can create and manage tasks — so an **internet-exposed panel with no authentication** hands an attacker control of the agent. Security firm **NorForge** reported on **27 October 2026** (covered by Cyber Security News and GBHackers) that attackers are doing exactly this in the wild, with activity observed from around **20 October**. NorForge watched the exposed panels **passively** and did not interact with the attackers.

**The injected tasks.** Across **at least 17 exposed panels** — some belonging to red-team and CTF exercises — NorForge saw malicious tasks:
- **SSH persistence**: a task named "Install kali SSH key" had the agent add an **attacker-controlled public key** to the kali user's `authorized_keys`, with agent output confirming it.
- **Malware**: on **21 October**, a "Local worker maintenance" task delivered a **base64-encoded script** that downloaded a **Poseidon implant** — a Go-based payload associated with the open-source **Mythic** command-and-control ecosystem, reportedly communicating via **Bunny.net** CDN infrastructure; it ran until an operator created a stop file.
- **Secret theft**: recon tasks searched files and environment variables for terms like `API_KEY` and `ANTHROPIC_AUTH_TOKEN`, and some tasks wrote secrets into public fact texts; NorForge reported **AI-model API keys stolen** (though it could not confirm whether attackers crossed container-isolation boundaries).

**Two clusters, and the autonomy caveat.** NorForge tracks two provisional clusters: **AIA0009** (random hex task-name suffixes, "cairnscan" tag; persistence, access and the only one seen deploying malware) and **AIA0010** (task names mimicking Cairn's intent labels; hunting internal services, credentials and more panels). It found **no shared hard indicators** between them, so treats them as separate. Importantly, NorForge **does not claim the campaigns were fully autonomous AI**: synchronized activity across panels suggests **scripting**, and it believes **humans intervened at key points** (a pause before malware deployment, and standing up the C2 and download servers). The entry point was **unauthenticated administrative access to exposed panels, not a newly-disclosed software vulnerability**.

**How it is graded.** `incident` — a real, in-the-wild campaign. `INFRA` (exposed AI-agent orchestration panels are the attack surface) + `WEAPON` (the hijacked agents are driven to install persistence, deploy a RAT and steal credentials). `real_harm: true`: a Poseidon implant was actually delivered and attacker SSH keys actually installed on compromised panels. Severity `high`: real in-the-wild agent weaponisation across ≥17 panels with RAT deployment, but bounded to **exposed/misconfigured** panels (several of them red-team/CTF environments) rather than hardened production, and with the autonomy/human-involvement caveat. Confidence `A`: NorForge's technical research, carried by Cyber Security News and GBHackers. Dated to the 27 October report; activity from ~20 October.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Cyber Security News (NorForge research) | <https://cybersecuritynews.com/ai-pentesting-agents/> |
| 2 | GBHackers (NorForge research) | <https://gbhackers.com/ai-pentesting-panels/> |
| 3 | Vibe Incidents | <https://vibeincidents.com/incidents/cairn-exposed-panels-ai-intrusions/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-27` (raw: 2026-10-27 NorForge report via Cyber Security News / GBHackers; activity from ~2026-10-20, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`WEAPON`](../../taxonomy/types.md#weapon) |
| Severity | **High** `high` |
| Confidence | **A** — NorForge research + Cyber Security News + GBHackers |
| Real harm | Yes — Poseidon implant delivered and attacker SSH keys installed on exposed Cairn panels in the wild |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-27-cairn-exposed-agent-panels-hijacked` |

<sub>**Why this classification:** In-the-wild hijacking of exposed Cairn AI-agent panels (`INFRA` — exposed agent orchestration) in which the agents are driven to install SSH persistence, deploy a Poseidon/Mythic implant and steal credentials (`WEAPON`). `incident` with `real_harm: true` because malware and attacker SSH keys were actually planted. `high`, not critical, because it is bounded to exposed/misconfigured panels (several red-team/CTF) and NorForge could not confirm full AI autonomy (human involvement at key points). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI](../../topics/offensive-ai.md)

**Related records:**

- `2026-10-21` [Storm-0940 drives the ConnectWise supply-chain compromise with the ARTEX agentic AI framework](2026-10-21-storm-0940-artex-connectwise-supply-chain.md)<br>  <sub>Another agentic-AI offensive framework used in the wild</sub>
- `2026-10-06` [ARTEX AI used against South Korean banks](2026-10-06-artex-ai-south-korea-banks.md)<br>  <sub>An open agentic pentest tool turned to real attacks</sub>
- `2026-09-22` [ClosedQuorum AI C2 implant](../2026-09/2026-09-22-closedquorum-ai-c2-implant.md)<br>  <sub>Another AI-driven command-and-control implant</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-27-cairn-exposed-agent-panels-hijacked.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
