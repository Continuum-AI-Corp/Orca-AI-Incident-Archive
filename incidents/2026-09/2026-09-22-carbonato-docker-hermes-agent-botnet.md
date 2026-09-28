---
id: 2026-09-22-carbonato-docker-hermes-agent-botnet
title: "CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys over Telegram"
title_zh: "CARBONATO：一个 Docker 僵尸网络植入 Hermes Agent，经 Telegram 收割 AI API 密钥"
title_ja: "CARBONATO：Docker ボットネットが Hermes Agent を導入し、Telegram 経由で AI API キーを奪う"
title_ko: "CARBONATO: Docker 봇넷이 Hermes Agent를 설치하고 Telegram으로 AI API 키를 약탈한다"
title_de: "CARBONATO: Ein Docker-Botnetz installiert Hermes Agent und raubt AI-API-Schlüssel über Telegram"
title_fr: "CARBONATO : un botnet Docker installe Hermes Agent et pille des clés API d'IA via Telegram"
title_es: "CARBONATO: un botnet Docker instala Hermes Agent y saquea claves API de IA por Telegram"
date: 2026-09-22
date_raw: "2026-09-22 (ThreatDown) / 2026-09-24 (BleepingComputer)"
date_precision: day

kind: incident
type: [WEAPON, INFRA, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **ThreatDown publishes CARBONATO, a botnet built around an AI agent: it compromises Docker daemons exposed without authentication on port 2375, launches a privileged container, and installs the Hermes Agent framework under an agent named "GH0ST" whose instructions overwrite the default `SOUL.md` persona file.** Operators then drive an *"interactive command loop"* over Telegram — *"the model interprets the task, writes terminal commands, reads the output, and decides what to do next"* — collecting **AI API keys, SSH credentials and access tokens** and returning the results to the same chat that receives deployment reports. Scripts scan the host's networks **every five minutes** for fresh port-2375 targets, making it worm-like. ThreatDown recovered operational evidence spanning **October 2024 to August 2026** from an open registry holding **59 repositories and 4.3 GB** (234 image tags, 605 verified blobs) of image data; no cluster attribution, with Costa Rica a possible operator location. It is the fifth recorded use of the Hermes Agent framework in this archive — after the agent swarm that breached Taiwanese government systems (`2026-07-01`, Hermes with OpenClaw), the Thailand Ministry of Finance intrusion (`2026-07-30`), Unit 42's Chinese-speaking autonomous campaign built on Hermes Agent with DeepSeek (`2026-07-30`), and Gambit (`2026-09-22`) — so the framework is now a repeat offender rather than a one-off.

summary_zh: |
  **ThreatDown 公布 CARBONATO——一个围绕 AI agent 构建的僵尸网络：它攻陷在 2375 端口无认证暴露的 Docker 守护进程，启动特权容器，并安装 Hermes Agent 框架，agent 名为「GH0ST」，其指令会覆盖默认人格文件 `SOUL.md`。** 操作者随后通过 Telegram 驱动一个*「交互式命令循环」*——*「模型解读任务、编写终端命令、读取输出，并决定下一步做什么」*——收集 **AI API 密钥、SSH 凭据与访问令牌**，并把结果回传到同一个聊天。脚本**每五分钟**扫描宿主所在网络寻找新的 2375 端口目标，因此具备蠕虫式扩散能力。ThreatDown 从一个开放镜像仓库取得跨越 **2024 年 10 月至 2026 年 8 月**的行动证据，该仓库含 **59 个仓库、4.3 GB**（234 个镜像标签、605 个已核验 blob）镜像数据；无团伙归属，哥斯达黎加可能是操作者所在地。这是本档案中第五起 Hermes Agent 使用记录——前四起为攻破台湾政府系统的 agent 蜂群（`2026-07-01`，Hermes 与 OpenClaw）、泰国财政部入侵（`2026-07-30`）、Unit 42 记录的以 Hermes Agent + DeepSeek 为执行者的中文操作者自主行动（`2026-07-30`）与 Gambit（`2026-09-22`）——该框架已从「个案」变成「惯犯」

summary_ja: |
  **ThreatDownは CARBONATO を公表した。AIエージェントを中核に据えたボットネットである。認証なしで2375番ポートに露出したDockerデーモンを侵害し、特権コンテナを起動し、Hermes Agentフレームワークを「GH0ST」というエージェント名で導入する。その指示は既定のペルソナファイル `SOUL.md` を上書きする。** 運用者はTelegram経由で*「対話型コマンドループ」*を回す——*「モデルはタスクを解釈し、端末コマンドを書き、出力を読み、次に何をするかを決める」*——**AI APIキー、SSH認証情報、アクセストークン**を収集し、同じチャットへ結果を返す。スクリプトは**5分ごと**にホストのネットワークを走査して新たな2375番の標的を探し、ワーム的に拡散する。ThreatDownは**2024年10月〜2026年8月**に及ぶ運用証拠を、**59リポジトリ・4.3GB**（イメージタグ234件、検証済みblob 605件）のイメージデータを置いた公開レジストリから取得した。帰属はなく、運用者拠点はコスタリカの可能性。台湾の政府システムを侵害したエージェント群集（`2026-07-01`、HermesとOpenClaw）、タイ財務省侵入（`2026-07-30`）、Unit 42が記録したHermes Agent＋DeepSeekによる中国語話者の自律キャンペーン（`2026-07-30`）、Gambit（`2026-09-22`）に続く、本アーカイブ5例目のHermes Agent事例——同フレームワークは単発ではなく常習的に使われ始めている

summary_ko: |
  **ThreatDown은 AI 에이전트를 중심에 둔 봇넷 CARBONATO를 공개했다. 인증 없이 2375 포트에 노출된 Docker 데몬을 장악하고, 권한 있는 컨테이너를 띄운 뒤 Hermes Agent 프레임워크를 "GH0ST"라는 에이전트 이름으로 설치한다. 이 에이전트의 지시는 기본 페르소나 파일 `SOUL.md`를 덮어쓴다.** 운영자는 Telegram으로 *"대화형 명령 루프"*를 돌린다 — *"모델은 작업을 해석하고 터미널 명령을 작성하며 출력을 읽고 다음 행동을 결정한다"* — **AI API 키, SSH 자격증명, 액세스 토큰**을 수집해 같은 채팅으로 결과를 돌려보낸다. 스크립트는 **5분마다** 호스트 네트워크를 훑어 새로운 2375 포트 대상을 찾아 웜처럼 확산한다. ThreatDown은 **2024년 10월~2026년 8월**에 걸친 운영 증거를 이미지 데이터 **59개 리포지토리·4.3GB**(이미지 태그 234개, 검증된 blob 605개)를 담은 공개 레지스트리에서 확보했다. 배후 조직은 미확인, 운영자 위치는 코스타리카 가능성. 대만 정부 시스템을 침해한 에이전트 군집(`2026-07-01`, Hermes와 OpenClaw), 태국 재무부 침입(`2026-07-30`), Unit 42가 기록한 Hermes Agent+DeepSeek 기반 중국어권 운영자의 자율 캠페인(`2026-07-30`), Gambit(`2026-09-22`)에 이은 본 아카이브 다섯 번째 Hermes Agent 사례다

summary_de: |
  **ThreatDown veröffentlicht CARBONATO, ein Botnetz um einen KI-Agenten: Es kompromittiert ohne Authentifizierung auf Port 2375 exponierte Docker-Daemons, startet einen privilegierten Container und installiert das Hermes-Agent-Framework unter einem Agenten namens „GH0ST", dessen Anweisungen die Standard-Persona-Datei `SOUL.md` überschreiben.** Die Betreiber steuern danach eine *„interaktive Befehlsschleife"* über Telegram — *„das Modell interpretiert die Aufgabe, schreibt Terminalbefehle, liest die Ausgabe und entscheidet, was als Nächstes zu tun ist"* — und sammeln **KI-API-Schlüssel, SSH-Zugangsdaten und Access-Tokens**; die Ergebnisse gehen in denselben Chat zurück. Skripte durchsuchen **alle fünf Minuten** die Netzwerke des Hosts nach neuen Port-2375-Zielen, also wurmartig. ThreatDown sicherte Belege von **Oktober 2024 bis August 2026** aus einer offenen Registry mit **59 Repositories und 4,3 GB** Image-Daten (234 Image-Tags, 605 verifizierte Blobs); keine Cluster-Zuordnung, Costa Rica als möglicher Standort der Betreiber. Es ist der fünfte Hermes-Agent-Fall des Archivs – nach dem Agentenschwarm gegen taiwanische Regierungssysteme (`2026-07-01`, Hermes mit OpenClaw), Thailand (`2026-07-30`), der von Unit 42 dokumentierten Kampagne chinesischsprachiger Betreiber mit Hermes Agent und DeepSeek (`2026-07-30`) und Gambit (`2026-09-22`)

summary_fr: |
  **ThreatDown publie CARBONATO, un botnet construit autour d'un agent IA : il compromet des démons Docker exposés sans authentification sur le port 2375, lance un conteneur privilégié et installe le framework Hermes Agent sous un agent nommé « GH0ST » dont les instructions écrasent le fichier de personnalité `SOUL.md`.** Les opérateurs pilotent ensuite une *« boucle de commandes interactive »* via Telegram — *« le modèle interprète la tâche, écrit les commandes terminal, lit la sortie et décide de la suite »* — en collectant **clés API d'IA, identifiants SSH et jetons d'accès** et en renvoyant les résultats dans le même salon. Des scripts balayent **toutes les cinq minutes** les réseaux de l'hôte à la recherche de nouvelles cibles sur le port 2375, ce qui le rend vermiforme. ThreatDown a récupéré des preuves couvrant **octobre 2024 à août 2026** dans un registre ouvert contenant **59 dépôts et 4,3 Go** d'images (234 tags d'image, 605 blobs vérifiés) ; aucune attribution, le Costa Rica étant une localisation possible de l'opérateur. Cinquième cas Hermes Agent de l'archive, après l'essaim d'agents qui a compromis des systèmes gouvernementaux taïwanais (`2026-07-01`, Hermes avec OpenClaw), la Thaïlande (`2026-07-30`), la campagne d'opérateurs sinophones documentée par Unit 42 avec Hermes Agent et DeepSeek (`2026-07-30`) et Gambit (`2026-09-22`)

