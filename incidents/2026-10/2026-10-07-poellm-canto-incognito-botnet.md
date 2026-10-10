---
id: 2026-10-07-poellm-canto-incognito-botnet
title: "PoeLLM: a botnet hides its C2 in a GitHub poem and turns exposed AI servers into mining proxies"
title_zh: "PoeLLM：僵尸网络把 C2 藏在 GitHub 诗歌里，把暴露的 AI 服务器变为挖矿代理"
title_ja: "PoeLLM：ボットネットはGitHubの詩にC2を隠し、露出したAIサーバーを採掘プロキシに変える"
title_ko: "PoeLLM: 봇넷이 GitHub 시(詩)에 C2를 숨기고 노출된 AI 서버를 채굴 프록시로 바꾼다"
title_de: "PoeLLM: Ein Botnetz versteckt sein C2 in einem GitHub-Gedicht und macht exponierte KI-Server zu Mining-Proxys"
title_fr: "PoeLLM : un botnet cache son C2 dans un poème GitHub et transforme les serveurs d'IA exposés en proxys de minage"
title_es: "PoeLLM: un botnet esconde su C2 en un poema de GitHub y convierte servidores de IA expuestos en proxys de minería"
date: 2026-10-07
date_raw: "active since April 2026; disclosed 2026-10-07 (Lumen Black Lotus Labs)"
date_precision: day

