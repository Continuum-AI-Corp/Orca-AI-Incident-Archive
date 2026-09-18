---
id: 2026-03-02-trivy-sheng-tai-chi-xu
title: "Sustained supply-chain compromise across the Trivy ecosystem"
title_zh: "Trivy 生态持续性供应链攻陷"
title_ja: "Trivyエコシステム全体にわたる持続的サプライチェーン侵害"
title_ko: "Trivy 생태계 전반의 지속적 공급망 침해"
title_de: "Anhaltende Supply-Chain-Kompromittierung im Trivy-Ökosystem"
title_fr: "Compromission prolongée de la chaîne d'approvisionnement dans l'écosystème Trivy"
title_es: "Compromiso sostenido de la cadena de suministro en el ecosistema Trivy"
date: 2026-03-02
date_precision: day
date_raw: "2026-03-02"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  GitHub repository credentials were compromised to distribute a malicious binary (v0.69.4), container images and GitHub Actions (trivy-action, setup-trivy). **The operation against the Trivy VS Code extension on OpenVSX was an AI-assisted attack — it used the victim's local AI coding assistant to exfiltrate system data**. Also affected Checkmarx KICS, LiteLLM, Telnyx and Axios


summary_zh: |
  攻破 GitHub 仓库凭据，分发恶意二进制(v0.69.4)、容器镜像、GitHub Actions（trivy-action、setup-trivy）。**其中针对 OpenVSX 上 Trivy VS Code 扩展的是 AI 辅助攻击 —— 利用受害者本机的 AI 编码助手把系统数据外带**。波及 Checkmarx KICS、LiteLLM、Telnyx、Axios

summary_ja: |
  GitHubリポジトリの認証情報が侵害され、悪性バイナリ（v0.69.4）、コンテナイメージ、GitHub Actions（trivy-action、setup-trivy）が配布された。**OpenVSX上のTrivy VS Code拡張機能に対する作戦はAI支援攻撃で、被害者のローカルAIコーディングアシスタントを使ってシステムデータを外部送信させた**。Checkmarx KICS、LiteLLM、Telnyx、Axiosも影響を受けた

summary_ko: |
  GitHub 저장소 자격 증명이 침해되어 악성 바이너리(v0.69.4), 컨테이너 이미지, GitHub Actions(trivy-action, setup-trivy)가 유포되었다. **OpenVSX의 Trivy VS Code 확장 프로그램을 겨냥한 작전은 AI 지원 공격으로, 피해자의 로컬 AI 코딩 어시스턴트를 이용해 시스템 데이터를 유출했다**. Checkmarx KICS, LiteLLM, Telnyx, Axios도 영향을 받았다

summary_de: |
  GitHub-Repository-Zugangsdaten wurden kompromittiert, um eine bösartige Binärdatei (v0.69.4), Container-Images und GitHub Actions (trivy-action, setup-trivy) zu verbreiten. **Die Operation gegen die Trivy-VS-Code-Erweiterung auf OpenVSX war ein KI-gestützter Angriff — sie nutzte den lokalen KI-Coding-Assistenten des Opfers, um Systemdaten zu exfiltrieren**. Betroffen waren außerdem Checkmarx KICS, LiteLLM, Telnyx und Axios

summary_fr: |
  Des identifiants de dépôt GitHub ont été compromis pour distribuer un binaire malveillant (v0.69.4), des images de conteneurs et des GitHub Actions (trivy-action, setup-trivy). **L'opération contre l'extension VS Code Trivy sur OpenVSX était une attaque assistée par IA — elle a utilisé l'assistant de code IA local de la victime pour exfiltrer des données système**. Également touchés : Checkmarx KICS, LiteLLM, Telnyx et Axios

summary_es: |
  Se comprometieron credenciales del repositorio de GitHub para distribuir un binario malicioso (v0.69.4), imágenes de contenedor y GitHub Actions (trivy-action, setup-trivy). **La operación contra la extensión de VS Code de Trivy en OpenVSX fue un ataque asistido por IA — usó el asistente de código con IA local de la víctima para exfiltrar datos del sistema**. También se vieron afectados Checkmarx KICS, LiteLLM, Telnyx y Axios

sources:
  - url: https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23
    label: Aqua advisory
  - url: https://socket.dev/blog/unauthorized-ai-agent-execution-code-published-to-openvsx-in-aqua-trivy-vs-code-extension
    label: Socket
  - url: https://www.trendmicro.com/ja_jp/jp-security/26/d/expertview-20260409-01.html
    label: Trend Micro

disputed: false
landmark: true
scan_month: 2026-03
scan_ref: "SCAN.md §6 2026-03"
---

# Sustained supply-chain compromise across the Trivy ecosystem

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

GitHub repository credentials were compromised to distribute a malicious binary (v0.69.4), container images and GitHub Actions (trivy-action, setup-trivy). **The operation against the Trivy VS Code extension on OpenVSX was an AI-assisted attack — it used the victim's local AI coding assistant to exfiltrate system data**. Also affected Checkmarx KICS, LiteLLM, Telnyx and Axios

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Aqua advisory | <https://github.com/aquasecurity/trivy/security/advisories/GHSA-69fq-xp46-6x23> |
| 2 | Socket | <https://socket.dev/blog/unauthorized-ai-agent-execution-code-published-to-openvsx-in-aqua-trivy-vs-code-extension> |
| 3 | Trend Micro | <https://www.trendmicro.com/ja_jp/jp-security/26/d/expertview-20260409-01.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-03-02` (raw: 2026-03-02, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-03-02-trivy-sheng-tai-chi-xu` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>
- `2026-03-24` [Backdoored LiteLLM release](2026-03-24-litellm-backdoored-release.md)<br>  <sub>Backdoored LiteLLM release</sub>
- `2026-03-30` [Axios npm package compromised](2026-03-30-axios-npm-compromised.md)<br>  <sub>Axios npm package compromised</sub>
- `2026-02-09` [Clinejection](../2026-02/2026-02-09-clinejection.md)<br>  <sub>Clinejection</sub>

---

[← 2026-03 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-03/2026-03-02-trivy-sheng-tai-chi-xu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
