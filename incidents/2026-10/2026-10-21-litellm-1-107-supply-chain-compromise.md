---
id: 2026-10-21-litellm-1-107-supply-chain-compromise
title: "LiteLLM 1.107.0 compromised: malicious PyPI/Docker build ships a credential stealer"
title_zh: "LiteLLM 1.107.0 被投毒：恶意 PyPI/Docker 构建植入凭据窃取器"
title_ja: "LiteLLM 1.107.0が侵害：悪意あるPyPI/Dockerビルドが認証情報スティーラーを配布"
title_ko: "LiteLLM 1.107.0 침해: 악성 PyPI/Docker 빌드가 자격 증명 탈취기를 배포"
title_de: "LiteLLM 1.107.0 kompromittiert: bösartiger PyPI/Docker-Build liefert einen Credential-Stealer"
title_fr: "LiteLLM 1.107.0 compromis : une build PyPI/Docker malveillante embarque un voleur d'identifiants"
title_es: "LiteLLM 1.107.0 comprometido: una build maliciosa de PyPI/Docker incluye un ladrón de credenciales"
date: 2026-10-21
date_raw: "2026-10-21 (malicious 1.107.0 uploaded 11:39 UTC, quarantined on PyPI 13:20 UTC)"
date_precision: day

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 21 October 2026 a malicious build of **LiteLLM 1.107.0** — the widely-used open-source LLM gateway/proxy that fronts models for many AI agents — was pushed to **PyPI (11:39 UTC) and Docker Hub**, carrying a credential stealer; it was quarantined on PyPI by **13:20 UTC** after roughly **49,000 downloads**.** The GitHub source was clean, but all seven prebuilt **wheels** carried the payload: a `.pth`/`sitecustomize` **Python startup hook that runs on every interpreter start** (even if an app never imports litellm), harvesting across ~16 modules — browser credentials/cookies, **AWS/GCP/Azure** credentials, **AI-provider API keys (OpenAI, Anthropic, Cohere)**, the **LLM-provider credentials stored in a LiteLLM Proxy's PostgreSQL database**, and SSH/GPG keys and shell history — then encrypting and exfiltrating them to an attacker domain. A dormant second-stage remote-code loader was present but not observed active. LiteLLM quarantined the release and pulled the Docker tags; the initial attack vector is still unknown. This is a **second** LiteLLM package compromise (after the [March 2026 backdoored release](../2026-03/2026-03-24-litellm-backdoored-release.md)). Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true` — a live malicious release of agent infrastructure with ~49k downloads.

summary_zh: |
  **2026 年 10 月 21 日，**LiteLLM 1.107.0** 的一个恶意构建——这个被广泛使用的开源 LLM 网关/代理，为众多 AI agent 前置托管模型——被推上 **PyPI（11:39 UTC）与 Docker Hub**，内含凭据窃取器；在约 **4.9 万次下载**后，于 **13:20 UTC** 被 PyPI 隔离。** GitHub 源码是干净的，但全部 7 个预编译 **wheel** 都带载荷：一个 `.pth`/`sitecustomize` 的 **Python 启动钩子，每次解释器启动即运行**（哪怕应用从不 import litellm），通过约 16 个模块收割——浏览器凭据/cookie、**AWS/GCP/Azure** 凭证、**AI 提供方 API 密钥（OpenAI、Anthropic、Cohere）**、**LiteLLM Proxy 的 PostgreSQL 数据库里存的 LLM 提供方凭证**、以及 SSH/GPG 密钥与 shell 历史——随后加密外带到攻击者域名。还带有一个**处于休眠**的二阶段远程代码加载器（未见激活）。LiteLLM 已隔离该版本并下架 Docker 标签；初始攻击向量仍不明。这是 LiteLLM 包的**第二次**被投毒（继 [2026 年 3 月的后门版本](../2026-03/2026-03-24-litellm-backdoored-release.md)之后）。记为 `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`——一次约 4.9 万次下载的 agent 基础设施恶意发行。

