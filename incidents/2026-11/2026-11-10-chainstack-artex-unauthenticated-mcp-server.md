---
id: 2026-11-10-chainstack-artex-unauthenticated-mcp-server
title: "Chainstack: an ARTEX-driven intrusion used an unauthenticated internal MCP tool server with cluster-admin rights to reach production"
title_zh: "Chainstack：ARTEX 驱动的入侵借一台未设认证、拥有集群管理员权限的内部 MCP 工具服务器打进生产环境"
title_ja: "Chainstack：ARTEXによる侵入が、認証なしでクラスタ管理者権限を持つ社内MCPツールサーバーを足がかりに本番環境へ到達"
title_ko: "Chainstack: ARTEX 기반 침입이 인증 없이 클러스터 관리자 권한을 가진 내부 MCP 도구 서버를 발판으로 운영 환경에 도달"
title_de: "Chainstack: Ein ARTEX-gestützter Angriff nutzte einen internen MCP-Tool-Server ohne Authentifizierung mit Cluster-Admin-Rechten, um die Produktion zu erreichen"
title_fr: "Chainstack : une intrusion pilotée par ARTEX s'est servie d'un serveur d'outils MCP interne sans authentification, doté des droits cluster-admin, pour atteindre la production"
title_es: "Chainstack: una intrusión impulsada por ARTEX usó un servidor interno de herramientas MCP sin autenticación y con permisos de cluster-admin para llegar a producción"
date: 2026-11-10
date_raw: "2026-11-10 (Chainstack adds technical details to its incident report first published 2026-11-03; intrusion ran 2026-10-26 to 2026-10-31, last use of a copied credential 2026-11-02)"
date_precision: day

