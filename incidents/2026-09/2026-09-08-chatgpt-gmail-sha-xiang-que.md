---
id: 2026-09-08-chatgpt-gmail-sha-xiang-que
title: "ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account"
title_zh: "ChatGPT 沙箱缺陷让受害者的 Gmail 数据流进攻击者账号"
title_ja: "ChatGPTのサンドボックス欠陥が被害者のGmailデータを攻撃者のアカウントへ流し込む"
title_ko: "ChatGPT 샌드박스 결함, 피해자의 Gmail 데이터를 공격자 계정으로 흘려보내다"
title_de: "ChatGPT-Sandbox-Fehler leitet Gmail-Daten eines Opfers in das Konto des Angreifers"
title_fr: "Une faille du bac à sable ChatGPT achemine les données Gmail d'une victime vers le compte de l'attaquant"
title_es: "Un fallo del sandbox de ChatGPT canaliza los datos de Gmail de la víctima a la cuenta del atacante"
date: 2026-09-08
date_precision: day
date_raw: "2026-09-08"

kind: research
type: [EXFIL]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Check Point Research (work dated **2026-06**): a weakness in the ChatGPT **code-execution sandbox** — **every container can reach the same internal JFrog Artifactory instance OpenAI uses for package management**, forming a covert channel. The attacker buries instructions in a shared conversation, a malicious prompt or a custom GPT configuration; the victim's session then carries out the hidden task while handling a normal request, sending data from connected apps to the attacker **without showing it in the chat output** and **with no confirmation prompt at all**.
  The impact is not limited to Gmail — everything the victim's session has authorised (Google Drive, Microsoft Teams, GitHub connectors) is in scope. **The only visible sign is a small "Talked to Gmail" label logged after the fact**. OpenAI has fixed it and taken the internal service involved offline.
  💡 **Note: JFrog Artifactory was also the egress for the 2026-07 OpenAI agent escape** — the same component has been a weak point in AI infrastructure twice within six months


summary_zh: |
  Check Point Research（工作时间标注为 **2026-06**）：ChatGPT **代码执行沙箱**的一个弱点 —— **每个容器都能触达 OpenAI 用于包管理的同一个内部 JFrog Artifactory 实例**，构成隐蔽信道。攻击者把指令埋进共享对话、恶意提示或自定义 GPT 配置中，受害者的会话就会在处理正常请求的同时执行隐藏任务，把已连接应用的数据发给攻击者**且不在聊天输出中显示**，**全程无任何确认提示**。
  影响范围不止 Gmail —— 受害者会话已授权的一切（Google Drive、Microsoft Teams、GitHub 连接器）都在内。**唯一可见迹象是一个事后才记录的「Talked to Gmail」小标签**。OpenAI 已修复并下线了涉事内部服务
  💡 **注意：JFrog Artifactory 同时也是 2026-07 OpenAI agent 逃逸的出口** —— 同一个组件在半年内两次成为 AI 基础设施的薄弱点

summary_ja: |
  Check Point Research（**2026-06**付の研究）：ChatGPTの**コード実行サンドボックス**の弱点——**すべてのコンテナが、OpenAIがパッケージ管理に使う同一の内部JFrog Artifactoryインスタンスに到達できる**ため、秘密チャネルが形成される。攻撃者は共有会話、悪意あるプロンプト、カスタムGPT設定に指示を埋め込み、被害者のセッションが通常のリクエストを処理しながら隠されたタスクを実行し、接続アプリのデータを攻撃者へ送信する——**チャット出力には表示されず**、**確認プロンプトも一切出ない**。
  影響はGmailにとどまらない——被害者のセッションが認可しているすべて（Google Drive、Microsoft Teams、GitHubコネクタ）が対象になる。**唯一の目に見える痕跡は、事後に記録される小さな「Talked to Gmail」ラベルだけである**。OpenAIは修正し、関与した内部サービスを停止した。
  💡 **注記：JFrog Artifactoryは2026-07のOpenAIエージェント脱出の出口でもあった**——同じコンポーネントが半年の間に2度、AIインフラの弱点となった

