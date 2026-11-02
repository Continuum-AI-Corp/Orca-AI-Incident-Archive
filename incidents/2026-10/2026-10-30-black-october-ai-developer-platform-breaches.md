---
id: 2026-10-30-black-october-ai-developer-platform-breaches
title: "\"Black October\": a coordinated wave breached at least nine AI developer platforms to harvest AI-access credentials"
title_zh: "\"Black October\"：一场协同攻击在一个月内攻破至少九家 AI 开发平台、收割可解锁 AI 的凭证"
title_ja: "「Black October」：協調的な攻撃がひと月で少なくとも9つのAI開発プラットフォームを侵害し、AIアクセス用の認証情報を収集"
title_ko: "\"Black October\": 한 달 새 최소 9개 AI 개발 플랫폼을 침해해 AI 접근용 자격 증명을 수집한 공조 공격"
title_de: "„Black October": Eine koordinierte Welle kompromittierte mindestens neun KI-Entwicklerplattformen, um KI-Zugangs-Credentials abzugreifen"
title_fr: "« Black October » : une vague coordonnée a compromis au moins neuf plateformes de développement IA pour récolter des identifiants d'accès à l'IA"
title_es: "\"Black October\": una oleada coordinada vulneró al menos nueve plataformas de desarrollo de IA para robar credenciales de acceso a IA"
date: 2026-10-30
date_raw: "2026-10-30 (Wiz \"Black October\" synthesis; campaign activity ~2026-10-06 to 2026-10-30)"
date_precision: day