summary_ja: |
  **2026年10月21日、**LiteLLM 1.107.0**（多くのAIエージェントのためにモデルを前段に置く、広く使われるオープンソースのLLMゲートウェイ/プロキシ）の悪意あるビルドが**PyPI（11:39 UTC）とDocker Hub**に公開され、認証情報スティーラーを内包していた。約**4万9千回のダウンロード**の後、**13:20 UTC**にPyPIで隔離された。** GitHubのソースはクリーンだったが、7つのプリビルド**ホイール**すべてにペイロードが含まれていた：`.pth`/`sitecustomize`の**インタープリタ起動時に毎回走るPythonスタートアップフック**（アプリがlitellmをimportしなくても）で、約16モジュールにわたり収集——ブラウザの認証情報/クッキー、**AWS/GCP/Azure**認証情報、**AIプロバイダーAPIキー（OpenAI、Anthropic、Cohere）**、**LiteLLM ProxyのPostgreSQLデータベースに保存されたLLMプロバイダー認証情報**、SSH/GPGキー、シェル履歴——を暗号化し攻撃者ドメインに送出した。休眠状態の二段目リモートコードローダーも存在したが稼働は観測されず。LiteLLMは当該版を隔離しDockerタグを削除。初期侵入経路は不明。これはLiteLLMパッケージの**2度目**の侵害（[2026年3月のバックドア版](../2026-03/2026-03-24-litellm-backdoored-release.md)に続く）。`incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_ko: |
  **2026년 10월 21일, 많은 AI 에이전트를 위해 모델을 앞단에서 중계하는 널리 쓰이는 오픈소스 LLM 게이트웨이/프록시 **LiteLLM 1.107.0**의 악성 빌드가 **PyPI(11:39 UTC)와 Docker Hub**에 올라왔고 자격 증명 탈취기를 담고 있었다. 약 **4만 9천 회 다운로드** 후 **13:20 UTC**에 PyPI에서 격리됐다.** GitHub 소스는 깨끗했지만 7개 사전빌드 **휠** 모두에 페이로드가 있었다: `.pth`/`sitecustomize`의 **인터프리터가 시작될 때마다 실행되는 Python 스타트업 훅**(앱이 litellm을 import하지 않아도)으로 약 16개 모듈에 걸쳐 수집——브라우저 자격 증명/쿠키, **AWS/GCP/Azure** 자격 증명, **AI 제공업체 API 키(OpenAI, Anthropic, Cohere)**, **LiteLLM Proxy의 PostgreSQL 데이터베이스에 저장된 LLM 제공업체 자격 증명**, SSH/GPG 키, 셸 기록——을 암호화해 공격자 도메인으로 유출했다. 휴면 상태의 2단계 원격 코드 로더도 있었으나 활성은 관측되지 않았다. LiteLLM은 해당 버전을 격리하고 Docker 태그를 내렸다. 최초 침입 경로는 불명. 이는 LiteLLM 패키지의 **두 번째** 침해([2026년 3월 백도어 버전](../2026-03/2026-03-24-litellm-backdoored-release.md)에 이어)다. `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_de: |
  **Am 21. Oktober 2026 wurde ein bösartiger Build von **LiteLLM 1.107.0** — dem weit verbreiteten quelloffenen LLM-Gateway/Proxy, der Modelle für viele KI-Agenten vorschaltet — auf **PyPI (11:39 UTC) und Docker Hub** veröffentlicht und enthielt einen Credential-Stealer; nach rund **49.000 Downloads** wurde er um **13:20 UTC** auf PyPI unter Quarantäne gestellt.** Der GitHub-Quellcode war sauber, doch alle sieben vorgebauten **Wheels** trugen die Payload: ein `.pth`/`sitecustomize`-**Python-Startup-Hook, der bei jedem Interpreterstart läuft** (auch wenn eine App litellm nie importiert) und über ~16 Module hinweg sammelt — Browser-Anmeldedaten/Cookies, **AWS/GCP/Azure**-Anmeldedaten, **KI-Anbieter-API-Schlüssel (OpenAI, Anthropic, Cohere)**, die **in der PostgreSQL-Datenbank eines LiteLLM-Proxys gespeicherten LLM-Anbieter-Anmeldedaten** sowie SSH-/GPG-Schlüssel und Shell-Verlauf — und sie verschlüsselt an eine Angreiferdomain exfiltriert. Ein ruhender Second-Stage-Remote-Code-Loader war vorhanden, aber nicht aktiv beobachtet. LiteLLM stellte die Version unter Quarantäne und entfernte die Docker-Tags; der ursprüngliche Angriffsvektor ist weiterhin unbekannt. Dies ist die **zweite** LiteLLM-Paketkompromittierung (nach der [Backdoor-Version vom März 2026](../2026-03/2026-03-24-litellm-backdoored-release.md)). `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_fr: |
  **Le 21 octobre 2026, une build malveillante de **LiteLLM 1.107.0** — la passerelle/proxy LLM open source très répandue qui place des modèles en frontal pour de nombreux agents IA — a été publiée sur **PyPI (11:39 UTC) et Docker Hub**, embarquant un voleur d'identifiants ; après environ **49 000 téléchargements**, elle a été mise en quarantaine sur PyPI à **13:20 UTC**.** La source GitHub était propre, mais les sept **wheels** précompilées portaient la charge : un **hook de démarrage Python** `.pth`/`sitecustomize` **exécuté à chaque lancement de l'interpréteur** (même si une app n'importe jamais litellm), collectant via ~16 modules — identifiants/cookies de navigateur, identifiants **AWS/GCP/Azure**, **clés API de fournisseurs d'IA (OpenAI, Anthropic, Cohere)**, les **identifiants de fournisseurs LLM stockés dans la base PostgreSQL d'un LiteLLM Proxy**, ainsi que clés SSH/GPG et historique shell — puis les chiffrant et exfiltrant vers un domaine attaquant. Un chargeur de code distant de second étage dormant était présent mais non observé actif. LiteLLM a mis la version en quarantaine et retiré les tags Docker ; le vecteur d'attaque initial reste inconnu. C'est la **deuxième** compromission du paquet LiteLLM (après la [version avec porte dérobée de mars 2026](../2026-03/2026-03-24-litellm-backdoored-release.md)). `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

