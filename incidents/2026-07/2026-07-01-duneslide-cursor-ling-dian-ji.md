---
id: 2026-07-01-duneslide-cursor-ling-dian-ji
title: "DuneSlide: zero-click sandbox escape in Cursor"
title_zh: "DuneSlide：Cursor 零点击沙箱逃逸"
title_ja: "DuneSlide：Cursorにおけるゼロクリックのサンドボックス脱出"
title_ko: "DuneSlide: Cursor의 제로클릭 샌드박스 탈출"
title_de: "DuneSlide: Zero-Click-Sandbox-Escape in Cursor"
title_fr: "DuneSlide : évasion de bac à sable zero-click dans Cursor"
title_es: "DuneSlide: escape de sandbox zero-click en Cursor"
date: 2026-07-01
date_precision: day
date_raw: "2026-07-01"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Cato AI Labs, both CVEs at **CVSS 9.8**:
  **CVE-2026-50548** abuses the optional `working_directory` parameter of the `run_terminal_cmd` tool — the sandbox lets the write command choose its working directory, and **the agent itself can set that directory without restriction**; prompt injection just has to point it at a system path outside the project
  **CVE-2026-50549** is a flaw in the path-resolution **fallback logic**: before writing a file, Cursor resolves symlinks to confirm the real target is inside the project, but **when that check fails it trusts the path the symlink declares for itself** instead of blocking outright
  CVEs assigned on 06-05, **fixed in Cursor 3.0 (released 04-02)**; everything before 3.0 is affected
  ⚠️ **CVE-2026-50549 shares its Cursor fix ID with Wiz's "GhostApproval" of 2026-07-09** — two teams independently found the same symlink flaw; **when ingesting, merge or tag `duplicate_of`, do not double-count**


summary_zh: |
  Cato AI Labs，两个 CVE 均 **CVSS 9.8**：
  **CVE-2026-50548** 滥用 `run_terminal_cmd` 工具的可选参数 `working_directory` —— 沙箱允许写入命令的工作目录，而**这个目录可以由 agent 自己不受限制地设定**，提示注入把它指向项目外的系统路径即可
  **CVE-2026-50549** 路径解析的**回退逻辑**缺陷：写文件前 Cursor 会解析符号链接确认真实目标在项目内，但**这个检查失败时它转而信任符号链接自己声明的路径**而非直接阻止
  CVE 于 06-05 分配，**Cursor 3.0（04-02 发布）已修复**，3.0 之前全部受影响
  ⚠️ **CVE-2026-50549 与 2026-07-09 Wiz「GhostApproval」中 Cursor 的修复编号是同一个** —— 两支团队独立发现了同一符号链接缺陷，**入库时应合并或标注 `duplicate_of`，不要重复计数**

summary_ja: |
  Cato AI Labs、両CVEとも**CVSS 9.8**：
  **CVE-2026-50548**は`run_terminal_cmd`ツールのオプションの`working_directory`パラメータを悪用する——サンドボックスは書き込みコマンドに作業ディレクトリを選ばせるが、**エージェント自身がそのディレクトリを制限なく設定できる**。プロンプトインジェクションでプロジェクト外のシステムパスを指定すればよい。
  **CVE-2026-50549**はパス解決の**フォールバックロジック**の欠陥：ファイルを書き込む前にCursorはシンボリックリンクを解決して実際のターゲットがプロジェクト内にあるか確認するが、**そのチェックが失敗すると、遮断せずにシンボリックリンクが自称するパスを信頼してしまう**。
  CVEは06-05に割り当てられ、**Cursor 3.0（04-02リリース）で修正**。3.0より前のすべてが対象。
  ⚠️ **CVE-2026-50549は2026-07-09のWizの「GhostApproval」と同じCursor修正IDを持つ**——2つのチームが同じシンボリックリンク欠陥を独立に発見した。**取り込み時は統合するか`duplicate_of`タグを付け、二重計上しないこと**

summary_ko: |
  Cato AI Labs, 두 CVE 모두 **CVSS 9.8**:
  **CVE-2026-50548**은 `run_terminal_cmd` 도구의 선택적 `working_directory` 매개변수를 악용한다 — 샌드박스가 쓰기 명령에 작업 디렉터리를 고르게 허용하고 **에이전트 스스로 그 디렉터리를 제한 없이 설정할 수 있다**. 프롬프트 인젝션으로 프로젝트 밖 시스템 경로를 가리키게 하기만 하면 된다
  **CVE-2026-50549**는 경로 해석 **폴백 로직**의 결함이다: 파일을 쓰기 전에 Cursor는 심볼릭 링크를 해석해 실제 대상이 프로젝트 안에 있는지 확인하지만, **그 검사가 실패하면 차단하는 대신 심볼릭 링크가 스스로 선언한 경로를 신뢰한다**
  CVE는 06-05에 부여되었고 **Cursor 3.0(04-02 출시)에서 수정**되었다. 3.0 이전 버전은 모두 영향받는다
  ⚠️ **CVE-2026-50549는 2026-07-09 Wiz의 "GhostApproval"과 Cursor 수정 ID를 공유한다** — 두 팀이 같은 심볼릭 링크 결함을 독립적으로 발견한 것이다. **등재 시 병합하거나 `duplicate_of`로 태그하고 이중 집계하지 말 것**

