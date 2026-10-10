---
id: 2026-10-08-tensorlake-npm-sdk-compromise
title: "Tensorlake's npm SDK is compromised in a ChainDrop/Shai-Hulud wave that harvests AI-agent credentials and configs"
title_zh: "Tensorlake 的 npm SDK 在 ChainDrop/Shai-Hulud 新一波攻击中被投毒：专门收割 agent 凭据与配置"
title_ja: "Tensorlakeのnpm SDKがChainDrop/Shai-Huludの新波で汚染される——エージェントの資格情報と設定を狙う"
title_ko: "Tensorlake npm SDK, ChainDrop/Shai-Hulud 새 물결에 오염 — 에이전트 자격 증명과 설정을 노린다"
title_de: "Tensorlakes npm-SDK in einer neuen ChainDrop/Shai-Hulud-Welle kompromittiert — sie erntet Agent-Zugangsdaten und -Konfigurationen"
title_fr: "Le SDK npm de Tensorlake compromis dans une nouvelle vague ChainDrop/Shai-Hulud qui récolte identifiants et configurations d'agents"
title_es: "El SDK npm de Tensorlake, comprometido en una nueva ola ChainDrop/Shai-Hulud que cosecha credenciales y configuraciones de agentes"
date: 2026-10-08
date_raw: "first rogue commit 2026-10-07 01:20 UTC; malicious 0.5.144 published 2026-10-08 01:12 UTC (flagged ~11 min later)"
date_precision: day

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 8 October 2026 a poisoned release of `tensorlake` — the npm SDK of Tensorlake, a platform that provides isolated sandboxes for running untrusted, LLM-generated code — reached the registry: version 0.5.144, published at 01:12 UTC, was flagged by Socket about 11 minutes later and has since been removed from the npm registry.** The rogue code entered via commits made under a maintainer's identity on 7 October (commit `41b38f0`); the repository was compromised for roughly 20 hours before the publish fired. It is the **ChainDrop / Shai-Hulud** worm lineage behind August's `keyv`/`cacheable` poisoning: a `preinstall` hook runs an obfuscated loader (`lib/setup.mjs`) that executes a credential-stealing, self-propagating payload (`lib/Math_Symbol.js`) via Bun — no import or agent start required. Beyond npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/wallet/messaging data, it specifically targets **AI development tooling — configuration and MCP files associated with Claude Code (`.claude`), Cursor, Kiro, Windsurf and Zed** — and writes `.claude/settings.json` and `.vscode/tasks.json` into reachable repositories, so it runs again when someone opens the project in Claude Code or VS Code. It republishes poisoned versions under a victim maintainer's identity (with valid Sigstore provenance), resolves C2 through an Ethereum contract with a GitHub fallback, and carries a "hostage token" dead-man switch: a PowerShell monitor wipes the home directory if the stolen GitHub token is revoked. No installs of 0.5.144 or downstream infections have been confirmed. Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`.

summary_zh: |
  **2026 年 10 月 8 日，`tensorlake` 的一个被投毒版本进入了 npm 仓库——它是 Tensorlake（提供"运行不可信、LLM 生成代码"隔离沙箱的平台）的 npm SDK：0.5.144 于 01:12 UTC 发布，约 11 分钟后被 Socket 标记，其后从 npm 仓库下架。** 恶意代码经由 10 月 7 日以维护者身份做出的提交进入（commit `41b38f0`）；仓库在被用于发版前已失陷约 20 小时。它属于 8 月 `keyv`/`cacheable` 投毒背后的 **ChainDrop / Shai-Hulud** 蠕虫谱系：`preinstall` 钩子运行混淆加载器（`lib/setup.mjs`），再由 Bun 执行窃密且自我复制的载荷（`lib/Math_Symbol.js`）——无需 import、无需启动 agent。除 npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/钱包/通讯应用数据外，它还**专门瞄准 AI 开发工具——Claude Code（`.claude`）、Cursor、Kiro、Windsurf 与 Zed 的配置与 MCP 文件**——并向可达仓库写入 `.claude/settings.json` 与 `.vscode/tasks.json`，使项目在 Claude Code 或 VS Code 中被打开时再次运行。它以受害者维护者身份自动重新发布被污染版本（带合法 Sigstore provenance），经以太坊合约解析 C2（GitHub 作后备），并带有"人质令牌"死手开关：若被盗 GitHub 令牌被撤销，一个 PowerShell 监视进程会清空用户主目录。目前尚无 0.5.144 的安装记录或下游感染被确认。记为 `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`。

