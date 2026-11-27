---
id: 2026-11-17-microsoft-agent-framework-pypi-hijack
title: "Microsoft's agent-framework PyPI package is hijacked to ship a credential stealer aimed at Azure and CI pipelines"
title_zh: "微软 agent-framework 的 PyPI 包被劫持，植入针对 Azure 和 CI 流水线的凭据窃取器"
title_ja: "Microsoftのagent-framework PyPIパッケージが乗っ取られ、AzureとCIパイプラインを狙う認証情報窃取コードを配布"
title_ko: "Microsoft의 agent-framework PyPI 패키지가 탈취되어 Azure와 CI 파이프라인을 노린 자격 증명 탈취 코드가 배포됨"
title_de: "Microsofts PyPI-Paket agent-framework wird gekapert und liefert einen Credential-Stealer für Azure und CI-Pipelines aus"
title_fr: "Le paquet PyPI agent-framework de Microsoft est détourné pour diffuser un voleur d'identifiants visant Azure et les pipelines CI"
title_es: "El paquete de PyPI agent-framework de Microsoft es secuestrado para distribuir un ladrón de credenciales dirigido a Azure y a los pipelines de CI"
date: 2026-11-17
date_raw: "2026-11-17 (malicious agent-framework 1.26.1 published 20:35 UTC and 1.26.2 about 21:08 UTC; both unavailable by about 21:30 UTC; Wiz root-cause update 2026-11-18)"
date_precision: day

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 17 November 2026, two malicious releases of `agent-framework`, Microsoft's official Python package for building AI agents, were published to PyPI with a credential stealer added.** Version 1.26.1 appeared at 20:35 UTC and 1.26.2 at about 21:08 UTC; both were unavailable by about 21:30 UTC, and 1.26.0 is the last safe version. The package has roughly 190,000 to 200,000 downloads a month. Each release dropped a `.pth` file into site-packages, so the stealer ran on every Python interpreter start even if the package was never imported. It collected secret-named environment variables (including Azure, AWS, GitHub, OpenAI and Hugging Face names), credential files such as Azure CLI state, `.npmrc`, `.git-credentials` and Docker config, secrets from other processes' environments, and tried to mint Azure managed-identity, Azure DevOps and GitHub Actions OIDC tokens; everything was posted to a single webhook.site URL. Wiz, which could read the attacker's free-tier webhook, counted 50 stored requests, of which 17 represent three unique, successful exfiltrations of victim data. Wiz reports that the attacker appears to have compromised a client certificate and private key for Microsoft's internal release pipeline (ESRP), and that the attacker's tooling identified itself as Cairn, an open-source AI penetration-testing framework. StepSecurity notes that a new maintainer account was added to the project the same day and that the second release was uploaded after PyPI quarantined the first. Microsoft has not published an advisory; a spokesperson told The Register it had made some repositories private while investigating malicious content. How the publishing credentials were obtained is not known.

summary_zh: |
  **2026 年 11 月 17 日，微软官方用于构建 AI agent 的 Python 包 `agent-framework` 有两个恶意版本被发布到 PyPI，其中加入了凭据窃取器。** 1.26.1 于 20:35 UTC 出现，1.26.2 约 21:08 UTC 出现；约 21:30 UTC 两者均已下架，最后一个安全版本是 1.26.0。该包月下载量约 19 万到 20 万。两个版本都会在 site-packages 里放一个 `.pth` 文件，因此只要 Python 解释器启动，窃取器就会运行，哪怕从未导入这个包。它收集名字像密钥的环境变量（含 Azure、AWS、GitHub、OpenAI、Hugging Face 等字样），收集 Azure CLI 状态、`.npmrc`、`.git-credentials`、Docker 配置等凭据文件，读取其他进程环境里的密钥，并尝试签发 Azure 托管身份、Azure DevOps 和 GitHub Actions 的 OIDC 令牌；全部内容发往同一个 webhook.site 地址。Wiz 能读到攻击者那个免费档 webhook，统计到 50 条留存请求，其中 17 条对应 3 起互不相同、成功外带受害方数据的案例。Wiz 报告称，攻击者似乎拿到了微软内部发布流水线（ESRP）的客户端证书和私钥，且攻击者的工具自称 Cairn（一款开源 AI 渗透测试框架）。StepSecurity 指出，当天项目新增了一个维护者账号，第二个恶意版本是在 PyPI 隔离第一个之后上传的。微软没有发布公告；其发言人对 The Register 表示，调查恶意内容期间已把部分仓库设为私有。发布凭据是如何被拿到的，目前不清楚。

