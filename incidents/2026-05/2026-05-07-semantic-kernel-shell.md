---
id: 2026-05-07-semantic-kernel-shell
title: "Semantic Kernel: prompt injection turns into a shell"
title_zh: "Semantic Kernel：提示注入变成 shell"
title_ja: "Semantic Kernel：プロンプトインジェクションがシェルに変わる"
title_ko: "Semantic Kernel: 프롬프트 인젝션이 셸로"
title_de: "Semantic Kernel: aus einer Prompt-Injection wird eine Shell"
title_fr: "Semantic Kernel : une injection de prompt se transforme en shell"
title_es: "Semantic Kernel: una inyección de prompt se convierte en un shell"
date: 2026-05-07
date_precision: day
date_raw: "2026-05-07"

kind: research
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft self-disclosed two agent-framework RCEs:
  **CVE-2026-26030** (CVSS 9.8, Python SDK < 1.39.4): the `InMemoryVectorStore` filter **passes attacker-controlled vector-store fields into Python `eval()`** — a crafted filter executes arbitrary code
  **CVE-2026-25592** (.NET): in `SessionsPythonPlugin`, **a developer mistakenly annotated the internal method `DownloadFileAsync` with `[KernelFunction]`**, effectively telling the model "this is a tool you can call" — **retrieving a single document was enough to start a process on the agent's host**
  Fixes: python-1.39.4 / .NET 1.71.0. **"A stray annotation turning host functionality into a model-callable tool" is a defect class unique to agent frameworks**


summary_zh: |
  Microsoft 自曝两个 agent 框架 RCE：
  **CVE-2026-26030**（CVSS 9.8，Python SDK < 1.39.4）`InMemoryVectorStore` 的 filter 把**攻击者可控的向量库字段送进 Python `eval()`** —— 构造一个恶意 filter 即可执行任意代码
  **CVE-2026-25592**（.NET）`SessionsPythonPlugin` 中，**开发者误把内部方法 `DownloadFileAsync` 打上了 `[KernelFunction]` 标注**，等于告诉模型「这是你可以调用的工具」——**检索到一份文档就足以在运行 agent 的宿主上启动进程**
  修复：python-1.39.4 / .NET 1.71.0。**「手滑加一个标注就把宿主功能变成模型可调工具」是 agent 框架特有的新缺陷类型**

summary_ja: |
  MicrosoftがエージェントフレームワークのRCE 2件を自行公表：
  **CVE-2026-26030**（CVSS 9.8、Python SDK < 1.39.4）：`InMemoryVectorStore`のフィルターが**攻撃者制御のベクトルストアフィールドをPythonの`eval()`に渡す**——細工されたフィルターで任意コードが実行される
  **CVE-2026-25592**（.NET）：`SessionsPythonPlugin`で、**開発者が内部メソッド`DownloadFileAsync`に誤って`[KernelFunction]`注釈を付けた**ため、モデルに「これは呼び出せるツールだ」と伝えることになった——**文書を1件取得するだけでエージェントのホスト上でプロセスを起動できた**
  修正：python-1.39.4／.NET 1.71.0。**「不要な注釈がホスト機能をモデル呼び出し可能なツールに変えてしまう」のはエージェントフレームワークに固有の欠陥クラスである**

summary_ko: |
  마이크로소프트가 에이전트 프레임워크 RCE 2건을 자체 공개했다:
  **CVE-2026-26030**(CVSS 9.8, Python SDK < 1.39.4): `InMemoryVectorStore` 필터가 **공격자가 제어하는 벡터 스토어 필드를 Python `eval()`로 전달**한다 — 조작된 필터가 임의 코드를 실행한다
  **CVE-2026-25592**(.NET): `SessionsPythonPlugin`에서 **개발자가 내부 메서드 `DownloadFileAsync`에 실수로 `[KernelFunction]`을 달아** 모델에게 "이것은 네가 호출할 수 있는 도구"라고 알려준 셈이다 — **문서 한 건을 조회하는 것만으로 에이전트 호스트에서 프로세스가 시작되었다**
  수정: python-1.39.4 / .NET 1.71.0. **"잘못 붙은 애너테이션이 호스트 기능을 모델이 호출 가능한 도구로 바꾸는 것"은 에이전트 프레임워크 고유의 결함 유형이다**

