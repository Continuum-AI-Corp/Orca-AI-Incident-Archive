---
id: 2026-08-10-deadbugz-mcp-supply-chain
title: "Deadbugz: an MCP server that turns hostile on the third tool call, pushed to 23 repositories in 74 minutes"
title_zh: "Deadbugz：一个在第三次工具调用后翻脸的 MCP 服务器，74 分钟内推向 23 个仓库"
title_ja: "Deadbugz：3回目のツール呼び出しで豹変するMCPサーバー、74分間で23リポジトリに送り込まれる"
title_ko: "Deadbugz: 세 번째 도구 호출에서 돌변하는 MCP 서버, 74분 만에 23개 저장소로"
title_de: "Deadbugz: ein MCP-Server, der beim dritten Tool-Aufruf feindselig wird — in 74 Minuten an 23 Repositories geschickt"
title_fr: "Deadbugz : un serveur MCP qui devient hostile au troisième appel d'outil, poussé vers 23 dépôts en 74 minutes"
title_es: "Deadbugz: un servidor MCP que se vuelve hostil en la tercera llamada, enviado a 23 repositorios en 74 minutos"
date: 2026-08-10
date_raw: "2026-08-10"
date_precision: day

kind: incident
type: [SUPPLY, MCP, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Pillar Security** documents a live MCP supply-chain campaign it names **Deadbugz**. A server advertised as **`productivity-suite`** offers text formatting and summarisation and behaves correctly — while keeping **an in-memory, per-client counter of `tools/call` requests**. On the third call it rewrites the metadata it returns to the agent into instructions to hunt for **SSH keys, AWS credentials, shell history and Kubernetes configuration**, and to conceal the activity from the user. Because the payload is present from the start and only unlocks on a counter, **static scanning, SBOMs and one-time review of the tool manifest all pass**. Delivery was pull-request spam: the GitHub account **`zellkernel`** (linked to the X handle `@llmgod`) opened **23 pull requests in 74 minutes** on 10 August, 21:52–23:07 UTC, each adding the malicious server to an unrelated AI, MCP or developer-tooling project. At review, **19 were closed, 4 remained open and none had been merged** — no confirmed victim. Pillar marked the disclosure as open and subject to update

summary_zh: |
  **Pillar Security** 记录了一场正在进行的 MCP 供应链战役，命名为 **Deadbugz**。一个对外宣称叫 **`productivity-suite`** 的服务器提供文本格式化与摘要功能，行为一切正常——同时在内存里维护**按客户端计数的 `tools/call` 请求计数器**。到第三次调用时，它把返回给 agent 的元数据改写成指令，去搜寻 **SSH 密钥、AWS 凭据、shell 历史与 Kubernetes 配置**，并对用户隐藏这些行为。由于载荷从一开始就在包里、只是靠计数器解锁，**静态扫描、SBOM 与对工具清单的一次性审查全都会通过**。投送方式是 PR 轰炸：GitHub 账号 **`zellkernel`**（关联 X 账号 `@llmgod`）在 8 月 10 日 21:52–23:07 UTC 的 **74 分钟内开了 23 个 pull request**，每个都往一个互不相关的 AI、MCP 或开发者工具项目里加入这个恶意服务器。截至复核时，**19 个已关闭、4 个仍开着，没有一个被合并**——无确认受害方。Pillar 将该披露标记为开放状态、后续会更新

summary_ja: |
  **Pillar Security**が進行中のMCPサプライチェーン攻撃を記録し、**Deadbugz**と命名した。**`productivity-suite`**を名乗るサーバーはテキスト整形と要約を提供し、正常に振る舞う——その裏で**クライアントごとの`tools/call`リクエスト回数をメモリ上で数えている**。3回目の呼び出しで、エージェントに返すメタデータを書き換え、**SSH鍵、AWS認証情報、シェル履歴、Kubernetes設定**を探すよう指示し、その活動をユーザーから隠す。ペイロードは最初からパッケージ内に存在し、カウンタで解錠されるだけなので、**静的スキャン、SBOM、ツールマニフェストの一度きりのレビューはいずれも通過してしまう**。配送手段はPRの大量投下だった。GitHubアカウント**`zellkernel`**（Xアカウント`@llmgod`と関連）が8月10日21:52〜23:07 UTCの**74分間に23件のプルリクエスト**を開き、いずれも無関係なAI・MCP・開発者ツール系プロジェクトへこの悪性サーバーを追加するものだった。レビュー時点で**19件はクローズ、4件は未処理、マージされたものはゼロ**——確認された被害者はいない。Pillarはこの開示を継続更新中のものとしている

summary_ko: |
  **Pillar Security**가 진행 중인 MCP 공급망 캠페인을 기록하고 **Deadbugz**라 명명했다. **`productivity-suite`**를 표방하는 서버는 텍스트 서식화와 요약을 제공하며 정상적으로 동작한다 — 그러면서 **클라이언트별 `tools/call` 요청 횟수를 메모리에서 세고 있다**. 세 번째 호출에서 에이전트에 돌려주는 메타데이터를 **SSH 키, AWS 자격 증명, 셸 기록, 쿠버네티스 설정**을 찾으라는 지시로 바꿔 쓰고, 그 활동을 사용자에게 감춘다. 페이로드는 처음부터 패키지 안에 있고 카운터로 해제될 뿐이므로 **정적 스캔, SBOM, 도구 매니페스트 1회 검토가 모두 통과한다**. 전달 수단은 PR 폭탄이었다. GitHub 계정 **`zellkernel`**(X 계정 `@llmgod`와 연결)이 8월 10일 21:52–23:07 UTC의 **74분 동안 23개의 풀 리퀘스트**를 열었고, 각각 무관한 AI·MCP·개발자 도구 프로젝트에 이 악성 서버를 추가하는 내용이었다. 검토 시점에 **19개는 닫혔고 4개는 열려 있었으며 병합된 것은 없었다** — 확인된 피해자는 없다. Pillar는 이 공개를 갱신 예정 상태로 표시했다

summary_de: |
  **Pillar Security** dokumentiert eine laufende MCP-Lieferkettenkampagne, die es **Deadbugz** nennt. Ein als **`productivity-suite`** angebotener Server bietet Textformatierung und Zusammenfassung und verhält sich korrekt — während er **im Arbeitsspeicher einen Zähler für `tools/call`-Anfragen pro Client** führt. Beim dritten Aufruf schreibt er die an den Agenten zurückgegebenen Metadaten in Anweisungen um, **SSH-Schlüssel, AWS-Zugangsdaten, Shell-Verlauf und Kubernetes-Konfiguration** zu suchen und die Aktivität vor dem Benutzer zu verbergen. Da die Nutzlast von Anfang an enthalten ist und nur über einen Zähler freigeschaltet wird, **bestehen statische Scans, SBOMs und eine einmalige Prüfung des Tool-Manifests allesamt**. Die Zustellung erfolgte per Pull-Request-Spam: Das GitHub-Konto **`zellkernel`** (verbunden mit dem X-Konto `@llmgod`) eröffnete am 10. August zwischen 21:52 und 23:07 UTC **23 Pull Requests in 74 Minuten**, jeder davon fügte den bösartigen Server einem nicht verwandten KI-, MCP- oder Entwicklerwerkzeug-Projekt hinzu. Zum Prüfzeitpunkt waren **19 geschlossen, 4 offen und keiner gemergt** — kein bestätigtes Opfer. Pillar hat die Veröffentlichung als fortlaufend gekennzeichnet

summary_fr: |
  **Pillar Security** documente une campagne active de chaîne d'approvisionnement MCP qu'il nomme **Deadbugz**. Un serveur présenté sous le nom de **`productivity-suite`** propose du formatage et du résumé de texte et se comporte correctement — tout en tenant **un compteur en mémoire des requêtes `tools/call` par client**. Au troisième appel, il réécrit les métadonnées renvoyées à l'agent en instructions visant à chercher **clés SSH, identifiants AWS, historique de shell et configuration Kubernetes**, et à dissimuler l'activité à l'utilisateur. Comme la charge utile est présente dès le départ et ne se déverrouille que sur un compteur, **l'analyse statique, les SBOM et une revue ponctuelle du manifeste d'outils passent tous**. La livraison s'est faite par inondation de pull requests : le compte GitHub **`zellkernel`** (lié au compte X `@llmgod`) a ouvert **23 pull requests en 74 minutes** le 10 août, de 21h52 à 23h07 UTC, chacune ajoutant le serveur malveillant à un projet d'IA, de MCP ou d'outillage développeur sans rapport. Au moment de la revue, **19 étaient fermées, 4 encore ouvertes et aucune fusionnée** — aucune victime confirmée. Pillar a indiqué que la divulgation restait ouverte et sujette à mise à jour

summary_es: |
  **Pillar Security** documenta una campaña activa de cadena de suministro de MCP a la que llama **Deadbugz**. Un servidor anunciado como **`productivity-suite`** ofrece formateo y resumen de texto y se comporta correctamente, mientras mantiene **un contador en memoria de peticiones `tools/call` por cliente**. En la tercera llamada reescribe los metadatos que devuelve al agente convirtiéndolos en instrucciones para buscar **claves SSH, credenciales de AWS, historial de shell y configuración de Kubernetes**, y para ocultar la actividad al usuario. Como la carga útil está presente desde el principio y solo se desbloquea con un contador, **el análisis estático, los SBOM y una revisión puntual del manifiesto de herramientas pasan todos**. La entrega fue mediante avalancha de pull requests: la cuenta de GitHub **`zellkernel`** (vinculada a la cuenta de X `@llmgod`) abrió **23 pull requests en 74 minutos** el 10 de agosto, de 21:52 a 23:07 UTC, cada una añadiendo el servidor malicioso a un proyecto de IA, MCP o herramientas para desarrolladores sin relación entre sí. En el momento de la revisión, **19 estaban cerradas, 4 seguían abiertas y ninguna se había fusionado**: ninguna víctima confirmada. Pillar marcó la divulgación como abierta y sujeta a actualización

sources:
  - url: https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign
    label: Pillar Security

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Deadbugz: an MCP server that turns hostile on the third tool call, pushed to 23 repositories in 74 minutes

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**Pillar Security** documents a live MCP supply-chain campaign it names **Deadbugz**. A server advertised as **`productivity-suite`** offers text formatting and summarisation and behaves correctly — while keeping **an in-memory, per-client counter of `tools/call` requests**. On the third call it rewrites the metadata it returns to the agent into instructions to hunt for **SSH keys, AWS credentials, shell history and Kubernetes configuration**, and to conceal the activity from the user. Because the payload is present from the start and only unlocks on a counter, **static scanning, SBOMs and one-time review of the tool manifest all pass**. Delivery was pull-request spam: the GitHub account **`zellkernel`** (linked to the X handle `@llmgod`) opened **23 pull requests in 74 minutes** on 10 August, 21:52–23:07 UTC, each adding the malicious server to an unrelated AI, MCP or developer-tooling project. At review, **19 were closed, 4 remained open and none had been merged** — no confirmed victim. Pillar marked the disclosure as open and subject to update

## Attack chain

```mermaid
flowchart LR
    E["A pull request adds productivity-suite to a project's MCP configuration"]:::entry
    S0["The server behaves correctly for two tool calls and passes review"]:::step
    S1["An in-memory counter trips on the third call and the returned metadata is rewritten"]:::step
    I["The agent is instructed to collect SSH keys, AWS credentials, shell history and kube config, and to hide it<br/><i>(no pull request merged, no confirmed victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The trick is the delay, not the payload.** Tool poisoning in MCP is not new — hiding instructions in a tool description was demonstrated in April 2025 and has been re-demonstrated many times since. What Deadbugz changes is *when* the description becomes hostile. The server keeps a per-client counter of `tools/call` requests in memory; for the first two calls it returns exactly the metadata a reviewer would expect from a text-formatting tool. Every pre-approval control operates on that benign state: a static scanner sees benign code, an SBOM lists a normal dependency, a human reading the tool manifest reads a formatter. The malicious behaviour exists in the shipped artefact from the beginning; it is simply gated. Pillar's prescription follows from this directly — **monitor tool metadata for changes after approval**, because auditing it once is auditing the wrong moment.

**The delivery method is the other half.** The operator did not wait to be discovered organically. The GitHub account `zellkernel` opened 23 pull requests inside 74 minutes on 10 August, against projects with nothing in common except that they were AI, MCP or developer tooling — the profile of repositories whose maintainers might plausibly accept a new MCP server. It is a volume play against review capacity, and on this occasion review capacity won: 19 of the 23 were closed and none were merged through GitHub's merge mechanism at the time Pillar reviewed them. Named artefacts were the hosted endpoint `productivity-suite-mcp.onrender.com/mcp` and a local delivery script `deadbug-mcp.py`.

**Why `real_harm: false` and why `high` anyway.** No pull request merged, so no downstream project is known to have shipped the server and no victim is confirmed — the archive records that as no real harm, and the number should not be inflated because the attempt was serious. It is nevertheless graded `high`: this is deployed adversary infrastructure aimed squarely at agent credentials, using a technique that defeats the standard pre-approval controls by design, and Pillar described the campaign as active with the disclosure left open for updates. The defensive lesson survives the failed delivery.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Pillar Security | <https://www.pillar.security/blog/deadbugz-currently-active-mcp-supply-chain-campaign> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-10` (raw: 2026-08-10, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`MCP`](../../taxonomy/types.md#mcp) MCP and tool-chain · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source: the research firm's own disclosure, with named accounts, artefacts and UTC timestamps |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-10-deadbugz-mcp-supply-chain` |

<sub>**Why this classification:** A real campaign in the wild rather than a demonstration, so `kind: incident` — but no pull request was merged and no victim is confirmed, so `real_harm: false`. Rated `high`: deployed adversary infrastructure targeting agent credentials with a technique specifically designed to pass pre-approval review, caught before delivery. Dated to the pull-request campaign (10 August) rather than to publication (12 August), per the archive's convention of dating by event. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-11` [GhostSplice: splitting one refused request across three trusted channels](2026-08-11-ghostsplice-cross-channel-fragmentation.md)<br>  <sub>Published a day later; the same surface, attacked by fragmentation rather than by delay</sub>
- `2026-08-18` [Context7 MCP prompt injection (CVE-2026-75130)](2026-08-18-context7-mcp-ti-shi-zhu.md)<br>  <sub>Hostile content reaching an agent through an MCP server</sub>
- `2025-09-25` [postmark-mcp malicious npm package](../2025-09/2025-09-25-postmark-mcp-npm.md)<br>  <sub>The first malicious MCP server found in the wild, also benign until a later version</sub>
- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>The same target — the agent's own configuration — at ecosystem scale</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-10-deadbugz-mcp-supply-chain.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
