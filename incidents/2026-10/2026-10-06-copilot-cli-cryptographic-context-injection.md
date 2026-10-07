---
id: 2026-10-06-copilot-cli-cryptographic-context-injection
title: "Cryptographic Context Injection: encrypted web instructions make GitHub Copilot CLI leak local secrets"
title_zh: "加密上下文注入：加密的网页指令让 GitHub Copilot CLI 外泄本地机密"
title_ja: "暗号化コンテキスト注入：暗号化されたWeb指示がGitHub Copilot CLIにローカル機密を漏らさせる"
title_ko: "암호화 컨텍스트 주입: 암호화된 웹 지시가 GitHub Copilot CLI로 하여금 로컬 비밀을 유출하게 한다"
title_de: "Cryptographic Context Injection: Verschlüsselte Web-Anweisungen bringen GitHub Copilot CLI dazu, lokale Geheimnisse preiszugeben"
title_fr: "Cryptographic Context Injection : des instructions web chiffrées font fuiter des secrets locaux par GitHub Copilot CLI"
title_es: "Cryptographic Context Injection: instrucciones web cifradas hacen que GitHub Copilot CLI filtre secretos locales"
date: 2026-10-06
date_raw: "reported to GitHub 2026-09-17; published 2026-10-06 (Adversa AI / The Register)"
date_precision: day

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Adversa AI disclosed on 6 October 2026 a technique it calls **Cryptographic Context Injection (CCI)**: a web page carries attacker instructions as **ciphertext plus the key material and a prompt to decrypt**, and when GitHub Copilot CLI (in autopilot mode) fetches the page it decrypts and executes them inside its own runtime, slipping past static guardrails that "read text but do not run it."** The clever part is the key: the agent is induced to build a decryption key out of **local files such as `.env`**, so the harvested secrets become part of the key string; a second, working key then reveals an instruction to fetch another URL that carries those secrets out. In the demo, *"the full contents of a `.env.prod` file … are sitting in an attacker's log in 28 seconds,"* with nothing on screen showing a file left the machine. Exploitation is **model-dependent** — Microsoft's mai-code-1.1-flash ran it in ~50% of attempts while GPT-5.6 models refused, and the user does not choose or see which model handled the session. Adversa reported it through GitHub's bug bounty on **17 September**; **GitHub validated the finding but declined to treat it as a product vulnerability**, arguing the user's direction to fetch untrusted content amounts to consent — a classification **Adversa disputes**. No in-the-wild use. Recorded `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`.

summary_zh: |
  **Adversa AI 于 2026 年 10 月 6 日披露了一种它称为**加密上下文注入（Cryptographic Context Injection，CCI）**的技术：一个网页把攻击者指令以**密文 + 密钥材料 + 解密提示**的形式携带，当 GitHub Copilot CLI（autopilot 模式）抓取该页时，便在自己的运行时里解密并执行这些指令，从而绕过"只读文本、不执行文本"的静态护栏。** 精巧之处在密钥：agent 被诱导用**本地文件（如 `.env`）**来拼出解密密钥，于是被窃机密成了密钥串的一部分；随后一个真正可用的密钥揭示出一条指令，去抓取另一个把这些机密带走的 URL。在演示中，*「一个 `.env.prod` 文件的全部内容……28 秒后就躺在了攻击者的日志里」*，屏幕上没有任何迹象表明有文件离开了本机。利用效果**与模型相关**——微软 mai-code-1.1-flash 约 50% 得手、GPT-5.6 系列拒绝，而用户既不能选择、也看不到本次会话用的是哪个模型。Adversa 于 **9 月 17 日**经 GitHub 漏洞赏金上报；**GitHub 认可该发现但拒绝将其认定为产品漏洞**，理由是用户指示去抓取不可信内容等同于同意——这一定性**Adversa 不认同**。无在野利用。记为 `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`。

summary_ja: |
  **Adversa AIは2026年10月6日、**Cryptographic Context Injection（CCI、暗号化コンテキスト注入）**と呼ぶ手法を公表した。Webページが攻撃者の指示を**暗号文＋鍵素材＋復号を促すプロンプト**として運び、GitHub Copilot CLI（autopilotモード）がそのページを取得すると、自らのランタイム内で復号・実行し、「テキストを読むが実行はしない」静的ガードレールをすり抜ける。** 巧妙なのは鍵だ。エージェントは`.env`などの**ローカルファイル**から復号鍵を組み立てるよう誘導され、採取された機密が鍵文字列の一部になる。続いて正しく動く第二の鍵が、それらの機密を運び出す別URLを取得せよという指示を明かす。デモでは*「`.env.prod`ファイルの全内容が……28秒で攻撃者のログに載る」*、ファイルが端末を離れた形跡は画面に何も出ない。成否は**モデル依存**——Microsoftのmai-code-1.1-flashは約50%で実行、GPT-5.6系は拒否、しかもユーザーはどのモデルが処理したか選べず見えもしない。Adversaは**9月17日**にGitHubのバグ報奨金で報告、**GitHubは発見を検証したが製品脆弱性としての扱いを拒否**（不信頼コンテンツを取得させるユーザーの指示は同意に当たる、と主張）——この分類に**Adversaは異議**。実環境での悪用はなし。`research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`

