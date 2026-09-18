---
id: 2026-04-14-vidoc-mythos-yong-gong-kai
title: "Vidoc reproduces Mythos's findings with public models"
title_zh: "Vidoc：用公开模型复现了 Mythos 的发现"
title_ja: "Vidocが公開モデルでMythosの発見を再現"
title_ko: "Vidoc, 공개 모델로 Mythos의 발견을 재현"
title_de: "Vidoc reproduziert die Funde von Mythos mit öffentlichen Modellen"
title_fr: "Vidoc reproduit les trouvailles de Mythos avec des modèles publics"
title_es: "Vidoc reproduce los hallazgos de Mythos con modelos públicos"
date: 2026-04-14
date_precision: day
date_raw: "2026-04-14"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  A small open-source model plus expert-designed scaffolding was enough to reproduce the FreeBSD NFS exploit and a SACK bug in OpenBSD from 27 years ago. **This shows the capability boundary is "jagged", not something only frontier models hold**


summary_zh: |
  小型开源模型 + 专家设计的脚手架即可复现 FreeBSD NFS 利用、OpenBSD 27 年前的 SACK bug。**说明能力边界是「锯齿状(jagged)」的，不是前沿模型独占**

summary_ja: |
  小さなオープンソースモデルと専門家が設計した足場（scaffolding）だけで、FreeBSDのNFSエクスプロイトとOpenBSDの27年前のSACKバグを再現できた。**これは能力の境界が「ぎざぎざ」であり、フロンティアモデルだけが持つものではないことを示している**

summary_ko: |
  소형 오픈소스 모델과 전문가가 설계한 스캐폴딩만으로 FreeBSD NFS 익스플로잇과 27년 된 OpenBSD의 SACK 버그를 재현할 수 있었다. **이는 능력 경계가 "들쭉날쭉"하며 프런티어 모델만의 것이 아님을 보여준다**

summary_de: |
  Ein kleines Open-Source-Modell plus von Experten entworfenes Scaffolding genügte, um den FreeBSD-NFS-Exploit und einen 27 Jahre alten SACK-Bug in OpenBSD zu reproduzieren. **Dies zeigt, dass die Fähigkeitsgrenze „zerklüftet“ ist und nicht nur Frontier-Modelle betrifft**

summary_fr: |
  Un petit modèle open source plus un échafaudage conçu par des experts ont suffi à reproduire l'exploit NFS de FreeBSD et un bug SACK d'OpenBSD vieux de 27 ans. **Cela montre que la frontière des capacités est « en dents de scie », et non l'apanage des modèles de frontière**

summary_es: |
  Un pequeño modelo de código abierto más un andamiaje diseñado por expertos bastó para reproducir el exploit de NFS de FreeBSD y un fallo de SACK en OpenBSD de hace 27 años. **Esto muestra que la frontera de capacidad es "irregular", no algo que solo posean los modelos de frontera**

sources:
  - url: https://blog.vidocsecurity.com/blog/we-reproduced-anthropics-mythos-findings-with-public-models
    label: Vidoc
  - url: https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier
    label: AISLE

disputed: false
landmark: false
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Vidoc reproduces Mythos's findings with public models

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

A small open-source model plus expert-designed scaffolding was enough to reproduce the FreeBSD NFS exploit and a SACK bug in OpenBSD from 27 years ago. **This shows the capability boundary is "jagged", not something only frontier models hold**

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
| 1 | Vidoc | <https://blog.vidocsecurity.com/blog/we-reproduced-anthropics-mythos-findings-with-public-models> |
| 2 | AISLE | <https://aisle.com/blog/ai-cybersecurity-after-mythos-the-jagged-frontier> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-14` (raw: 2026-04-14, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-14-vidoc-mythos-yong-gong-kai` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-04-07` [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](2026-04-07-claude-mythos-preview-project.md)<br>  <sub>Claude Mythos Preview cyber capability disclosure, Project Glasswing formed</sub>
- `2026-04-13` [UK AISI independently evaluates Claude Mythos Preview](2026-04-13-uk-aisi-claude-mythos.md)<br>  <sub>UK AISI independently evaluates Claude Mythos Preview</sub>
- `2026-04-30` [OpenAI launches Advanced Account Security](2026-04-30-tui-chu-gao-ji-zhang.md)<br>  <sub>OpenAI launches Advanced Account Security</sub>
- `2026-05-12` [Brazilian labour court sanctions lawyers over prompt injection](../2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md)<br>  <sub>Brazilian labour court sanctions lawyers over prompt injection</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-14-vidoc-mythos-yong-gong-kai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
