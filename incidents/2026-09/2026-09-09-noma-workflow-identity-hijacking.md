---
id: 2026-09-09-noma-workflow-identity-hijacking
title: "Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access"
title_zh: "工作流身份劫持：Noma Labs 让一封普通支持邮件变成特权数据访问"
title_ja: "ワークフローIDハイジャック：Noma Labs、普通のサポートメールを特権データアクセスに変える"
title_ko: "워크플로 신원 하이재킹: Noma Labs, 평범한 지원 이메일을 특권 데이터 접근으로 바꾸다"
title_de: "Workflow Identity Hijacking: Noma Labs macht aus einer gewöhnlichen Support-E-Mail privilegierten Datenzugriff"
title_fr: "Détournement d'identité de workflow : Noma Labs transforme un simple e-mail de support en accès privilégié aux données"
title_es: "Secuestro de identidad de flujo de trabajo: Noma Labs convierte un correo de soporte normal en acceso privilegiado a datos"
date: 2026-09-09
date_raw: "2026-09-09"
date_precision: day

kind: research
type: [INFRA, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Noma Labs** describes **workflow identity hijacking**, a systemic authorization flaw in enterprise AI workflows — demonstrated with an ordinary message to a company's public support inbox that comes back with *“the quarterly sales numbers from the Finance Director's most recent email.”* No prompt injection is involved: the model is not manipulated, tricked or jailbroken; it reads the request, the pipeline executes exactly as designed, and the reply goes out — *“all the attacker had to do was ask.”* The root cause is that *“the identity and permissions of the user who triggers a workflow are decoupled from the identity and permissions used to execute it”*: AI workflows act with high-privilege service accounts or developer API keys instead of enforcing the requester's permissions, becoming *“unauthenticated proxies for privileged actions and silent data exfiltration.”* Noma says it reported the same risk vector in **Google Workflows**, and that Google acknowledged the report and **confirmed a fix** without disclosing implementation details — a vendor statement the archive records as Noma's claim, as Google has published nothing itself. The group's earlier discovery, **GitLost**, was the same boundary seen from one angle; this names the general pattern and moves the defense to identity-aware token delegation and authorization checkpoints outside the model

summary_zh: |
  **Noma Labs** 描述了**工作流身份劫持（workflow identity hijacking）**——企业 AI 工作流中的一类系统性授权缺陷。演示场景很简单：给公司公开的支持邮箱发一封普通消息，回信里带着*「财务总监最近一封邮件里的季度销售数字」*。全程没有提示注入：模型没有被操纵、诱骗或越狱，它读了请求，流水线完全按设计执行，回复发出——*「攻击者要做的只是开口问。」* 根因在于*「触发工作流的用户身份与权限，和执行工作流所用的身份与权限相互脱钩」*：AI 工作流以高权限服务账号或开发者 API 密钥行动，而不是按请求者的权限执行，从而变成*「特权操作的未认证代理与静默数据外泄通道」*。Noma 称它在 **Google Workflows** 中报告了同一风险点，谷歌确认收到并**确认已修复**，但未披露实现细节——这是 Noma 的陈述，谷歌自己尚未公开发布任何内容，本档案按此口径记录。该团队此前的发现 **GitLost** 是同一道边界的单侧视角；这一次给出了通用模式，并把防御移出模型：面向身份的令牌委派、在模型输出之后的授权检查点，以及数据检索与对外通信的非对称隔离

summary_ja: |
  **Noma Labs** は**ワークフローIDハイジャック**——企業AIワークフローに潜む体系的な認可の欠陥——を報告した。実演は単純だ。企業の公開サポート受信箱に普通のメッセージを送ると、返信に*「財務部長の最新メールにある四半期売上数字」*が含まれてくる。プロンプトインジェクションは一切ない。モデルは操作も欺瞞も脱獄もされておらず、リクエストを読み、パイプラインは設計どおりに実行し、返信が送られる——*「攻撃者はただ尋ねればよかった。」* 根本原因は、*「ワークフローを起動するユーザーの身元と権限が、それを実行する身元と権限から切り離されている」*ことにある。AIワークフローは高権限のサービスアカウントや開発者APIキーで動作し、要求者の権限を強制しないため、*「特権操作の未認証プロキシであり、静かなデータ流出路」*になる。Nomaは同じリスクを**Google Workflows**で報告し、Googleが報告を認めて**修正を確認した**と述べるが実装は非公開——これはNomaの主張であり、Google自身は何も公表していない。同チームの以前の発見**GitLost**は同じ境界の一断面であり、今回は一般パターンに命名し、防御をモデルの外——ID認識型のトークン委譲、モデル出力後の認可チェックポイント、データ取得と対外通信の非対称分離——へ移す

summary_ko: |
  **Noma Labs**가 **워크플로 신원 하이재킹(workflow identity hijacking)** — 기업 AI 워크플로에 숨은 체계적 인가 결함 — 을 발표했다. 시연은 단순하다. 회사의 공개 지원 메일함에 평범한 메시지를 보내면 답장으로 *"재무 담당 임원의 최근 이메일에 있던 분기 매출 수치"*가 돌아온다. 프롬프트 인젝션은 전혀 없다. 모델은 조작되거나 속거나 탈옥되지 않았고, 요청을 읽었으며 파이프라인은 설계대로 실행했고 답장이 나갔다 — *"공격자는 그저 물어보기만 하면 됐다."* 근본 원인은 *"워크플로를 트리거하는 사용자의 신원과 권한이 실행에 쓰이는 신원·권한과 분리되어 있는"* 것이다. AI 워크플로는 요청자의 권한을 강제하는 대신 고권한 서비스 계정이나 개발자 API 키로 행동해 *"특권 행위의 미인증 프록시이자 조용한 데이터 유출 통로"*가 된다. Noma는 같은 위험을 **Google Workflows**에서 보고했고 구글이 보고를 인정하고 **수정을 확인했다**고 밝히지만 구현은 비공개다. 이는 Noma의 주장이며 구글은 스스로 아무것도 공개하지 않았다. 같은 팀의 이전 발견 **GitLost**는 같은 경계의 한 단면이었고, 이번에는 일반 패턴에 이름을 붙이고 방어를 모델 밖 — 신원 인식 토큰 위임, 모델 출력 뒤의 인가 체크포인트, 데이터 조회와 외부 통신의 비대칭 분리 — 으로 옮긴다

summary_de: |
  **Noma Labs** beschreibt **Workflow Identity Hijacking** – ein systemisches Autorisierungsproblem in Unternehmens-KI-Workflows, demonstriert mit einer gewöhnlichen Nachricht an ein öffentliches Support-Postfach, die mit *„den Quartalsverkaufszahlen aus der letzten E-Mail der Finanzdirektorin“* zurückkommt. Kein Prompt Injection: Das Modell wird nicht manipuliert, getäuscht oder jailbroken; es liest die Anfrage, die Pipeline läuft exakt wie entworfen, die Antwort geht raus – *„der Angreifer musste nur fragen.“* Die Ursache: *„Identität und Berechtigungen des Nutzers, der einen Workflow auslöst, sind von der Identität und den Berechtigungen seiner Ausführung entkoppelt“* – KI-Workflows handeln mit hochprivilegierten Dienstkonten oder Entwickler-API-Schlüsseln, statt die Rechte des Anfragenden durchzusetzen, und werden so zu *„unauthentifizierten Proxys für privilegierte Aktionen und stiller Datenexfiltration.“* Noma zufolge wurde derselbe Risikovektor in **Google Workflows** gemeldet; Google habe den Bericht anerkannt und **einen Fix bestätigt**, ohne Details zu nennen – eine Aussage von Noma, Google selbst hat nichts veröffentlicht. Der frühere Fund **GitLost** war dieselbe Grenze aus einem Blickwinkel; dieser benennt das Muster und verlagert die Verteidigung nach außen: identitätsbewusste Token-Delegation, Autorisierungs-Checkpoints nach der Modellausgabe, asymmetrische Trennung von Datenabruf und Außenkommunikation

summary_fr: |
  **Noma Labs** décrit le **détournement d'identité de workflow**, un défaut d'autorisation systémique des workflows d'IA en entreprise — démontré par un simple message à la boîte support publique d'une société, auquel la réponse contient *« les chiffres de ventes trimestriels du dernier e-mail du directeur financier. »* Aucune injection de prompt : le modèle n'est ni manipulé, ni trompé, ni jailbreaké ; il lit la demande, le pipeline s'exécute comme prévu, la réponse part — *« l'attaquant n'a eu qu'à demander. »* La cause racine : *« l'identité et les permissions de l'utilisateur qui déclenche un workflow sont découplées de l'identité et des permissions utilisées pour l'exécuter »* — les workflows d'IA agissent avec des comptes de service à privilèges élevés ou des clés d'API, au lieu d'appliquer les permissions du demandeur, devenant *« des proxys non authentifiés pour des actions privilégiées et une exfiltration silencieuse de données. »* Noma dit avoir signalé le même vecteur dans **Google Workflows**, et que Google a reconnu le rapport et **confirmé un correctif**, sans en détailler l'implémentation — une affirmation de Noma, Google n'ayant rien publié. La découverte antérieure **GitLost** montrait la même frontière sous un angle ; celle-ci nomme le schéma général et déplace la défense hors du modèle : délégation de jetons sensible à l'identité, points de contrôle d'autorisation après la sortie du LLM, séparation asymétrique entre récupération de données et communications externes

summary_es: |
  **Noma Labs** describe el **secuestro de identidad de flujo de trabajo**, un fallo de autorización sistémico en flujos de IA empresariales — demostrado con un mensaje normal a la bandeja pública de soporte de una empresa que vuelve con *«las cifras trimestrales de ventas del último correo del director financiero»*. No hay inyección de prompt: el modelo no es manipulado, engañado ni jailbreakeado; lee la petición, el pipeline se ejecuta tal como fue diseñado y la respuesta sale — *«el atacante solo tuvo que preguntar»*. La causa raíz: *«la identidad y los permisos del usuario que dispara un flujo están desacoplados de la identidad y los permisos con los que se ejecuta»* — los flujos de IA actúan con cuentas de servicio de altos privilegios o claves de API, en lugar de aplicar los permisos del solicitante, y se convierten en *«proxies no autenticados de acciones privilegiadas y exfiltración silenciosa de datos»*. Noma afirma haber reportado el mismo vector en **Google Workflows**, y que Google reconoció el informe y **confirmó un arreglo**, sin detallar la implementación — una afirmación de Noma; Google no ha publicado nada. Su hallazgo anterior, **GitLost**, mostraba la misma frontera desde un ángulo; este nombra el patrón general y mueve la defensa fuera del modelo: delegación de tokens consciente de la identidad, puntos de control de autorización tras la salida del modelo y separación asimétrica entre recuperación de datos y comunicación externa

sources:
  - url: https://noma.security/noma-labs/workflow-identity-hijacking-the-silent-backdoor-in-ai-workflows
    label: Noma Labs (Noma Security)
  - url: https://www.darkreading.com/threat-intelligence/identity-based-ai-attack-security-enterprise-data
    label: Dark Reading

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

**Noma Labs** describes **workflow identity hijacking**, a systemic authorization flaw in enterprise AI workflows — demonstrated with an ordinary message to a company's public support inbox that comes back with *“the quarterly sales numbers from the Finance Director's most recent email.”* No prompt injection is involved: the model is not manipulated, tricked or jailbroken; it reads the request, the pipeline executes exactly as designed, and the reply goes out — *“all the attacker had to do was ask.”* The root cause is that *“the identity and permissions of the user who triggers a workflow are decoupled from the identity and permissions used to execute it”*: AI workflows act with high-privilege service accounts or developer API keys instead of enforcing the requester's permissions, becoming *“unauthenticated proxies for privileged actions and silent data exfiltration.”* Noma says it reported the same risk vector in **Google Workflows**, and that Google acknowledged the report and **confirmed a fix** without disclosing implementation details — a vendor statement the archive records as Noma's claim, as Google has published nothing itself. The group's earlier discovery, **GitLost**, was the same boundary seen from one angle; this names the general pattern and moves the defense to identity-aware token delegation and authorization checkpoints outside the model

## Attack chain

```mermaid
flowchart LR
    E["An attacker sends an ordinary request to a public entry point: support inbox, issue, web form"]:::entry
    S0["The AI workflow reads it and executes exactly as designed — with its creator's privileges"]:::step
    I["Privileged internal data is returned to someone with no authority to ask<br/><i>(no prompt injection; the authorization boundary itself is misplaced)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What it is, and what it is not.** Noma draws a clean line between three things. Direct prompt injection manipulates the model's instructions; indirect prompt injection hides malicious instructions in content the model later consumes; **workflow identity hijacking manipulates neither** — the attacker submits *“a normal, benign request through an unauthenticated entry point (such as a support inbox, GitHub issue, web form, or shared document),”* the model understands it correctly, and *“the core failure is that the requester had no authority to make that request.”* The illustration is deliberately mundane: *“What are the quarterly sales numbers from the Finance Director's most recent email?”* is a legitimate question from a CFO and a boundary violation from an outside sender — and standard prompt-injection detectors and guardrails classify the two inputs identically, because *“there is no malicious phrasing in the prompt; the security risk isn't in the prompt; it is in the authorization boundary.”* The root cause Noma names is an architectural decoupling: workflows execute downstream actions *“using high-privilege service accounts or developer API keys rather than enforcing the permissions of the external user,”* which makes every such automation *“an unauthenticated proxy for privileged actions and silent data exfiltration.”*

**Why existing defenses miss it.** The report's argument is that the market's controls target the wrong layer. Autonomous agents get tool-scoping and permission monitoring; static AI workflows — the pipeline shape where *“the LLM processes data or transforms text, but the deterministic pipeline around it controls the sequence of actions”* — do not, because their guardrails *“were not designed to serve as an authorization boundary.”* Auditing who can *trigger* a workflow is also insufficient when the workflow runs on a schedule against an inbox anyone can write to: *“Every automation must be assessed by the least-trusted party capable of influencing what it acts on.”* Noma connects this to its own July disclosure, **GitLost**, where a public GitHub issue assignment let external users pull private repository data through an agent that held organization-wide read access — the same boundary crossing, seen from the input side.

**The Google claim, and the caveats this record keeps.** Noma says it *“identified and responsibly reported this same risk vector within Google Workflows to Google. Google acknowledged Noma's report and confirmed a fix, without disclosing implementation details.”* The archive records that as Noma's statement: Google has published nothing, and no CVE or advisory anchors the Google find. The record is rated `research` / `medium` with `real_harm: false` because the demonstrations are the vendor's own, no named victim is attached, and the described exploitation is a design flaw rather than a campaign. What makes it worth recording is the re-framing: through a season of prompt-injection records, this is the reminder that many agent failures are not about the model at all — they are about whose authority the workflow borrows, and whether anyone checks that the answer is allowed. The defenses Noma proposes are correspondingly outside the model: identity-aware token delegation, authorization checkpoints between LLM output and any downstream action, and structural separation between data retrieval and external response channels.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Noma Labs (Noma Security) | <https://noma.security/noma-labs/workflow-identity-hijacking-the-silent-backdoor-in-ai-workflows> |
| 2 | Dark Reading | <https://www.darkreading.com/threat-intelligence/identity-based-ai-attack-security-enterprise-data> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-09` (raw: 2026-09-09, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source: Noma Labs' own write-up; the Google fix is recorded explicitly as Noma's claim |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-09-noma-workflow-identity-hijacking` |

<sub>**Why this classification:** A vendor research disclosure with a clear, checkable mechanism and no named victim; `medium` / `real_harm: false` follows the archive's treatment of the GitLost and ForcedLeak design-flaw records. Classified `INFRA` (the flaw lives in the workflow platform's execution identity) with `EXFIL` (data leaves to an unauthorised requester) — and deliberately **not** `IPI`, which is the distinction the research itself is built on. Dated to the Noma Labs post (9 September 2026). Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md) · [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-07-07` [GitLost: GitHub Agentic Workflows leak private repositories](../2026-07/2026-07-07-gitlost-github-agentic-workflows.md)<br>  <sub>The same authorization boundary, from the same team</sub>
- `2026-09-01` [OWASP publishes the Agent Control Standard and formally announces the 2026 LLM Top 10](../2026-09/2026-09-01-owasp-agent-control-standard.md)<br>  <sub>The standard aimed at exactly this class of boundary failure</sub>
- `2025-09-25` [ForcedLeak (Salesforce Agentforce)](../2025-09/2025-09-25-forcedleak-salesforce-agentforce.md)<br>  <sub>An earlier enterprise-agent data-return flaw</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-09-noma-workflow-identity-hijacking.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