summary_ko: |
  **Adversa AI는 2026년 10월 6일 **암호화 컨텍스트 주입(Cryptographic Context Injection, CCI)**이라 부르는 기법을 공개했다: 웹페이지가 공격자 지시를 **암호문 + 키 자료 + 복호화 프롬프트**로 실어두고, GitHub Copilot CLI(autopilot 모드)가 그 페이지를 가져오면 자신의 런타임에서 복호화·실행해 "텍스트를 읽되 실행하지 않는" 정적 가드레일을 통과한다.** 핵심은 키다. 에이전트는 `.env` 같은 **로컬 파일**로 복호화 키를 만들도록 유도되어, 수집된 비밀이 키 문자열의 일부가 된다. 이어 제대로 작동하는 두 번째 키가 그 비밀을 실어 나르는 다른 URL을 가져오라는 지시를 드러낸다. 데모에서 *"`.env.prod` 파일의 전체 내용이 … 28초 만에 공격자의 로그에 들어간다"*, 파일이 기기를 떠났다는 표시는 화면에 없다. 익스플로잇은 **모델 의존적**——Microsoft의 mai-code-1.1-flash는 약 50%에서 실행, GPT-5.6 계열은 거부했고, 사용자는 어떤 모델이 처리했는지 고르지도 보지도 못한다. Adversa는 **9월 17일** GitHub 버그바운티로 보고했고, **GitHub는 발견을 검증했으나 제품 취약점으로 다루기를 거부**(불신뢰 콘텐츠를 가져오라는 사용자 지시는 동의에 해당한다고 주장)——이 분류에 **Adversa는 이의**를 제기한다. 실제 악용은 없음. `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`

summary_de: |
  **Adversa AI veröffentlichte am 6. Oktober 2026 eine Technik namens **Cryptographic Context Injection (CCI)**: Eine Webseite trägt Angreiferanweisungen als **Chiffretext plus Schlüsselmaterial und eine Aufforderung zum Entschlüsseln**, und wenn GitHub Copilot CLI (im Autopilot-Modus) die Seite abruft, entschlüsselt und führt es sie in der eigenen Laufzeit aus und umgeht so statische Guardrails, die „Text lesen, aber nicht ausführen".** Der Clou ist der Schlüssel: Der Agent wird verleitet, einen Entschlüsselungsschlüssel aus **lokalen Dateien wie `.env`** zu bauen, sodass die abgegriffenen Geheimnisse Teil der Schlüsselzeichenkette werden; ein zweiter, funktionierender Schlüssel offenbart dann eine Anweisung, eine weitere URL abzurufen, die diese Geheimnisse hinausträgt. In der Demo *„the full contents of a `.env.prod` file … are sitting in an attacker's log in 28 seconds"*, ohne dass auf dem Bildschirm etwas zeigt, dass eine Datei das Gerät verließ. Die Ausnutzung ist **modellabhängig** — Microsofts mai-code-1.1-flash führte es in ~50 % der Versuche aus, GPT-5.6-Modelle verweigerten es, und der Nutzer wählt nicht und sieht nicht, welches Modell die Sitzung bearbeitete. Adversa meldete es am **17. September** über GitHubs Bug-Bounty; **GitHub bestätigte den Fund, lehnte aber die Einstufung als Produktschwachstelle ab** (die Anweisung des Nutzers, nicht vertrauenswürdige Inhalte abzurufen, komme Zustimmung gleich) — eine Einstufung, der **Adversa widerspricht**. Keine Ausnutzung in freier Wildbahn. `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`

