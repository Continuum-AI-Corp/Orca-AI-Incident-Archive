---
id: 2026-09-04-ying-zi-zhi-ren-jian
title: "Japan: shadow AI exposes health data on 726 people"
title_zh: "日本：影子 AI 致 726 人健康信息泄露"
title_ja: "日本：シャドーAIが726人分の健康データを露出"
title_ko: "일본: 섀도 AI로 726명의 건강 데이터 유출"
title_de: "Japan: Schatten-KI legt Gesundheitsdaten von 726 Personen offen"
title_fr: "Japon : du shadow AI expose les données de santé de 726 personnes"
title_es: "Japón: la IA en la sombra expone datos de salud de 726 personas"
date: 2026-09-04
date_precision: day
date_raw: "2026-09-04"

kind: incident
type: [OTHER]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [JP]

summary: |
  Employees fed business data into an **unapproved** generative AI service. It involved **726 people** at a local civil-servant credit union: names, dates of birth and **health conditions (hypertension, diabetes, dyslipidaemia)**. The incident occurred **2026-08-20** and was disclosed 09-04


summary_zh: |
  员工把业务数据输入**未经批准的**生成式 AI 服务。涉及地方公务员信用合作社的 **726 人**：姓名、出生日期、**健康状况（高血压、糖尿病、血脂异常）**。事故发生 **2026-08-20**，09-04 披露

summary_ja: |
  従業員が業務データを**未承認**の生成AIサービスに入力した。地方公務員信用組合の**726人分**が該当し、氏名、生年月日、**健康状態（高血圧、糖尿病、脂質異常症）**が含まれた。インシデントは**2026-08-20**に発生し、09-04に公表された

summary_ko: |
  직원들이 업무 데이터를 **승인되지 않은** 생성 AI 서비스에 입력했다. 지역 공무원 신용조합의 **726명**이 관련되었고, 이름, 생년월일, **건강 상태(고혈압, 당뇨병, 이상지질혈증)**가 포함되었다. 사고는 **2026-08-20**에 발생해 09-04에 공개되었다

summary_de: |
  Beschäftigte speisten Geschäftsdaten in einen **nicht genehmigten** generativen KI-Dienst ein. Betroffen waren **726 Personen** bei einer lokalen Genossenschaftsbank für Beamte: Namen, Geburtsdaten und **Gesundheitszustände (Hypertonie, Diabetes, Dyslipidämie)**. Der Vorfall ereignete sich am **2026-08-20** und wurde am 09-04 offengelegt

summary_fr: |
  Des employés ont versé des données professionnelles dans un service d'IA générative **non approuvé**. Cela a concerné **726 personnes** d'une mutuelle de fonctionnaires locale : noms, dates de naissance et **conditions de santé (hypertension, diabète, dyslipidémie)**. L'incident a eu lieu le **2026-08-20** et a été divulgué le 09-04

summary_es: |
  Los empleados introdujeron datos empresariales en un servicio de IA generativa **no aprobado**. Afectó a **726 personas** de una cooperativa de crédito de funcionarios locales: nombres, fechas de nacimiento y **condiciones de salud (hipertensión, diabetes, dislipidemia)**. El incidente ocurrió el **2026-08-20** y se divulgó el 09-04

sources:
  - url: https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/
    label: RIZAP advisory / Security NEXT (relayed)

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Japan: shadow AI exposes health data on 726 people

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: OTHER](https://img.shields.io/badge/type-OTHER-B08528?style=flat-square)

## Summary

Employees fed business data into an **unapproved** generative AI service. It involved **726 people** at a local civil-servant credit union: names, dates of birth and **health conditions (hypertension, diabetes, dyslipidaemia)**. The incident occurred **2026-08-20** and was disclosed 09-04

## Attack chain

```mermaid
flowchart LR
    E["Entry point"]:::entry
    S0["Process"]:::step
    I["Result"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | RIZAP advisory / Security NEXT (relayed) | <https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-04` (raw: 2026-09-04, precision `day`) |
| Kind | Incident `incident` |
| Type | [`OTHER`](../../taxonomy/types.md#other) Other |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Japan](../../regions/jp.md) |
| Archive ID | `2026-09-04-ying-zi-zhi-ren-jian` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-04-ying-zi-zhi-ren-jian.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
