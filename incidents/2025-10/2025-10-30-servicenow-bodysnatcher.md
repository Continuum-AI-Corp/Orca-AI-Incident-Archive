---
id: 2025-10-30-servicenow-bodysnatcher
title: "ServiceNow BodySnatcher"
title_zh: "ServiceNow BodySnatcher"
title_ja: "ServiceNow BodySnatcher"
title_ko: "ServiceNow BodySnatcher"
title_de: "ServiceNow BodySnatcher"
title_fr: "ServiceNow BodySnatcher"
title_es: "BodySnatcher de ServiceNow"
date: 2025-10-30
date_precision: day
date_raw: "2025-10-30"

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  AppOmni discovered CVE-2025-12420, **CVSS 9.3**. The Virtual Agent API **issues the same hard-coded key** `servicenowexternalagent` to **every customer**; combined with trusted-email account linking it lets an attacker bypass MFA/SSO and impersonate any user. Fixes were pushed to most hosted instances on 10-30


summary_zh: |
  AppOmni 发现 CVE-2025-12420，**CVSS 9.3**。Virtual Agent API 对**所有客户下发同一个硬编码密钥** `servicenowexternalagent`，配合信任邮箱的账号关联逻辑可绕过 MFA/SSO 冒充任意用户。10-30 向多数托管实例推送修复

summary_ja: |
  AppOmniがCVE-2025-12420を発見、**CVSS 9.3**。Virtual Agent APIは**同じハードコードされたキー**`servicenowexternalagent`を**すべての顧客に**発行しており、信頼済みメールによるアカウント連携と組み合わせると、攻撃者はMFA/SSOをバイパスして任意のユーザーになりすませる。修正は10-30に大半のホスト型インスタンスへ適用された

summary_ko: |
  AppOmni는 CVE-2025-12420(**CVSS 9.3**)을 발견했다. Virtual Agent API가 **동일한 하드코딩 키** `servicenowexternalagent`를 **모든 고객에게** 발급하며, 신뢰 이메일 계정 연결과 결합하면 공격자가 MFA/SSO를 우회해 아무 사용자나 사칭할 수 있다. 10-30 대부분의 호스팅 인스턴스에 수정이 배포되었다

summary_de: |
  AppOmni entdeckte CVE-2025-12420, **CVSS 9.3**. Die Virtual-Agent-API **gibt denselben fest codierten Schlüssel** `servicenowexternalagent` **jedem Kunden** aus; zusammen mit der Kontoverknüpfung über vertrauenswürdige E-Mail-Adressen kann ein Angreifer MFA/SSO umgehen und sich als beliebiger Nutzer ausgeben. Die Korrekturen wurden am 10-30 auf die meisten gehosteten Instanzen ausgerollt

summary_fr: |
  AppOmni a découvert CVE-2025-12420, **CVSS 9.3**. L'API Virtual Agent **délivre la même clé codée en dur** `servicenowexternalagent` à **chaque client** ; combinée à l'association de comptes par e-mail de confiance, elle permet à un attaquant de contourner MFA/SSO et d'usurper n'importe quel utilisateur. Les correctifs ont été déployés sur la plupart des instances hébergées le 10-30

summary_es: |
  AppOmni descubrió CVE-2025-12420, **CVSS 9.3**. La API de Virtual Agent **entrega la misma clave codificada de forma fija** `servicenowexternalagent` a **todos los clientes**; combinado con la vinculación de cuentas por correo confiable, permite a un atacante eludir MFA/SSO y suplantar a cualquier usuario. Las correcciones se aplicaron a la mayoría de las instancias alojadas el 10-30

sources:
  - url: https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/
    label: AppOmni
  - url: https://cyberscoop.com/servicenow-fixes-critical-ai-vulnerability-cve-2025-12420/
    label: CyberScoop

disputed: false
landmark: false
scan_month: 2025-10
scan_ref: "SCAN.md §5 2025-10"
---

# ServiceNow BodySnatcher

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

AppOmni discovered CVE-2025-12420, **CVSS 9.3**. The Virtual Agent API **issues the same hard-coded key** `servicenowexternalagent` to **every customer**; combined with trusted-email account linking it lets an attacker bypass MFA/SSO and impersonate any user. Fixes were pushed to most hosted instances on 10-30

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | AppOmni | <https://appomni.com/ao-labs/bodysnatcher-agentic-ai-security-vulnerability-in-servicenow/> |
| 2 | CyberScoop | <https://cyberscoop.com/servicenow-fixes-critical-ai-vulnerability-cve-2025-12420/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-10-30` (raw: 2025-10-30, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-10-30-servicenow-bodysnatcher` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2025-11-01` [ShadowRay 2.0 (Ray framework)](../2025-11/2025-11-01-shadowray-2-ray-framework.md)<br>  <sub>ShadowRay 2.0 (Ray framework)</sub>
- `2026-01-26` [Clawdbot gateways exposed at scale](../2026-01/2026-01-26-clawdbot-wang-guan-gui-mo.md)<br>  <sub>Clawdbot gateways exposed at scale</sub>
- `2026-01-29` [OpenClaw Control UI WebSocket hijack RCE](../2026-01/2026-01-29-openclaw-control-ui-websocket.md)<br>  <sub>OpenClaw Control UI WebSocket hijack RCE</sub>
- `2026-02-28` [CodeWall breaches McKinsey's internal "Lilli" AI platform](../2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br>  <sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub>

---

[← 2025-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-10/2025-10-30-servicenow-bodysnatcher.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
