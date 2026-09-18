---
id: 2026-03-02-amazon-yin-sheng-cheng-dai
title: "Amazon hit by back-to-back outages from AI-generated code"
title_zh: "⚠️ Amazon 因 AI 生成代码连续宕机"
title_ja: "Amazon、AI生成コードによる連続障害に見舞われる"
title_ko: "아마존, AI 생성 코드로 연속 장애"
title_de: "Amazon von aufeinanderfolgenden Ausfällen durch KI-generierten Code getroffen"
title_fr: "Amazon frappé par des pannes en série dues à du code généré par IA"
title_es: "Amazon sufre caídas consecutivas por código generado por IA"
date: 2026-03-02
date_precision: day
date_raw: "2026-03-02 / 03-05"

kind: incident
type: [ROGUE]
severity: high
confidence: B
real_harm: true
ai_involvement: disputed

region: [US]

summary: |
  On 03-02 Amazon Q gave wrong advice based on an **outdated internal wiki** → 120,000 orders lost and 1.6 million website errors; on 03-05 North America order volume collapsed 99%, with **6.3 million orders lost**. Amazon already requires engineers to spend 80% of every week using its internal AI coding assistant Kiro. Response: a 90-day "code security reset" for about **335 Tier-1 systems**, with AI-assisted code changes now needing two-person review plus formal documented approval. **Business Insider obtained internal documents**


summary_zh: |
  03-02 Amazon Q 依据**已过期的内部 wiki** 给出错误建议 → 12 万订单丢失、160 万次网站错误；03-05 北美站订单量暴跌 99%，**630 万订单丢失**。Amazon 已强制工程师每周 80% 使用内部 AI 编码助手 Kiro。回应：对约 **335 个 Tier-1 系统**启动 90 天「代码安全重置」，AI 辅助的代码变更须两人评审 + 正式文档审批。**Business Insider 取得内部文件**

summary_ja: |
  03-02にAmazon Qが**古い社内wiki**に基づく誤った助言をし、12万件の注文が失われ160万件のサイトエラーが発生。03-05には北米の注文量が99%崩壊し、**630万件の注文が失われた**。Amazonはすでにエンジニアに対し毎週80%の時間を社内AIコーディングアシスタントKiroの使用に充てることを求めている。対応：約**335のTier-1システム**に対する90日間の「コードセキュリティ・リセット」で、AI支援によるコード変更には2名レビューと正式な文書化された承認が必要になった。**Business Insiderが内部文書を入手**

summary_ko: |
  03-02 Amazon Q가 **오래된 내부 위키**를 근거로 잘못된 조언을 해 주문 12만 건이 유실되고 웹사이트 오류 160만 건이 발생했다. 03-05에는 북미 주문량이 99% 폭락해 **주문 630만 건이 유실**되었다. 아마존은 이미 엔지니어에게 매주 업무 시간의 80%를 내부 AI 코딩 어시스턴트 Kiro와 함께 쓰도록 요구하고 있었다. 대응: 약 **335개 Tier-1 시스템**에 대한 90일 "코드 보안 재정비"를 실시하고, AI 지원 코드 변경에는 2인 검토와 공식 문서화된 승인을 요구했다. **Business Insider가 내부 문서를 입수했다**

summary_de: |
  Am 03-02 gab Amazon Q auf Basis eines **veralteten internen Wikis** falsche Empfehlungen → 120,000 verlorene Bestellungen und 1.6 Millionen Website-Fehler; am 03-05 brach das Bestellvolumen in Nordamerika um 99% ein, mit **6.3 Millionen verlorenen Bestellungen**. Amazon verlangt von seinen Entwicklern bereits, 80% jeder Woche mit dem internen KI-Coding-Assistenten Kiro zu arbeiten. Reaktion: ein 90-tägiger „Code Security Reset“ für etwa **335 Tier-1-Systeme**, wobei KI-gestützte Codeänderungen nun Zwei-Augen-Prinzip plus förmliche dokumentierte Genehmigung erfordern. **Business Insider liegen interne Dokumente vor**