kind: incident
type: [CRED, INFRA]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 30 October 2026, Wiz published "Black October," documenting a coordinated wave in which at least nine AI developer platforms disclosed security incidents in a single month, with attackers "explicitly hunting stored environment variables, with a focus on those granting AI access."** The nine: Fireworks AI (Oct 6), Andromeda (Oct 9), Zeabur (Oct 14), Lightning AI (Oct 15), OpenCode (Oct 16–17), Railway (Oct 20), Warp (Oct 23), CommandCode (Oct 28), and Northflank (Oct 30). Several victims (Fireworks, OpenCode, Warp) reported indications of an **"agent-swarm"** attack. Stolen keys were abused **within ~30 minutes** for AWS Bedrock `InvokeModel` calls from residential IPs, and downstream resale operations ("momo", "Xingjiabi") were observed — though Wiz says it cannot definitively link the resellers to the initial compromise. Independently, **Zeabur's own report** confirms ~**3.2M environment-variable records** read (and the company is shutting down), and **Railway's own report** confirms encrypted env vars were accessed (third parties cite up to 100k workspaces; an alleged $371k crypto theft is unverified). Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true` — a confirmed, cross-platform campaign targeting AI credentials; attribution is loose (Wiz does not tie it to one actor) and several per-platform investigations are ongoing.

summary_zh: |
  **2026 年 10 月 30 日，Wiz 发布《Black October》报告：记录了一个月内至少九家 AI 开发平台相继披露安全事件的协同攻击浪潮，攻击者"明确地猎取存储的环境变量，尤其是能授予 AI 访问权限的那些"。** 九家为：Fireworks AI（10-6）、Andromeda（10-9）、Zeabur（10-14）、Lightning AI（10-15）、OpenCode（10-16/17）、Railway（10-20）、Warp（10-23）、CommandCode（10-28）、Northflank（10-30）。数家受害方（Fireworks、OpenCode、Warp）报告有 **"agent 蜂群"** 攻击迹象。被窃的 key **在约 30 分钟内**即被用于从住宅 IP 发起 AWS Bedrock `InvokeModel` 调用，并观察到下游转售团伙（"momo"、"Xingjiabi"）——不过 Wiz 称无法确证转售方与最初入侵的直接关联。独立地，**Zeabur 自己的报告**确认约 **320 万条环境变量记录**被读取（且公司将关停），**Railway 自己的报告**确认加密环境变量被访问（第三方称涉最多 10 万 workspace；所称 $37.1 万加密货币被盗未经证实）。记为 `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`——一场已确认、跨平台、瞄准 AI 凭证的战役；归因松散（Wiz 未归于单一 actor），多家平台的调查仍在进行。

summary_ja: |
  **2026年10月30日、Wizは「Black October」を公開し、ひと月で少なくとも9つのAI開発プラットフォームが相次いでセキュリティ事案を公表した協調的な攻撃の波を記録した。攻撃者は「保存された環境変数、とりわけAIアクセスを与えるものを明確に狙った」。** 9社：Fireworks AI（10/6）、Andromeda（10/9）、Zeabur（10/14）、Lightning AI（10/15）、OpenCode（10/16–17）、Railway（10/20）、Warp（10/23）、CommandCode（10/28）、Northflank（10/30）。複数の被害者（Fireworks、OpenCode、Warp）は「エージェント・スウォーム」攻撃の兆候を報告した。盗まれた鍵は**約30分以内**に住宅IPからのAWS Bedrock `InvokeModel`呼び出しに悪用され、下流の転売組織（「momo」「Xingjiabi」）も観測された（ただしWizは転売と初期侵害の直接的関連は断定できないとする）。独立して、**Zeabur自身の報告**は約**320万件の環境変数レコード**の読み取りを確認し（同社は事業を停止）、**Railway自身の報告**は暗号化環境変数へのアクセスを確認した。`incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_ko: |
  **2026년 10월 30일, Wiz는 "Black October"를 공개해 한 달 새 최소 9개 AI 개발 플랫폼이 잇따라 보안 사고를 공개한 공조 공격 물결을 기록했다. 공격자는 "저장된 환경 변수, 특히 AI 접근을 부여하는 변수를 명시적으로 노렸다."** 9곳: Fireworks AI(10/6), Andromeda(10/9), Zeabur(10/14), Lightning AI(10/15), OpenCode(10/16–17), Railway(10/20), Warp(10/23), CommandCode(10/28), Northflank(10/30). 여러 피해자(Fireworks, OpenCode, Warp)가 **"에이전트 스웜"** 공격 정황을 보고했다. 탈취된 키는 **약 30분 이내**에 주거용 IP에서 AWS Bedrock `InvokeModel` 호출에 악용됐고, 하류 재판매 조직("momo", "Xingjiabi")도 관측됐다(단 Wiz는 재판매와 최초 침해의 직접 연관은 단정할 수 없다고 밝힘). 독립적으로 **Zeabur 자체 보고서**는 약 **320만 건의 환경 변수 레코드** 열람을 확인했고(회사는 서비스 종료 예정), **Railway 자체 보고서**는 암호화 환경 변수 접근을 확인했다. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_de: |
  **Am 30. Oktober 2026 veröffentlichte Wiz „Black October" und dokumentierte eine koordinierte Angriffswelle, bei der in einem einzigen Monat mindestens neun KI-Entwicklerplattformen Sicherheitsvorfälle meldeten — die Angreifer „jagten gezielt gespeicherte Umgebungsvariablen, mit Fokus auf solche, die KI-Zugang gewähren".** Die neun: Fireworks AI (6.10.), Andromeda (9.10.), Zeabur (14.10.), Lightning AI (15.10.), OpenCode (16.–17.10.), Railway (20.10.), Warp (23.10.), CommandCode (28.10.) und Northflank (30.10.). Mehrere Opfer (Fireworks, OpenCode, Warp) meldeten Hinweise auf einen „Agent-Swarm"-Angriff. Gestohlene Schlüssel wurden **binnen ~30 Minuten** für AWS-Bedrock-`InvokeModel`-Aufrufe von Residential-IPs missbraucht, und nachgelagerte Wiederverkaufs-Operationen („momo", „Xingjiabi") wurden beobachtet. Unabhängig bestätigt **Zeaburs eigener Bericht** ~**3,2 Mio. Umgebungsvariablen-Datensätze** als gelesen (das Unternehmen stellt den Betrieb ein), und **Railways eigener Bericht** bestätigt Zugriff auf verschlüsselte Umgebungsvariablen. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_fr: |
  **Le 30 octobre 2026, Wiz a publié « Black October », documentant une vague coordonnée au cours de laquelle au moins neuf plateformes de développement IA ont signalé des incidents de sécurité en un seul mois — les attaquants « traquant explicitement les variables d'environnement stockées, en ciblant celles qui donnent accès à l'IA ».** Les neuf : Fireworks AI (6 oct.), Andromeda (9 oct.), Zeabur (14 oct.), Lightning AI (15 oct.), OpenCode (16–17 oct.), Railway (20 oct.), Warp (23 oct.), CommandCode (28 oct.) et Northflank (30 oct.). Plusieurs victimes (Fireworks, OpenCode, Warp) ont signalé des indices d'une attaque en « essaim d'agents ». Les clés volées ont été exploitées **en ~30 minutes** pour des appels AWS Bedrock `InvokeModel` depuis des IP résidentielles, et des opérations de revente en aval (« momo », « Xingjiabi ») ont été observées. Indépendamment, **le rapport de Zeabur** confirme ~**3,2 M d'enregistrements de variables d'environnement** lus (l'entreprise ferme), et **le rapport de Railway** confirme l'accès à des variables d'environnement chiffrées. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

summary_es: |
  **El 30 de octubre de 2026, Wiz publicó "Black October", documentando una oleada coordinada en la que al menos nueve plataformas de desarrollo de IA revelaron incidentes de seguridad en un solo mes — con los atacantes "cazando explícitamente variables de entorno almacenadas, centrándose en las que otorgan acceso a IA".** Las nueve: Fireworks AI (6 oct), Andromeda (9 oct), Zeabur (14 oct), Lightning AI (15 oct), OpenCode (16–17 oct), Railway (20 oct), Warp (23 oct), CommandCode (28 oct) y Northflank (30 oct). Varias víctimas (Fireworks, OpenCode, Warp) reportaron indicios de un ataque de "enjambre de agentes". Las claves robadas se abusaron **en ~30 minutos** para llamadas AWS Bedrock `InvokeModel` desde IP residenciales, y se observaron operaciones de reventa ("momo", "Xingjiabi"). De forma independiente, **el propio informe de Zeabur** confirma la lectura de ~**3,2 M de registros de variables de entorno** (la empresa cierra), y **el informe de Railway** confirma el acceso a variables de entorno cifradas. `incident` / `CRED` + `INFRA` / `high` / `real_harm: true`

sources:
  - url: https://wiz.io/blog/black-october-for-ai-developer-platforms
    label: Wiz Research ("Black October")
  - url: https://zeabur.com/blogs/october-2026-security-incident
    label: Zeabur (preliminary incident report)
  - url: https://www.bleepingcomputer.com/news/security/zeabur-shutting-down-after-second-security-breach-in-two-months/
    label: BleepingComputer (Zeabur)
  - url: https://blog.railway.com/p/preliminary-report-october-security-incident
    label: Railway (preliminary incident report)
  - url: https://www.axios.com/2026/10/28/cybersecurity-black-october-ai-hacks
    label: Axios
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.35"
---

# "Black October": a coordinated wave breached at least nine AI developer platforms to harvest AI-access credentials

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-8F6A3C?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-3C6E8F?style=flat-square)

