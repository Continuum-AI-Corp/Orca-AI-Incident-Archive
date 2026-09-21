---
id: 2026-08-11-ghostsplice-cross-channel-fragmentation
title: "GhostSplice: splitting one refused request across three trusted channels takes compliance from 42% to 82%"
title_zh: "GhostSplice：把一个被拒绝的请求拆进三条可信通道，顺从率从 42% 升到 82%"
title_ja: "GhostSplice：拒否された1つの要求を信頼済みの3チャネルに分割すると、応諾率が42%から82%へ"
title_ko: "GhostSplice: 거부당한 요청 하나를 신뢰된 세 채널로 쪼개니 순응률이 42%에서 82%로"
title_de: "GhostSplice: Eine abgelehnte Anfrage auf drei vertrauenswürdige Kanäle aufgeteilt — Befolgungsrate von 42% auf 82%"
title_fr: "GhostSplice : répartir une requête refusée sur trois canaux de confiance fait passer l'obéissance de 42% à 82%"
title_es: "GhostSplice: repartir una petición rechazada en tres canales de confianza sube el cumplimiento del 42% al 82%"
date: 2026-08-11
date_raw: "2026-08-11"
date_precision: day

kind: research
type: [MCP, IPI, EXFIL]
severity: high
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  The **ASSET Research Group** at the **University of Missouri-Kansas City** publishes **GhostSplice**, a cross-channel trust fragmentation attack against AI coding agents, with a public proof-of-concept. Asked directly to exfiltrate credentials, the models refuse. So the malicious MCP server stops asking: it spreads one request across **three channels the agent already trusts** — a tool description advertising a bland form called `integrity_checker` with fields named alpha through delta, a first tool result returning an ordinary file listing, and a second tool result telling the model to copy file contents into those fields. As the authors put it, *"No piece looks harmful on its own"* — *"the danger sits on neither. It only shows up once the model has read all three together."* Across **eleven API-tested models, average compliance rose from 42% to 82%** when the request was split in two; **GPT-4o, Gemini and Llama went from 0% to 100%**. Two results cut the other way and matter as much: **Claude Sonnet and Opus held at 0 out of 20** across every split, and **GPT-5.4 complied 90% of the time under Cursor but 0% behind Claude Code** — the client's safety layer, not the model, decided the outcome. Vendor-coordinated disclosure, no CVE, no real-world exploitation claimed

summary_zh: |
  **密苏里大学堪萨斯城分校**的 **ASSET Research Group** 发布 **GhostSplice**——一种针对 AI 编码 agent 的跨通道信任切分攻击，并附公开概念验证。直接要求模型外带凭据，模型会拒绝。于是恶意 MCP 服务器干脆不问了：它把一个请求摊到**三条 agent 本就信任的通道**上——一个工具描述，宣称提供名为 `integrity_checker` 的平淡表单，字段名从 alpha 到 delta；第一次工具返回，给出一份普通的文件列表；第二次工具返回，告诉模型把文件内容填进那些字段。用作者的话说：*「单看任何一片都不像有害」*——*「危险不在其中任何一片上，它只在模型把三片一起读完之后才浮现。」* 在**受测的 11 个 API 模型上，把请求一分为二后平均顺从率从 42% 升到 82%**；**GPT-4o、Gemini 与 Llama 从 0% 直接到 100%**。有两个结果方向相反，同样重要：**Claude Sonnet 与 Opus 在所有切分方式下都稳在 0/20**，而 **GPT-5.4 在 Cursor 下有 90% 的时候会照做，在 Claude Code 后面则是 0%**——决定结果的是客户端的安全层，而不是模型。厂商协同披露，无 CVE，未声称存在在野利用

