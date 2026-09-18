---
id: 2026-04-24-gemini-cli-pr-ci
title: "Gemini CLI CVSS 10.0: one pull request compromises CI"
title_zh: "Gemini CLI CVSS 10.0：一个 PR 就能打穿 CI"
title_ja: "Gemini CLIのCVSS 10.0：1つのプルリクエストでCIが侵害される"
title_ko: "Gemini CLI CVSS 10.0: 풀 리퀘스트 하나로 CI 침해"
title_de: "Gemini CLI CVSS 10.0: ein Pull Request kompromittiert die CI"
title_fr: "Gemini CLI CVSS 10.0 : une pull request compromet la CI"
title_es: "Gemini CLI CVSS 10.0: una sola pull request compromete el CI"
date: 2026-04-24
date_precision: day
date_raw: "2026-04-24"

kind: vulnerability
type: [SANDBOX, SUPPLY]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Google advisory **GHSA-wpqr-6v78-jr5g**, **CVSS 3.1 score 10.0**, **no CVE assigned**. Two design gaps combine: (1) **headless mode automatically trusts any workspace directory it processes** — a malicious `.gemini/` config is loaded without user consent; (2) **`--yolo` mode ignores the fine-grained tool allowlist** — a prompt injection can invoke arbitrary shell commands.
  Result: **an unprivileged outsider (say, a contributor submitting a PR) can execute commands on the CI runner before the Gemini sandbox initialises**, obtaining secrets, credentials and source code from the workflow environment. Fixed in: `@google/gemini-cli` v0.39.1+ (preview line v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+


summary_zh: |
  Google 公告 **GHSA-wpqr-6v78-jr5g**，**CVSS 3.1 满分 10.0**，**未分配 CVE 编号**。两个设计缺口叠加：① **headless 模式自动信任它处理的任何工作区目录** —— 恶意 `.gemini/` 配置无需用户同意即被加载 ② **`--yolo` 模式无视细粒度工具白名单** —— 提示注入可调起任意 shell 命令。
  结果：**一个无特权的外部人员（比如提交 PR 的贡献者）就能在 Gemini 沙箱初始化之前于 CI runner 上执行命令**，拿到工作流环境中的密钥、凭据与源码。修复版本：`@google/gemini-cli` v0.39.1+（预览线 v0.40.0-preview.3）、`google-github-actions/run-gemini-cli` v0.1.22+

summary_ja: |
  Googleアドバイザリ**GHSA-wpqr-6v78-jr5g**、**CVSS 3.1スコア10.0**、**CVE未割り当て**。2つの設計上のギャップが組み合わさる：(1) **ヘッドレスモードが処理するあらゆるワークスペースディレクトリを自動的に信頼する**——悪性の`.gemini/`設定がユーザーの同意なしに読み込まれる。(2) **`--yolo`モードが細粒度のツール許可リストを無視する**——プロンプトインジェクションで任意のシェルコマンドを起動できる。
  結果：**非特権の外部者（例えばPRを提出するコントリビューター）が、Geminiサンドボックスの初期化前にCIランナー上でコマンドを実行**し、ワークフロー環境からシークレット、認証情報、ソースコードを取得できる。修正：`@google/gemini-cli` v0.39.1以降（プレビュー系はv0.40.0-preview.3）、`google-github-actions/run-gemini-cli` v0.1.22以降

summary_ko: |
  Google 권고 **GHSA-wpqr-6v78-jr5g**, **CVSS 3.1 점수 10.0**, **CVE 미부여**. 두 가지 설계 공백이 결합한다: (1) **헤드리스 모드가 처리하는 모든 워크스페이스 디렉터리를 자동으로 신뢰**해 사용자 동의 없이 악성 `.gemini/` 설정이 로드된다. (2) **`--yolo` 모드가 세분화된 도구 허용 목록을 무시**해 프롬프트 인젝션으로 임의 셸 명령을 호출할 수 있다.
  결과: **권한 없는 외부인(예: PR을 제출한 기여자)이 Gemini 샌드박스가 초기화되기 전에 CI 러너에서 명령을 실행**해 워크플로 환경의 비밀 정보, 자격 증명, 소스 코드를 얻을 수 있다. 수정 버전: `@google/gemini-cli` v0.39.1+(프리뷰 라인 v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+

summary_de: |
  Google-Meldung **GHSA-wpqr-6v78-jr5g**, **CVSS-3.1-Score 10.0**, **keine CVE vergeben**. Zwei Designlücken greifen ineinander: (1) **Der Headless-Modus vertraut automatisch jedem Workspace-Verzeichnis, das er verarbeitet** — eine bösartige `.gemini/`-Konfiguration wird ohne Zustimmung des Nutzers geladen; (2) **Der `--yolo`-Modus ignoriert die feinkörnige Tool-Positivliste** — eine Prompt-Injection kann beliebige Shell-Befehle aufrufen.
  Ergebnis: **Ein nicht privilegierter Außenstehender (etwa ein Contributor, der einen PR einreicht) kann Befehle auf dem CI-Runner ausführen, bevor die Gemini-Sandbox initialisiert wird**, und so Secrets, Zugangsdaten und Quellcode aus der Workflow-Umgebung erlangen. Behoben in: `@google/gemini-cli` v0.39.1+ (Preview-Linie v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+

summary_fr: |
  Avis Google **GHSA-wpqr-6v78-jr5g**, **score CVSS 3.1 de 10.0**, **aucun CVE attribué**. Deux lacunes de conception se combinent : (1) **le mode headless fait automatiquement confiance à tout répertoire d'espace de travail qu'il traite** — une configuration `.gemini/` malveillante est chargée sans consentement de l'utilisateur ; (2) **le mode `--yolo` ignore la liste blanche fine d'outils** — une injection de prompt peut invoquer des commandes shell arbitraires.
  Résultat : **un outsider non privilégié (par exemple un contributeur soumettant une PR) peut exécuter des commandes sur le runner de CI avant l'initialisation du bac à sable Gemini**, obtenant des secrets, des identifiants et du code source de l'environnement du workflow. Corrigé dans : `@google/gemini-cli` v0.39.1+ (ligne preview v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+

summary_es: |
  Aviso de Google **GHSA-wpqr-6v78-jr5g**, **puntuación CVSS 3.1 de 10.0**, **sin CVE asignado**. Se combinan dos fallos de diseño: (1) **el modo headless confía automáticamente en cualquier directorio de espacio de trabajo que procesa** — se carga una configuración `.gemini/` maliciosa sin consentimiento del usuario; (2) **el modo `--yolo` ignora la lista detallada de herramientas permitidas** — una inyección de prompt puede invocar comandos de shell arbitrarios.
  Resultado: **un externo sin privilegios (por ejemplo, un colaborador que envía un PR) puede ejecutar comandos en el runner de CI antes de que se inicialice el sandbox de Gemini**, obteniendo secretos, credenciales y código fuente del entorno del flujo de trabajo. Corregido en: `@google/gemini-cli` v0.39.1+ (línea preview v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+

sources:
  - url: https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html
    label: THN
  - url: https://hackread.com/google-cvss-10-gemini-cli-vulnerability-github-rce/
    label: HackRead
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-gemini-cli-rce-cvss10-ai-tool-security-202/
    label: CSA

disputed: false
landmark: true
scan_month: 2026-04
scan_ref: "SCAN.md §6 2026-04"
---

# Gemini CLI CVSS 10.0: one pull request compromises CI

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

Google advisory **GHSA-wpqr-6v78-jr5g**, **CVSS 3.1 score 10.0**, **no CVE assigned**. Two design gaps combine: (1) **headless mode automatically trusts any workspace directory it processes** — a malicious `.gemini/` config is loaded without user consent; (2) **`--yolo` mode ignores the fine-grained tool allowlist** — a prompt injection can invoke arbitrary shell commands.

Result: **an unprivileged outsider (say, a contributor submitting a PR) can execute commands on the CI runner before the Gemini sandbox initialises**, obtaining secrets, credentials and source code from the workflow environment. Fixed in: `@google/gemini-cli` v0.39.1+ (preview line v0.40.0-preview.3), `google-github-actions/run-gemini-cli` v0.1.22+

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    S1["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation<br/><i>(flaw disclosed, no known in-the-wild exploitation)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | THN | <https://thehackernews.com/2026/04/google-fixes-cvss-10-gemini-cli-ci-rce.html> |
| 2 | HackRead | <https://hackread.com/google-cvss-10-gemini-cli-vulnerability-github-rce/> |
| 3 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-gemini-cli-rce-cvss10-ai-tool-security-202/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-04-24` (raw: 2026-04-24, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape · [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-04-24-gemini-cli-pr-ci` |

<sub>**Why this classification:** Vulnerability disclosure; as of archiving there is no evidence of in-the-wild exploitation, so `real_harm: false`. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md) · [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-04-15` [Windsurf zero-click MCP RCE (CVE-2026-30615)](2026-04-15-windsurf-mcp-rce.md)<br>  <sub>Windsurf zero-click MCP RCE (CVE-2026-30615)</sub>
- `2026-04-19` [Vercel OAuth supply-chain intrusion](2026-04-19-vercel-oauth-gong-ying-lian.md)<br>  <sub>Vercel OAuth supply-chain intrusion</sub>
- `2026-04-28` [OpenAI Codex sandbox-escape zero-day](2026-04-28-codex-sha-xiang-rao-guo.md)<br>  <sub>OpenAI Codex sandbox-escape zero-day</sub>
- `2026-03-01` [Hades: a sustained campaign turning AI coding assistants into the attack surface](../2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br>  <sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub>

---

[← 2026-04 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-04/2026-04-24-gemini-cli-pr-ci.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
