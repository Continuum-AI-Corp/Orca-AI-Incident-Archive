---
id: 2026-06-30-guardfall-agent-shell
title: "GuardFall: 10 of 11 open-source agents can be pushed past their shell boundary"
title_zh: "GuardFall：11 个开源 agent 中 10 个可绕过 shell 边界"
title_ja: "GuardFall：11のオープンソースエージェントのうち10がシェル境界を突破可能"
title_ko: "GuardFall: 오픈소스 에이전트 11개 중 10개가 셸 경계를 넘을 수 있다"
title_de: "GuardFall: 10 von 11 Open-Source-Agenten lassen sich über ihre Shell-Grenze treiben"
title_fr: "GuardFall : 10 agents open source sur 11 peuvent franchir leur frontière shell"
title_es: "GuardFall: 10 de 11 agentes de código abierto pueden ser empujados más allá de su frontera de shell"
date: 2026-06-30
date_precision: day
date_raw: "2026-06-30"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Adversa: the root cause is that the guardrail compares against the **raw command string**, while bash performs quote removal, expansion and command substitution before execution — **the string that is checked and the command that actually runs are not the same thing**. Five bypass classes: `r''m`, `$IFS`, command substitution, piping base64 to sh, and `find -delete`. **Only Continue structurally blocks most of them in its default IDE mode**. ⚠️ Lab-verified, not in the wild; and it requires two preconditions: "indirect prompt injection makes the LLM misjudge" + "auto-execute mode is on or the sandbox is local"


summary_zh: |
  Adversa：根因是护栏比对**原始命令字符串**，而 bash 执行前会做引号去除、展开、命令替换 —— **检查的字符串和实际执行的指令不是同一个东西**。5 类绕过：`r''m`、`$IFS`、命令替换、base64 管道给 sh、`find -delete`。**只有 Continue 在默认 IDE 模式下从结构上堵住大部分**。⚠️ 实验室实证，非在野；且需满足「间接提示注入让 LLM 误判」+「自动执行模式开启或沙箱为 local」两个前提

summary_ja: |
  Adversa：根本原因は、ガードレールが**生のコマンド文字列**と比較する一方、bashは実行前に引用符の除去、展開、コマンド置換を行うこと——**検査される文字列と実際に実行されるコマンドが同じではない**。5つのバイパスクラス：`r''m`、`$IFS`、コマンド置換、base64のshへのパイプ、`find -delete`。**デフォルトのIDEモードでその大半を構造的にブロックするのはContinueだけである**。⚠️ ラボ検証済みで実環境では未確認。前提条件が2つある：「間接プロンプトインジェクションでLLMを誤判断させる」＋「自動実行モードがオン、またはサンドボックスがローカル」

summary_ko: |
  Adversa: 근본 원인은 가드레일이 **원시 명령 문자열**과 비교하는 반면, bash는 실행 전에 따옴표 제거, 확장, 명령 치환을 수행한다는 것이다 — **검사하는 문자열과 실제 실행되는 명령이 같지 않다**. 다섯 가지 우회 유형: `r''m`, `$IFS`, 명령 치환, base64를 sh로 파이프, `find -delete`. **Continue만이 기본 IDE 모드에서 대부분을 구조적으로 차단한다**. ⚠️ 실험실 검증이며 실제 악용은 아니고, "간접 프롬프트 인젝션으로 LLM이 오판" + "자동 실행 모드가 켜져 있거나 샌드박스가 로컬"이라는 두 전제 조건이 필요하다

summary_de: |
  Adversa: Die Ursache ist, dass die Guardrail gegen den **rohen Befehlsstring** prüft, während bash vor der Ausführung Anführungszeichen entfernt, expandiert und Befehle substituiert — **der geprüfte String und der tatsächlich ausgeführte Befehl sind nicht dasselbe**. Fünf Umgehungsklassen: `r''m`, `$IFS`, Befehlssubstitution, Piping von base64 an sh und `find -delete`. **Nur Continue blockiert die meisten davon strukturell in seinem standardmäßigen IDE-Modus**. ⚠️ Im Labor verifiziert, nicht in freier Wildbahn; zudem braucht es zwei Vorbedingungen: „indirekte Prompt-Injection lässt das LLM falsch urteilen“ + „Auto-Execute-Modus ist an oder die Sandbox ist lokal“

summary_fr: |
  Adversa : la cause racine est que le garde-fou compare la **chaîne de commande brute**, tandis que bash effectue la suppression des guillemets, l'expansion et la substitution de commandes avant l'exécution — **la chaîne vérifiée et la commande réellement exécutée ne sont pas la même chose**. Cinq classes de contournement : `r''m`, `$IFS`, la substitution de commandes, le passage de base64 à sh, et `find -delete`. **Seul Continue bloque structurellement la plupart d'entre eux dans son mode IDE par défaut**. ⚠️ Vérifié en laboratoire, pas en conditions réelles ; et il faut deux préconditions : « une injection indirecte de prompt amène le LLM à mal juger » + « le mode auto-exécution est activé ou le bac à sable est local »

summary_es: |
  Adversa: la causa raíz es que el guardrail compara contra la **cadena de comando sin procesar**, mientras que bash realiza eliminación de comillas, expansión y sustitución de comandos antes de ejecutar — **la cadena que se comprueba y el comando que realmente se ejecuta no son lo mismo**. Cinco clases de omisión: `r''m`, `$IFS`, sustitución de comandos, enviar base64 a sh por tubería y `find -delete`. **Solo Continue bloquea estructuralmente la mayoría de ellas en su modo IDE predeterminado**. ⚠️ Verificado en laboratorio, no en entornos reales; y requiere dos precondiciones: "la inyección indirecta de prompt hace que el LLM juzgue mal" + "el modo de ejecución automática está activado o el sandbox es local""

sources:
  - url: https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/
    label: Adversa

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# GuardFall: 10 of 11 open-source agents can be pushed past their shell boundary

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Adversa: the root cause is that the guardrail compares against the **raw command string**, while bash performs quote removal, expansion and command substitution before execution — **the string that is checked and the command that actually runs are not the same thing**. Five bypass classes: `r''m`, `$IFS`, command substitution, piping base64 to sh, and `find -delete`. **Only Continue structurally blocks most of them in its default IDE mode**. ⚠️ Lab-verified, not in the wild; and it requires two preconditions: "indirect prompt injection makes the LLM misjudge" + "auto-execute mode is on or the sandbox is local"

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
| 1 | Adversa | <https://adversa.ai/blog/opensource-ai-coding-agents-shell-injection-vulnerability/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-30` (raw: 2026-06-30, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-06-30-guardfall-agent-shell` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-05-08` [Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)](../2026-05/2026-05-08-cline-kanban-websocket.md)<br>  <sub>Cline Kanban cross-origin WebSocket hijack (CVE-2026-44211)</sub>
- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](../2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](../2026-07/2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-30-guardfall-agent-shell.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
