---
id: 2026-11-07-mittwald-mcp-server-breach
title: "German host Mittwald breached through a shell-injection flaw in its own MCP server; 56 customer projects compromised"
title_zh: "德国主机商 Mittwald 因自家 MCP 服务器的 shell 注入漏洞被入侵，56 个客户项目被攻陷"
title_ja: "ドイツのホスティング企業Mittwald、自社MCPサーバーのシェルインジェクション欠陥から侵入され、顧客プロジェクト56件が侵害"
title_ko: "독일 호스팅 업체 Mittwald, 자사 MCP 서버의 셸 인젝션 결함으로 침해되어 고객 프로젝트 56개가 장악됨"
title_de: "Mittwald über eine Shell-Injection-Lücke im eigenen MCP-Server angegriffen; 56 Kundenprojekte kompromittiert"
title_fr: "L'hébergeur allemand Mittwald piraté via une injection shell dans son propre serveur MCP ; 56 projets clients compromis"
title_es: "El proveedor de hosting alemán Mittwald, vulnerado por una inyección de shell en su propio servidor MCP; 56 proyectos de clientes comprometidos"
date: 2026-11-07
date_raw: "2026-11-07 (Mittwald incident post; flaw first probed 2026-10-21, exploited from 2026-10-27, detected 2026-11-04; post-mortem published 2026-11-25)"
date_precision: day

