---
id: 2026-11-20-cairn-agents-monai-label-zero-day
title: "Amazon: a China-nexus actor's Cairn AI agents found and exploited a MONAI Label zero-day on their own to root a university server"
title_zh: "Amazon：某中国关联攻击者的 Cairn AI agent 自行发现并利用 MONAI Label 零日漏洞，拿下一所大学服务器的 root"
title_ja: "Amazon：中国関連アクターのCairn AIエージェントがMONAI Labelのゼロデイを自力で発見・悪用し、大学サーバーのroot権限を奪取"
title_ko: "Amazon: 중국 연계 공격자의 Cairn AI 에이전트가 MONAI Label 제로데이를 스스로 찾아 악용해 대학 서버의 root 권한을 탈취"
title_de: "Amazon: Cairn-KI-Agenten eines China-nahen Akteurs fanden und nutzten eigenständig eine Zero-Day-Lücke in MONAI Label und erlangten Root auf einem Universitätsserver"
title_fr: "Amazon : les agents IA Cairn d'un acteur lié à la Chine ont trouvé et exploité seuls une faille zero-day de MONAI Label pour obtenir les droits root sur un serveur universitaire"
title_es: "Amazon: los agentes de IA Cairn de un actor vinculado a China hallaron y explotaron por sí solos un zero-day de MONAI Label y obtuvieron root en un servidor universitario"
date: 2026-11-20
date_raw: "2026-11-20 (Amazon Threat Intelligence post; campaign ran 2026-09-08 to 2026-09-10; MONAI Label advisory GHSA-qc22-rmgc-vg94 published 2026-11-18; CVE-2026-133968 added to CISA KEV 2026-11-23)"
date_precision: day

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [APAC]

summary: |
  **On 20 November 2026, Amazon Threat Intelligence reported that autonomous AI agents run by a China-nexus actor discovered a previously unknown vulnerability in the open-source medical-imaging AI application MONAI Label and used it to take full control of a university server.** Amazon found the operator's Cairn instance (an open-source autonomous AI penetration-testing framework) exposed without authentication on 10 September 2026, with prompts, project configurations and AI output readable by anyone. The campaign ran for about 48 hours from 8 September against IP addresses of universities in East Asia outside mainland China, with goals that were variations of "obtain shell access". Against the MONAI Label server the agents mapped the API, tested an upload endpoint's filename parameter for path traversal and reached arbitrary file write in about 11 minutes; in a later session they wrote a Python reverse shell to `sitecustomize.py`, triggered a training endpoint and got a shell running as root. Amazon assesses with high confidence that the flaw was a zero-day. The operator then gave the agents a proxy into a second university network through a server running the same software, which Amazon infers was compromised with the same flaw. Two other operations failed: about 16 hours and 148 actions against an open Redis server, and more than 30,000 credential combinations against a GPU server. The maintainers published advisory GHSA-qc22-rmgc-vg94 on 18 November (versions up to 0.8.5 affected, 0.8.6 patched); CISA added CVE-2026-133968 to its Known Exploited Vulnerabilities catalog on 23 November. Attribution to a China-nexus actor is Amazon's moderate-confidence assessment; the victims are not named and no data theft is stated.

summary_zh: |
  **2026 年 11 月 20 日，Amazon Threat Intelligence 披露：某中国关联攻击者运行的自主 AI agent 自行发现了开源医学影像 AI 应用 MONAI Label 中一个此前未知的漏洞，并用它完全控制了一所大学的服务器。** Amazon 于 2026 年 9 月 10 日发现该操作者的 Cairn 实例（一款开源自主 AI 渗透测试框架）未设认证、暴露在公网，提示词、项目配置和 AI 输出任何人可读。战役自 9 月 8 日起持续约 48 小时，目标是中国大陆以外东亚地区高校的 IP 地址，下达的目标是“obtain shell access”（拿到 shell）的各种变体。针对 MONAI Label 服务器，agent 先梳理 API，再对上传端点的文件名参数测试路径穿越，约 11 分钟就做到任意文件写入；在之后的一次会话中，它们把 Python 反弹 shell 写进 `sitecustomize.py`，触发训练端点，拿到以 root 运行的 shell。Amazon 以高置信度判断该漏洞为零日。随后操作者给 agent 提供了一个通往第二所大学网络的代理，代理所连的服务器运行同一软件，Amazon 推断它也是被同一漏洞攻陷的。另有两次行动失败：对一台开放的 Redis 服务器用了约 16 小时、148 步操作；对一台 GPU 服务器尝试了 3 万多组凭据。维护者于 11 月 18 日发布公告 GHSA-qc22-rmgc-vg94（影响 0.8.5 及以下版本，0.8.6 修复）；CISA 于 11 月 23 日把 CVE-2026-133968 列入已知被利用漏洞目录。“中国关联”是 Amazon 中等置信度的判断；受害方未具名，也未提到数据被窃。