summary_ja: |
  **2026年10月8日、`tensorlake` の汚染されたリリースがnpmレジストリに到達した。Tensorlakeは「信頼できないLLM生成コード」を動かす分離サンドボックスを提供するプラットフォームで、そのnpm SDK バージョン0.5.144は01:12 UTCに公開され、約11分後にSocketが検知し、その後npmレジストリから削除された。** 悪意あるコードは10月7日にメンテナーの身元で行われたコミット（`41b38f0`）から入り、公開の約20時間前からリポジトリが侵害されていた。8月の`keyv`/`cacheable`汚染と同じ **ChainDrop / Shai-Hulud** ワーム系統である：`preinstall`フックが難読化ローダー（`lib/setup.mjs`）を実行し、Bun経由で資格情報窃取・自己増殖ペイロード（`lib/Math_Symbol.js`）を走らせる——importもエージェント起動も不要。npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/ウォレット/メッセージアプリのデータに加え、**AI開発ツール——Claude Code（`.claude`）、Cursor、Kiro、Windsurf、Zedの設定とMCPファイル——を特に狙い**、到達可能なリポジトリに`.claude/settings.json`と`.vscode/tasks.json`を書き込むため、Claude CodeやVS Codeでプロジェクトを開くと再実行される。被害メンテナーの身元で（有効なSigstore provenance付きで）汚染版を再公開し、C2はイーサリアムコントラクト＋GitHubフォールバックで解決。盗んだGitHubトークンが失効されるとPowerShell監視プロセスがホームディレクトリを消去する「人質トークン」デッドマンスイッチを備える。0.5.144のインストールや下流感染は未確認。`incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`

summary_ko: |
  **2026년 10월 8일, `tensorlake`의 오염된 릴리스가 npm 레지스트리에 도달했다. Tensorlake는 "신뢰할 수 없는 LLM 생성 코드"를 실행하는 격리 샌드박스를 제공하는 플랫폼이며, 문제의 npm SDK 버전 0.5.144는 01:12 UTC에 게시되어 약 11분 뒤 Socket이 탐지했고 이후 npm 레지스트리에서 내려갔다.** 악성 코드는 10월 7일 유지관리자 신원으로 만들어진 커밋(`41b38f0`)으로 들어왔고, 저장소는 게시 전 약 20시간 동안 침해 상태였다. 8월 `keyv`/`cacheable` 오염과 같은 **ChainDrop / Shai-Hulud** 웜 계열이다: `preinstall` 훅이 난독화 로더(`lib/setup.mjs`)를 실행하고 Bun으로 자격 증명 탈취·자기 복제 페이로드(`lib/Math_Symbol.js`)를 구동한다 — import나 에이전트 시작이 필요 없다. npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/지갑/메신저 데이터 외에도 **AI 개발 도구 — Claude Code(`.claude`), Cursor, Kiro, Windsurf, Zed의 설정과 MCP 파일 — 를 특별히 노리고**, 접근 가능한 저장소에 `.claude/settings.json`과 `.vscode/tasks.json`을 기록해 Claude Code나 VS Code에서 프로젝트를 열면 다시 실행되게 한다. 피해 유지관리자 신원으로 (유효한 Sigstore 출처 증명과 함께) 오염 버전을 재배포하며, C2는 이더리움 컨트랙트＋GitHub 폴백으로 해석한다. 탈취한 GitHub 토큰이 폐기되면 PowerShell 모니터가 홈 디렉터리를 삭제하는 '인질 토큰' 데드맨 스위치가 있다. 0.5.144 설치나 하류 감염은 확인되지 않았다. `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`

