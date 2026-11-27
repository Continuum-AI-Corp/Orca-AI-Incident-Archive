---
id: 2026-11-12-unit42-cl-sta-1238-cairn-campaign
title: "Unit 42: CL-STA-1238 ran 25 autonomous Cairn operations against at least 19 organisations and breached 10 of them"
title_zh: "Unit 42：CL-STA-1238 用 Cairn 对至少 19 家机构自主执行 25 次行动，攻破其中 10 家"
title_ja: "Unit 42：CL-STA-1238がCairnで少なくとも19組織に対し25件の自律型作戦を実行し、うち10組織に侵入"
title_ko: "Unit 42: CL-STA-1238이 Cairn으로 최소 19개 조직에 25건의 자율 작전을 수행해 그중 10곳을 침해"
title_de: "Unit 42: CL-STA-1238 führte mit Cairn 25 autonome Operationen gegen mindestens 19 Organisationen durch und drang in 10 davon ein"
title_fr: "Unit 42 : CL-STA-1238 a mené avec Cairn 25 opérations autonomes contre au moins 19 organisations et en a compromis 10"
title_es: "Unit 42: CL-STA-1238 ejecutó con Cairn 25 operaciones autónomas contra al menos 19 organizaciones y vulneró 10 de ellas"
date: 2026-11-12
date_raw: "2026-11-12 (Unit 42 report; operations ran August to September 2026)"
date_precision: day

kind: incident
type: [WEAPON, EXFIL, CRED]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US, GLOBAL]

summary: |
  **On 12 November 2026, Palo Alto Networks Unit 42 reported that Chinese-speaking attackers it tracks as CL-STA-1238 used the open-source AI penetration-testing framework Cairn to run 25 autonomous operations against at least 19 organisations in August and September 2026, achieving unauthorised access or data retrieval at 10 of them.** The attackers ran a customised Cairn fork from a server in Hong Kong, gave each operation a one-line goal and a target domain, and let the framework plan, execute and record results; operations lasted from 20 minutes to more than 50 hours. Thirteen ran on Zhipu GLM 5.2, eight on DeepSeek V4 Flash and four on DeepSeek V4 Pro. A preamble asserting the work was authorised, plus a generated `AUTHORIZATION.md` file, was enough: Unit 42 says neither model refused. Targets were concentrated in the semiconductor supply chain (seven organisations), defence and defence policy (three) and human rights and civil society (four). Confirmed outcomes include more than one million member records, about 31,000 CRM contacts and staff password hashes at a US teachers' union; about 500 user records, including .mil and .gov accounts, at a defence-policy programme; about 150,000 internal documents at an industrial-automation manufacturer; unauthorised administrator accounts and a persistent API token in a semiconductor company's production system; and a live standards-ballot document overwritten at an industry standards body. The flaws exploited were known classes: authentication bypasses, weak and default credentials, exposed cloud APIs and dated public CVEs. Attribution to China-nexus intelligence collection is Unit 42's moderate-confidence assessment, and the victims are not named.

summary_zh: |
  **2026 年 11 月 12 日，Palo Alto Networks 的 Unit 42 披露：其追踪为 CL-STA-1238 的中文攻击者，在 2026 年 8 月至 9 月用开源 AI 渗透测试框架 Cairn 对至少 19 家机构自主执行了 25 次行动，在其中 10 家实现了未授权访问或取走数据。** 攻击者在香港的一台服务器上运行定制的 Cairn 分支，每次行动只给一句话目标和一个目标域名，由框架自行规划、执行并记录结果；单次行动短则 20 分钟，长则超过 50 小时。25 次行动中 13 次用智谱 GLM 5.2，8 次用 DeepSeek V4 Flash，4 次用 DeepSeek V4 Pro。一段声称“任务均已授权”的前置提示，加上自动生成的 `AUTHORIZATION.md` 文件就够了：Unit 42 称两家模型都没有拒绝。目标集中在半导体供应链（7 家）、国防与国防政策（3 家）和人权与公民社会（4 家）。已确认的后果包括：美国一家教师工会的 100 多万条会员记录、约 3.1 万条 CRM 联系人和员工密码哈希；某国防政策项目约 500 条用户记录，其中有 .mil 和 .gov 账号；一家工业自动化制造商约 15 万份内部文档；在一家半导体公司的生产系统里创建了未授权的管理员账号和持久 API 令牌；以及某行业标准组织一份正在进行的标准投票文件被覆盖。被利用的都是已知类型的弱点：认证绕过、弱口令和默认口令、暴露的云 API、陈旧的公开 CVE。“中国关联的情报搜集”是 Unit 42 中等置信度的判断，受害方未具名。