kind: incident
type: [WEAPON, MCP, CRED, EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 10 November 2026 the blockchain-infrastructure provider Chainstack added technical details to the incident report it first published on 3 November, describing an intrusion that it assesses with high confidence was carried out with ARTEX, an open-source framework that orchestrates LLM agents to automate intrusions.** The attacker entered on 26 October through an internet-exposed test Grafana instance in a development Kubernetes cluster that still had its default administrator credentials, and used Grafana's data-source proxy to reach internal services. One of those was an internal MCP tool server that exposes Kubernetes operations to AI agents: it required no authentication and ran with a service account bound to cluster-admin, and Chainstack says it served as the attacker's command executor. From development the attacker obtained machine credentials that also reached production, on 29 October listed and read secrets in a production cluster, and on 31 October read secrets in bulk from the production cloud secrets manager, used a compromised VPN key to join the database network and queried production databases. A database containing customer account information was accessed: organisation names, account-holder names, member email addresses and password hashes may have been exposed, and systems holding node credentials were reachable, so customers were asked to change passwords and rotate node credentials and API keys. Chainstack detected the intrusion on 31 October and cut the access paths that day. It found no evidence that a software vulnerability was exploited: the chain was default credentials, exposed administrative functionality, missing authentication, over-broad permissions and long-lived credentials. Chainstack attributes the tooling, not the actor.

summary_zh: |
  **2026 年 11 月 10 日，区块链基础设施服务商 Chainstack 为其 11 月 3 日首发的事件报告补充了技术细节，描述了一起入侵；它以高置信度判断攻击者用的是 ARTEX，一款编排 LLM agent、把入侵自动化的开源框架。** 攻击者 10 月 26 日从开发 Kubernetes 集群里一个暴露在公网、仍是默认管理员口令的测试 Grafana 实例进入，再借 Grafana 的数据源代理访问内部服务。其中一个是内部的 MCP 工具服务器，它把 Kubernetes 操作开放给 AI agent 使用：不需要任何认证，且以绑定了 cluster-admin 的服务账号运行；Chainstack 说它成了攻击者的命令执行器。攻击者在开发环境拿到了同样能通到生产的机器凭据，10 月 29 日列出并读取了一个生产集群的 secrets，10 月 31 日又从生产云密钥管理服务里批量读取 secrets，用一把被盗的 VPN 密钥接入数据库网络，并查询了生产数据库。一个存有客户账户信息的数据库被访问：机构名称、账户持有人姓名、成员邮箱和密码哈希可能已泄露；存放节点凭据的系统也在其可达范围内，因此 Chainstack 要求客户修改密码、轮换节点凭据和 API 密钥。Chainstack 于 10 月 31 日发现入侵并在当天切断了访问路径。它没有发现任何软件漏洞被利用的证据：整条链靠的是默认口令、暴露的管理功能、缺失的认证、过宽的权限和长期有效的凭据。Chainstack 归因的是工具，不是攻击者身份。

summary_ja: |
  **2026年11月10日、ブロックチェーン基盤プロバイダーのChainstackは、11月3日に初めて公開したインシデント報告に技術的詳細を追加し、LLMエージェントを統率して侵入を自動化するオープンソースのフレームワークARTEXが使われたと高い確度で評価する侵入について説明した。** 攻撃者は10月26日、開発用Kubernetesクラスタ内でインターネットに公開され、既定の管理者認証情報のままだったテスト用Grafanaインスタンスから侵入し、Grafanaのデータソースプロキシを使って内部サービスに到達した。その一つが、Kubernetes操作をAIエージェントに公開する社内MCPツールサーバーだった。認証を必要とせず、cluster-adminに紐づくサービスアカウントで動いており、Chainstackによれば攻撃者のコマンド実行役になった。攻撃者は開発環境から本番にも届くマシン認証情報を入手し、10月29日に本番クラスタのシークレットを一覧・読み取り、10月31日には本番のクラウドシークレットマネージャーからシークレットを一括で読み取り、侵害したVPN鍵でデータベースネットワークに接続して本番データベースに問い合わせた。顧客アカウント情報を含むデータベースがアクセスされ、組織名、アカウント保有者名、メンバーのメールアドレス、パスワードハッシュが漏えいした可能性があり、ノード認証情報を保持するシステムにも到達可能だったため、顧客にはパスワードの変更とノード認証情報・APIキーのローテーションが求められた。Chainstackは10月31日に侵入を検知し、同日中にアクセス経路を遮断した。ソフトウェアの脆弱性が悪用された証拠は見つかっておらず、連鎖したのは既定の認証情報、公開された管理機能、認証の欠如、過剰な権限、長期間有効な認証情報だった。Chainstackはツールを特定したのであり、行為者を特定したのではない。

summary_ko: |
  **2026년 11월 10일, 블록체인 인프라 제공업체 Chainstack은 11월 3일 처음 공개한 사고 보고서에 기술적 세부 사항을 추가해, LLM 에이전트를 조율해 침입을 자동화하는 오픈소스 프레임워크 ARTEX가 사용된 것으로 높은 신뢰도로 평가하는 침입을 설명했다.** 공격자는 10월 26일 개발용 Kubernetes 클러스터에서 인터넷에 노출된 채 기본 관리자 자격 증명이 그대로였던 테스트용 Grafana 인스턴스로 들어와, Grafana의 데이터 소스 프록시를 이용해 내부 서비스에 접근했다. 그중 하나가 Kubernetes 작업을 AI 에이전트에 제공하는 내부 MCP 도구 서버였다. 인증이 필요 없었고 cluster-admin에 바인딩된 서비스 계정으로 실행됐으며, Chainstack은 이것이 공격자의 명령 실행기 역할을 했다고 밝혔다. 공격자는 개발 환경에서 운영 환경에도 닿는 머신 자격 증명을 얻어 10월 29일 운영 클러스터의 시크릿을 나열하고 읽었으며, 10월 31일에는 운영 클라우드 시크릿 매니저에서 시크릿을 대량으로 읽고, 탈취한 VPN 키로 데이터베이스 네트워크에 접속해 운영 데이터베이스를 조회했다. 고객 계정 정보가 담긴 데이터베이스가 접근됐고, 조직명과 계정 보유자 이름, 구성원 이메일 주소, 비밀번호 해시가 노출됐을 수 있으며, 노드 자격 증명을 보관하는 시스템도 접근 가능한 범위에 있었기에 고객에게 비밀번호 변경과 노드 자격 증명 및 API 키 교체를 요청했다. Chainstack은 10월 31일 침입을 탐지해 같은 날 접근 경로를 차단했다. 소프트웨어 취약점이 악용된 증거는 찾지 못했으며, 공격은 기본 자격 증명, 노출된 관리 기능, 인증 부재, 과도한 권한, 장기 자격 증명을 연결한 것이었다. Chainstack은 행위자가 아니라 도구를 특정했다.

summary_de: |
  **Am 10. November 2026 ergänzte der Blockchain-Infrastrukturanbieter Chainstack seinen erstmals am 3. November veröffentlichten Vorfallsbericht um technische Details und beschrieb einen Angriff, der nach seiner Einschätzung mit hoher Sicherheit mit ARTEX durchgeführt wurde, einem quelloffenen Framework, das LLM-Agenten orchestriert, um Einbrüche zu automatisieren.** Der Angreifer kam am 26. Oktober über eine aus dem Internet erreichbare Test-Grafana-Instanz in einem Entwicklungs-Kubernetes-Cluster herein, die noch die voreingestellten Administrator-Zugangsdaten hatte, und nutzte Grafanas Data-Source-Proxy, um interne Dienste zu erreichen. Einer davon war ein interner MCP-Tool-Server, der Kubernetes-Operationen für KI-Agenten bereitstellt: Er verlangte keine Authentifizierung und lief mit einem an cluster-admin gebundenen Service-Account; laut Chainstack diente er dem Angreifer als Befehlsausführer. In der Entwicklungsumgebung erlangte der Angreifer Maschinen-Zugangsdaten, die auch in die Produktion reichten, listete und las am 29. Oktober Secrets in einem Produktionscluster, las am 31. Oktober massenhaft Secrets aus dem produktiven Cloud-Secrets-Manager, verband sich mit einem kompromittierten VPN-Schlüssel mit dem Datenbanknetz und fragte Produktionsdatenbanken ab. Auf eine Datenbank mit Kundenkontoinformationen wurde zugegriffen: Organisationsnamen, Namen der Kontoinhaber, E-Mail-Adressen von Mitgliedern und Passwort-Hashes könnten offengelegt worden sein, und Systeme mit Node-Zugangsdaten waren erreichbar; Kunden wurden daher gebeten, Passwörter zu ändern sowie Node-Zugangsdaten und API-Schlüssel zu rotieren. Chainstack entdeckte den Angriff am 31. Oktober und kappte die Zugangswege am selben Tag. Es fand keine Hinweise auf eine ausgenutzte Software-Schwachstelle: Die Kette bestand aus Standard-Zugangsdaten, exponierten Verwaltungsfunktionen, fehlender Authentifizierung, zu weit gefassten Berechtigungen und langlebigen Zugangsdaten. Chainstack ordnet das Werkzeug zu, nicht den Akteur.

summary_fr: |
  **Le 10 novembre 2026, le fournisseur d'infrastructure blockchain Chainstack a ajouté des détails techniques au rapport d'incident qu'il avait publié le 3 novembre, décrivant une intrusion qu'il estime, avec un degré de confiance élevé, avoir été menée avec ARTEX, un cadre open source qui orchestre des agents LLM pour automatiser les intrusions.** L'attaquant est entré le 26 octobre par une instance Grafana de test exposée sur Internet dans un cluster Kubernetes de développement, qui conservait ses identifiants administrateur par défaut, et a utilisé le proxy de sources de données de Grafana pour atteindre des services internes. L'un d'eux était un serveur d'outils MCP interne qui expose des opérations Kubernetes aux agents IA : il n'exigeait aucune authentification et tournait avec un compte de service lié à cluster-admin ; selon Chainstack, il a servi d'exécuteur de commandes à l'attaquant. Depuis le développement, l'attaquant a obtenu des identifiants machine qui donnaient aussi accès à la production, a listé et lu le 29 octobre les secrets d'un cluster de production, puis, le 31 octobre, a lu en masse les secrets du gestionnaire de secrets cloud de production, utilisé une clé VPN compromise pour rejoindre le réseau des bases de données et interrogé des bases de production. Une base contenant des informations de comptes clients a été consultée : les noms d'organisations, les noms des titulaires de comptes, les adresses e-mail des membres et les hachages de mots de passe ont pu être exposés, et des systèmes détenant des identifiants de nœuds étaient accessibles ; les clients ont donc été invités à changer leurs mots de passe et à renouveler identifiants de nœuds et clés d'API. Chainstack a détecté l'intrusion le 31 octobre et coupé les accès le jour même. Il n'a trouvé aucune preuve de l'exploitation d'une vulnérabilité logicielle : la chaîne reposait sur des identifiants par défaut, des fonctions d'administration exposées, l'absence d'authentification, des permissions trop larges et des identifiants à longue durée de vie. Chainstack attribue l'outillage, pas l'acteur.

summary_es: |
  **El 10 de noviembre de 2026, el proveedor de infraestructura blockchain Chainstack añadió detalles técnicos al informe de incidente que había publicado por primera vez el 3 de noviembre, describiendo una intrusión que, según evalúa con confianza alta, se llevó a cabo con ARTEX, un marco de código abierto que orquesta agentes LLM para automatizar intrusiones.** El atacante entró el 26 de octubre por una instancia de Grafana de pruebas expuesta a Internet en un clúster de Kubernetes de desarrollo, que conservaba sus credenciales de administrador por defecto, y usó el proxy de fuentes de datos de Grafana para llegar a servicios internos. Uno de ellos era un servidor interno de herramientas MCP que expone operaciones de Kubernetes a agentes de IA: no exigía autenticación y se ejecutaba con una cuenta de servicio ligada a cluster-admin; según Chainstack, sirvió de ejecutor de comandos del atacante. Desde desarrollo, el atacante obtuvo credenciales de máquina que también alcanzaban producción, el 29 de octubre listó y leyó secretos de un clúster de producción y, el 31 de octubre, leyó secretos en masa del gestor de secretos en la nube de producción, usó una clave VPN comprometida para unirse a la red de bases de datos y consultó bases de datos de producción. Se accedió a una base de datos con información de cuentas de clientes: nombres de organizaciones, nombres de titulares, direcciones de correo de los miembros y hashes de contraseñas pudieron quedar expuestos, y los sistemas que guardan credenciales de nodos estaban al alcance, por lo que se pidió a los clientes cambiar contraseñas y rotar credenciales de nodos y claves de API. Chainstack detectó la intrusión el 31 de octubre y cortó las vías de acceso ese mismo día. No halló indicios de que se explotara una vulnerabilidad de software: la cadena fueron credenciales por defecto, funciones administrativas expuestas, falta de autenticación, permisos demasiado amplios y credenciales de larga duración. Chainstack atribuye las herramientas, no al actor.

sources:
  - url: https://chainstack.com/security-incident-nov-2026/
    label: Chainstack incident report (created 2026-11-03, technical details added 2026-11-10)
  - url: https://www.govinfosecurity.com/cryptohack-roundup-chainstack-luxors-ai-breaches-a-33445
    label: GovInfoSecurity
  - url: https://econotimes.com/Chainstack-Breach-May-Have-Exposed-Customer-Account-Data-1776115
    label: EconoTimes
  - url: https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks
    label: Wiz Research (lists Chainstack among the campaign's victims)
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# Chainstack: an ARTEX-driven intrusion used an unauthenticated internal MCP tool server with cluster-admin rights to reach production

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**On 10 November 2026 the blockchain-infrastructure provider Chainstack added technical details to the incident report it first published on 3 November, describing an intrusion that it assesses with high confidence was carried out with ARTEX, an open-source framework that orchestrates LLM agents to automate intrusions.** The attacker entered on 26 October through an internet-exposed test Grafana instance in a development Kubernetes cluster that still had its default administrator credentials, and used Grafana's data-source proxy to reach internal services. One of those was an internal MCP tool server that exposes Kubernetes operations to AI agents: it required no authentication and ran with a service account bound to cluster-admin, and Chainstack says it served as the attacker's command executor. From development the attacker obtained machine credentials that also reached production, on 29 October listed and read secrets in a production cluster, and on 31 October read secrets in bulk from the production cloud secrets manager, used a compromised VPN key to join the database network and queried production databases. A database containing customer account information was accessed: organisation names, account-holder names, member email addresses and password hashes may have been exposed, and systems holding node credentials were reachable, so customers were asked to change passwords and rotate node credentials and API keys. Chainstack detected the intrusion on 31 October and cut the access paths that day. It found no evidence that a software vulnerability was exploited: the chain was default credentials, exposed administrative functionality, missing authentication, over-broad permissions and long-lived credentials. Chainstack attributes the tooling, not the actor.

## Attack chain

```mermaid
flowchart LR
    A["Exposed test Grafana with default<br/>admin credentials; its data-source<br/>proxy reaches internal services"]:::entry
    B["Unauthenticated internal MCP tool<br/>server with cluster-admin becomes<br/>the attacker's command executor"]:::step
    C["Automation workflow hijacked;<br/>machine identities from development<br/>also reach production"]:::step
    D["Production secrets read in bulk;<br/>customer account database queried;<br/>node credentials treated as exposed"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**Initial access.** A test Grafana instance had been deployed to a development Kubernetes cluster in July 2026. It was reachable from the internet with no single sign-on or basic authentication in front of it, and its default administrator credentials had never been changed. From 19:26 UTC on 26 October the attacker logged in, created data sources pointing at internal addresses and used Grafana's data-source proxy as a pivot, connecting over about two hours to dozens of internal services including identity, database, automation and monitoring endpoints. The proxy had no destination allowlist and no network policy limited where Grafana could connect.

**The MCP tool server.** At 21:01 the attacker reached an internal MCP tool server that exposes Kubernetes operations to AI agents. It required no authentication and ran with a service account bound to cluster-admin. Chainstack says network flows, those permissions and the changes that followed indicate it served as the attacker's command executor; the individual tool calls could not be recovered. Over the next hour and a half the attacker tested write access to an internal workflow engine, created administrator users in the development identity provider, and replaced the JavaScript served by a development web application by mounting attacker-supplied files over the originals through ConfigMap volumes. The same technique was applied to the staging web application and the development Grafana on 27 October; the injected loader referenced a second-stage script that Chainstack did not retrieve.

**From development to production.** On 29 October the attacker rewrote a workflow in the workflow-automation platform directly in its database so that it ran shell commands, triggered it with a valid webhook token and restored the original. The run returned the automation pod's environment, its Kubernetes service-account token and a machine identity for the infrastructure access gateway. That identity and a second one belonging to deployment automation were then used to list the secrets of a production Kubernetes cluster and read several, including cloud and infrastructure credentials. On 31 October, with a key for the cloud service account of the infrastructure-as-code automation, the attacker read secrets in bulk from the production cloud secrets manager between 01:40 and 08:31, created further keys and a Kubernetes service account as an independent way back in, ran short-lived and privileged pods in production and registered rogue instances with the access gateway.

**Database access and detection.** The secrets included the private key of a VPN peer on the database network. When the attacker used it, two clients presented the same peer identity, the tunnel endpoint flapped between them and a database replication pipeline failed; that failure started the investigation. From about 07:30 the attacker connected to a production database as an administrative user from attacker-created pods and exfiltrated query results through pod command output in base64 chunks, and queried the view that holds role password hashes on one instance. Separately the attacker used a BI tool's API key to run SQL queries and read stored connection details. Chainstack cut the access paths on 31 October; some copied credentials for external services kept working until rotated, with the last observed use at 06:28 on 2 November.

**What was exposed.** A database containing customer account information: organisation names, account-holder names, the email addresses of organisation members and password hashes may have been exposed. Systems holding node credentials were accessible; Chainstack has no evidence they were read but treats them as exposed. Customer nodes, the console and the API were not modified, and payment-card details are not stored. Customers were asked to change passwords, rotate node credentials, regenerate platform API keys and watch for phishing.

**Why Chainstack names ARTEX.** Attacker-created resources consistently carried `artx` / `artex` prefixes, often with numeric suffixes, in workflow names, identities, pods, service accounts, a systemd timer and DNS proof records. Chainstack assesses with high confidence that the attacker used ARTEX and says the conclusion concerns the tooling: none of its indicators appear among the actor-specific indicators published for the named groups known to use the framework, so it attributes the tooling, not the actor. It also says its findings indicate the incident was part of a broader AI-powered campaign reported in late October. No outside party has independently verified the account; GovInfoSecurity and EconoTimes report from Chainstack's page, and Wiz lists Chainstack's default-credential Grafana among that campaign's entry points.

**How it is graded.** `incident`: a breach confirmed by the affected company with customer data accessed. `WEAPON` because an agent framework was the attacker's tool; `MCP` because the pivotal step was an unauthenticated MCP tool server carrying cluster-admin rights; `CRED` because the intrusion advanced by harvesting machine identities, keys and secrets; `EXFIL` because database query results left the environment. `high`: production secrets read in bulk and customer account data accessed at an infrastructure provider, with no evidence of customer-facing services being altered.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Chainstack incident report (created 2026-11-03, technical details added 2026-11-10) | <https://chainstack.com/security-incident-nov-2026/> |
| 2 | GovInfoSecurity | <https://www.govinfosecurity.com/cryptohack-roundup-chainstack-luxors-ai-breaches-a-33445> |
| 3 | EconoTimes | <https://econotimes.com/Chainstack-Breach-May-Have-Exposed-Customer-Account-Data-1776115> |
| 4 | Wiz Research (lists Chainstack among the campaign's victims) | <https://www.wiz.io/blog/agentic-attacks-artex-offensive-ai-frameworks> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-10` (raw: 2026-11-10 (Chainstack adds technical details to its incident report first published 2026-11-03; intrusion ran 2026-10-26 to 2026-10-31, last use of a copied credential 2026-11-02), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`MCP`](../../taxonomy/types.md#mcp) [`CRED`](../../taxonomy/types.md#cred) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — Chainstack's own incident report with a detailed technical timeline and indicators; GovInfoSecurity and EconoTimes report from it; Wiz lists it among the campaign's victims |
| Real harm | Yes — a customer account database queried; production secrets read in bulk; node credentials treated as exposed and rotated |
| AI involvement | Confirmed `confirmed` — Chainstack assesses with high confidence that ARTEX was used, from `artx` / `artex` markers across the attacker's artifacts; this is its own assessment of tooling, not actor |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-11-10-chainstack-artex-unauthenticated-mcp-server` |

<sub>**Why this classification:** A breach confirmed by the affected company in which an agent framework was the attacker's tooling (`WEAPON`), the pivotal step was an unauthenticated MCP tool server with cluster-admin rights (`MCP`), the intrusion advanced by harvesting identities and secrets (`CRED`) and database results were taken out (`EXFIL`), hence `incident` and `real_harm: true`. `high`: production secrets and customer account data at an infrastructure provider, with customer-facing services unaltered. `confidence: A` for a first-hand report with a technical timeline; the ARTEX finding is the company's own high-confidence assessment and is recorded as such. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md) · [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-11-07` [German host Mittwald breached through a shell-injection flaw in its own MCP server](2026-11-07-mittwald-mcp-server-breach.md)<br>  <sub>The same weeks: another provider whose own MCP server was the way in</sub>
- `2026-10-30` [Black October: a coordinated wave breached at least nine AI developer platforms](../2026-10/2026-10-30-black-october-ai-developer-platform-breaches.md)<br>  <sub>The late-October campaign Chainstack says its incident belongs to</sub>
- `2026-11-06` [WorkOS traces a customer-data breach to a security researcher's escaped ARTEX AI agent](2026-11-06-workos-escaped-artex-agent-breach.md)<br>  <sub>Another company that identified ARTEX from markers in its own logs, in the same week</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-10-chainstack-artex-unauthenticated-mcp-server.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
