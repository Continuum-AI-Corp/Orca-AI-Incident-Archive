---
id: 2026-11-11-barracuda-artex-stale-ai-vendor-key
title: "Barracuda: an ARTEX-matched intrusion crossed about 10 cloud accounts in 44 hours through a stale key left with an AI vendor"
title_zh: "Barracuda：一起与 ARTEX 特征吻合的入侵，靠留在某 AI 供应商处的过期未回收密钥，44 小时内横穿约 10 个云账号"
title_ja: "Barracuda：ARTEXと一致する侵入が、AIベンダーに預けたまま失効させていなかった鍵を使い、44時間で約10のクラウドアカウントを横断"
title_ko: "Barracuda: ARTEX와 일치하는 침입이 AI 공급업체에 남겨 둔 채 폐기하지 않은 키로 44시간 동안 약 10개 클라우드 계정을 넘나듦"
title_de: "Barracuda: Ein zu ARTEX passender Angriff durchquerte in 44 Stunden rund 10 Cloud-Konten über einen nie zurückgezogenen Schlüssel bei einem KI-Dienstleister"
title_fr: "Barracuda : une intrusion correspondant à ARTEX a traversé une dizaine de comptes cloud en 44 heures grâce à une clé jamais révoquée laissée chez un prestataire d'IA"
title_es: "Barracuda: una intrusión que coincide con ARTEX atravesó unas 10 cuentas en la nube en 44 horas mediante una clave sin retirar que seguía en manos de un proveedor de IA"
date: 2026-11-11
date_raw: "2026-11-11 (Barracuda blog post; Trust Center advisory 2026-11-10; intrusion ran 2026-11-01 04:33 UTC to 2026-11-02 23:31 UTC, detected 2026-11-04)"
date_precision: day