summary_de: |
  Microsoft hat zwei RCEs in Agent-Frameworks selbst offengelegt:
  **CVE-2026-26030** (CVSS 9.8, Python SDK < 1.39.4): Der `InMemoryVectorStore`-Filter **gibt vom Angreifer kontrollierte Felder des Vektorspeichers an Pythons `eval()` weiter** — ein präparierter Filter führt beliebigen Code aus
  **CVE-2026-25592** (.NET): In `SessionsPythonPlugin` **hat ein Entwickler die interne Methode `DownloadFileAsync` versehentlich mit `[KernelFunction]` annotiert** und dem Modell damit faktisch gesagt: „Das ist ein Tool, das du aufrufen kannst“ — **das Abrufen eines einzigen Dokuments genügte, um einen Prozess auf dem Host des Agenten zu starten**
  Korrekturen: python-1.39.4 / .NET 1.71.0. **„Eine versehentliche Annotation, die Host-Funktionalität in ein modellaufrufbares Tool verwandelt“, ist eine Defektklasse, die es nur in Agent-Frameworks gibt**

summary_fr: |
  Microsoft a auto-divulgué deux RCE dans son framework d'agents :
  **CVE-2026-26030** (CVSS 9.8, SDK Python < 1.39.4) : le filtre `InMemoryVectorStore` **fait passer des champs de vector-store contrôlés par l'attaquant dans `eval()` de Python** — un filtre fabriqué exécute du code arbitraire
  **CVE-2026-25592** (.NET) : dans `SessionsPythonPlugin`, **un développeur a annoté par erreur la méthode interne `DownloadFileAsync` avec `[KernelFunction]`**, disant de fait au modèle « voici un outil que tu peux appeler » — **récupérer un seul document suffisait à lancer un processus sur l'hôte de l'agent**
  Correctifs : python-1.39.4 / .NET 1.71.0. **« Une annotation égarée qui transforme une fonctionnalité de l'hôte en outil appelable par le modèle » est une classe de défaut propre aux frameworks d'agents**

summary_es: |
  Microsoft autodivulgó dos RCE en marcos de agentes:
  **CVE-2026-26030** (CVSS 9.8, SDK de Python < 1.39.4): el filtro de `InMemoryVectorStore` **pasa campos del almacén vectorial controlados por el atacante al `eval()` de Python** — un filtro diseñado ejecuta código arbitrario
  **CVE-2026-25592** (.NET): en `SessionsPythonPlugin`, **un desarrollador anotó por error el método interno `DownloadFileAsync` con `[KernelFunction]`**, diciéndole en la práctica al modelo "esta es una herramienta que puedes llamar" — **recuperar un solo documento bastaba para iniciar un proceso en el host del agente**
  Correcciones: python-1.39.4 / .NET 1.71.0. **"Una anotación perdida que convierte funcionalidad del host en una herramienta invocable por el modelo" es una clase de defecto exclusiva de los marcos de agentes**

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/
    label: Microsoft

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Semantic Kernel: prompt injection turns into a shell

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

Microsoft self-disclosed two agent-framework RCEs:

**CVE-2026-26030** (CVSS 9.8, Python SDK < 1.39.4): the `InMemoryVectorStore` filter **passes attacker-controlled vector-store fields into Python `eval()`** — a crafted filter executes arbitrary code

**CVE-2026-25592** (.NET): in `SessionsPythonPlugin`, **a developer mistakenly annotated the internal method `DownloadFileAsync` with `[KernelFunction]`**, effectively telling the model "this is a tool you can call" — **retrieving a single document was enough to start a process on the agent's host**

Fixes: python-1.39.4 / .NET 1.71.0. **"A stray annotation turning host functionality into a model-callable tool" is a defect class unique to agent frameworks**

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft | <https://www.microsoft.com/en-us/security/blog/2026/05/07/prompts-become-shells-rce-vulnerabilities-ai-agent-frameworks/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-07` (raw: 2026-05-07, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-07-semantic-kernel-shell` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-05-28` [BadHost (CVE-2026-48710)](2026-05-28-badhost.md)<br>  <sub>BadHost (CVE-2026-48710)</sub>
- `2026-04-16` [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br>  <sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub>
- `2026-04-07` [Flowise CVE-2025-59528 exploited in the wild](../2026-04/2026-04-07-flowise-ye-li-yong.md)<br>  <sub>Flowise CVE-2025-59528 exploited in the wild</sub>
- `2026-04-23` [OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed](../2026-04/2026-04-23-openclaw-claw-chain.md)<br>  <sub>OpenClaw "Claw Chain": four chained flaws, 245,000 servers exposed</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-07-semantic-kernel-shell.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
