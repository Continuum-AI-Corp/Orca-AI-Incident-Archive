---
id: 2026-09-01-owasp-agent-control-standard
title: "OWASP publishes the Agent Control Standard and formally announces the 2026 LLM Top 10"
title_zh: "OWASP 发布 Agent Control Standard，并正式公布 2026 版 LLM Top 10"
title_ja: "OWASP、Agent Control Standardを公開しLLM Top 10 2026を正式発表"
title_ko: "OWASP, Agent Control Standard를 공개하고 2026 LLM Top 10을 공식 발표"
title_de: "OWASP veröffentlicht den Agent Control Standard und kündigt offiziell die LLM Top 10 2026 an"
title_fr: "OWASP publie l'Agent Control Standard et annonce officiellement le LLM Top 10 2026"
title_es: "OWASP publica el Agent Control Standard y anuncia formalmente el LLM Top 10 2026"
date: 2026-09-01
date_raw: "2026-09-01"
date_precision: day

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **The OWASP GenAI Security Project** publishes the **Agent Control Standard (ACS)** on 1 September — an open foundation for controlling enterprise agents, which the project says must be *“inspectable, traceable and instrumentable”*: showing what they are, what they can access, what they did and why. ACS defines how agent platforms expose **middleware hooks** and how safety policies can be enforced through them, enabling **declarative controls that are portable across agent frameworks and enforced at runtime**. It appears in the same September release round that formally announces the **OWASP GenAI LLM Top 10 2026** — a community guide developed with hundreds of AI security experts and grounded in thousands of real-world incidents, mapping risks to NIST, MITRE ATLAS, CWE and the OWASP Top 10 for Agentic Applications — whose resource page had already been online since **3 August**. Recorded as a governance marker: the control layer for agents is being standardised while the year's agent incidents accumulate, and this archive treats it as policy, not an incident

summary_zh: |
  **OWASP GenAI Security Project** 于 9 月 1 日发布 **Agent Control Standard（ACS）**——一个面向企业 agent 控制的开源基础，项目方称 agent 必须*「可检查、可追踪、可插桩」*：能看清它们是什么、能访问什么、做了什么以及为什么。ACS 定义了 agent 平台如何暴露**中间件钩子（middleware hooks）**、安全策略又如何通过这些钩子强制执行，从而提供**声明式、可跨 agent 框架移植、在运行时生效的控制**。它与正式公布 **2026 版 OWASP GenAI LLM Top 10** 的九月发布批次同期——后者由数百名 AI 安全专家共同开发、以数千起真实事件为依据，并把风险映射到 NIST、MITRE ATLAS、CWE 和 OWASP Agentic Applications Top 10；其资源页其实早在 **8 月 3 日**就已上线。收录它是作为治理层的标记：agent 的控制层正在被标准化，而今年的 agent 事故仍在累积；本档案将其视为政策类条目而非事故

summary_ja: |
  **OWASP GenAI Security Project** は9月1日、**Agent Control Standard（ACS）** を公開した。エンタープライズ向けエージェント制御のオープンな基盤であり、エージェントは*「検査可能・追跡可能・計装可能」*——何であるか、何にアクセスできるか、何をしたか、なぜそうしたかが見えるべきだと位置づける。ACSはエージェント基盤が**ミドルウェアフック**をどう公開し、安全ポリシーをそこを通じてどう強制するかを定義し、**エージェントフレームワーク間で移植可能で、実行時に適用される宣言的コントロール**を可能にする。同じ9月のリリースラウンドでは**OWASP GenAI LLM Top 10 2026**も正式発表された——数百名の専門家が開発し、数千件の実事例に基づき、リスクをNIST、MITRE ATLAS、CWE、OWASP Agentic Applications Top 10へマッピングするガイドで、リソースページ自体は**8月3日**から公開されていた。本年もエージェント事故が積み上がる中で制御層の標準化が進んでいることを示すガバナンスの記録であり、本アーカイブではインシデントではなく政策として扱う

summary_ko: |
  **OWASP GenAI Security Project**가 9월 1일 **Agent Control Standard(ACS)**를 공개했다. 기업 에이전트 통제를 위한 오픈 기반으로, 프로젝트는 에이전트가 *"검사 가능하고, 추적 가능하며, 계측 가능"*해야 한다고 말한다. 즉 무엇인지, 무엇에 접근할 수 있는지, 무엇을 했고 왜 했는지가 보여야 한다. ACS는 에이전트 플랫폼이 **미들웨어 훅**을 어떻게 노출하고, 보안 정책을 그 훅을 통해 어떻게 강제하는지 정의해, **에이전트 프레임워크 간에 이식 가능하고 런타임에 적용되는 선언적 통제**를 가능하게 한다. 같은 9월 릴리스 라운드에서 **OWASP GenAI LLM Top 10 2026**도 공식 발표됐다. 수백 명의 전문가가 개발하고 수천 건의 실제 사건에 기반해 위험을 NIST, MITRE ATLAS, CWE, OWASP Agentic Applications Top 10에 매핑한 가이드이며, 리소스 페이지 자체는 **8월 3일**부터 온라인이었다. 올해도 에이전트 사고가 쌓이는 가운데 통제 계층이 표준화되고 있음을 보여주는 거버넌스 기록이며, 이 아카이브는 이를 사건이 아닌 정책으로 취급한다