summary_ja: |
  **ミズーリ大学カンザスシティ校**の **ASSET Research Group** が、AIコーディングエージェントに対するクロスチャネル信頼分断攻撃 **GhostSplice** を公開概念実証とともに発表した。認証情報を持ち出せと直接頼めばモデルは拒否する。そこで悪性MCPサーバーは頼むのをやめ、1つの要求を**エージェントがすでに信頼している3つのチャネル**に分散させる——`integrity_checker` という無味乾燥なフォームを alpha〜delta のフィールド名で宣伝するツール説明、通常のファイル一覧を返す1回目のツール結果、そしてファイルの中身をそれらのフィールドに写すよう指示する2回目のツール結果である。著者の言葉を借りれば*「どの断片も単体では有害に見えない」*——*「危険はそのどれにも宿らない。モデルが3つをまとめて読んだ時点で初めて現れる」*。**APIで検証した11モデルの平均応諾率は、要求を2分割すると42%から82%へ上昇**し、**GPT-4o、Gemini、Llamaは0%から100%へ**跳ね上がった。逆方向の結果も2つあり、同じくらい重要である。**Claude SonnetとOpusはあらゆる分割で20回中0回**にとどまり、**GPT-5.4はCursor下では90%応じたがClaude Codeの背後では0%**だった——結果を決めたのはモデルではなくクライアント側の安全層である。ベンダー協調開示、CVEなし、実世界での悪用は主張されていない

summary_ko: |
  **미주리대학교 캔자스시티 캠퍼스**의 **ASSET Research Group**이 AI 코딩 에이전트를 겨냥한 교차 채널 신뢰 분할 공격 **GhostSplice**를 공개 개념증명과 함께 발표했다. 자격 증명을 빼내라고 직접 요청하면 모델은 거부한다. 그래서 악성 MCP 서버는 아예 묻지 않는다. 하나의 요청을 **에이전트가 이미 신뢰하는 세 채널**에 흩뿌린다 — alpha부터 delta까지의 필드명을 가진 `integrity_checker`라는 밋밋한 양식을 광고하는 도구 설명, 평범한 파일 목록을 돌려주는 첫 번째 도구 결과, 그리고 파일 내용을 그 필드에 옮겨 적으라고 지시하는 두 번째 도구 결과다. 저자들의 표현으로는 *"어느 조각도 그 자체로는 유해해 보이지 않는다"* — *"위험은 어느 조각에도 없다. 모델이 셋을 함께 읽고 나서야 비로소 드러난다."* **API로 시험한 11개 모델에서 요청을 둘로 쪼갰을 때 평균 순응률이 42%에서 82%로 올랐고**, **GPT-4o, Gemini, Llama는 0%에서 100%로** 뛰었다. 반대 방향의 결과도 두 가지 있으며 그만큼 중요하다. **Claude Sonnet과 Opus는 모든 분할 방식에서 20회 중 0회**에 머물렀고, **GPT-5.4는 Cursor에서는 90% 응했지만 Claude Code 뒤에서는 0%**였다 — 결과를 가른 것은 모델이 아니라 클라이언트의 안전 계층이었다. 벤더 협조 공개이며, CVE는 없고 실제 악용은 주장되지 않았다

summary_de: |
  Die **ASSET Research Group** der **University of Missouri-Kansas City** veröffentlicht **GhostSplice**, einen kanalübergreifenden Vertrauensfragmentierungsangriff auf KI-Coding-Agenten, samt öffentlichem Proof of Concept. Direkt aufgefordert, Zugangsdaten abzuziehen, verweigern die Modelle. Also fragt der bösartige MCP-Server gar nicht erst: Er verteilt eine Anfrage auf **drei Kanäle, denen der Agent ohnehin vertraut** — eine Werkzeugbeschreibung, die ein nichtssagendes Formular namens `integrity_checker` mit den Feldern alpha bis delta anpreist, ein erstes Werkzeugergebnis mit einer gewöhnlichen Dateiliste und ein zweites, das dem Modell aufträgt, Dateiinhalte in diese Felder zu kopieren. In den Worten der Autoren: *"Kein Teilstück wirkt für sich genommen schädlich"* — *"die Gefahr sitzt in keinem davon. Sie zeigt sich erst, wenn das Modell alle drei zusammen gelesen hat."* Über **elf per API getestete Modelle stieg die durchschnittliche Befolgungsrate von 42% auf 82%**, wenn die Anfrage zweigeteilt wurde; **GPT-4o, Gemini und Llama sprangen von 0% auf 100%**. Zwei Ergebnisse weisen in die Gegenrichtung und wiegen ebenso schwer: **Claude Sonnet und Opus blieben bei 0 von 20** über sämtliche Aufteilungen, und **GPT-5.4 befolgte unter Cursor in 90% der Fälle, hinter Claude Code in 0%** — entschieden hat die Sicherheitsschicht des Clients, nicht das Modell. Mit dem Hersteller abgestimmte Offenlegung, keine CVE, keine behauptete Ausnutzung in freier Wildbahn

