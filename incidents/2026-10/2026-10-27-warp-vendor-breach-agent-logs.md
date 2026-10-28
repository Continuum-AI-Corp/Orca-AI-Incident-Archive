---
id: 2026-10-27-warp-vendor-breach-agent-logs
title: "Warp discloses a third-party vendor breach that exposed AI-agent decision logs and user telemetry"
title_zh: "Warp 披露第三方供应商被攻破，泄露了 AI agent 决策日志与用户遥测"
title_ja: "Warp、第三者ベンダー侵害でAIエージェントの決定ログとユーザーテレメトリが流出と公表"
title_ko: "Warp, 제3자 벤더 침해로 AI 에이전트 결정 로그와 사용자 텔레메트리 유출 공개"
title_de: "Warp meldet einen Drittanbieter-Einbruch, bei dem KI-Agenten-Entscheidungslogs und Nutzer-Telemetrie offengelegt wurden"
title_fr: "Warp signale une brèche chez un fournisseur tiers ayant exposé les journaux de décision d'agents IA et la télémétrie des utilisateurs"
title_es: "Warp revela una brecha en un proveedor externo que expuso los registros de decisiones de agentes de IA y la telemetría de usuarios"
date: 2026-10-27
date_raw: "2026-10-27 (Warp disclosure)"
date_precision: day

kind: incident
type: [EXFIL, INFRA]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 27 October 2026, **Warp** — an agentic development environment / AI terminal — disclosed that an attack on a **third-party vendor** in its infrastructure exposed **AI-agent decision logs and user telemetry**.** CEO Zach Lloyd said Warp detected the activity on a Friday, estimated roughly **1% of its users** may be affected (Warp reports **800,000+** users, implying several thousand accounts), and said it has engaged **CrowdStrike**, notified law enforcement, and alerted affected users. Warp **did not clarify** whether source code, prompts, or credentials were among the exposed data — the confirmed categories are agent decision logs and telemetry. Reports describing an "agent-swarm" attack are an analyst **hypothesis, not a confirmed attribution**, and the vendor has not been named. Recorded `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true` — a real breach exposing agent-specific operational data, scope and sensitivity still bounded/unconfirmed.

summary_zh: |
  **2026 年 10 月 27 日，**Warp**——一个 agentic 开发环境／AI 终端——披露：其基础设施中一家**第三方供应商**遭攻击，泄露了 **AI agent 决策日志与用户遥测**。** CEO Zach Lloyd 称 Warp 在某个周五检测到该活动，估计约 **1% 用户**可能受影响（Warp 称有 **80 万+** 用户，意味着数千账户），并已请 **CrowdStrike** 介入、通知执法、告知受影响用户。Warp **未说明**暴露数据是否含源码、prompt 或凭证——已确认的类别是 agent 决策日志与遥测。将其描述为"agent 蜂群"攻击的说法只是分析**假设、未经证实**，供应商名称也未公布。记为 `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`——一次真实泄露、暴露了 agent 专有的运行数据，但范围与敏感度仍有界/未确认。

summary_ja: |
  **2026年10月27日、**Warp**（agentic開発環境／AIターミナル）は、インフラ内の**第三者ベンダー**への攻撃により **AIエージェントの決定ログとユーザーテレメトリ**が流出したと公表した。** CEOのZach Lloyd氏は、ある金曜にこの活動を検知し、約**1%のユーザー**が影響を受けた可能性があると見積もり（Warpのユーザーは**80万人超**で、数千アカウントに相当）、**CrowdStrike**を起用し、法執行機関に通知、影響を受けたユーザーに連絡したと述べた。Warpは、流出データにソースコード・プロンプト・認証情報が含まれていたかは**明言していない**——確認されたのはエージェントの決定ログとテレメトリである。「エージェント・スウォーム」攻撃という記述は分析上の**仮説であり確定した帰属ではなく**、ベンダー名も公表されていない。`incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`

summary_ko: |
  **2026년 10월 27일, **Warp**(agentic 개발 환경/AI 터미널)는 인프라 내 **제3자 벤더**에 대한 공격으로 **AI 에이전트 결정 로그와 사용자 텔레메트리**가 유출됐다고 공개했다.** CEO Zach Lloyd는 금요일에 해당 활동을 탐지했으며 약 **1% 사용자**가 영향받았을 수 있다고 추정하고(Warp는 **80만 명 이상** 사용자로, 수천 계정에 해당), **CrowdStrike**를 투입하고 법 집행기관에 통지, 영향받은 사용자에게 알렸다고 밝혔다. Warp는 유출 데이터에 소스 코드·프롬프트·자격 증명이 포함됐는지 **밝히지 않았다**——확인된 범주는 에이전트 결정 로그와 텔레메트리다. "에이전트 스웜" 공격이라는 서술은 분석상 **가설이며 확정된 귀속이 아니고**, 벤더명도 공개되지 않았다. `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`