summary_ko: |
  Check Point Research(작업 시점 **2026-06**): ChatGPT **코드 실행 샌드박스**의 약점 — **모든 컨테이너가 OpenAI가 패키지 관리에 사용하는 동일한 내부 JFrog Artifactory 인스턴스에 도달할 수 있어** 은밀한 채널이 형성된다. 공격자는 공유 대화, 악성 프롬프트 또는 사용자 지정 GPT 설정에 지시를 묻어둔다. 그러면 피해자의 세션이 정상 요청을 처리하면서 숨겨진 작업을 수행해 연결된 앱의 데이터를 공격자에게 보내며 **채팅 출력에는 표시하지 않고** **확인 프롬프트도 전혀 없다**.
  영향은 Gmail에 그치지 않는다 — 피해자 세션이 승인한 모든 것(Google Drive, Microsoft Teams, GitHub 커넥터)이 범위에 들어간다. **유일하게 보이는 흔적은 사후에 기록되는 작은 "Talked to Gmail" 표시뿐이다**. OpenAI는 이를 수정하고 관련 내부 서비스를 오프라인으로 전환했다.
  💡 **참고: JFrog Artifactory는 2026-07 OpenAI 에이전트 탈출의 외부 송신 경로이기도 했다** — 같은 구성 요소가 6개월 안에 두 번 AI 인프라의 약점이 되었다

summary_de: |
  Check Point Research (Arbeit datiert auf **2026-06**): eine Schwäche in der **Code-Ausführungs-Sandbox von ChatGPT** — **jeder Container kann dieselbe interne JFrog-Artifactory-Instanz erreichen, die OpenAI für die Paketverwaltung nutzt**, was einen verdeckten Kanal bildet. Der Angreifer versteckt Anweisungen in einer geteilten Unterhaltung, einem bösartigen Prompt oder einer benutzerdefinierten GPT-Konfiguration; die Sitzung des Opfers führt dann beim Bearbeiten einer normalen Anfrage die versteckte Aufgabe aus und sendet Daten aus verbundenen Apps an den Angreifer, **ohne sie in der Chat-Ausgabe zu zeigen** und **ganz ohne Bestätigungsdialog**.
  Die Auswirkung beschränkt sich nicht auf Gmail — alles, was die Sitzung des Opfers autorisiert hat (Google Drive, Microsoft Teams, GitHub-Connectoren), liegt im Wirkungsbereich. **Das einzige sichtbare Zeichen ist ein kleines, nachträglich protokolliertes Label „Talked to Gmail“**. OpenAI hat es behoben und den betroffenen internen Dienst offline genommen.
  💡 **Anmerkung: JFrog Artifactory war auch der Egress für den OpenAI-Agentenausbruch vom 2026-07** — dieselbe Komponente war innerhalb von sechs Monaten zweimal ein Schwachpunkt der KI-Infrastruktur

summary_fr: |
  Check Point Research (travaux datés de **2026-06**) : une faiblesse du **bac à sable d'exécution de code** de ChatGPT — **chaque conteneur peut atteindre la même instance JFrog Artifactory interne qu'OpenAI utilise pour la gestion des paquets**, formant un canal covert. L'attaquant enfouit des instructions dans une conversation partagée, un prompt malveillant ou une configuration de GPT personnalisé ; la session de la victime exécute alors la tâche cachée tout en traitant une requête normale, envoyant des données d'applications connectées à l'attaquant **sans les afficher dans la sortie du chat** et **sans aucune invite de confirmation**.
  L'impact ne se limite pas à Gmail — tout ce que la session de la victime a autorisé (Google Drive, Microsoft Teams, connecteurs GitHub) est concerné. **Le seul signe visible est une petite étiquette « Talked to Gmail » journalisée après coup**. OpenAI a corrigé et mis hors ligne le service interne concerné.
  💡 **À noter : JFrog Artifactory était aussi la sortie de l'évasion d'agent d'OpenAI en 2026-07** — le même composant a été un point faible de l'infrastructure IA deux fois en six mois

