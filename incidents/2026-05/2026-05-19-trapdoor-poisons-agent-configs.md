---
id: 2026-05-19-trapdoor-poisons-agent-configs
title: "TrapDoor: poisoning three ecosystems to corrupt AI assistant configs"
title_zh: "TrapDoor：跨三个生态投毒，专门污染 AI 助手配置"
title_ja: "TrapDoor：3つのエコシステムを汚染してAIアシスタントの設定を破壊"
title_ko: "TrapDoor: 세 생태계를 오염시켜 AI 어시스턴트 설정을 변조"
title_de: "TrapDoor: Vergiftung dreier Ökosysteme zur Manipulation von KI-Assistenten-Konfigurationen"
title_fr: "TrapDoor : empoisonner trois écosystèmes pour corrompre les configurations d'assistants IA"
title_es: "TrapDoor: envenenar tres ecosistemas para corromper las configuraciones de asistentes de IA"
date: 2026-05-19
date_precision: day
date_raw: "2026-05-19"

kind: incident
type: [SUPPLY, CRED]
severity: critical
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **34 malicious packages, 384+ artifact versions** spanning **npm (21) + PyPI (7) + Crates.io (6)**; the earliest artifact was uploaded 2026-05-22, while the infrastructure shows an actual start on 05-19. Beyond the usual theft (SSH keys, AWS credentials, GitHub tokens, Sui/Solana/Aptos wallets, browser login data, environment variables, API keys), **the novel technique hides instructions behind zero-width Unicode inside `.cursorrules` and `CLAUDE.md`** — when Claude Code or Cursor reads those files, it performs a **fake "security scan"** and quietly carries the credentials away


summary_zh: |
  **34 个恶意包、384+ 个构件版本**，横跨 **npm(21) + PyPI(7) + Crates.io(6)**，最早构件 2026-05-22 上传、基础设施显示实际起点 05-19。除常规窃取（SSH 密钥、AWS 凭据、GitHub token、Sui/Solana/Aptos 钱包、浏览器登录数据、环境变量、API key）外，**新技法是把用零宽 Unicode 隐藏的指令塞进 `.cursorrules` 与 `CLAUDE.md`** —— 当 Claude Code 或 Cursor 读到这些文件时，就会执行一次**假的「安全扫描」**，静默把凭据带走

summary_ja: |
  **34個の悪性パッケージ、384以上のアーティファクトバージョン**で、**npm（21）＋PyPI（7）＋Crates.io（6）**にまたがる。最古のアーティファクトは2026-05-22にアップロードされたが、インフラは実際には05-19に開始していたことを示す。通常の窃取（SSHキー、AWS認証情報、GitHubトークン、Sui/Solana/Aptosウォレット、ブラウザのログインデータ、環境変数、APIキー）に加え、**新しい手法として`.cursorrules`と`CLAUDE.md`内のゼロ幅Unicodeの背後に指示を隠す**——Claude CodeやCursorがこれらのファイルを読むと、**偽の「セキュリティスキャン」**を実行し、静かに認証情報を持ち去る

summary_ko: |
  **악성 패키지 34개, 아티팩트 버전 384개 이상**이 **npm(21) + PyPI(7) + Crates.io(6)**에 걸쳐 있다. 가장 이른 아티팩트는 2026-05-22에 업로드되었지만 인프라로 보아 실제 시작은 05-19이다. 통상적인 탈취(SSH 키, AWS 자격 증명, GitHub 토큰, Sui/Solana/Aptos 지갑, 브라우저 로그인 데이터, 환경 변수, API 키) 외에 **새로운 기법으로 `.cursorrules`와 `CLAUDE.md` 안의 제로 폭 유니코드 뒤에 지시를 숨겼다** — Claude Code나 Cursor가 그 파일을 읽으면 **가짜 "보안 스캔"**을 수행하고 자격 증명을 조용히 빼돌린다