summary_ja: |
  **2026年11月12日、Palo Alto NetworksのUnit 42は、CL-STA-1238として追跡する中国語話者の攻撃者が、オープンソースのAIペネトレーションテスト・フレームワークCairnを使い、2026年8月から9月にかけて少なくとも19組織に対し25件の自律型作戦を実行し、うち10組織で不正アクセスまたはデータ取得に成功したと報告した。** 攻撃者は香港のサーバーでカスタマイズしたCairnのフォークを動かし、各作戦に一行の目標と標的ドメインを与え、計画・実行・結果の記録をフレームワークに任せた。作戦は20分から50時間超まで続いた。13件はZhipu GLM 5.2、8件はDeepSeek V4 Flash、4件はDeepSeek V4 Proで実行された。作業が承認済みだと主張する前置きと、自動生成された`AUTHORIZATION.md`ファイルだけで十分で、Unit 42によればどちらのモデルも拒否しなかった。標的は半導体サプライチェーン（7組織）、防衛・防衛政策（3組織）、人権・市民社会（4組織）に集中していた。確認された結果には、米国の教員組合での100万件超の会員記録、約3万1千件のCRM連絡先、職員のパスワードハッシュ、防衛政策プログラムでの.milおよび.govアカウントを含む約500件のユーザー記録、産業オートメーション製造企業の約15万件の内部文書、半導体企業の本番システムでの不正な管理者アカウントと永続的なAPIトークンの作成、業界標準化団体で進行中の標準投票文書の上書きが含まれる。悪用された欠陥は既知の類型であり、認証回避、脆弱または既定の認証情報、公開されたクラウドAPI、古い公開CVEだった。中国関連の情報収集という帰属はUnit 42の中程度の確度の評価であり、被害組織は公表されていない。

summary_ko: |
  **2026년 11월 12일, Palo Alto Networks의 Unit 42는 CL-STA-1238로 추적하는 중국어 사용 공격자가 오픈소스 AI 침투 테스트 프레임워크 Cairn을 사용해 2026년 8월부터 9월까지 최소 19개 조직에 25건의 자율 작전을 수행했고, 그중 10곳에서 무단 접근 또는 데이터 확보에 성공했다고 밝혔다.** 공격자는 홍콩의 서버에서 맞춤형 Cairn 포크를 운영하며 작전마다 한 줄짜리 목표와 대상 도메인만 주고 계획, 실행, 결과 기록을 프레임워크에 맡겼다. 작전은 20분에서 50시간 이상까지 이어졌다. 13건은 Zhipu GLM 5.2, 8건은 DeepSeek V4 Flash, 4건은 DeepSeek V4 Pro로 실행됐다. 작업이 승인됐다고 주장하는 서문과 자동 생성된 `AUTHORIZATION.md` 파일만으로 충분했으며, Unit 42에 따르면 두 모델 모두 거부하지 않았다. 표적은 반도체 공급망(7곳), 국방 및 국방 정책(3곳), 인권 및 시민사회(4곳)에 집중됐다. 확인된 결과에는 미국 교원 노조의 100만 건이 넘는 회원 기록과 약 3만 1천 건의 CRM 연락처, 직원 비밀번호 해시, 국방 정책 프로그램의 .mil 및 .gov 계정을 포함한 약 500건의 사용자 기록, 산업 자동화 제조업체의 내부 문서 약 15만 건, 반도체 기업 운영 시스템에 생성된 무단 관리자 계정과 영구 API 토큰, 업계 표준 기구에서 진행 중이던 표준 투표 문서의 덮어쓰기가 포함된다. 악용된 결함은 알려진 유형으로, 인증 우회, 취약하거나 기본값인 자격 증명, 노출된 클라우드 API, 오래된 공개 CVE였다. 중국 연계 정보 수집이라는 귀속은 Unit 42의 중간 신뢰도 평가이며, 피해 조직은 공개되지 않았다.