summary_de: |
  Cato AI Labs, beide CVEs mit **CVSS 9.8**:
  **CVE-2026-50548** missbraucht den optionalen `working_directory`-Parameter des Tools `run_terminal_cmd` — die Sandbox lässt den Schreibbefehl sein Arbeitsverzeichnis selbst wählen, und **der Agent selbst kann dieses Verzeichnis ohne Einschränkung setzen**; eine Prompt-Injection muss es nur auf einen Systempfad außerhalb des Projekts richten
  **CVE-2026-50549** ist ein Fehler in der **Fallback-Logik** der Pfadauflösung: Vor dem Schreiben einer Datei löst Cursor Symlinks auf, um zu bestätigen, dass das reale Ziel innerhalb des Projekts liegt, doch **wenn diese Prüfung fehlschlägt, vertraut es stattdessen dem Pfad, den der Symlink für sich selbst angibt**, anstatt ihn rundheraus zu blockieren
  CVEs am 06-05 vergeben, **behoben in Cursor 3.0 (veröffentlicht 04-02)**; alles vor 3.0 ist betroffen
  ⚠️ **CVE-2026-50549 teilt sich die Cursor-Fix-ID mit Wizs „GhostApproval“ vom 2026-07-09** — zwei Teams fanden unabhängig dieselbe Symlink-Schwachstelle; **beim Erfassen zusammenführen oder mit `duplicate_of` kennzeichnen, nicht doppelt zählen**

summary_fr: |
  Cato AI Labs, les deux CVE à **CVSS 9.8** :
  **CVE-2026-50548** exploite le paramètre optionnel `working_directory` de l'outil `run_terminal_cmd` — le bac à sable laisse la commande d'écriture choisir son répertoire de travail, et **l'agent lui-même peut définir ce répertoire sans restriction** ; il suffit qu'une injection de prompt le pointe vers un chemin système hors du projet
  **CVE-2026-50549** est une faille dans la **logique de repli** de résolution de chemin : avant d'écrire un fichier, Cursor résout les liens symboliques pour confirmer que la cible réelle est dans le projet, mais **quand cette vérification échoue il fait confiance au chemin que le lien symbolique déclare pour lui-même** au lieu de bloquer purement et simplement
  CVE attribués le 06-05, **corrigés dans Cursor 3.0 (sorti le 04-02)** ; tout ce qui précède 3.0 est affecté
  ⚠️ **CVE-2026-50549 partage son identifiant de correctif Cursor avec « GhostApproval » de Wiz du 2026-07-09** — deux équipes ont trouvé indépendamment la même faille de lien symbolique ; **lors de l'ingestion, fusionner ou étiqueter `duplicate_of`, ne pas compter deux fois**

summary_es: |
  Cato AI Labs, ambos CVE con **CVSS 9.8**:
  **CVE-2026-50548** abusa del parámetro opcional `working_directory` de la herramienta `run_terminal_cmd` — el sandbox deja que el comando de escritura elija su directorio de trabajo, y **el propio agente puede fijar ese directorio sin restricción**; la inyección de prompt solo tiene que apuntarlo a una ruta del sistema fuera del proyecto
  **CVE-2026-50549** es un fallo en la **lógica de reserva** de resolución de rutas: antes de escribir un archivo, Cursor resuelve los enlaces simbólicos para confirmar que el destino real está dentro del proyecto, pero **cuando esa comprobación falla confía en la ruta que el propio enlace simbólico declara** en lugar de bloquear directamente
  CVE asignados el 06-05, **corregidos en Cursor 3.0 (lanzado el 04-02)**; todo lo anterior a 3.0 se ve afectado
  ⚠️ **CVE-2026-50549 comparte su ID de corrección de Cursor con el "GhostApproval" de Wiz del 2026-07-09** — dos equipos encontraron de forma independiente el mismo fallo de enlace simbólico; **al ingresar registros, combínalos o etiquétalos como `duplicate_of`, no los cuentes dos veces**

sources:
  - url: https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/
    label: Cato Networks
  - url: https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html
    label: THN
  - url: https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/
    label: SecurityWeek

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# DuneSlide: zero-click sandbox escape in Cursor

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Cato AI Labs, both CVEs at **CVSS 9.8**:

**CVE-2026-50548** abuses the optional `working_directory` parameter of the `run_terminal_cmd` tool — the sandbox lets the write command choose its working directory, and **the agent itself can set that directory without restriction**; prompt injection just has to point it at a system path outside the project

**CVE-2026-50549** is a flaw in the path-resolution **fallback logic**: before writing a file, Cursor resolves symlinks to confirm the real target is inside the project, but **when that check fails it trusts the path the symlink declares for itself** instead of blocking outright

CVEs assigned on 06-05, **fixed in Cursor 3.0 (released 04-02)**; everything before 3.0 is affected

⚠️ **CVE-2026-50549 shares its Cursor fix ID with Wiz's "GhostApproval" of 2026-07-09** — two teams independently found the same symlink flaw; **when ingesting, merge or tag `duplicate_of`, do not double-count**

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Cato Networks | <https://www.catonetworks.com/blog/duneslide-two-critical-rce-vulnerabilities/> |
| 2 | THN | <https://thehackernews.com/2026/07/critical-cursor-flaws-could-let-prompt.html> |
| 3 | SecurityWeek | <https://www.securityweek.com/critical-cursor-ai-ide-flaws-could-lead-to-os-level-remote-code-execution/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-01` (raw: 2026-07-01, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-01-duneslide-cursor-ling-dian-ji` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-20` [Six sandbox escapes across four coding agents in one week](2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>
- `2026-07-22` [SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host](2026-07-22-sharedroot-claude-cowork-linux.md)<br>  <sub>SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