summary_es: |
  **El 21 de octubre de 2026, una build maliciosa de **LiteLLM 1.107.0** —la pasarela/proxy de LLM de código abierto muy usada que antepone modelos para muchos agentes de IA— se publicó en **PyPI (11:39 UTC) y Docker Hub**, con un ladrón de credenciales; tras unas **49.000 descargas**, fue puesta en cuarentena en PyPI a las **13:20 UTC**.** El código de GitHub estaba limpio, pero las siete **wheels** precompiladas llevaban la carga: un **hook de arranque de Python** `.pth`/`sitecustomize` **que se ejecuta en cada inicio del intérprete** (aunque una app nunca importe litellm), recopilando a través de ~16 módulos — credenciales/cookies de navegador, credenciales **AWS/GCP/Azure**, **claves API de proveedores de IA (OpenAI, Anthropic, Cohere)**, las **credenciales de proveedores LLM almacenadas en la base PostgreSQL de un LiteLLM Proxy**, además de claves SSH/GPG e historial de shell — y luego cifrándolas y exfiltrándolas a un dominio del atacante. Había un cargador de código remoto de segunda etapa inactivo, pero no se observó activo. LiteLLM puso la versión en cuarentena y retiró las etiquetas de Docker; el vector de ataque inicial sigue siendo desconocido. Es la **segunda** compromisión del paquete LiteLLM (tras la [versión con puerta trasera de marzo de 2026](../2026-03/2026-03-24-litellm-backdoored-release.md)). `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true`

sources:
  - url: https://www.wiz.io/blog/litellm-compromised-steals-credentials
    label: Wiz
  - url: https://research.jfrog.com/post/litellm-hijacked-again/
    label: JFrog Security Research
  - url: https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html
    label: The Hacker News
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.32"
---

# LiteLLM 1.107.0 compromised: malicious PyPI/Docker build ships a credential stealer

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 21 October 2026 a malicious build of LiteLLM 1.107.0 — the widely-used open-source LLM gateway/proxy that fronts models for many AI agents — was pushed to PyPI (11:39 UTC) and Docker Hub, carrying a credential stealer; it was quarantined on PyPI by 13:20 UTC after roughly 49,000 downloads.** The GitHub source was clean, but all seven prebuilt wheels carried the payload: a `.pth`/`sitecustomize` Python startup hook that runs on every interpreter start (even if an app never imports litellm), harvesting across ~16 modules — browser credentials/cookies, AWS/GCP/Azure credentials, AI-provider API keys (OpenAI, Anthropic, Cohere), the LLM-provider credentials stored in a LiteLLM Proxy's PostgreSQL database, and SSH/GPG keys and shell history — then encrypting and exfiltrating them to an attacker domain. A dormant second-stage remote-code loader was present but not observed active. LiteLLM quarantined the release and pulled the Docker tags; the initial attack vector is still unknown. This is a second LiteLLM package compromise (after the [March 2026 backdoored release](../2026-03/2026-03-24-litellm-backdoored-release.md)). Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: true` — a live malicious release of agent infrastructure with ~49k downloads.

## Attack chain

