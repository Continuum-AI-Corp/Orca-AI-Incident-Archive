---
id: 2026-09-23-ibm-ftm-rag-poisoning
title: "IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools"
title_zh: "IBM FTM：未授权 RAG 投毒可操纵支付 agent 的 MCP 工具调用"
title_ja: "IBM FTM：未認証のRAGポイズニングが決済エージェントのMCPツールを操作可能"
title_ko: "IBM FTM: 미인증 RAG 포이즈닝이 결제 에이전트의 MCP 도구 호출을 조종할 수 있었다"
title_de: "IBM FTM: Unauthentifiziertes RAG-Poisoning konnte die MCP-Tools des Zahlungsagenten steuern"
title_fr: "IBM FTM : un empoisonnement RAG non authentifié pouvait piloter les outils MCP de l'agent de paiement"
title_es: "IBM FTM: el envenenamiento RAG no autenticado podía dirigir las herramientas MCP del agente de pagos"
date: 2026-09-23
date_raw: "2026-09-23"
date_precision: day

kind: vulnerability
type: [IPI, INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **IBM discloses a flaw in the AI agent server of Financial Transaction Manager (FTM): an unauthenticated attacker can insert malicious runbook content into the agent's vector database and thereby steer its MCP tool calls** — *"potentially triggering unauthorized payment actions or exfiltrating payment data."* The advisory (CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N`; CWE-74) locates the issue in `api.vectordb.runbooks.js:51` — an **unauthenticated runbook upsert**. It is the archive's first **RAG-poisoning** case: instead of injecting instructions through a page or document the agent fetches, the attacker writes the poisoned "knowledge" straight into the retrieval store the agent trusts, so the agent's own tools execute what the poisoned entry suggests. No exploitation in the wild is known. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`, following the archive's treatment of un-exploited agent-infrastructure CVEs

summary_zh: |
  **IBM 披露 Financial Transaction Manager（FTM）AI agent 服务器中的一处缺陷：未授权攻击者可以向该 agent 的向量数据库插入恶意 runbook 内容，从而操纵其 MCP 工具调用**——*「可能触发未授权支付操作或外泄支付数据。」* 该公告（CVE-2026-18875，CVSS 3.1 **7.3**，`AV:N/AC:L/PR:N/UI:N`；CWE-74）把问题定位在 `api.vectordb.runbooks.js:51`——一处**未授权的 runbook upsert（插入/更新）**。这是本档案首个 **RAG 投毒**案例：攻击者不通过 agent 抓取的页面或文档注入指令，而是把投毒的「知识」直接写进 agent 所信任的检索库，于是 agent 自己的工具就会执行投毒条目所建议的动作。目前无在野利用。本条记为 `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`，沿用档案对未在野 agent 基础设施 CVE 的处理口径

summary_ja: |
  **IBMがFinancial Transaction Manager（FTM）のAIエージェントサーバーにおける欠陥を公表：未認証の攻撃者がエージェントのベクターデータベースに悪意あるrunbookコンテンツを挿入し、それによってMCPツール呼び出しを誘導できる**——*「未承認の支払い操作や支払いデータの外部送信を引き起こす可能性がある」*。勧告（CVE-2026-18875、CVSS 3.1 **7.3**、`AV:N/AC:L/PR:N/UI:N`、CWE-74）は問題を`api.vectordb.runbooks.js:51`——**未認証のrunbookアップサート**——に特定している。これは本アーカイブ初の**RAGポイズニング**事例である。攻撃者はエージェントが取得するページや文書を介さず、信頼された検索ストアに毒入りナレッジを直接書き込む。実環境での悪用は知られていない

summary_ko: |
  **IBM이 Financial Transaction Manager(FTM)의 AI 에이전트 서버 결함을 공개했다: 미인증 공격자가 에이전트의 벡터 데이터베이스에 악성 runbook 콘텐츠를 삽입해 MCP 도구 호출을 조종할 수 있다** — *"미승인 결제 작업을 유발하거나 결제 데이터를 유출할 가능성이 있다."* 권고문(CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N`, CWE-74)은 문제를 `api.vectordb.runbooks.js:51` — **미인증 runbook upsert** — 로 특정했다. 본 아카이브 최초의 **RAG 포이즈닝** 사례다: 공격자는 에이전트가 가져오는 페이지나 문서를 통하지 않고, 에이전트가 신뢰하는 검색 저장소에 오염된 지식을 직접 기록한다. 실제 악용은 알려지지 않았다

summary_de: |
  **IBM meldet eine Schwachstelle im KI-Agenten-Server des Financial Transaction Manager (FTM): Ein nicht authentifizierter Angreifer kann bösartigen Runbook-Inhalt in die Vektordatenbank des Agenten einfügen und dadurch dessen MCP-Tool-Aufrufe steuern** – *„möglicherweise unautorisierte Zahlungsvorgänge auslösend oder Zahlungsdaten exfiltrierend.“* Die Advisory (CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N`; CWE-74) verortet das Problem in `api.vectordb.runbooks.js:51` – einem **nicht authentifizierten Runbook-Upsert**. Es ist der erste **RAG-Poisoning**-Fall des Archivs: Der Angreifer schreibt das vergiftete „Wissen“ direkt in den vom Agenten vertrauten Retrieval-Store. Ausnutzung in freier Wildbahn ist nicht bekannt

summary_fr: |
  **IBM divulgue une faille dans le serveur d'agent IA de Financial Transaction Manager (FTM) : un attaquant non authentifié peut insérer du contenu runbook malveillant dans la base vectorielle de l'agent et ainsi piloter ses appels d'outils MCP** — *« susceptible de déclencher des opérations de paiement non autorisées ou d'exfiltrer des données de paiement »*. L'avis (CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N` ; CWE-74) situe le problème dans `api.vectordb.runbooks.js:51` — un **upsert runbook non authentifié**. C'est le premier cas d'**empoisonnement RAG** de l'archive : l'attaquant écrit directement le « savoir » empoisonné dans le store de récupération auquel l'agent fait confiance. Aucune exploitation réelle n'est connue

summary_es: |
  **IBM divulga una falla en el servidor de agente de IA de Financial Transaction Manager (FTM): un atacante no autenticado puede insertar contenido runbook malicioso en la base vectorial del agente y dirigir así sus llamadas a herramientas MCP** — *«potencialmente desencadenando operaciones de pago no autorizadas o exfiltrando datos de pago»*. El aviso (CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N`; CWE-74) sitúa el problema en `api.vectordb.runbooks.js:51` — un **upsert de runbook no autenticado**. Es el primer caso de **envenenamiento RAG** del archivo: el atacante escribe el «conocimiento» envenenado directamente en el almacén de recuperación en el que confía el agente. No se conoce explotación real

sources:
  - url: https://www.ibm.com/support/pages/node/7288641
    label: IBM Support
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-18875
    label: NVD

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**IBM discloses a flaw in the AI agent server of Financial Transaction Manager (FTM): an unauthenticated attacker can insert malicious runbook content into the agent's vector database and thereby steer its MCP tool calls** — *"potentially triggering unauthorized payment actions or exfiltrating payment data."* The advisory (CVE-2026-18875, CVSS 3.1 **7.3**, `AV:N/AC:L/PR:N/UI:N`; CWE-74) locates the issue in `api.vectordb.runbooks.js:51` — an **unauthenticated runbook upsert**. It is the archive's first **RAG-poisoning** case: instead of injecting instructions through a page or document the agent fetches, the attacker writes the poisoned "knowledge" straight into the retrieval store the agent trusts, so the agent's own tools execute what the poisoned entry suggests. No exploitation in the wild is known. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`, following the archive's treatment of un-exploited agent-infrastructure CVEs

## Attack chain

```mermaid
flowchart LR
    E["Unauthenticated attacker reaches<br/>the runbook upsert endpoint"]:::entry
    S1["Poisoned runbook lands in the agent's<br/>vector database"]:::step
    S2["The agent retrieves it as trusted knowledge<br/>and steers its MCP tool calls"]:::step
    I["Potential: unauthorised payment actions<br/>or payment-data exfiltration"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The advisory, in its own words.** IBM's support note lists **CVE-2026-18875**: *"IBM Financial Transaction Manager (FTM) 4.x is vulnerable to RAG poisoning via unauthenticated runbook upsert (CWE-74) in the FTM AI agent server (api.vectordb.runbooks.js:51). An unauthenticated attacker can insert malicious runbook content into the agent's vector database to steer AI-driven MCP tool calls, potentially triggering unauthorized payment actions or exfiltrating payment data."* CVSS 3.1 base score **7.3** (`AV:N/AC:L/PR:N/UI:N/S:U/C:L/I:L/A:L`), weakness CWE-74 (injection). The NVD entry mirrors the advisory; no exploitation in the wild is recorded, and no public PoC is referenced.

**Why this is a distinct pattern.** The archive's injection records so far are **indirect prompt injection** in the classical sense: the payload rides in content the agent fetches — a web page, an email, a repository file, a dataset. This case is a **direct write into the retrieval store itself**: the runbook upsert endpoint accepts unauthenticated writes, so the attacker skips the delivery problem entirely and plants the poisoned instructions where the agent's retrieval step is *designed* to trust them. It is, for the archive, the first entry where the vector database is both the injection point and — under the `INFRA` lens (exposed vector stores) — the exposed asset, and where the payload's stated goal is steering **MCP tool calls** rather than text output. The combination is exactly the failure mode defenders have been warned about for RAG-based agent stacks, now with a CVE number on an enterprise payments product.

**Context and grading.** FTM is an enterprise payments product (4.x, on Red Hat OpenShift); the affected AI agent server sits in that stack, and the vendor's own impact statement ties the poisoned tool calls to payment actions — so the *potential* blast radius is financial, even though the severity here is bounded by what actually happened: **no exploitation, no confirmed harm**. The archive therefore records it as `vulnerability` / `medium` / `real_harm: false`, the same treatment given to other un-exploited agent-infrastructure CVEs (Bifrost, WSP-type plugin flaws and the MCP tool CVEs of 2025). It is dated to the NVD publication (23 September 2026), matching IBM's advisory release window.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | IBM Support | <https://www.ibm.com/support/pages/node/7288641> |
| 2 | NVD | <https://nvd.nist.gov/vuln/detail/CVE-2026-18875> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-23` (raw: 2026-09-23, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **Medium** `medium` |
| Confidence | **A** — vendor advisory (IBM) plus the NVD record |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-23-ibm-ftm-rag-poisoning` |

<sub>**Why this classification:** A disclosed flaw in an enterprise vendor's AI agent server — the poisoned retrieval store is both the injection vector (`IPI`, dataset-class source) and the exposed runtime asset (`INFRA`) — with no known exploitation, hence `vulnerability` / `real_harm: false`. Rated `medium` per the archive's severity ladder: a moderate flaw (CVSS 7.3, unauthenticated) without evidence of use; `high` would require CVSS 9+ or confirmed damage. Dated to NVD publication (23 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-09-14` [Bifrost AI gateway: CVE-2026-90898](2026-09-14-bifrost-ai-gateway-cve-2026-90898.md)<br>  <sub>The other September AI-infrastructure CVE - unauthenticated, agent-facing</sub>
- `2026-09-02` [Langflow exploited in the wild](2026-09-02-langflow-jin-di-ye-li.md)<br>  <sub>When agent-platform flaws do get used</sub>
- `2025-06-04` [Asana MCP server flaw](../2025-06/2025-06-04-asana-mcp-server.md)<br>  <sub>Earlier MCP-tool exposure in the same lineage</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-23-ibm-ftm-rag-poisoning.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
