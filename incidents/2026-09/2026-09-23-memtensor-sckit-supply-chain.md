---
id: 2026-09-23-memtensor-sckit-supply-chain
title: "sckit: MemTensor's AI memory packages were backdoored to steal agent credentials and prompts"
title_zh: "sckit：MemTensor 的 AI 记忆包被投毒，窃取 agent 凭据与提示词"
title_ja: "sckit：MemTensorのAIメモリパッケージが改ざんされ、エージェントの資格情報とプロンプトを窃取"
title_ko: "sckit: MemTensor의 AI 메모리 패키지가 백도어되어 에이전트 자격 증명과 프롬프트를 탈취"
title_de: "sckit: MemTensors KI-Speicherpakete wurden mit einem Backdoor versehen, das Agent-Zugangsdaten und Prompts stiehlt"
title_fr: "sckit : les paquets mémoire IA de MemTensor piégés pour voler identifiants et prompts d'agents"
title_es: "sckit: los paquetes de memoria IA de MemTensor fueron puertas traseras para robar credenciales y prompts de agentes"
date: 2026-09-23
date_raw: "2026-09-23"
date_precision: day

kind: incident
type: [SUPPLY, CRED]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **Four teams — Socket, StepSecurity, SafeDep and Aikido — independently document a compromise of MemTensor's MemOS, an open-source memory framework for LLMs and agents (~11,500 GitHub stars) whose plugin powers OpenClaw agents.** On 23 September attackers published four malicious releases — npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23 and 0.1.25** plus PyPI **MemoryOS 2.0.34** — each shipping the same cross-platform Go implant, **sckit**, and each briefly the registry's **latest** version, so a plain `npm install` or `pip install` pulled the backdoor. The payload starts **when the OpenClaw gateway boots and again on every memory recall — passing the user's prompt text to the executable** — and hunts `$HOME` for npm, PyPI, GitHub, GitLab, AWS, Vault and SSH secrets, exfiltrating to `skyleen[.]fr`. Initial access came through **MemTensor's own GitHub Actions release pipelines**: the attacker pushed commits that made the release job hand over the npm or PyPI publish token before publishing, then built malicious versions through affected CI. The binaries contain functions named `recursivePublish`, `prepareRemoteNode` and `prepareRemotePython` plus a GitHub Actions template — a **worm design built to republish itself using stolen tokens**, though StepSecurity notes the code paths were not observed executing. No compromise of downstream users has been reported; recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false` pending evidence of installed-and-executed victims

summary_zh: |
  **四支团队——Socket、StepSecurity、SafeDep 与 Aikido——独立记录了 MemTensor 旗下 MemOS 的投毒事件**：MemOS 是面向 LLM 与 agent 的开源记忆框架（GitHub 约 11,500 stars），其插件为 OpenClaw agent 提供记忆能力。9 月 23 日，攻击者发布了四个恶意版本——npm 包 `@memtensor/memos-cloud-openclaw-plugin` **0.1.21、0.1.23、0.1.25** 与 PyPI 包 **MemoryOS 2.0.34**——各自携带同一个跨平台 Go 植入体 **sckit**，且都一度是 registry 上的 **latest** 版本，因此一次普通的 `npm install` 或 `pip install` 就会拉下后门。载荷的启动时机是**OpenClaw 网关启动时、以及每次记忆召回时——并把用户提示词文本传给该可执行文件**；它在 `$HOME` 中搜寻 npm、PyPI、GitHub、GitLab、AWS、Vault 与 SSH 凭据，外传至 `skyleen[.]fr`。初始访问来自 **MemTensor 自己的 GitHub Actions 发布管线**：攻击者推送了让发布任务在发布前把 npm / PyPI 令牌交出的提交，再借被污染的 CI 构建恶意版本。二进制中包含 `recursivePublish`、`prepareRemoteNode`、`prepareRemotePython` 等函数与一份 GitHub Actions 模板——这是一种**用窃得令牌自我重新发布的蠕虫设计**，但 StepSecurity 注明未观察到这些代码路径实际执行。尚无下游用户受害报告；本条记为 `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false`（待人机实际执行的受害证据）

summary_ja: |
  **Socket、StepSecurity、SafeDep、Aikidoの4チームが独立に、MemTensorのMemOS（LLMとエージェント向けのオープンソース記憶フレームワーク、GitHub約11,500スター）の侵害を記録した**。9月23日、攻撃者は4つの悪意あるリリース——npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21、0.1.23、0.1.25** とPyPI **MemoryOS 2.0.34**——を公開し、いずれも同一のクロスプラットフォームGoインプラント**sckit**を同梱、いずれも一時はregistryの**latest**だったため、通常の`npm install`や`pip install`がバックドアを引き込んだ。ペイロードは**OpenClawゲートウェイ起動時と、記憶リコールのたびに起動し、ユーザーのプロンプト文を実行ファイルに渡す**。`$HOME`内のnpm、PyPI、GitHub、GitLab、AWS、Vault、SSHの秘匿情報を探索し、`skyleen[.]fr`へ送信する。初期侵入は**MemTensor自身のGitHub Actionsリリースパイプライン**経由：攻撃者はリリースジョブに公開前にnpm/PyPIトークンを渡させるコミットを push した。バイナリには`recursivePublish`、`prepareRemoteNode`、`prepareRemotePython`という関数とGitHub Actionsテンプレートが含まれる——**窃取したトークンで自己再公開するワーム設計**だが、StepSecurityは実際の実行は確認していないと注記。下流ユーザーの被害報告はまだない

summary_ko: |
  **Socket, StepSecurity, SafeDep, Aikido 네 팀이 독립적으로 MemTensor의 MemOS(LLM과 에이전트용 오픈소스 메모리 프레임워크, GitHub 약 11,500 스타) 침해를 문서화했다.** 9월 23일 공격자는 네 개의 악성 릴리스 — npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23, 0.1.25**와 PyPI **MemoryOS 2.0.34** — 를 게시했고, 모두 동일한 크로스 플랫폼 Go 임플란트 **sckit**을 포함했으며 잠시 registry의 **latest**였기 때문에 일반적인 `npm install`이나 `pip install`이 백도어를 끌어왔다. 페이로드는 **OpenClaw 게이트웨이 시작 시 그리고 모든 메모리 리콜 시 실행되어 사용자 프롬프트 텍스트를 실행 파일에 전달한다**. `$HOME`에서 npm, PyPI, GitHub, GitLab, AWS, Vault, SSH 비밀을 찾아 `skyleen[.]fr`로 유출한다. 초기 침투는 **MemTensor 자체의 GitHub Actions 릴리스 파이프라인**을 통해 이루어졌다. 바이너리에는 `recursivePublish`, `prepareRemoteNode`, `prepareRemotePython` 함수와 GitHub Actions 템플릿이 있다 — **탈취한 토큰으로 스스로 재배포하는 웜 설계**이지만 StepSecurity는 실제 실행은 관찰되지 않았다고 밝혔다. 하위 사용자 피해 보고는 아직 없다

summary_de: |
  **Vier Teams – Socket, StepSecurity, SafeDep und Aikido – dokumentieren unabhängig die Kompromittierung von MemTensors MemOS, einem Open-Source-Speicherframework für LLMs und Agenten (~11.500 GitHub-Stars), dessen Plugin OpenClaw-Agenten antreibt.** Am 23. September veröffentlichten Angreifer vier bösartige Releases – npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23 und 0.1.25** sowie PyPI **MemoryOS 2.0.34** –, die alle dasselbe plattformübergreifende Go-Implantat **sckit** enthielten und zeitweise die **latest**-Version der Registry waren; ein einfaches `npm install` oder `pip install` zog das Backdoor. Die Payload startet **beim Start des OpenClaw-Gateways und erneut bei jedem Memory-Recall – und übergibt den Prompt-Text des Nutzers an die ausführbare Datei**. Sie durchsucht `$HOME` nach npm-, PyPI-, GitHub-, GitLab-, AWS-, Vault- und SSH-Geheimnissen und exfiltriert sie an `skyleen[.]fr`. Der Erstzugang lief über **MemTensors eigene GitHub-Actions-Release-Pipelines**: Der Angreifer pushte Commits, die den Release-Job den npm- oder PyPI-Token vor der Veröffentlichung übergeben ließen. Die Binaries enthalten Funktionen wie `recursivePublish`, `prepareRemoteNode` und `prepareRemotePython` sowie eine GitHub-Actions-Vorlage – ein **Wurm-Design, das sich mit gestohlenen Tokens selbst neu veröffentlicht**, wobei StepSecurity anmerkt, dass die Codepfade nicht in Ausführung beobachtet wurden

summary_fr: |
  **Quatre équipes — Socket, StepSecurity, SafeDep et Aikido — documentent indépendamment la compromission de MemOS de MemTensor, un framework de mémoire open source pour LLM et agents (~11 500 étoiles GitHub) dont le plugin anime les agents OpenClaw.** Le 23 septembre, l'attaquant a publié quatre versions malveillantes — npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23 et 0.1.25** et PyPI **MemoryOS 2.0.34** —, toutes portant le même implant Go multiplateforme **sckit**, et toutes brièvement **latest** sur leur registre : un simple `npm install` ou `pip install` tirait la porte dérobée. La charge s'exécute **au démarrage de la passerelle OpenClaw et à chaque rappel de mémoire — en transmettant le prompt de l'utilisateur à l'exécutable** —, fouille `$HOME` à la recherche de secrets npm, PyPI, GitHub, GitLab, AWS, Vault et SSH, et les exfiltre vers `skyleen[.]fr`. L'accès initial est passé par **les propres pipelines de release GitHub Actions de MemTensor** : l'attaquant a poussé des commits faisant remettre le jeton de publication avant l'envoi. Les binaires contiennent des fonctions `recursivePublish`, `prepareRemoteNode` et `prepareRemotePython` ainsi qu'un modèle GitHub Actions — un **ver conçu pour se republier avec les jetons volés**, sans exécution observée selon StepSecurity

summary_es: |
  **Cuatro equipos — Socket, StepSecurity, SafeDep y Aikido — documentan de forma independiente el compromiso de MemOS de MemTensor, un framework de memoria de código abierto para LLM y agentes (~11.500 estrellas en GitHub) cuyo plugin impulsa agentes OpenClaw.** El 23 de septiembre el atacante publicó cuatro versiones maliciosas — npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23 y 0.1.25** y PyPI **MemoryOS 2.0.34** —, todas con el mismo implante Go multiplataforma **sckit**, y todas momentáneamente **latest** en su registro, de modo que un simple `npm install` o `pip install` descargaba la puerta trasera. La carga se inicia **al arrancar la pasarela OpenClaw y en cada recuerdo de memoria — pasando el texto del prompt del usuario al ejecutable** —, busca en `$HOME` secretos de npm, PyPI, GitHub, GitLab, AWS, Vault y SSH, y los exfiltra a `skyleen[.]fr`. El acceso inicial llegó por **los propios pipelines de release de GitHub Actions de MemTensor**: el atacante empujó commits que hacían entregar el token de publicación antes de publicar. Los binarios contienen funciones `recursivePublish`, `prepareRemoteNode` y `prepareRemotePython` y una plantilla de GitHub Actions — un **diseño de gusano para republicarse con tokens robados**, aunque StepSecurity señala que no se observó su ejecución

sources:
  - url: https://socket.dev/blog/memtensor-compromise
    label: Socket
  - url: https://www.stepsecurity.io/blog/sckit-supply-chain-worm-hits-memtensor-npm-pypi-scopes
    label: StepSecurity
  - url: https://safedep.io/memtensor-sckit-worm-npm-pypi/
    label: SafeDep
  - url: https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html
    label: The Hacker News

disputed: false
landmark: false
scan_month: 2026-09
scan_ref: "SCAN.md §6 2026-09"
---

# sckit: MemTensor's AI memory packages were backdoored to steal agent credentials and prompts

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-3C6E8F?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-6E4B8F?style=flat-square)

## Summary

**Four teams — Socket, StepSecurity, SafeDep and Aikido — independently document a compromise of MemTensor's MemOS, an open-source memory framework for LLMs and agents (~11,500 GitHub stars) whose plugin powers OpenClaw agents.** On 23 September attackers published four malicious releases — npm `@memtensor/memos-cloud-openclaw-plugin` **0.1.21, 0.1.23 and 0.1.25** plus PyPI **MemoryOS 2.0.34** — each shipping the same cross-platform Go implant, **sckit**, and each briefly the registry's **latest** version, so a plain `npm install` or `pip install` pulled the backdoor. The payload starts **when the OpenClaw gateway boots and again on every memory recall — passing the user's prompt text to the executable** — and hunts `$HOME` for npm, PyPI, GitHub, GitLab, AWS, Vault and SSH secrets, exfiltrating to `skyleen[.]fr`. Initial access came through **MemTensor's own GitHub Actions release pipelines**: the attacker pushed commits that made the release job hand over the npm or PyPI publish token before publishing, then built malicious versions through affected CI. The binaries contain functions named `recursivePublish`, `prepareRemoteNode` and `prepareRemotePython` plus a GitHub Actions template — a **worm design built to republish itself using stolen tokens**, though StepSecurity notes the code paths were not observed executing. No compromise of downstream users has been reported; recorded `incident` / `SUPPLY` + `CRED` / `high` / `real_harm: false` pending evidence of installed-and-executed victims

## Attack chain

```mermaid
flowchart LR
    E["Attacker pushes commits that make MemTensor's release job<br/>hand over its npm / PyPI publish token"]:::entry
    S1["Four malicious releases published - each briefly 'latest'<br/>(npm 0.1.21 / 0.1.23 / 0.1.25, PyPI 2.0.34)"]:::step
    S2["sckit starts at OpenClaw gateway boot<br/>and on every memory recall<br/><i>(user prompt text passed to the binary)</i>"]:::step
    I["Credentials from $HOME exfiltrated to skyleen[.]fr<br/><i>recursivePublish code paths present but not observed executing</i>"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**A memory plugin becomes the entry point.** MemOS is MemTensor's open-source memory layer for LLMs and agents: the npm package is the **OpenClaw lifecycle plugin** that adds memory recall and storage to OpenClaw agents, and the PyPI package is the framework's Python library. Socket's reconstruction: on **23 September 2026** the attacker published malicious versions on both registries, "each currently the latest version on its registry", so *"a default install from either registry therefore pulls a compromised build."* The npm plugin's launcher is wired into the plugin's **existing registration and recall logic** — no install hooks, which means `--ignore-scripts` does not help — and calls `launchStageZero()` **at gateway startup and again on every memory recall, passing the stripped user prompt text into the child process** (StepSecurity's static review shows the prompt is captured *before* the empty-prompt check). The PyPI package starts the same binary as soon as the `memos` module is imported. StepSecurity summarises the exposure plainly: *"The evidence points to a credential-harvesting design with potential consequences beyond the memory service."*

