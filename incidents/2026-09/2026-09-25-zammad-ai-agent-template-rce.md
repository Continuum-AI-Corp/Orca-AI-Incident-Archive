---
id: 2026-09-25-zammad-ai-agent-template-rce
title: "Zammad: crafted text in an AI Agent field bypasses the sanitizer and runs commands on the server"
title_zh: "Zammad：写入 AI Agent 字段的特制文本绕过过滤器，并在服务器上执行命令"
title_ja: "Zammad：AI Agent フィールドに細工したテキストを入れるとサニタイザを迂回し、サーバー上でコマンドが実行される"
title_ko: "Zammad: AI Agent 필드에 조작된 텍스트를 넣으면 새니타이저를 우회해 서버에서 명령이 실행된다"
title_de: "Zammad: Präparierter Text in einem AI-Agent-Feld umgeht den Filter und führt Befehle auf dem Server aus"
title_fr: "Zammad : un texte façonné dans un champ d'AI Agent contourne l'assainissement et exécute des commandes sur le serveur"
title_es: "Zammad: un texto manipulado en un campo de AI Agent burla el saneamiento y ejecuta comandos en el servidor"
date: 2026-09-25
date_raw: "GHSA 2026-08-04 / NVD 2026-09-25"
date_precision: day

kind: vulnerability
type: [IPI, INFRA]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **CVE-2026-84462: in Zammad before 7.1.2, *"a security filter that protects Zammad's AI Agent configuration can be bypassed by entering specially crafted text into one of an AI Agent's fields,"* letting an administrator who can create or edit AI Agents *"run arbitrary commands on the server that hosts Zammad."*** The GitHub advisory calls it *"AI Agent template sanitizer bypass leads to remote code execution"*; NVD adds that *"no interaction from other users is needed; the malicious code runs automatically the next time the affected AI Agent processes a ticket."* CVSS 4.0 **8.6** (`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), weaknesses CWE-20 / CWE-94 / CWE-1336; fixed in **7.1.2**. The pattern matters more than the score: the **agent definition itself** — the instructions, templates and filters a helpdesk admin writes for an AI Agent — is a remote code execution surface. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_zh: |
  **CVE-2026-84462：在 7.1.2 之前的 Zammad 中，*「保护 Zammad AI Agent 配置的安全过滤器可被绕过——只要在某个 AI Agent 的字段里输入特制文本，」*使有权创建或编辑 AI Agent 的管理员*「在承载 Zammad 的服务器上执行任意命令。」*** GitHub 公告把它命名为*「AI Agent 模板 sanitizer 绕过导致远程代码执行」*；NVD 补充说*「无需其他用户交互；恶意代码会在受影响的 AI Agent 下次处理工单时自动运行。」* CVSS 4.0 **8.6**（`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`），弱点 CWE-20 / CWE-94 / CWE-1336；已在 **7.1.2** 修复。模式比分数更重要：**agent 定义本身**——客服管理员为 AI Agent 编写的指令、模板与过滤器——就是一个远程代码执行攻击面。无在野利用记录。本条记为 `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_ja: |
  **CVE-2026-84462：7.1.2 より前の Zammad では、*「Zammad の AI Agent 設定を保護するセキュリティフィルタは、AI Agent のいずれかのフィールドに細工したテキストを入力することで迂回できる」*ため、AI Agent を作成・編集できる管理者が*「Zammad をホストするサーバー上で任意のコマンドを実行できる」。*** GitHub のアドバイザリはこれを *"AI Agent template sanitizer bypass leads to remote code execution"* と名付ける。NVD は *「他のユーザーの操作は不要で、悪意あるコードは影響を受けた AI Agent が次にチケットを処理したときに自動的に実行される」*と補足する。CVSS 4.0 **8.6**（`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`）、弱点 CWE-20 / CWE-94 / CWE-1336、**7.1.2** で修正。重要なのはスコアよりパターンだ。**エージェント定義そのもの**——管理者が AI Agent のために書く指示・テンプレート・フィルタ——がリモートコード実行の攻撃面になっている。実環境での悪用は記録されていない。`vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_ko: |
  **CVE-2026-84462: 7.1.2 이전 Zammad에서 *"Zammad AI Agent 구성을 보호하는 보안 필터는 AI Agent 필드 중 하나에 특수하게 조작된 텍스트를 입력해 우회할 수 있다"*. 따라서 AI Agent를 생성·편집할 수 있는 관리자가 *"Zammad를 호스팅하는 서버에서 임의 명령을 실행할 수 있다."*** GitHub 권고문은 이를 *"AI Agent template sanitizer bypass leads to remote code execution"*으로 명명한다. NVD는 *"다른 사용자의 상호작용은 필요 없고, 악성 코드는 해당 AI Agent가 다음에 티켓을 처리할 때 자동으로 실행된다"*고 덧붙인다. CVSS 4.0 **8.6**(`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), 약점 CWE-20 / CWE-94 / CWE-1336, **7.1.2**에서 수정. 점수보다 패턴이 중요하다. **에이전트 정의 자체**——헬프데스크 관리자가 AI Agent용으로 작성하는 지시·템플릿·필터——가 원격 코드 실행 공격면이다. 실제 악용은 기록되지 않았다. `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_de: |
  **CVE-2026-84462: In Zammad vor 7.1.2 *„kann ein Sicherheitsfilter, der die AI-Agent-Konfiguration von Zammad schützt, durch die Eingabe speziell präparierten Textes in eines der AI-Agent-Felder umgangen werden"*, sodass ein Administrator, der AI-Agents erstellen oder bearbeiten darf, *„beliebige Befehle auf dem Server ausführen kann, der Zammad hostet".*** Das GitHub-Advisory nennt es *„AI Agent template sanitizer bypass leads to remote code execution"*; NVD ergänzt: *„Es ist keine Interaktion anderer Benutzer erforderlich; der bösartige Code läuft automatisch, wenn der betroffene AI-Agent das nächste Mal ein Ticket bearbeitet."* CVSS 4.0 **8.6** (`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), Schwächen CWE-20 / CWE-94 / CWE-1336, behoben in **7.1.2**. Das Muster wiegt mehr als die Punktzahl: Die **Agent-Definition selbst** — Anweisungen, Vorlagen und Filter, die ein Helpdesk-Admin für einen KI-Agenten schreibt — ist eine RCE-Angriffsfläche. Keine Ausnutzung bekannt. Verzeichnet als `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_fr: |
  **CVE-2026-84462 : dans Zammad avant 7.1.2, *« un filtre de sécurité qui protège la configuration AI Agent de Zammad peut être contourné en saisissant un texte spécialement conçu dans l'un des champs d'un AI Agent »*, permettant à un administrateur habilité à créer ou modifier des AI Agents *« d'exécuter des commandes arbitraires sur le serveur qui héberge Zammad ».*** L'avis GitHub l'intitule *« AI Agent template sanitizer bypass leads to remote code execution »* ; le NVD ajoute qu'*« aucune interaction d'un autre utilisateur n'est nécessaire ; le code malveillant s'exécute automatiquement au prochain traitement d'un ticket par l'AI Agent concerné. »* CVSS 4.0 **8.6** (`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), faiblesses CWE-20 / CWE-94 / CWE-1336, corrigé en **7.1.2**. Le motif compte plus que le score : la **définition de l'agent elle-même** — instructions, modèles et filtres écrits par un administrateur — est une surface d'exécution de code à distance. Aucune exploitation constatée. Enregistré `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

summary_es: |
  **CVE-2026-84462: en Zammad anterior a 7.1.2, *«un filtro de seguridad que protege la configuración de AI Agent de Zammad puede evadirse introduciendo texto especialmente manipulado en uno de los campos de un AI Agent»*, lo que permite a un administrador con permiso para crear o editar AI Agents *«ejecutar comandos arbitrarios en el servidor que aloja Zammad»*.** El aviso de GitHub lo titula *«AI Agent template sanitizer bypass leads to remote code execution»*; el NVD añade que *«no se necesita interacción de otros usuarios; el código malicioso se ejecuta automáticamente la próxima vez que el AI Agent afectado procese un ticket»*. CVSS 4.0 **8.6** (`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), debilidades CWE-20 / CWE-94 / CWE-1336, corregido en **7.1.2**. El patrón importa más que la puntuación: la **definición del agente en sí** — instrucciones, plantillas y filtros que escribe un administrador — es una superficie de ejecución remota de código. No se registra explotación real. Registrado `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`