summary_es: |
  **ThreatDown publica CARBONATO, un botnet construido en torno a un agente de IA: compromete demonios Docker expuestos sin autenticación en el puerto 2375, lanza un contenedor privilegiado e instala el framework Hermes Agent bajo un agente llamado «GH0ST» cuyas instrucciones sobrescriben el archivo de personalidad `SOUL.md`.** Los operadores dirigen después un *«bucle de comandos interactivo»* por Telegram — *«el modelo interpreta la tarea, escribe comandos de terminal, lee la salida y decide qué hacer a continuación»* — recogiendo **claves API de IA, credenciales SSH y tokens de acceso** y devolviendo los resultados al mismo chat. Los scripts rastrean **cada cinco minutos** las redes del host en busca de nuevos objetivos en el puerto 2375, lo que lo hace similar a un gusano. ThreatDown recuperó evidencia de **octubre de 2024 a agosto de 2026** en un registro abierto con **59 repositorios y 4,3 GB** de imágenes (234 etiquetas de imagen, 605 blobs verificados); sin atribución, con Costa Rica como posible ubicación del operador. Es el quinto caso de Hermes Agent en el archivo, tras el enjambre de agentes que vulneró sistemas del Gobierno de Taiwán (`2026-07-01`, Hermes con OpenClaw), Tailandia (`2026-07-30`), la campaña de operadores de habla china documentada por Unit 42 con Hermes Agent y DeepSeek (`2026-07-30`) y Gambit (`2026-09-22`)

