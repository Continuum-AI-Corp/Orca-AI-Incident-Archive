---
id: 2026-09-25-divd-agentic-ai-breach
title: "An autonomous AI agent breached DIVD, the Dutch vulnerability-disclosure nonprofit"
title_zh: "一个自主 AI agent 入侵了荷兰漏洞披露机构 DIVD"
title_ja: "自律型AIエージェントがオランダの脆弱性開示NPO・DIVDに侵入"
title_ko: "자율 AI 에이전트가 네덜란드 취약점 공개 비영리기관 DIVD를 침해했다"
title_de: "Ein autonomer KI-Agent kompromittierte DIVD, die niederländische Non-Profit für Schwachstellenoffenlegung"
title_fr: "Un agent IA autonome a compromis DIVD, l'ONG néerlandaise de divulgation de vulnérabilités"
title_es: "Un agente de IA autónomo vulneró DIVD, la ONG neerlandesa de divulgación de vulnerabilidades"
date: 2026-09-25
date_raw: "DIVD CSIRT 2026-09-24 / confirmed 2026-09-25 / update 2026-09-28 / BleepingComputer 2026-09-29"
date_precision: day

kind: incident
type: [WEAPON]
severity: medium
confidence: A
real_harm: true
ai_involvement: confirmed

region: [EU]

summary: |
  **DIVD, the Dutch Institute for Vulnerability Disclosure — a nonprofit of volunteer researchers that scans the internet for flaws and warns owners — disclosed that after almost seven years it "got hacked," and that the intrusion was carried out autonomously by an AI agent.** DIVD: *"This is an attack we have not seen before … the modus operandi indicates that this is an agentic AI powered attack."* The actor exploited a *"technical vulnerability"* in an undisclosed system (DIVD explicitly said it was **not** Citrix NetScaler), then used an automated agent for post-exploitation: *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic."* The agent *"did some pretty dumb things"* — including interfering with its own adversary-in-the-middle attack via password spraying — and *"over-explain[ed] its decisions in its comments,"* which DIVD says will help reverse-engineer the incident; it believes the agent was *"poorly trained and configured."* DIVD isolated its infrastructure, engaged a third-party forensics team, notified affected parties, reported to the **Autoriteit Persoonsgegevens** (data-protection authority) and the **NCSC**, and consulted police, handling it as *"assume breach until proven otherwise,"* with a fuller update due 1 October. Recorded `incident` / `WEAPON` / `medium` / `real_harm: true`.

summary_zh: |
  **荷兰漏洞披露机构 DIVD（一个由志愿研究者组成、在互联网上扫描漏洞并通知责任方的非营利组织）披露：在近七年之后它"被黑了"，而且这次入侵是由一个 AI agent 自主完成的。** DIVD 称：*「这是一种我们此前没见过的攻击……其作案手法表明这是一次 agentic AI 驱动的攻击。」* 攻击者利用某个未披露系统的*「技术漏洞」*（DIVD 明确表示**不是** Citrix NetScaler）拿到入口后，用一个自动化 agent 做后渗透：*「我们能看到这个 agent 在自动运行，因为它每做完一步就自己决定下一步，快得惊人、逻辑却很糙。」* 这个 agent*「干了些相当蠢的事」*——包括用密码喷洒把自己的中间人攻击搞砸——还*「在注释里把自己的决策过度解释了一番」*，DIVD 说这反而有助于逆向复盘；他们判断该 agent*「训练与配置都很差」*。DIVD 已隔离基础设施、聘请第三方取证团队、通知受影响方，并上报**荷兰数据保护局（AP）**与 **NCSC**、与警方商议，按*「先假定已被入侵，直到证明并非如此」*处理，更详细的更新定于 10 月 1 日。本条记为 `incident` / `WEAPON` / `medium` / `real_harm: true`。

