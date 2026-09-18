---
id: 2026-03-01-hades-campaign-ai-coding-assistants
title: "Hades: a sustained campaign turning AI coding assistants into the attack surface"
title_zh: "Hades：把 AI 编码助手本身变成攻击面的持续战役"
title_ja: "Hades：AIコーディングアシスタントを攻撃面に変える持続キャンペーン"
title_ko: "Hades: AI 코딩 어시스턴트를 공격 표면으로 만든 지속 작전"
title_de: "Hades: eine anhaltende Kampagne, die KI-Coding-Assistenten zur Angriffsfläche macht"
title_fr: "Hades : une campagne prolongée qui transforme les assistants de code IA en surface d'attaque"
title_es: "Hades: una campaña sostenida que convierte a los asistentes de código con IA en la superficie de ataque"
date: 2026-03-01
date_precision: month
date_raw: "from 2026-03"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Running at least since 2026-03 and continuing to this day, it has stolen **294,842 secrets from 6,943 developer machines**. Tradecraft: malicious npm/PyPI packages **typosquatting MCP libraries at scale** (`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`), plus **rule files and configuration directories for 14 different AI agents** seeded with custom prompt instructions or hooks — **triggering `bun run bootstrap` when the victim opens or consults the workspace with an AI assistant**. Harvests `ANTHROPIC_API_KEY`, Claude Desktop/Claude Code config, `.mcp.json`, as well as `.npmrc`/`.pypirc`/SSH keys/AWS-GCP-Azure tokens/K8s secrets/GitHub PATs and Actions tokens/Docker config/`.env`/shell history. Stolen publishing credentials are used to keep infecting more packages, forming worm-like self-propagation. CSO Online's headline is "**the malware that lies to AI security agents**"


summary_zh: |
  至少从 2026-03 持续至今，已从 **6,943 台开发者机器窃取 294,842 个密钥**。手法：恶意 npm/PyPI 包**大量 typosquat MCP 库**（`langchain-core-mcp`、`instructor-mcp`、`openai-mcp`、`tiktoken-mcp`、`ray-mcp-server`），并**针对 14 种不同 AI agent 的规则文件与配置目录**植入自定义提示指令或钩子 —— **当受害者用 AI 助手打开或查阅该工作区时触发 `bun run bootstrap`**。收集 `ANTHROPIC_API_KEY`、Claude Desktop/Claude Code 配置、`.mcp.json`，以及 `.npmrc`/`.pypirc`/SSH 密钥/AWS-GCP-Azure 令牌/K8s secret/GitHub PAT 与 Actions token/Docker 配置/`.env`/shell 历史。窃得的发布凭据用于继续感染更多包，形成蠕虫式自传播。CSO Online 的标题是「**会对 AI 安全 agent 撒谎的恶意软件**」

summary_ja: |
  少なくとも2026-03から現在まで続いており、**6,943台の開発者マシンから294,842件のシークレットを窃取**した。手口：悪性npm/PyPIパッケージが**MCPライブラリを大規模にtyposquatting**（`langchain-core-mcp`、`instructor-mcp`、`openai-mcp`、`tiktoken-mcp`、`ray-mcp-server`）し、さらに**14種類のAIエージェントのルールファイルと設定ディレクトリ**にカスタムのプロンプト指示やフックを仕込み、**被害者がAIアシスタントでワークスペースを開くか参照した時に`bun run bootstrap`を発火させる**。`ANTHROPIC_API_KEY`、Claude Desktop/Claude Codeの設定、`.mcp.json`、そして`.npmrc`/`.pypirc`/SSHキー/AWS-GCP-Azureトークン/K8sシークレット/GitHub PATとActionsトークン/Docker設定/`.env`/シェル履歴を収集する。窃取した公開用認証情報を使い、感染をさらに広げてワーム的な自己増殖を形成。CSO Onlineの見出しは「**AIセキュリティエージェントに嘘をつくマルウェア**」

summary_ko: |
  최소 2026-03부터 지금까지 이어지고 있으며 **개발자 머신 6,943대에서 294,842건의 비밀 정보를 탈취**했다. 수법: 악성 npm/PyPI 패키지로 **MCP 라이브러리를 대규모로 타이포스쿼팅**(`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`)하고, **14종 AI 에이전트의 규칙 파일과 설정 디렉터리**에 맞춤 프롬프트 지시나 훅을 심었다 — **피해자가 AI 어시스턴트로 워크스페이스를 열거나 조회하면 `bun run bootstrap`이 실행된다**. `ANTHROPIC_API_KEY`, Claude Desktop/Claude Code 설정, `.mcp.json`은 물론 `.npmrc`/`.pypirc`/SSH 키/AWS-GCP-Azure 토큰/K8s 시크릿/GitHub PAT와 Actions 토큰/Docker 설정/`.env`/셸 기록을 수집한다. 탈취한 게시 자격 증명으로 더 많은 패키지를 계속 감염시켜 웜처럼 자기 전파한다. CSO Online의 제목은 "**AI 보안 에이전트를 속이는 악성코드**"다

