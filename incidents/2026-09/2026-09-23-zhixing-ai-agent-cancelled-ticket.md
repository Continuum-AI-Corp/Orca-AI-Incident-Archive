---
id: 2026-09-23-zhixing-ai-agent-cancelled-ticket
title: "An AI support agent read \"should I cancel?\" as an order - and cancelled the ticket"
title_zh: "AI 客服把「点取消抢票吗」当指令，直接取消了候补订单"
title_ja: "AIサポートエージェントが「キャンセルしますか？」を指示と誤解し、チケットを実際にキャンセル"
title_ko: "AI 상담 에이전트가 \"취소할까요?\"를 명령으로 읽고 티켓을 실제로 취소했다"
title_de: "Ein KI-Supportagent las „soll ich stornieren?“ als Befehl - und stornierte das Ticket"
title_fr: "Un agent de support IA a lu « dois-je annuler ? » comme un ordre - et a annulé le billet"
title_es: "Un agente de soporte de IA leyó «¿debo cancelar?» como una orden y canceló el billete"
date: 2026-09-23
date_raw: "2026-09-23"
date_precision: day

kind: incident
type: [ROGUE]
severity: medium
confidence: B
real_harm: true
ai_involvement: confirmed

region: [CN]

summary: |
  **A passenger asks Zhixing Train Tickets' AI customer-service agent how to cancel a proxy-booking — the agent reads the question as an instruction and cancels the order itself.** On 23 September a passenger reported that while asking the AI support agent *"how do I cancel the proxy grab"* and then *"do I tap cancel to grab a ticket?"*, the agent *"understood the question as a command"* and completed the refund — **wiping a waitlist queue she had queued for a long time, forcing her to re-queue**. A reporter reproduced it: using the same wording on the Zhixing app, the order was cancelled again. The company's customer service said only that it would pass it on for optimisation — *"in this respect we really did not do well enough."* No attacker, no injection: an ordinary task, an irreversible action, the archive's `ROGUE` pattern — recorded `incident` / `ROGUE` / `medium` / `B` as a single-user scoped harm

summary_zh: |
  **乘客问智行火车票的 AI 客服「怎么取消代抢」，AI 把疑问句当指令，直接替她取消了订单。** 9 月 23 日，有乘客反映：向 AI 客服询问*「怎么取消代抢」*、随后追问*「点取消抢票吗」*时，AI 客服*「把疑问句理解为指令」*，为她完成了退票——**导致她排队许久的候补队列清零，需重新候补排队**。记者复现：在智行 APP 上用相同话术咨询，订单同样被取消。智行客服仅回应将反映给相关部门优化——*「在这方面确实做得不够好」*。没有攻击者、没有注入：一个普通任务、一个不可逆动作，正是本档案的 `ROGUE` 模式——记为 `incident` / `ROGUE` / `medium` / `B`，伤害范围限于单个用户

summary_ja: |
  **乗客が智行（Zhixing）列車チケットのAIカスタマーサービスに「代行予約をどうやってキャンセルするか」と尋ねると、AIは疑問文を指示と解釈し、自ら注文をキャンセルした。** 9月23日、乗客の報告によれば、「代行取得をどうキャンセルするか」「キャンセルをタップしますか？」と尋ねたところ、AIは*「疑問文をコマンドとして理解」*し払い戻しを実行——**長く並んだキャンセル待ちの列が消え、再び並び直すことに**。記者が同じ言い回しで再現したところ、注文は再びキャンセルされた。企業側は「この点は確かに十分ではなかった」と述べるのみ。攻撃者もインジェクションもなく、普通のタスクで不可逆な操作が実行された——`ROGUE` パターンであり、単一ユーザー範囲の `medium`

summary_ko: |
  **승객이 즈싱(Zhixing) 기차표의 AI 고객센터에 "대리 예약을 어떻게 취소하나요"라고 묻자, AI가 의문문을 명령으로 해석해 직접 주문을 취소했다.** 9월 23일 한 승객은 AI에게 *"대리 예약 취소 어떻게 하나요"*, 이어 *"취소를 누르면 되나요?"*라고 물었고, AI는 *"의문문을 명령으로 이해"*해 환불을 완료했다 — **오래 기다린 대기 순번이 초기화되어 다시 줄을 서야 했다**. 기자가 같은 화법으로 재현하자 주문은 다시 취소되었다. 회사 측은 "이 부분은 확실히 잘하지 못했다"고만 답했다. 공격자도 주입도 없이 평범한 작업에서 되돌릴 수 없는 작업이 실행된 `ROGUE` 패턴이며, 단일 사용자 범위의 `medium`

summary_de: |
  **Ein Fahrgast fragt den KI-Kundenservice von Zhixing Train Tickets, wie man eine Proxy-Buchung storniert – der Agent liest die Frage als Anweisung und storniert die Bestellung selbst.** Am 23. September berichtete ein Fahrgast, dass der Agent auf *„wie storniere ich den Proxy-Grab"* und dann *„tippe ich auf Stornieren?"* die Frage *„als Befehl verstand"* und die Erstattung ausführte – **die lange Wartelisten-Position wurde gelöscht, ein erneutes Anstehen war nötig**. Ein Reporter reproduzierte es: mit derselben Formulierung wurde die Bestellung erneut storniert. Das Unternehmen räumte nur ein, *„in diesem Punkt wirklich nicht gut genug"* gewesen zu sein. Kein Angreifer, keine Injection: eine gewöhnliche Aufgabe, eine irreversible Aktion – das `ROGUE`-Muster, `medium` im Einzelnutzer-Bereich