```mermaid
flowchart LR
    E["Malicious LiteLLM 1.107.0 wheels pushed to<br/>PyPI (11:39 UTC) + Docker Hub"]:::entry
    S1["GitHub source clean; payload only in the<br/>7 prebuilt wheels (absent from the git tag)"]:::step
    S2["Python startup hook runs on every interpreter<br/>start → ~16-module credential stealer"]:::step
    I["Browser/cloud/AI-provider keys + LiteLLM Proxy<br/>DB creds + SSH/GPG exfiltrated; ~49k downloads"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **21 October 2026**, a malicious version **1.107.0** of **LiteLLM** — the widely-used open-source LLM gateway/proxy that many AI agents and apps use to route to model providers — was published to **PyPI at 11:39 UTC** and to **Docker Hub**. Multiple security vendors (Wiz, JFrog, Mend, OX Security, Datadog, Chainguard, Endor, plus SafeDep/Socket/StepSecurity/Upwind via The Hacker News) analysed it. PyPI **quarantined** the release by **13:20 UTC**; ClickPy data indicates roughly **49,000 downloads** before removal.

**The payload.** The **GitHub source was clean**, but all **seven prebuilt wheels** (and the Docker images) carried the malware — the payload traces to a commit absent from the v1.107.0 git tag. A `.pth` file plus a `sitecustomize.py` install a **Python startup hook that executes on every interpreter start**, so the stealer runs **even if an application never imports `litellm`**. Across ~16 modules it harvests browser credentials and cookies (Chrome/Firefox/Edge/Safari), **AWS/GCP/Azure** credentials and tokens, **AI-provider API keys (OpenAI, Anthropic, Cohere)**, the **LLM-provider credentials stored in a LiteLLM Proxy's PostgreSQL database**, and SSH/GPG keys and shell history, then **encrypts and exfiltrates** them to an attacker-controlled domain. A **second-stage remote-code loader was present but dormant** — Wiz did not observe it fetching/running remote code — so this is scoped as a credential stealer with a latent loader, not an actively-running RAT.

**Why `real_harm: true`.** Unlike a PoC or a quickly-caught upload with no installs, this was a **live malicious release that was actually distributed** (~49,000 downloads) with a stealer that runs on import-less Python startup; the consistent vendor guidance is to **assume exposure and rotate every credential** the host could reach. No single named victim's loss is published, but real credential exposure at scale is the expected effect. (LiteLLM's March 2026 compromise is recorded separately; this is the second.)

**How it is graded.** `incident` — a real malicious distribution, not a disclosed-but-unused flaw. `SUPPLY` (poisoned PyPI/Docker build of agent infrastructure) + `CRED` (what is stolen is keys — cloud, AI-provider and proxy-stored LLM credentials). `real_harm: true` (live, downloaded ~49k times, active stealer). Severity `high`: wide distribution and credential theft, but caught and quarantined within ~1.6 hours and the second stage stayed dormant. Confidence `A`: concurrent first-party analyses from many security vendors (Wiz, JFrog, Mend, OX, Datadog, Chainguard, Endor) and The Hacker News.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz | <https://www.wiz.io/blog/litellm-compromised-steals-credentials> |
| 2 | JFrog Security Research | <https://research.jfrog.com/post/litellm-hijacked-again/> |
| 3 | The Hacker News | <https://thehackernews.com/2026/10/litellm-compromised-in-supply-chain.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-21` (raw: malicious 1.107.0 uploaded 11:39 UTC, quarantined on PyPI 13:20 UTC, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — concurrent analyses from Wiz, JFrog, Mend, OX, Datadog, Chainguard, Endor + The Hacker News |
| Real harm | Yes — live malicious release, ~49k downloads, credential stealer running on Python startup |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-21-litellm-1-107-supply-chain-compromise` |

<sub>**Why this classification:** A poisoned PyPI/Docker build of LiteLLM, the LLM gateway fronting many agents (`SUPPLY`), carrying a credential stealer that targets cloud, AI-provider and proxy-stored LLM keys (`CRED`). `incident` with `real_harm: true` because it was a live, widely-downloaded release with an active stealer (vendors advise assuming credential exposure). `high` not `critical`: broad reach but quarantined within ~1.6 hours and the remote-code loader stayed dormant. Second LiteLLM compromise, recorded separately from the March 2026 one. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply chain](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-03-24` [LiteLLM ships a backdoored release](../2026-03/2026-03-24-litellm-backdoored-release.md)<br>  <sub>The first LiteLLM package compromise — this is the second</sub>
- `2026-10-08` [Tensorlake npm SDK compromise harvests agent config and credentials](2026-10-08-tensorlake-npm-sdk-compromise.md)<br>  <sub>Same month — supply-chain theft of AI-agent provider keys</sub>
- `2026-08-04` [ChainDrop npm supply-chain wave](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>Another agent-targeting package-registry compromise</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-21-litellm-1-107-supply-chain-compromise.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
