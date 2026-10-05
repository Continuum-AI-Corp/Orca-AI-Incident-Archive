---
id: 2026-10-02-gitlab-duo-ai-gateway-rce
title: "GitLab Duo AI Gateway: a prompt-template sandbox escape runs commands on the host (CVE-2026-90970)"
title_zh: "GitLab Duo AI Gateway：提示模板沙箱逃逸可在主机执行命令（CVE-2026-90970）"
title_ja: "GitLab Duo AIゲートウェイ：プロンプトテンプレートのサンドボックス脱出でホスト上でコマンド実行（CVE-2026-90970）"
title_ko: "GitLab Duo AI 게이트웨이: 프롬프트 템플릿 샌드박스 탈출로 호스트에서 명령 실행 (CVE-2026-90970)"
title_de: "GitLab Duo AI Gateway: Ein Prompt-Template-Sandbox-Ausbruch führt Befehle auf dem Host aus (CVE-2026-90970)"
title_fr: "GitLab Duo AI Gateway : une évasion du bac à sable de modèle de prompt exécute des commandes sur l'hôte (CVE-2026-90970)"
title_es: "GitLab Duo AI Gateway: una fuga del sandbox de plantillas de prompt ejecuta comandos en el host (CVE-2026-90970)"
date: 2026-10-02
date_raw: "2026-10-02 (GitLab advisory)"
date_precision: day