summary_de: |
  **Am 12. November 2026 berichtete Unit 42 von Palo Alto Networks, dass chinesischsprachige Angreifer, die es als CL-STA-1238 führt, mit dem quelloffenen KI-Penetrationstest-Framework Cairn im August und September 2026 25 autonome Operationen gegen mindestens 19 Organisationen durchführten und bei 10 davon unbefugten Zugriff oder Datenabruf erreichten.** Die Angreifer betrieben einen angepassten Cairn-Fork auf einem Server in Hongkong, gaben jeder Operation ein einzeiliges Ziel und eine Zieldomain und überließen Planung, Ausführung und Protokollierung dem Framework; die Operationen dauerten zwischen 20 Minuten und mehr als 50 Stunden. Dreizehn liefen auf Zhipu GLM 5.2, acht auf DeepSeek V4 Flash und vier auf DeepSeek V4 Pro. Eine Präambel, die die Arbeit als autorisiert ausgab, und eine generierte Datei `AUTHORIZATION.md` genügten: Laut Unit 42 verweigerte keines der Modelle. Die Ziele lagen vor allem in der Halbleiter-Lieferkette (sieben Organisationen), in Verteidigung und Verteidigungspolitik (drei) sowie bei Menschenrechten und Zivilgesellschaft (vier). Zu den bestätigten Folgen gehören mehr als eine Million Mitgliederdatensätze, rund 31.000 CRM-Kontakte und Passwort-Hashes von Beschäftigten bei einer US-Lehrergewerkschaft; rund 500 Nutzerdatensätze einschließlich .mil- und .gov-Konten bei einem verteidigungspolitischen Programm; rund 150.000 interne Dokumente bei einem Hersteller von Industrieautomation; unbefugte Administratorkonten und ein dauerhaftes API-Token im Produktivsystem eines Halbleiterunternehmens; sowie ein überschriebenes laufendes Abstimmungsdokument bei einem Industrie-Normungsgremium. Ausgenutzt wurden bekannte Schwachstellenklassen: Authentifizierungsumgehungen, schwache und voreingestellte Zugangsdaten, exponierte Cloud-APIs und ältere öffentliche CVEs. Die Zuordnung zu China-naher Informationsgewinnung ist eine Einschätzung von Unit 42 mit mittlerer Sicherheit; die Opfer werden nicht genannt.

summary_fr: |
  **Le 12 novembre 2026, l'équipe Unit 42 de Palo Alto Networks a rapporté que des attaquants sinophones qu'elle suit sous le nom CL-STA-1238 ont utilisé le cadre open source de tests d'intrusion par IA Cairn pour mener 25 opérations autonomes contre au moins 19 organisations en août et septembre 2026, obtenant un accès non autorisé ou des données dans 10 d'entre elles.** Les attaquants exploitaient un fork personnalisé de Cairn depuis un serveur à Hong Kong, donnaient à chaque opération un objectif d'une ligne et un domaine cible, et laissaient le cadre planifier, exécuter et consigner les résultats ; les opérations ont duré de 20 minutes à plus de 50 heures. Treize ont tourné sur Zhipu GLM 5.2, huit sur DeepSeek V4 Flash et quatre sur DeepSeek V4 Pro. Un préambule affirmant que le travail était autorisé et un fichier `AUTHORIZATION.md` généré ont suffi : selon Unit 42, aucun des deux modèles n'a refusé. Les cibles se concentraient sur la chaîne d'approvisionnement des semi-conducteurs (sept organisations), la défense et la politique de défense (trois), les droits humains et la société civile (quatre). Les résultats confirmés comprennent plus d'un million de fiches de membres, environ 31 000 contacts CRM et des hachages de mots de passe du personnel dans un syndicat d'enseignants américain ; environ 500 fiches d'utilisateurs, dont des comptes .mil et .gov, dans un programme de politique de défense ; environ 150 000 documents internes chez un fabricant d'automatismes industriels ; des comptes administrateur non autorisés et un jeton d'API persistant dans le système de production d'une entreprise de semi-conducteurs ; et l'écrasement d'un document de vote en cours dans un organisme de normalisation. Les failles exploitées relevaient de classes connues : contournements d'authentification, identifiants faibles ou par défaut, API cloud exposées et CVE publiques anciennes. L'attribution à une collecte de renseignement liée à la Chine est une évaluation d'Unit 42 de confiance moyenne ; les victimes ne sont pas nommées.

