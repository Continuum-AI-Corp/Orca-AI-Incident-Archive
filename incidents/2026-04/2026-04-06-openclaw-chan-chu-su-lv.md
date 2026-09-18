---
id: 2026-04-06-openclaw-chan-chu-su-lv
title: "OpenClaw's CVE rate: 2.2 per day"
title_zh: "OpenClaw 的 CVE 产出速率：每天 2.2 个"
title_ja: "OpenClawのCVE発生率：1日あたり2.2件"
title_ko: "OpenClaw의 CVE 발생률: 하루 2.2건"
title_de: "OpenClaws CVE-Rate: 2.2 pro Tag"
title_fr: "Le rythme de CVE d'OpenClaw : 2,2 par jour"
title_es: "La tasa de CVE de OpenClaw: 2.2 por día"
date: 2026-04-06
date_precision: day
date_raw: "2026-04-06"

kind: policy
type: [INFRA]
severity: info
confidence: B
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  As of 2026-04-06 OpenClaw had accumulated **138 CVEs**, all inside a single **63-day** window — about **2.2 per day**, of which **7 critical and 49 high**. The most severe, **CVE-2026-22172** and **CVE-2026-32922**, are both **CVSS 9.9** (unauthenticated administrative control and privilege escalation respectively). Also: **the first formal audit on 2026-01-25 alone found 512 vulnerabilities, 8 of them critical**
  💡 The rate itself is a data point: **a component that produced 138 CVEs in two months is being installed on developer machines as a personal AI assistant**


summary_zh: |
  截至 2026-04-06，OpenClaw 累计 **138 个 CVE**，全部集中在一个 **63 天**的窗口内 —— 约 **2.2 个/天**，其中 **7 个 critical、49 个 high**。最严重的 **CVE-2026-22172** 与 **CVE-2026-32922** 均为 **CVSS 9.9**（分别为无凭据取得管理控制、权限提升）。另：**2026-01-25 的首次正式审计就发现 512 个漏洞，其中 8 个 critical**
  💡 这个速率本身就是一条数据：**一个在两个月内爆出 138 个 CVE 的组件，正被当作个人 AI 助理装在开发机上**

summary_ja: |
  2026-04-06時点でOpenClawは**138件のCVE**を蓄積しており、すべて**63日間**という単一の期間内——1日あたり約**2.2件**で、うち**7件がcritical、49件がhigh**。最も深刻な**CVE-2026-22172**と**CVE-2026-32922**はいずれも**CVSS 9.9**（それぞれ認証不要の管理制御と権限昇格）。また、**2026-01-25の最初の正式監査だけで512件の脆弱性が見つかり、うち8件がcritical**だった。
  💡 この発生率自体がデータ点である：**2か月で138件のCVEを生んだコンポーネントが、パーソナルAIアシスタントとして開発者のマシンにインストールされている**

summary_ko: |
  2026-04-06 기준 OpenClaw은 **CVE 138건**을 누적했고, 모두 **63일**이라는 한 구간 안에서 발생했다 — 하루 약 **2.2건**이며 그중 **심각 7건, 높음 49건**이다. 가장 심각한 **CVE-2026-22172**와 **CVE-2026-32922**는 모두 **CVSS 9.9**다(각각 무인증 관리 통제와 권한 상승). 또한 **2026-01-25 첫 정식 감사에서만 취약점 512건이 발견되었고 그중 8건이 심각**이었다
  💡 이 발생률 자체가 하나의 데이터 포인트다: **두 달에 CVE 138건을 쏟아낸 구성 요소가 개인 AI 어시스턴트로 개발자 머신에 설치되고 있다**

summary_de: |
  Stand 2026-04-06 hatte OpenClaw **138 CVEs** angesammelt, alle innerhalb eines einzigen **63-Tage**-Fensters — etwa **2.2 pro Tag**, davon **7 kritisch und 49 hoch**. Die schwersten, **CVE-2026-22172** und **CVE-2026-32922**, liegen beide bei **CVSS 9.9** (nicht authentifizierte administrative Kontrolle bzw. Rechteerweiterung). Außerdem: **Allein das erste formelle Audit am 2026-01-25 fand 512 Schwachstellen, 8 davon kritisch**
  💡 Die Rate selbst ist ein Datenpunkt: **Eine Komponente, die in zwei Monaten 138 CVEs hervorbrachte, wird als persönlicher KI-Assistent auf Entwicklerrechnern installiert**

summary_fr: |
  Au 2026-04-06, OpenClaw avait accumulé **138 CVE**, toutes dans une seule fenêtre de **63 jours** — environ **2,2 par jour**, dont **7 critiques et 49 élevées**. Les plus graves, **CVE-2026-22172** et **CVE-2026-32922**, sont toutes deux **CVSS 9.9** (contrôle administratif non authentifié et élévation de privilèges respectivement). Autre point : **le premier audit formel, le 2026-01-25, a lui seul trouvé 512 vulnérabilités, dont 8 critiques**
  💡 Le rythme est en soi une donnée : **un composant qui a produit 138 CVE en deux mois est installé sur les machines des développeurs comme assistant IA personnel**

summary_es: |
  Hasta el 2026-04-06 OpenClaw había acumulado **138 CVE**, todos dentro de una única ventana de **63 días** — unos **2.2 por día**, de los cuales **7 críticos y 49 altos**. Los más graves, **CVE-2026-22172** y **CVE-2026-32922**, son ambos **CVSS 9.9** (control administrativo sin autenticación y escalada de privilegios, respectivamente). Además: **solo la primera auditoría formal, el 2026-01-25, encontró 512 vulnerabilidades, 8 de ellas críticas**
  💡 La tasa en sí es un dato: **un componente que produjo 138 CVE en dos meses se está instalando en las máquinas de los desarrolladores como asistente personal de IA**

sources:
  - url: https://www.betterclaw.io/blog/openclaw-security-2026
    label: CVE roundup
  - url: https://www.armosec.io/blog/cve-2026-32922-openclaw-privilege-escalation-cloud-security/
    label: "ARMO(CVE-2026-32922)"

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# OpenClaw's CVE rate: 2.2 per day

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

As of 2026-04-06 OpenClaw had accumulated **138 CVEs**, all inside a single **63-day** window — about **2.2 per day**, of which **7 critical and 49 high**. The most severe, **CVE-2026-22172** and **CVE-2026-32922**, are both **CVSS 9.9** (unauthenticated administrative control and privilege escalation respectively). Also: **the first formal audit on 2026-01-25 alone found 512 vulnerabilities, 8 of them critical**

💡 The rate itself is a data point: **a component that produced 138 CVEs in two months is being installed on developer machines as a personal AI assistant**

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CVE roundup | <https://www.betterclaw.io/blog/openclaw-security-2026> |
| 2 | ARMO(CVE-2026-32922) | <https://www.armosec.io/blog/cve-2026-32922-openclaw-privilege-escalation-cloud-security/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-06` (raw: 2026-04-06, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **Info** `info` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-06-openclaw-chan-chu-su-lv` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 exploited in the wild](2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-23` [OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed](2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>
- `2026-04-01` [Google Vertex AI "Double Agent" permission abuse](2026-04-01-google-vertex-double-agent.md)<br>  <sub>Google Vertex AI "Double Agent" permission abuse</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-06-openclaw-chan-chu-su-lv.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