summary_de: |
  **Am 27. Oktober 2026 teilte **Warp** — eine agentische Entwicklungsumgebung / ein KI-Terminal — mit, dass ein Angriff auf einen **Drittanbieter** in seiner Infrastruktur **KI-Agenten-Entscheidungslogs und Nutzer-Telemetrie** offengelegt habe.** CEO Zach Lloyd sagte, Warp habe die Aktivität an einem Freitag entdeckt, schätzte, dass etwa **1% der Nutzer** betroffen sein könnten (Warp nennt **800.000+** Nutzer, also mehrere Tausend Konten), und habe **CrowdStrike** eingeschaltet, Strafverfolgungsbehörden informiert und betroffene Nutzer benachrichtigt. Warp hat **nicht klargestellt**, ob Quellcode, Prompts oder Anmeldedaten zu den offengelegten Daten gehörten — bestätigt sind Agenten-Entscheidungslogs und Telemetrie. Beschreibungen eines „Agent-Swarm"-Angriffs sind eine Analysten-**Hypothese, keine bestätigte Zuordnung**, und der Anbieter wurde nicht genannt. `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`

summary_fr: |
  **Le 27 octobre 2026, **Warp** — un environnement de développement agentique / terminal IA — a signalé qu'une attaque contre un **fournisseur tiers** de son infrastructure avait exposé les **journaux de décision d'agents IA et la télémétrie des utilisateurs**.** Le PDG Zach Lloyd a dit que Warp avait détecté l'activité un vendredi, estimé qu'environ **1 % des utilisateurs** pourraient être touchés (Warp déclare **800 000+** utilisateurs, soit plusieurs milliers de comptes), et qu'il avait sollicité **CrowdStrike**, prévenu les forces de l'ordre et alerté les utilisateurs concernés. Warp **n'a pas précisé** si du code source, des prompts ou des identifiants figuraient parmi les données exposées — les catégories confirmées sont les journaux de décision d'agents et la télémétrie. Les descriptions d'une attaque en « essaim d'agents » relèvent d'une **hypothèse d'analyste, pas d'une attribution confirmée**, et le fournisseur n'a pas été nommé. `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`

summary_es: |
  **El 27 de octubre de 2026, **Warp** —un entorno de desarrollo agéntico / terminal de IA— reveló que un ataque a un **proveedor externo** de su infraestructura expuso los **registros de decisiones de agentes de IA y la telemetría de usuarios**.** El CEO Zach Lloyd dijo que Warp detectó la actividad un viernes, estimó que cerca del **1 % de los usuarios** podría estar afectado (Warp declara **más de 800.000** usuarios, lo que implica varios miles de cuentas), y que ha contratado a **CrowdStrike**, notificado a las autoridades y avisado a los usuarios afectados. Warp **no aclaró** si el código fuente, los prompts o las credenciales estaban entre los datos expuestos — las categorías confirmadas son registros de decisiones de agentes y telemetría. Las descripciones de un ataque de "enjambre de agentes" son una **hipótesis de analistas, no una atribución confirmada**, y no se ha nombrado al proveedor. `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true`

sources:
  - url: https://www.bleepingcomputer.com/news/security/warp-discloses-breach-exposing-ai-agent-logs-user-telemetry-data/
    label: BleepingComputer
  - url: https://atlabyte.com/en/news/warp-reports-data-breach-ai-agent-logs-and-user-telemetry-affected
    label: Atlabyte
  - url: https://www.archyde.com/warp-exposes-user-logs-and-telemetry-in-third-party-vendor-breach/
    label: Archyde
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.34"
---

# Warp discloses a third-party vendor breach that exposed AI-agent decision logs and user telemetry

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**On 27 October 2026, Warp — an agentic development environment / AI terminal — disclosed that an attack on a third-party vendor in its infrastructure exposed AI-agent decision logs and user telemetry.** CEO Zach Lloyd said Warp detected the activity on a Friday, estimated roughly 1% of its users may be affected (Warp reports 800,000+ users, implying several thousand accounts), and said it has engaged CrowdStrike, notified law enforcement, and alerted affected users. Warp did not clarify whether source code, prompts, or credentials were among the exposed data — the confirmed categories are agent decision logs and telemetry. Reports describing an "agent-swarm" attack are an analyst hypothesis, not a confirmed attribution, and the vendor has not been named. Recorded `incident` / `EXFIL` + `INFRA` / `medium` / `real_harm: true` — a real breach exposing agent-specific operational data, scope and sensitivity still bounded/unconfirmed.