summary_ja: |
  **オランダの脆弱性開示NPO・DIVD（ボランティア研究者がインターネットを走査して欠陥を所有者に通知する非営利団体）は、約7年を経て「ハッキングされた」こと、そしてその侵入がAIエージェントによって自律的に実行されたことを公表した。** DIVD：*「これは我々が見たことのない攻撃だ……手口はagentic AIによる攻撃であることを示している。」* 攻撃者は未公開システムの*「技術的脆弱性」*（DIVDはCitrix NetScaringではないと明言）を突いて侵入し、自動化エージェントでポストエクスプロイトを行った：*「エージェントが自動で動いているのが見えた。各アクションの後に自分で次の手を決め、猛烈な速さで、雑なロジックだった。」* エージェントは*「かなり間抜けなこと」*——パスワードスプレーで自らの中間者攻撃を妨害するなど——をし、*「コメントで自分の判断を過剰に説明」*しており、これが逆解析に役立つとDIVDは言う。DIVDはインフラを隔離し、第三者フォレンジックを起用し、影響当事者に通知し、**個人データ保護局（AP）**と**NCSC**に報告し、警察と協議、*「証明されるまで侵害を前提」*として対応、より詳しい更新は10月1日の予定。`incident` / `WEAPON` / `medium` / `real_harm: true`

summary_ko: |
  **네덜란드 취약점 공개 비영리기관 DIVD(자원봉사 연구자들이 인터넷을 스캔해 결함을 소유자에게 알리는 비영리단체)가 약 7년 만에 "해킹당했다"고, 그리고 그 침입이 AI 에이전트에 의해 자율적으로 수행됐다고 공개했다.** DIVD: *"이것은 우리가 본 적 없는 공격이다 … 수법이 agentic AI 기반 공격임을 가리킨다."* 공격자는 미공개 시스템의 *"기술적 취약점"*(DIVD는 Citrix NetScaler가 **아니라고** 명시)을 악용해 침입한 뒤 자동화 에이전트로 사후 공격을 수행했다: *"에이전트가 자동으로 작동하는 것이 보였다. 각 행동 후 스스로 다음 단계를 정했고, 빛의 속도로, 엉성한 로직이었다."* 에이전트는 *"꽤 멍청한 짓들"*(패스워드 스프레이로 자신의 중간자 공격을 방해하는 등)을 했고 *"주석에 자기 결정을 과하게 설명"*했으며, 이것이 역분석에 도움이 된다고 DIVD는 말한다. DIVD는 인프라를 격리하고 제3자 포렌식 팀을 투입했으며 영향받은 당사자에 통지하고 **개인정보보호청(AP)**과 **NCSC**에 신고, 경찰과 협의했고, *"입증 전까지 침해 가정"*으로 대응하며 더 자세한 업데이트는 10월 1일 예정이다. `incident` / `WEAPON` / `medium` / `real_harm: true`

summary_de: |
  **DIVD, das Dutch Institute for Vulnerability Disclosure — eine Non-Profit aus freiwilligen Forschern, die das Internet nach Schwachstellen absucht und Betreiber warnt — teilte mit, dass es nach fast sieben Jahren „gehackt" wurde und dass der Angriff autonom von einem KI-Agenten ausgeführt wurde.** DIVD: *"This is an attack we have not seen before … the modus operandi indicates that this is an agentic AI powered attack."* Der Akteur nutzte eine *"technical vulnerability"* in einem nicht genannten System (ausdrücklich **nicht** Citrix NetScaler) und setzte dann einen automatisierten Agenten für die Post-Exploitation ein: *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic."* Der Agent *"did some pretty dumb things"* — u. a. störte er per Password-Spraying seinen eigenen Adversary-in-the-Middle-Angriff — und *"over-explain[ed] its decisions in its comments"*, was laut DIVD das Reverse-Engineering erleichtert; er sei *"poorly trained and configured"* gewesen. DIVD isolierte seine Infrastruktur, zog ein externes Forensik-Team hinzu, benachrichtigte Betroffene, meldete an die **Autoriteit Persoonsgegevens** und das **NCSC** und beriet sich mit der Polizei, unter der Annahme *"assume breach until proven otherwise"*; ein ausführlicheres Update folgt am 1. Oktober. Verzeichnet als `incident` / `WEAPON` / `medium` / `real_harm: true`