**What sckit takes.** Six statically-linked, stripped Go binaries (~7.4 MB each for linux/darwin/windows on amd64 and arm64) live in a hidden `.sckit/` directory. String and configuration analysis shows they walk the home directory for **npm, PyPI, GitHub, GitLab, AWS, Vault and SSH secrets** — credential files like `.npmrc`, `.vault-token`, `id_ecdsa`, `credentials.db`, `access_tokens.json`, and environment variables such as `NPM_TOKEN` and `PYPI_API_TOKEN` — and report to C2 under **`skyleen[.]fr`**. Socket lists Hugging Face, HashiCorp Vault, Slack and Stripe among the token targets. The embedded configuration names a campaign id, **`cloud-openclaw-semi-nuclear`**, and the Go module is `supplychain.local/campaign`.

**Initial access: the project's own release pipeline.** SafeDep traces the entry: *"The attacker got the publish tokens from MemTensor's own GitHub Actions release pipelines. To do this, they pushed commits that made the release job hand its npm or PyPI token to the attacker before the job published anything."* Socket found the same commits in both repositories (signed `Memtensor-AI` and `MemTensor CI Review`), each adding the sckit binaries plus launch code **and altering the project's release tooling to target its registry publish token**; neither is referenced by any branch or tag. The npm releases came from the same account as legitimate releases but **without a `gitHead`** — i.e. not from the project's CI workflow. Discovery came from the community: **issue #173** on the plugin repository flagged that 0.1.21 and 0.1.23 matched no commit; the four tracking teams then pulled every version published that day and compared against the last clean release.