## Summary

**On 30 October 2026, Wiz published "Black October," documenting a coordinated wave in which at least nine AI developer platforms disclosed security incidents in a single month, with attackers "explicitly hunting stored environment variables, with a focus on those granting AI access."** The nine: Fireworks AI (Oct 6), Andromeda (Oct 9), Zeabur (Oct 14), Lightning AI (Oct 15), OpenCode (Oct 16–17), Railway (Oct 20), Warp (Oct 23), CommandCode (Oct 28), and Northflank (Oct 30). Several victims (Fireworks, OpenCode, Warp) reported indications of an "agent-swarm" attack. Stolen keys were abused within ~30 minutes for AWS Bedrock `InvokeModel` calls from residential IPs, and downstream resale operations ("momo", "Xingjiabi") were observed — though Wiz says it cannot definitively link the resellers to the initial compromise. Independently, Zeabur's own report confirms ~3.2M environment-variable records read (and the company is shutting down), and Railway's own report confirms encrypted env vars were accessed (third parties cite up to 100k workspaces; an alleged $371k crypto theft is unverified). Recorded `incident` / `CRED` + `INFRA` / `high` / `real_harm: true` — a confirmed, cross-platform campaign targeting AI credentials; attribution is loose (Wiz does not tie it to one actor) and several per-platform investigations are ongoing.

