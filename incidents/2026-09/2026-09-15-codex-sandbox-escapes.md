---
id: 2026-09-15-codex-sandbox-escapes
title: "Two ways out of the OpenAI Codex sandbox: Heapjack and Overpatch"
title_zh: "OpenAI Codex 沙箱的两种逃逸：Heapjack 与 Overpatch"
title_ja: "OpenAI Codexサンドボックスからの2つの脱出：HeapjackとOverpatch"
title_ko: "OpenAI Codex 샌드박스 탈출 두 가지: Heapjack과 Overpatch"
title_de: "Zwei Wege aus der OpenAI-Codex-Sandbox: Heapjack und Overpatch"
title_fr: "Deux façons de sortir du bac à sable d'OpenAI Codex : Heapjack et Overpatch"
title_es: "Dos formas de salir del sandbox de OpenAI Codex: Heapjack y Overpatch"
date: 2026-09-15
date_raw: "2026-09-15"
date_precision: day

kind: research
type: [SANDBOX]
severity: high
confidence: B
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Oren Yomtov (Accomplish AI)** discloses two ways out of the **OpenAI Codex** sandbox, reported on **12 August** and fixed within eight days. **Heapjack**: Codex Desktop installs an unsandboxed native `node_repl` tool whose trusted and untrusted V8 contexts **share one memory heap**, so the untrusted side reads the trust token from a heap snapshot, forges a request onto the pipe to the native parent and gets **unsandboxed command execution from read-only mode** — no approval prompt, nothing on screen; open someone's repository, ask a question, and its author can run code on your machine. **Overpatch**: Codex CLI's `apply_patch` grants write access to the parent folder of every path in a patch, so naming `/tmp` widens the grant to the whole disk and one appended line to `.zshrc` runs in the next terminal. Fixed in Codex Desktop **26.818.21641** and Codex CLI **0.149.0**

summary_zh: |
  **Oren Yomtov（Accomplish AI）**披露 **OpenAI Codex** 沙箱的两种逃逸方式，均于 **8 月 12 日**上报、8 天内修复。**Heapjack**：Codex Desktop 会安装一个未沙箱化的原生 `node_repl` 工具，其可信与不可信两个 V8 上下文**共享同一内存堆**——不可信代码从堆快照中读出信任令牌，伪造请求写入通往原生父进程的管道，从而**在 read-only（最严格）模式下取得未沙箱化的命令执行**：无审批提示、界面无任何显示；打开别人的仓库、问一个问题，仓库作者就能在你的机器上执行代码。**Overpatch**：Codex CLI 的 `apply_patch` 会为补丁中每个路径的父目录授予写权限——命名 `/tmp` 即把授权扩大到整个磁盘，再经软链向 `.zshrc` 追加一行，下个终端就会执行。修复版本：Codex Desktop **26.818.21641**、Codex CLI **0.149.0**

summary_ja: |
  **Oren Yomtov氏（Accomplish AI）**が**OpenAI Codex**サンドボックスの2つの脱出経路を公表。いずれも**8月12日**に報告され、8日以内に修正された。**Heapjack**：Codex Desktopはサンドボックス外のネイティブ`node_repl`ツールを導入し、信頼済み／未信頼の2つのV8コンテキストが**同一ヒープを共有**。未信頼側はヒープスナップショットから信頼トークンを読み取り、ネイティブ親プロセスへのパイプに偽のリクエストを書き込み、**read-only（最厳格モード）からサンドボックス外のコマンド実行**を得る——承認プロンプトも画面表示もなし。他人のリポジトリを開いて質問するだけで、作者があなたのマシンでコードを実行できる。**Overpatch**：Codex CLIの`apply_patch`はパッチ内の各パスの親フォルダに書き込み権限を与えるため、`/tmp`と名付けるだけでディスク全体に権限が広がり、`.zshrc`への1行追記が次のターミナルで実行される。修正版：Codex Desktop **26.818.21641**、Codex CLI **0.149.0**