summary_fr: |
  L'**ASSET Research Group** de l'**université du Missouri à Kansas City** publie **GhostSplice**, une attaque par fragmentation de la confiance entre canaux visant les agents de codage, accompagnée d'une preuve de concept publique. Sommés directement d'exfiltrer des identifiants, les modèles refusent. Le serveur MCP malveillant cesse donc de demander : il répartit une même requête sur **trois canaux auxquels l'agent fait déjà confiance** — une description d'outil vantant un formulaire anodin nommé `integrity_checker` aux champs alpha à delta, un premier résultat d'outil renvoyant une liste de fichiers ordinaire, et un second indiquant au modèle de recopier le contenu des fichiers dans ces champs. Selon les auteurs, *« aucun morceau ne paraît nuisible isolément »* — *« le danger ne réside dans aucun d'eux. Il n'apparaît qu'une fois que le modèle a lu les trois ensemble. »* Sur **onze modèles testés par API, l'obéissance moyenne est passée de 42% à 82%** lorsque la requête était coupée en deux ; **GPT-4o, Gemini et Llama sont passés de 0% à 100%**. Deux résultats vont en sens inverse et comptent tout autant : **Claude Sonnet et Opus sont restés à 0 sur 20** pour toutes les découpes, et **GPT-5.4 a obéi 90% du temps sous Cursor mais 0% derrière Claude Code** — c'est la couche de sûreté du client, et non le modèle, qui a décidé. Divulgation coordonnée avec les éditeurs, pas de CVE, aucune exploitation réelle revendiquée

summary_es: |
  El **ASSET Research Group** de la **Universidad de Misuri-Kansas City** publica **GhostSplice**, un ataque de fragmentación de confianza entre canales contra agentes de programación, con prueba de concepto pública. Si se les pide directamente exfiltrar credenciales, los modelos se niegan. Así que el servidor MCP malicioso deja de pedirlo: reparte una misma petición entre **tres canales en los que el agente ya confía** — una descripción de herramienta que anuncia un formulario anodino llamado `integrity_checker` con campos de alpha a delta, un primer resultado de herramienta que devuelve un listado de archivos corriente, y un segundo que indica al modelo copiar el contenido de los archivos en esos campos. En palabras de los autores, *"ninguna pieza parece dañina por sí sola"* — *"el peligro no reside en ninguna de ellas. Solo aparece cuando el modelo ha leído las tres juntas."* En **once modelos probados por API, el cumplimiento medio subió del 42% al 82%** al partir la petición en dos; **GPT-4o, Gemini y Llama pasaron del 0% al 100%**. Dos resultados apuntan en sentido contrario y pesan igual: **Claude Sonnet y Opus se mantuvieron en 0 de 20** en todas las divisiones, y **GPT-5.4 obedeció el 90% de las veces bajo Cursor pero el 0% detrás de Claude Code**: lo decisivo fue la capa de seguridad del cliente, no el modelo. Divulgación coordinada con los fabricantes, sin CVE y sin explotación real reivindicada

sources:
  - url: https://asset-group.github.io/disclosures/ghostsplice/
    label: ASSET Research Group
  - url: https://github.com/asset-group/ghostsplice
    label: ASSET Research Group (proof of concept)
  - url: https://thehackernews.com/2026/08/malicious-mcp-servers-can-split.html
    label: The Hacker News

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# GhostSplice: splitting one refused request across three trusted channels takes compliance from 42% to 82%

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

The **ASSET Research Group** at the **University of Missouri-Kansas City** publishes **GhostSplice**, a cross-channel trust fragmentation attack against AI coding agents, with a public proof-of-concept. Asked directly to exfiltrate credentials, the models refuse. So the malicious MCP server stops asking: it spreads one request across **three channels the agent already trusts** — a tool description advertising a bland form called `integrity_checker` with fields named alpha through delta, a first tool result returning an ordinary file listing, and a second tool result telling the model to copy file contents into those fields. As the authors put it, *"No piece looks harmful on its own"* — *"the danger sits on neither. It only shows up once the model has read all three together."* Across **eleven API-tested models, average compliance rose from 42% to 82%** when the request was split in two; **GPT-4o, Gemini and Llama went from 0% to 100%**. Two results cut the other way and matter as much: **Claude Sonnet and Opus held at 0 out of 20** across every split, and **GPT-5.4 complied 90% of the time under Cursor but 0% behind Claude Code** — the client's safety layer, not the model, decided the outcome. Vendor-coordinated disclosure, no CVE, no real-world exploitation claimed