summary_de: |
  Läuft mindestens seit 2026-03 und bis heute und hat **294,842 Secrets von 6,943 Entwicklerrechnern** gestohlen. Vorgehensweise: bösartige npm-/PyPI-Pakete, die **MCP-Bibliotheken in großem Umfang typosquatten** (`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`), plus **Regeldateien und Konfigurationsverzeichnisse für 14 verschiedene KI-Agenten**, die mit eigenen Prompt-Anweisungen oder Hooks versehen wurden — **was `bun run bootstrap` auslöst, wenn das Opfer den Workspace mit einem KI-Assistenten öffnet oder konsultiert**. Erntet `ANTHROPIC_API_KEY`, Claude-Desktop-/Claude-Code-Konfiguration, `.mcp.json` sowie `.npmrc`/`.pypirc`/SSH-Schlüssel/AWS-GCP-Azure-Token/K8s-Secrets/GitHub-PATs und Actions-Token/Docker-Konfiguration/`.env`/Shell-Historie. Gestohlene Veröffentlichungs-Zugangsdaten werden genutzt, um immer weitere Pakete zu infizieren, was eine wurmartige Selbstverbreitung ergibt. Die Schlagzeile von CSO Online lautet: „**die Malware, die KI-Sicherheitsagenten belügt**“

summary_fr: |
  Active au moins depuis 2026-03 et toujours en cours, elle a volé **294 842 secrets sur 6 943 machines de développeurs**. Mode opératoire : des paquets npm/PyPI malveillants qui **typosquattent des bibliothèques MCP à grande échelle** (`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`), plus des **fichiers de règles et répertoires de configuration de 14 agents IA différents** garnis d'instructions de prompt personnalisées ou de hooks — **déclenchant `bun run bootstrap` quand la victime ouvre ou consulte l'espace de travail avec un assistant IA**. Récolte `ANTHROPIC_API_KEY`, la configuration Claude Desktop/Claude Code, `.mcp.json`, ainsi que `.npmrc`/`.pypirc`/clés SSH/jetons AWS-GCP-Azure/secrets K8s/PAT GitHub et jetons Actions/config Docker/`.env`/historique shell. Les identifiants de publication volés servent à infecter toujours plus de paquets, formant une auto-propagation de type ver. Le titre de CSO Online : « **le malware qui ment aux agents de sécurité IA** »

summary_es: |
  Activa al menos desde 2026-03 y continúa hasta hoy, ha robado **294,842 secretos de 6,943 máquinas de desarrolladores**. Técnica: paquetes npm/PyPI maliciosos que **hacen typosquatting de bibliotecas MCP a escala** (`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`), además de **archivos de reglas y directorios de configuración de 14 agentes de IA distintos** sembrados con instrucciones de prompt personalizadas o hooks — **disparando `bun run bootstrap` cuando la víctima abre o consulta el espacio de trabajo con un asistente de IA**. Recolecta `ANTHROPIC_API_KEY`, la configuración de Claude Desktop/Claude Code, `.mcp.json`, así como `.npmrc`/`.pypirc`/claves SSH/tokens de AWS-GCP-Azure/secretos de K8s/PAT y tokens de Actions de GitHub/configuración de Docker/`.env`/historial del shell. Las credenciales de publicación robadas se usan para seguir infectando más paquetes, formando una autorreplicación tipo gusano. El titular de CSO Online es "**el malware que miente a los agentes de seguridad de IA**"

sources:
  - url: https://orca.security/resources/blog/hades-pypi-supply-chain-attack/
    label: Orca Security
  - url: https://www.morphisec.com/blog/when-your-ai-coding-assistant-becomes-the-attack-the-hades-supply-chain-campaign/
    label: Morphisec
  - url: https://www.csoonline.com/article/4182707/meet-hades-the-malware-that-lies-to-ai-security-agents-2.html
    label: CSO Online

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Hades: a sustained campaign turning AI coding assistants into the attack surface

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Running at least since 2026-03 and continuing to this day, it has stolen **294,842 secrets from 6,943 developer machines**. Tradecraft: malicious npm/PyPI packages **typosquatting MCP libraries at scale** (`langchain-core-mcp`, `instructor-mcp`, `openai-mcp`, `tiktoken-mcp`, `ray-mcp-server`), plus **rule files and configuration directories for 14 different AI agents** seeded with custom prompt instructions or hooks — **triggering `bun run bootstrap` when the victim opens or consults the workspace with an AI assistant**. Harvests `ANTHROPIC_API_KEY`, Claude Desktop/Claude Code config, `.mcp.json`, as well as `.npmrc`/`.pypirc`/SSH keys/AWS-GCP-Azure tokens/K8s secrets/GitHub PATs and Actions tokens/Docker config/`.env`/shell history. Stolen publishing credentials are used to keep infecting more packages, forming worm-like self-propagation. CSO Online's headline is "**the malware that lies to AI security agents**"

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks it up and calls it"]:::step
    I["Credential abuse"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Orca Security | <https://orca.security/resources/blog/hades-pypi-supply-chain-attack/> |
| 2 | Morphisec | <https://www.morphisec.com/blog/when-your-ai-coding-assistant-becomes-the-attack-the-hades-supply-chain-campaign/> |
| 3 | CSO Online | <https://www.csoonline.com/article/4182707/meet-hades-the-malware-that-lies-to-ai-security-agents-2.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-01` (raw: from 2026-03, precision `month`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-01-hades-campaign-ai-coding-assistants` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-03-24` [Backdoored LiteLLM release](2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-30` [Axios npm package compromised](2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>
- `2026-03-02` [Sustained supply-chain compromise across the Trivy ecosystem](2026-03-02-trivy-sheng-tai-chi-xu.md)<br>  <sub>Sustained supply-chain compromise across the Trivy ecosystem</sub>
- `2026-03-26` [Anthropic CMS misconfiguration reveals the existence of "Mythos"](2026-03-26-anthropic-cms-mythos.md)<br>  <sub>Anthropic CMS misconfiguration reveals the existence of "Mythos"</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