summary_de: |
  **34 bösartige Pakete, 384+ Artefaktversionen** über **npm (21) + PyPI (7) + Crates.io (6)** verteilt; das früheste Artefakt wurde am 2026-05-22 hochgeladen, während die Infrastruktur einen tatsächlichen Beginn am 05-19 zeigt. Neben dem üblichen Diebstahl (SSH-Schlüssel, AWS-Zugangsdaten, GitHub-Token, Sui-/Solana-/Aptos-Wallets, Browser-Logindaten, Umgebungsvariablen, API-Schlüssel) **versteckt die neuartige Technik Anweisungen hinter Zero-Width-Unicode in `.cursorrules` und `CLAUDE.md`** — wenn Claude Code oder Cursor diese Dateien liest, führt es einen **vorgetäuschten „Sicherheitsscan“** aus und trägt die Zugangsdaten still davon

summary_fr: |
  **34 paquets malveillants, plus de 384 versions d'artefacts** répartis sur **npm (21) + PyPI (7) + Crates.io (6)** ; l'artefact le plus ancien a été téléversé le 2026-05-22, tandis que l'infrastructure indique un début réel le 05-19. Au-delà des vols habituels (clés SSH, identifiants AWS, jetons GitHub, portefeuilles Sui/Solana/Aptos, données de connexion des navigateurs, variables d'environnement, clés API), **la technique inédite cache des instructions derrière des caractères Unicode de largeur nulle dans `.cursorrules` et `CLAUDE.md`** — quand Claude Code ou Cursor lit ces fichiers, il effectue un **faux « scan de sécurité »** et emporte discrètement les identifiants

summary_es: |
  **34 paquetes maliciosos, más de 384 versiones de artefactos** que abarcan **npm (21) + PyPI (7) + Crates.io (6)**; el artefacto más antiguo se subió el 2026-05-22, mientras que la infraestructura muestra un inicio real el 05-19. Además del robo habitual (claves SSH, credenciales de AWS, tokens de GitHub, carteras Sui/Solana/Aptos, datos de inicio de sesión de navegadores, variables de entorno, claves de API), **la técnica novedosa esconde instrucciones tras Unicode de ancho cero dentro de `.cursorrules` y `CLAUDE.md`** — cuando Claude Code o Cursor lee esos archivos, realiza un **falso "análisis de seguridad"** y se lleva las credenciales sin hacer ruido

sources:
  - url: https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html
    label: THN
  - url: https://slowmist.medium.com/threat-intelligence-trapdoor-analysis-a-cross-ecosystem-supply-chain-credential-theft-operation-a9a4e11616ea
    label: SlowMist analysis
  - url: https://phoenix.security/trapdoor-supply-chain-ai-poisoning-npm-pypi-crates/
    label: Phoenix Security

disputed: false
landmark: true
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# TrapDoor: poisoning three ecosystems to corrupt AI assistant configs

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

**34 malicious packages, 384+ artifact versions** spanning **npm (21) + PyPI (7) + Crates.io (6)**; the earliest artifact was uploaded 2026-05-22, while the infrastructure shows an actual start on 05-19. Beyond the usual theft (SSH keys, AWS credentials, GitHub tokens, Sui/Solana/Aptos wallets, browser login data, environment variables, API keys), **the novel technique hides instructions behind zero-width Unicode inside `.cursorrules` and `CLAUDE.md`** — when Claude Code or Cursor reads those files, it performs a **fake "security scan"** and quietly carries the credentials away

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    S1["The agent picks them up and calls out"]:::step
    I["Credentials are abused"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/05/trapdoor-supply-chain-attack-spreads.html> |
| 2 | SlowMist analysis | <https://slowmist.medium.com/threat-intelligence-trapdoor-analysis-a-cross-ecosystem-supply-chain-credential-theft-operation-a9a4e11616ea> |
| 3 | Phoenix Security | <https://phoenix.security/trapdoor-supply-chain-ai-poisoning-npm-pypi-crates/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-19` (raw: 2026-05-19, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning · [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-19-trapdoor-poisons-agent-configs` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `critical`: confirmed real damage at the multi-organization / government / critical-infrastructure / supply-chain-worm level, or a first-of-its-kind capability milestone with real victims. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>
- `2026-05-04` [Braintrust's AWS account compromised, all customers told to rotate AI keys](2026-05-04-braintrust-aws-zhang-hao-gong.md)<br>  <sub>Braintrust's AWS account compromised, all customers told to rotate AI keys</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