summary_ja: |
  **2026年11月20日、Amazon Threat Intelligenceは、中国関連アクターが運用する自律型AIエージェントが、オープンソースの医用画像AIアプリケーションMONAI Labelの未知の脆弱性を自ら発見し、それを使って大学サーバーを完全に掌握したと報告した。** Amazonは2026年9月10日、認証なしで公開されていた運用者のCairnインスタンス（オープンソースの自律型AIペネトレーションテスト・フレームワーク）を発見し、プロンプト、プロジェクト設定、AIの出力が誰でも閲覧できる状態だった。キャンペーンは9月8日から約48時間、中国本土以外の東アジアの大学のIPアドレスを標的とし、目標は「obtain shell access」の各種バリエーションだった。MONAI Labelサーバーに対してエージェントはAPIを調べ、アップロード用エンドポイントのファイル名パラメータでパストラバーサルを試し、約11分で任意ファイル書き込みに到達した。後のセッションではPythonのリバースシェルを`sitecustomize.py`に書き込み、学習用エンドポイントを起動してroot権限のシェルを得た。Amazonはこの欠陥がゼロデイだったと高い確度で評価している。その後、運用者は同じソフトウェアが動くサーバー経由で第二の大学ネットワークに入るプロキシをエージェントに与えており、Amazonは同じ欠陥で侵害されたと推定している。他の二つの作戦は失敗した。公開状態のRedisサーバーに対する約16時間・148回の操作と、GPUサーバーに対する3万件超の認証情報の試行である。メンテナーは11月18日にアドバイザリGHSA-qc22-rmgc-vg94を公開し（0.8.5以前が影響、0.8.6で修正）、CISAは11月23日にCVE-2026-133968を既知の悪用された脆弱性カタログに追加した。中国関連という帰属はAmazonの中程度の確度の評価であり、被害組織は公表されず、データ窃取も述べられていない。

summary_ko: |
  **2026년 11월 20일, Amazon Threat Intelligence는 중국 연계 공격자가 운영한 자율 AI 에이전트가 오픈소스 의료 영상 AI 애플리케이션 MONAI Label의 알려지지 않은 취약점을 스스로 발견하고 이를 이용해 한 대학 서버를 완전히 장악했다고 밝혔다.** Amazon은 2026년 9월 10일 인증 없이 노출된 운영자의 Cairn 인스턴스(오픈소스 자율 AI 침투 테스트 프레임워크)를 발견했으며, 프롬프트와 프로젝트 설정, AI 출력이 누구에게나 보이는 상태였다. 캠페인은 9월 8일부터 약 48시간 동안 중국 본토 밖 동아시아 대학들의 IP 주소를 겨냥했고, 목표는 "obtain shell access"의 여러 변형이었다. MONAI Label 서버에 대해 에이전트는 API를 파악하고 업로드 엔드포인트의 파일명 매개변수로 경로 탐색을 시험해 약 11분 만에 임의 파일 쓰기에 도달했다. 이후 세션에서는 Python 리버스 셸을 `sitecustomize.py`에 쓰고 학습 엔드포인트를 호출해 root로 실행되는 셸을 얻었다. Amazon은 이 결함이 제로데이였다고 높은 신뢰도로 평가한다. 그 뒤 운영자는 같은 소프트웨어가 실행되는 서버를 거쳐 두 번째 대학 네트워크로 들어가는 프록시를 에이전트에 제공했고, Amazon은 그 서버도 같은 결함으로 침해된 것으로 추정한다. 다른 두 작전은 실패했다. 열려 있는 Redis 서버에 대한 약 16시간, 148회의 작업과 GPU 서버에 대한 3만 건이 넘는 자격 증명 시도였다. 유지관리자는 11월 18일 권고문 GHSA-qc22-rmgc-vg94를 공개했고(0.8.5 이하 영향, 0.8.6에서 수정), CISA는 11월 23일 CVE-2026-133968을 알려진 악용 취약점 목록에 추가했다. 중국 연계라는 귀속은 Amazon의 중간 신뢰도 평가이며, 피해 기관은 공개되지 않았고 데이터 탈취도 언급되지 않았다.