summary_de: |
  **Das OWASP GenAI Security Project** veröffentlicht am 1. September den **Agent Control Standard (ACS)** – eine offene Grundlage für die Kontrolle von Unternehmensagenten, die laut Projekt *„inspizierbar, nachverfolgbar und instrumentierbar“* sein müssen: sichtbar darin, was sie sind, worauf sie zugreifen können, was sie getan haben und warum. ACS definiert, wie Agentenplattformen **Middleware-Hooks** bereitstellen und wie Sicherheitsrichtlinien darüber durchgesetzt werden – **deklarative Kontrollen, die über Agenten-Frameworks hinweg portierbar und zur Laufzeit wirksam sind**. Im selben September-Release wird die **OWASP GenAI LLM Top 10 2026** offiziell angekündigt – ein mit Hunderten Expertinnen und Experten entwickelter Leitfaden auf Basis Tausender realer Vorfälle, der Risiken auf NIST, MITRE ATLAS, CWE und die OWASP Top 10 for Agentic Applications abbildet – deren Ressourcenseite bereits seit dem **3. August** online war. Festgehalten als Governance-Marker: Die Kontrollschicht für Agenten wird standardisiert, während die Agentenvorfälle des Jahres weiter zunehmen; dieses Archiv führt den Eintrag als Politik, nicht als Vorfall

summary_fr: |
  **L'OWASP GenAI Security Project** publie le 1er septembre l'**Agent Control Standard (ACS)** — une base ouverte pour le contrôle des agents en entreprise, qui doivent selon le projet être *« inspectables, traçables et instrumentables »* : montrer ce qu'ils sont, ce à quoi ils accèdent, ce qu'ils ont fait et pourquoi. L'ACS définit comment les plateformes d'agents exposent des **hooks de middleware** et comment les politiques de sécurité y sont appliquées, permettant des **contrôles déclaratifs, portables entre frameworks d'agents et appliqués à l'exécution**. Il paraît dans la même vague de septembre qui annonce officiellement l'**OWASP GenAI LLM Top 10 2026** — un guide développé avec des centaines d'experts, fondé sur des milliers d'incidents réels et mappé vers NIST, MITRE ATLAS, CWE et l'OWASP Top 10 for Agentic Applications — dont la page ressource était déjà en ligne depuis le **3 août**. Consigné comme jalon de gouvernance : la couche de contrôle des agents se normalise pendant que les incidents de l'année s'accumulent ; cette archive le classe en politique, non en incident

summary_es: |
  **El OWASP GenAI Security Project** publica el 1 de septiembre el **Agent Control Standard (ACS)** — una base abierta para el control de agentes empresariales, que según el proyecto deben ser *«inspeccionables, trazables e instrumentables»*: mostrar qué son, a qué pueden acceder, qué hicieron y por qué. El ACS define cómo las plataformas de agentes exponen **hooks de middleware** y cómo se aplican las políticas de seguridad a través de ellos, habilitando **controles declarativos portables entre frameworks de agentes y aplicados en tiempo de ejecución**. Aparece en la misma tanda de septiembre que anuncia formalmente el **OWASP GenAI LLM Top 10 2026** —una guía desarrollada con cientos de expertos, basada en miles de incidentes reales y mapeada a NIST, MITRE ATLAS, CWE y el OWASP Top 10 for Agentic Applications— cuya página de recurso ya estaba en línea desde el **3 de agosto**. Se registra como hito de gobernanza: la capa de control de agentes se estandariza mientras los incidentes del año se acumulan; este archivo lo trata como política, no como incidente

sources:
  - url: https://genai.owasp.org/resource/agent-control-standard-acs/
    label: OWASP Agent Control Standard (ACS)
  - url: https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/
    label: OWASP GenAI LLM Top 10 2026
  - url: https://genai.owasp.org/resources/
    label: OWASP GenAI Security Project — Resources Archive
  - url: https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/
    label: OWASP press release
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/
    label: Cloud Security Alliance

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# OWASP publishes the Agent Control Standard and formally announces the 2026 LLM Top 10

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