summary_de: |
  **Am 8. Oktober 2026 erreichte eine vergiftete Version von `tensorlake` die npm-Registry — das npm-SDK von Tensorlake, einer Plattform, die isolierte Sandboxes für die Ausführung nicht vertrauenswürdigen, LLM-generierten Codes bereitstellt: Version 0.5.144 wurde um 01:12 UTC veröffentlicht, rund 11 Minuten später von Socket erkannt und seither aus der npm-Registry entfernt.** Der Schadcode gelangte über Commits unter der Identität eines Maintainers am 7. Oktober hinein (Commit `41b38f0`); das Repository war etwa 20 Stunden lang kompromittiert, bevor die Veröffentlichung ausgelöst wurde. Es ist die **ChainDrop-/Shai-Hulud**-Wurm-Linie hinter der `keyv`/`cacheable`-Vergiftung im August: Ein `preinstall`-Hook führt einen obfuskierten Loader (`lib/setup.mjs`) aus, der über Bun eine zugangsdatensammelnde, selbstreplizierende Nutzlast (`lib/Math_Symbol.js`) startet — ohne Import oder Agent-Start. Neben npm-/GitHub-/AWS-/Vault-/Kubernetes-/SSH-/`.env`-/Wallet-/Messenger-Daten zielt sie **speziell auf KI-Entwicklungswerkzeuge — Konfigurations- und MCP-Dateien von Claude Code (`.claude`), Cursor, Kiro, Windsurf und Zed** — und schreibt `.claude/settings.json` und `.vscode/tasks.json` in erreichbare Repositories, sodass sie beim Öffnen des Projekts in Claude Code oder VS Code erneut läuft. Sie veröffentlicht vergiftete Versionen unter der Identität eines Opfer-Maintainers (mit gültiger Sigstore-Provenienz), löst C2 über einen Ethereum-Vertrag mit GitHub-Fallback auf und trägt einen „Geisel-Token"-Dead-Man-Switch: Wird das gestohlene GitHub-Token widerrufen, löscht ein PowerShell-Monitor das Home-Verzeichnis. Installationen von 0.5.144 oder Folgeinfektionen sind nicht bestätigt. `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`

summary_fr: |
  **Le 8 octobre 2026, une version empoisonnée de `tensorlake` a atteint le registre npm — le SDK npm de Tensorlake, une plateforme qui fournit des sandboxes isolées pour exécuter du code non fiable généré par LLM : la version 0.5.144, publiée à 01:12 UTC, a été signalée par Socket environ 11 minutes plus tard, puis retirée du registre npm.** Le code malveillant est entré via des commits faits sous l'identité d'un mainteneur le 7 octobre (commit `41b38f0`) ; le dépôt est resté compromis environ 20 heures avant la publication. C'est la lignée du ver **ChainDrop / Shai-Hulud** derrière l'empoisonnement de `keyv`/`cacheable` en août : un hook `preinstall` exécute un loader obfusqué (`lib/setup.mjs`) qui lance via Bun une charge utile voleuse d'identifiants et auto-réplicante (`lib/Math_Symbol.js`) — sans import ni démarrage d'agent. Au-delà des données npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/portefeuilles/messagerie, elle cible **spécifiquement les outils de développement IA — fichiers de configuration et MCP de Claude Code (`.claude`), Cursor, Kiro, Windsurf et Zed** — et écrit `.claude/settings.json` et `.vscode/tasks.json` dans les dépôts accessibles, pour se réexécuter à l'ouverture du projet dans Claude Code ou VS Code. Elle republie des versions empoisonnées sous l'identité d'un mainteneur victime (avec une provenance Sigstore valide), résout son C2 via un contrat Ethereum avec repli GitHub, et porte un interrupteur « jeton-otage » : si le jeton GitHub volé est révoqué, un moniteur PowerShell efface le répertoire personnel. Aucune installation de 0.5.144 ni infection en aval n'a été confirmée. `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`

summary_es: |
  **El 8 de octubre de 2026 llegó al registro npm una versión envenenada de `tensorlake` — el SDK npm de Tensorlake, una plataforma que ofrece sandboxes aisladas para ejecutar código no confiable generado por LLM: la versión 0.5.144, publicada a las 01:12 UTC, fue marcada por Socket unos 11 minutos después; desde entonces fue retirada del registro npm.** El código malicioso entró mediante commits hechos bajo la identidad de un mantenedor el 7 de octubre (commit `41b38f0`); el repositorio estuvo comprometido unas 20 horas antes de que se disparara la publicación. Es la línea del gusano **ChainDrop / Shai-Hulud** detrás del envenenamiento de `keyv`/`cacheable` en agosto: un hook `preinstall` ejecuta un loader ofuscado (`lib/setup.mjs`) que lanza vía Bun una carga útil robacredenciales y autorreplicante (`lib/Math_Symbol.js`) — sin necesidad de import ni de iniciar un agente. Además de datos de npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/carteras/mensajería, apunta **específicamente a herramientas de desarrollo de IA — archivos de configuración y MCP de Claude Code (`.claude`), Cursor, Kiro, Windsurf y Zed** — y escribe `.claude/settings.json` y `.vscode/tasks.json` en repositorios alcanzables, de modo que se ejecuta de nuevo al abrir el proyecto en Claude Code o VS Code. Republica versiones envenenadas bajo la identidad de un mantenedor víctima (con procedencia Sigstore válida), resuelve su C2 mediante un contrato de Ethereum con respaldo en GitHub, y lleva un interruptor de hombre muerto tipo «token rehén»: si se revoca el token de GitHub robado, un monitor de PowerShell borra el directorio personal. No se han confirmado instalaciones de 0.5.144 ni infecciones posteriores. `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`