summary_de: |
  **Am 20. November 2026 berichtete Amazon Threat Intelligence, dass autonome KI-Agenten eines China-nahen Akteurs eine bislang unbekannte Schwachstelle in der quelloffenen KI-Anwendung für medizinische Bildgebung MONAI Label entdeckten und damit die vollständige Kontrolle über einen Universitätsserver erlangten.** Amazon fand die Cairn-Instanz des Betreibers (ein quelloffenes Framework für autonome KI-Penetrationstests) am 10. September 2026 ohne Authentifizierung im Internet; Prompts, Projektkonfigurationen und KI-Ausgaben waren für jeden lesbar. Die Kampagne lief ab dem 8. September rund 48 Stunden gegen IP-Adressen von Universitäten in Ostasien außerhalb Festlandchinas, mit Zielen, die Varianten von "obtain shell access" waren. Gegen den MONAI-Label-Server kartierten die Agenten die API, prüften den Dateinamen-Parameter eines Upload-Endpunkts auf Path Traversal und erreichten in etwa 11 Minuten beliebiges Schreiben von Dateien; in einer späteren Sitzung schrieben sie eine Python-Reverse-Shell in `sitecustomize.py`, lösten einen Trainings-Endpunkt aus und erhielten eine Shell mit Root-Rechten. Amazon stuft die Lücke mit hoher Sicherheit als Zero-Day ein. Danach gab der Betreiber den Agenten einen Proxy in ein zweites Universitätsnetz über einen Server mit derselben Software, der nach Amazons Schlussfolgerung mit derselben Lücke kompromittiert wurde. Zwei weitere Operationen scheiterten: rund 16 Stunden und 148 Aktionen gegen einen offenen Redis-Server sowie mehr als 30.000 Zugangsdaten-Kombinationen gegen einen GPU-Server. Die Maintainer veröffentlichten am 18. November das Advisory GHSA-qc22-rmgc-vg94 (betroffen bis 0.8.5, behoben in 0.8.6); CISA nahm CVE-2026-133968 am 23. November in den Katalog bekannter ausgenutzter Schwachstellen auf. Die Zuordnung zu einem China-nahen Akteur ist Amazons Einschätzung mit mittlerer Sicherheit; die Opfer werden nicht genannt, ein Datendiebstahl wird nicht angegeben.

summary_fr: |
  **Le 20 novembre 2026, Amazon Threat Intelligence a rapporté que des agents IA autonomes exploités par un acteur lié à la Chine ont découvert une vulnérabilité jusque-là inconnue dans MONAI Label, application open source d'IA pour l'imagerie médicale, et s'en sont servis pour prendre le contrôle total d'un serveur universitaire.** Amazon a trouvé le 10 septembre 2026 l'instance Cairn de l'opérateur (un cadre open source de tests d'intrusion autonomes par IA) exposée sans authentification ; les prompts, les configurations de projet et les sorties de l'IA étaient lisibles par tous. La campagne a duré environ 48 heures à partir du 8 septembre contre des adresses IP d'universités d'Asie de l'Est hors de Chine continentale, avec des objectifs qui étaient des variantes de "obtain shell access". Contre le serveur MONAI Label, les agents ont cartographié l'API, testé le paramètre de nom de fichier d'un point de téléversement pour une traversée de répertoires et obtenu l'écriture arbitraire de fichiers en 11 minutes environ ; lors d'une session ultérieure, ils ont écrit un reverse shell Python dans `sitecustomize.py`, déclenché un point d'entraînement et obtenu un shell exécuté en root. Amazon estime avec un degré de confiance élevé que la faille était un zero-day. L'opérateur a ensuite fourni aux agents un proxy vers le réseau d'une seconde université, via un serveur exécutant le même logiciel, qu'Amazon suppose compromis par la même faille. Deux autres opérations ont échoué : environ 16 heures et 148 actions contre un serveur Redis ouvert, et plus de 30 000 combinaisons d'identifiants contre un serveur GPU. Les mainteneurs ont publié l'avis GHSA-qc22-rmgc-vg94 le 18 novembre (versions jusqu'à 0.8.5 touchées, 0.8.6 corrigée) ; la CISA a ajouté CVE-2026-133968 à son catalogue des vulnérabilités exploitées le 23 novembre. L'attribution à un acteur lié à la Chine est une évaluation d'Amazon de confiance moyenne ; les victimes ne sont pas nommées et aucun vol de données n'est indiqué.