kind: incident
type: [INFRA, WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Lumen's Black Lotus Labs disclosed on 7 October 2026 a financially motivated botnet campaign — tracked as **Canto Incognito**, malware dubbed **PoeLLM** — that has compromised **more than 3,400 internet-facing servers since at least April 2026**, concentrated in the US and Western Europe, by exploiting exposed AI and developer services: **LiteLLM, Ollama, Gotenberg and Gitea**, plus an Ivanti Sentry entry point (CVE-2026-10520).** Exploitation includes **CVE-2026-42271 — command injection in LiteLLM's MCP testing endpoint (`/mcp-rest/test/connection`)** — the flaw this archive already recorded in June. Victims are mined for cryptocurrency (XMRig and Iron, connected to Kryptex) and repurposed as internet scanners and exploit servers — *"a private army of AI-enabled proxies"* — with remote-shell capability observed. The campaign's signature is its C2: there is **no hardcoded domain — four words extracted from a poem hosted on GitHub ("On the Nature of Connection", edited 11+ times and possibly AI-written) are mapped through a hard-coded dictionary into the current C2 IPv4 address**, so editing the poem moves the whole botnet. Peak activity reached **~2,200 affected servers in mid-June, with nearly 800 active per day**; recent SSH brute-force traffic suggests further experimentation. Lumen attributes the operation to an **Italian-speaking threat actor** with moderate confidence. The poem's GitHub repository has since been taken down, disrupting the campaign. Recorded `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`.

summary_zh: |
  **Lumen 旗下 Black Lotus Labs 于 2026 年 10 月 7 日披露了一个财务动机的僵尸网络行动——行动代号 **Canto Incognito**、恶意软件称 **PoeLLM**——自 2026 年 4 月以来已攻陷 **超过 3400 台面向互联网的服务器**，集中在美欧，手法是攻击暴露的 AI 与开发者服务：**LiteLLM、Ollama、Gotenberg、Gitea**，以及作为发现入口的 Ivanti Sentry（CVE-2026-10520）。** 利用的漏洞包括 **CVE-2026-42271——LiteLLM MCP 测试端点（`/mcp-rest/test/connection`）的命令注入**——本档案 6 月已有该漏洞记录。受害主机被用于挖矿（XMRig 与 Iron，接入 Kryptex）并被改造成全网扫描器与漏洞攻击服务器——*「一支由 AI 赋能代理组成的私人军队」*——并观测到远程 shell 能力。该行动最独特的是 C2：**没有硬编码域名——从 GitHub 上一首诗（《On the Nature of Connection》，已改 11 次以上、可能由 AI 写成）中抽出的四个词，经病毒内置字典映射出当前 C2 的 IPv4 地址**，改诗即可整体迁移僵尸网络。活动峰值在 6 月中旬：**约 2200 台受影响、日活近 800 台**；近期 SSH 暴力破解流量显示其仍在试验新能力。Lumen 以中等置信度将该行动归因于一个**讲意大利语的攻击者**。诗歌所在的 GitHub 仓库其后被下线，行动遭打断。记为 `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`。

summary_ja: |
  **LumenのBlack Lotus Labsは2026年10月7日、金銭目的のボットネット作戦——作戦名 **Canto Incognito**、マルウェア名 **PoeLLM**——を公表した。2026年4月以降、米国と西ヨーロッパを中心に**3,400台超のインターネット公開サーバー**を、露出したAI・開発者向けサービス（**LiteLLM、Ollama、Gotenberg、Gitea**、および発見の入口となったIvanti Sentry、CVE-2026-10520）を攻撃して侵害してきた。** 悪用には **CVE-2026-42271——LiteLLMのMCPテスト用エンドポイント（`/mcp-rest/test/connection`）のコマンドインジェクション**——が含まれ、本アーカイブは6月に同脆弱性を記録済み。被害ホストは暗号通貨の採掘（XMRigとIron、Kryptex接続）とネットスキャナー・攻撃サーバーへの転用——*「AIで武装したプロキシの私設軍隊」*——に使われ、リモートシェル能力も観測された。特徴はC2で、**ハードコードされたドメインはなく、GitHub上の詩（『On the Nature of Connection』、11回以上改訂、AI作の可能性）から抽出した4語を内蔵辞書でIPv4に変換**するため、詩を変えればボットネット全体が移動する。ピークは6月中旬で**約2,200台が影響、日次アクティブは約800台**。最近のSSHブルートフォース通信は新たな実験を示唆。Lumenは**イタリア語話者のアクター**と中程度の確信度で帰属。詩のGitHubリポジトリはその後削除され、作戦は妨害された。`incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_ko: |
  **Lumen의 Black Lotus Labs는 2026년 10월 7일 금전 목적의 봇넷 작전 — 작전명 **Canto Incognito**, 멀웨어명 **PoeLLM** — 을 공개했다. 2026년 4월부터 미국·서유럽을 중심으로 노출된 AI·개발자 서비스(**LiteLLM, Ollama, Gotenberg, Gitea**, 그리고 발견 경로가 된 Ivanti Sentry, CVE-2026-10520)를 공격해 **3,400대 넘는 인터넷 노출 서버**를 침해했다.** 악용에는 **CVE-2026-42271 — LiteLLM의 MCP 테스트 엔드포인트(`/mcp-rest/test/connection`) 명령 주입** — 이 포함되며, 본 아카이브는 6월에 이 취약점을 기록했다. 피해 호스트는 암호화폐 채굴(XMRig·Iron, Kryptex 연결)과 인터넷 스캐너·공격 서버로 전용된다 — *"AI로 무장한 프록시의 사설 군대"* — 원격 셸 능력도 관측됐다. 특징은 C2다: **하드코딩된 도메인이 없고, GitHub의 시(「On the Nature of Connection」, 11회 이상 개정, AI 작성 가능성)에서 추출한 네 단어를 내장 사전으로 IPv4로 변환**하므로 시를 고치면 봇넷 전체가 이동한다. 최고치는 6월 중순 **약 2,200대 영향, 일일 활성 약 800대**였고, 최근 SSH 무차별 대입 트래픽은 추가 실험을 시사한다. Lumen은 **이탈리아어 사용 위협 행위자**로 중간 신뢰도로 귀속했다. 시의 GitHub 저장소는 이후 삭제되어 작전이 중단됐다. `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_de: |
  **Lumens Black Lotus Labs veröffentlichten am 7. Oktober 2026 eine finanziell motivierte Botnetz-Kampagne — verfolgt als **Canto Incognito**, Malware **PoeLLM** — die seit mindestens April 2026 **mehr als 3.400 internetseitige Server** kompromittiert hat, vor allem in den USA und Westeuropa, indem sie exponierte KI- und Entwicklerdienste angreift: **LiteLLM, Ollama, Gotenberg und Gitea** sowie einen Ivanti-Sentry-Einstiegspunkt (CVE-2026-10520).** Die Ausnutzung umfasst **CVE-2026-42271 — Command Injection im LiteLLM-MCP-Testendpunkt (`/mcp-rest/test/connection`)** — die dieses Archiv bereits im Juni erfasste. Opfer werden für Kryptomining (XMRig und Iron, angebunden an Kryptex) missbraucht und zu Internetscannern und Exploit-Servern umfunktioniert — *„eine private Armee KI-gestützter Proxys"* — mit beobachteter Remote-Shell-Fähigkeit. Die Signatur der Kampagne ist ihr C2: **keine fest codierte Domain — vier Wörter aus einem auf GitHub gehosteten Gedicht („On the Nature of Connection", 11+ Mal geändert, möglicherweise KI-geschrieben) werden über ein fest codiertes Wörterbuch in die aktuelle C2-IPv4-Adresse übersetzt**, sodass eine Gedichtänderung das gesamte Botnetz bewegt. Spitzenwerte: **~2.200 betroffene Server Mitte Juni, fast 800 täglich aktiv**; jüngster SSH-Brute-Force-Verkehr deutet auf weitere Experimente hin. Lumen ordnet die Operation mit mittlerer Konfidenz einem **italienischsprachigen Akteur** zu. Das GitHub-Repository des Gedichts wurde inzwischen entfernt und die Kampagne so gestört. `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_fr: |
  **Les Black Lotus Labs de Lumen ont révélé le 7 octobre 2026 une campagne de botnet à motivation financière — suivie sous le nom de **Canto Incognito**, maliciel **PoeLLM** — qui a compromis **plus de 3 400 serveurs exposés à internet depuis au moins avril 2026**, surtout aux États-Unis et en Europe de l'Ouest, en exploitant des services d'IA et de développement exposés : **LiteLLM, Ollama, Gotenberg et Gitea**, plus un point d'entrée Ivanti Sentry (CVE-2026-10520).** L'exploitation inclut **CVE-2026-42271 — injection de commandes dans le point de terminaison MCP de test de LiteLLM (`/mcp-rest/test/connection`)** — faille déjà recensée dans cette archive en juin. Les victimes sont minées pour de la cryptomonnaie (XMRig et Iron, reliés à Kryptex) et transformées en scanners internet et serveurs d'exploit — *« une armée privée de proxys dopés à l'IA »* — avec une capacité de shell distant observée. La signature de la campagne est son C2 : **aucun domaine codé en dur — quatre mots extraits d'un poème hébergé sur GitHub (« On the Nature of Connection », modifié plus de 11 fois et peut-être écrit par une IA) sont convertis via un dictionnaire codé en dur en l'adresse IPv4 du C2**, de sorte que modifier le poème déplace tout le botnet. Pic d'activité : **~2 200 serveurs touchés à la mi-juin, près de 800 actifs par jour** ; un récent trafic de force brute SSH suggère de nouvelles expérimentations. Lumen attribue l'opération avec confiance modérée à un **acteur italophone**. Le dépôt GitHub du poème a depuis été retiré, perturbant la campagne. `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