summary_fr: |
  Le 03-02, Amazon Q a donné de mauvais conseils fondés sur un **wiki interne obsolète** → 120 000 commandes perdues et 1,6 million d'erreurs de site web ; le 03-05, le volume de commandes en Amérique du Nord s'est effondré de 99 %, avec **6,3 millions de commandes perdues**. Amazon exige déjà de ses ingénieurs qu'ils passent 80 % de chaque semaine à utiliser son assistant de code IA interne Kiro. Réponse : une « remise à zéro de la sécurité du code » de 90 jours pour environ **335 systèmes de niveau 1**, les modifications de code assistées par IA devant désormais passer par une revue à deux personnes plus une approbation formelle documentée. **Business Insider a obtenu des documents internes**

summary_es: |
  El 03-02 Amazon Q dio consejos incorrectos basados en una **wiki interna desactualizada** → 120,000 pedidos perdidos y 1.6 millones de errores en el sitio web; el 03-05 el volumen de pedidos de Norteamérica se desplomó un 99%, con **6.3 millones de pedidos perdidos**. Amazon ya exige a los ingenieros dedicar el 80% de cada semana a usar su asistente interno de código con IA, Kiro. Respuesta: un "reinicio de seguridad del código" de 90 días para unos **335 sistemas de Nivel 1**, y los cambios de código asistidos por IA ahora requieren revisión de dos personas más aprobación formal documentada. **Business Insider obtuvo documentos internos**

sources:
  - url: https://www.digitaltrends.com/computing/ai-code-wreaked-havoc-with-amazon-outage-and-now-the-company-is-making-tight-rules/
    label: Digital Trends
  - url: https://securityboulevard.com/2026/03/amazon-lost-6-3-million-orders-to-vibe-coding-your-soc-is-next/
    label: Security Boulevard

disputed: true
landmark: false
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Amazon hit by back-to-back outages from AI-generated code

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: disputed](https://img.shields.io/badge/AI_involvement-disputed-D1394B?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

> [!WARNING]
> **This record contains disputed or not fully verified facts**; the accounts of the parties are kept side by side in the body — do not quote one side alone.
> **AI involvement is disputed in attribution**; the vendor and the reporting outlets disagree — see "Metadata".

## Summary

On 03-02 Amazon Q gave wrong advice based on an **outdated internal wiki** → 120,000 orders lost and 1.6 million website errors; on 03-05 North America order volume collapsed 99%, with **6.3 million orders lost**. Amazon already requires engineers to spend 80% of every week using its internal AI coding assistant Kiro. Response: a 90-day "code security reset" for about **335 Tier-1 systems**, with AI-assisted code changes now needing two-person review plus formal documented approval. **Business Insider obtained internal documents**

## Attack chain

```mermaid
flowchart LR
    E["An ordinary task handed to the agent"]:::entry
    S0["<i>(AI involvement in the steps below is disputed in attribution)</i><br/>The agent misreads the situation and escalates on its own"]:::step
    I["A destructive command is executed"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Digital Trends | <https://www.digitaltrends.com/computing/ai-code-wreaked-havoc-with-amazon-outage-and-now-the-company-is-making-tight-rules/> |
| 2 | Security Boulevard | <https://securityboulevard.com/2026/03/amazon-lost-6-3-million-orders-to-vibe-coding-your-soc-is-next/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-02` (raw: 2026-03-02 / 03-05, precision `day`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **High** `high` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Disputed `disputed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-03-02-amazon-yin-sheng-cheng-dai` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2026-03-18` [Meta internal AI agent data exposure](2026-03-18-meta-agent-nei-bu-shu.md)<br>  <sub>Meta internal AI agent data exposure</sub>
- `2026-02-26` [Claude Code runs terraform destroy on all of DataTalks.Club's production](../2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br>  <sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub>
- `2026-04-25` [Cursor and Claude Opus 4.6 wipe production and backups in nine seconds](../2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br>  <sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub>
- `2026-02-18` [Microsoft 365 Copilot summarises confidential mail it shouldn't see](../2026-02/2026-02-18-microsoft-copilot-yue-quan-zong.md)<br>  <sub>Microsoft 365 Copilot summarises confidential mail it shouldn't see</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-02-amazon-yin-sheng-cheng-dai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