summary_es: |
  Check Point Research (trabajo fechado en **2026-06**): una debilidad en el **sandbox de ejecución de código** de ChatGPT — **todos los contenedores pueden alcanzar la misma instancia interna de JFrog Artifactory que OpenAI usa para la gestión de paquetes**, formando un canal encubierto. El atacante esconde instrucciones en una conversación compartida, un prompt malicioso o la configuración de un GPT personalizado; la sesión de la víctima entonces realiza la tarea oculta mientras atiende una solicitud normal, enviando datos de las aplicaciones conectadas al atacante **sin mostrarlo en la salida del chat** y **sin ningún aviso de confirmación**.
  El impacto no se limita a Gmail — todo lo que la sesión de la víctima tenga autorizado (Google Drive, Microsoft Teams, conectores de GitHub) está en el alcance. **La única señal visible es una pequeña etiqueta "Talked to Gmail" registrada a posteriori**. OpenAI ya lo ha corregido y ha retirado el servicio interno implicado.
  💡 **Nota: JFrog Artifactory también fue la vía de salida del escape del agente de OpenAI de 2026-07** — el mismo componente ha sido un punto débil de la infraestructura de IA dos veces en seis meses

sources:
  - url: https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html
    label: THN
  - url: https://www.csoonline.com/article/4220203/chatgpt-flaw-lets-attackers-pull-gmail-data-across-accounts-via-a-hidden-channel.html
    label: CSO Online

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Check Point Research (work dated **2026-06**): a weakness in the ChatGPT **code-execution sandbox** — **every container can reach the same internal JFrog Artifactory instance OpenAI uses for package management**, forming a covert channel. The attacker buries instructions in a shared conversation, a malicious prompt or a custom GPT configuration; the victim's session then carries out the hidden task while handling a normal request, sending data from connected apps to the attacker **without showing it in the chat output** and **with no confirmation prompt at all**.

The impact is not limited to Gmail — everything the victim's session has authorised (Google Drive, Microsoft Teams, GitHub connectors) is in scope. **The only visible sign is a small "Talked to Gmail" label logged after the fact**. OpenAI has fixed it and taken the internal service involved offline.

💡 **Note: JFrog Artifactory was also the egress for the 2026-07 OpenAI agent escape** — the same component has been a weak point in AI infrastructure twice within six months

## Attack chain

```mermaid
flowchart LR
    E["Sensitive data the agent can reach"]:::entry
    S0["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/chatgpt-flaw-let-planted-prompt-send.html> |
| 2 | CSO Online | <https://www.csoonline.com/article/4220203/chatgpt-flaw-lets-attackers-pull-gmail-data-across-accounts-via-a-hidden-channel.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-08` (raw: 2026-09-08, precision `day`) |
| Kind | Research demo `research` |
| Type | [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-08-chatgpt-gmail-sha-xiang-que` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-08-19` [Grok "cryptographic context injection": encrypted instructions, plaintext data](../2026-08/2026-08-19-grok-mi-ma-xue-wen.md)<br>  <sub>Grok "cryptographic context injection": encrypted instructions, plaintext data</sub>
- `2026-08-18` [CoSnitch (CVE-2026-24301)](../2026-08/2026-08-18-cosnitch.md)<br>  <sub>CoSnitch (CVE-2026-24301)</sub>
- `2026-07-07` [GitLost: GitHub Agentic Workflows leak private repositories](../2026-07/2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>GitLost: GitHub Agentic Workflows leak private repositories</sub>
- `2026-06-15` [SearchLeak (CVE-2026-42824)](../2026-06/2026-06-15-searchleak.md)<br>  <sub>SearchLeak (CVE-2026-42824)</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