summary_es: |
  **El 20 de noviembre de 2026, Amazon Threat Intelligence informó de que agentes de IA autónomos operados por un actor vinculado a China descubrieron una vulnerabilidad hasta entonces desconocida en MONAI Label, una aplicación de IA de código abierto para imagen médica, y la usaron para tomar el control total de un servidor universitario.** Amazon encontró el 10 de septiembre de 2026 la instancia de Cairn del operador (un marco de código abierto de pruebas de penetración autónomas con IA) expuesta sin autenticación; los prompts, las configuraciones de proyecto y la salida de la IA eran legibles por cualquiera. La campaña duró unas 48 horas desde el 8 de septiembre contra direcciones IP de universidades de Asia Oriental fuera de China continental, con objetivos que eran variantes de "obtain shell access". Contra el servidor de MONAI Label, los agentes mapearon la API, probaron el parámetro de nombre de archivo de un endpoint de subida en busca de path traversal y lograron la escritura arbitraria de archivos en unos 11 minutos; en una sesión posterior escribieron un reverse shell de Python en `sitecustomize.py`, activaron un endpoint de entrenamiento y obtuvieron un shell como root. Amazon evalúa con confianza alta que el fallo era un zero-day. Después el operador dio a los agentes un proxy hacia la red de una segunda universidad a través de un servidor con el mismo software, que Amazon infiere que fue comprometido con el mismo fallo. Otras dos operaciones fracasaron: unas 16 horas y 148 acciones contra un servidor Redis abierto, y más de 30.000 combinaciones de credenciales contra un servidor de GPU. Los mantenedores publicaron el aviso GHSA-qc22-rmgc-vg94 el 18 de noviembre (afecta hasta la 0.8.5, corregido en la 0.8.6); la CISA añadió CVE-2026-133968 a su catálogo de vulnerabilidades explotadas el 23 de noviembre. La atribución a un actor vinculado a China es una evaluación de Amazon con confianza moderada; no se nombra a las víctimas ni se indica robo de datos.

sources:
  - url: https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
    label: Amazon Threat Intelligence (AWS Security Blog, CJ Moses)
  - url: https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94
    label: MONAI Label security advisory GHSA-qc22-rmgc-vg94
  - url: https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968
    label: CISA Known Exploited Vulnerabilities catalog (CVE-2026-133968, added 2026-11-23)
  - url: https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/
    label: SecurityWeek
  - url: https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382
    label: The Register
disputed: false
landmark: true
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# Amazon: a China-nexus actor's Cairn AI agents found and exploited a MONAI Label zero-day on their own to root a university server

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square)

## Summary

