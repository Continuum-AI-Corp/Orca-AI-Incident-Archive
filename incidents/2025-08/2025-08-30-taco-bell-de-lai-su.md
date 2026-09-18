---
id: 2025-08-30-taco-bell-de-lai-su
title: "Taco Bell drive-thru AI ordering breaks down"
title_zh: "Taco Bell 得来速 AI 点单失控"
title_ja: "タコベルのドライブスルーAI注文が機能不全に"
title_ko: "타코벨 드라이브스루 AI 주문, 무너지다"
title_de: "Taco Bells Drive-thru-KI-Bestellsystem bricht zusammen"
title_fr: "La commande par IA au drive de Taco Bell s'enraye"
title_es: "El pedido con IA en el autoservicio de Taco Bell se descompone"
date: 2025-08-30
date_precision: day
date_raw: "2025-08-30"

kind: incident
type: [ROGUE]
severity: low
confidence: B
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  Voice AI deployed at 500+ locations since 2023. Customers deliberately pushed the AI to hand off to a human with absurd orders like "18,000 cups of water"; instead, the AI lengthened queues and staff had to watch almost every order, ready to take over. CDTO Dane Mathews told the WSJ that "not every drive-thru should be AI-only"; the company switched busy locations back to humans


summary_zh: |
  2023 年起在 500+ 家店铺部署语音 AI。顾客用「18,000 杯水」等荒谬订单**故意把 AI 逼到转人工**；AI 反而拉长排队、员工几乎每单都要盯着随时接管。CDTO Dane Mathews 对 WSJ 表示「未必所有得来速都该只用 AI」，公司改为繁忙门店转人工

summary_ja: |
  2023年以降500店舗以上に導入された音声AI。顧客が「水18,000杯」のような荒唐無稽な注文でAIを人間への引き継ぎに追い込むと、むしろAIが行列を長くし、スタッフはほぼ全注文を監視して引き継ぎに備える羽目になった。CDTOのDane Mathews氏はWSJに「すべてのドライブスルーをAIだけにすべきではない」と述べ、同社は混雑店舗を人間に戻した

summary_ko: |
  2023년부터 500개 이상 매장에 음성 AI가 배치되었다. 고객들이 "물 18,000잔" 같은 터무니없는 주문으로 AI를 일부러 사람에게 넘기게 만들었고, 오히려 AI가 대기열을 늘려 직원들이 거의 모든 주문을 지켜보며 개입할 준비를 해야 했다. CDTO Dane Mathews는 WSJ에 "모든 드라이브스루가 AI 전용이어야 하는 것은 아니다"라고 말했고, 회사는 혼잡한 매장을 다시 사람으로 전환했다

summary_de: |
  Seit 2023 ist Sprach-KI an 500+ Standorten im Einsatz. Kunden brachten die KI absichtlich mit absurden Bestellungen wie „18,000 Becher Wasser“ dazu, an einen Menschen zu übergeben; stattdessen verlängerte die KI die Schlangen, und das Personal musste fast jede Bestellung überwachen, um übernehmen zu können. CDTO Dane Mathews sagte dem WSJ, „nicht jeder Drive-thru sollte nur mit KI betrieben werden“; das Unternehmen stellte stark frequentierte Standorte wieder auf Menschen um

summary_fr: |
  IA vocale déployée dans plus de 500 établissements depuis 2023. Des clients ont délibérément poussé l'IA à passer à un humain avec des commandes absurdes comme « 18 000 gobelets d'eau » ; résultat, l'IA a allongé les files d'attente et le personnel devait surveiller presque chaque commande, prêt à reprendre la main. Le CDTO Dane Mathews a déclaré au WSJ que « tous les drive-thru ne devraient pas être 100 % IA » ; l'entreprise est revenue aux humains dans les établissements fréquentés

summary_es: |
  IA de voz desplegada en más de 500 locales desde 2023. Los clientes empujaban deliberadamente a la IA a pasar con un humano con pedidos absurdos como "18,000 vasos de agua"; en cambio, la IA alargó las colas y el personal tuvo que vigilar casi todos los pedidos, listo para intervenir. El CDTO Dane Mathews dijo al WSJ que "no todos los autoservicios deberían ser solo IA"; la empresa volvió a poner humanos en los locales concurridos

sources:
  - url: https://techcrunch.com/2025/08/30/taco-bell-is-having-second-thoughts-about-relying-on-ai-at-the-drive-through/
    label: TechCrunch

disputed: false
landmark: false
scan_month: 2025-08
scan_ref: "SCAN.md §5 2025-08"
---

# Taco Bell drive-thru AI ordering breaks down

![severity: low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: ROGUE](https://img.shields.io/badge/type-ROGUE-B08528?style=flat-square)

## Summary

Voice AI deployed at 500+ locations since 2023. Customers deliberately pushed the AI to hand off to a human with absurd orders like "18,000 cups of water"; instead, the AI lengthened queues and staff had to watch almost every order, ready to take over. CDTO Dane Mathews told the WSJ that "not every drive-thru should be AI-only"; the company switched busy locations back to humans

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
| 1 | TechCrunch | <https://techcrunch.com/2025/08/30/taco-bell-is-having-second-thoughts-about-relying-on-ai-at-the-drive-through/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-08-30` (raw: 2025-08-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`ROGUE`](../../taxonomy/types.md#rogue) Rogue agent action |
| Severity | **Low** `low` |
| Confidence | **B** — research lab or major outlet with checkable detail |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2025-08-30-taco-bell-de-lai-su` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `low`: context entry, kept for timeline continuity. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Coding agent autonomous sabotage](../../topics/rogue-agents.md)

**Related records:**

- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-07-18` [Replit Agent deletes a production database](../2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br>  <sub>Replit Agent deletes a production database</sub>
- `2025-10-01` [Claude Code recursively deletes from the filesystem root](../2025-10/2025-10-01-claude-code-gen-mu-lu.md)<br>  <sub>Claude Code recursively deletes from the filesystem root</sub>
- `2025-06-01` [Cursor YOLO mode wipes a dev machine](../2025-06/2025-06-01-cursor-yolo-mo-shi-qing.md)<br>  <sub>Cursor YOLO mode wipes a dev machine</sub>

---

[← 2025-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-08/2025-08-30-taco-bell-de-lai-su.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
