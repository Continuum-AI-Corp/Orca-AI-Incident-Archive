---
id: 2026-03-24-litellm-backdoored-release
title: "Backdoored LiteLLM release"
title_zh: "LiteLLM 后门版本"
title_ja: "バックドア入りLiteLLMリリース"
title_ko: "백도어가 심긴 LiteLLM 릴리스"
title_de: "LiteLLM-Veröffentlichung mit Backdoor"
title_fr: "Une version backdoorée de LiteLLM publiée"
title_es: "Versión de LiteLLM con puerta trasera"
date: 2026-03-24
date_precision: day
date_raw: "2026-03-24"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Attack chain: Trivy CI compromised → aqua-bot credentials stolen → trivy-action tampered with → LiteLLM's PyPI token stolen → malicious versions 1.82.7 / 1.82.8 published. **LiteLLM is the model gateway for dozens of agent frameworks including CrewAI, DSPy and Microsoft GraphRAG**. Attribution to **TeamPCP (UNC6780)**, embedding the SANDCLOCK credential stealer
  ⚠️ **Conflicting download figures: 119,000 within 2.5 hours / 47,000 within 3 hours**


summary_zh: |
  攻击链：Trivy CI 被攻陷 → 盗 aqua-bot 凭据 → 篡改 trivy-action → 窃取 LiteLLM 的 PyPI token → 发布恶意版本 1.82.7 / 1.82.8。**LiteLLM 是 CrewAI、DSPy、Microsoft GraphRAG 等数十个 agent 框架的模型网关**。归因 **TeamPCP (UNC6780)**，嵌入 SANDCLOCK 凭据窃取器
  ⚠️ **下载量来源冲突：2.5 小时内 11.9 万次 / 3 小时内 4.7 万次**

summary_ja: |
  攻撃チェーン：Trivy CIの侵害→aqua-botの認証情報窃取→trivy-actionの改ざん→LiteLLMのPyPIトークン窃取→悪性バージョン1.82.7／1.82.8の公開。**LiteLLMはCrewAI、DSPy、Microsoft GraphRAGを含む数十のエージェントフレームワークのモデルゲートウェイである**。帰属は**TeamPCP（UNC6780）**で、SANDCLOCK認証情報窃取ツールを組み込んでいた。
  ⚠️ **ダウンロード数は情報源が矛盾：2.5時間で119,000／3時間で47,000**

summary_ko: |
  공격 사슬: Trivy CI 침해 → aqua-bot 자격 증명 탈취 → trivy-action 변조 → LiteLLM의 PyPI 토큰 탈취 → 악성 버전 1.82.7 / 1.82.8 게시. **LiteLLM은 CrewAI, DSPy, Microsoft GraphRAG 등 수십 개 에이전트 프레임워크의 모델 게이트웨이**다. **TeamPCP (UNC6780)**로 귀속되었으며 SANDCLOCK 자격 증명 탈취기를 내장했다
  ⚠️ **다운로드 수치는 엇갈린다: 2.5시간 내 119,000회 / 3시간 내 47,000회**

summary_de: |
  Angriffskette: Trivy-CI kompromittiert → aqua-bot-Zugangsdaten gestohlen → trivy-action manipuliert → LiteLLMs PyPI-Token gestohlen → bösartige Versionen 1.82.7 / 1.82.8 veröffentlicht. **LiteLLM ist das Modell-Gateway für Dutzende Agent-Frameworks, darunter CrewAI, DSPy und Microsoft GraphRAG**. Zuschreibung an **TeamPCP (UNC6780)**, eingebettet ist der Zugangsdaten-Stealer SANDCLOCK
  ⚠️ **Widersprüchliche Downloadzahlen: 119,000 innerhalb von 2.5 Stunden / 47,000 innerhalb von 3 Stunden**

summary_fr: |
  Chaîne d'attaque : CI Trivy compromise → identifiants aqua-bot volés → trivy-action altérée → jeton PyPI de LiteLLM volé → publication des versions malveillantes 1.82.7 / 1.82.8. **LiteLLM est la passerelle de modèles de dizaines de frameworks d'agents, dont CrewAI, DSPy et Microsoft GraphRAG**. Attribution à **TeamPCP (UNC6780)**, intégrant le voleur d'identifiants SANDCLOCK
  ⚠️ **Chiffres de téléchargement contradictoires : 119 000 en 2,5 heures / 47 000 en 3 heures**

summary_es: |
  Cadena de ataque: CI de Trivy comprometido → credenciales de aqua-bot robadas → trivy-action manipulado → token de PyPI de LiteLLM robado → publicación de las versiones maliciosas 1.82.7 / 1.82.8. **LiteLLM es la puerta de enlace de modelos para decenas de marcos de agentes, incluidos CrewAI, DSPy y Microsoft GraphRAG**. Atribuido a **TeamPCP (UNC6780)**, con el stealer de credenciales SANDCLOCK incrustado
  ⚠️ **Cifras de descargas en conflicto: 119,000 en 2.5 horas / 47,000 en 3 horas**

sources:
  - url: https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access
    label: GTIG
  - url: https://theori.io/ko/blog/2026-h1-hot-security-issue-case
    label: Theori

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Backdoored LiteLLM release

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Attack chain: Trivy CI compromised → aqua-bot credentials stolen → trivy-action tampered with → LiteLLM's PyPI token stolen → malicious versions 1.82.7 / 1.82.8 published. **LiteLLM is the model gateway for dozens of agent frameworks including CrewAI, DSPy and Microsoft GraphRAG**. Attribution to **TeamPCP (UNC6780)**, embedding the SANDCLOCK credential stealer

⚠️ **Conflicting download figures: 119,000 within 2.5 hours / 47,000 within 3 hours**

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
| 1 | GTIG | <https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access> |
| 2 | Theori | <https://theori.io/ko/blog/2026-h1-hot-security-issue-case> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-24` (raw: 2026-03-24, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-24-litellm-backdoored-release` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-30` [Axios npm package compromised](2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>
- `2026-03-02` [Sustained supply-chain compromise across the Trivy ecosystem](2026-03-02-trivy-sheng-tai-chi-xu.md)<br>  <sub>Sustained supply-chain compromise across the Trivy ecosystem</sub>
- `2026-03-26` [Anthropic CMS misconfiguration reveals the existence of "Mythos"](2026-03-26-anthropic-cms-mythos.md)<br>  <sub>Anthropic CMS misconfiguration reveals the existence of "Mythos"</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-24-litellm-backdoored-release.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
