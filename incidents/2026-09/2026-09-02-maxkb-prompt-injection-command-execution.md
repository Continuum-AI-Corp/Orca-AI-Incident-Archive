---
id: 2026-09-02-maxkb-prompt-injection-command-execution
title: "MaxKB CVE-2026-77521: a prompt-injectable agent runs shell commands on the host (CVSS 10.0)"
title_zh: "MaxKB CVE-2026-77521：可被提示注入的 agent 在主机上执行 shell 命令（CVSS 10.0）"
title_ja: "MaxKB CVE-2026-77521：プロンプトインジェクション可能なエージェントがホスト上でシェルコマンドを実行（CVSS 10.0）"
title_ko: "MaxKB CVE-2026-77521: 프롬프트 인젝션 가능한 에이전트가 호스트에서 셸 명령을 실행한다(CVSS 10.0)"
title_de: "MaxKB CVE-2026-77521: Ein prompt-injizierbarer Agent führt Shell-Befehle auf dem Host aus (CVSS 10.0)"
title_fr: "MaxKB CVE-2026-77521 : un agent vulnérable à l'injection de prompt exécute des commandes shell sur l'hôte (CVSS 10.0)"
title_es: "MaxKB CVE-2026-77521: un agente vulnerable a inyección de prompt ejecuta comandos shell en el host (CVSS 10.0)"
date: 2026-09-02
date_raw: "GHSA 2026-09-02 / NVD 2026-09-21"
date_precision: day

