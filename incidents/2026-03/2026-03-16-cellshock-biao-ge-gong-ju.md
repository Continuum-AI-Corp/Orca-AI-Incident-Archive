---
id: 2026-03-16-cellshock-biao-ge-gong-ju
title: "CellShock: data exfiltration through an AI spreadsheet tool"
title_zh: "AI 表格工具数据外泄（CellShock）"
title_ja: "CellShock：AI表計算ツール経由のデータ外部送信"
title_ko: "CellShock: AI 스프레드시트 도구를 통한 데이터 유출"
title_de: "CellShock: Datenexfiltration über ein KI-Tabellenkalkulationstool"
title_fr: "CellShock : exfiltration de données via un outil tableur IA"
title_es: "CellShock: exfiltración de datos a través de una herramienta de hojas de cálculo con IA"
date: 2026-03-16
date_precision: day
date_raw: "2026-03-16"

kind: research
type: [IPI, EXFIL]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  PromptArmor: instructions planted in an external dataset tricked Claude for Excel / Ramp Sheets AI into generating an **`=IMAGE()` formula** that sent confidential data to an attacker's server. **It abuses a normal spreadsheet feature, so it bypasses every defense**. Anthropic and Ramp added warnings and user confirmation, but that is still not enough


summary_zh: |
  PromptArmor：外部数据集里埋指令，诱导 Claude for Excel / Ramp Sheets AI 生成 **`=IMAGE()` 公式**把机密数据发往攻击者服务器。**滥用的是表格的正常功能，所以绕过所有防护**。Anthropic 与 Ramp 引入了警告与用户确认，但仍不充分

summary_ja: |
  PromptArmor：外部データセットに仕込まれた指示が、Claude for Excel／Ramp Sheets AIに**`=IMAGE()`数式**を生成させ、機密データを攻撃者のサーバーへ送信させた。**通常の表計算機能を悪用するため、あらゆる防御をバイパスする**。AnthropicとRampは警告とユーザー確認を追加したが、それでも十分ではない

summary_ko: |
  PromptArmor: 외부 데이터셋에 심은 지시로 Claude for Excel / Ramp Sheets AI가 **`=IMAGE()` 수식**을 생성하게 해 기밀 데이터를 공격자 서버로 전송했다. **정상적인 스프레드시트 기능을 악용하므로 모든 방어를 우회한다**. Anthropic과 Ramp는 경고와 사용자 확인 절차를 추가했지만 그것만으로는 부족하다

summary_de: |
  PromptArmor: In einem externen Datensatz platzierte Anweisungen brachten Claude for Excel / Ramp Sheets AI dazu, eine **`=IMAGE()`-Formel** zu erzeugen, die vertrauliche Daten an einen Server des Angreifers sendete. **Es missbraucht eine normale Tabellenkalkulationsfunktion und umgeht damit jede Abwehr**. Anthropic und Ramp fügten Warnungen und eine Nutzerbestätigung hinzu, doch das reicht noch nicht

summary_fr: |
  PromptArmor : des instructions plantées dans un jeu de données externe ont amené Claude for Excel / Ramp Sheets AI à générer une **formule `=IMAGE()`** qui envoyait des données confidentielles vers le serveur d'un attaquant. **Elle abuse d'une fonctionnalité normale de tableur, donc elle contourne toutes les défenses**. Anthropic et Ramp ont ajouté des avertissements et une confirmation utilisateur, mais cela ne suffit toujours pas

summary_es: |
  PromptArmor: instrucciones plantadas en un conjunto de datos externo engañaron a Claude for Excel / Ramp Sheets AI para que generara una **fórmula `=IMAGE()`** que enviaba datos confidenciales al servidor de un atacante. **Abusa de una función normal de la hoja de cálculo, así que elude todas las defensas**. Anthropic y Ramp añadieron advertencias y confirmación del usuario, pero eso aún no es suficiente

sources:
  - url: https://www.promptarmor.com/resources/cellshock-claude-ai-is-excel-lent-at-stealing-data
    label: PromptArmor CellShock
  - url: https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials
    label: PromptArmor Ramp

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# CellShock: data exfiltration through an AI spreadsheet tool

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

PromptArmor: instructions planted in an external dataset tricked Claude for Excel / Ramp Sheets AI into generating an **`=IMAGE()` formula** that sent confidential data to an attacker's server. **It abuses a normal spreadsheet feature, so it bypasses every defense**. Anthropic and Ramp added warnings and user confirmation, but that is still not enough

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | PromptArmor CellShock | <https://www.promptarmor.com/resources/cellshock-claude-ai-is-excel-lent-at-stealing-data> |
| 2 | PromptArmor Ramp | <https://www.promptarmor.com/resources/ramps-sheets-ai-exfiltrates-financials> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-16` (raw: 2026-03-16, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-16-cellshock-biao-ge-gong-ju` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-03-01` [Claudy Day: a three-flaw chain in claude.ai](2026-03-01-claudy-day-claude-ai.md)<br>  <sub>Claudy Day: a three-flaw chain in claude.ai</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>
- `2026-04-01` [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](../2026-04/2026-04-01-claude-code-github-action.md)<br>  <sub>Three CVEs in the Claude Code GitHub Action: a PR title steals your API key</sub>
- `2026-04-15` [ShareLeak (CVE-2026-21520) and PipeLeak](../2026-04/2026-04-15-shareleak-pipeleak.md)<br>  <sub>ShareLeak (CVE-2026-21520) and PipeLeak</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-16-cellshock-biao-ge-gong-ju.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