summary_fr: |
  **DIVD, l'Institut néerlandais de divulgation de vulnérabilités — une ONG de chercheurs bénévoles qui scanne internet à la recherche de failles et alerte les propriétaires — a révélé qu'après presque sept ans il « s'est fait pirater », et que l'intrusion a été menée de façon autonome par un agent IA.** DIVD : *"This is an attack we have not seen before … the modus operandi indicates that this is an agentic AI powered attack."* L'acteur a exploité une *"technical vulnerability"* dans un système non divulgué (explicitement **pas** Citrix NetScaler), puis a utilisé un agent automatisé pour la post-exploitation : *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic."* L'agent *"did some pretty dumb things"* — dont perturber sa propre attaque de type adversary-in-the-middle par password spraying — et *"over-explain[ed] its decisions in its comments"*, ce qui, selon DIVD, aidera à la rétro-ingénierie ; il était *"poorly trained and configured"*. DIVD a isolé son infrastructure, engagé une équipe de forensique tierce, notifié les parties concernées, signalé à l'**Autoriteit Persoonsgegevens** et au **NCSC**, et consulté la police, en traitant l'affaire comme *"assume breach until proven otherwise"* ; une mise à jour plus complète est prévue le 1er octobre. Enregistré `incident` / `WEAPON` / `medium` / `real_harm: true`

summary_es: |
  **DIVD, el Instituto Neerlandés de Divulgación de Vulnerabilidades — una ONG de investigadores voluntarios que rastrea internet en busca de fallos y avisa a los propietarios — reveló que tras casi siete años «lo hackearon», y que la intrusión la ejecutó de forma autónoma un agente de IA.** DIVD: *"This is an attack we have not seen before … the modus operandi indicates that this is an agentic AI powered attack."* El actor explotó una *"technical vulnerability"* en un sistema no divulgado (explícitamente **no** Citrix NetScaler) y luego usó un agente automatizado para la post-explotación: *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic."* El agente *"did some pretty dumb things"* — entre ellas interferir en su propio ataque adversary-in-the-middle mediante password spraying — y *"over-explain[ed] its decisions in its comments"*, lo que según DIVD ayudará a la ingeniería inversa; creen que estaba *"poorly trained and configured"*. DIVD aisló su infraestructura, contrató a un equipo forense externo, notificó a los afectados, reportó a la **Autoriteit Persoonsgegevens** y al **NCSC**, y consultó a la policía, tratándolo como *"assume breach until proven otherwise"*; habrá una actualización más completa el 1 de octubre. Registrado `incident` / `WEAPON` / `medium` / `real_harm: true`

sources:
  - url: https://csirt.divd.nl/2026/09/24/when-not-if/
    label: DIVD CSIRT (primary)
  - url: https://www.bleepingcomputer.com/news/security/automated-ai-agent-used-to-breach-cybersecurity-nonprofit-divd/
    label: BleepingComputer
  - url: https://databreaches.net/2026/09/25/divd-dutch-institute-for-vulnerability-disclosure-investigating-agentic-ai-powered-attack/
    label: DataBreaches.Net
disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §13.23"
---

# An autonomous AI agent breached DIVD, the Dutch vulnerability-disclosure nonprofit

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-1F9D55?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-8F6A3C?style=flat-square)

## Summary

**DIVD, the Dutch Institute for Vulnerability Disclosure — a nonprofit of volunteer researchers that scans the internet for flaws and warns owners — disclosed that after almost seven years it "got hacked," and that the intrusion was carried out autonomously by an AI agent.** DIVD: *"This is an attack we have not seen before … the modus operandi indicates that this is an agentic AI powered attack."* The actor exploited a *"technical vulnerability"* in an undisclosed system (DIVD explicitly said it was **not** Citrix NetScaler), then used an automated agent for post-exploitation: *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic."* The agent *"did some pretty dumb things"* — including interfering with its own adversary-in-the-middle attack via password spraying — and *"over-explain[ed] its decisions in its comments,"* which DIVD says will help reverse-engineer the incident; it believes the agent was *"poorly trained and configured."* DIVD isolated its infrastructure, engaged a third-party forensics team, notified affected parties, reported to the **Autoriteit Persoonsgegevens** (data-protection authority) and the **NCSC**, and consulted police, handling it as *"assume breach until proven otherwise,"* with a fuller update due 1 October. Recorded `incident` / `WEAPON` / `medium` / `real_harm: true`.

## Attack chain