sources:
  - url: https://github.com/zammad/zammad/security/advisories/GHSA-gp3x-9xm8-rcj6
    label: Zammad security advisory (GHSA)
  - url: https://nvd.nist.gov/vuln/detail/CVE-2026-84462
    label: NVD

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.20"
---

# Zammad: crafted text in an AI Agent field bypasses the sanitizer and runs commands on the server

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**CVE-2026-84462: in Zammad before 7.1.2, *"a security filter that protects Zammad's AI Agent configuration can be bypassed by entering specially crafted text into one of an AI Agent's fields,"* letting an administrator who can create or edit AI Agents *"run arbitrary commands on the server that hosts Zammad."*** The GitHub advisory calls it *"AI Agent template sanitizer bypass leads to remote code execution"*; NVD adds that *"no interaction from other users is needed; the malicious code runs automatically the next time the affected AI Agent processes a ticket."* CVSS 4.0 **8.6** (`AV:N/AC:L/AT:N/PR:H/UI:N/VC:H/VI:H/VA:H`), weaknesses CWE-20 / CWE-94 / CWE-1336; fixed in **7.1.2**. The pattern matters more than the score: the **agent definition itself** — the instructions, templates and filters a helpdesk admin writes for an AI Agent — is a remote code execution surface. No exploitation in the wild is recorded. Recorded `vulnerability` / `IPI` + `INFRA` / `medium` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["Administrator writes crafted text<br/>into an AI Agent field"]:::entry
    S1["The sanitizer meant to protect the<br/>AI Agent configuration is bypassed"]:::step
    S2["The payload persists in the<br/>agent definition"]:::step
    I["Next ticket processed by that agent:<br/>arbitrary commands run on the Zammad server"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The advisory.** Zammad's GitHub security advisory **GHSA-gp3x-9xm8-rcj6**, *"AI Agent template sanitizer bypass leads to remote code execution,"* covers Zammad before 7.1.2. NVD's synchronised text: *"a security filter that protects Zammad's AI Agent configuration can be bypassed by entering specially crafted text into one of an AI Agent's fields. An administrator with permission to create or edit AI Agents could exploit this to run arbitrary commands on the server that hosts Zammad, potentially reading, modifying, or destroying all data stored on that server. No interaction from other users is needed; the malicious code runs automatically the next time the affected AI Agent processes a ticket. This issue is fixed in version 7.1.2."* CVSS 4.0 base **8.6** with `PR:H` (high privileges required) and full confidentiality/integrity/availability impact; weaknesses **CWE-20** (improper input validation), **CWE-94** (code injection) and **CWE-1336** (template engine injection).

**On the dates.** The GitHub advisory was published on **4 August 2026**; NVD synchronised it on **25 September 2026**, which is how this sweep picked it up. The record is dated to the NVD publication, following the archive's practice of dating CVE entries to the point they enter the CVE record.

**Why the archive records it.** Two CVEs published the same week (25 September) target the same new surface from opposite ends — CVE-2026-84462 in Zammad's helpdesk AI Agent and CVE-2026-94111 in a browser agent's daemon. In both, the thing being attacked is not the model but the **plumbing that defines what the agent is**: its fields, templates, filters and transports. Zammad is the sharper case, because the store is persistent and self-triggering: the payload sits in the agent definition and fires on the next ticket, with no user interaction — an agent-configuration injection that behaves like stored XSS but lands as server command execution.

**Grading.** `vulnerability` / `real_harm: false` — disclosed by the maintainer, fixed in 7.1.2, no known exploitation. Severity `medium` under the archive's ladder despite CVSS 8.6: the flaw requires an administrator who can already create or edit AI Agents, and the archive reserves `high` for CVSS 9+ or confirmed damage. Confidence **A**: the maintainer's advisory plus the NVD record.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Zammad security advisory GHSA-gp3x-9xm8-rcj6 | <https://github.com/zammad/zammad/security/advisories/GHSA-gp3x-9xm8-rcj6> |
| 2 | NVD — CVE-2026-84462 | <https://nvd.nist.gov/vuln/detail/CVE-2026-84462> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-25` (raw: GHSA 2026-08-04 / NVD 2026-09-25, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **Medium** `medium` |
| Confidence | **A** — maintainer advisory (GHSA) plus the NVD record |
| Real harm | No — fixed in 7.1.2, no known exploitation |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-25-zammad-ai-agent-template-rce` |

<sub>**Why this classification:** what is attacked is the agent's own configuration store (`INFRA`) and the payload reaches execution as content the agent processes (`IPI`, template-injection class). `real_harm: false` because it was disclosed and patched with no known exploitation. `medium` rather than `high` under the archive's ladder — CVSS 8.6 is below the 9+ band and the flaw needs an administrator who can already author agents; `high` would also require confirmed damage. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-09-20` [Tencent BrowserSkill: any 32-character extension origin can pose as the browser client](2026-09-20-tencent-browserskill-origin-bypass.md)<br>  <sub>The same week, the same idea one layer down — the agent's transport, not its definition</sub>
- `2026-09-23` [IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools](2026-09-23-ibm-ftm-rag-poisoning.md)<br>  <sub>Injection into what the agent trusts, reaching its tools</sub>
- `2026-09-14` [Bifrost AI gateway: one unauthenticated MCP registration runs commands as the gateway user](2026-09-14-bifrost-ai-gateway-cve-2026-90898.md)<br>  <sub>The September pattern: agent plumbing as an RCE surface</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-25-zammad-ai-agent-template-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