kind: vulnerability
type: [INFRA, SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **GitLab disclosed **CVE-2026-90970** (CVSS **9.9**, critical) on 2 October 2026: an authenticated user with access to the **Duo Agent Platform** can supply a crafted *flow configuration* that escapes the AI Gateway's Jinja2-style **prompt-template sandbox** and executes arbitrary commands on the AI Gateway host.** The AI Gateway is the middleware that connects a GitLab instance to its AI models; a successful escape means full compromise of a self-hosted gateway. The flaw is classified **CWE-1336** (improper neutralisation of special elements in a template engine). **Only self-hosted AI Gateways need to act** — GitLab had already patched its own hosted gateways, so GitLab.com / Dedicated / self-managed instances connected to a GitLab-hosted gateway are not affected. Fixed in AI Gateway **19.2.4, 19.3.2 and 19.4.1**. It was reported by HackerOne researcher **invisiblemeerkat**, and GitLab's advisory does **not** report any in-the-wild exploitation. Recorded `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false` — a CVSS-9+ flaw in agent infrastructure with no known exploitation.

summary_zh: |
  **GitLab 于 2026 年 10 月 2 日披露 **CVE-2026-90970**（CVSS **9.9**，严重）：一个对 **Duo Agent Platform** 有访问权的已认证用户，可提交构造的 *flow 配置*，逃出 AI Gateway 的 Jinja2 式**提示模板沙箱**，在 AI Gateway 主机上执行任意命令。** AI Gateway 是把 GitLab 实例连到其 AI 模型的中间件；一次成功逃逸意味着自托管网关被完全攻陷。该缺陷归类 **CWE-1336**（模板引擎中特殊元素处理不当）。**只有自托管的 AI Gateway 需要处置**——GitLab 已修好自家托管网关，故连接到 GitLab 托管网关的 GitLab.com／Dedicated／自管实例不受影响。已在 AI Gateway **19.2.4、19.3.2、19.4.1** 修复。由 HackerOne 研究者 **invisiblemeerkat** 报告，GitLab 通告**未**报告任何在野利用。记为 `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`——一个 CVSS 9+、位于 agent 基础设施、无已知利用的缺陷。

summary_ja: |
  **GitLabは2026年10月2日、**CVE-2026-90970**（CVSS **9.9**、クリティカル）を公表した。**Duo Agent Platform** にアクセスできる認証済みユーザーが、細工した *flow 構成* を与えることで、AIゲートウェイのJinja2系**プロンプトテンプレート・サンドボックス**を脱出し、AIゲートウェイのホスト上で任意コマンドを実行できる。** AIゲートウェイはGitLabインスタンスとAIモデルを繋ぐミドルウェアで、脱出成功は自己ホスト型ゲートウェイの完全な侵害を意味する。欠陥は **CWE-1336**（テンプレートエンジンにおける特殊要素の不適切な無害化）に分類。**対応が必要なのは自己ホスト型AIゲートウェイのみ**——GitLabは自社ホスト型ゲートウェイを既に修正済みで、GitLab.com／Dedicated／GitLabホスト型ゲートウェイに接続する自己管理インスタンスは影響を受けない。AIゲートウェイ **19.2.4、19.3.2、19.4.1** で修正。HackerOne研究者 **invisiblemeerkat** が報告し、GitLabの勧告は実環境での悪用を報告して**いない**。`vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`

summary_ko: |
  **GitLab은 2026년 10월 2일 **CVE-2026-90970**(CVSS **9.9**, 심각)을 공개했다: **Duo Agent Platform**에 접근 권한이 있는 인증 사용자가 조작된 *flow 구성*을 제공해 AI 게이트웨이의 Jinja2 계열 **프롬프트 템플릿 샌드박스**를 탈출하고 AI 게이트웨이 호스트에서 임의 명령을 실행할 수 있다.** AI 게이트웨이는 GitLab 인스턴스를 AI 모델에 연결하는 미들웨어로, 탈출 성공은 자체 호스팅 게이트웨이의 완전한 침해를 뜻한다. 결함은 **CWE-1336**(템플릿 엔진의 특수 요소 부적절 무력화)으로 분류된다. **조치가 필요한 것은 자체 호스팅 AI 게이트웨이뿐**——GitLab은 자사 호스팅 게이트웨이를 이미 패치했으므로 GitLab.com／Dedicated／GitLab 호스팅 게이트웨이에 연결된 자체 관리 인스턴스는 영향받지 않는다. AI 게이트웨이 **19.2.4, 19.3.2, 19.4.1**에서 수정. HackerOne 연구자 **invisiblemeerkat**가 보고했고 GitLab 권고는 실제 악용을 보고하지 **않았다**. `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`

summary_de: |
  **GitLab veröffentlichte am 2. Oktober 2026 **CVE-2026-90970** (CVSS **9.9**, kritisch): Ein authentifizierter Nutzer mit Zugriff auf die **Duo Agent Platform** kann eine präparierte *Flow-Konfiguration* liefern, die die Jinja2-artige **Prompt-Template-Sandbox** des AI Gateway verlässt und beliebige Befehle auf dem AI-Gateway-Host ausführt.** Das AI Gateway ist die Middleware, die eine GitLab-Instanz mit ihren KI-Modellen verbindet; ein erfolgreicher Ausbruch bedeutet die vollständige Kompromittierung eines selbst gehosteten Gateways. Der Fehler ist als **CWE-1336** eingestuft (unzureichende Neutralisierung von Sonderzeichen in einer Template-Engine). **Nur selbst gehostete AI Gateways müssen handeln** — GitLab hatte seine eigenen gehosteten Gateways bereits gepatcht, sodass GitLab.com / Dedicated / selbstverwaltete Instanzen, die mit einem GitLab-gehosteten Gateway verbunden sind, nicht betroffen sind. Behoben in AI Gateway **19.2.4, 19.3.2 und 19.4.1**. Gemeldet von HackerOne-Forscher **invisiblemeerkat**; GitLabs Advisory meldet **keine** Ausnutzung in freier Wildbahn. `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`

summary_fr: |
  **GitLab a divulgué **CVE-2026-90970** (CVSS **9.9**, critique) le 2 octobre 2026 : un utilisateur authentifié ayant accès à la **Duo Agent Platform** peut fournir une *configuration de flow* forgée qui s'échappe du **bac à sable de modèle de prompt** de type Jinja2 de l'AI Gateway et exécute des commandes arbitraires sur l'hôte de l'AI Gateway.** L'AI Gateway est l'intergiciel qui relie une instance GitLab à ses modèles d'IA ; une évasion réussie signifie la compromission totale d'une passerelle auto-hébergée. La faille est classée **CWE-1336** (neutralisation incorrecte d'éléments spéciaux dans un moteur de templates). **Seules les AI Gateways auto-hébergées doivent agir** — GitLab avait déjà corrigé ses propres passerelles hébergées, de sorte que GitLab.com / Dedicated / les instances autogérées connectées à une passerelle hébergée par GitLab ne sont pas affectées. Corrigé dans AI Gateway **19.2.4, 19.3.2 et 19.4.1**. Signalé par le chercheur HackerOne **invisiblemeerkat** ; l'avis de GitLab ne fait état d'**aucune** exploitation dans la nature. `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`

summary_es: |
  **GitLab divulgó **CVE-2026-90970** (CVSS **9.9**, crítica) el 2 de octubre de 2026: un usuario autenticado con acceso a la **Duo Agent Platform** puede suministrar una *configuración de flow* manipulada que escapa del **sandbox de plantillas de prompt** estilo Jinja2 del AI Gateway y ejecuta comandos arbitrarios en el host del AI Gateway.** El AI Gateway es el middleware que conecta una instancia de GitLab con sus modelos de IA; una fuga exitosa implica el compromiso total de una pasarela autoalojada. El fallo se clasifica como **CWE-1336** (neutralización incorrecta de elementos especiales en un motor de plantillas). **Solo las AI Gateways autoalojadas deben actuar** — GitLab ya había parcheado sus propias pasarelas alojadas, por lo que GitLab.com / Dedicated / instancias autogestionadas conectadas a una pasarela alojada por GitLab no se ven afectadas. Corregido en AI Gateway **19.2.4, 19.3.2 y 19.4.1**. Reportado por el investigador de HackerOne **invisiblemeerkat**; el aviso de GitLab no informa de **ninguna** explotación en la naturaleza. `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false`

sources:
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-90970
    label: NVD (CVE-2026-90970)
  - url: https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html
    label: The Hacker News
  - url: https://securityaffairs.com/200283/hacking/cve-2026-90970-critical-gitlab-ai-gateway-flaw-fixed.html
    label: Security Affairs
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.26"
---

# GitLab Duo AI Gateway: a prompt-template sandbox escape runs commands on the host (CVE-2026-90970)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-8F6A3C?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-3C6E8F?style=flat-square)

## Summary

**GitLab disclosed CVE-2026-90970 (CVSS 9.9, critical) on 2 October 2026: an authenticated user with access to the Duo Agent Platform can supply a crafted *flow configuration* that escapes the AI Gateway's Jinja2-style prompt-template sandbox and executes arbitrary commands on the AI Gateway host.** The AI Gateway is the middleware that connects a GitLab instance to its AI models; a successful escape means full compromise of a self-hosted gateway. The flaw is classified CWE-1336 (improper neutralisation of special elements in a template engine). **Only self-hosted AI Gateways need to act** — GitLab had already patched its own hosted gateways, so GitLab.com / Dedicated / self-managed instances connected to a GitLab-hosted gateway are not affected. Fixed in AI Gateway 19.2.4, 19.3.2 and 19.4.1. It was reported by HackerOne researcher invisiblemeerkat, and GitLab's advisory does **not** report any in-the-wild exploitation. Recorded `vulnerability` / `INFRA` + `SANDBOX` / `high` / `real_harm: false` — a CVSS-9+ flaw in agent infrastructure with no known exploitation.

## Attack chain

```mermaid
flowchart LR
    E["Authenticated user with Duo Agent<br/>Platform access"]:::entry
    S1["Supplies a crafted flow configuration<br/>with template-engine payload (Jinja2)"]:::step
    S2["Escapes the prompt-template sandbox<br/>(CWE-1336) on the AI Gateway"]:::step
    I["Arbitrary command execution on the<br/>self-hosted AI Gateway host"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The flaw.** GitLab's 2 October advisory describes an **improper-neutralisation** bug in how the Duo Agent Platform's AI Gateway builds prompts. The gateway uses a Jinja2-style template engine to insert user-controlled data into prompts; because the sandbox around that templating is insufficient, an authenticated user with Duo Agent Platform access can supply a **crafted flow configuration** whose payload escapes the template sandbox and runs arbitrary commands on the gateway host. GitLab rated it **CVSS 9.9** and NVD files it under **CWE-1336** (improper neutralisation of special elements used in a template engine). A successful attack yields full system compromise of the self-hosted AI Gateway.

**Who must act.** The AI Gateway is the service that connects a GitLab instance to AI models. GitLab says it had **already patched its own GitLab-hosted gateways**, so customers on GitLab.com, GitLab Dedicated, or a self-managed instance connected to a GitLab-hosted gateway do not need to take action. **Only organisations running their own (self-hosted) AI Gateway are affected**, and they should upgrade to **19.2.4, 19.3.2 or 19.4.1**. The issue was reported through HackerOne by a researcher using the handle **invisiblemeerkat**.

**How it is graded.** Recorded `vulnerability` — a disclosed flaw, not a used-in-anger incident. `INFRA` (the agent's runtime middleware, the AI Gateway) and `SANDBOX` (escape of the prompt-template execution boundary). `real_harm: false`: GitLab's advisory reports no known in-the-wild exploitation and the fix shipped with the disclosure. Severity `high` rather than `critical` despite the CVSS 9.9 — this archive's severity reflects **what has already happened**, and a severe flaw with no known exploitation is `high` here (the same basis as [EchoLeak](../2025-06/2025-06-11-echoleak.md), CVSS 9.3, no in-the-wild use). Confidence `A`: GitLab's own advisory and the NVD record, with independent reporting.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | NVD — CVE-2026-90970 | <https://nvd.nist.gov/vuln/detail/CVE-2026-90970> |
| 2 | The Hacker News | <https://thehackernews.com/2026/10/gitlab-patches-critical-self-hosted-ai.html> |
| 3 | Security Affairs | <https://securityaffairs.com/200283/hacking/cve-2026-90970-critical-gitlab-ai-gateway-flaw-fixed.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-02` (raw: 2026-10-02 GitLab advisory, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`SANDBOX`](../../taxonomy/types.md#sandbox) |
| Severity | **High** `high` |
| Confidence | **A** — GitLab advisory + NVD, with independent reporting |
| Real harm | No — fix shipped with disclosure; no known in-the-wild exploitation |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-02-gitlab-duo-ai-gateway-rce` |

<sub>**Why this classification:** A disclosed flaw in the GitLab Duo AI Gateway's prompt-templating (`INFRA` — agent runtime middleware; `SANDBOX` — escape of the template execution boundary). `vulnerability`, not an incident. `real_harm: false` because GitLab reports no known exploitation and patched it on disclosure. `high` not `critical`: severity here records what has happened, and a CVSS-9+ flaw with no in-the-wild use is `high` (as with EchoLeak). Dated to the GitLab advisory (2 October 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-08-26` [GitLab Duo's Claude agent can be steered into exfiltration](../2026-08/2026-08-26-gitlab-duo-claude-agent.md)<br>  <sub>An earlier GitLab Duo weakness — a different mechanism</sub>
- `2025-05-01` [GitLab Duo remote prompt injection](../2025-05/2025-05-01-gitlab-duo-yuan-cheng-ti.md)<br>  <sub>The first GitLab Duo issue in the archive</sub>
- `2026-08-06` [Langflow RCE added to CISA KEV](../2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Another agent-infrastructure RCE — that one exploited in the wild</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-02-gitlab-duo-ai-gateway-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