```mermaid
flowchart LR
    E["Attacker exploits a technical vulnerability<br/>in an undisclosed DIVD system (not NetScaler)"]:::entry
    S1["An automated AI agent runs post-exploitation,<br/>deciding each next step itself at machine speed"]:::step
    S2["Sloppy: password-spraying interferes with its own<br/>AitM; over-explains its decisions in comments"]:::step
    I["DIVD detects it, isolates infra, forensics + notifies<br/>AP / NCSC / police; 'assume breach'"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** DIVD — a volunteer nonprofit that scans the internet for known vulnerabilities and notifies owners — said in a CSIRT post ("It was a matter of when, not if…", 24 September) that it had detected suspicious activity, investigated, and concluded it had been breached: *"we're the hackers that got hacked."* In a follow-up on Monday 28 September it added detail while withholding specifics to protect the investigation and other potential victims. The distinguishing feature is the actor's method: *"This is an attack we have not seen before. Not because it's our first, but because the modus operandi indicates that this is an agentic AI-powered attack."* The attacker exploited a *"technical vulnerability"* in an undisclosed system — DIVD specifically noted it was **not** Citrix NetScaler — and then used an automated AI agent for the post-exploitation phase.

**How the agent behaved.** DIVD describes an autonomous loop, not a human operator: *"We could see the agent working automated, because after every action it decided the next step itself, at the speed of light and sloppy logic or pattern."* The attack was *"loud and very very messy,"* leaving ample evidence: the agent *"did some pretty dumb things,"* including interfering with its own adversary-in-the-middle attack via password spraying, and it *"over-explain[ed] its decisions in its comments."* DIVD believes the agent was *"poorly trained and configured for such operations,"* which is why it left enough behind to reconstruct the incident.

**Response and grading.** DIVD went into full incident response — isolating its infrastructure, engaging a third-party incident-response team for forensics, notifying directly involved parties, reporting to the **Autoriteit Persoonsgegevens** and the **National Cyber Security Centre**, and discussing options with police — and is treating the situation as *"assume breach until proven otherwise,"* with a fuller update promised for **1 October** (and a pledge to warn other victims of the same vulnerability). Recorded `incident` / `WEAPON`: a human-directed intrusion whose post-exploitation was run by an autonomous agent. `real_harm: true` — a confirmed unauthorized intrusion into a real organisation's network, reported to the regulator and police. `medium` rather than `high` because the concrete impact is not yet established (DIVD is still in forensics, the agent was "messy" and self-caught); this may be revised after the 1 October update. Confidence **A**: the affected party's own first-hand disclosure, corroborated by BleepingComputer and DataBreaches.Net.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | DIVD CSIRT — "It was a matter of when, not if…" | <https://csirt.divd.nl/2026/09/24/when-not-if/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/automated-ai-agent-used-to-breach-cybersecurity-nonprofit-divd/> |
| 3 | DataBreaches.Net | <https://databreaches.net/2026/09/25/divd-dutch-institute-for-vulnerability-disclosure-investigating-agentic-ai-powered-attack/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-25` (raw: DIVD CSIRT 2026-09-24 / confirmed 2026-09-25 / update 2026-09-28 / BleepingComputer 2026-09-29, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) |
| Severity | **Medium** `medium` |
| Confidence | **A** — the affected party's own disclosure plus independent reporting |
| Real harm | Yes — a confirmed unauthorized intrusion, reported to the regulator and police |
| AI involvement | Confirmed `confirmed` |
| Region | [EU](../../regions/eu.md) — Netherlands |
| Archive ID | `2026-09-25-divd-agentic-ai-breach` |

<sub>**Why this classification:** a human-directed intrusion whose post-exploitation was carried out by an autonomous AI agent (`WEAPON`). `real_harm: true` because an organisation's network was actually breached and the incident was reported to the Dutch DPA and police, even though the exact impact is still under forensic investigation. `medium` rather than `high` because the concrete damage is not yet quantified and DIVD detected and contained it; the 1 October update may warrant a revision. Dated to the confirmed intrusion / first public disclosure (24–25 September); the widely-read BleepingComputer write-up is 29 September. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution (WEAPON)](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-25` [JadePuffer/Storm-3168: an agentic actor deletes an Azure tenant's storage](2026-09-25-jadepuffer-storm3168-azure-destruction.md)<br>  <sub>The same week — another autonomous agent running post-exploitation against a real target</sub>
- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](../2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Near-autonomous agent intrusion of a real organisation, with a Hermes/OpenClaw stack</sub>
- `2026-09-22` [CARBONATO: a Docker botnet installs Hermes Agent and loots AI API keys](2026-09-22-carbonato-docker-hermes-agent-botnet.md)<br>  <sub>Agent installed on the victim as the post-exploitation brain</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-25-divd-agentic-ai-breach.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
