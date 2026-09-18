---
id: 2026-05-21-composio-agent-automation-privesc
title: "Composio: agent automation itself becomes the privilege-escalation path"
title_zh: "Composio：agent 自动化本身成了提权路径"
title_ja: "Composio：エージェント自動化そのものが権限昇格経路になる"
title_ko: "Composio: 에이전트 자동화 자체가 권한 상승 경로가 되다"
title_de: "Composio: Agentenautomatisierung selbst wird zum Pfad der Rechteerweiterung"
title_fr: "Composio : l'automatisation d'agents devient elle-même la voie d'élévation de privilèges"
title_es: "Composio: la propia automatización de agentes se convierte en la vía de escalada de privilegios"
date: 2026-05-21
date_precision: day
date_raw: "2026-05-21"

kind: incident
type: [CRED, SUPPLY]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Agentic integration platform Composio self-disclosed that an attacker exfiltrated **about 5,241 API keys and 5,001 GitHub OAuth tokens**.
  The attack chain deserves a note of its own: the attacker **first gained a foothold on an internal agentic tool that monitors Composio's own infrastructure**, then **escalated through the automated remediation system that repairs connector errors**, registered malicious tool definitions in the platform sandbox and finally achieved arbitrary code execution inside the tool-execution sandbox — **an agent meant to automate operations became the attacker's escalation ladder**


summary_zh: |
  agentic 集成平台 Composio 自曝：攻击者外带 **约 5,241 个 API key 与 5,001 个 GitHub OAuth token**。
  攻击链值得单独记：攻击者**先在一个「监控 Composio 自身基础设施的内部 agentic 工具」上取得立足点**，再**经由那套「自动修复连接器错误的自动化补救系统」提权**，然后在平台沙箱中注册恶意工具定义，最终在工具执行沙箱内取得任意代码执行 —— **用来自动化运维的 agent，成了攻击者的提权阶梯**

summary_ja: |
  エージェント連携プラットフォームのComposioが、攻撃者に**約5,241件のAPIキーと5,001件のGitHub OAuthトークン**を外部送信されたと自行公表した。
  攻撃チェーンは特筆に値する：攻撃者は**まずComposio自身のインフラを監視する社内エージェントツールに足場を築き**、次に**コネクタのエラーを修復する自動修復システムを通じて権限を昇格**させ、プラットフォームのサンドボックスに悪性のツール定義を登録し、最終的にツール実行サンドボックス内で任意コード実行を達成した——**運用自動化のためのエージェントが、攻撃者の昇格のはしごになった**

summary_ko: |
  에이전트 통합 플랫폼 Composio는 공격자가 **API 키 약 5,241개와 GitHub OAuth 토큰 5,001개**를 유출했다고 자체 공개했다.
  공격 사슬은 따로 언급할 가치가 있다: 공격자는 **먼저 Composio 자체 인프라를 모니터링하는 내부 에이전틱 도구에서 발판을 얻고**, **커넥터 오류를 복구하는 자동 교정 시스템을 통해 권한을 상승**시킨 뒤 플랫폼 샌드박스에 악성 도구 정의를 등록해 마침내 도구 실행 샌드박스 안에서 임의 코드 실행을 달성했다 — **운영 자동화를 위한 에이전트가 공격자의 권한 상승 사다리가 된 것이다**

summary_de: |
  Die agentische Integrationsplattform Composio hat selbst offengelegt, dass ein Angreifer **etwa 5,241 API-Schlüssel und 5,001 GitHub-OAuth-Token** exfiltrierte.
  Die Angriffskette verdient eine eigene Anmerkung: Der Angreifer **verschaffte sich zunächst einen Fußpunkt auf einem internen agentischen Tool, das Composios eigene Infrastruktur überwacht**, **eskalierte dann über das automatisierte Behebungssystem, das Connector-Fehler repariert**, registrierte bösartige Tool-Definitionen in der Plattform-Sandbox und erreichte schließlich beliebige Codeausführung innerhalb der Tool-Ausführungs-Sandbox — **ein Agent, der den Betrieb automatisieren sollte, wurde zur Eskalationsleiter des Angreifers**

summary_fr: |
  La plateforme d'intégration agentique Composio a auto-divulgué qu'un attaquant a exfiltré **environ 5 241 clés API et 5 001 jetons OAuth GitHub**.
  La chaîne d'attaque mérite une note à part : l'attaquant **a d'abord pris pied sur un outil agentique interne qui surveille l'infrastructure de Composio**, puis **s'est élevé via le système de remédiation automatique qui répare les erreurs de connecteurs**, a enregistré des définitions d'outils malveillantes dans le bac à sable de la plateforme et a finalement obtenu une exécution de code arbitraire dans le bac à sable d'exécution d'outils — **un agent censé automatiser les opérations est devenu l'échelle d'escalade de l'attaquant**

summary_es: |
  La plataforma de integración agéntica Composio autodivulgó que un atacante exfiltró **unas 5,241 claves de API y 5,001 tokens OAuth de GitHub**.
  La cadena de ataque merece una nota aparte: el atacante **primero obtuvo un punto de apoyo en una herramienta agéntica interna que monitorea la propia infraestructura de Composio**, luego **escaló a través del sistema de remediación automatizada que repara errores de conectores**, registró definiciones de herramientas maliciosas en el sandbox de la plataforma y finalmente logró ejecución de código arbitrario dentro del sandbox de ejecución de herramientas — **un agente destinado a automatizar operaciones se convirtió en la escalera de escalada del atacante**

sources:
  - url: https://composio.dev/blog/composio-may-2026-security-incident
    label: Composio official incident report
  - url: https://material.security/resources/the-composio-breach-one-token-10242-doors
    label: Material Security analysis

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Composio: agent automation itself becomes the privilege-escalation path

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Agentic integration platform Composio self-disclosed that an attacker exfiltrated **about 5,241 API keys and 5,001 GitHub OAuth tokens**.

The attack chain deserves a note of its own: the attacker **first gained a foothold on an internal agentic tool that monitors Composio's own infrastructure**, then **escalated through the automated remediation system that repairs connector errors**, registered malicious tool definitions in the platform sandbox and finally achieved arbitrary code execution inside the tool-execution sandbox — **an agent meant to automate operations became the attacker's escalation ladder**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    S1["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Composio official incident report | <https://composio.dev/blog/composio-may-2026-security-incident> |
| 2 | Material Security analysis | <https://material.security/resources/the-composio-breach-one-token-10242-doors> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-21` (raw: 2026-05-21, precision `day`) |
| Kind | Incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse · [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-21-composio-agent-automation-privesc` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>
- `2026-05-04` [Braintrust's AWS account compromised, all customers told to rotate AI keys](2026-05-04-braintrust-aws-zhang-hao-gong.md)<br>  <sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-21-composio-agent-automation-privesc.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
