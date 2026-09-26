---
id: 2026-09-21-maxkb-tool-permission-bypass
title: "MaxKB: the agent dispatch path lets a user denied a tool still call it and read its credentials"
title_zh: "MaxKB：agent 派发路径让被拒绝使用某工具的用户仍能调用它并读取其凭据"
title_ja: "MaxKB：エージェントのディスパッチ経路により、ツールを拒否されたユーザーでも実行でき、その認証情報を読めてしまう"
title_ko: "MaxKB: 에이전트 디스패치 경로 때문에 도구 사용이 거부된 사용자도 호출하고 자격증명을 읽을 수 있다"
title_de: "MaxKB: Der Agent-Dispatch-Pfad erlaubt einem abgelehnten Nutzer das Tool dennoch aufzurufen und seine Zugangsdaten zu lesen"
title_fr: "MaxKB : le chemin de distribution de l'agent permet à un utilisateur refusé d'appeler l'outil et d'en lire les identifiants"
title_es: "MaxKB: la ruta de despacho del agente permite que un usuario denegado llame a la herramienta y lea sus credenciales"
date: 2026-09-21
date_raw: "2026-09-21 (NVD, GHSA)"
date_precision: day

kind: vulnerability
type: [INFRA, CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVE-2026-77516: in MaxKB 2.0.0 through 2.9.2, *"a lowest-role workspace member denied access to a tool by WorkspaceUserResourcePermission can still bind its identifier through `tool_ids`, `skill_tool_ids`, or `mcp_tool_ids` and execute it through the agent or workflow dispatch path"* — and because *"tool execution decrypts server-side `init_params`, allowing the caller to receive credentials carried by the denied tool,"* the bypass returns keys, not just a result.** The advisory, titled *"Missing per-tool authorization in the agent and workflow tool-dispatch path,"* names CWE-862 (missing authorization) and CWE-639 (authorization bypass through user-controlled key); CVSS 3.1 **5.4**; *"No fixed version is available as of this review."* The structure is the point: the per-tool grant is enforced on the dedicated tool routes, but the **agent dispatch path is a second door to the same capability** that does not re-check it. Recorded `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_zh: |
  **CVE-2026-77516：在 MaxKB 2.0.0 至 2.9.2 中，*「被 WorkspaceUserResourcePermission 拒绝访问某工具的最低权限工作区成员，仍可通过 `tool_ids`、`skill_tool_ids` 或 `mcp_tool_ids` 绑定其标识符，并经 agent 或工作流派发路径执行它」*——而且由于*「工具执行会解密服务端的 `init_params`，使调用方能拿到被拒绝工具所携带的凭据，」*这次绕过返回的不仅是结果，还有密钥。** 该公告题为*「agent 与工作流工具派发路径中缺少逐工具授权」*，列出 CWE-862（缺少授权）与 CWE-639（通过用户可控键绕过授权）；CVSS 3.1 **5.4**；*「截至本次评审无可用修复版本。」* 关键在结构：逐工具授权在专用工具路由上执行，但 **agent 派发路径是通向同一能力的第二道门**，而它并不复查该授权。本条记为 `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_ja: |
  **CVE-2026-77516：MaxKB 2.0.0〜2.9.2 では、*「WorkspaceUserResourcePermission によってツールへのアクセスを拒否された最低権限のワークスペースメンバーが、`tool_ids`、`skill_tool_ids`、`mcp_tool_ids` を通じてその識別子を束縛し、エージェントまたはワークフローのディスパッチ経路から実行できてしまう」*——さらに*「ツール実行はサーバー側の `init_params` を復号するため、呼び出し側は拒否されたツールが保持する認証情報を受け取れてしまう。」*つまりこの迂回は結果だけでなく鍵も返す。公告は *"Missing per-tool authorization in the agent and workflow tool-dispatch path"* と題し、CWE-862（認可の欠如）と CWE-639（ユーザー制御キーによる認可迂回）を挙げる。CVSS 3.1 **5.4**、*「本レビュー時点で修正版は未提供。」* 重要なのは構造だ。ツールごとの許可は専用ツール経路で強制されるが、**エージェントのディスパッチ経路は同じ能力への第二の扉**であり、そこでは再チェックされない。`vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_ko: |
  **CVE-2026-77516: MaxKB 2.0.0~2.9.2에서 *"WorkspaceUserResourcePermission으로 도구 접근이 거부된 최하위 권한 워크스페이스 멤버도 `tool_ids`, `skill_tool_ids`, `mcp_tool_ids`로 식별자를 바인딩해 에이전트·워크플로 디스패치 경로로 실행할 수 있다"* — 게다가 *"도구 실행은 서버 측 `init_params`를 복호화하므로 호출자는 거부된 도구가 지닌 자격증명을 받게 된다."* 즉 이 우회는 결과뿐 아니라 키도 돌려준다. 권고문 제목은 *"Missing per-tool authorization in the agent and workflow tool-dispatch path"*, CWE-862(인가 누락)와 CWE-639(사용자 제어 키를 통한 인가 우회)를 명시. CVSS 3.1 **5.4**, *"본 검토 시점에 수정 버전 없음."* 핵심은 구조다. 도구별 권한은 전용 도구 경로에서만 강제되고, **에이전트 디스패치 경로는 같은 기능으로 향하는 두 번째 문**인데 거기선 재검사하지 않는다. `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_de: |
  **CVE-2026-77516: In MaxKB 2.0.0 bis 2.9.2 *„kann ein Arbeitsbereichsmitglied mit der niedrigsten Rolle, dem der Zugriff auf ein Tool durch WorkspaceUserResourcePermission verweigert wurde, dessen Kennung dennoch über `tool_ids`, `skill_tool_ids` oder `mcp_tool_ids` binden und über den Agenten- oder Workflow-Dispatch-Pfad ausführen"* — und weil *„die Tool-Ausführung serverseitige `init_params` entschlüsselt, kann der Aufrufer die Zugangsdaten des verweigerten Tools erhalten."*** Das Advisory heißt *„Missing per-tool authorization in the agent and workflow tool-dispatch path"* und nennt CWE-862 (fehlende Autorisierung) sowie CWE-639 (Autorisierungs-Umgehung über einen benutzerkontrollierten Schlüssel); CVSS 3.1 **5.4**; *„Zum Zeitpunkt dieser Prüfung ist keine behobene Version verfügbar."* Entscheidend ist die Struktur: Die Tool-spezifische Freigabe wird auf den dedizierten Tool-Routen geprüft, aber der **Agent-Dispatch-Pfad ist eine zweite Tür zur selben Fähigkeit**, die sie nicht erneut prüft. Verzeichnet als `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_fr: |
  **CVE-2026-77516 : dans MaxKB 2.0.0 à 2.9.2, *« un membre d'espace de travail au rôle le plus bas, auquel l'accès à un outil est refusé par WorkspaceUserResourcePermission, peut tout de même lier son identifiant via `tool_ids`, `skill_tool_ids` ou `mcp_tool_ids` et l'exécuter par le chemin de distribution de l'agent ou du workflow »* — et comme *« l'exécution de l'outil déchiffre les `init_params` côté serveur, l'appelant reçoit les identifiants portés par l'outil refusé. »*** L'avis s'intitule *« Missing per-tool authorization in the agent and workflow tool-dispatch path »* et cite CWE-862 (autorisation manquante) et CWE-639 (contournement d'autorisation via une clé contrôlée par l'utilisateur) ; CVSS 3.1 **5.4** ; *« aucune version corrigée n'est disponible à la date de cet examen. »* La structure importe : l'autorisation par outil est appliquée sur les routes d'outils dédiées, mais le **chemin de distribution de l'agent est une seconde porte vers la même capacité**, sans nouvelle vérification. Enregistré `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

summary_es: |
  **CVE-2026-77516: en MaxKB 2.0.0 a 2.9.2, *«un miembro del espacio de trabajo con el rol más bajo al que WorkspaceUserResourcePermission deniega el acceso a una herramienta puede aun así vincular su identificador mediante `tool_ids`, `skill_tool_ids` o `mcp_tool_ids` y ejecutarla por la ruta de despacho del agente o del flujo de trabajo»* — y como *«la ejecución de la herramienta descifra los `init_params` del servidor, el llamante recibe las credenciales que porta la herramienta denegada».*** El aviso se titula *«Missing per-tool authorization in the agent and workflow tool-dispatch path»* y señala CWE-862 (autorización ausente) y CWE-639 (omisión de autorización mediante clave controlada por el usuario); CVSS 3.1 **5.4**; *«no hay versión corregida disponible al momento de esta revisión»*. Lo relevante es la estructura: la autorización por herramienta se aplica en las rutas dedicadas, pero la **ruta de despacho del agente es una segunda puerta a la misma capacidad** que no la vuelve a comprobar. Registrado `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`

sources:
  - url: https://github.com/1Panel-dev/MaxKB/security/advisories/GHSA-383v-fx78-pphm
    label: MaxKB security advisory (GHSA)
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-77516
    label: NVD

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# MaxKB: the agent dispatch path lets a user denied a tool still call it and read its credentials

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**CVE-2026-77516: in MaxKB 2.0.0 through 2.9.2, *"a lowest-role workspace member denied access to a tool by WorkspaceUserResourcePermission can still bind its identifier through `tool_ids`, `skill_tool_ids`, or `mcp_tool_ids` and execute it through the agent or workflow dispatch path"* — and because *"tool execution decrypts server-side `init_params`, allowing the caller to receive credentials carried by the denied tool,"* the bypass returns keys, not just a result.** The advisory, titled *"Missing per-tool authorization in the agent and workflow tool-dispatch path,"* names CWE-862 (missing authorization) and CWE-639 (authorization bypass through user-controlled key); CVSS 3.1 **5.4**; *"No fixed version is available as of this review."* The structure is the point: the per-tool grant is enforced on the dedicated tool routes, but the **agent dispatch path is a second door to the same capability** that does not re-check it. Recorded `vulnerability` / `INFRA` + `CRED` / `medium` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["Lowest-role workspace member<br/>denied a specific tool"]:::entry
    S1["Submits the tool id via tool_ids /<br/>skill_tool_ids / mcp_tool_ids"]:::step
    S2["Agent or workflow dispatch path<br/>does not reapply the per-tool grant"]:::step
    I["Denied tool executes and its<br/>decrypted init_params credentials are returned"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The advisory.** MaxKB's GitHub security advisory **GHSA-383v-fx78-pphm**, *"Missing per-tool authorization in the agent and workflow tool-dispatch path (CWE-862 / CWE-639),"* covers versions 2.0.0 through 2.9.2 of the open-source enterprise AI assistant. NVD's synchronised description: *"a lowest-role workspace member denied access to a tool by WorkspaceUserResourcePermission can still bind its identifier through tool_ids, skill_tool_ids, or mcp_tool_ids and execute it through the agent or workflow dispatch path. The dispatch path does not reapply the per-tool grant enforced by dedicated tool routes, and tool execution decrypts server-side init_params, allowing the caller to receive credentials carried by the denied tool."* CVSS 3.1 base **5.4**; *"No fixed version is available as of this review."*

**Why the archive records it.** This is the authorisation version of a pattern the archive keeps meeting: **the agent is a second path to the same capability**. The permission model was written for the route a human calls directly; the agent or workflow dispatch path reaches the same tool through a different door, and the per-tool grant is not reapplied there. Because the tool's `init_params` are decrypted server-side at execution time, the failure does not stop at "the agent did something it should not" — it hands back the credentials the tool was configured with, which is why this is also a `CRED` record. It sits close to Noma's workflow-identity finding (09-09), where the misalignment was also between an authorisation model and the path actually taken.

**Grading.** `vulnerability` / `real_harm: false` — a published advisory with no known exploitation; `medium` under the archive's ladder (CVSS 5.4, a controlled authorisation bypass with no confirmed damage). Confidence **A**: the maintainer's advisory plus the NVD record. Note that no fixed version existed at the time of the advisory.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | MaxKB security advisory GHSA-383v-fx78-pphm | <https://github.com/1Panel-dev/MaxKB/security/advisories/GHSA-383v-fx78-pphm> |
| 2 | NVD — CVE-2026-77516 | <https://nvd.nist.gov/vuln/detail/CVE-2026-77516> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-21` (raw: NVD / GHSA 2026-09-21, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **Medium** `medium` |
| Confidence | **A** — maintainer advisory (GHSA) plus the NVD record |
| Real harm | No — no known exploitation |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-21-maxkb-tool-permission-bypass` |

<sub>**Why this classification:** the failure is in the agent platform's own dispatch path and permission enforcement (`INFRA`), and what it yields is the credentials the denied tool carries (`CRED`). It is not `IPI` — no external content steers the agent; the request itself names the tool. `medium` under the archive's ladder: CVSS 5.4, an authorisation bypass with no confirmed damage; `high` would need CVSS 9+ or confirmed harm. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-09-09` [Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access](2026-09-09-noma-workflow-identity-hijacking.md)<br>  <sub>The same misalignment: an authorisation model that does not match the path taken</sub>
- `2026-09-25` [Zammad: crafted text in an AI Agent field bypasses the sanitizer](2026-09-25-zammad-ai-agent-template-rce.md)<br>  <sub>The other September agent-platform flaw where the agent definition is the surface</sub>
- `2026-09-23` [IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools](2026-09-23-ibm-ftm-rag-poisoning.md)<br>  <sub>Tool invocation reached by a path the permission model did not anticipate</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-21-maxkb-tool-permission-bypass.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