## Attack chain

```mermaid
flowchart LR
    E["≥9 AI developer platforms<br/>(Oct 6–30, 2026)"]:::entry
    S1["Attackers hunt stored env vars,<br/>esp. those granting AI access"]:::step
    S2["Stolen keys abused in ~30 min:<br/>AWS Bedrock InvokeModel from residential IPs"]:::step
    I["Zeabur ~3.2M env-var records read (shutting down);<br/>Railway encrypted env vars accessed; resale ('momo'/'Xingjiabi')"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What "Black October" is.** On **30 October 2026**, Wiz researchers (Benjamin Read, Rami McCarthy) published **"Black October for AI Developer Platforms,"** synthesizing a month in which **at least nine AI developer platforms disclosed security incidents**. Wiz frames them as connected by a shared pattern rather than attributed to a single operator: *"While there is no single vulnerability or dependency linking these attacks, the overall picture is strongly aligned…"* The common thread: *"All public reports highlight targeted exploitation, explicitly hunting stored environment variables, with a focus on those granting AI access."* Axios covered the wave on **28 October** (framing it as a "Y2K lesson" for AI developer tooling).

**The nine platforms (with disclosed/observed dates).**

| Platform | Date | What was reported |
|---|---|---|
| Fireworks AI | Oct 6 | Reported **indications of an "agent-swarm" attack**; root cause attributed to credential access |
| Andromeda | Oct 9 | Called the attack part of an "industry-wide attack" |
| **Zeabur** | Oct 14 | Leaked internal credentials → shared cluster → platform DB; **~3.2M env-var records read**; **company shutting down** |
| Lightning AI | Oct 15 | Credential access (previously hit in the Mini-Shai-Hulud supply-chain campaign) |
| **OpenCode** | Oct 16–17 | **Indications of an "agent-swarm" attack** — *already in this archive* ([record](2026-10-17-opencode-console-breach-api-keys.md)) |
| Railway | Oct 20 | Privilege escalation in build infrastructure; **encrypted env vars accessed** (third parties: up to 100k workspaces); alleged $371k crypto theft **unverified** |
| **Warp** | Oct 23 | **Indications of an "agent-swarm" attack**; third-party vendor dependency — *already in this archive* ([record](2026-10-27-warp-vendor-breach-agent-logs.md)) |
| CommandCode | Oct 28 | Attributed its incident to an attempted "distillation" |
| Northflank | Oct 30 | Listed; details pending |

**The "agent-swarm" thread and downstream abuse.** Fireworks, OpenCode, and Warp each reported *indications* of an "agent-swarm" attack. Wiz observed that the **first unauthorized use of stolen keys came within ~30 minutes** of credential access — a single `InvokeModel` call from a residential IP, sweeping multiple organizations in a one-minute burst. Wiz also documented two reselling operations for abused LLM tokens ("momo", centered on `23.106.46.239`; "Xingjiabi", at `xingjiabiapi.org` / `38.246.114.118`), but states plainly: *"We do not have evidence that links them directly to the 'Black October' attacks."* No CVE is named; Wiz assigns no formal threat-actor name.

**Independently confirmed harm.** This record does not rest on Wiz alone. **Zeabur's own preliminary report** (and BleepingComputer/SCWorld coverage) confirms that, on **Oct 14–15**, an attacker used leaked plaintext internal credentials (not rotated after an August breach) to reach the shared cluster and read the platform database — **~3.2M environment-variable records** — and that Zeabur is **winding down** (services stop by 31 Dec 2026). **Railway's own preliminary report** confirms a privilege-escalation issue in build infrastructure (Oct 20) and anomalous access to systems storing customer environment variables (Oct 21), with encrypted env vars possibly accessed.

**How it is graded.** `incident` — a confirmed, real, cross-platform campaign (multiple victims published their own breach reports), not a single disclosed flaw. `CRED` (the defining loot is AI-access credentials / API keys / tokens harvested from env vars) + `INFRA` (AI developer platforms are the attack surface). `real_harm: true`: Zeabur read of ~3.2M records and forced shutdown, Railway env-var access, and confirmed Bedrock token abuse are real-world harm. Severity `high` rather than critical: breadth is large and one platform is shutting down, but attribution is deliberately loose (Wiz ties nothing to a single actor), several per-platform investigations are ongoing, and the largest dollar claims (Railway's alleged $371k; OpenCode's "consumer bills in the hundreds to thousands") are unverified social-media reports. Confidence `A`: Wiz research + Zeabur's and Railway's own reports + BleepingComputer/SCWorld + Axios.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Wiz Research ("Black October") | <https://wiz.io/blog/black-october-for-ai-developer-platforms> |
| 2 | Zeabur (preliminary incident report) | <https://zeabur.com/blogs/october-2026-security-incident> |
| 3 | BleepingComputer (Zeabur shutting down) | <https://www.bleepingcomputer.com/news/security/zeabur-shutting-down-after-second-security-breach-in-two-months/> |
| 4 | Railway (preliminary incident report) | <https://blog.railway.com/p/preliminary-report-october-security-incident> |
| 5 | Axios | <https://www.axios.com/2026/10/28/cybersecurity-black-october-ai-hacks> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-30` (raw: 2026-10-30 Wiz "Black October" synthesis; campaign activity ~2026-10-06 to 2026-10-30, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`CRED`](../../taxonomy/types.md#cred) [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **High** `high` |
| Confidence | **A** — Wiz research + Zeabur's & Railway's own reports + BleepingComputer/SCWorld + Axios |
| Real harm | Yes — Zeabur ~3.2M env-var records read and shutting down; Railway encrypted env vars accessed; Bedrock token abuse confirmed |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-30-black-october-ai-developer-platform-breaches` |

<sub>**Why this classification:** A confirmed, cross-platform campaign (≥9 AI developer platforms in one month) whose defining goal was harvesting stored environment variables that grant AI access (`CRED`), with the platforms themselves as the attack surface (`INFRA`). `incident` with `real_harm: true` because multiple victims published their own breach reports with concrete impact (Zeabur ~3.2M records + shutdown; Railway env-var access; Bedrock abuse). `high`, not critical: broad but with loose attribution (Wiz ties it to no single actor), ongoing per-platform investigations, and unverified top-line dollar claims. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-27` [Warp discloses a third-party vendor breach that exposed AI-agent decision logs and user telemetry](2026-10-27-warp-vendor-breach-agent-logs.md)<br>  <sub>One of the nine "Black October" platforms, recorded individually</sub>
- `2026-10-17` [OpenCode Console breach exposes users' stored AI-provider API keys](2026-10-17-opencode-console-breach-api-keys.md)<br>  <sub>Another of the nine, recorded individually</sub>
- `2026-10-21` [LiteLLM 1.107.0 supply-chain compromise](2026-10-21-litellm-1-107-supply-chain-compromise.md)<br>  <sub>Same month, AI infrastructure targeted for credentials</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-30-black-october-ai-developer-platform-breaches.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
