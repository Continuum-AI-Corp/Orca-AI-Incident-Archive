---
id: 2026-06-15-unc6508-redcap-jing-ru-qin
title: "UNC6508 breaches North American research institutions via REDCap"
title_zh: "UNC6508 经 REDCap 入侵北美研究机构"
title_ja: "UNC6508がREDCap経由で北米の研究機関を侵害"
title_ko: "UNC6508, REDCap을 통해 북미 연구기관 침해"
title_de: "UNC6508 dringt über REDCap in nordamerikanische Forschungseinrichtungen ein"
title_fr: "UNC6508 compromet des institutions de recherche nord-américaines via REDCap"
title_es: "UNC6508 vulnera instituciones de investigación norteamericanas a través de REDCap"
date: 2026-06-15
date_precision: day
date_raw: "2026-06-15"

kind: incident
type: [WEAPON]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [US]

summary: |
  GTIG attributes this with high confidence to a China-linked actor. Targets included national, state and civilian medical institutions, academic centers and military medical facilities; the actor collected defense information, Indo-Pacific military operations, AI, drone systems and medical research. Earliest intrusion in 2023-09, with activity at one institution continuing into 2025-11. It planted INFINITERED, which rewrites legitimate REDCap files and re-injects itself on every upgrade, surviving for over a year. It abused the compliance rule **"Patroit"** to regex-match sent and received mail and silently BCC it to an attacker Gmail account — **GTIG calls this unprecedented among China-linked actors**


summary_zh: |
  GTIG 高置信度归因中国相关行为者。目标含国家/州/民间医疗机构、学术中心、军方医疗机构；收集国防信息、印太军作战、AI、无人机系统、医学研究。最早入侵 2023-09，某机构活动持续到 2025-11。植入 INFINITERED 改写 REDCap 正规文件、每次升级自我重注入存活 1 年+。滥用合规规则 **"Patroit"** 用正则匹配收发邮件并静默 BCC 到攻击者 Gmail —— **GTIG 称中国相关行为者中前所未见**

summary_ja: |
  GTIGはこれを中国関連のアクターに高い確度で帰属している。標的には国立・州立・民間の医療機関、学術センター、軍の医療施設が含まれ、アクターは防衛情報、インド太平洋の軍事作戦、AI、ドローンシステム、医学研究を収集していた。最古の侵入は2023-09で、ある機関での活動は2025-11まで続いた。正規のREDCapファイルを書き換え、アップグレードのたびに自身を再注入して1年以上存続するINFINITEREDを仕込んだ。コンプライアンスルール**「Patroit」**を悪用して送受信メールを正規表現でマッチさせ、攻撃者のGmailアカウントへ無言でBCC送信していた——**GTIGは中国関連アクターの中でも前例のない手法だと述べている**

summary_ko: |
  GTIG는 이를 중국 연계 행위자로 높은 확신을 가지고 귀속했다. 대상에는 국립·주립·민간 의료기관, 학술 센터, 군 의료 시설이 포함되었고, 행위자는 국방 정보, 인도태평양 군사 작전, AI, 드론 시스템, 의료 연구를 수집했다. 최초 침입은 2023-09이며 한 기관에서의 활동은 2025-11까지 이어졌다. 정상 REDCap 파일을 재작성하고 업그레이드마다 스스로를 다시 주입하는 INFINITERED를 심어 1년 넘게 생존했다. 준수 규칙 **"Patroit"**을 악용해 발신·수신 메일을 정규식으로 매칭하고 공격자의 Gmail 계정으로 조용히 BCC했다 — **GTIG는 중국 연계 행위자 가운데 이런 사례는 전례가 없다고 말한다**

summary_de: |
  GTIG schreibt dies mit hoher Konfidenz einem Akteur mit China-Bezug zu. Zu den Zielen gehörten nationale, staatliche und zivile medizinische Einrichtungen, akademische Zentren und militärmedizinische Einrichtungen; der Akteur sammelte Verteidigungsinformationen, Angaben zu Militäroperationen im Indopazifik, KI, Drohnensysteme und medizinische Forschung. Die früheste Intrusion erfolgte im 2023-09, wobei die Aktivität bei einer Einrichtung bis in den 2025-11 anhielt. Er pflanzte INFINITERED, das legitime REDCap-Dateien umschreibt und sich bei jedem Upgrade erneut injiziert, und überlebte so über ein Jahr. Er missbrauchte die Compliance-Regel **„Patroit“**, um gesendete und empfangene E-Mails per Regex abzugleichen und sie still per BCC an ein Gmail-Konto des Angreifers zu senden — **GTIG nennt dies unter Akteuren mit China-Bezug beispiellos**