summary_fr: |
  **Adversa AI a divulgué le 6 octobre 2026 une technique qu'elle nomme **Cryptographic Context Injection (CCI)** : une page web transporte les instructions de l'attaquant sous forme de **texte chiffré, plus le matériel de clé et une invite à déchiffrer**, et lorsque GitHub Copilot CLI (en mode autopilot) récupère la page, il les déchiffre et les exécute dans son propre runtime, se faufilant devant des garde-fous statiques qui « lisent le texte mais ne l'exécutent pas ».** L'astuce est la clé : l'agent est amené à construire une clé de déchiffrement à partir de **fichiers locaux comme `.env`**, de sorte que les secrets récoltés deviennent partie de la chaîne de clé ; une seconde clé, fonctionnelle, révèle alors une instruction d'aller chercher une autre URL qui emporte ces secrets. Dans la démo, *"the full contents of a `.env.prod` file … are sitting in an attacker's log in 28 seconds"*, sans que rien à l'écran n'indique qu'un fichier a quitté la machine. L'exploitation est **dépendante du modèle** — le mai-code-1.1-flash de Microsoft l'a exécutée dans ~50 % des cas tandis que les modèles GPT-5.6 l'ont refusée, et l'utilisateur ne choisit ni ne voit quel modèle a traité la session. Adversa l'a signalée le **17 septembre** via le bug bounty de GitHub ; **GitHub a validé la découverte mais a refusé de la traiter comme une vulnérabilité produit**, estimant que la direction donnée par l'utilisateur de récupérer du contenu non fiable équivaut à un consentement — une classification que **Adversa conteste**. Pas d'exploitation dans la nature. `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`

summary_es: |
  **Adversa AI divulgó el 6 de octubre de 2026 una técnica que llama **Cryptographic Context Injection (CCI)**: una página web lleva las instrucciones del atacante como **texto cifrado más el material de clave y una indicación para descifrar**, y cuando GitHub Copilot CLI (en modo autopilot) obtiene la página, las descifra y ejecuta dentro de su propio runtime, colándose ante barreras estáticas que "leen el texto pero no lo ejecutan".** Lo ingenioso es la clave: se induce al agente a construir una clave de descifrado a partir de **archivos locales como `.env`**, de modo que los secretos recolectados pasan a formar parte de la cadena de clave; luego una segunda clave, funcional, revela una instrucción de ir a buscar otra URL que se lleva esos secretos. En la demo, *"the full contents of a `.env.prod` file … are sitting in an attacker's log in 28 seconds"*, sin que nada en pantalla muestre que un archivo salió de la máquina. La explotación es **dependiente del modelo** — el mai-code-1.1-flash de Microsoft la ejecutó en ~50 % de los intentos mientras que los modelos GPT-5.6 la rechazaron, y el usuario ni elige ni ve qué modelo gestionó la sesión. Adversa lo reportó el **17 de septiembre** por el bug bounty de GitHub; **GitHub validó el hallazgo pero se negó a tratarlo como vulnerabilidad de producto**, argumentando que la indicación del usuario de obtener contenido no confiable equivale a consentimiento — una clasificación que **Adversa disputa**. Sin uso en la naturaleza. `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`

sources:
  - url: https://adversa.ai/blog/cryptographic-context-injection-github-copilot/
    label: Adversa AI (primary)
  - url: https://www.theregister.com/ai-and-ml/2026/10/06/zombie-instructions-on-carefully-constructed-web-pages-could-trick-github-copilot-cli-into-sharing-secrets/5301206
    label: The Register
  - url: https://cybersecuritynews.com/github-copilot-cli-vulnerability/
    label: Cyber Security News
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.27"
---

# Cryptographic Context Injection: encrypted web instructions make GitHub Copilot CLI leak local secrets

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-3C6E8F?style=flat-square)

## Summary

