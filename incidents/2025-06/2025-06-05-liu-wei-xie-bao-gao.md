---
id: 2025-06-05-liu-wei-xie-bao-gao
title: "OpenAI June threat report"
title_zh: "OpenAI 六月威胁报告"
title_ja: "OpenAIの6月脅威レポート"
title_ko: "OpenAI 6월 위협 보고서"
title_de: "OpenAI-Bedrohungsbericht Juni"
title_fr: "Rapport de menace de juin d'OpenAI"
title_es: "Informe de amenazas de OpenAI de junio"
date: 2025-06-05
date_precision: day
date_raw: "2025-06-05"

kind: report
type: [WEAPON]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Discloses 10 operations from 6 countries, including **ScopeCreep** (a Russian-speaking actor used ChatGPT to write and debug Windows malware, even having the AI troubleshoot a Telegram alerting feature), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite, Wrong Number


summary_zh: |
  披露来自 6 个国家的 10 起行动，含 **ScopeCreep**（俄语系行为者用 ChatGPT 编写并调试 Windows 恶意软件，连 Telegram 告警功能都让 AI 排错）、Sneer Review、Uncle Spam、VAGue Focus、Helgoland Bite、Wrong Number

summary_ja: |
  6か国・10の工作活動を公表。**ScopeCreep**（ロシア語話者のアクターがChatGPTでWindowsマルウェアを作成・デバッグし、Telegram通知機能のトラブルシューティングまでAIにやらせた）、Sneer Review、Uncle Spam、VAGue Focus、Helgoland Bite、Wrong Numberなど

summary_ko: |
  6개국에서 10건의 작전을 공개했으며 **ScopeCreep**(러시아어권 행위자가 ChatGPT로 Windows 악성코드를 작성·디버깅하고 Telegram 알림 기능 문제 해결까지 AI에 맡김), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite, Wrong Number 등이 포함된다

summary_de: |
  Legt 10 Operationen aus 6 Ländern offen, darunter **ScopeCreep** (ein russischsprachiger Akteur nutzte ChatGPT zum Schreiben und Debuggen von Windows-Malware und ließ die KI sogar eine Telegram-Benachrichtigungsfunktion debuggen), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite, Wrong Number

summary_fr: |
  Divulgue 10 opérations dans 6 pays, dont **ScopeCreep** (un acteur russophone a utilisé ChatGPT pour écrire et déboguer un malware Windows, allant jusqu'à faire dépanner par l'IA une fonction d'alerte Telegram), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite et Wrong Number

summary_es: |
  Divulga 10 operaciones de 6 países, entre ellas **ScopeCreep** (un actor de habla rusa usó ChatGPT para escribir y depurar malware de Windows, incluso haciendo que la IA solucionara una función de alertas de Telegram), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite, Wrong Number

sources:
  - url: https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf
    label: OpenAI PDF

disputed: false
landmark: false
scan_month: 2025-06
scan_ref: "SCAN.md §5 2025-06"
---

# OpenAI June threat report

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: report](https://img.shields.io/badge/kind-report-48545A?style=flat-square) ![type: WEAPON](https://img.shields.io/badge/type-WEAPON-B08528?style=flat-square)

## Summary

Discloses 10 operations from 6 countries, including **ScopeCreep** (a Russian-speaking actor used ChatGPT to write and debug Windows malware, even having the AI troubleshoot a Telegram alerting feature), Sneer Review, Uncle Spam, VAGue Focus, Helgoland Bite, Wrong Number

## Attack chain

```mermaid
flowchart LR
    E["Attacker + jailbreak prompts"]:::entry
    S0["An LLM orchestrator drives a cluster of sub-agents"]:::step
    I["The target system is compromised"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenAI PDF | <https://cdn.openai.com/threat-intelligence-reports/5f73af09-a3a3-4a55-992e-069237681620/disrupting-malicious-uses-of-ai-june-2025.pdf> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-06-05` (raw: 2025-06-05, precision `day`) |
| Kind | Threat report `report` |
| Type | [`WEAPON`](../../taxonomy/types.md#weapon) Agent used as a weapon |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-06-05-liu-wei-xie-bao-gao` |

<sub>**Why this classification:** Threat intelligence report covering several incidents; it is not counted as a single incident itself, so `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Offensive AI capability evolution](../../topics/offensive-ai.md)

**Related records:**

- `2025-06-01` [Check Point's "Skynet" sample](2025-06-01-check-point-skynet.md)<br>  <sub>Check Point's "Skynet" sample</sub>
- `2025-06-01` [Anthropic logs the precursor to GTG-1002](2025-06-01-anthropic-gtg-ji-lu-shen.md)<br>  <sub>Anthropic logs the precursor to GTG-1002</sub>
- `2025-05-01` [Anthropic logs the start of GTG-2002 activity](../2025-05/2025-05-01-anthropic-gtg-ji-lu-huo.md)<br>  <sub>Anthropic logs the start of GTG-2002 activity</sub>
- `2025-05-01` [AI-driven credential stuffing and scanning goes to scale](../2025-05/2025-05-01-qu-dong-zhuang-ku-zi.md)<br>  <sub>AI-driven credential stuffing and scanning goes to scale</sub>

---

[← 2025-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-06/2025-06-05-liu-wei-xie-bao-gao.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