summary_ja: |
  **2026年11月17日、AIエージェント構築用のMicrosoft公式Pythonパッケージ`agent-framework`の悪意あるリリース2件が、認証情報窃取コードを加えた状態でPyPIに公開された。** 1.26.1は20:35 UTC、1.26.2は21:08 UTCごろに現れ、21:30 UTCごろまでに両方とも入手できなくなった。最後の安全なバージョンは1.26.0である。このパッケージの月間ダウンロード数は約19万から20万。各リリースはsite-packagesに`.pth`ファイルを置くため、パッケージを一度もインポートしなくても、Pythonインタプリタが起動するたびに窃取コードが実行された。秘密情報らしい名前の環境変数（Azure、AWS、GitHub、OpenAI、Hugging Faceなどを含む）、Azure CLIの状態、`.npmrc`、`.git-credentials`、Docker設定などの認証情報ファイル、他プロセスの環境変数内の秘密情報を収集し、AzureマネージドID、Azure DevOps、GitHub ActionsのOIDCトークンの発行も試みた。すべて単一のwebhook.siteのURLに送信された。攻撃者の無料枠のwebhookを閲覧できたWizは、保存された50件のリクエストを数え、そのうち17件が被害者データの流出に成功した3件の個別事例に当たるとした。Wizによれば、攻撃者はMicrosoftの社内リリースパイプライン（ESRP）のクライアント証明書と秘密鍵を侵害したとみられ、攻撃者のツールは自らをCairn（オープンソースのAIペネトレーションテスト・フレームワーク）と名乗っていた。StepSecurityは、同日にプロジェクトへ新しいメンテナーアカウントが追加され、2件目はPyPIが1件目を隔離した後にアップロードされたと指摘する。Microsoftはアドバイザリを公開しておらず、広報担当者はThe Registerに対し、悪意あるコンテンツの調査中は一部のリポジトリを非公開にしたと述べた。公開用の認証情報がどう入手されたかは分かっていない。

summary_ko: |
  **2026년 11월 17일, AI 에이전트 구축용 Microsoft 공식 Python 패키지 `agent-framework`의 악성 릴리스 두 개가 자격 증명 탈취 코드가 추가된 채 PyPI에 게시됐다.** 1.26.1은 20:35 UTC에, 1.26.2는 21:08 UTC 무렵에 올라왔고, 21:30 UTC 무렵에는 둘 다 내려갔다. 마지막 안전 버전은 1.26.0이다. 이 패키지의 월간 다운로드는 약 19만에서 20만 건이다. 각 릴리스는 site-packages에 `.pth` 파일을 떨어뜨려, 패키지를 한 번도 임포트하지 않아도 Python 인터프리터가 시작될 때마다 탈취 코드가 실행됐다. 비밀 값처럼 보이는 이름의 환경 변수(Azure, AWS, GitHub, OpenAI, Hugging Face 등 포함), Azure CLI 상태와 `.npmrc`, `.git-credentials`, Docker 설정 같은 자격 증명 파일, 다른 프로세스 환경의 비밀 값을 수집했고, Azure 관리 ID와 Azure DevOps, GitHub Actions OIDC 토큰 발급도 시도했다. 모든 데이터는 하나의 webhook.site URL로 전송됐다. 공격자의 무료 등급 webhook을 읽을 수 있었던 Wiz는 저장된 요청 50건을 확인했고, 그중 17건이 피해자 데이터 유출에 성공한 서로 다른 3건에 해당한다고 밝혔다. Wiz에 따르면 공격자는 Microsoft 내부 릴리스 파이프라인(ESRP)의 클라이언트 인증서와 개인 키를 탈취한 것으로 보이며, 공격자의 도구는 스스로를 Cairn(오픈소스 AI 침투 테스트 프레임워크)이라고 밝혔다. StepSecurity는 같은 날 프로젝트에 새 유지관리자 계정이 추가됐고, 두 번째 릴리스는 PyPI가 첫 번째를 격리한 뒤 업로드됐다고 지적한다. Microsoft는 권고문을 내지 않았으며, 대변인은 The Register에 악성 콘텐츠를 조사하는 동안 일부 저장소를 비공개로 전환했다고 말했다. 게시용 자격 증명이 어떻게 확보됐는지는 알려지지 않았다.