sources:
  - url: https://www.threatdown.com/blog/carbonato/
    label: ThreatDown
  - url: https://www.bleepingcomputer.com/news/security/new-carbonato-malware-uses-ai-agents-to-hijack-exposed-docker-hosts/
    label: BleepingComputer
  - url: https://www.securityweek.com/in-other-news-clop-leak-site-takeover-docker-botnet-hunts-ai-keys-water-utility-exposure/
    label: SecurityWeek

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys over Telegram

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**ThreatDown publishes CARBONATO, a botnet built around an AI agent: it compromises Docker daemons exposed without authentication on port 2375, launches a privileged container, and installs the Hermes Agent framework under an agent named "GH0ST" whose instructions overwrite the default `SOUL.md` persona file.** Operators then drive an *"interactive command loop"* over Telegram — *"the model interprets the task, writes terminal commands, reads the output, and decides what to do next"* — collecting **AI API keys, SSH credentials and access tokens** and returning the results to the same chat that receives deployment reports. Scripts scan the host's networks **every five minutes** for fresh port-2375 targets, making it worm-like. ThreatDown recovered operational evidence spanning **October 2024 to August 2026** from an open registry holding **59 repositories and 4.3 GB** (234 image tags, 605 verified blobs) of image data; no cluster attribution, with Costa Rica a possible operator location. It is the fifth recorded use of the Hermes Agent framework in this archive — after the agent swarm that breached Taiwanese government systems (`2026-07-01`, Hermes with OpenClaw), the Thailand Ministry of Finance intrusion (`2026-07-30`), Unit 42's Chinese-speaking autonomous campaign built on Hermes Agent with DeepSeek (`2026-07-30`), and Gambit (`2026-09-22`) — so the framework is now a repeat offender rather than a one-off.