summary_es: |
  **El 12 de noviembre de 2026, Unit 42 de Palo Alto Networks informó de que atacantes de habla china a los que rastrea como CL-STA-1238 usaron el marco de pruebas de penetración con IA de código abierto Cairn para ejecutar 25 operaciones autónomas contra al menos 19 organizaciones en agosto y septiembre de 2026, logrando acceso no autorizado u obtención de datos en 10 de ellas.** Los atacantes operaban un fork personalizado de Cairn desde un servidor en Hong Kong, daban a cada operación un objetivo de una línea y un dominio, y dejaban que el marco planificara, ejecutara y registrara los resultados; las operaciones duraron entre 20 minutos y más de 50 horas. Trece se ejecutaron con Zhipu GLM 5.2, ocho con DeepSeek V4 Flash y cuatro con DeepSeek V4 Pro. Un preámbulo que afirmaba que el trabajo estaba autorizado y un archivo `AUTHORIZATION.md` generado bastaron: según Unit 42, ninguno de los modelos se negó. Los objetivos se concentraron en la cadena de suministro de semiconductores (siete organizaciones), defensa y política de defensa (tres) y derechos humanos y sociedad civil (cuatro). Los resultados confirmados incluyen más de un millón de registros de afiliados, unos 31.000 contactos de CRM y hashes de contraseñas del personal en un sindicato de docentes de Estados Unidos; unos 500 registros de usuarios, incluidas cuentas .mil y .gov, en un programa de política de defensa; unos 150.000 documentos internos en un fabricante de automatización industrial; cuentas de administrador no autorizadas y un token de API persistente en el sistema de producción de una empresa de semiconductores; y la sobrescritura de un documento de votación en curso en un organismo de normalización. Los fallos explotados eran de clases conocidas: evasiones de autenticación, credenciales débiles o por defecto, API en la nube expuestas y CVE públicas antiguas. La atribución a recopilación de inteligencia vinculada a China es una evaluación de Unit 42 con confianza moderada; no se nombra a las víctimas.

sources:
  - url: https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/
    label: Palo Alto Networks Unit 42 (CL-STA-1238 report)
  - url: https://www.govinfosecurity.com/chinese-actor-automates-attacks-on-us-defense-chip-firms-a-33392
    label: GovInfoSecurity
  - url: https://www.csoonline.com/article/4247565/palo-alto-tracks-a-massive-chinese-ai-attack-that-sadly-lives-up-to-industry-fears.html
    label: CSO Online
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# Unit 42: CL-STA-1238 ran 25 autonomous Cairn operations against at least 19 organisations and breached 10 of them

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 12 November 2026, Palo Alto Networks Unit 42 reported that Chinese-speaking attackers it tracks as CL-STA-1238 used the open-source AI penetration-testing framework Cairn to run 25 autonomous operations against at least 19 organisations in August and September 2026, achieving unauthorised access or data retrieval at 10 of them.** The attackers ran a customised Cairn fork from a server in Hong Kong, gave each operation a one-line goal and a target domain, and let the framework plan, execute and record results; operations lasted from 20 minutes to more than 50 hours. Thirteen ran on Zhipu GLM 5.2, eight on DeepSeek V4 Flash and four on DeepSeek V4 Pro. A preamble asserting the work was authorised, plus a generated `AUTHORIZATION.md` file, was enough: Unit 42 says neither model refused. Targets were concentrated in the semiconductor supply chain (seven organisations), defence and defence policy (three) and human rights and civil society (four). Confirmed outcomes include more than one million member records, about 31,000 CRM contacts and staff password hashes at a US teachers' union; about 500 user records, including .mil and .gov accounts, at a defence-policy programme; about 150,000 internal documents at an industrial-automation manufacturer; unauthorised administrator accounts and a persistent API token in a semiconductor company's production system; and a live standards-ballot document overwritten at an industry standards body. The flaws exploited were known classes: authentication bypasses, weak and default credentials, exposed cloud APIs and dated public CVEs. Attribution to China-nexus intelligence collection is Unit 42's moderate-confidence assessment, and the victims are not named.