summary_ko: |
  **Oren Yomtov(Accomplish AI)**가 **OpenAI Codex** 샌드박스를 빠져나가는 두 가지 방법을 공개했다. 둘 다 **8월 12일**에 보고돼 8일 안에 수정됐다. **Heapjack**: Codex Desktop은 샌드박스 밖 네이티브 `node_repl` 도구를 설치하는데, 신뢰/비신뢰 두 V8 컨텍스트가 **하나의 메모리 힙을 공유**한다. 비신뢰 측은 힙 스냅샷에서 신뢰 토큰을 읽어 네이티브 부모 프로세스로 가는 파이프에 위조 요청을 쓰고, **read-only(가장 엄격한 모드)에서 샌드박스 밖 명령 실행**을 얻는다 — 승인 프롬프트도, 화면 표시도 없다. 남의 저장소를 열고 질문만 해도 작성자가 당신 컴퓨터에서 코드를 실행할 수 있다. **Overpatch**: Codex CLI의 `apply_patch`는 패치에 적힌 각 경로의 상위 폴더에 쓰기 권한을 부여하므로 `/tmp`라고 쓰면 권한이 디스크 전체로 확대되고, `.zshrc`에 한 줄만 덧붙이면 다음 터미널에서 실행된다. 수정 버전: Codex Desktop **26.818.21641**, Codex CLI **0.149.0**

summary_de: |
  **Oren Yomtov (Accomplish AI)** veröffentlicht zwei Wege aus der **OpenAI-Codex-Sandbox**, gemeldet am **12. August** und binnen acht Tagen behoben. **Heapjack**: Codex Desktop installiert ein nicht sandboxed natives `node_repl`-Tool, dessen vertrauenswürdiger und nicht vertrauenswürdiger V8-Kontext **einen Heap teilen** — die nicht vertrauenswürdige Seite liest das Vertrauens-Token aus einem Heap-Snapshot, schreibt eine gefälschte Anfrage in die Pipe zum nativen Elternprozess und erhält **unsandboxed Befehlsausführung aus dem read-only-Modus** — ohne Genehmigungsdialog, ohne sichtbare Anzeige; ein fremdes Repository öffnen und eine Frage stellen genügt, damit dessen Autor Code auf dem eigenen Rechner ausführt. **Overpatch**: Das `apply_patch` der Codex CLI gewährt Schreibzugriff auf den Elternordner jedes im Patch genannten Pfads — `/tmp` zu nennen erweitert die Freigabe auf die ganze Festplatte, und eine angehängte Zeile in `.zshrc` läuft im nächsten Terminal. Behoben in Codex Desktop **26.818.21641** und Codex CLI **0.149.0**

summary_fr: |
  **Oren Yomtov (Accomplish AI)** divulgue deux façons de sortir du bac à sable d'**OpenAI Codex**, signalées le **12 août** et corrigées en huit jours. **Heapjack** : Codex Desktop installe un outil natif `node_repl` hors bac à sable dont les contextes V8 de confiance et non fiables **partagent un même tas mémoire** ; le côté non fiable lit le jeton de confiance dans un instantané du tas, écrit une requête forgée dans le tuyau vers le processus parent natif et obtient **l'exécution de commandes hors bac à sable depuis le mode read-only** — sans invite d'approbation ni affichage ; ouvrir le dépôt de quelqu'un et poser une question suffit à ce que son auteur exécute du code sur votre machine. **Overpatch** : l'`apply_patch` de la CLI Codex accorde l'écriture au dossier parent de chaque chemin du patch — nommer `/tmp` étend l'autorisation à tout le disque, et une ligne ajoutée à `.zshrc` s'exécute au terminal suivant. Corrigé dans Codex Desktop **26.818.21641** et Codex CLI **0.149.0**

summary_es: |
  **Oren Yomtov (Accomplish AI)** divulga dos formas de salir del sandbox de **OpenAI Codex**, reportadas el **12 de agosto** y corregidas en ocho días. **Heapjack**: Codex Desktop instala una herramienta nativa `node_repl` fuera del sandbox cuyos contextos V8 de confianza y no confiable **comparten un mismo montón de memoria**: el lado no confiable lee el token de confianza de una instantánea del montón, escribe una petición falsificada en la tubería hacia el proceso padre nativo y logra **ejecución de comandos fuera del sandbox desde el modo read-only** — sin aviso de aprobación ni nada en pantalla; basta abrir el repositorio de otra persona y hacerle una pregunta para que su autor ejecute código en tu máquina. **Overpatch**: el `apply_patch` de la CLI de Codex concede escritura a la carpeta padre de cada ruta del parche — nombrar `/tmp` amplía el permiso a todo el disco y una línea añadida a `.zshrc` se ejecuta en el siguiente terminal. Corregido en Codex Desktop **26.818.21641** y Codex CLI **0.149.0**

sources:
  - url: https://accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/
    label: Accomplish
  - url: https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/
    label: BleepingComputer
  - url: https://www.51cto.com/article/856105.html
    label: 51CTO

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# Two ways out of the OpenAI Codex sandbox: Heapjack and Overpatch

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