summary_es: |
  **Los Black Lotus Labs de Lumen revelaron el 7 de octubre de 2026 una campaña de botnet con motivación financiera — seguida como **Canto Incognito**, con el malware **PoeLLM** — que ha comprometido **más de 3 400 servidores expuestos a internet desde al menos abril de 2026**, concentrados en EE. UU. y Europa Occidental, explotando servicios de IA y de desarrollo expuestos: **LiteLLM, Ollama, Gotenberg y Gitea**, más un punto de entrada Ivanti Sentry (CVE-2026-10520).** La explotación incluye **CVE-2026-42271 — inyección de comandos en el endpoint MCP de pruebas de LiteLLM (`/mcp-rest/test/connection`)** — fallo ya registrado en este archivo en junio. Las víctimas son minadas para criptomonedas (XMRig e Iron, conectados a Kryptex) y reconvertidas en escáneres de internet y servidores de exploit — *«un ejército privado de proxys impulsados por IA»* — con capacidad de shell remoto observada. La firma de la campaña es su C2: **no hay dominio codificado — cuatro palabras extraídas de un poema alojado en GitHub («On the Nature of Connection», editado más de 11 veces y posiblemente escrito por IA) se convierten mediante un diccionario interno en la dirección IPv4 del C2**, de modo que editar el poema mueve todo el botnet. El pico fue de **~2 200 servidores afectados a mediados de junio, con casi 800 activos al día**; el reciente tráfico de fuerza bruta SSH sugiere más experimentos. Lumen atribuye la operación con confianza moderada a un **actor de habla italiana**. El repositorio de GitHub del poema ya fue retirado, interrumpiendo la campaña. `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`

