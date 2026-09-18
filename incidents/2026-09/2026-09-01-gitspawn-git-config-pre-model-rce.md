---
id: 2026-09-01-gitspawn-git-config-pre-model-rce
title: "GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted"
title_zh: "GitSpawn：恶意 .git/config 让 7 款编码 agent 在联系模型之前就执行攻击者代码"
title_ja: "GitSpawn：悪性の.git/configが7つのコーディングエージェントでモデル接続前に攻撃者コードを実行"
title_ko: "GitSpawn: 악성 .git/config가 모델에 접촉하기도 전에 7개 코딩 에이전트에서 공격자 코드를 실행"
title_de: "GitSpawn: Eine bösartige .git/config führt Angreifercode in 7 Coding-Agenten aus, bevor das Modell überhaupt kontaktiert wird"
title_fr: "GitSpawn : un .git/config malveillant exécute du code attaquant dans 7 agents de code avant même tout contact avec le modèle"
title_es: "GitSpawn: un `.git/config` malicioso ejecuta código del atacante en 7 agentes de código antes de contactar siquiera con el modelo"
date: 2026-09-01
date_precision: day
date_raw: "2026-09-01"

kind: research
type: [SUPPLY, SANDBOX]
severity: critical
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **8 Git-configuration flaws** let a cloned repository run commands through **7 AI coding agents** (including Claude Code, Codex and Cursor), and **4 vendors had still not fixed them at disclosure time**.
  The most dangerous property: **when certain commands are run inside a malicious repository, the attacker's code executes before "any prompt submitted, any model invoked, any tool approval, any trust prompt" — the command runs before the agent ever contacts the model**. The researchers demonstrated escalating a configuration-only credential leak into full RCE, harvesting 136 secrets


summary_zh: |
  **8 个 Git 配置类缺陷**让被克隆的仓库能通过 **7 款 AI 编码 agent**（含 Claude Code、Codex、Cursor）执行命令，**披露时仍有 4 家未修**。
  最要命的性质：**在恶意仓库里跑某些命令时，攻击者代码的执行发生在「没有提交任何提示、没有调用模型、没有工具批准、没有信任提示」之前 —— 命令在 agent 联系模型之前就已经执行了**。研究者演示把一个仅涉及配置的凭据泄露升级为完整 RCE，收割了 136 个密钥

summary_ja: |
  **8件のGit設定の欠陥**により、cloneしたリポジトリが**7つのAIコーディングエージェント**（Claude Code、Codex、Cursorを含む）を通じてコマンドを実行でき、**公表時点で4ベンダーが未修正のままだった**。
  最も危険な性質：**悪性リポジトリ内で特定のコマンドを実行すると、「プロンプトの送信、モデルの呼び出し、ツールの承認、信頼プロンプト」のいずれよりも前に攻撃者のコードが実行される——エージェントがモデルに接続する前にコマンドが走る**。研究者は設定のみの認証情報漏えいを完全なRCEへエスカレートさせ、136件のシークレットを収集した

summary_ko: |
  **Git 설정 결함 8건**으로 클론한 저장소가 **AI 코딩 에이전트 7개**(Claude Code, Codex, Cursor 등 포함)를 통해 명령을 실행할 수 있었고, **공개 시점에 4개 벤더는 여전히 수정하지 않았다**.
  가장 위험한 특성: **악성 저장소 안에서 특정 명령을 실행하면 "프롬프트 제출, 모델 호출, 도구 승인, 신뢰 프롬프트"보다 먼저 공격자 코드가 실행된다 — 에이전트가 모델에 접촉하기 전에 명령이 돌아간다**. 연구진은 설정만으로 가능한 자격 증명 유출을 완전한 RCE로 확대하는 것을 시연하고 비밀 정보 136건을 수집했다

summary_de: |
  **8 Fehler in der Git-Konfiguration** erlauben einem geklonten Repository, Befehle über **7 KI-Coding-Agenten** auszuführen (darunter Claude Code, Codex und Cursor), und **4 Anbieter hatten sie zum Zeitpunkt der Offenlegung noch immer nicht behoben**.
  Die gefährlichste Eigenschaft: **Wenn bestimmte Befehle in einem bösartigen Repository ausgeführt werden, läuft der Code des Angreifers, bevor „irgendein Prompt übermittelt, irgendein Modell aufgerufen, irgendeine Tool-Genehmigung erteilt, irgendein Vertrauensdialog angezeigt“ wird — der Befehl läuft, bevor der Agent das Modell überhaupt kontaktiert**. Die Forschenden demonstrierten, wie sich ein reines Zugangsdatenleck aus der Konfiguration zu vollständiger RCE ausbauen ließ, und ernteten dabei 136 Secrets

summary_fr: |
  **8 failles de configuration Git** permettent à un dépôt cloné d'exécuter des commandes à travers **7 agents de code IA** (dont Claude Code, Codex et Cursor), et **4 fournisseurs ne les avaient toujours pas corrigées au moment de la divulgation**.
  La propriété la plus dangereuse : **lorsque certaines commandes sont exécutées dans un dépôt malveillant, le code de l'attaquant s'exécute avant « tout prompt soumis, tout modèle invoqué, toute approbation d'outil, toute invite de confiance » — la commande s'exécute avant même que l'agent ne contacte le modèle**. Les chercheurs ont démontré l'escalade d'une fuite d'identifiants par simple configuration jusqu'au RCE complet, récoltant 136 secrets

summary_es: |
  **8 fallos de configuración de Git** permiten que un repositorio clonado ejecute comandos a través de **7 agentes de código con IA** (incluidos Claude Code, Codex y Cursor), y **4 proveedores aún no los habían corregido en el momento de la divulgación**.
  La propiedad más peligrosa: **cuando se ejecutan ciertos comandos dentro de un repositorio malicioso, el código del atacante se ejecuta antes de "cualquier prompt enviado, cualquier modelo invocado, cualquier aprobación de herramienta, cualquier aviso de confianza" — el comando se ejecuta antes de que el agente contacte con el modelo**. Los investigadores demostraron cómo escalar una fuga de credenciales solo por configuración hasta RCE completo, recolectando 136 secretos

sources:
  - url: https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html
    label: THN

disputed: false
landmark: true
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

**8 Git-configuration flaws** let a cloned repository run commands through **7 AI coding agents** (including Claude Code, Codex and Cursor), and **4 vendors had still not fixed them at disclosure time**.

The most dangerous property: **when certain commands are run inside a malicious repository, the attacker's code executes before "any prompt submitted, any model invoked, any tool approval, any trust prompt" — the command runs before the agent ever contacts the model**. The researchers demonstrated escalating a configuration-only credential leak into full RCE, harvesting 136 secrets

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/09/malicious-git-configs-can-make-claude.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-01` (raw: 2026-09-01, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-01-gitspawn-git-config-pre-model-rce` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `critical` but `real_harm: false`: the third trigger applies — **this research overturns a widely deployed defensive assumption**, and its significance is not about how much damage has already been done. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md) · [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>
- `2026-08-26` [Trail of Bits: VMs won't contain cyber-capable agents](../2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br>  <sub>Trail of Bits: VMs won't contain cyber-capable agents</sub>
- `2026-08-17` [AI finds a flaw AI helped write: Snowflake's Jira token](../2026-08/2026-08-17-snowflake-jira-zhao-dao-can.md)<br>  <sub>AI finds a flaw AI helped write: Snowflake's Jira token</sub>
- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](../2026-07/2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>

---

[← 2026-09 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