summary_de: |
  **Am 17. November 2026 wurden zwei bösartige Versionen von `agent-framework`, Microsofts offiziellem Python-Paket zum Bau von KI-Agenten, mit einem zusätzlichen Credential-Stealer auf PyPI veröffentlicht.** Version 1.26.1 erschien um 20:35 UTC, 1.26.2 gegen 21:08 UTC; gegen 21:30 UTC waren beide nicht mehr verfügbar, die letzte sichere Version ist 1.26.0. Das Paket kommt auf rund 190.000 bis 200.000 Downloads im Monat. Jede Version legte eine `.pth`-Datei in site-packages ab, sodass der Stealer bei jedem Start eines Python-Interpreters lief, auch wenn das Paket nie importiert wurde. Er sammelte Umgebungsvariablen mit geheimnisverdächtigen Namen (darunter Azure, AWS, GitHub, OpenAI und Hugging Face), Zugangsdateien wie den Azure-CLI-Zustand, `.npmrc`, `.git-credentials` und die Docker-Konfiguration, Geheimnisse aus den Umgebungen anderer Prozesse und versuchte, OIDC-Token für Azure Managed Identities, Azure DevOps und GitHub Actions auszustellen; alles ging an eine einzige webhook.site-URL. Wiz konnte den Free-Tier-Webhook des Angreifers einsehen und zählte 50 gespeicherte Anfragen, von denen 17 auf drei eindeutige, erfolgreiche Exfiltrationen von Opferdaten entfallen. Wiz berichtet, der Angreifer habe offenbar ein Client-Zertifikat samt privatem Schlüssel für Microsofts interne Release-Pipeline (ESRP) kompromittiert, und sein Werkzeug habe sich als Cairn ausgegeben, ein quelloffenes Framework für KI-Penetrationstests. StepSecurity merkt an, dass dem Projekt am selben Tag ein neues Maintainer-Konto hinzugefügt wurde und die zweite Version hochgeladen wurde, nachdem PyPI die erste unter Quarantäne gestellt hatte. Microsoft hat kein Advisory veröffentlicht; ein Sprecher sagte The Register, man habe einige Repositories während der Untersuchung bösartiger Inhalte auf privat gestellt. Wie die Veröffentlichungs-Zugangsdaten erlangt wurden, ist nicht bekannt.

summary_fr: |
  **Le 17 novembre 2026, deux versions malveillantes de `agent-framework`, le paquet Python officiel de Microsoft pour construire des agents IA, ont été publiées sur PyPI avec un voleur d'identifiants ajouté.** La version 1.26.1 est apparue à 20 h 35 UTC et la 1.26.2 vers 21 h 08 UTC ; les deux n'étaient plus disponibles vers 21 h 30 UTC, et la 1.26.0 est la dernière version saine. Le paquet compte environ 190 000 à 200 000 téléchargements par mois. Chaque version déposait un fichier `.pth` dans site-packages, de sorte que le voleur s'exécutait à chaque démarrage d'un interpréteur Python, même si le paquet n'était jamais importé. Il collectait les variables d'environnement au nom évocateur de secrets (dont Azure, AWS, GitHub, OpenAI et Hugging Face), des fichiers d'identifiants comme l'état d'Azure CLI, `.npmrc`, `.git-credentials` et la configuration Docker, les secrets des environnements d'autres processus, et tentait d'émettre des jetons OIDC d'identité managée Azure, d'Azure DevOps et de GitHub Actions ; le tout était envoyé à une seule URL webhook.site. Wiz, qui pouvait lire le webhook gratuit de l'attaquant, a compté 50 requêtes stockées, dont 17 correspondent à trois exfiltrations distinctes et réussies de données de victimes. Wiz indique que l'attaquant semble avoir compromis un certificat client et une clé privée du pipeline de publication interne de Microsoft (ESRP), et que son outillage s'identifiait comme Cairn, un cadre open source de tests d'intrusion par IA. StepSecurity note qu'un nouveau compte de mainteneur a été ajouté au projet le même jour et que la seconde version a été envoyée après la mise en quarantaine de la première par PyPI. Microsoft n'a pas publié d'avis ; un porte-parole a déclaré à The Register avoir rendu privés certains dépôts le temps d'enquêter sur du contenu malveillant. On ignore comment les identifiants de publication ont été obtenus.