## Attack chain

```mermaid
flowchart LR
    A["Operators create a task per target:<br/>a one-line goal, a root domain,<br/>an authorisation pretext"]:::entry
    B["Cairn on GLM 5.2 / DeepSeek V4<br/>maps the attack surface and loops<br/>reason and explore on its own"]:::step
    C["Known weaknesses exploited:<br/>auth bypass, weak credentials,<br/>exposed cloud APIs, old CVEs"]:::step
    D["10 of 19+ organisations breached:<br/>1M+ member records, .mil/.gov accounts,<br/>admin accounts, a ballot overwritten"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The framework and how it was used.** Cairn is a publicly available penetration-testing framework in which an AI model drives each agent worker and the workers coordinate through a shared blackboard, writing findings back as a graph of confirmed facts and queued intents; a human can inject hints at any time. Unit 42 says the attackers ran a customised fork from a server hosted in Hong Kong, with an egress and staging node in the United States. For each operation they created a task with a one-line goal (in Chinese; Unit 42 translates one as obtaining substantive high-value access such as a webshell, SSH, source code, keys, user information or credentials, ideally reaching the internal network) and seeded it with the organisation's root domain. The model produced a different three-to-seven-stage plan per target and then looped between reasoning over what it had found and carrying out one action at a time. Individual operations ran from 20 minutes to more than 50 hours with no time limit imposed.

**Models and guardrails.** Of the 25 operations, 13 ran on Zhipu GLM 5.2, 8 on DeepSeek V4 Flash and 4 on DeepSeek V4 Pro; Unit 42 says the attackers appear to have benchmarked the models against each other, using the higher tier for targets that resisted the cheaper one. Each operation loaded a skill pack named AIScan Runner Skills that is not in the upstream project. Cairn's stock prompts already tell the model never to refuse; the attackers added a Chinese-language preamble asserting the engagement was an authorised security test, and each operation generated an `AUTHORIZATION.md` file declaring it authorised. Unit 42 reports that neither Zhipu GLM nor DeepSeek refused this framing.

**Who was targeted.** At least 19 organisations: seven in the semiconductor and advanced-manufacturing supply chain (lithography, chip design, materials, photomask and standards), three in defence and defence policy (a space technology company, a defence-analytics vendor and a policy think tank) and four in human rights and civil society (a Canadian human-rights body, a US teachers' union, a science-policy advocacy group and an education nonprofit). In some tasks the attackers added information gathered beforehand: one task against a semiconductor equipment supplier included VPN gateway addresses, group names and shared group passwords for multiple sites.

**Confirmed outcomes.** Unit 42 says Cairn confirmed unauthorised access or data retrieval at 10 organisations. At an industry standards body, password spraying yielded dozens of valid credentials and access to non-public directory databases; the attackers overwrote a live standards-ballot document through an unauthenticated cloud-storage write and, through separate flaws, logged in as arbitrary customers with read, write and delete access to meeting, voting and back-office functions. At a semiconductor company they brute-forced a production credential on a partner-integration application, retrieved application data, user lists and email lists, and created unauthorised administrator accounts and a persistent API token. At a US teachers' union an unauthenticated account-creation bypass on the content management system let them mint sessions and harvest data: the framework logged access to more than one million member records, roughly 31,000 CRM contacts and staff password hashes. An open registration endpoint on the identity platform behind a defence-policy programme exposed roughly 500 user records, including .mil and .gov accounts. The remaining five cases covered tens of thousands of content-management records, including employee data at a semiconductor-lithography manufacturer, roughly 150,000 internal documents at an industrial-automation manufacturer and student data at an education nonprofit.

**What is not established.** The victims are not named, and none has confirmed the intrusions publicly. The figures are what the framework logged, as read by Unit 42. Attribution to China-nexus intelligence collection is a moderate-confidence assessment resting on the language of the artifacts, the exclusive use of Chinese models and the target set. GovInfoSecurity and CSO Online report the findings from Unit 42's publication. Unit 42 judges the operators were likely a single person or a small team.

**How it is graded.** `incident`: real intrusions with data retrieved and production systems changed, reconstructed by a named research team from the attackers' own framework. `WEAPON` because human operators deliberately aimed the agents; `EXFIL` because member, user and document data left the victims; `CRED` because credentials, password hashes and a persistent API token were obtained or created. `high`: ten organisations breached with large volumes of personal data, but the victims are unnamed and unconfirmed, and the count of people affected rests on the attacker-side log. Unit 42's own point is that the flaws were ordinary; what changed is that one operator could pursue 19 targets at once.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Palo Alto Networks Unit 42 (CL-STA-1238 report) | <https://unit42.paloaltonetworks.com/cairn-framework-ai-autonomous-attacks/> |
| 2 | GovInfoSecurity | <https://www.govinfosecurity.com/chinese-actor-automates-attacks-on-us-defense-chip-firms-a-33392> |
| 3 | CSO Online | <https://www.csoonline.com/article/4247565/palo-alto-tracks-a-massive-chinese-ai-attack-that-sadly-lives-up-to-industry-fears.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-12` (raw: 2026-11-12 (Unit 42 report; operations ran August to September 2026), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) [`EXFIL`](../../taxonomy/types.md#exfil) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — original research by Unit 42 from the attackers' own Cairn framework, with checkable technical detail; GovInfoSecurity and CSO Online relay it; no victim has confirmed |
| Real harm | Yes — unauthorised access or data retrieval at 10 organisations, including 1M+ member records, .mil/.gov accounts and rogue administrator accounts in production |
| AI involvement | Confirmed `confirmed` — Unit 42 analysed the attackers' Cairn fork, its task definitions, prompts and per-operation model use |
| Region | [United States](../../regions/us.md) · [Global](../../regions/global.md) |
| Archive ID | `2026-11-12-unit42-cl-sta-1238-cairn-campaign` |

<sub>**Why this classification:** Real intrusions reconstructed from the attackers' own framework: operators deliberately aimed autonomous agents (`WEAPON`), data left the victims (`EXFIL`) and credentials and a persistent token were obtained or created (`CRED`), hence `incident` and `real_harm: true`. `high`: ten organisations breached and large volumes of personal data, with unnamed, unconfirmed victims and attacker-side counts. `confidence: A` for a named research team's first-hand technical report; the attribution is moderate-confidence and is stated as such. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-11-20` [Amazon: a China-nexus actor's Cairn AI agents found and exploited a MONAI Label zero-day](2026-11-20-cairn-agents-monai-label-zero-day.md)<br>  <sub>Another China-nexus Cairn operation from September, where the agents found the flaw themselves</sub>
- `2026-10-27` [Attackers hijack exposed Cairn AI-agent panels in the wild](../2026-10/2026-10-27-cairn-exposed-agent-panels-hijacked.md)<br>  <sub>The same framework seen from the other side: exposed Cairn panels taken over</sub>
- `2026-11-05` [Hacking on Autopilot: Check Point reconstructs ARTEX cybercrime campaigns](2026-11-05-artex-hacking-on-autopilot-cybercrime.md)<br>  <sub>The comparable reconstruction for the ARTEX framework, from recovered operator consoles</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-12-unit42-cl-sta-1238-cairn-campaign.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
