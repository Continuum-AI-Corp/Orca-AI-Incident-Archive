---
id: 2026-06-08-agentforger-yi-tiao-lian-jie
title: "AgentForger: one link forges an \"AI insider\""
title_zh: "AgentForger：一条链接伪造出一个「AI 内鬼」"
title_ja: "AgentForger：1つのリンクで「AIインサイダー」を鋳造"
title_ko: "AgentForger: 링크 하나로 \"AI 내부자\"를 위조하다"
title_de: "AgentForger: Ein Link erzeugt einen „KI-Insider“"
title_fr: "AgentForger : un lien fabrique un « initié IA »"
title_es: "AgentForger: un enlace forja un \"insider de IA\""
date: 2026-06-08
date_precision: day
date_raw: "2026-06-08"

kind: research
type: [IPI, CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Zenity Labs (researcher Mike Takahashi); OpenAI fixed it on 06-08 and disclosed it in July. This is a **CSRF — but what gets forged is an attacker-controlled autonomous AI agent**. An employee opening one seemingly harmless ChatGPT link spawns a new agent inside the company's trust boundary, **under that employee's real permissions and with approvals turned off**. This "agentic insider" can map the org chart, exfiltrate sensitive documents and harvest credentials, and it **impersonates the victim on Slack, Teams and email**; reports say it **fetches new instructions from the attacker every five minutes**


summary_zh: |
  Zenity Labs（研究者 Mike Takahashi），OpenAI 于 06-08 修复、07 月公开。这是一次 **CSRF —— 但伪造出来的是一个攻击者控制的自主 AI agent**。员工点开一条看起来无害的 ChatGPT 链接，就会在公司信任边界内**凭该员工的真实权限、且审批被关掉**地生成一个新 agent。这个「agentic 内鬼」可以测绘组织结构、外带敏感文档、收割凭据，并**在 Slack、Teams 与邮件中冒充受害者**；报道称它**每五分钟就向攻击者领一次指令**

summary_ja: |
  Zenity Labs（研究者Mike Takahashi氏）。OpenAIは06-08に修正し、7月に公表した。これは**CSRFだが、偽造されるのは攻撃者制御の自律AIエージェントである**。従業員が一見無害なChatGPTリンクを開くと、企業の信頼境界の内側に新しいエージェントが生成される——**その従業員の実際の権限で、承認はオフのまま**。この「エージェント型インサイダー」は組織図を把握し、機密文書を外部送信し、認証情報を収集でき、**Slack、Teams、メールで被害者になりすます**。報告によれば**5分ごとに攻撃者から新しい指示を取得する**という

summary_ko: |
  Zenity Labs(연구자 Mike Takahashi). OpenAI는 06-08에 수정하고 7월에 공개했다. 이것은 **CSRF지만 위조되는 것은 공격자가 제어하는 자율 AI 에이전트**다. 직원이 무해해 보이는 ChatGPT 링크 하나를 열면 회사의 신뢰 경계 안에 새 에이전트가 생겨나며, **그 직원의 실제 권한으로 승인 절차는 꺼진 상태**다. 이 "에이전틱 내부자"는 조직도를 파악하고 민감 문서를 유출하며 자격 증명을 수집할 수 있고, **Slack, Teams, 이메일에서 피해자를 사칭**한다. 보도에 따르면 **5분마다 공격자로부터 새 지시를 받아온다**

summary_de: |
  Zenity Labs (Forscher Mike Takahashi); OpenAI behob es am 06-08 und legte es im Juli offen. Dies ist eine **CSRF — doch gefälscht wird ein vom Angreifer kontrollierter autonomer KI-Agent**. Ein Mitarbeiter, der einen scheinbar harmlosen ChatGPT-Link öffnet, erzeugt einen neuen Agenten innerhalb der Vertrauensgrenze des Unternehmens, **unter den echten Berechtigungen dieses Mitarbeiters und mit abgeschalteten Genehmigungen**. Dieser „agentische Insider“ kann das Organigramm kartieren, sensible Dokumente exfiltrieren und Zugangsdaten sammeln, und er **gibt sich auf Slack, Teams und per E-Mail als das Opfer aus**; Berichten zufolge **holt er alle fünf Minuten neue Anweisungen vom Angreifer**

summary_fr: |
  Zenity Labs (chercheur Mike Takahashi) ; OpenAI l'a corrigé le 06-08 et divulgué en juillet. C'est un **CSRF — mais ce qui est forgé est un agent IA autonome contrôlé par l'attaquant**. Un employé qui ouvre un lien ChatGPT apparemment inoffensif fait naître un nouvel agent à l'intérieur du périmètre de confiance de l'entreprise, **sous les permissions réelles de cet employé et avec les approbations désactivées**. Cet « initié agentique » peut cartographier l'organigramme, exfiltrer des documents sensibles et récolter des identifiants, et il **usurpe la victime sur Slack, Teams et par e-mail** ; des rapports indiquent qu'il **récupère de nouvelles instructions auprès de l'attaquant toutes les cinq minutes**

summary_es: |
  Zenity Labs (el investigador Mike Takahashi); OpenAI lo corrigió el 06-08 y lo divulgó en julio. Esto es un **CSRF — pero lo que se forja es un agente de IA autónomo controlado por el atacante**. Un empleado que abre un enlace aparentemente inofensivo de ChatGPT hace nacer un nuevo agente dentro del límite de confianza de la empresa, **con los permisos reales de ese empleado y con las aprobaciones desactivadas**. Este "insider agéntico" puede mapear el organigrama, exfiltrar documentos sensibles y recolectar credenciales, y **suplanta a la víctima en Slack, Teams y el correo**; los informes dicen que **obtiene nuevas instrucciones del atacante cada cinco minutos**

sources:
  - url: https://labs.zenity.io/p/agentforger-part-1-chatgpt-cross-site-agent-forgery
    label: Zenity Labs
  - url: https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html
    label: THN

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# AgentForger: one link forges an "AI insider"

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Zenity Labs (researcher Mike Takahashi); OpenAI fixed it on 06-08 and disclosed it in July. This is a **CSRF — but what gets forged is an attacker-controlled autonomous AI agent**. An employee opening one seemingly harmless ChatGPT link spawns a new agent inside the company's trust boundary, **under that employee's real permissions and with approvals turned off**. This "agentic insider" can map the org chart, exfiltrate sensitive documents and harvest credentials, and it **impersonates the victim on Slack, Teams and email**; reports say it **fetches new instructions from the attacker every five minutes**

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["The agent picks it up and calls it"]:::step
    I["Credential abuse<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Zenity Labs | <https://labs.zenity.io/p/agentforger-part-1-chatgpt-cross-site-agent-forgery> |
| 2 | THN | <https://thehackernews.com/2026/07/chatgpt-agentforger-flaw-could-deploy.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-08` (raw: 2026-06-08, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-08-agentforger-yi-tiao-lian-jie` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-04` [Claude Oceanus-v1-p illegally redistributed](2026-06-04-claude-oceanus-fei-fa-fen.md)<br>  <sub>Claude Oceanus-v1-p illegally redistributed</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-08-agentforger-yi-tiao-lian-jie.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