**The OWASP GenAI Security Project** publishes the **Agent Control Standard (ACS)** on 1 September — an open foundation for controlling enterprise agents, which the project says must be *“inspectable, traceable and instrumentable”*: showing what they are, what they can access, what they did and why. ACS defines how agent platforms expose **middleware hooks** and how safety policies can be enforced through them, enabling **declarative controls that are portable across agent frameworks and enforced at runtime**. It appears in the same September release round that formally announces the **OWASP GenAI LLM Top 10 2026** — a community guide developed with hundreds of AI security experts and grounded in thousands of real-world incidents, mapping risks to NIST, MITRE ATLAS, CWE and the OWASP Top 10 for Agentic Applications — whose resource page had already been online since **3 August**. Recorded as a governance marker: the control layer for agents is being standardised while the year's agent incidents accumulate, and this archive treats it as policy, not an incident

## Attack chain

```mermaid
flowchart LR
    A["A community standard for controlling enterprise agents"]:::entry
    B["Platforms expose middleware hooks; policies are declared once and enforced at runtime"]:::step
    C["Agents become inspectable, traceable and instrumentable across frameworks<br/><i>(the intended path — no incident is claimed)</i>"]:::impact
    A --> B --> C
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What the standard proposes.** ACS starts from a trust argument: *“Widescale adoption of AI agents depends on trust, and trust requires transparency and control. Enterprises cannot rely on black-box agents operating across cloud, SaaS, on-premises and endpoint environments.”* The mechanism it standardises is a middleware layer — hooks that agent platforms expose so that safety policies can be attached to an agent's actions and enforced while it runs, rather than only reviewed before deployment. The controls are **declarative** (expressed as policy, not code wired into each integration) and **portable across agent frameworks**, which is the part enterprises have lacked while agent tooling fragments: *“Together, transparency and standardized control provide the foundation for trustworthy agents at enterprise scale.”* The project notes the standard is now part of the OWASP GenAI Security Project. The CSA’s review of the release adds detail on what that makes ACS: a **donated** specification at **version 0.1**, built around an Agent Control System with “guardian agent” enforcement points, an observability layer using OpenTelemetry and OCSF, and an **Agent Bill of Materials (AgBOM)** in CycloneDX, SWID and SPDX formats — with instrumentation samples and further protocol support targeted for later versions.

**What shipped alongside it.** The same 1 September round carries the **GenAI Security Industry Framework Crosswalk**, which maps 51 GenAI vulnerabilities across four source lists to established governance and compliance frameworks. The round also formally announces the **OWASP GenAI LLM Top 10 2026** — “updated rankings, expanded threat coverage, and new research grounded in thousands of real-world AI security incidents”, developed by hundreds of experts and mapped to NIST, MITRE ATLAS, CWE and the OWASP Top 10 for Agentic Applications. One precision note: the Top 10's resource page has been live since **3 August**; the September dates in the announcement round refer to the formal launch, and this record is dated to the ACS release.

**How to read it.** This is a framework release, not an incident: `kind: policy`, `severity: info`, `real_harm: null`, and like the archive's other policy records it is excluded from incident counts. It is recorded because it marks the defensive side of the year's central lesson — that agent failures cluster at identity, permission and control boundaries rather than in model behaviour. The same week the standard appeared, Noma Labs published a design flaw (workflow identity hijacking) that is almost a worked example of what an enforced authorization boundary would have prevented.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OWASP Agent Control Standard (ACS) | <https://genai.owasp.org/resource/agent-control-standard-acs/> |
| 2 | OWASP GenAI LLM Top 10 2026 | <https://genai.owasp.org/resource/owasp-genai-llm-top-10-2026/> |
| 3 | OWASP GenAI Security Project — Resources Archive | <https://genai.owasp.org/resources/> |
| 4 | OWASP press release | <https://genai.owasp.org/2026/09/01/owasp-genai-security-project-unveils-2026-top-10-for-llm-applications-new-agent-control-standard-and-sponsors-as-community-tops-30000-members/> |
| 5 | Cloud Security Alliance | <https://labs.cloudsecurityalliance.org/research/csa-research-note-owasp-genai-top10-2026-agent-control-stand/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-01` (raw: 2026-09-01, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source: the standards body's own resource pages |
| Real harm | Not applicable |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-01-owasp-agent-control-standard` |

<sub>**Why this classification:** A standards release with no incident attached — recorded as `kind: policy` / `GOV` / `info`, excluded from incident counts like the archive's other policy entries. Dated to the ACS resource page (1 September 2026); the LLM Top 10 2026 page carries 3 August as its own date and is described here as the same round's formal announcement. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-09-09` [Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access](../2026-09/2026-09-09-noma-workflow-identity-hijacking.md)<br>  <sub>The design flaw an enforced authorization boundary would have prevented</sub>
- `2026-07-27` [NVIDIA convenes the Open Secure AI Alliance](../2026-07/2026-07-27-nvidia-open-secure-alliance.md)<br>  <sub>Another defensive-side project from the same quarter</sub>
- `2026-07-17` [Anthropic, "A CISO's guide to agentic AI"](../2026-07/2026-07-17-anthropic-ciso-guide-agentic.md)<br>  <sub>Vendor-side guidance on securing agent deployments</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-01-owasp-agent-control-standard.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