## Attack chain

```mermaid
flowchart LR
    E["Attack on a third-party vendor in<br/>Warp's infrastructure"]:::entry
    S1["AI-agent decision logs and user<br/>telemetry exposed"]:::step
    S2["~1% of 800k+ users; source code /<br/>prompts / credentials unconfirmed"]:::step
    I["CrowdStrike engaged; law enforcement<br/>notified; affected users alerted"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **27 October 2026**, Warp — an **agentic development environment / AI terminal** — disclosed a breach affecting a **third-party vendor** in its infrastructure. The exposed data, per the company, consisted of **AI-agent decision logs and user telemetry**. CEO **Zach Lloyd** said the activity was detected on a Friday and that the incident remains under investigation.

**Scope and response.** Lloyd estimated roughly **1% of users** may be affected; with Warp reporting **800,000+** users, that implies several thousand accounts. Warp has engaged **CrowdStrike** to assist, **notified law enforcement**, and **alerted affected users**. The company has **not named the vendor** and has **not clarified** whether source code, prompts, or credentials were among the exposed data — only agent decision logs and telemetry are confirmed. Because agent decision logs can capture what a coding agent did and saw, security commentators advised affected users to rotate any secrets they may have pasted into Warp AI.

**Caveats.** Some coverage frames this as an "agent-swarm" intrusion, but that is an **analyst working hypothesis, not a confirmed attribution** by Warp. The precise sensitivity of the exposed logs is not established.

**How it is graded.** `incident` — a confirmed, real breach, not a disclosed-but-unused flaw. `EXFIL` (agent-specific data left the trust boundary via the vendor compromise) and `INFRA` (the exposed asset is the operational data of an agentic development platform). `real_harm: true`: real user data (agent decision logs + telemetry) was exposed in a confirmed breach affecting real accounts — unlike a demo. Severity `medium`: bounded to ~1% of users and the sensitivity of the exposed logs is unconfirmed (no confirmed source code, prompt, or credential leak), so it is not graded higher. Confidence `A`: BleepingComputer's first reporting plus Warp's CEO statement and independent coverage.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/warp-discloses-breach-exposing-ai-agent-logs-user-telemetry-data/> |
| 2 | Atlabyte | <https://atlabyte.com/en/news/warp-reports-data-breach-ai-agent-logs-and-user-telemetry-affected> |
| 3 | Archyde | <https://www.archyde.com/warp-exposes-user-logs-and-telemetry-in-third-party-vendor-breach/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-27` (raw: 2026-10-27 Warp disclosure, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`EXFIL`](../../taxonomy/types.md#exfil) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **Medium** `medium` |
| Confidence | **A** — BleepingComputer + Warp CEO statement + independent coverage |
| Real harm | Yes — agent decision logs and user telemetry exposed in a confirmed breach affecting real accounts |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-27-warp-vendor-breach-agent-logs` |

<sub>**Why this classification:** A confirmed third-party-vendor breach of the Warp agentic development platform that exposed agent decision logs and user telemetry (`EXFIL` — agent data left the boundary; `INFRA` — operational data of an agent platform). `incident` with `real_harm: true` because real user data was exposed in a real breach. `medium` because it is bounded (~1% of users) and the sensitivity is unconfirmed (no confirmed source/prompt/credential leak); the "agent-swarm" attribution is an unconfirmed hypothesis. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-17` [OpenCode Console breach exposes users' stored AI-provider API keys](2026-10-17-opencode-console-breach-api-keys.md)<br>  <sub>Another agent-platform breach exposing user data the same month</sub>
- `2026-09-29` [PixelLeak: coding agents pushed internal screenshots to public GitHub](../2026-09/2026-09-29-pixelleak-coding-agents-screenshots-github.md)<br>  <sub>Another exposure of agent-side operational data</sub>
- `2026-09-26` [Meta Muse marketplace address leak](../2026-09/2026-09-26-meta-muse-marketplace-address-leak.md)<br>  <sub>Another agent-platform data exposure</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-27-warp-vendor-breach-agent-logs.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
