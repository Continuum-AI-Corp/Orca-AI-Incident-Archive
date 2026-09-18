---
id: 2026-07-07-gitlost-github-agentic-workflows
title: "GitLost: GitHub Agentic Workflows leak private repositories"
title_zh: "GitLost：GitHub Agentic Workflows 泄露私有仓库"
title_ja: "GitLost：GitHub Agentic Workflowsが非公開リポジトリを漏えい"
title_ko: "GitLost: GitHub 에이전틱 워크플로가 비공개 저장소를 유출"
title_de: "GitLost: GitHub Agentic Workflows geben private Repositories preis"
title_fr: "GitLost : les Agentic Workflows de GitHub font fuiter des dépôts privés"
title_es: "GitLost: los flujos de trabajo agénticos de GitHub filtran repositorios privados"
date: 2026-07-07
date_precision: day
date_raw: "2026-07-07"

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Noma Labs: an attacker only needs to open an Issue in the same organisation's **public** repo disguised as a business request, with plaintext instructions in the body — **no code knowledge, credentials or permissions required**. The agent complies and posts the private repo's README content as a public comment. Preconditions: the workflow is triggered by Issue assignment and holds both cross-repo read and comment permissions. GitHub's guardrail is bypassed by adding an "**Additionally**" (which turns it into rewriting the output rather than refusing). ⚠️ Reproduced in a controlled environment, **no real victim**


summary_zh: |
  Noma Labs：攻击者只需在同组织的**公开**仓库开一个伪装成业务需求的 Issue，正文里写明文指令 —— **不需要代码知识、凭据或权限**。agent 照做，把私有仓库 README 内容作为公开评论发出。成立条件：该工作流由 Issue 指派触发、同时具备跨仓读取与评论权限。GitHub 的护栏加一个 "**Additionally**" 就被绕过（变成改写输出而非拒绝）。⚠️ 验证环境复现，**非真实受害**

summary_ja: |
  Noma Labs：攻撃者は同じ組織の**公開**リポジトリで、ビジネス依頼を装ったIssueを開き、本文に平文の指示を書くだけでよい——**コードの知識も認証情報も権限も不要**。エージェントはそれに従い、非公開リポジトリのREADMEの内容を公開コメントとして投稿する。前提条件：ワークフローがIssueのアサインでトリガーされ、クロスリポジトリの読み取りとコメントの両方の権限を持つこと。GitHubのガードレールは「**Additionally**」を追加することで回避される（拒否ではなく出力の書き換えに変わる）。⚠️ 管理された環境での再現であり、**実際の被害者はなし**

summary_ko: |
  Noma Labs: 공격자는 같은 조직의 **공개** 저장소에 업무 요청으로 위장한 이슈를 열고 본문에 평문 지시를 넣기만 하면 된다 — **코드 지식, 자격 증명, 권한이 전혀 필요 없다**. 에이전트가 이를 따르고 비공개 저장소의 README 내용을 공개 댓글로 게시한다. 전제 조건: 워크플로가 이슈 할당으로 작동하고 저장소 간 읽기와 댓글 권한을 모두 보유해야 한다. GitHub의 가드레일은 "**Additionally**"를 덧붙이면 우회된다(거부 대신 출력 재작성으로 처리하게 만든다). ⚠️ 통제된 환경에서 재현되었고 **실제 피해자는 없다**

summary_de: |
  Noma Labs: Ein Angreifer muss nur ein Issue im **öffentlichen** Repository derselben Organisation öffnen, als Geschäftsanfrage getarnt und mit Klartextanweisungen im Text — **keine Codekenntnisse, Zugangsdaten oder Berechtigungen nötig**. Der Agent befolgt sie und veröffentlicht den README-Inhalt des privaten Repositories als öffentlichen Kommentar. Vorbedingungen: Der Workflow wird durch Issue-Zuweisung ausgelöst und besitzt sowohl repositoryübergreifende Lese- als auch Kommentarberechtigungen. GitHubs Guardrail wird umgangen, indem man ein „**Additionally**“ hinzufügt (was es zu einer Umschreibung der Ausgabe statt einer Verweigerung macht). ⚠️ In einer kontrollierten Umgebung reproduziert, **kein reales Opfer**

summary_fr: |
  Noma Labs : il suffit à un attaquant d'ouvrir une issue dans le dépôt **public** de la même organisation, déguisée en demande métier avec des instructions en clair dans le corps — **aucune connaissance du code, d'identifiants ou de permissions n'est requise**. L'agent obéit et publie le contenu du README du dépôt privé en commentaire public. Préconditions : le workflow est déclenché par l'assignation d'une issue et détient à la fois la lecture inter-dépôts et la permission de commenter. Le garde-fou de GitHub est contourné en ajoutant un « **Additionally** » (qui transforme le refus en réécriture de la sortie). ⚠️ Reproduit en environnement contrôlé, **aucune victime réelle**

summary_es: |
  Noma Labs: un atacante solo necesita abrir un Issue en el repositorio **público** de la misma organización disfrazado de solicitud de negocio, con instrucciones en texto plano en el cuerpo — **no se necesitan conocimientos de código, credenciales ni permisos**. El agente obedece y publica el contenido del README del repositorio privado como comentario público. Precondiciones: el flujo de trabajo se activa al asignar un Issue y tiene permisos de lectura entre repositorios y de comentar. El guardrail de GitHub se elude añadiendo un "**Additionally**" (lo que lo convierte en reescribir la salida en lugar de negarse). ⚠️ Reproducido en un entorno controlado, **sin víctima real**

sources:
  - url: https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/
    label: Noma Labs
  - url: https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/
    label: GitHub feature announcement

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# GitLost: GitHub Agentic Workflows leak private repositories

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Noma Labs: an attacker only needs to open an Issue in the same organisation's **public** repo disguised as a business request, with plaintext instructions in the body — **no code knowledge, credentials or permissions required**. The agent complies and posts the private repo's README content as a public comment. Preconditions: the workflow is triggered by Issue assignment and holds both cross-repo read and comment permissions. GitHub's guardrail is bypassed by adding an "**Additionally**" (which turns it into rewriting the output rather than refusing). ⚠️ Reproduced in a controlled environment, **no real victim**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Noma Labs | <https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/> |
| 2 | GitHub feature announcement | <https://github.blog/changelog/2026-02-13-github-agentic-workflows-are-now-in-technical-preview/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-07` (raw: 2026-07-07, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-07-gitlost-github-agentic-workflows` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-07-02` [Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)](2026-07-02-hidden-web-instructions-payment-fraud.md)<br>  <sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-12` [Agentjacking: one public DSN hijacks AI coding agents](../2026-06/2026-06-12-agentjacking-public-dsn.md)<br>  <sub>Agentjacking: one public DSN hijacks AI coding agents</sub>
- `2026-08-19` [Grok "cryptographic context injection": encrypted instructions, plaintext data](../2026-08/2026-08-19-grok-mi-ma-xue-wen.md)<br>  <sub>Grok "cryptographic context injection": encrypted instructions, plaintext data</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-07-gitlost-github-agentic-workflows.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
