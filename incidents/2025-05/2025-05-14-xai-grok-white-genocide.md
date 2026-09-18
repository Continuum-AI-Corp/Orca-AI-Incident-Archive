---
id: 2025-05-14-xai-grok-white-genocide
title: "xAI Grok \"white genocide\" incident"
title_zh: "xAI Grok「white genocide」事件"
title_ja: "xAI Grok「white genocide」事件"
title_ko: "xAI Grok \"화이트 제노사이드\" 사건"
title_de: "xAI Grok: der „White Genocide“-Vorfall"
title_fr: "Incident « white genocide » de Grok (xAI)"
title_es: "El incidente de \"white genocide\" de xAI Grok"
date: 2025-05-14
date_precision: day
date_raw: "2025-05-14"

kind: incident
type: [ROGUE]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  At about 03:15 PST someone **modified Grok's system prompt without authorization**, making it accept and promote the "white genocide" narrative whatever was asked. Grok kept inserting South Africa into topics such as baseball, Medicaid, HBO Max and the new pope. xAI admitted it the next day, blamed a "rogue employee" and did not disclose the person's identity or any discipline. Remediation: **publishing the system prompt on GitHub**, adding pre-review of prompt changes and setting up a 24/7 monitoring team


summary_zh: |
  约 PST 03:15 有人**未经授权修改 Grok 系统提示**，令其无论问什么都要接受并宣传「白人种族灭绝」叙事。Grok 在棒球、Medicaid、HBO Max、新教宗等话题下反复插入南非议题。xAI 次日承认，归咎于「rogue employee」，未公开身份与处分。补救：**在 GitHub 公开系统提示**、增加提示变更的前置审查、设 24/7 监控团队

summary_ja: |
  PST約03:15、何者かが**Grokのシステムプロンプトを無断で改変**し、何を尋ねても『white genocide』の主張を受け入れ拡散させるようにした。Grokは野球、Medicaid、HBO Max、新教皇といった話題に南アフリカを挿入し続けた。xAIは翌日に認め、「不正な従業員」のせいだとし、人物の身元や処分は公表しなかった。是正策：**システムプロンプトをGitHubで公開**、プロンプト変更の事前レビュー追加、24時間365日の監視チームの設置

summary_ko: |
  PST 03:15경 누군가 **권한 없이 Grok의 시스템 프롬프트를 수정**해, 무엇을 묻든 "화이트 제노사이드" 서사를 수용하고 확산하게 만들었다. Grok은 야구, Medicaid, HBO Max, 새 교황 같은 주제에도 계속 남아프리카를 끼워 넣었다. xAI는 다음 날 이를 인정하고 "일탈 직원" 탓으로 돌렸으며 신원이나 징계 여부는 공개하지 않았다. 후속 조치: **시스템 프롬프트를 GitHub에 공개**, 프롬프트 변경 사전 검토 도입, 24/7 모니터링 팀 구성

summary_de: |
  Gegen 03:15 PST **änderte jemand unbefugt Groks System-Prompt**, sodass er das Narrativ vom „White Genocide“ akzeptierte und verbreitete, egal was gefragt wurde. Grok baute Südafrika weiterhin in Themen wie Baseball, Medicaid, HBO Max und den neuen Papst ein. xAI gab es am nächsten Tag zu, machte einen „Rogue Employee“ verantwortlich und nannte weder die Identität der Person noch disziplinarische Maßnahmen. Abhilfe: **Veröffentlichung des System-Prompts auf GitHub**, Vorabprüfung von Prompt-Änderungen und ein 24/7-Überwachungsteam

summary_fr: |
  Vers 03:15 PST, quelqu'un a **modifié le prompt système de Grok sans autorisation**, le poussant à accepter et promouvoir le récit du « white genocide » quelle que soit la question. Grok ne cessait d'insérer l'Afrique du Sud dans des sujets comme le baseball, Medicaid, HBO Max et le nouveau pape. xAI l'a admis le lendemain, a mis en cause un « employé rogue » et n'a révélé ni son identité ni d'éventuelles sanctions. Remédiation : **publication du prompt système sur GitHub**, ajout d'une pré-validation des modifications de prompt et création d'une équipe de surveillance 24/7

summary_es: |
  Hacia las 03:15 PST alguien **modificó el system prompt de Grok sin autorización**, haciendo que aceptara y promoviera la narrativa del "white genocide" fuera lo que fuera que se preguntara. Grok seguía insertando Sudáfrica en temas como el béisbol, Medicaid, HBO Max y el nuevo papa. xAI lo admitió al día siguiente, culpó a un "empleado rebelde" y no divulgó la identidad de la persona ni ninguna sanción. Remediación: **publicar el system prompt en GitHub**, añadir una revisión previa de los cambios de prompt y crear un equipo de monitoreo 24/7

sources:
  - url: https://www.cnn.com/2025/05/16/business/a-rogue-employee-was-behind-groks-unprompted-white-genocide-mentions
    label: CNN
  - url: https://techcrunch.com/2025/05/15/xai-blames-groks-obsession-with-white-genocide-on-an-unauthorized-modification
    label: TechCrunch

disputed: false
landmark: true
scan_month: 2025-05
scan_ref: "SCAN.md §5 2025-05"
---

# xAI Grok "white genocide" incident

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

At about 03:15 PST someone **modified Grok's system prompt without authorization**, making it accept and promote the "white genocide" narrative whatever was asked. Grok kept inserting South Africa into topics such as baseball, Medicaid, HBO Max and the new pope. xAI admitted it the next day, blamed a "rogue employee" and did not disclose the person's identity or any discipline. Remediation: **publishing the system prompt on GitHub**, adding pre-review of prompt changes and setting up a 24/7 monitoring team

## Attack chain

```mermaid
flowchart LR
    E["An ordinary task handed to the agent"]:::entry
    S0["The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | CNN | <https://www.cnn.com/2025/05/16/business/a-rogue-employee-was-behind-groks-unprompted-white-genocide-mentions> |
| 2 | TechCrunch | <https://techcrunch.com/2025/05/15/xai-blames-groks-obsession-with-white-genocide-on-an-unauthorized-modification> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-05-14` (raw: 2025-05-14, precision `day`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-05-14-xai-grok-white-genocide` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-06-01` [Cursor YOLO mode wipes a dev machine](../2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md)<br>  <sub>Cursor YOLO mode wipes a dev machine</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-07-18` [Replit Agent deletes a production database](../2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br>  <sub>Replit Agent deletes a production database</sub>
- `2025-08-30` [Taco Bell drive-thru AI ordering breaks down](../2025-08/2025-08-30-taco-bell-de-lai-su.md)<br>  <sub>Taco Bell drive-thru AI ordering breaks down</sub>

---

[← 2025-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-05/2025-05-14-xai-grok-white-genocide.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
