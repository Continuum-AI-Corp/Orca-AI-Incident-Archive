---
id: 2026-09-21-meta-muse-not-a-mused-dictation-hijack
title: "Not-a-Mused: an undocumented Muse setting redirects dictation and hands the agent's token to an attacker"
title_zh: "Not-a-Mused：一个未公开的 Muse 设置项把语音输入重定向，并把 agent 的令牌交给攻击者"
title_ja: "Not-a-Mused：未公開の Muse 設定が音声入力を奪い、エージェントのトークンを攻撃者に渡す"
title_ko: "Not-a-Mused: 문서화되지 않은 Muse 설정이 음성 입력을 리다이렉트하고 에이전트 토큰을 공격자에게 넘긴다"
title_de: "Not-a-Mused: Eine undokumentierte Muse-Einstellung lenkt Diktate um und gibt das Agenten-Token an einen Angreifer"
title_fr: "Not-a-Mused : un réglage non documenté de Muse redirige la dictée et livre le jeton de l'agent à un attaquant"
title_es: "Not-a-Mused: un ajuste no documentado de Muse redirige el dictado y entrega el token del agente al atacante"
date: 2026-09-21
date_raw: "2026-09-21 (Wardle PoC) / 2026-09-22 (The Hacker News)"
date_precision: day