**On 20 November 2026, Amazon Threat Intelligence reported that autonomous AI agents run by a China-nexus actor discovered a previously unknown vulnerability in the open-source medical-imaging AI application MONAI Label and used it to take full control of a university server.** Amazon found the operator's Cairn instance (an open-source autonomous AI penetration-testing framework) exposed without authentication on 10 September 2026, with prompts, project configurations and AI output readable by anyone. The campaign ran for about 48 hours from 8 September against IP addresses of universities in East Asia outside mainland China, with goals that were variations of "obtain shell access". Against the MONAI Label server the agents mapped the API, tested an upload endpoint's filename parameter for path traversal and reached arbitrary file write in about 11 minutes; in a later session they wrote a Python reverse shell to `sitecustomize.py`, triggered a training endpoint and got a shell running as root. Amazon assesses with high confidence that the flaw was a zero-day. The operator then gave the agents a proxy into a second university network through a server running the same software, which Amazon infers was compromised with the same flaw. Two other operations failed: about 16 hours and 148 actions against an open Redis server, and more than 30,000 credential combinations against a GPU server. The maintainers published advisory GHSA-qc22-rmgc-vg94 on 18 November (versions up to 0.8.5 affected, 0.8.6 patched); CISA added CVE-2026-133968 to its Known Exploited Vulnerabilities catalog on 23 November. Attribution to a China-nexus actor is Amazon's moderate-confidence assessment; the victims are not named and no data theft is stated.

## Attack chain

```mermaid
flowchart LR
    A["Operator gives Cairn agents<br/>university IP addresses and the goal<br/>'obtain shell access'"]:::entry
    B["Agents map a MONAI Label API,<br/>test an upload filename parameter,<br/>find path traversal in ~11 minutes"]:::step
    C["Agents write a reverse shell to<br/>sitecustomize.py and trigger<br/>a training endpoint"]:::step
    D["Root shell on a university server;<br/>operator pivots into a second<br/>university network"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**How Amazon saw it.** On 10 September 2026 Amazon Threat Intelligence identified a server with a publicly hosted, unauthenticated instance of Cairn. Because the operator left it open, the whole operational history was visible: project configurations, the operator's prompts and the AI output. The prompts were written in Simplified Chinese and timestamps in executed scripts were set to China Standard Time. The campaign targeted IP addresses associated with universities in East Asia outside mainland China over about 48 hours beginning 8 September 2026. The operator supplied a list of IP addresses and variations of the goal to obtain shell access; the agents planned, executed and adjusted without the operator choosing each next step.

**The zero-day.** Against a server running MONAI Label, the agents identified the framework, mapped its API endpoints and found an upload endpoint with a filename parameter. They tested it for path traversal and it was vulnerable: per Amazon, about 11 minutes passed between mapping the API and arbitrarily writing files on the server. In a later session the agents used the same flaw to write a Python reverse-shell payload to `sitecustomize.py`, a file Python imports at interpreter startup, then called a training API endpoint to spawn a new Python process, which imported the payload and opened a reverse shell running as root. Amazon says the flaw matched no advisory, fix, issue or database entry at the time and assesses with high confidence that it was a zero-day.

**What the maintainers and CISA published.** The MONAI Label advisory GHSA-qc22-rmgc-vg94 (published 18 November 2026, rated Critical by the maintainers, credited to Amazon's vulnerability disclosure programme) describes the flaw: the `PUT /datastore/image` endpoint uses a caller-controlled `image` query parameter as the image ID without validation, so a value such as `../../../tmp/x` writes the uploaded content anywhere the process can write; `PUT /datastore/label` builds its destination the same way. Versions up to and including 0.8.5 are affected and 0.8.6 is patched. The CISA catalog lists CVE-2026-133968 for this flaw, added on 23 November 2026 with a remediation due date of 26 November.

**The operations that failed.** The longest operation ran about 16 hours and 148 sequential actions against a Redis instance that allowed unauthenticated access: the agents tried replication abuse, a scripting-sandbox escape, configuration-file writes and memory corruption, attempted Log4Shell against another service on the host, mapped the internal Docker network through a server-side request forgery flaw in a co-located Qdrant instance and sprayed credentials at PostgreSQL, SSH and other services. None of it worked. A second operation ran for more than 6 hours against a university GPU server: the agents built a list of about 80 real usernames from faculty directories, lab sites, archived pages and papers, then tried more than 30,000 credential combinations against SSH and other university systems without finding a working login.

**Where the human stepped in.** After the agents found the zero-day, the operator supplied a proxy that tunnelled into a second university network. The server behind the proxy ran the same vulnerable software; Amazon infers, but does not state as observed, that the operator had used the zero-day to compromise it. The operator then directed the agents at other machines in that network.

**What is not established.** Attribution to a China-nexus actor is Amazon's moderate-confidence assessment, based on the language of the prompts, the script timezone and the choice of targets. The affected universities are not named; they were not AWS customers and were notified through a government partner. Amazon does not describe data being taken. The model driving the agents is not named. The account rests on Amazon's reading of the exposed instance; SecurityWeek and The Register report it from Amazon's post rather than from independent access.

**How it is graded.** `incident`: a real intrusion against real organisations, observed from the attacker's own console, with a maintainer advisory and a CISA catalog entry that confirm the flaw and its exploitation. `WEAPON`: a human operator deliberately pointed an agent framework at targets. `high`: full control of one server is confirmed and a second compromise is inferred, but no data loss or service impact is reported, so it is not graded `critical`. It is marked as a landmark because the agents found the vulnerability themselves during the operation, rather than being handed a known exploit.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Amazon Threat Intelligence (AWS Security Blog, CJ Moses) | <https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/> |
| 2 | MONAI Label security advisory GHSA-qc22-rmgc-vg94 | <https://github.com/Project-MONAI/MONAILabel/security/advisories/GHSA-qc22-rmgc-vg94> |
| 3 | CISA Known Exploited Vulnerabilities catalog (CVE-2026-133968, added 2026-11-23) | <https://www.cisa.gov/known-exploited-vulnerabilities-catalog?field_cve=CVE-2026-133968> |
| 4 | SecurityWeek | <https://www.securityweek.com/amazon-china-linked-hackers-ai-agents-exploited-medical-software-zero-day/> |
| 5 | The Register | <https://www.theregister.com/security/2026/11/20/china-attackers-deployed-ai-agents-that-autonomously-found-and-exploited-a-0-day-to-take-over-a-university-server/5311382> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-20` (raw: 2026-11-20 (Amazon Threat Intelligence post; campaign ran 2026-09-08 to 2026-09-10; MONAI Label advisory GHSA-qc22-rmgc-vg94 published 2026-11-18; CVE-2026-133968 added to CISA KEV 2026-11-23), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) |
| Severity | **High** `high` |
| Confidence | **A** — Amazon Threat Intelligence's own report from the attacker's exposed console, plus the maintainers' advisory and the CISA catalog entry; SecurityWeek and The Register relay Amazon |
| Real harm | Yes — root shell on one university server; a second university server inferred compromised; no data loss stated |
| AI involvement | Confirmed `confirmed` — Amazon read the agents' prompts, actions and output in the operator's unauthenticated Cairn instance |
| Region | [Asia-Pacific](../../regions/apac.md) |
| Archive ID | `2026-11-20-cairn-agents-monai-label-zero-day` |