## Attack chain

```mermaid
flowchart LR
    E["Docker daemon exposed on port 2375<br/>without authentication"]:::entry
    S1["Attacker orders a privileged container;<br/>reverse SSH tunnel, SSH key, cron/systemd persistence"]:::step
    S2["Hermes Agent installed as 'GH0ST';<br/>instructions overwrite SOUL.md"]:::step
    S3["Telegram task loop: the model writes commands,<br/>reads output and decides the next step"]:::step
    I["AI API keys, SSH credentials and tokens<br/>collected and exfiltrated; rescan every 5 minutes"]:::impact
    E --> S1 --> S2 --> S3 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What the researchers found.** ThreatDown describes CARBONATO as *"a botnet built around an AI agent"*: the malware connects to an unauthenticated Docker API on port 2375 and instructs the daemon to launch a privileged container, which gives it the host. It opens a reverse SSH tunnel, installs an SSH server with the operators' key, and reports each new deployment to Telegram, while scripts add persistence through cron jobs, systemd timers, `rc.local` and OpenRC hooks. On top of that host foothold sits the agent: **Hermes Agent** is installed with an agent named **"GH0ST"** whose instructions overwrite the default `SOUL.md` persona file. Hermes then works through tasks sent over Telegram — collecting AI API keys, SSH credentials and access tokens, running commands and sending back the results, as BleepingComputer summarises it — in what the researchers call an *"interactive command loop"*: *"The model interprets the task, writes terminal commands, reads the output, and decides what to do next. The agent runs those commands on the victim and returns its report to the Telegram chat that also receives deployment reports."* Spreading is handled by scripts that scan networks attached to the host **every five minutes**; each new compromise pulls the implant, launches the same privileged container and rejoins the loop. The persona prompt states the priority outright: it *"prioritizes the collection of AI API keys"* ahead of SSH credentials, access tokens and databases, naming **14 providers**.

**Scale, timeline and attribution.** The operational evidence ThreatDown retrieved spans **October 2024 to August 2026** and came from an unauthenticated registry holding **59 repositories and 4.3 GB** (234 image tags, 605 verified blobs) of image data, alongside a linked operation distributing trojanized cryptocurrency wallet apps (ThreatDown calls them *"two linked product lines"*). BleepingComputer notes that ThreatDown could not tie the botnet to a known threat cluster; ThreatDown's own attribution section places the operators in Costa Rica on four signals — voseo Spanish in the deployment reports, UTC-06:00 build timestamps matching the Costa Rica timezone, the Telegram handle `Carbo506` (+506 is Costa Rica's calling code), and reverse tunnels ending in the Costa Rican network AS262145. SecurityWeek, summarising the same report in its 25 September round-up, headlines the priority order: *"Docker botnet ranks AI API keys above all other loot."*

**Why it belongs here.** CARBONATO is the fifth documented use of the same open-source **Hermes Agent** framework in the archive — after the agent swarm that breached Taiwanese government systems in early July (`2026-07-01`, Dream: Hermes and OpenClaw sub-agents), the Thailand Ministry of Finance intrusion (`2026-07-30`, Hunt.io, YOLO no-approval mode), Unit 42's Chinese-speaking autonomous campaign that ran on Hermes Agent with DeepSeek across 460+ targets (`2026-07-30`), and the Gambit card-skimming operation (`2026-09-22`, Claude Opus 4.6 orchestration). Where Gambit used Hermes for orchestration inside a criminal business and Taiwan and Thailand for government espionage, CARBONATO is the **infrastructure-access** variant: the agent is installed *on the victim* as the post-exploitation brain, and its brief is explicitly to harvest the credentials of other AI systems. The pattern the archive has been tracking — one self-hosted agent stack reused across unrelated operators within three months — now spans espionage, financial crime and commodity botnet operations.

**Grading.** Recorded as `incident` / `WEAPON` + `INFRA` + `CRED` / `high` / `real_harm: true`. The `real_harm` call rests on the report's own language about machines it has already taken, not on capability alone: each deployment report carries *"the container ID, hostname, IP address, and country"* of the host, the scanner *"avoids hosts it has already infected"*, and *"infected hosts also repeatedly pulled the implant from the registry"* — which is why the archive records a confirmed victim set rather than a demonstration: this is a live botnet with confirmed compromises (a multi-year operational archive, worm-style spread), not a PoC — but the damage is per-victim host compromise of limited, unquantified scope, so it does not reach `critical` (which the archive reserves for confirmed damage at multi-organisation, government, critical-infrastructure or supply-chain-worm scale, or a first-of-its-kind milestone with a real victim; ThreatDown gives no count of infected hosts). Confidence **A**: the vendor's own research report plus two independent outlets reporting the same details.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | ThreatDown — "CARBONATO: a botnet built around an AI agent" | <https://www.threatdown.com/blog/carbonato/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/new-carbonato-malware-uses-ai-agents-to-hijack-exposed-docker-hosts/> |
| 3 | SecurityWeek, "In Other News" (25 Sep 2026) | <https://www.securityweek.com/in-other-news-clop-leak-site-takeover-docker-botnet-hunts-ai-keys-water-utility-exposure/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-22` (raw: ThreatDown 2026-09-22 / BleepingComputer 2026-09-24, precision `day`) |
| Kind | Real-world event `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`INFRA`](../../taxonomy/types.md#infra) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — vendor research report (ThreatDown) plus two independent outlets |
| Real harm | Yes — a live botnet with a multi-year operational trail |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-22-carbonato-docker-hermes-agent-botnet` |