summary_es: |
  **El 17 de noviembre de 2026 se publicaron en PyPI dos versiones maliciosas de `agent-framework`, el paquete oficial de Python de Microsoft para construir agentes de IA, con un ladrón de credenciales añadido.** La versión 1.26.1 apareció a las 20:35 UTC y la 1.26.2 hacia las 21:08 UTC; hacia las 21:30 UTC ninguna estaba disponible, y la 1.26.0 es la última versión segura. El paquete tiene entre unas 190.000 y 200.000 descargas al mes. Cada versión dejaba un archivo `.pth` en site-packages, de modo que el ladrón se ejecutaba en cada arranque de un intérprete de Python aunque el paquete nunca se importara. Recogía variables de entorno con nombres propios de secretos (entre ellos Azure, AWS, GitHub, OpenAI y Hugging Face), archivos de credenciales como el estado de Azure CLI, `.npmrc`, `.git-credentials` y la configuración de Docker, secretos de los entornos de otros procesos, e intentaba emitir tokens OIDC de identidad administrada de Azure, de Azure DevOps y de GitHub Actions; todo se enviaba a una única URL de webhook.site. Wiz, que pudo leer el webhook gratuito del atacante, contó 50 peticiones almacenadas, de las que 17 corresponden a tres exfiltraciones únicas y exitosas de datos de víctimas. Wiz señala que el atacante parece haber comprometido un certificado de cliente y una clave privada del pipeline interno de publicación de Microsoft (ESRP), y que sus herramientas se identificaban como Cairn, un marco de código abierto de pruebas de penetración con IA. StepSecurity apunta que ese mismo día se añadió al proyecto una nueva cuenta de mantenedor y que la segunda versión se subió después de que PyPI pusiera en cuarentena la primera. Microsoft no ha publicado un aviso; un portavoz dijo a The Register que había hecho privados algunos repositorios mientras investigaba contenido malicioso. No se sabe cómo se obtuvieron las credenciales de publicación.