summary_fr: |
  GTIG attribue cela avec un haut degré de confiance à un acteur lié à la Chine. Les cibles incluaient des institutions médicales nationales, fédérées et civiles, des centres universitaires et des établissements médicaux militaires ; l'acteur a collecté des informations de défense, des opérations militaires indo-pacifiques, des données sur l'IA, les systèmes de drones et la recherche médicale. Intrusion la plus ancienne en 2023-09, avec une activité dans une institution se poursuivant jusqu'en 2025-11. Il a planté INFINITERED, qui réécrit des fichiers REDCap légitimes et se réinjecte à chaque mise à niveau, survivant plus d'un an. Il a abusé de la règle de conformité **« Patroit »** pour faire correspondre par regex les courriers envoyés et reçus et les mettre silencieusement en CCI vers un compte Gmail d'attaquant — **GTIG qualifie cela d'inédit parmi les acteurs liés à la Chine**

summary_es: |
  GTIG lo atribuye con alta confianza a un actor vinculado a China. Los objetivos incluían instituciones médicas nacionales, estatales y civiles, centros académicos e instalaciones médicas militares; el actor recopiló información de defensa, operaciones militares del Indo-Pacífico, IA, sistemas de drones e investigación médica. La intrusión más temprana es de 2023-09, con actividad en una institución que continuó hasta 2025-11. Plantó INFINITERED, que reescribe archivos legítimos de REDCap y se reinyecta en cada actualización, sobreviviendo más de un año. Abusó de la regla de cumplimiento **"Patroit"** para hacer coincidencias por regex en el correo enviado y recibido y ponerlo silenciosamente en CCO hacia una cuenta de Gmail del atacante — **GTIG lo califica de sin precedentes entre los actores vinculados a China**

sources:
  - url: https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research
    label: Google Cloud

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# UNC6508 breaches North American research institutions via REDCap

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

GTIG attributes this with high confidence to a China-linked actor. Targets included national, state and civilian medical institutions, academic centers and military medical facilities; the actor collected defense information, Indo-Pacific military operations, AI, drone systems and medical research. Earliest intrusion in 2023-09, with activity at one institution continuing into 2025-11. It planted INFINITERED, which rewrites legitimate REDCap files and re-injects itself on every upgrade, surviving for over a year. It abused the compliance rule **"Patroit"** to regex-match sent and received mail and silently BCC it to an attacker Gmail account — **GTIG calls this unprecedented among China-linked actors**

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak script"]:::entry
    S0["LLM orchestrator drives a cluster of sub-agents"]:::step
    I["Target systems compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Google Cloud | <https://cloud.google.com/blog/topics/threat-intelligence/prc-targets-us-medical-research> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-15` (raw: 2026-06-15, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [United States](../../regions/us.md) |
| Archive ID | `2026-06-15-unc6508-redcap-jing-ru-qin` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-06-02` [CleverHans Lab adaptive AI worm PoC](2026-06-02-cleverhans-lab-poc.md)<br>  <sub>CleverHans Lab adaptive AI worm PoC</sub>
- `2026-06-24` [macOS.Gaslight: malware prompt-injects the AI analyst](2026-06-24-macos-gaslight-e-yi-ruan-jian.md)<br>  <sub>macOS.Gaslight: malware prompt-injects the AI analyst</sub>
- `2026-06-03` [Anthropic, "LLM ATT&CK Navigator"](2026-06-03-anthropic-llm-att-ck.md)<br>  <sub>Anthropic, "LLM ATT&CK Navigator"</sub>
- `2026-06-09` [Anthropic: N-day is really "N-hour"](2026-06-09-anthropic-day-hour.md)<br>  <sub>Anthropic: N-day is really "N-hour"</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-15-unc6508-redcap-jing-ru-qin.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
