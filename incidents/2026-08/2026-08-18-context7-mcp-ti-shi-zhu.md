---
id: 2026-08-18-context7-mcp-ti-shi-zhu
title: "Context7 MCP prompt injection (CVE-2026-75130)"
title_zh: "Context7 MCP 提示注入（CVE-2026-75130）"
title_ja: "Context7 MCPのプロンプトインジェクション（CVE-2026-75130）"
title_ko: "Context7 MCP 프롬프트 인젝션 (CVE-2026-75130)"
title_de: "Context7 MCP Prompt-Injection (CVE-2026-75130)"
title_fr: "Injection de prompt dans Context7 MCP (CVE-2026-75130)"
title_es: "Inyección de prompt en Context7 MCP (CVE-2026-75130)"
date: 2026-08-18
date_precision: day
date_raw: "2026-08-18"

kind: research
type: [MCP, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Context7 ≤ 2.1.2: the **Custom AI Instructions feature** served over MCP does not sanitise content; once an attacker poisons the custom instructions, **a single routine library-docs lookup by the agent** exfiltrates credentials from `.env` to the attacker's service and runs destructive file deletion on the victim's machine. CVSS 3.1 **9.0** (CVSS 4.0 6.4). ⚠️ **As of the disclosure date there is no public fix for that version range**


summary_zh: |
  Context7 ≤ 2.1.2：经 MCP 提供的 **Custom AI Instructions 功能**未净化内容，攻击者投毒自定义指令后，**agent 只要做一次例行的库文档查询**，就会把 `.env` 里的凭据外带到攻击者服务，并在受害者机器上执行破坏性文件删除。CVSS 3.1 **9.0**（CVSS 4.0 为 6.4）。⚠️ **截至披露日该版本区间无公开修复**

summary_ja: |
  Context7 ≤ 2.1.2：MCP経由で提供される**Custom AI Instructions機能**がコンテンツをサニタイズしない。攻撃者がカスタム指示を汚染すると、**エージェントによる通常のライブラリドキュメント検索1回**で`.env`の認証情報が攻撃者のサービスへ外部送信され、被害者のマシンで破壊的なファイル削除が実行される。CVSS 3.1 **9.0**（CVSS 4.0は6.4）。⚠️ **公表日時点でそのバージョン範囲に対する公開修正はない**

summary_ko: |
  Context7 ≤ 2.1.2: MCP로 제공되는 **Custom AI Instructions 기능**이 콘텐츠를 정제하지 않는다. 공격자가 사용자 지정 지시를 오염시키면 **에이전트의 평범한 라이브러리 문서 조회 한 번**으로 `.env`의 자격 증명이 공격자 서비스로 유출되고 피해자 머신에서 파괴적 파일 삭제가 실행된다. CVSS 3.1 **9.0**(CVSS 4.0 6.4). ⚠️ **공개 시점 기준 해당 버전 범위에 대한 공개 수정이 없다**

summary_de: |
  Context7 ≤ 2.1.2: Die über MCP bereitgestellte **Funktion für benutzerdefinierte KI-Anweisungen** bereinigt Inhalte nicht; sobald ein Angreifer die benutzerdefinierten Anweisungen vergiftet, **genügt ein einziger routinemäßiger Bibliotheksdokumentations-Abruf des Agenten**, um Zugangsdaten aus `.env` zum Dienst des Angreifers zu exfiltrieren und auf dem Rechner des Opfers destruktive Dateilöschungen auszuführen. CVSS 3.1 **9.0** (CVSS 4.0 6.4). ⚠️ **Zum Zeitpunkt der Offenlegung gibt es für diesen Versionsbereich keinen öffentlichen Fix**

summary_fr: |
  Context7 ≤ 2.1.2 : la **fonctionnalité Custom AI Instructions** servie via MCP ne sanitise pas le contenu ; une fois les instructions personnalisées empoisonnées par un attaquant, **une simple consultation de documentation de bibliothèque par l'agent** exfiltre les identifiants de `.env` vers le service de l'attaquant et lance une suppression destructrice de fichiers sur la machine de la victime. CVSS 3.1 **9.0** (CVSS 4.0 6.4). ⚠️ **À la date de divulgation, aucun correctif public n'existe pour cette plage de versions**

summary_es: |
  Context7 ≤ 2.1.2: la **función Custom AI Instructions** servida por MCP no sanitiza el contenido; una vez que un atacante envenena las instrucciones personalizadas, **una sola consulta rutinaria de documentación de una biblioteca por parte del agente** exfiltra credenciales de `.env` al servicio del atacante y ejecuta un borrado destructivo de archivos en la máquina de la víctima. CVSS 3.1 **9.0** (CVSS 4.0 6.4). ⚠️ **En la fecha de divulgación no hay corrección pública para ese rango de versiones**

sources:
  - url: https://app.opencve.io/cve/CVE-2026-75130
    label: OpenCVE
  - url: https://www.digitalapplied.com/blog/context7-mcp-prompt-injection-cve-2026-75130
    label: Analysis

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Context7 MCP prompt injection (CVE-2026-75130)

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: MCP](https://img.shields.io/badge/type-MCP-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Context7 ≤ 2.1.2: the **Custom AI Instructions feature** served over MCP does not sanitise content; once an attacker poisons the custom instructions, **a single routine library-docs lookup by the agent** exfiltrates credentials from `.env` to the attacker's service and runs destructive file deletion on the victim's machine. CVSS 3.1 **9.0** (CVSS 4.0 6.4). ⚠️ **As of the disclosure date there is no public fix for that version range**

## Attack chain

```mermaid
flowchart LR
    E["Malicious MCP server or tool description"]:::entry
    S0["The agent toolchain loads and trusts it"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credential abuse<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenCVE | <https://app.opencve.io/cve/CVE-2026-75130> |
| 2 | Analysis | <https://www.digitalapplied.com/blog/context7-mcp-prompt-injection-cve-2026-75130> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-18` (raw: 2026-08-18, precision `day`) |
| Kind | Research demo `research` |
| Type | [`MCP`](../../taxonomy/types.md#mcp) MCP & tool-chain · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-18-context7-mcp-ti-shi-zhu` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-05` [AWS Transform MCP arbitrary file write](2026-08-05-aws-transform-mcp.md)<br>  <sub>AWS Transform MCP arbitrary file write</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-08-17` [AI finds a flaw AI helped write: Snowflake's Jira token](2026-08-17-snowflake-jira-zhao-dao-can.md)<br>  <sub>AI finds a flaw AI helped write: Snowflake's Jira token</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-18-context7-mcp-ti-shi-zhu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