sources:
  - url: https://socket.dev/blog/tensorlake-compromise
    label: Socket (primary)
  - url: https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm
    label: StepSecurity
  - url: https://www.aikido.dev/blog/tensorlake-npm-package-compromised
    label: Aikido Security
  - url: https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html
    label: The Hacker News
  - url: https://github.com/tensorlakeai/tensorlake/issues/1014
    label: tensorlakeai/tensorlake issue #1014
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.28"
---

# Tensorlake's npm SDK is compromised in a ChainDrop/Shai-Hulud wave that harvests AI-agent credentials and configs

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-8F6A3C?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-3C6E8F?style=flat-square)

## Summary

**On 8 October 2026 a poisoned release of `tensorlake` — the npm SDK of Tensorlake, a platform that provides isolated sandboxes for running untrusted, LLM-generated code — reached the registry: version 0.5.144, published at 01:12 UTC, was flagged by Socket about 11 minutes later and has since been removed from the npm registry.** The rogue code entered via commits made under a maintainer's identity on 7 October (commit `41b38f0`); the repository was compromised for roughly 20 hours before the publish fired. It is the **ChainDrop / Shai-Hulud** worm lineage behind August's `keyv`/`cacheable` poisoning: a `preinstall` hook runs an obfuscated loader (`lib/setup.mjs`) that executes a credential-stealing, self-propagating payload (`lib/Math_Symbol.js`) via Bun — no import or agent start required. Beyond npm/GitHub/AWS/Vault/Kubernetes/SSH/`.env`/wallet/messaging data, it specifically targets **AI development tooling — configuration and MCP files associated with Claude Code (`.claude`), Cursor, Kiro, Windsurf and Zed** — and writes `.claude/settings.json` and `.vscode/tasks.json` into reachable repositories, so it runs again when someone opens the project in Claude Code or VS Code. It republishes poisoned versions under a victim maintainer's identity (with valid Sigstore provenance), resolves C2 through an Ethereum contract with a GitHub fallback, and carries a "hostage token" dead-man switch: a PowerShell monitor wipes the home directory if the stolen GitHub token is revoked. No installs of 0.5.144 or downstream infections have been confirmed. Recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["Rogue commits under a maintainer's identity (7 Oct 01:20 UTC);<br/>tensorlake@0.5.144 published 8 Oct 01:12 UTC"]:::entry
    S1["preinstall hook → Bun runs lib/setup.mjs,<br/>which launches lib/Math_Symbol.js — no import needed"]:::step
    S2["Harvests npm/GitHub/AWS/Vault/K8s secrets +<br/>.claude/.cursor/.kiro/Windsurf/Zed configs and MCP files"]:::step
    I["Self-propagation with valid provenance; dead-man switch<br/>wipes the home directory if the stolen token is revoked"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **7 October 2026 at 01:20 UTC** a threat actor made verified commits to `tensorlakeai/tensorlake` under a maintainer's identity, introducing the malware via direct file upload (commit `41b38f0`) and then working to bump versions and trigger publishing. The repository remained compromised for roughly **20 hours** until the release workflow published **`tensorlake@0.5.144` to npm on 8 October at 01:12:07 UTC**; Socket flagged it at 01:23:10 UTC — about **11 minutes** later — and the version is no longer downloadable. Tensorlake's own platform provides *"isolated sandboxes for running untrusted, LLM-generated code"*; its TypeScript SDK is what developers install to create and manage those environments, so the compromise lands **on the machine installing the SDK**, before any generated code reaches a sandbox. The package sees ~12K weekly downloads and has 100,000+ lifetime installs; there is no sign the attacker reached the PyPI or Cargo distributions, and no official Tensorlake advisory has been published — the only public trace so far is [GitHub issue #1014](https://github.com/tensorlakeai/tensorlake/issues/1014), opened by StepSecurity.

**What the worm does.** The release carries a `preinstall` hook (`node lib/setup.mjs`). Socket flagged two files: an obfuscated loader (`lib/setup.mjs`, SHA-256 `25a0735d…c3bcb5ef`) that drops Bun and executes the second file, and the worm payload itself (`lib/Math_Symbol.js`, SHA-256 `b50a0090…a0ad6fec`). Aikido's analysis finds a `WORMTAG` marker indicating a **novel compromise rather than reinfection** from an earlier Shai-Hulud wave, and notes the operator's added focus on quickly monetizing infected developer endpoints. Collection targets include npm/GitHub tokens; AWS, Vault and Kubernetes credentials; SSH keys, `.env` files, cryptocurrency wallets and messaging data — and, from **AI development tools, the configuration and MCP files associated with Claude Code (`.claude`), Cursor, `.kiro`, Windsurf and Zed**. The worm also writes **`.claude/settings.json` and `.vscode/tasks.json`** into repositories it can reach, "so it runs again when someone opens the project in Claude Code or VS Code." It propagates by enumerating the victim's publishable packages and republishing compromised versions **with valid Sigstore provenance**; strings referencing a fake Copilot/Dependabot workflow suggest it also plants GitHub Actions workflows. The C2 has no hardcoded domain dependency: it resolves `iseekaigogo[.]com` first, then falls back to an **Ethereum contract** read through ~30 public RPC endpoints, and stows encrypted data in GitHub repositories described as *"Shai-Hulud: Here We Go Again."* The **dead-man switch** — a scheduled PowerShell monitor polling `api.github.com/user` with the stolen token — runs an attacker handler through `Invoke-Expression` if the token is revoked, wiping the home directory; the string `IfYouRevokeThisTokenItWillWipeTheComputerOfTheOwner` has appeared in earlier waves. Socket's remediation order matters: **stop and delete the token monitor before revoking any credential.**

**Why it is recorded, and how graded.** This is a supply-chain poisoning aimed at **agent infrastructure tooling**, whose credential harvest is **specifically extended to agent configs and MCP files** — core scope under the archive's supply-chain category. It is a **new wave** of the same family recorded on [2026-08-04](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md), not a new detail of that record: a different package, a different compromise and a different release pipeline (the archive keeps Shai-Hulud waves as separate records). `real_harm: false` — the malicious version was flagged about 11 minutes after publication, and **no confirmed installs or downstream infections** have been reported (Socket explicitly cautions its 12K weekly figure describes the package overall, not the malicious release). `high`: a worm-grade compromise with agent-credential targeting but no confirmed victim damage, consistent with the grading of the September MemTensor package poisoning. Confidence `A`: Socket's primary technical write-up, plus independent analyses from StepSecurity and Aikido and mainstream coverage.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Socket — "TensorLake npm SDK Compromised…" | <https://socket.dev/blog/tensorlake-compromise> |
| 2 | StepSecurity — "tensorlake-npm-compromised-hostage-token-worm" | <https://www.stepsecurity.io/blog/tensorlake-npm-compromised-hostage-token-worm> |
| 3 | Aikido Security | <https://www.aikido.dev/blog/tensorlake-npm-package-compromised> |
| 4 | The Hacker News | <https://thehackernews.com/2026/10/tensorlake-npm-package-compromised-to.html> |
| 5 | tensorlakeai/tensorlake issue #1014 | <https://github.com/tensorlakeai/tensorlake/issues/1014> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-08` (raw: first rogue commit 2026-10-07 01:20 UTC; malicious 0.5.144 published 2026-10-08 01:12 UTC, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — Socket's primary analysis plus StepSecurity and Aikido write-ups and mainstream coverage |
| Real harm | No — the malicious release was live for ~11 minutes; no confirmed installs or downstream infections |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-08-tensorlake-npm-sdk-compromise` |

<sub>**Why this classification:** A supply-chain poisoning (`SUPPLY`) of an SDK for AI-agent sandboxes whose credential theft explicitly targets agent configs and MCP files (`CRED`). `high` and `real_harm: false`: worm-grade capability aimed at agent tooling, but the malicious version was flagged within minutes and no victim installs are confirmed — matched to the September MemTensor package-poisoning grading. Recorded as a new wave of the ChainDrop/Shai-Hulud family rather than an update to the August record (different package, compromise and pipeline). Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>The same family's first agent-infrastructure wave — 400+ packages, provenance-signed</sub>
- `2026-09-23` [sckit: MemTensor's AI memory packages were backdoored](../2026-09/2026-09-23-memtensor-sckit-supply-chain.md)<br>  <sub>Another package poisoning that went straight for agent credentials and prompts</sub>
- `2025-11-21` [Shai-Hulud, second wave](../2025-11/2025-11-21-shai-hulud.md)<br>  <sub>The wave whose dead-man switch and Ethereum-C2 traits this one reuses</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-08-tensorlake-npm-sdk-compromise.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