kind: incident
type: [MCP, CRED, EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [EU]

summary: |
  **On 7 November 2026 the German web host Mittwald disclosed that an attacker had broken into its platform through a flaw in its MCP server, the service that lets customers connect AI assistants such as Claude or ChatGPT to the mStudio hosting panel.** In a post-mortem published on 25 November, Mittwald identified the flaw as a shell injection in one of the server's tools: the `comment` and `passphrase` parameters of a tool call were placed into a command line and run with `execSync`, giving arbitrary command execution in the server's container. The MCP server holds valid access and refresh tokens for every active user, so the attacker read those tokens, including those of Mittwald employees, and used them to create SSH users and API tokens in other people's names and to copy configuration files and credentials out of projects. The attacker first probed the flaw on 21 October, exploited it from 27 October and was detected on 4 November; Mittwald shut the MCP server down, revoked all tokens and suspended mStudio login and SSH access from 5 to 7 November. It classified 56 projects as compromised and assumes data left them. Everyone who had used the MCP server was affected, along with projects their accounts could reach. Mittwald says it built the MCP server largely with AI coding agents and that the vulnerable code came from a test context and reached production unnoticed. In a second phase from 9 November the attacker returned, and on the night of 12 November exploited a previously unknown flaw in the Neos CMS to breach mittwald.de. Mittwald infers from the speed of the logged steps that the attacker used AI tools; The Record notes it gave no other evidence for that.

summary_zh: |
  **2026 年 11 月 7 日，德国主机商 Mittwald 披露：有攻击者通过其 MCP 服务器的一个漏洞侵入了平台。该 MCP 服务器用于让客户把 Claude、ChatGPT 等 AI 助手接到 mStudio 主机管理面板上。** 在 11 月 25 日发布的复盘中，Mittwald 指出漏洞是服务器某个工具里的 shell 注入：工具调用的 `comment` 和 `passphrase` 参数被直接拼进命令行，再用 `execSync` 执行，攻击者由此可在服务器容器内执行任意命令。MCP 服务器随时持有所有活跃用户的有效 access token 和 refresh token，于是攻击者读走了这些令牌（包括 Mittwald 员工的），再用它们冒名创建 SSH 用户和 API 令牌，并从项目里拷走配置文件和凭据。攻击者 10 月 21 日首次试探该漏洞，10 月 27 日起加以利用，11 月 4 日被发现；Mittwald 关停了 MCP 服务器、吊销全部令牌，并在 11 月 5 日至 7 日暂停了 mStudio 登录和 SSH 访问。它把 56 个项目定为已被攻陷，并认定其中有数据流出。凡是用过 MCP 服务器的人都受影响，他们账号能访问的项目也在内。Mittwald 表示，这个 MCP 服务器大部分是用 AI 编码 agent 写的，出问题的代码来自测试场景，未被察觉就进了生产路径。11 月 9 日起攻击者卷土重来，并在 11 月 12 日夜间利用 Neos CMS 一个此前未知的漏洞攻入了 mittwald.de。Mittwald 根据日志里步骤之间只隔几秒，推断攻击者使用了 AI 工具；The Record 指出除此之外它没有给出别的证据。

summary_ja: |
  **2026年11月7日、ドイツのホスティング企業Mittwaldは、攻撃者が同社のMCPサーバーの欠陥を通じてプラットフォームに侵入したと公表した。このMCPサーバーは、顧客がClaudeやChatGPTなどのAIアシスタントをホスティング管理画面mStudioに接続するためのサービスである。** 11月25日に公開した事後分析でMittwaldは、欠陥がサーバーのツールの一つにあるシェルインジェクションだったと特定した。ツール呼び出しの`comment`と`passphrase`パラメータがコマンドラインに埋め込まれ`execSync`で実行されており、サーバーのコンテナ内で任意のコマンドを実行できた。MCPサーバーはすべてのアクティブユーザーの有効なアクセストークンとリフレッシュトークンを保持しているため、攻撃者はMittwald従業員のものを含むトークンを読み取り、それを使って他人の名義でSSHユーザーとAPIトークンを作成し、プロジェクトから設定ファイルと認証情報をコピーした。攻撃者は10月21日に初めて欠陥を試し、10月27日から悪用し、11月4日に検知された。MittwaldはMCPサーバーを停止し、すべてのトークンを失効させ、11月5日から7日までmStudioへのログインとSSHアクセスを停止した。同社は56件のプロジェクトを侵害されたと分類し、データが流出したとみなしている。MCPサーバーを利用した全員と、そのアカウントがアクセスできたプロジェクトが影響を受けた。MittwaldはMCPサーバーの大部分をAIコーディングエージェントで構築したと述べ、脆弱なコードはテスト用の文脈から来て気づかれずに本番に入ったとしている。11月9日からの第二段階で攻撃者は戻り、11月12日の夜にはNeos CMSの未知の欠陥を悪用してmittwald.deに侵入した。Mittwaldは記録された手順の速さから攻撃者がAIツールを使ったと推定しているが、The Recordはそれ以外の根拠は示されていないと指摘している。

summary_ko: |
  **2026년 11월 7일, 독일 호스팅 업체 Mittwald는 공격자가 자사 MCP 서버의 결함을 통해 플랫폼에 침입했다고 공개했다. 이 MCP 서버는 고객이 Claude나 ChatGPT 같은 AI 어시스턴트를 호스팅 관리 패널 mStudio에 연결할 수 있게 하는 서비스다.** 11월 25일 공개한 사후 분석에서 Mittwald는 결함이 서버 도구 중 하나의 셸 인젝션이었다고 밝혔다. 도구 호출의 `comment`와 `passphrase` 매개변수가 명령줄에 그대로 들어가 `execSync`로 실행됐고, 이로써 서버 컨테이너 안에서 임의 명령을 실행할 수 있었다. MCP 서버는 모든 활성 사용자의 유효한 액세스 토큰과 리프레시 토큰을 보관하고 있어, 공격자는 Mittwald 직원의 것을 포함한 토큰을 읽어 다른 사람 명의로 SSH 사용자와 API 토큰을 만들고 프로젝트에서 설정 파일과 자격 증명을 복사했다. 공격자는 10월 21일 결함을 처음 시험했고 10월 27일부터 악용했으며 11월 4일에 탐지됐다. Mittwald는 MCP 서버를 종료하고 모든 토큰을 폐기했으며 11월 5일부터 7일까지 mStudio 로그인과 SSH 접근을 중단했다. 회사는 프로젝트 56개를 침해된 것으로 분류했고 데이터가 유출된 것으로 간주한다. MCP 서버를 사용한 모든 사람과 그 계정이 접근할 수 있던 프로젝트가 영향을 받았다. Mittwald는 MCP 서버 대부분을 AI 코딩 에이전트로 만들었으며, 취약한 코드는 테스트용 맥락에서 나와 눈에 띄지 않고 운영 경로에 들어갔다고 밝혔다. 11월 9일부터의 두 번째 단계에서 공격자는 다시 돌아왔고, 11월 12일 밤 Neos CMS의 알려지지 않은 결함을 악용해 mittwald.de에 침입했다. Mittwald는 기록된 단계의 속도를 근거로 공격자가 AI 도구를 썼다고 추정하지만, The Record는 그 밖의 근거는 제시되지 않았다고 지적한다.

summary_de: |
  **Am 7. November 2026 machte der deutsche Webhoster Mittwald öffentlich, dass ein Angreifer über eine Lücke in seinem MCP-Server in die Plattform eingedrungen war, dem Dienst, über den Kunden KI-Assistenten wie Claude oder ChatGPT an das Hosting-Panel mStudio anbinden.** In einem am 25. November veröffentlichten Postmortem benannte Mittwald die Lücke als Shell Injection in einem Tool des Servers: Die Parameter `comment` und `passphrase` eines Tool-Aufrufs wurden in eine Kommandozeile eingesetzt und mit `execSync` ausgeführt, was beliebige Befehle im Container des Servers erlaubte. Der MCP-Server hält gültige Access- und Refresh-Tokens aller aktiven Nutzer; der Angreifer las diese Tokens aus, auch die von Mittwald-Mitarbeitenden, legte damit im Namen anderer SSH-User und API-Tokens an und kopierte Konfigurationsdateien und Zugangsdaten aus Projekten. Erste Tests gab es am 21. Oktober, gezielt genutzt wurde die Lücke ab dem 27. Oktober, entdeckt wurde der Angriff am 4. November; Mittwald schaltete den MCP-Server ab, widerrief alle Tokens und sperrte vom 5. bis 7. November mStudio-Login und SSH. 56 Projekte stuft das Unternehmen als kompromittiert ein und geht dort von abgeflossenen Daten aus. Betroffen waren alle, die den MCP-Server genutzt haben, sowie die Projekte, auf die ihre Konten Zugriff hatten. Mittwald gibt an, den MCP-Server zu großen Teilen mit KI-Coding-Agenten gebaut zu haben; der fehlerhafte Code stammte aus einem Testumfeld und gelangte unbemerkt in den produktiven Pfad. In einer zweiten Phase ab dem 9. November kehrte der Angreifer zurück und nutzte in der Nacht zum 12. November eine bis dahin unbekannte Lücke im CMS Neos, um in mittwald.de einzubrechen. Aus dem Tempo der protokollierten Schritte schließt Mittwald, dass der Angreifer KI-Werkzeuge eingesetzt hat; The Record merkt an, dass es dafür keine weiteren Belege nannte.

summary_fr: |
  **Le 7 novembre 2026, l'hébergeur allemand Mittwald a révélé qu'un attaquant s'était introduit dans sa plateforme par une faille de son serveur MCP, le service qui permet aux clients de relier des assistants IA comme Claude ou ChatGPT au panneau d'hébergement mStudio.** Dans un post-mortem publié le 25 novembre, Mittwald a identifié la faille comme une injection shell dans l'un des outils du serveur : les paramètres `comment` et `passphrase` d'un appel d'outil étaient insérés dans une ligne de commande exécutée avec `execSync`, ce qui donnait l'exécution de commandes arbitraires dans le conteneur du serveur. Le serveur MCP détient des jetons d'accès et de rafraîchissement valides pour chaque utilisateur actif ; l'attaquant a donc lu ces jetons, y compris ceux d'employés de Mittwald, et s'en est servi pour créer des utilisateurs SSH et des jetons d'API au nom d'autres personnes et pour copier des fichiers de configuration et des identifiants hors des projets. L'attaquant a testé la faille pour la première fois le 21 octobre, l'a exploitée à partir du 27 octobre et a été détecté le 4 novembre ; Mittwald a arrêté le serveur MCP, révoqué tous les jetons et suspendu la connexion à mStudio et l'accès SSH du 5 au 7 novembre. L'entreprise classe 56 projets comme compromis et considère que des données en sont sorties. Toutes les personnes ayant utilisé le serveur MCP sont concernées, ainsi que les projets auxquels leurs comptes avaient accès. Mittwald indique avoir construit le serveur MCP en grande partie avec des agents de codage IA et précise que le code vulnérable venait d'un contexte de test et a atteint la production sans être remarqué. Dans une seconde phase à partir du 9 novembre, l'attaquant est revenu et, dans la nuit du 12 novembre, a exploité une faille jusque-là inconnue du CMS Neos pour pénétrer mittwald.de. Mittwald déduit de la rapidité des étapes journalisées que l'attaquant a utilisé des outils d'IA ; The Record relève qu'aucune autre preuve n'a été fournie.

summary_es: |
  **El 7 de noviembre de 2026, el proveedor de hosting alemán Mittwald reveló que un atacante había entrado en su plataforma a través de un fallo en su servidor MCP, el servicio que permite a los clientes conectar asistentes de IA como Claude o ChatGPT al panel de hosting mStudio.** En un post-mortem publicado el 25 de noviembre, Mittwald identificó el fallo como una inyección de shell en una de las herramientas del servidor: los parámetros `comment` y `passphrase` de una llamada a la herramienta se insertaban en una línea de comandos y se ejecutaban con `execSync`, lo que permitía ejecutar comandos arbitrarios en el contenedor del servidor. El servidor MCP guarda tokens de acceso y de renovación válidos de todos los usuarios activos, así que el atacante leyó esos tokens, incluidos los de empleados de Mittwald, y los usó para crear usuarios SSH y tokens de API en nombre de otras personas y para copiar archivos de configuración y credenciales de los proyectos. El atacante probó el fallo por primera vez el 21 de octubre, lo explotó desde el 27 de octubre y fue detectado el 4 de noviembre; Mittwald apagó el servidor MCP, revocó todos los tokens y suspendió el inicio de sesión en mStudio y el acceso SSH del 5 al 7 de noviembre. La empresa clasifica 56 proyectos como comprometidos y da por hecho que salieron datos de ellos. Resultaron afectados todos los que habían usado el servidor MCP y los proyectos a los que sus cuentas tenían acceso. Mittwald afirma que construyó el servidor MCP en gran parte con agentes de codificación de IA y que el código vulnerable procedía de un contexto de pruebas y llegó a producción sin ser advertido. En una segunda fase desde el 9 de noviembre el atacante volvió y, en la noche del 12 de noviembre, explotó un fallo hasta entonces desconocido del CMS Neos para entrar en mittwald.de. Mittwald deduce de la velocidad de los pasos registrados que el atacante usó herramientas de IA; The Record señala que no aportó ninguna otra prueba.

sources:
  - url: https://www.mittwald.de/blog/mittwald/sicherheitsvorfall-am-mcp-server
    label: Mittwald incident post (Robert Meyer, 2026-11-07, in German)
  - url: https://www.mittwald.de/blog/mittwald/postmortem-wie-ein-angreifer-ueber-unseren-mcp-server-und-neos-eindrang
    label: Mittwald post-mortem (Martin Helmich, 2026-11-25, in German)
  - url: https://therecord.media/cyberattack-germany-ai-mittwald
    label: The Record
  - url: https://webhosting.today/2026/11/09/mittwald-traces-a-breach-of-56-customer-projects-to-its-mcp-server/
    label: webhosting.today
disputed: false
landmark: false
scan_month: 2026-11
scan_ref: "SCAN.md §13.39"
---

# German host Mittwald breached through a shell-injection flaw in its own MCP server; 56 customer projects compromised

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**On 7 November 2026 the German web host Mittwald disclosed that an attacker had broken into its platform through a flaw in its MCP server, the service that lets customers connect AI assistants such as Claude or ChatGPT to the mStudio hosting panel.** In a post-mortem published on 25 November, Mittwald identified the flaw as a shell injection in one of the server's tools: the `comment` and `passphrase` parameters of a tool call were placed into a command line and run with `execSync`, giving arbitrary command execution in the server's container. The MCP server holds valid access and refresh tokens for every active user, so the attacker read those tokens, including those of Mittwald employees, and used them to create SSH users and API tokens in other people's names and to copy configuration files and credentials out of projects. The attacker first probed the flaw on 21 October, exploited it from 27 October and was detected on 4 November; Mittwald shut the MCP server down, revoked all tokens and suspended mStudio login and SSH access from 5 to 7 November. It classified 56 projects as compromised and assumes data left them. Everyone who had used the MCP server was affected, along with projects their accounts could reach. Mittwald says it built the MCP server largely with AI coding agents and that the vulnerable code came from a test context and reached production unnoticed. In a second phase from 9 November the attacker returned, and on the night of 12 November exploited a previously unknown flaw in the Neos CMS to breach mittwald.de. Mittwald infers from the speed of the logged steps that the attacker used AI tools; The Record notes it gave no other evidence for that.

## Attack chain

```mermaid
flowchart LR
    A["Attacker registers accounts and<br/>calls a tool on Mittwald's<br/>MCP server"]:::entry
    B["Tool parameters reach execSync:<br/>shell injection gives commands<br/>in the server's container"]:::step
    C["Attacker reads the stored access<br/>and refresh tokens of all<br/>active MCP users"]:::step
    D["SSH users and API tokens created<br/>in others' names; config and<br/>credentials copied from 56 projects"]:::impact
    A --> B --> C --> D
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What the MCP server was for.** Mittwald's MCP server let a customer connect the mStudio panel to an AI assistant and then create projects, install apps or manage SSH access by chat. A customer signed in to the MCP server with OAuth2; the server received an access token and a refresh token for the Mittwald API and kept both in a session store, and when the assistant called a tool the server used that token to talk to the API in the customer's name. Some tools were wrappers around Mittwald's command-line client. As the post-mortem puts it, the consequence that mattered is that the MCP server holds the valid tokens of all active users at all times.

**The flaw.** One tool built a command line from the `comment` and `passphrase` parameters of the tool call using a template string and ran it with `execSync`, which hands the whole string to a shell. Whoever calls the tool chooses those parameters freely, so a command substitution in the comment ran before the intended `ssh-keygen` command started. The post-mortem says the temporary file name `mcp-eval-key` suggests the code came from a test context and moved into the production path unnoticed, and that no static analysis was configured for the project to flag `execSync` with interpolated variables.

**Mittwald's account of why it shipped.** The company says it built the MCP server largely with AI coding agents, a deliberate choice to gain early experience with agentic workflows in a fast-moving area. Its review practice and guardrails for agent-written code were less developed then than now; agent-written code usually looks plausible, is cleanly commented and follows known patterns, which tempts reviewers to check function rather than whether each line is safe in context. Mittwald adds that the same mistake happens to humans and that a thorough review should have caught it. It now applies binding review rules to agent-written code.

**Timeline of the first phase.** First tests on 21 October 2026, the evening much of the industry was occupied with the PHP2Shell vulnerability. From 23 October the attacker moved on the platform as a regular user, registering test accounts and trying simple injections. On 27 October at 14:58 the attacker registered another account and at 15:03 exploited the MCP flaw. Mittwald noticed unusual behaviour on the morning of 4 November, blocked the attacker's first account at 11:11, identified the MCP server as the entry point and shut it down. On 5 November it disabled new registrations and then mStudio login and SSH access to customer projects; both came back on 7 November. Outside forensic specialists were engaged and the authorities informed.

**What was taken and who was affected.** With the tokens, the attacker created SSH users and API tokens in other people's names in mStudio and copied configuration files and credentials out of projects. Mittwald says everyone who used the MCP server was affected, together with the projects their accounts could access, even where the project owner never used the MCP server. In 56 of those projects the attacker demonstrably acted; Mittwald classed them as compromised, assumes data left them, locked them and examined them forensically. An attempt in the first phase to reach Mittwald's internal systems through a further flaw in extension webhooks failed.

**The second phase.** From 9 November the attacker looked for new ways in, including throwaway mStudio accounts, hosting accounts managed through the older customer centre and vulnerable plugins in customer websites. On the night of 12 November the attacker exploited a zero-day in the Neos content management system that runs mittwald.de: the underlying Flow framework processed file uploads before checking that the requester was logged in, and the extension blocklist let `.phar` files through, so a web shell could be uploaded. The attacker read the site's configuration and database. Mittwald noticed shortly after the web shell's first call, suspended logins again on 12 and 13 November, and says a Neos security update has been available since 13 November. The MCP server remains offline.

**AI use by the attacker is an inference.** Mittwald writes that only seconds lay between individual steps and many actions ran in parallel, and that it therefore assumes the attacker used AI tools. The Record reports that Mittwald provided no other evidence of AI involvement and did not answer when asked how it distinguishes AI tools from conventional scripts. The record's `ai_involvement: confirmed` refers to the attack surface, which Mittwald itself identifies as its MCP server; it does not rest on the claim about the attacker's tooling.

**How it is graded.** `incident`: a confirmed breach disclosed by the affected company, with customer projects compromised. `MCP` because the flaw is in a tool of the MCP server itself; `CRED` because what the attacker took from the server were the users' tokens; `EXFIL` because configuration files and credentials were copied out of projects and Mittwald assumes data left the 56 compromised ones. `high`: a confirmed breach of customer environments at a hosting provider through its agent-facing interface, with a bounded number of projects and no evidence that internal systems were reached.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Mittwald incident post (Robert Meyer, 2026-11-07, in German) | <https://www.mittwald.de/blog/mittwald/sicherheitsvorfall-am-mcp-server> |
| 2 | Mittwald post-mortem (Martin Helmich, 2026-11-25, in German) | <https://www.mittwald.de/blog/mittwald/postmortem-wie-ein-angreifer-ueber-unseren-mcp-server-und-neos-eindrang> |
| 3 | The Record | <https://therecord.media/cyberattack-germany-ai-mittwald> |
| 4 | webhosting.today | <https://webhosting.today/2026/11/09/mittwald-traces-a-breach-of-56-customer-projects-to-its-mcp-server/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-11-07` (raw: 2026-11-07 (Mittwald incident post; flaw first probed 2026-10-21, exploited from 2026-10-27, detected 2026-11-04; post-mortem published 2026-11-25), precision `day`) |
| Kind | Real incident `incident` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) [`CRED`](../../taxonomy/types.md#cred) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **High** `high` |
| Confidence | **A** — Mittwald's own incident post and detailed post-mortem; The Record and webhosting.today report from them |
| Real harm | Yes — 56 customer projects classed as compromised; user tokens read and abused; configuration files and credentials copied |
| AI involvement | Confirmed `confirmed` — the entry point is Mittwald's MCP server, by its own account; the attacker's use of AI tools is Mittwald's inference from timing and is not confirmed |
| Region | [Europe](../../regions/eu.md) |
| Archive ID | `2026-11-07-mittwald-mcp-server-breach` |

<sub>**Why this classification:** A breach confirmed by the affected company, entered through a flaw in a tool of its own MCP server (`MCP`), in which the tokens the server held for its users were read and abused (`CRED`) and project data copied (`EXFIL`), hence `incident` and `real_harm: true`. `high`: customer environments at a hosting provider compromised through the agent-facing interface, bounded at 56 projects. `confidence: A` for a first-hand disclosure with a technical post-mortem. The claim that the attacker used AI is flagged as an inference; the classification does not depend on it. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-11-10` [Chainstack: an ARTEX-driven intrusion used an unauthenticated internal MCP tool server with cluster-admin rights](2026-11-10-chainstack-artex-unauthenticated-mcp-server.md)<br>  <sub>The same weeks, the same lesson: an MCP server holding broad privileges became the attacker's lever</sub>
- `2026-10-19` [OpenCode: a malicious MCP server runs code on the developer's machine during OAuth sign-in](../2026-10/2026-10-19-opencode-mcp-oauth-rce.md)<br>  <sub>Another MCP flaw on the OAuth and token path, from the client side</sub>
- `2026-11-05` [AgentScope: MCP stdio command injection (CVE-2026-123022)](2026-11-05-agentscope-mcp-command-injection-cve-2026-123022.md)<br>  <sub>The same bug class, command injection through an MCP path, disclosed two days earlier as a CVE</sub>

---

[← 2026-11 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-11/2026-11-07-mittwald-mcp-server-breach.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