sources:
  - url: https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware
    label: Lumen Black Lotus Labs (primary)
  - url: https://cyberscoop.com/poellm-malware-botnet-poem-lumen-black-lotus-labs/
    label: CyberScoop
  - url: https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html
    label: The Hacker News
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.28"
---

# PoeLLM: a botnet hides its C2 in a GitHub poem and turns exposed AI servers into mining proxies

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-8F6A3C?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-3C6E8F?style=flat-square)

## Summary

**Lumen's Black Lotus Labs disclosed on 7 October 2026 a financially motivated botnet campaign — tracked as Canto Incognito, malware dubbed PoeLLM — that has compromised more than 3,400 internet-facing servers since at least April 2026, concentrated in the US and Western Europe, by exploiting exposed AI and developer services: LiteLLM, Ollama, Gotenberg and Gitea, plus an Ivanti Sentry entry point (CVE-2026-10520).** Exploitation includes **CVE-2026-42271 — command injection in LiteLLM's MCP testing endpoint (`/mcp-rest/test/connection`)** — the flaw this archive already recorded in June. Victims are mined for cryptocurrency (XMRig and Iron, connected to Kryptex) and repurposed as internet scanners and exploit servers — *"a private army of AI-enabled proxies"* — with remote-shell capability observed. The campaign's signature is its C2: there is **no hardcoded domain — four words extracted from a poem hosted on GitHub ("On the Nature of Connection", edited 11+ times and possibly AI-written) are mapped through a hard-coded dictionary into the current C2 IPv4 address**, so editing the poem moves the whole botnet. Peak activity reached **~2,200 affected servers in mid-June, with nearly 800 active per day**; recent SSH brute-force traffic suggests further experimentation. Lumen attributes the operation to an **Italian-speaking threat actor** with moderate confidence. The poem's GitHub repository has since been taken down, disrupting the campaign. Recorded `incident` / `INFRA` + `WEAPON` / `high` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Scans for exposed AI services:<br/>LiteLLM, Ollama, Gotenberg, Gitea"]:::entry
    S1["Exploits known flaws incl. the LiteLLM MCP<br/>endpoint (CVE-2026-42271) to install PoeLLM"]:::step
    S2["C2 IPv4 derived from four words in a GitHub poem;<br/>the poem is edited 11+ times to rotate servers"]:::step
    I["3,400+ servers mine crypto (XMRig/Iron → Kryptex)<br/>and become scanner / exploit proxies"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The campaign.** Since at least **April 2026**, a financially motivated operation — **"Canto Incognito"**, delivering the **PoeLLM** malware — has been compromising internet-exposed AI and adjacent services for cryptocurrency mining and botnet expansion. Lumen counted **more than 3,400 victim servers**, with peak activity in **mid-June at ~2,200 affected hosts and nearly 800 active per day**; victims are concentrated in **the United States and Western Europe**. Targets are enterprise, internet-facing deployments of **LiteLLM** (primary port 4000), **Ollama**, **Gotenberg** (port 3000) and **Gitea**; the investigation began from an **Ivanti Sentry** compromise (CVE-2026-10520). One of the exploits used is **CVE-2026-42271, a command-injection in LiteLLM's MCP testing endpoint (`/mcp-rest/test/connection`)** — this archive [recorded that flaw on 2026-06-08](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md); it is cross-linked rather than re-recorded here.

**C2 by poem.** The distinguishing technique: PoeLLM derives its C2 address from a poem, *"On the Nature of Connection"*, hosted in a GitHub repository (a fork of nodejs.org sources). Four words or phrases, extracted between fixed text anchors, are converted through a **hard-coded dictionary** (e.g. `driver` → 92, `diode` → 119) into the four octets of the current C2 IPv4 address; the poem was updated **11 times**, each time pointing infected hosts at a new server, and *"to anyone who comes across it, this is simply a poem on GitHub. It has no links, no files to download, no encrypted text."* Lumen notes the poem contains no Italian yet the actor's prose elsewhere is Italian — and assesses it "likely written by AI" precisely because it would have worked in any language. The GitHub repository has since been taken down, which Lumen describes as fully disrupting that C2 layer.

**Impact and grading.** Infected hosts are turned into **scanners and exploit servers** — *"the actor has effectively created a private army of AI-enabled proxies, which will continue to multiply and provide additional vectors for attack, credential theft, token abuse and more"* — and run **XMRig and Iron** miners paying into **Kryptex**. The malware can deploy remote-shells and further exploits from the C2; recent traffic toward SSH and other login portals suggests **distributed brute-force experimentation** whose maturity is unclear. Lumen assesses an **Italian-speaking actor** with moderate confidence (Italian code comments, Italian-hosted admin infrastructure). Recorded `INFRA` — in-the-wild exploitation of exposed LLM-serving services (including an MCP endpoint flaw) — **+** `WEAPON` — compromised AI servers repurposed as attack infrastructure. `real_harm: true` (3,400+ confirmed victims with mining and re-attack capability); `high` matches the archive's grading for the September CARBONATO botnet rather than `critical`. Confidence `A`: Lumen's primary report plus independent coverage from CyberScoop and The Hacker News.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Lumen Black Lotus Labs — "Canto incognito: tracking the PoeLLM malware" | <https://www.lumen.com/blog/en-us/canto-incognito-tracking-the-poellm-malware> |
| 2 | CyberScoop | <https://cyberscoop.com/poellm-malware-botnet-poem-lumen-black-lotus-labs/> |
| 3 | The Hacker News | <https://thehackernews.com/2026/10/poellm-malware-infects-3400-servers-to.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-07` (raw: active since April 2026; disclosed 2026-10-07, precision `day`) |
| Kind | Incident `incident` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`WEAPON`](../../taxonomy/types.md#weapon) |
| Severity | **High** `high` |
| Confidence | **A** — Lumen Black Lotus Labs primary report plus CyberScoop and The Hacker News |
| Real harm | Yes — 3,400+ servers compromised, mined and repurposed as attack proxies |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-07-poellm-canto-incognito-botnet` |

<sub>**Why this classification:** In-the-wild exploitation of exposed LLM-serving infrastructure (`INFRA`, including the MCP-endpoint flaw CVE-2026-42271 already recorded on 2026-06-08) combined with the mass weaponization of compromised AI servers as scanners/exploit proxies (`WEAPON`). `real_harm: true` — more than 3,400 confirmed victims. `high` under the confirmed-limited-scope-damage band, matched to the September CARBONATO botnet grading; the campaign is financially motivated and disruptive rather than a multi-organisation / critical-infrastructure event. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-06-08` [LiteLLM CVE-2026-42271 MCP endpoint takeover](../2026-06/2026-06-08-litellm-mcp-duan-dian-jie.md)<br>  <sub>The exact flaw PoeLLM exploits — recorded in June, now mass-exploited</sub>
- `2026-09-22` [CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys](../2026-09/2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>The closest precedent: a botnet monetizing and weaponizing AI-adjacent infrastructure</sub>
- `2025-02-01` [Ollama servers exposed at scale](../2025-02/2025-02-01-ollama-fu-wu-qi-gui.md)<br>  <sub>The oldest exposure in the same target class: unauthenticated, internet-facing LLM services</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-07-poellm-canto-incognito-botnet.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