**A worm in design, unproven in execution.** The payload includes functions named **`recursivePublish`**, `prepareRemoteNode` and `prepareRemotePython`, and a GitHub Actions workflow template that runs `sckit stage0` on push — code whose evident purpose is to **copy itself into repositories and packages reachable with the stolen credentials, republishing as it spreads**. StepSecurity is careful: the findings *"support intended credential collection and propagation across repositories and ecosystems"* but *"do not establish which functions are reached… or that additional packages were published."* The record keeps that boundary.

**Timeline and cleanup.** Last known-good versions: npm **0.1.20** (3 August) and PyPI **2.0.33** (3 September). The malicious sequence ran on **23 September**: 00:48 UTC the plugin commit; 02:23 npm 0.1.21; 03:17 the MemOS commit; 03:45 npm 0.1.22 (clean — differs from 0.1.20 only by version string); 03:49 npm 0.1.23; 04:33 npm 0.1.24 (clean); 04:36 npm 0.1.25 tagged latest; 05:25 the 19.2 MB MemoryOS 2.0.34 wheel (vs 951 KB for 2.0.33). The interleaving of clean and malicious versions — and the size jump — are themselves detection signals. No malicious install hook existed at any point.

**Why it lands in this archive.** The target profile is exactly the `SUPPLY` category: a package whose reason to exist is serving **agent runtimes**, whose malicious payload triggers on **agent lifecycle events** (gateway boot, memory recall), and which treats **the prompt itself as an exfiltration target** alongside classic developer credentials. It is the third such case in September, after the **Deadbugz** MCP server and the **GemStuffer** RubyGems campaign — and the first seen wiring its exfiltration into OpenClaw's memory loop.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Socket | <https://socket.dev/blog/memtensor-compromise> |
| 2 | StepSecurity | <https://www.stepsecurity.io/blog/sckit-supply-chain-worm-hits-memtensor-npm-pypi-scopes> |
| 3 | SafeDep | <https://safedep.io/memtensor-sckit-worm-npm-pypi/> |
| 4 | The Hacker News | <https://thehackernews.com/2026/09/compromised-memtensor-packages-deliver.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-09-23` (raw: 2026-09-23, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) [`CRED`](../../taxonomy/types.md#cred) |
| Severity | **High** `high` |
| Confidence | **A** — four independent security firms with byte-level and static analysis of the same artifacts, plus registry timeline |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-09-23-memtensor-sckit-supply-chain` |

<sub>**Why this classification:** A supply-chain compromise of packages that serve agent runtimes, with the payload deliberately wired into agent lifecycle events and aimed at credentials and prompts — `SUPPLY` + `CRED` as an intentional intrusion, not a demonstration, hence `incident`. Rated `high`: worm-design propagation code, publish-token theft through CI, and payloads that were briefly the default install — but no confirmed downstream victim, no observed propagation execution, and rapid coordinated removal, so `real_harm: false` (the same treatment as Deadbugz, which was also caught before confirmed impact). Dated to the day of the malicious releases and the first public analyses (23 September 2026). Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply chain](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-08-10` [Deadbugz: an MCP server that turns hostile on the third tool call](../2026-08/2026-08-10-deadbugz-mcp-supply-chain.md)<br>  <sub>The MCP-side precedent: a package built to strike mid-session</sub>
- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>Registry-worm economics before this case</sub>
- `2026-09-11` [Researchers link OpenAI agents to the RubyGems "GemStuffer" campaign](2026-09-11-rubygems-gemstuffer.md)<br>  <sub>The package-registry thread earlier in September</sub>

---