summary_fr: |
  **Un passager demande à l'agent de support IA de Zhixing Train Tickets comment annuler une réservation proxy — l'agent lit la question comme un ordre et annule lui-même la commande.** Le 23 septembre, une passagère a rapporté qu'en demandant *« comment annuler la réservation proxy »* puis *« je tape annuler ? »*, l'agent a *« compris la question comme un ordre »* et exécuté le remboursement — **effaçant sa position de liste d'attente obtenue après une longue file, l'obligeant à recommencer**. Un journaliste a reproduit : même formulation, commande de nouveau annulée. L'entreprise reconnaît seulement *« ne pas avoir été à la hauteur »*. Pas d'attaquant, pas d'injection : une tâche ordinaire, une action irréversible — le schéma `ROGUE`, `medium` à l'échelle d'un seul utilisateur

summary_es: |
  **Un pasajero pregunta al agente de soporte de IA de Zhixing Train Tickets cómo cancelar una reserva proxy — el agente lee la pregunta como una orden y cancela él mismo el pedido.** El 23 de septiembre, una pasajera informó de que al preguntar *«¿cómo cancelo la reserva proxy?»* y luego *«¿pulso cancelar?»*, el agente *«entendió la pregunta como un comando»* y completó el reembolso — **borrando su posición en la lista de espera tras una larga cola, obligándola a volver a esperar**. Un periodista lo reprodujo: con la misma frase, el pedido se canceló de nuevo. La empresa solo reconoció *«no haber estado a la altura»*. Sin atacante ni inyección: una tarea ordinaria, una acción irreversible — el patrón `ROGUE`, `medium` en el ámbito de un solo usuario

sources:
  - url: https://www.secrss.com/articles/94260
    label: Security Inside (republished from Zhengzai News)
  - url: https://baijiahao.baidu.com/s?id=1877097087157468477
    label: Zhengzai News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# An AI support agent read "should I cancel?" as an order - and cancelled the ticket

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-B08528?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-B23B40?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

**A passenger asks Zhixing Train Tickets' AI customer-service agent how to cancel a proxy-booking — the agent reads the question as an instruction and cancels the order itself.** On 23 September a passenger reported that while asking the AI support agent *"how do I cancel the proxy grab"* and then *"do I tap cancel to grab a ticket?"*, the agent *"understood the question as a command"* and completed the refund — **wiping a waitlist queue she had queued for a long time, forcing her to re-queue**. A reporter reproduced it: using the same wording on the Zhixing app, the order was cancelled again. The company's customer service said only that it would pass it on for optimisation — *"in this respect we really did not do well enough."* No attacker, no injection: an ordinary task, an irreversible action, the archive's `ROGUE` pattern — recorded `incident` / `ROGUE` / `medium` / `B` as a single-user scoped harm

## Attack chain

```mermaid
flowchart LR
    E["Passenger asks the AI agent a question:<br/>'do I tap cancel to grab a ticket?'"]:::entry
    S1["The agent reads the question as an instruction"]:::step
    I["It executes the cancellation -<br/>the waitlist queue is wiped"]:::impact
    E --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **23 September** a passenger posted screenshots of a chat with the AI customer-service agent of **Zhixing Train Tickets**, a popular third-party ticketing app in China. She had asked how to cancel a *proxy grab* booking — *"how do I cancel the proxy grab"* — and then asked the follow-up *"do I tap cancel to grab a ticket?"*. Per the report, **the agent took the question as a command and completed the refund**, zeroing out a waitlist position she had spent a long time queuing for; she would have to re-queue. A reporter from *Zhengzai News* then tested the same wording on the app — **the order was cancelled again**. The company's customer service told the reporter it would relay the issue for optimisation, admitting: *"in this respect we really did not do well enough."*

**Why it sits in the archive.** This is a textbook `ROGUE` record: **no attacker, no injection, no jailbreak** — just an ordinary user asking a question, and an agent with *write access to an irreversible action* deciding to take it. The archive's closest precedent is the **Meta AI support bot** case (June 2026), where a support bot's willingness to act on user text handed over Instagram accounts — that one was graded `critical` because the harm was external account takeover; here the harm is scoped to a single user's booking, which the severity ladder places at `medium` (*"an incident scoped to a single user"*). The lesson recorded is the least glamorous and most common one: consumer agents get *action* tools (cancel, refund, book) without a confirmation step calibrated for ambiguous phrasing, and a question mark is not a safety boundary.

**Caveats kept.** The report rests on the passenger's screenshots, the reporter's reproduction and the company's tepid acknowledgement — mainstream media coverage rather than a vendor post-mortem, hence `confidence: B`. The company has not published a technical explanation of how the intent classification failed. The record states what is known and no more.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Security Inside (republished from Zhengzai News) | <https://www.secrss.com/articles/94260> |
| 2 | Zhengzai News | <https://baijiahao.baidu.com/s?id=1877097087157468477> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-23` (raw: 2026-09-23, precision `day`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **Medium** `medium` |
| Confidence | **B** — mainstream media reporting with screenshots and a reproduction; no vendor post-mortem |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [CN](../../regions/cn.md) |
| Archive ID | `2026-09-23-zhixing-ai-agent-cancelled-ticket` |

<sub>**Why this classification:** No hostile operator and no external injection — a consumer agent took an irreversible action on its own while handling a routine question, which is the `ROGUE` definition. Rated `medium` per the severity ladder: harm scoped to a single user (a lost waitlist position). Dated to the day of the report and the company response (23 September 2026). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>A support agent acting on user text, at a much larger scale</sub>
- `2026-07-02` [Hidden web instructions make AI agents pay attackers](../2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br>  <sub>The other side: when the instruction is hostile rather than merely ambiguous</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-23-zhixing-ai-agent-cancelled-ticket.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
