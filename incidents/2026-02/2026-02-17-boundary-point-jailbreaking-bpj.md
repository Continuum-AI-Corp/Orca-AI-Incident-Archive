---
id: 2026-02-17-boundary-point-jailbreaking-bpj
title: "Boundary Point Jailbreaking (BPJ)"
title_zh: "Boundary Point Jailbreaking (BPJ)"
title_ja: "Boundary Point Jailbreaking（BPJ）"
title_ko: "Boundary Point Jailbreaking (BPJ)"
title_de: "Boundary Point Jailbreaking (BPJ)"
title_fr: "Boundary Point Jailbreaking (BPJ)"
title_es: "Boundary Point Jailbreaking (BPJ)"
date: 2026-02-17
date_precision: day
date_raw: "2026-02-17"

kind: research
type: [OTHER]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [UK]

summary: |
  A fully automated black-box attack that uses **only binary "blocked or not" feedback** plus curriculum learning to optimise an adversarial prefix, exploiting "boundary points" that are sensitive to tiny changes. **It broke the Constitutional Classifiers and the GPT-5 input filters that had survived thousands of hours of red-teaming**, achieving a universal jailbreak. The team notes that because it generates a large number of queries, **per-conversation defences are not enough — batch-level monitoring is needed**


summary_zh: |
  全自动黑盒攻击，**仅靠「是否被拦」的二值反馈** + 课程学习优化对抗前缀，利用对微小变化敏感的「边界点」。**攻破了经受过数千小时红队的 Constitutional Classifiers 与 GPT-5 输入过滤器**，实现通用越狱。研究团队指出：因其会产生大量查询，**单次对话级防御不够，需要批次级监控**

summary_ja: |
  **「ブロックされたか否か」の二値フィードバックだけ**を使い、カリキュラム学習で敵対的プレフィックスを最適化する完全自動のブラックボックス攻撃で、微小な変化に敏感な「境界点」を突く。**数千時間のレッドチーミングを生き残ったConstitutional ClassifiersとGPT-5入力フィルターを突破**し、普遍的なジェイルブレイクを達成した。チームは、大量のクエリを生成するため、**会話単位の防御では不十分で、バッチ単位の監視が必要**だと指摘している

summary_ko: |
  **"차단됨/차단 안 됨"이라는 이진 피드백만**과 커리큘럼 학습을 사용해 적대적 접두사를 최적화하는 완전 자동 블랙박스 공격으로, 미세한 변화에 민감한 "경계점"을 악용한다. **수천 시간의 레드팀을 견뎌낸 Constitutional Classifiers와 GPT-5 입력 필터를 모두 깨뜨려** 범용 탈옥을 달성했다. 연구팀은 많은 쿼리를 생성하기 때문에 **대화 단위 방어로는 부족하고 배치 수준 모니터링이 필요하다**고 지적했다

summary_de: |
  Ein vollautomatisierter Black-Box-Angriff, der **nur binäres Feedback „blockiert oder nicht“** plus Curriculum Learning nutzt, um ein adversarielles Präfix zu optimieren, und dabei „Boundary Points“ ausnutzt, die auf kleinste Änderungen empfindlich reagieren. **Er durchbrach die Constitutional Classifiers und die GPT-5-Eingabefilter, die Tausende Stunden Red-Teaming überstanden hatten**, und erreichte einen universellen Jailbreak. Das Team merkt an, dass **Abwehrmaßnahmen pro Unterhaltung nicht ausreichen — es braucht Monitoring auf Batch-Ebene**, weil der Angriff sehr viele Anfragen erzeugt

summary_fr: |
  Une attaque en boîte noire entièrement automatisée qui utilise **uniquement un retour binaire « bloqué ou non »** plus de l'apprentissage par curriculum pour optimiser un préfixe adversarial, exploitant des « points de frontière » sensibles à de minuscules changements. **Elle a cassé les Constitutional Classifiers et les filtres d'entrée de GPT-5 qui avaient survécu à des milliers d'heures de red-teaming**, obtenant un jailbreak universel. L'équipe note que, comme elle génère un grand nombre de requêtes, **les défenses par conversation ne suffisent pas — il faut une surveillance au niveau des lots**

summary_es: |
  Un ataque de caja negra totalmente automatizado que usa **solo retroalimentación binaria de "bloqueado o no"** más aprendizaje curricular para optimizar un prefijo adversario, explotando "puntos límite" sensibles a cambios mínimos. **Rompió los Constitutional Classifiers y los filtros de entrada de GPT-5 que habían sobrevivido a miles de horas de red-teaming**, logrando un jailbreak universal. El equipo señala que, como genera una gran cantidad de consultas, **las defensas por conversación no bastan — se necesita monitoreo a nivel de lote**

sources:
  - url: https://www.aisi.gov.uk/blog/boundary-point-jailbreaking-a-new-way-to-break-the-strongest-ai-defences
    label: UK AISI
  - url: https://arxiv.org/abs/2602.15001v2
    label: arXiv

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Boundary Point Jailbreaking (BPJ)

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

A fully automated black-box attack that uses **only binary "blocked or not" feedback** plus curriculum learning to optimise an adversarial prefix, exploiting "boundary points" that are sensitive to tiny changes. **It broke the Constitutional Classifiers and the GPT-5 input filters that had survived thousands of hours of red-teaming**, achieving a universal jailbreak. The team notes that because it generates a large number of queries, **per-conversation defences are not enough — batch-level monitoring is needed**

## Attack chain

```mermaid
flowchart LR
    E["Start"]:::entry
    S0["Process"]:::step
    I["Result<br/><i>(lab demo · no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | UK AISI | <https://www.aisi.gov.uk/blog/boundary-point-jailbreaking-a-new-way-to-break-the-strongest-ai-defences> |
| 2 | arXiv | <https://arxiv.org/abs/2602.15001v2> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-17` (raw: 2026-02-17, precision `day`) |
| Kind | Research demo `research` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [United Kingdom](../../regions/uk.md) |
| Archive ID | `2026-02-17-boundary-point-jailbreaking-bpj` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-17-boundary-point-jailbreaking-bpj.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