<sub>**Why this classification:** A real intrusion in which an operator pointed autonomous agents at targets (`WEAPON`) and the agents themselves found and exploited an unknown flaw, confirmed by the maintainers' advisory and a CISA KEV entry, hence `incident` and `real_harm: true`. `high`, not `critical`: one server fully controlled and a second inferred, with no reported data loss. `confidence: A` for a first-hand vendor threat-intelligence report backed by the advisory and the catalog; the attribution is moderate-confidence and the second compromise is an inference, both stated as such. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-11-12` [Unit 42: CL-STA-1238 ran 25 autonomous Cairn operations against at least 19 organisations](2026-11-12-unit42-cl-sta-1238-cairn-campaign.md)<br>  <sub>Another China-nexus Cairn campaign from the same weeks, disclosed eight days earlier</sub>
- `2026-10-27` [Attackers hijack exposed Cairn AI-agent panels in the wild](../2026-10/2026-10-27-cairn-exposed-agent-panels-hijacked.md)<br>  <sub>The same framework, with the exposure running the other way: open Cairn panels taken over by third parties</sub>
- `2026-09-22` [Gambit: three AI harnesses stole 600,000 card records from online retailers](../2026-09/2026-09-22-gambit-ai-agent-retail-card-theft.md)<br>  <sub>The financially motivated Cairn use that Amazon's post cites as a separate actor</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-20-cairn-agents-monai-label-zero-day.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