kind: vulnerability
type: [INFRA, CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [US]

summary: |
  **Patrick Wardle shows that a hidden preference in Meta's Muse assistant for macOS — `endo_voyager_dictation_endpoint`, stored in the app's preferences and writable by any process running as the logged-in user, with no extra permissions — decides where dictation is sent.** Point it at an attacker's address and Muse's microphone input and its transcript leave the device: the attacker can *"read what the user dictated, add extra instructions that Muse trusts and acts on, and capture a token that signs in to the user's Muse account"* — then read the account's chat history and drive the assistant on **any device where that account is signed in** (Wardle made the iPhone app report its location, run a Bluetooth scan and list smart-home commands). Muse, Meta's personal agent launched in the US this month, holds whatever access the user granted across files, email, messages, calendar and shopping; Wardle calls it *"trivial to turn Muse into the ultimate backdoor."* It cannot break into a Mac on its own — code execution as the user, or a ClickFix trick, is required — and it does not defeat macOS app isolation or Meta's cloud separation. Wardle went public without pre-notifying Meta; Meta has since pushed what he calls a "fix", with no advisory

summary_zh: |
  **Patrick Wardle 展示：Meta 面向 macOS 的 Muse 助手里有一个隐藏配置项——`endo_voyager_dictation_endpoint`——它决定语音输入被发送到哪里，存于应用偏好设置中，任何以登录用户身份运行的进程都可改写，且无需额外权限。** 把它指向攻击者的地址，Muse 的麦克风输入与转写文本就离开设备：攻击者可以*「读取用户的语音内容、追加 Muse 信任并执行的额外指令，并捕获用于登录用户 Muse 账户的令牌」*——随后读取该账户的聊天记录，并在**该账户登录的任何设备**上驱动这个助手（Wardle 让 iPhone 端上报了精确位置、执行蓝牙扫描并列出可下发的智能家居指令）。Muse 是 Meta 本月在美国推出的个人 agent，持有用户授予的跨文件、邮件、消息、日历与购物的访问权限；Wardle 称把它*「变成终极后门易如反掌」*。它无法自行攻入一台 Mac——需要先以用户身份执行代码，或用 ClickFix 手法——也没有攻破 macOS 的应用隔离或 Meta 的云端隔离。Wardle 未事先通知 Meta 就公开；Meta 随后推送了他所称的「修复」，但未发布公告

summary_ja: |
  **Patrick Wardle氏は、macOS版Meta「Muse」に隠し設定 `endo_voyager_dictation_endpoint` があることを示した。この設定は音声入力の送信先を決めるもので、アプリの環境設定に格納され、追加権限なしでログインユーザーとして動く任意のプロセスから書き換えられる。** 攻撃者のアドレスを指定すると、Museのマイク入力と文字起こしが端末外へ流出する。攻撃者は*「ユーザーの発話内容を読み、Museが信じて実行する追加指示を差し込み、ユーザーのMuseアカウントにサインインするトークンを取得できる」*——その後アカウントのチャット履歴を読み、**そのアカウントがサインインしている任意の端末**でそのエージェントを操作できる（Wardle氏はiPhoneアプリに正確な位置を報告させ、Bluetoothスキャンを実行させ、送れるスマートホーム指令を列挙させた）。MuseはMetaが今月米国で投入したパーソナルエージェントで、ユーザーが許可したファイル・メール・メッセージ・カレンダー・買い物へのアクセス権を持つ。Wardle氏は*「Museを究極のバックドアに変えるのはたやすい」*と述べる。単独でMacに侵入することはできず、ユーザー権限でのコード実行かClickFixが必要。macOSのアプリ分離やMetaのクラウド分離は破っていない。Wardle氏は事前通知せず公開し、Metaはその後「修正」を出したが勧告は出していない

summary_ko: |
  **Patrick Wardle은 macOS용 Meta Muse에 숨겨진 설정 `endo_voyager_dictation_endpoint` 가 있음을 보여줬다. 이 설정은 음성 입력이 전송될 위치를 결정하며 앱 환경설정에 저장되고, 추가 권한 없이 로그인 사용자로 동작하는 모든 프로세스가 변경할 수 있다.** 이를 공격자 주소로 바꾸면 Muse의 마이크 입력과 전사 텍스트가 기기를 떠난다. 공격자는 *"사용자가 말한 내용을 읽고, Muse가 신뢰하고 실행하는 추가 지시를 덧붙이며, 사용자의 Muse 계정에 로그인하는 토큰을 가로챌 수 있다"* — 이후 계정의 대화 기록을 읽고 **그 계정이 로그인된 모든 기기**에서 에이전트를 조종할 수 있다(Wardle은 iPhone 앱에 정확한 위치를 보고하게 하고, 블루투스 스캔을 실행하게 하고, 내릴 수 있는 스마트홈 명령을 나열하게 했다). Muse는 Meta가 이번 달 미국에 출시한 개인 에이전트로, 사용자가 허용한 파일·메일·메시지·캘린더·쇼핑 접근 권한을 가진다. Wardle은 *"Muse를 궁극의 백도어로 바꾸는 것은trivial(아주 쉽다)"*고 말한다. 단독으로 Mac에 침입할 수는 없고 사용자 권한 코드 실행이나 ClickFix가 필요하다. macOS 앱 격리나 Meta의 클라우드 격리를 깨지도 않았다. Wardle은 사전 통보 없이 공개했고 Meta는 이후 "수정"을 배포했으나 권고문은 없다

summary_de: |
  **Patrick Wardle zeigt, dass eine versteckte Einstellung in Metas Muse-Assistent für macOS — `endo_voyager_dictation_endpoint`, in den App-Preferences gespeichert und von jedem Prozess des angemeldeten Benutzers ohne zusätzliche Rechte schreibbar — bestimmt, wohin Diktate gesendet werden.** Zeigt sie auf die Adresse eines Angreifers, verlassen Mikrofon-Eingabe und Transkript das Gerät: Der Angreifer kann *„lesen, was der Benutzer diktiert hat, zusätzliche Anweisungen hinzufügen, denen Muse vertraut und die es ausführt, und ein Token abgreifen, das sich beim Muse-Konto des Benutzers anmeldet"* — und damit den Chatverlauf lesen und den Assistenten auf **jedem Gerät steuern, auf dem das Konto angemeldet ist** (Wardle ließ die iPhone-App ihren Standort melden, einen Bluetooth-Scan ausführen und Smart-Home-Befehle auflisten). Muse, Metas in diesem Monat in den USA gestarteter persönlicher Agent, hält alle Zugriffe, die der Nutzer über Dateien, E-Mail, Nachrichten, Kalender und Shopping gewährt hat; Wardle nennt es *„trivial, Muse in die ultimative Hintertür zu verwandeln."* Es kann einen Mac nicht von sich aus kompromittieren — Codeausführung als Benutzer oder ein ClickFix-Trick ist nötig — und bricht weder die macOS-App-Isolation noch Metas Cloud-Trennung. Wardle veröffentlichte ohne Vorabinformation an Meta; Meta hat seither einen von ihm so genannten „Fix" ausgeliefert, ohne Advisory

summary_fr: |
  **Patrick Wardle montre qu'un réglage caché de l'assistant Muse de Meta pour macOS — `endo_voyager_dictation_endpoint`, stocké dans les préférences de l'app et modifiable par tout processus s'exécutant comme l'utilisateur connecté, sans permission supplémentaire — décide où la dictée est envoyée.** En le pointant vers une adresse contrôlée par l'attaquant, l'entrée micro et la transcription quittent l'appareil : l'attaquant peut *« lire ce que l'utilisateur a dicté, ajouter des instructions supplémentaires auxquelles Muse fait confiance et qu'il exécute, et capturer un jeton qui ouvre le compte Muse de l'utilisateur »* — puis lire l'historique des conversations et piloter l'assistant sur **tout appareil où ce compte est connecté** (Wardle a fait reporter sa position à l'app iPhone, lancer un scan Bluetooth et lister les commandes domotiques disponibles). Muse, l'agent personnel lancé par Meta aux États-Unis ce mois-ci, détient tous les accès accordés par l'utilisateur sur les fichiers, les e-mails, les messages, le calendrier et les achats ; Wardle parle d'une chose *« triviale : transformer Muse en backdoor ultime »*. Il ne peut pas pénétrer un Mac de lui-même — une exécution de code en tant qu'utilisateur, ou une ruse ClickFix, est nécessaire — et ne casse ni l'isolation des apps macOS ni la séparation cloud de Meta. Wardle a publié sans prévenir Meta ; Meta a depuis poussé ce qu'il appelle un « correctif », sans avis de sécurité

summary_es: |
  **Patrick Wardle demuestra que un ajuste oculto del asistente Muse de Meta para macOS — `endo_voyager_dictation_endpoint`, guardado en las preferencias de la app y modificable por cualquier proceso que se ejecute como el usuario sin permisos adicionales — decide a dónde se envía el dictado.** Al apuntarlo a una dirección del atacante, la entrada del micrófono y la transcripción salen del dispositivo: el atacante puede *«leer lo que el usuario dictó, añadir instrucciones adicionales en las que Muse confía y ejecuta, y capturar un token que inicia sesión en la cuenta Muse del usuario»* — y luego leer el historial de chat y manejar el asistente en **cualquier dispositivo donde esa cuenta esté abierta** (Wardle hizo que la app del iPhone informara de su ubicación, ejecutara un escaneo Bluetooth y listara los comandos de hogar inteligente disponibles). Muse, el agente personal lanzado por Meta en EE. UU. este mes, tiene todos los accesos que el usuario le concedió sobre archivos, correo, mensajes, calendario y compras; Wardle lo califica de *«trivial: convertir Muse en la puerta trasera definitiva»*. No puede entrar en un Mac por sí solo — hace falta ejecución de código como el usuario o un truco ClickFix — y no rompe ni el aislamiento de apps de macOS ni la separación en la nube de Meta. Wardle publicó sin avisar antes a Meta; Meta lanzó después lo que él llama un «arreglo», sin aviso de seguridad

sources:
  - url: https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html
    label: The Hacker News
  - url: https://github.com/pwardle/not-a-mused
    label: Patrick Wardle proof of concept
  - url: https://finance.sina.com.cn/tech/digi/2026-09-25/doc-iniszmmz7778318.shtml
    label: IT Home (Chinese coverage)

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# Not-a-Mused: an undocumented Muse setting redirects dictation and hands the agent's token to an attacker

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**Patrick Wardle shows that a hidden preference in Meta's Muse assistant for macOS — `endo_voyager_dictation_endpoint`, stored in the app's preferences and writable by any process running as the logged-in user, with no extra permissions — decides where dictation is sent.** Point it at an attacker's address and Muse's microphone input and its transcript leave the device: the attacker can *"read what the user dictated, add extra instructions that Muse trusts and acts on, and capture a token that signs in to the user's Muse account"* — then read the account's chat history and drive the assistant on **any device where that account is signed in** (Wardle made the iPhone app report its location, run a Bluetooth scan and list smart-home commands). Muse, Meta's personal agent launched in the US this month, holds whatever access the user granted across files, email, messages, calendar and shopping; Wardle calls it *"trivial to turn Muse into the ultimate backdoor."* It cannot break into a Mac on its own — code execution as the user, or a ClickFix trick, is required — and it does not defeat macOS app isolation or Meta's cloud separation. Wardle went public without pre-notifying Meta; Meta has since pushed what he calls a "fix", with no advisory.

## Attack chain

```mermaid
flowchart LR
    E["Attacker already runs code as the user<br/>(or a ClickFix trick gets one command run)"]:::entry
    S1["Writes the undocumented preference<br/>endo_voyager_dictation_endpoint"]:::step
    S2["Muse sends audio and transcript<br/>to the attacker's endpoint"]:::step
    I["Read dictation, inject trusted instructions,<br/>capture the Muse token — control on any device"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The finding.** Wardle published a proof of concept, *not-a-mused*, on 21 September 2026. The setting is *"undocumented and decides where Muse sends dictation"*; it is stored in the Mac app's preferences under `endo_voyager_dictation_endpoint`, and *"any program running as the logged-in user can point it at an address the attacker controls, without needing extra permissions."* After that, *"the dictation no longer goes to Meta. When the user speaks a prompt, the audio and the text go to a small program the attacker is running on the same Mac."* From there he demonstrated three things: *"read what the user dictated, add extra instructions that Muse trusts and acts on, and capture a token that signs in to the user's Muse account, then use it to read the account's chat history and control the assistant directly."*

**Why the agent is the prize.** macOS normally prevents one app from reading another app's files, microphone, camera or saved logins, so ordinary malware is limited. *"An attacker who can quietly steer Muse instead gets everything the user allowed the app to do"* — and because a Muse account can be signed in on several devices, an attacker holding the token can issue orders from anywhere: Wardle *"used it to direct the Muse app on his own iPhone to report its exact location, run a Bluetooth scan of nearby devices, and list the smart-home commands it could send."* In his tests the assistant only drafted messages rather than sending them. Security software may not notice, because the commands come from Muse — *"a normal signed app."*

**What it does not do, and how it was disclosed.** It does not defeat macOS app isolation: *"Muse sends its token along with the redirected dictation, and the attack works by getting Muse to act with access it already has."* Nor does it show that Meta's cloud isolation was broken; the flaw is in the Mac app. It *"cannot break into a Mac on its own"* — it needs code execution as the logged-in user, reachable through a ClickFix trick. Wardle deliberately did not report to Meta first, choosing full disclosure; Meta has since pushed what he calls a "fix", which The Hacker News *"could not confirm"*, and has published no advisory. Wardle says he has found further flaws in AI assistants, to be presented at Objective by the Sea in November.

**Context and grading.** Muse launched in the US this month with wide user-granted reach across files, email, messages, calendar, shopping and smart-home apps — which is exactly why the archive treats the **agent client** as agent infrastructure: the assistant concentrates permissions, so anything that can steer the client inherits them. Recorded `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`: a controlled demonstration on a single machine that requires a prior foothold and has no confirmed victims, so it stays below the `high` band. Confidence **A**: the researcher's published PoC plus independent reporting in English and Chinese.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | The Hacker News (22 Sep 2026) | <https://thehackernews.com/2026/09/one-hidden-meta-muse-setting-could-let.html> |
| 2 | Patrick Wardle — "not-a-mused" proof of concept (21 Sep 2026) | <https://github.com/pwardle/not-a-mused> |
| 3 | IT Home (Chinese coverage, 25 Sep 2026) | <https://finance.sina.com.cn/tech/digi/2026-09-25/doc-iniszmmz7778318.shtml> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-21` (raw: PoC 2026-09-21 / The Hacker News 2026-09-22, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **Medium** `medium` |
| Confidence | **A** — researcher's published proof of concept plus independent reporting |
| Real harm | No — a demonstration; no confirmed victims |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) — Muse launched in the US |
| Archive ID | `2026-09-21-meta-muse-not-a-mused-dictation-hijack` |

<sub>**Why this classification:** the exposed asset is the agent's own client-side runtime and its configuration surface (`INFRA`), and what is taken is a signing token plus the ability to issue trusted instructions (`CRED`). `vulnerability` with `real_harm: false` because it is a PoC with no known exploitation. `medium` rather than `high` under the archive's ladder: a controlled, single-machine demonstration that additionally requires the attacker to already run code as the user — `high` would need confirmed damage, a CVSS 9+ flaw, or a capability demonstration that does not presuppose a foothold. Dated to the PoC release (21 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-09-16` [BragJack: one browser extension hijacks the AI agents in five major browsers](2026-09-16-bragjack-browser-agents.md)<br>  <sub>Same shape of problem on the browser surface: steer the client, inherit its permissions</sub>
- `2026-09-15` [Codex sandbox escapes](2026-09-15-codex-sandbox-escapes.md)<br>  <sub>The other side of the boundary question — what the agent is allowed to reach</sub>
- `2026-09-18` [Zhipu's ZCode agent silently uploaded whole repositories](2026-09-18-zcode-silent-upload.md)<br>  <sub>When the agent client itself is the leak path</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-21-meta-muse-not-a-mused-dictation-hijack.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