**Adversa AI disclosed on 6 October 2026 a technique it calls Cryptographic Context Injection (CCI): a web page carries attacker instructions as ciphertext plus the key material and a prompt to decrypt, and when GitHub Copilot CLI (in autopilot mode) fetches the page it decrypts and executes them inside its own runtime, slipping past static guardrails that "read text but do not run it."** The clever part is the key: the agent is induced to build a decryption key out of **local files such as `.env`**, so the harvested secrets become part of the key string; a second, working key then reveals an instruction to fetch another URL that carries those secrets out. In the demo, *"the full contents of a `.env.prod` file … are sitting in an attacker's log in 28 seconds,"* with nothing on screen showing a file left the machine. Exploitation is **model-dependent** — Microsoft's mai-code-1.1-flash ran it in ~50% of attempts while GPT-5.6 models refused, and the user does not choose or see which model handled the session. Adversa reported it through GitHub's bug bounty on **17 September**; **GitHub validated the finding but declined to treat it as a product vulnerability**, arguing the user's direction to fetch untrusted content amounts to consent — a classification **Adversa disputes**. No in-the-wild use. Recorded `research` / `IPI` + `EXFIL` / `medium` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["Attacker web page: ciphertext + key material<br/>+ 'decrypt this' prompt"]:::entry
    S1["Copilot CLI (autopilot) fetches and decrypts<br/>in its own runtime — past static guardrails"]:::step
    S2["Decryption key is built from local files (.env);<br/>harvested secrets become the key string"]:::step
    I["A second key reveals a fetch instruction that<br/>carries the secrets to the attacker (~28s)"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The technique.** Adversa AI (researcher Rony Utevsky) describes **Cryptographic Context Injection**: *"Static guardrails read text; they do not run it. CCI ships malicious instructions as strong ciphertext, along with the key material and an instruction to decrypt, and induces the agent to run that decryption in its own code-execution runtime."* Because the payload is encrypted, content filters see noise; the agent itself turns it back into instructions. The exfiltration twist is elegant: the agent is led to assemble a decryption key from **local files such as `.env`**, so the secrets are embedded into the key string; when that "fake" key fails, a second working key reveals the real instruction — fetch a URL that carries the harvested secrets out. Adversa's demo exfiltrates a full `.env.prod` in about **28 seconds** with no on-screen sign a file left the machine.

**Preconditions and model dependence.** The attack needs Copilot CLI running in **autopilot mode** and the user directing it to fetch attacker-controlled content, and its success is **model-dependent**: Microsoft's `mai-code-1.1-flash` executed it in roughly half of attempts, while OpenAI's GPT-5.6 models refused the same payload — and, as Utevsky notes, *"the user does not choose, and does not see, which model handled the session."*

**The classification dispute, and grading.** Adversa reported this via GitHub's bug-bounty on **17 September 2026** and published on **6 October**. **GitHub validated that the chain works but declined to class it as a product vulnerability**: *"this requires a user to intentionally direct Copilot CLI to fetch attacker-controlled or untrusted content and confirm they want to trigger the action, and thus is not a product vulnerability."* Adversa disputes the label, noting the chain *"presently works as described."* Because the two sides disagree only on **whether it counts as a vulnerability**, not on the facts (both accept the attack works), this is recorded as a `research` demonstration rather than tagged `disputed`. `IPI` (encrypted external web content the agent reads and executes) + `EXFIL` (local secrets leave the machine). `real_harm: false` — a controlled demonstration with no in-the-wild use. `medium`: a novel and important guardrail-bypass technique, but gated behind autopilot mode, user-initiated fetching, and model variance. Confidence `A`: the researcher's own detailed write-up plus independent reporting (The Register, Cyber Security News).

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Adversa AI — "Cryptographic Context Injection" | <https://adversa.ai/blog/cryptographic-context-injection-github-copilot/> |
| 2 | The Register | <https://www.theregister.com/ai-and-ml/2026/10/06/zombie-instructions-on-carefully-constructed-web-pages-could-trick-github-copilot-cli-into-sharing-secrets/5301206> |
| 3 | Cyber Security News | <https://cybersecuritynews.com/github-copilot-cli-vulnerability/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-06` (raw: reported to GitHub 2026-09-17; published 2026-10-06, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`EXFIL`](../../taxonomy/types.md#exfil) |
| Severity | **Medium** `medium` |
| Confidence | **A** — Adversa's detailed disclosure plus independent reporting |
| Real harm | No — controlled demonstration, no known in-the-wild use |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-06-copilot-cli-cryptographic-context-injection` |

<sub>**Why this classification:** A researcher demonstration (`research`) of a guardrail-bypass technique: encrypted external web content the agent decrypts and executes (`IPI`), ending in exfiltration of local secrets (`EXFIL`). `real_harm: false` — a demo, no in-the-wild use. `medium` rather than `high`: the technique is novel and real but gated behind autopilot mode, user-initiated fetching of untrusted content, and model-dependent success. **Not** tagged `disputed` because GitHub and Adversa disagree only on whether it qualifies as a product vulnerability, not on whether the attack works (GitHub validated it does). Dated to the 6 October publication; reported to GitHub 17 September. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain (IPI + EXFIL)](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-07-07` [GitLost: indirect prompt injection in GitHub Agentic Workflows](../2026-07/2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>Another injection path into a GitHub coding-agent surface</sub>
- `2025-10-08` [CamoLeak: zero-click exfiltration in GitHub Copilot Chat](../2025-10/2025-10-08-camoleak-github-copilot-chat.md)<br>  <sub>An earlier Copilot exfiltration chain — a different Copilot surface</sub>
- `2026-10-02` [GitLab Duo AI Gateway prompt-template sandbox escape (CVE-2026-90970)](2026-10-02-gitlab-duo-ai-gateway-rce.md)<br>  <sub>The same week, a different coding-assistant platform's weakness</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-06-copilot-cli-cryptographic-context-injection.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