kind: incident
type: [WEAPON, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  **On 11 November 2026 the security vendor Barracuda published an account of an intrusion into parts of its cloud environment, saying the attacker's probe names, indicators, working order and built-in routines for hunting credentials and wallets all match ARTEX, an open-source AI-driven penetration-testing framework.** The attacker did not exploit a vulnerability: it used a valid cloud access key that Barracuda had given a third-party vendor, a company working in AI, for an earlier project and never retired. The vendor's own development environment was compromised in October, which appears to be where the key was found. The first call with the key came at 04:33 UTC on 1 November; over the next 24 hours the attacker used each secret it found to reach the next system, from cloud accounts to a data-analytics system, to a source-code access token, to Kubernetes clusters. Early on 2 November it pushed short-lived branches to a handful of repositories to trigger a build workflow written to print the build system's secrets into the job log, encoded to defeat log masking. The last recorded activity was at 23:31 UTC on 2 November: about 10 cloud accounts in roughly 44 hours. It deployed a container that mounted a server's file system to harvest credentials and tried to create a new administrative cloud identity, which was blocked. An engineer noticed unusual activity on 4 November, by which time the attacker had finished. One system it reached stores the credentials Barracuda XDR uses to collect data from customers' systems; Barracuda found no direct evidence they were viewed but could not rule it out and asked potentially affected customers to recreate them. Barracuda attributes how the attacker operated, not who it was.

summary_zh: |
  **2026 年 11 月 11 日，安全厂商 Barracuda 公布了自家部分云环境被入侵的经过，称攻击者的探测名称、各项指标、行动顺序以及内置的凭据和钱包搜寻例程全都与 ARTEX 吻合。ARTEX 是一款开源的 AI 驱动渗透测试框架。** 攻击者没有利用漏洞：它用的是一把有效的云访问密钥，这把密钥是 Barracuda 以前为某个项目交给一家第三方供应商（一家做 AI 的公司）的，项目结束后一直没有回收。该供应商自己的开发环境在 10 月被攻陷，密钥看来就是在那里被找到的。11 月 1 日 04:33（UTC），攻击者用这把密钥发出第一次调用；之后 24 小时里，它每找到一个密钥就拿去打开下一个系统：从云账号到一个数据分析系统，再到一个源码访问令牌，再到 Kubernetes 集群。11 月 2 日凌晨，它向少数几个仓库推送短命分支，触发一个专门把构建系统密钥打印到任务日志里的构建工作流，并对密钥做了编码以绕过日志脱敏。最后一次有记录的活动是 11 月 2 日 23:31（UTC）：约 44 小时内碰了约 10 个云账号。它还部署了一个挂载宿主机文件系统的容器来收割凭据，并试图给自己新建一个云管理员身份，这一步被拦下。11 月 4 日，一名工程师注意到异常活动，此时攻击者早已收工。它触及的系统之一存放着 Barracuda XDR 用来从客户系统采集数据的凭据；Barracuda 没有发现这些凭据被查看的直接证据，但也无法排除，于是请可能受影响的客户重建凭据。Barracuda 归因的是攻击者的作业方式，不是其身份。

summary_ja: |
  **2026年11月11日、セキュリティベンダーのBarracudaは、自社クラウド環境の一部への侵入の経緯を公表し、攻撃者のプローブ名、各種指標、作業の順序、認証情報とウォレットを探す組み込みルーチンのすべてが、オープンソースのAI駆動ペネトレーションテスト・フレームワークARTEXと一致すると述べた。** 攻撃者は脆弱性を突いたのではない。Barracudaが以前のプロジェクトのために第三者のベンダー（AI関連企業）に渡し、その後失効させていなかった有効なクラウドアクセスキーを使った。このベンダー自身の開発環境が10月に侵害されており、鍵はそこで見つかったとみられる。鍵を使った最初の呼び出しは11月1日04:33 UTCで、その後24時間、攻撃者は見つけたシークレットを次のシステムへの足がかりにし、クラウドアカウントからデータ分析システムへ、ソースコードのアクセストークンへ、Kubernetesクラスタへと進んだ。11月2日未明には少数のリポジトリに短命のブランチをプッシュし、ビルドシステムのシークレットをジョブログに出力するよう書かれたビルドワークフローを起動した。シークレットはログのマスキングを回避するよう符号化されていた。記録された最後の活動は11月2日23:31 UTCで、およそ44時間で約10のクラウドアカウントに触れたことになる。攻撃者はサーバーのファイルシステムをマウントするコンテナを配備して認証情報を収集し、新しい管理者クラウドIDの作成も試みたが、これは阻止された。11月4日にエンジニアが異常な活動に気づいたとき、攻撃者はすでに作業を終えていた。到達されたシステムの一つは、Barracuda XDRが顧客のシステムからデータを収集するための認証情報を保管している。Barracudaはそれらが閲覧された直接の証拠は見つけていないが否定もできず、影響を受けた可能性のある顧客に再作成を求めた。Barracudaが特定したのは攻撃者の手口であり、誰であるかではない。

summary_ko: |
  **2026년 11월 11일, 보안 업체 Barracuda는 자사 클라우드 환경 일부에 대한 침입 경위를 공개하며, 공격자의 프로브 이름과 지표, 작업 순서, 자격 증명과 지갑을 찾는 내장 루틴이 모두 오픈소스 AI 기반 침투 테스트 프레임워크 ARTEX와 일치한다고 밝혔다.** 공격자는 취약점을 악용하지 않았다. Barracuda가 이전 프로젝트를 위해 제3자 공급업체(AI 분야 기업)에 제공하고 이후 폐기하지 않은 유효한 클라우드 액세스 키를 사용했다. 이 공급업체의 개발 환경이 10월에 침해됐고, 키는 그곳에서 발견된 것으로 보인다. 키를 이용한 첫 호출은 11월 1일 04:33 UTC였고, 이후 24시간 동안 공격자는 찾아낸 시크릿을 다음 시스템으로 가는 발판으로 삼아 클라우드 계정에서 데이터 분석 시스템으로, 소스 코드 액세스 토큰으로, Kubernetes 클러스터로 이동했다. 11월 2일 이른 시간에는 몇몇 저장소에 단명 브랜치를 푸시해, 빌드 시스템의 시크릿을 작업 로그에 출력하도록 작성된 빌드 워크플로를 실행시켰다. 시크릿은 로그 마스킹을 피하도록 인코딩돼 있었다. 마지막으로 기록된 활동은 11월 2일 23:31 UTC로, 약 44시간 동안 약 10개 클라우드 계정을 건드린 셈이다. 공격자는 서버의 파일 시스템을 마운트하는 컨테이너를 배포해 자격 증명을 수집했고 새 관리자 클라우드 ID 생성도 시도했으나 차단됐다. 11월 4일 한 엔지니어가 이상 활동을 알아챘을 때 공격자는 이미 작업을 끝낸 뒤였다. 공격자가 도달한 시스템 중 하나에는 Barracuda XDR이 고객 시스템에서 데이터를 수집하는 데 쓰는 자격 증명이 저장돼 있다. Barracuda는 그것이 열람됐다는 직접 증거를 찾지 못했지만 배제할 수도 없어, 영향을 받았을 수 있는 고객에게 재생성을 요청했다. Barracuda가 특정한 것은 공격자의 작업 방식이지 정체가 아니다.

summary_de: |
  **Am 11. November 2026 veröffentlichte der Sicherheitsanbieter Barracuda einen Bericht über einen Einbruch in Teile seiner Cloud-Umgebung und erklärte, die Probe-Namen des Angreifers, die Indikatoren, die Arbeitsreihenfolge und die eingebauten Routinen zur Suche nach Zugangsdaten und Wallets passten sämtlich zu ARTEX, einem quelloffenen KI-gesteuerten Penetrationstest-Framework.** Der Angreifer nutzte keine Schwachstelle aus: Er verwendete einen gültigen Cloud-Zugriffsschlüssel, den Barracuda einem Drittanbieter, einem im KI-Bereich tätigen Unternehmen, für ein früheres Projekt gegeben und nie zurückgezogen hatte. Die Entwicklungsumgebung dieses Anbieters wurde im Oktober kompromittiert; dort wurde der Schlüssel offenbar gefunden. Der erste Aufruf mit dem Schlüssel erfolgte am 1. November um 04:33 UTC; in den folgenden 24 Stunden nutzte der Angreifer jedes gefundene Geheimnis, um das nächste System zu erreichen: von Cloud-Konten zu einem Datenanalysesystem, zu einem Quellcode-Zugriffstoken, zu Kubernetes-Clustern. Früh am 2. November schob er kurzlebige Branches in einige Repositories, um einen Build-Workflow auszulösen, der die Geheimnisse des Build-Systems ins Job-Log schrieb, kodiert, um die Log-Maskierung zu umgehen. Die letzte aufgezeichnete Aktivität war am 2. November um 23:31 UTC: rund 10 Cloud-Konten in etwa 44 Stunden. Er setzte einen Container ein, der das Dateisystem eines Servers einband, um Zugangsdaten zu sammeln, und versuchte, eine neue administrative Cloud-Identität anzulegen, was blockiert wurde. Ein Ingenieur bemerkte am 4. November ungewöhnliche Aktivität; da war der Angreifer bereits fertig. Eines der erreichten Systeme speichert die Zugangsdaten, mit denen Barracuda XDR Daten aus Kundensystemen einsammelt; Barracuda fand keine direkten Belege für einen Zugriff darauf, konnte ihn aber nicht ausschließen und bat möglicherweise betroffene Kunden, sie neu zu erstellen. Barracuda ordnet zu, wie der Angreifer vorging, nicht wer er war.

summary_fr: |
  **Le 11 novembre 2026, l'éditeur de sécurité Barracuda a publié le récit d'une intrusion dans une partie de son environnement cloud, indiquant que les noms de sondes de l'attaquant, les indicateurs, l'ordre de travail et les routines intégrées de recherche d'identifiants et de portefeuilles correspondent tous à ARTEX, un cadre open source de tests d'intrusion piloté par IA.** L'attaquant n'a pas exploité de vulnérabilité : il a utilisé une clé d'accès cloud valide que Barracuda avait remise à un prestataire tiers, une entreprise du secteur de l'IA, pour un projet antérieur et n'avait jamais révoquée. L'environnement de développement de ce prestataire a été compromis en octobre ; c'est apparemment là que la clé a été trouvée. Le premier appel avec la clé a eu lieu le 1er novembre à 04 h 33 UTC ; durant les 24 heures suivantes, l'attaquant s'est servi de chaque secret trouvé pour atteindre le système suivant : des comptes cloud à un système d'analyse de données, puis à un jeton d'accès au code source, puis à des clusters Kubernetes. Tôt le 2 novembre, il a poussé des branches éphémères vers quelques dépôts pour déclencher un workflow de build écrit pour afficher les secrets du système de build dans le journal de la tâche, encodés pour déjouer le masquage des journaux. La dernière activité enregistrée date du 2 novembre à 23 h 31 UTC : une dizaine de comptes cloud en 44 heures environ. Il a déployé un conteneur montant le système de fichiers d'un serveur pour récolter des identifiants et a tenté de créer une nouvelle identité cloud d'administration, tentative bloquée. Un ingénieur a remarqué une activité inhabituelle le 4 novembre ; l'attaquant avait alors terminé. L'un des systèmes atteints stocke les identifiants que Barracuda XDR utilise pour collecter des données dans les systèmes des clients ; Barracuda n'a trouvé aucune preuve directe de leur consultation mais n'a pas pu l'exclure et a demandé aux clients potentiellement concernés de les recréer. Barracuda attribue la manière d'opérer de l'attaquant, pas son identité.

summary_es: |
  **El 11 de noviembre de 2026, el proveedor de seguridad Barracuda publicó el relato de una intrusión en partes de su entorno en la nube y afirmó que los nombres de las sondas del atacante, los indicadores, el orden de trabajo y las rutinas integradas de búsqueda de credenciales y monederos coinciden todos con ARTEX, un marco de pruebas de penetración de código abierto impulsado por IA.** El atacante no explotó una vulnerabilidad: usó una clave de acceso a la nube válida que Barracuda había entregado a un proveedor externo, una empresa del sector de la IA, para un proyecto anterior y que nunca retiró. El entorno de desarrollo de ese proveedor fue comprometido en octubre; al parecer fue allí donde se encontró la clave. La primera llamada con la clave se produjo el 1 de noviembre a las 04:33 UTC; durante las 24 horas siguientes el atacante usó cada secreto que encontraba para llegar al siguiente sistema: de las cuentas en la nube a un sistema de analítica de datos, a un token de acceso al código fuente, a clústeres de Kubernetes. A primera hora del 2 de noviembre empujó ramas efímeras a unos pocos repositorios para activar un workflow de compilación escrito para imprimir los secretos del sistema de compilación en el registro del trabajo, codificados para eludir el enmascaramiento del registro. La última actividad registrada fue el 2 de noviembre a las 23:31 UTC: unas 10 cuentas en la nube en aproximadamente 44 horas. Desplegó un contenedor que montaba el sistema de archivos de un servidor para recoger credenciales e intentó crear una nueva identidad administrativa en la nube, intento que fue bloqueado. Un ingeniero advirtió actividad inusual el 4 de noviembre, cuando el atacante ya había terminado. Uno de los sistemas alcanzados almacena las credenciales que Barracuda XDR usa para recopilar datos de los sistemas de los clientes; Barracuda no halló pruebas directas de que se consultaran, pero no pudo descartarlo y pidió a los clientes potencialmente afectados que las recrearan. Barracuda atribuye cómo operó el atacante, no quién era.

sources:
  - url: https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion
    label: Barracuda blog (Arve Kjoelen, CISO): Forty-four hours
  - url: https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/
    label: BleepingComputer
  - url: https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/
    label: SecurityWeek
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# Barracuda: an ARTEX-matched intrusion crossed about 10 cloud accounts in 44 hours through a stale key left with an AI vendor

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 11 November 2026 the security vendor Barracuda published an account of an intrusion into parts of its cloud environment, saying the attacker's probe names, indicators, working order and built-in routines for hunting credentials and wallets all match ARTEX, an open-source AI-driven penetration-testing framework.** The attacker did not exploit a vulnerability: it used a valid cloud access key that Barracuda had given a third-party vendor, a company working in AI, for an earlier project and never retired. The vendor's own development environment was compromised in October, which appears to be where the key was found. The first call with the key came at 04:33 UTC on 1 November; over the next 24 hours the attacker used each secret it found to reach the next system, from cloud accounts to a data-analytics system, to a source-code access token, to Kubernetes clusters. Early on 2 November it pushed short-lived branches to a handful of repositories to trigger a build workflow written to print the build system's secrets into the job log, encoded to defeat log masking. The last recorded activity was at 23:31 UTC on 2 November: about 10 cloud accounts in roughly 44 hours. It deployed a container that mounted a server's file system to harvest credentials and tried to create a new administrative cloud identity, which was blocked. An engineer noticed unusual activity on 4 November, by which time the attacker had finished. One system it reached stores the credentials Barracuda XDR uses to collect data from customers' systems; Barracuda found no direct evidence they were viewed but could not rule it out and asked potentially affected customers to recreate them. Barracuda attributes how the attacker operated, not who it was.

## Attack chain

```mermaid
flowchart LR
    A["A cloud key Barracuda gave an<br/>AI vendor is never retired;<br/>the vendor is breached in October"]:::entry
    B["Attacker uses the valid key and<br/>chains each secret it finds<br/>to the next system"]:::step
    C["Build workflow made to print<br/>secrets; container mounts a<br/>server's file system"]:::step
    D["About 10 cloud accounts in 44 hours;<br/>XDR integration credentials reachable,<br/>customers asked to recreate them"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**How it started.** Barracuda says the attacker did not break in but used a valid cloud access key. As part of a previous project the company had given a cloud access key to a third-party vendor, a company working in AI, and did not retire the key when that work finished; the post says plainly that this is on Barracuda. In October the vendor's own development environment was compromised, and that appears to be where the attacker found the key. The vendor is not named.

**What Barracuda observed.** All times are UTC. On 1 November at 04:33 the attacker made its first call with the key and within minutes was mapping what the key could reach, reading stored secrets such as AWS access keys and Azure service-principal secrets. Over the next 24 hours it used each secret to reach the next system: from cloud accounts to a data-analytics system, from there to a source-code access token, from there to Kubernetes clusters. In just under four hours early on 2 November it pushed short-lived branches to a handful of repositories to trigger a build workflow written to print the build system's secrets into the job log, with the secrets encoded so the log's usual masking would not hide them. The last recorded activity was on 2 November at 23:31. In all the attacker touched about 10 cloud accounts in roughly 44 hours.

**Why Barracuda says ARTEX.** The attacker referred to resources with machine-style labels, the letter i followed by digits. Barracuda says the probe names, the other indicators it collected, the order in which the attacker worked through its systems and its built-in routines for hunting credentials and wallets all match ARTEX, an open-source AI-driven penetration-testing framework released in July 2026 in which a planner agent decides the next step and worker agents run common tools. Because many groups use ARTEX, Barracuda says the match tells it how the attacker operated, not who it was. This identification is Barracuda's own and has not been independently verified.

**What the attacker wanted.** Credentials and secrets everywhere: it read secret stores, decrypted infrastructure-as-code state files, and pulled credentials from server metadata services and Kubernetes service accounts. On servers where it gained shell access its commands searched for environment variables named WALLET, MNEMONIC, SEED and PRIV, Ethereum keystore files, extended private keys and seed-phrase files; no wallet material existed there. Barracuda adds that some of the secrets within reach were credentials for AI services, that the vendor it came through is an AI company, and that it would be naive to rule out AI credentials and compute as part of the prize. It compares the chain to the October intrusion at Railway.

**Persistence, detection and customers.** Using access to a Kubernetes cluster, the attacker deployed a container that mounted the underlying server's file system read-only, enough to harvest that server's credentials, and tried to create a new administrative cloud identity, which was blocked. On 4 November an engineer noticed unusual activity on their own account, and the same day the vendor contacted Barracuda about its own incident. The container was removed that evening and credentials were rotated across every system involved. One system the attacker reached stores the credentials Barracuda XDR uses to collect data from customers' connected systems. Barracuda found no direct evidence they were viewed, but logging there was not detailed enough to rule it out, so it treated every credential in reach as potentially compromised and contacted customers with potentially affected Managed XDR Cloud or Monitored Endpoint integration credentials, asking them to revoke and recreate them.

**How it is graded.** `incident`: an intrusion disclosed by the affected company with a timeline and a customer advisory. `WEAPON` because, on Barracuda's account, an agent framework was the attacker's tool; `CRED` because the whole intrusion ran on a stale key and the secrets harvested from it, and what was put at risk is customer integration credentials. `real_harm: true`: about 10 cloud accounts, source repositories, the build system and Kubernetes clusters were accessed and secrets read. `high`: a security vendor's cloud environment compromised and customer credentials placed in reach, with no evidence that those credentials were used.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Barracuda blog (Arve Kjoelen, CISO): Forty-four hours | <https://blog.barracuda.com/2026/11/11/anatomy-of-a-machine-speed-intrusion> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/barracuda-links-cloud-breach-to-artex-ai-powered-cyberattack/> |
| 3 | SecurityWeek | <https://www.securityweek.com/barracuda-hacked-amid-surge-in-artex-powered-cyberattacks/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-11` (raw: 2026-11-11 (Barracuda blog post; Trust Center advisory 2026-11-10; intrusion ran 2026-11-01 04:33 UTC to 2026-11-02 23:31 UTC, detected 2026-11-04), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — Barracuda's own account by its CISO, with a timeline and a customer advisory; BleepingComputer and SecurityWeek report from it; the vendor is unnamed and the ARTEX match is not independently verified |
| Real harm | Yes — about 10 cloud accounts, source repositories, the build system and Kubernetes clusters accessed and secrets read; customer XDR integration credentials in reach and rotated as a precaution |
| AI involvement | Confirmed `confirmed` — Barracuda says the attacker's probe names, indicators, working order and credential- and wallet-hunting routines all match ARTEX; this is its own identification of tooling, not of the actor |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-11-11-barracuda-artex-stale-ai-vendor-key` |

<sub>**Why this classification:** An intrusion disclosed by the affected company in which, by its own account, an agent framework was the attacker's tooling (`WEAPON`) and every step ran on a stale third-party key and the secrets chained from it (`CRED`), hence `incident` and `real_harm: true`. `high`: a security vendor's cloud environment was crossed in under two days and customer integration credentials were put in reach, with no evidence they were used. `confidence: A` for a first-hand disclosure; the ARTEX identification is Barracuda's own and is recorded as such. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-10-30` [Black October: a coordinated wave breached at least nine AI developer platforms](../2026-10/2026-10-30-black-october-ai-developer-platform-breaches.md)<br>  <sub>The October wave Barracuda's post points to, including the Railway intrusion it compares itself with</sub>
- `2026-11-10` [Chainstack: an ARTEX-driven intrusion reached production through an unauthenticated MCP tool server](2026-11-10-chainstack-artex-unauthenticated-mcp-server.md)<br>  <sub>Another company-disclosed ARTEX intrusion from the same days, also chaining credentials rather than exploiting a flaw</sub>
- `2026-10-21` [Microsoft ties the ConnectWise supply-chain compromise to Storm-0940 driving attacks with ARTEX](../2026-10/2026-10-21-storm-0940-artex-connectwise-supply-chain.md)<br>  <sub>An earlier ARTEX intrusion that also arrived through a supplier relationship</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-11-barracuda-artex-stale-ai-vendor-key.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
