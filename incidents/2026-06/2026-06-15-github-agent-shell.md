---
id: 2026-06-15-github-agent-shell
title: "Innocuous-looking GitHub repos make agents open a reverse shell"
title_zh: "无害外观的 GitHub 仓库让 agent 执行反弹 shell"
title_ja: "一見無害なGitHubリポジトリがエージェントにリバースシェルを開かせる"
title_ko: "무해해 보이는 GitHub 저장소가 에이전트의 리버스 셸을 열게 하다"
title_de: "Harmlos wirkende GitHub-Repositories bringen Agenten dazu, eine Reverse Shell zu öffnen"
title_fr: "Des dépôts GitHub d'apparence anodine font ouvrir un reverse shell aux agents"
title_es: "Repositorios de GitHub aparentemente inofensivos hacen que los agentes abran un reverse shell"
date: 2026-06-15
date_precision: day
date_raw: "2026-06-15"

kind: research
type: [SUPPLY]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Mozilla 0DIN's three-stage chain: the README says to run the ordinary `python3 -m axiom init` → the Python package **deliberately errors out**, luring the agent into running the initialization → `setup.sh` uses `dig +short TXT _axiom-config` to fetch DNS TXT record contents and feeds them to `bash -c`. **Claude Code executes something it has never reviewed itself** (a trusted error message + a script that pulls values from outside + an invisible DNS record, three stages of indirection). Demonstrated in a test environment; no in-the-wild reports


summary_zh: |
  Mozilla 0DIN 三段式：README 写常规 `python3 -m axiom init` → Python 包**故意报错**诱导执行初始化 → `setup.sh` 用 `dig +short TXT _axiom-config` 取 DNS TXT 记录内容喂给 `bash -c`。**Claude Code 会执行一个它自己从未审阅过的东西**（可信的错误信息 + 外取值的脚本 + 看不见的 DNS 记录，三段迂回）。检证环境实证，无在野报告

summary_ja: |
  Mozilla 0DINの3段階チェーン：READMEが通常の`python3 -m axiom init`の実行を指示→Pythonパッケージが**意図的にエラーを起こし**、エージェントを初期化の実行に誘い込む→`setup.sh`が`dig +short TXT _axiom-config`でDNS TXTレコードの内容を取得し`bash -c`に渡す。**Claude Codeは自分で一度もレビューしていないものを実行してしまう**（信頼されたエラーメッセージ＋外部から値を取得するスクリプト＋見えないDNSレコードという3段階の間接化）。テスト環境で実証され、実環境での報告はない

summary_ko: |
  Mozilla 0DIN의 3단계 사슬: README가 평범한 `python3 -m axiom init` 실행을 안내한다 → Python 패키지가 **일부러 오류를 내** 에이전트를 초기화 실행으로 유인한다 → `setup.sh`가 `dig +short TXT _axiom-config`로 DNS TXT 레코드 내용을 가져와 `bash -c`에 넘긴다. **Claude Code는 스스로 검토한 적 없는 것을 실행한다**(신뢰된 오류 메시지 + 외부에서 값을 가져오는 스크립트 + 보이지 않는 DNS 레코드라는 세 단계 간접화). 테스트 환경에서 시연되었고 실제 악용 보고는 없다

summary_de: |
  Die dreistufige Kette von Mozilla 0DIN: Die README sagt, man solle das gewöhnliche `python3 -m axiom init` ausführen → das Python-Paket **bricht absichtlich mit einem Fehler ab** und lockt den Agenten dazu, die Initialisierung auszuführen → `setup.sh` nutzt `dig +short TXT _axiom-config`, um den Inhalt des DNS-TXT-Eintrags abzurufen und an `bash -c` zu übergeben. **Claude Code führt etwas aus, das es selbst nie geprüft hat** (eine vertrauenswürdige Fehlermeldung + ein Skript, das Werte von außen holt + ein unsichtbarer DNS-Eintrag, drei Stufen der Indirektion). In einer Testumgebung demonstriert; keine Berichte aus freier Wildbahn

summary_fr: |
  La chaîne en trois étapes de Mozilla 0DIN : le README dit d'exécuter l'ordinaire `python3 -m axiom init` → le paquet Python **échoue délibérément**, attirant l'agent vers l'exécution de l'initialisation → `setup.sh` utilise `dig +short TXT _axiom-config` pour récupérer le contenu d'un enregistrement DNS TXT et l'injecte dans `bash -c`. **Claude Code exécute quelque chose qu'il n'a jamais examiné lui-même** (un message d'erreur de confiance + un script qui tire des valeurs de l'extérieur + un enregistrement DNS invisible, trois niveaux d'indirection). Démontré en environnement de test ; aucun signalement en conditions réelles

summary_es: |
  La cadena de tres etapas de Mozilla 0DIN: el README dice que se ejecute el ordinario `python3 -m axiom init` → el paquete de Python **falla deliberadamente**, atrayendo al agente a ejecutar la inicialización → `setup.sh` usa `dig +short TXT _axiom-config` para obtener el contenido de un registro TXT de DNS y lo pasa a `bash -c`. **Claude Code ejecuta algo que nunca ha revisado por sí mismo** (un mensaje de error de confianza + un script que toma valores del exterior + un registro DNS invisible, tres etapas de indirección). Demostrado en un entorno de prueba; sin informes en entornos reales

sources:
  - url: https://0din.ai/blog/clone-this-repo-and-i-own-your-machine
    label: 0DIN

disputed: false
landmark: false
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# Innocuous-looking GitHub repos make agents open a reverse shell

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Mozilla 0DIN's three-stage chain: the README says to run the ordinary `python3 -m axiom init` → the Python package **deliberately errors out**, luring the agent into running the initialization → `setup.sh` uses `dig +short TXT _axiom-config` to fetch DNS TXT record contents and feeds them to `bash -c`. **Claude Code executes something it has never reviewed itself** (a trusted error message + a script that pulls values from outside + an invisible DNS record, three stages of indirection). Demonstrated in a test environment; no in-the-wild reports

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | 0DIN | <https://0din.ai/blog/clone-this-repo-and-i-own-your-machine> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-15` (raw: 2026-06-15, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-15-github-agent-shell` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-18` [ClickFix malvertising abuses claude.ai shared conversations](2026-06-18-clickfix-claude-ai-e-yi-guang.md)<br>  <sub>ClickFix malvertising abuses claude.ai shared conversations</sub>
- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-15-github-agent-shell.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