sources:
  - url: https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi
    label: Wiz Research (timeline, root cause, analysis of exfiltrated data)
  - url: https://www.ox.security/blog/breaking-hijacked-releases-of-microsofts-official-agent-framework-steals-azure-and-ci-credentials/
    label: OX Security (payload analysis)
  - url: https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised
    label: StepSecurity (release and maintainer timeline)
  - url: https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858
    label: The Register (carries Microsoft's statement)
  - url: https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/
    label: BleepingComputer
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# Microsoft's agent-framework PyPI package is hijacked to ship a credential stealer aimed at Azure and CI pipelines

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 17 November 2026, two malicious releases of `agent-framework`, Microsoft's official Python package for building AI agents, were published to PyPI with a credential stealer added.** Version 1.26.1 appeared at 20:35 UTC and 1.26.2 at about 21:08 UTC; both were unavailable by about 21:30 UTC, and 1.26.0 is the last safe version. The package has roughly 190,000 to 200,000 downloads a month. Each release dropped a `.pth` file into site-packages, so the stealer ran on every Python interpreter start even if the package was never imported. It collected secret-named environment variables (including Azure, AWS, GitHub, OpenAI and Hugging Face names), credential files such as Azure CLI state, `.npmrc`, `.git-credentials` and Docker config, secrets from other processes' environments, and tried to mint Azure managed-identity, Azure DevOps and GitHub Actions OIDC tokens; everything was posted to a single webhook.site URL. Wiz, which could read the attacker's free-tier webhook, counted 50 stored requests, of which 17 represent three unique, successful exfiltrations of victim data. Wiz reports that the attacker appears to have compromised a client certificate and private key for Microsoft's internal release pipeline (ESRP), and that the attacker's tooling identified itself as Cairn, an open-source AI penetration-testing framework. StepSecurity notes that a new maintainer account was added to the project the same day and that the second release was uploaded after PyPI quarantined the first. Microsoft has not published an advisory; a spokesperson told The Register it had made some repositories private while investigating malicious content. How the publishing credentials were obtained is not known.

## Attack chain

```mermaid
flowchart LR
    A["Attacker obtains publishing access<br/>to Microsoft's agent-framework<br/>on PyPI (route not established)"]:::entry
    B["Malicious 1.26.1 and 1.26.2<br/>ship a .pth file that runs<br/>on every Python start"]:::step
    C["Stealer collects env secrets,<br/>credential files and Azure /<br/>CI OIDC tokens"]:::step
    D["Data posted to webhook.site;<br/>three unique victim<br/>exfiltrations counted by Wiz"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What was published and when.** `agent-framework` is Microsoft's Python framework for building AI agents and coordinating them in workflows. The legitimate 1.26.0 was published on 12 November 2026. On 17 November a malicious 1.26.1 was uploaded at 20:35 UTC and a second malicious release, 1.26.2, at about 21:08 UTC; by about 21:30 UTC neither was available on PyPI. StepSecurity records that a maintainer account named `vibiret` was created and added to the project on 17 November, that 1.26.1 was uploaded as a wheel only with no provenance, and that the second release was uploaded after the first had been quarantined. OX Security gives 192,534 monthly downloads; Wiz gives about 41,000 a week and BleepingComputer roughly 200,000 a month.

**How the payload ran.** Version 1.26.1 dropped `agent_framework_meta.pth` into the site-packages root. Python executes import lines in `.pth` files at every interpreter start, so the stealer ran in every Python process in that environment whether or not the package was imported. Because the release pulled in the genuine `agent-framework-core` 1.26.0, the framework kept working. The code forked into a detached session, set a marker environment variable so it fired once per process tree, and used file and function names made to look like SDK telemetry. Version 1.26.2 was a repack with a different trigger (`af_runtime_diag.pth` and a new top-level module), so a search for the 1.26.1 file names misses it.

**What it collected.** Environment variables whose names contain strings such as TOKEN, SECRET, PASSWORD, KEY, AZURE, AWS, GITHUB, OPENAI, HF_ and FOUNDRY; secret-looking values from up to 300 other processes' environments; up to 60 credential files (Azure CLI state, `.npmrc`, `pip.conf`, `.netrc`, `.git-credentials`, Docker config, Hugging Face tokens, Azure DevOps agent credentials, `.env` and JSON files under `/app` and `/workspace`); Azure DevOps OIDC tokens where the pipeline variables were present; and Azure managed-identity tokens for a dozen resources including ARM, Graph, Key Vault and Storage. Version 1.26.2 added GitHub Actions OIDC theft in workflows with `id-token: write`, more variable names and GitHub-hosted runner paths. Everything was compressed, encoded and sent in one HTTPS POST to a hard-coded webhook.site URL, with no fallback channel and no retry.

**What limited the damage.** The attacker used a free-tier webhook.site URL not attached to an account, which accepts at most 100 requests and expires after seven days. Wiz confirmed the token was on the free tier and that a maximum of 50 requests were captured. Of those, four came from the attacker's own machines, 29 appear to come from sandboxes, vendor scanners and tests, and the remaining 17 represent three unique, successful exfiltrations of victim data. Those requests can still contain working cloud, CI and registry credentials.

**How the attacker got publishing access is not settled.** Wiz reports that the attacker appears to have compromised a client certificate and private key for Microsoft ESRP, the internal service used to sign and publish the package; a first publish attempt from AWS was rejected by ESRP's IP filtering and a second from Microsoft-owned IP space succeeded. The Register's reporting points at a compromised administrator account in Microsoft's GitHub organisation, and OX Security says the attackers appear to have found a way to hijack the wheel creation flow. Microsoft has published no advisory or post-mortem; its statement to The Register says only that it had made some repositories private while it investigates malicious content. How the credentials were obtained is not known.

**The attacker's tooling.** Wiz observed part of the operation because the attacker's tooling reported its own progress to the same public webhook it used for exfiltration. That tooling identified itself as Cairn: it staged the package at `/tmp/cairn_pkg` and sent a `CAIRN_ESRP_PROBE2` connectivity probe. Before publishing, the attacker ran the stealer on their own machine, and that run captured an AI coding-agent configuration that appears to be the open-source Pi harness backed by a GLM-family model. This is Wiz's observation alone and has not been confirmed by Microsoft.

**How it is graded.** `incident`: malicious code was served from the official package of a major vendor and ran on real hosts. `SUPPLY` because the attack sits on the dependency chain of agent builders; `CRED` because what the payload takes is keys and tokens. `real_harm: true` on Wiz's count of three successful victim exfiltrations. `high`: an official agent framework was trojanised and working credentials left victim environments, while the exposure window was under an hour and the confirmed victim count is small.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz Research (timeline, root cause, analysis of exfiltrated data) | <https://www.wiz.io/blog/malicious-version-of-microsofts-agent-framework-published-to-pypi> |
| 2 | OX Security (payload analysis) | <https://www.ox.security/blog/breaking-hijacked-releases-of-microsofts-official-agent-framework-steals-azure-and-ci-credentials/> |
| 3 | StepSecurity (release and maintainer timeline) | <https://www.stepsecurity.io/blog/microsoft-agent-framework-pypi-package-compromised> |
| 4 | The Register (carries Microsoft's statement) | <https://www.theregister.com/security/2026/11/18/microsofts-official-python-agent-framework-hijacked-to-distribute-malware/5310858> |
| 5 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/microsofts-agent-framework-pypi-package-compromised-to-steal-credentials/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-17` (raw: 2026-11-17 (malicious agent-framework 1.26.1 published 20:35 UTC and 1.26.2 about 21:08 UTC; both unavailable by about 21:30 UTC; Wiz root-cause update 2026-11-18), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — three independent technical analyses of the published artefacts (Wiz, OX Security, StepSecurity), plus BleepingComputer's reporting and Microsoft's statement to The Register; no Microsoft advisory |
| Real harm | Yes — three unique, successful exfiltrations of victim data counted by Wiz from the attacker's webhook |
| AI involvement | Confirmed `confirmed` — the trojanised package is Microsoft's official framework for building AI agents; Wiz additionally reports the attacker's tooling identified itself as the Cairn agent framework |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-11-17-microsoft-agent-framework-pypi-hijack` |

<sub>**Why this classification:** Malicious releases of an official agent framework ran on real hosts (`incident`): the attack is on the dependency chain of agent builders (`SUPPLY`) and takes keys and tokens (`CRED`), with three successful victim exfiltrations counted, hence `real_harm: true`. `high`: a major vendor's agent package was trojanised, limited by a sub-hour window and a capped webhook. `confidence: A`: several independent analyses of the same public artefacts agree on the payload and timeline; the route to publishing access differs between sources and is recorded as unsettled. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-10-21` [LiteLLM 1.107.0 compromised: malicious PyPI/Docker build ships a credential stealer](../2026-10/2026-10-21-litellm-1-107-supply-chain-compromise.md)<br>  <sub>The previous month's trojanised AI-tooling release on PyPI, with the same goal of harvesting credentials</sub>
- `2026-10-08` [Tensorlake's npm SDK is compromised in a wave that harvests AI-agent credentials and configs](../2026-10/2026-10-08-tensorlake-npm-sdk-compromise.md)<br>  <sub>The npm-side counterpart: an agent SDK used to collect agent credentials</sub>
- `2026-11-20` [Amazon: a China-nexus actor's Cairn AI agents found and exploited a MONAI Label zero-day](2026-11-20-cairn-agents-monai-label-zero-day.md)<br>  <sub>Another November report in which the attacker's tooling is the Cairn framework</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-17-microsoft-agent-framework-pypi-hijack.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