**Oren Yomtov (Accomplish AI)** discloses two ways out of the **OpenAI Codex** sandbox, reported on **12 August** and fixed within eight days. **Heapjack**: Codex Desktop installs an unsandboxed native `node_repl` tool whose trusted and untrusted V8 contexts **share one memory heap**, so the untrusted side reads the trust token from a heap snapshot, forges a request onto the pipe to the native parent and gets **unsandboxed command execution from read-only mode** — no approval prompt, nothing on screen; open someone's repository, ask a question, and its author can run code on your machine. **Overpatch**: Codex CLI's `apply_patch` grants write access to the parent folder of every path in a patch, so naming `/tmp` widens the grant to the whole disk and one appended line to `.zshrc` runs in the next terminal. Fixed in Codex Desktop **26.818.21641** and Codex CLI **0.149.0**

## Attack chain

```mermaid
flowchart LR
    E["A malicious repository or patch processed by Codex"]:::entry
    S0["Heapjack reads the trust token from the shared heap / Overpatch widens its own write grant"]:::step
    I["Unsandboxed command execution on the developer's machine<br/><i>(fixed, no known exploitation)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**Heapjack, or the secret kept in the same heap.** Codex Desktop writes an `[mcp_servers.node_repl]` block into the global `~/.codex/config.toml` **at install time** — no opt-in, no setting to turn it off — so plain Codex CLI users inherit the tool too. `node_repl` is a native, **unsandboxed** Rust program that launches a Node process *inside* the sandbox; inside that one process live two V8 contexts: a trusted one holding OpenAI's own code, and an untrusted one running the agent's code. The trusted context proves itself with a random token generated fresh each run — but both contexts share one heap, and the token is just a string in it. The attack takes a heap snapshot (`v8.getHeapSnapshot()`), tries every UUID-shaped string against the pipe to the native parent, and uses the difference between "not authorized" and a real validation error as an oracle. With the token, the untrusted code writes its own request onto the same pipe, and the parent executes it: the proof of concept ran the system `open` command, launching an application outside Codex's process tree entirely. The same token reaches any Unix socket — a Docker daemon socket being the obvious target — and a tool that edits the global config. All of this runs at **read-only**, the strictest sandbox mode, with no approval prompt and nothing shown on screen.

**Overpatch, or permissions derived from attacker input.** In the open-source Codex CLI's `workspace-write` mode the agent may only write inside the project folder, and a command aimed at `$HOME` is refused. But Codex's own file-editing tool, `apply_patch`, **grants write access to the parent folder of each path named in the patch** — so a patch that merely names `/tmp` widens the grant to the root of the disk. The working exploit uses a patch with two changes: one appends a line to `.zshrc` through a symlink into the home directory, the other names `/tmp` and does nothing else. Remove the second change and the write is refused; with it, the next terminal the developer opens runs the attacker's line, unsandboxed.

**Why it matters.** Both bugs share one shape: **the enforcement mechanism lived inside the thing it was meant to enforce** — `apply_patch` derived its own permissions from input it was handed, and `node_repl` kept the secret separating trusted from untrusted code in the same memory as the untrusted code. That is the same class Pillar Security demonstrated across Cursor, Codex, Gemini CLI and Antigravity in July 2026, and it is why Accomplish's own answer is to run the entire agent inside a VM with no real credentials in the guest. OpenAI fixed both — Codex Desktop **26.818.21641** and Codex CLI **0.149.0** — but has not published a public advisory, which is why this record is graded `B`. There is no evidence either flaw was exploited in the wild.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Accomplish | <https://accomplish.ai/blog/escaping-the-openai-codex-sandbox-twice/> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/researchers-escape-openai-codex-sandbox-to-run-commands-on-host/> |
| 3 | 51CTO | <https://www.51cto.com/article/856105.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-15` (raw: 2026-09-15, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **B** — research organisation or mainstream media, with checkable detail |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-15-codex-sandbox-escapes` |

<sub>**Why this classification:** Coordinated disclosure by a security research firm, `real_harm: false`; the record marks when the attack surface became public. Graded `B` because there is no CVE or vendor advisory to anchor it. Rated `high`: a capability demonstration of significance — two escapes from the strictest sandbox of a widely deployed coding agent. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-20` [Six sandbox escapes across four coding agents in one week](../2026-07/2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>
- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-15-codex-sandbox-escapes.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
