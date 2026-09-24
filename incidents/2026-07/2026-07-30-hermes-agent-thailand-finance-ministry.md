---
id: 2026-07-30-hermes-agent-thailand-finance-ministry
title: "Hermes Agent attacks Thailand's Ministry of Finance unattended"
title_zh: "Hermes Agent 无人值守模式攻击泰国财政部"
title_ja: "Hermes Agentがタイ財務省を無人のまま攻撃"
title_ko: "Hermes Agent, 태국 재무부를 무인 공격"
title_de: "Hermes Agent greift unbeaufsichtigt Thailands Finanzministerium an"
title_fr: "Hermes Agent attaque sans supervision le ministère thaïlandais des Finances"
title_es: "Hermes Agent ataca el Ministerio de Finanzas de Tailandia sin supervisión"
date: 2026-07-30
date_precision: day
date_raw: "2026-07-30"

kind: incident
type: [WEAPON]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [SEA]

summary: |
  Hunt.io (with Bob Diachenko): an exposed directory on a Hong Kong host shows the operators were running Hermes Agent in **YOLO (no human approval) mode**, delegating a LinPEAS privilege-escalation assessment and enumeration of the Permanent Secretary's Office web root; plus Hadoop-targeting scripts and an unpublished Go implant, **Hades**. **No evidence that files were taken, and the initial intrusion path is undetermined**. Thailand's CERT and NCSA were notified; the Ministry of Finance itself has not commented publicly


summary_zh: |
  Hunt.io（与 Bob Diachenko 合作）：香港主机上暴露的目录显示，运营者以 **YOLO（免人工批准）模式**运行 Hermes Agent，委派 LinPEAS 提权评估与常务次长办公室 Web 根目录枚举；另有针对 Hadoop 的脚本和未公开的 Go 植入体 **Hades**。**无文件被带走的证据，初始入侵路径未查明**。已通知泰国 CERT 与 NCSA；财政部本身未公开说明

summary_ja: |
  Hunt.io（Bob Diachenko氏協力）：香港のホスト上の露出ディレクトリから、運用者がHermes Agentを**YOLO（人間の承認なし）モード**で実行していたことが判明。LinPEASによる権限昇格評価と常任官事務所のWebルートの列挙を委任し、Hadoopを標的とするスクリプトと未公開のGoインプラント**Hades**もあった。**ファイルが持ち出された証拠はなく、初期侵入経路は未確定**。タイのCERTとNCSAに通知された。財務省自体は公にコメントしていない

summary_ko: |
  Hunt.io(Bob Diachenko와 함께): 홍콩 호스트의 노출된 디렉터리에서 운영자들이 Hermes Agent를 **YOLO(사람 승인 없음) 모드**로 실행하며 LinPEAS 권한 상승 평가와 사무차관실 웹 루트 열거를 맡기고 있었음이 드러났다. 또한 Hadoop 대상 스크립트와 미공개 Go 임플란트 **Hades**도 있었다. **파일이 탈취되었다는 증거는 없고 최초 침입 경로는 밝혀지지 않았다**. 태국 CERT와 NCSA에 통보되었으나 재무부 자체는 공개적으로 언급하지 않았다

summary_de: |
  Hunt.io (mit Bob Diachenko): Ein exponiertes Verzeichnis auf einem Host in Hongkong zeigt, dass die Betreiber Hermes Agent im **YOLO-Modus (ohne menschliche Genehmigung)** laufen ließen und eine LinPEAS-Bewertung zur Rechteerweiterung sowie eine Enumeration des Web-Roots des Büros des Staatssekretärs delegierten; dazu kamen Skripte gegen Hadoop und ein unveröffentlichtes Go-Implantat, **Hades**. **Keine Hinweise darauf, dass Dateien abgegriffen wurden, und der ursprüngliche Intrusionsweg ist ungeklärt**. Thailands CERT und NCSA wurden benachrichtigt; das Finanzministerium selbst hat sich nicht öffentlich geäußert

summary_fr: |
  Hunt.io (avec Bob Diachenko) : un répertoire exposé sur un hôte de Hong Kong montre que les opérateurs faisaient tourner Hermes Agent en **mode YOLO (sans approbation humaine)**, déléguant une évaluation d'élévation de privilèges LinPEAS et l'énumération de la racine web du bureau du secrétaire permanent ; plus des scripts ciblant Hadoop et un implant Go non publié, **Hades**. **Aucune preuve que des fichiers ont été pris, et le chemin d'intrusion initial reste indéterminé**. Le CERT et la NCSA thaïlandais ont été notifiés ; le ministère des Finances lui-même n'a pas commenté publiquement

summary_es: |
  Hunt.io (junto con Bob Diachenko): un directorio expuesto en un host de Hong Kong muestra que los operadores ejecutaban Hermes Agent en **modo YOLO (sin aprobación humana)**, delegando una evaluación de escalada de privilegios con LinPEAS y la enumeración de la raíz web de la Oficina del Secretario Permanente; además, scripts dirigidos a Hadoop y un implante en Go no publicado, **Hades**. **No hay evidencia de que se tomaran archivos, y la ruta de intrusión inicial no está determinada**. Se notificó al CERT y a la NCSA de Tailandia; el propio Ministerio de Finanzas no ha comentado públicamente

sources:
  - url: https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent
    label: Hunt.io

disputed: false
landmark: false
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Hermes Agent attacks Thailand's Ministry of Finance unattended

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Hunt.io (with Bob Diachenko): an exposed directory on a Hong Kong host shows the operators were running Hermes Agent in **YOLO (no human approval) mode**, delegating a LinPEAS privilege-escalation assessment and enumeration of the Permanent Secretary's Office web root; plus Hadoop-targeting scripts and an unpublished Go implant, **Hades**. **No evidence that files were taken, and the initial intrusion path is undetermined**. Thailand's CERT and NCSA were notified; the Ministry of Finance itself has not commented publicly

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
| 1 | Hunt.io | <https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-30` (raw: 2026-07-30, precision `day`) |
| Kind | Incident `incident` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Southeast Asia](../../regions/sea.md) |
| Archive ID | `2026-07-30-hermes-agent-thailand-finance-ministry` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2026-09-22` [Gambit: three AI harnesses stole 600,000 card records from online retailers](../2026-09/2026-09-22-gambit-ai-agent-retail-card-theft.md)<br>  <sub>Same open-source Hermes framework, two months later, running the campaign</sub>
- `2026-07-01` [Taiwan's nuclear safety commission and other agencies breached by an agent swarm](2026-07-01-taiwan-government-agent-swarm.md)<br>  <sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub>
- `2026-07-01` [JADEPUFFER: first ransomware driven end-to-end by an LLM](2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br>  <sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>
- `2026-07-30` [Unit 42: autonomous campaigns run by Chinese-speaking operators](2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br>  <sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