<sub>**Why this classification:** a human operator deliberately deploys an agent framework on compromised hosts as the execution layer (`WEAPON`), the entry point is exposed agent-era infrastructure (`INFRA`, internet-facing Docker daemons), and what is taken is keys rather than data (`CRED`). `real_harm: true` because the campaign is operational and confirmed, `high` rather than `critical` because the archive reserves `critical` for confirmed multi-organisation / government / supply-chain-worm-scale damage or first-of-its-kind milestones — Hermes is now the fifth case, so the novelty trigger does not apply. Dated to the vendor's publication (22 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution (WEAPON)](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-22` [Gambit: three AI harnesses stole 600,000 card records](2026-09-22-gambit-ai-agent-retail-card-theft.md)<br>  <sub>The same Hermes framework, used as the orchestration layer of a card-skimming operation</sub>
- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>The earliest Hermes case in the archive — Hermes and OpenClaw sub-agents against Taiwanese government systems</sub>
- `2026-07-30` [Hermes agent at Thailand's Ministry of Finance](../2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br>  <sub>Government espionage with Hermes Agent in YOLO no-approval mode</sub>
- `2026-07-30` [Unit 42: autonomous campaigns run by Chinese-speaking operators](../2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br>  <sub>Hermes Agent with DeepSeek as the executor of a 460-target campaign</sub>
- `2026-09-10` [Anthropic's September threat report](2026-09-10-anthropic-september-threat-report.md)<br>  <sub>The defensive-side reading of agent-enabled post-exploitation</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-22-carbonato-docker-hermes-agent-botnet.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