kind: vulnerability
type: [IPI, INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVE-2026-77521 (CVSS 3.1 **10.0**): any MaxKB assistant with a tool, MCP tool, skill or sub-application attached routes chat through a `deepagents` agent built on a host-shell backend (`SandboxShellBackend`) that auto-exposes an `execute` shell tool MaxKB never removes or gates.** The advisory's own words: *"Untrusted chat - or indirect prompt injection via content the assistant ingests (RAG / uploaded documents) - can therefore drive the model to run shell commands."* On a bare-metal deployment `MAXKB_SANDBOX` is off by default, so `execute` runs commands directly on the host as the application user (remote code execution); on the official image the container runs as root (no `USER` directive) and the sandbox wrapper is bypassable. GHSA-f36j-f34j-h3rx, weaknesses **CWE-78 / CWE-250 / CWE-749**, reported by **Lasso Security**; affected `<= 2.10.3-lts`, fixed in **v2.10.5-lts**. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false` — the archive's second MaxKB record from this September batch, alongside the tool-permission bypass (`2026-09-02`, CVE-2026-77516).

summary_zh: |
  **CVE-2026-77521（CVSS 3.1 **10.0**）：任何挂了工具、MCP 工具、技能或子应用的 MaxKB 助手，其对话都会走一个基于主机 shell 后端（`SandboxShellBackend`）构建的 `deepagents` agent，而该后端会自动暴露一个 `execute` shell 工具，MaxKB 既没移除也没设人工确认。** 公告原文：*「不可信的对话——或经助手摄取的内容（RAG／上传文档）进行的间接提示注入——因此可以驱动模型执行 shell 命令。」* 在裸机部署下 `MAXKB_SANDBOX` 默认关闭，于是 `execute` 直接以应用用户身份在主机上执行命令（远程代码执行）；官方镜像里容器以 root 运行（无 `USER` 指令），且沙箱包装器可被绕过。GHSA-f36j-f34j-h3rx，弱点 **CWE-78 / CWE-250 / CWE-749**，由 **Lasso Security** 报告；影响 `<= 2.10.3-lts`，**v2.10.5-lts** 修复。无在野利用记录。本条记为 `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`——是本次九月这批里第二条 MaxKB 记录，与逐工具授权绕过（`2026-09-02`，CVE-2026-77516）并列。

summary_ja: |
  **CVE-2026-77521（CVSS 3.1 **10.0**）：ツール、MCPツール、スキル、またはサブアプリを1つでも接続したMaxKBアシスタントは、ホストシェルのバックエンド（`SandboxShellBackend`）上に構築された`deepagents`エージェント経由でチャットを処理する。このバックエンドは`execute`シェルツールを自動的に公開し、MaxKBはそれを除去も制限もしない。** 勧告の原文：*「信頼できないチャット、あるいはアシスタントが取り込むコンテンツ（RAG／アップロード文書）を介した間接プロンプトインジェクションが、モデルにシェルコマンドを実行させ得る。」* ベアメタル配備では`MAXKB_SANDBOX`が既定で無効のため、`execute`はアプリユーザー権限でホスト上に直接コマンドを実行する（リモートコード実行）。公式イメージではコンテナがroot（`USER`指定なし）で動作し、サンドボックスのラッパーも回避可能。GHSA-f36j-f34j-h3rx、弱点 **CWE-78 / CWE-250 / CWE-749**、報告は **Lasso Security**。影響は`<= 2.10.3-lts`、**v2.10.5-lts**で修正。実環境での悪用は記録なし。`vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`

summary_ko: |
  **CVE-2026-77521(CVSS 3.1 **10.0**): 도구, MCP 도구, 스킬 또는 서브앱이 하나라도 연결된 MaxKB 어시스턴트는 호스트 셸 백엔드(`SandboxShellBackend`) 위에 만들어진 `deepagents` 에이전트를 통해 대화를 처리한다. 이 백엔드는 `execute` 셸 도구를 자동으로 노출하며, MaxKB는 이를 제거하지도 통제하지도 않는다.** 권고문 원문: *"신뢰할 수 없는 대화 — 또는 어시스턴트가 수집하는 콘텐츠(RAG／업로드 문서)를 통한 간접 프롬프트 인젝션 — 이 모델로 하여금 셸 명령을 실행하게 만들 수 있다."* 베어메탈 배포에서는 `MAXKB_SANDBOX`가 기본 비활성이라 `execute`가 애플리케이션 사용자 권한으로 호스트에서 직접 명령을 실행한다(원격 코드 실행). 공식 이미지에서는 컨테이너가 root(`USER` 지시어 없음)로 실행되고 샌드박스 래퍼도 우회 가능하다. GHSA-f36j-f34j-h3rx, 약점 **CWE-78 / CWE-250 / CWE-749**, 보고자 **Lasso Security**. 영향 `<= 2.10.3-lts`, **v2.10.5-lts**에서 수정. 실제 악용은 기록되지 않았다. `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`

summary_de: |
  **CVE-2026-77521 (CVSS 3.1 **10.0**): Jeder MaxKB-Assistent, an den ein Tool, ein MCP-Tool, ein Skill oder eine Sub-App angehängt ist, leitet den Chat über einen `deepagents`-Agenten, der auf einem Host-Shell-Backend (`SandboxShellBackend`) aufsetzt und automatisch ein `execute`-Shell-Tool bereitstellt, das MaxKB weder entfernt noch absichert.** Im Wortlaut des Advisorys: *"Untrusted chat - or indirect prompt injection via content the assistant ingests (RAG / uploaded documents) - can therefore drive the model to run shell commands."* Auf einer Bare-Metal-Installation ist `MAXKB_SANDBOX` standardmäßig aus, sodass `execute` Befehle direkt auf dem Host als Anwendungsbenutzer ausführt (Remote Code Execution); im offiziellen Image läuft der Container als root (keine `USER`-Direktive) und der Sandbox-Wrapper ist umgehbar. GHSA-f36j-f34j-h3rx, Schwächen **CWE-78 / CWE-250 / CWE-749**, gemeldet von **Lasso Security**; betroffen `<= 2.10.3-lts`, behoben in **v2.10.5-lts**. Keine Ausnutzung in freier Wildbahn bekannt. Verzeichnet als `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`

summary_fr: |
  **CVE-2026-77521 (CVSS 3.1 **10.0**) : tout assistant MaxKB auquel est rattaché un outil, un outil MCP, un skill ou une sous-application achemine la conversation via un agent `deepagents` construit sur un backend shell hôte (`SandboxShellBackend`) qui expose automatiquement un outil shell `execute` que MaxKB ne retire ni n'encadre.** Selon l'avis lui-même : *"Untrusted chat - or indirect prompt injection via content the assistant ingests (RAG / uploaded documents) - can therefore drive the model to run shell commands."* Sur un déploiement bare-metal, `MAXKB_SANDBOX` est désactivé par défaut, si bien qu'`execute` exécute des commandes directement sur l'hôte sous l'identité de l'utilisateur applicatif (exécution de code à distance) ; sur l'image officielle, le conteneur tourne en root (pas de directive `USER`) et l'enveloppe du bac à sable est contournable. GHSA-f36j-f34j-h3rx, faiblesses **CWE-78 / CWE-250 / CWE-749**, signalé par **Lasso Security** ; affecté `<= 2.10.3-lts`, corrigé dans **v2.10.5-lts**. Aucune exploitation constatée. Enregistré `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`

summary_es: |
  **CVE-2026-77521 (CVSS 3.1 **10.0**): cualquier asistente de MaxKB con una herramienta, herramienta MCP, skill o subaplicación adjunta enruta el chat a través de un agente `deepagents` construido sobre un backend de shell del host (`SandboxShellBackend`) que expone automáticamente una herramienta de shell `execute` que MaxKB no elimina ni restringe.** En palabras del propio aviso: *"Untrusted chat - or indirect prompt injection via content the assistant ingests (RAG / uploaded documents) - can therefore drive the model to run shell commands."* En un despliegue bare-metal `MAXKB_SANDBOX` está desactivado por defecto, así que `execute` ejecuta comandos directamente en el host como el usuario de la aplicación (ejecución remota de código); en la imagen oficial el contenedor corre como root (sin directiva `USER`) y el envoltorio del sandbox es evadible. GHSA-f36j-f34j-h3rx, debilidades **CWE-78 / CWE-250 / CWE-749**, reportado por **Lasso Security**; afectado `<= 2.10.3-lts`, corregido en **v2.10.5-lts**. No se registra explotación real. Registrado `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false`

sources:
  - url: https://github.com/1Panel-dev/MaxKB/security/advisories/GHSA-f36j-f34j-h3rx
    label: MaxKB security advisory (GHSA)
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-77521
    label: NVD
disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.21"
---

# MaxKB CVE-2026-77521: a prompt-injectable agent runs shell commands on the host (CVSS 10.0)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**CVE-2026-77521 (CVSS 3.1 **10.0**): any MaxKB assistant with a tool, MCP tool, skill or sub-application attached routes chat through a `deepagents` agent built on a host-shell backend (`SandboxShellBackend`) that auto-exposes an `execute` shell tool MaxKB never removes or gates.** The advisory's own words: *"Untrusted chat - or indirect prompt injection via content the assistant ingests (RAG / uploaded documents) - can therefore drive the model to run shell commands."* On a bare-metal deployment `MAXKB_SANDBOX` is off by default, so `execute` runs commands directly on the host as the application user (remote code execution); on the official image the container runs as root (no `USER` directive) and the sandbox wrapper is bypassable. GHSA-f36j-f34j-h3rx, weaknesses **CWE-78 / CWE-250 / CWE-749**, reported by **Lasso Security**; affected `<= 2.10.3-lts`, fixed in **v2.10.5-lts**. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `high` / `real_harm: false` — the archive's second MaxKB record from this September batch, alongside the tool-permission bypass (`2026-09-02`, CVE-2026-77516).

## Attack chain

```mermaid
flowchart LR
    E["Untrusted chat, or a poisoned RAG /<br/>uploaded document the assistant ingests"]:::entry
    S1["Assistant with any tool/MCP/skill attached<br/>routes to a deepagents host-shell agent"]:::step
    S2["The auto-exposed execute tool is neither<br/>removed nor gated by human confirmation"]:::step
    I["Model runs shell commands: host RCE as the<br/>app user (bare-metal) or as root (container)"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The advisory.** MaxKB's GitHub security advisory **GHSA-f36j-f34j-h3rx**, *"Prompt-injectable agent can lead to command execution,"* covers MaxKB `<= 2.10.3-lts` (the maintainers note the vulnerable path likely predates that and affects all versions that build chat agents on `deepagents` + `SandboxShellBackend`). The chain, in the advisory's terms: any assistant with a tool, MCP tool, skill or sub-application attached enters the agent path (`base_chat_node.py:409`); the agent is built with `SandboxShellBackend`, which *"auto-adds `execute` + fs tools"*; MaxKB does not remove it (`excluded_tools` is unused) and does not gate it (`interrupt_on` covers only `write_file` / `read_file` / `edit_file`, **never `execute`**). So untrusted chat, or **indirect prompt injection via ingested content (RAG or uploaded documents)**, can make the model run shell commands.

**Why the impact reaches the host.** Containment depends entirely on `MAXKB_SANDBOX`. On a source / bare-metal deployment it defaults **off**, so `execute` runs *"directly on the host as the application user (remote code execution)."* On the official image the sandbox is compiled but, as the advisory documents, the container has **no `USER` directive and runs as root (UID 0)**, and the sandbox wrapper is separately bypassable — so even the "contained" configuration crosses to host and, with `S:C` (scope changed), to other tenants and reachable internal services. CVSS 3.1 base **10.0** (`AV:N/AC:L/PR:N/UI:N/S:C/C:H/I:H/A:H`) for the public / embedded anonymous-assistant case; weaknesses **CWE-78** (OS command injection), **CWE-250** (execution with unnecessary privileges) and **CWE-749** (exposed dangerous method). Credited to **Lasso Security**. Fixed in **v2.10.5-lts**.

**Why the archive records it.** This is the sharp end of the same surface as the archive's other MaxKB entry from this batch: there, the agent dispatch path was a second door around per-tool authorization ([CVE-2026-77516](2026-09-02-maxkb-tool-permission-bypass.md)); here, the agent path exposes a shell that untrusted input can drive to code execution. It is the recurring agent-platform failure — a capability wired into the agent that the product never constrained — carried all the way to host RCE, and it is reachable by indirect prompt injection, not only by a logged-in user, which is why the record carries both `IPI` and `INFRA`.

**Grading.** `vulnerability` / `real_harm: false` — a maintainer-disclosed flaw, fixed in v2.10.5-lts, with no known exploitation in the wild. Severity **high** under the archive's ladder: a severe flaw at CVSS 9+ is graded `high` even without in-the-wild exploitation, and `critical` is reserved for confirmed real damage or a first-of-its-kind milestone with a real victim. Confidence **A**: the maintainer's advisory plus the NVD record.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | MaxKB security advisory GHSA-f36j-f34j-h3rx | <https://github.com/1Panel-dev/MaxKB/security/advisories/GHSA-f36j-f34j-h3rx> |
| 2 | NVD — CVE-2026-77521 | <https://nvd.nist.gov/vuln/detail/CVE-2026-77521> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-02` (raw: GHSA 2026-09-02 / NVD 2026-09-21, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **High** `high` |
| Confidence | **A** — maintainer advisory (GHSA) plus the NVD record |
| Real harm | No — fixed in v2.10.5-lts, no known exploitation |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-02-maxkb-prompt-injection-command-execution` |

<sub>**Why this classification:** the agent's own runtime exposes an ungated shell tool (`INFRA`) that external, ingested content can drive to execution (`IPI`, via RAG / uploaded documents). `vulnerability` + `real_harm: false` because it was disclosed and patched with no known exploitation. `high` rather than `critical` under the archive's ladder — a CVSS 9+ flaw with no confirmed damage; `critical` needs confirmed harm or a first-of-its-kind milestone with a real victim. Dated to the GitHub advisory (2 September 2026); NVD listed it on 21 September. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-09-02` [MaxKB: the agent dispatch path lets a user denied a tool still call it and read its credentials](2026-09-02-maxkb-tool-permission-bypass.md)<br>  <sub>The same September MaxKB advisory batch — the authorization side of the same agent path</sub>
- `2026-08-04` [Zammad: crafted text in an AI Agent field bypasses the sanitizer and runs commands](../2026-08/2026-08-04-zammad-ai-agent-template-rce.md)<br>  <sub>Another agent-platform flaw where the agent's own configuration reaches server command execution</sub>
- `2026-09-23` [IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools](2026-09-23-ibm-ftm-rag-poisoning.md)<br>  <sub>Also reached through ingested content the agent trusts</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-02-maxkb-prompt-injection-command-execution.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