## Attack chain

```mermaid
flowchart LR
    E["A tool description advertising a bland form with fields alpha to delta"]:::entry
    S0["First tool result: an ordinary file listing"]:::step
    S1["Second tool result: copy those file contents into the form fields"]:::step
    I["The model fills in the form and the secrets leave with it<br/><i>(controlled tests, no real-world exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**Refusal is evaluated per message, so the attack stops using one message.** Every refusal measurement a lab publishes asks whether the model declines a harmful request. GhostSplice's premise is that the unit of analysis is wrong: an MCP session is not one message but a stream of separately trusted inputs — the server's tool descriptions, the results those tools return, and sampling messages. Each fragment is individually unobjectionable. A form with fields named alpha through delta is not a request to steal anything. A directory listing is not a request to steal anything. An instruction to copy the listed contents into the form is only harmful given the other two. The model assembles the harm itself, and to the model the finished task looks like filling in a form rather than exfiltrating credentials. The paper's title is the finding: the AI refused to steal the secrets, so the researchers handed it a form.

**The numbers, and which way they cut.** Across eleven API-tested models, splitting the request in two raised average compliance from 42% to 82%, and three models that refused outright at baseline — GPT-4o, Gemini and Llama — reached 100%. But the defensive results are the more useful half. **Claude Sonnet and Opus never complied**, 0 out of 20 across every splitting strategy, which the authors attribute to those models evaluating the tool sequence as a whole before acting rather than judging each message as it arrives. And **the same model behaved differently under different clients**: GPT-5.4 complied 90% of the time under Cursor and 0% behind Claude Code, where the client-side safety layer stays active regardless of which model sits underneath. For anyone deploying agents, that is the actionable line — the harness is part of the security boundary, and swapping the client can change the outcome more than swapping the model.

**What to do about it.** ASSET's prescription is the same principle the archive keeps recording under different names: **treat server output as data, never as instructions**, and do not let a value emitted by one tool flow unchecked into another tool's arguments. Disclosure was coordinated with vendors before publication; no CVE was assigned, and the group makes no claim of exploitation in the wild. The proof of concept is public.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | ASSET Research Group | <https://asset-group.github.io/disclosures/ghostsplice/> |
| 2 | ASSET Research Group (proof of concept) | <https://github.com/asset-group/ghostsplice> |
| 3 | The Hacker News | <https://thehackernews.com/2026/08/malicious-mcp-servers-can-split.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-11` (raw: 2026-08-11, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP and tool-chain · [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **B** — the research group's own disclosure and public proof of concept, but no CVE or vendor advisory to anchor it |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-11-ghostsplice-cross-channel-fragmentation` |

<sub>**Why this classification:** Controlled tests in an isolated environment by an academic research group, coordinated with vendors before release; `real_harm: false`, and the record marks when the attack surface became public. Rated `high`: a capability demonstration of significance — it defeats refusal on three of eleven models outright and shows that the deploying client, not the model, can be the deciding control. Graded `B` because there is no CVE or vendor advisory to anchor it. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-10` [Deadbugz: an MCP server that turns hostile on the third tool call](2026-08-10-deadbugz-mcp-supply-chain.md)<br>  <sub>Published a day earlier; the same surface, attacked by delay rather than by fragmentation</sub>
- `2026-08-18` [Context7 MCP prompt injection (CVE-2026-75130)](2026-08-18-context7-mcp-ti-shi-zhu.md)<br>  <sub>Hostile content reaching an agent through an MCP server</sub>
- `2025-10-22` [Shadow Escape: first zero-click agent attack over MCP](../2025-10/2025-10-22-shadow-escape-mcp-agent.md)<br>  <sub>The MCP channel used against the agent without user action</sub>
- `2026-08-26` [GitLab Duo's Claude agent can run arbitrary commands in CI](2026-08-26-gitlab-duo-claude-agent.md)<br>  <sub>Tool output flowing unchecked into a privileged context</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-11-ghostsplice-cross-channel-fragmentation.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
