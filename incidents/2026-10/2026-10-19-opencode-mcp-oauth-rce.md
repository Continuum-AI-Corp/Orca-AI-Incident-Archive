---
id: 2026-10-19-opencode-mcp-oauth-rce
title: "OpenCode: a malicious MCP server runs code on the developer's machine during OAuth sign-in"
title_zh: "OpenCode：恶意 MCP 服务器可在 OAuth 登录时于开发者机器上执行代码"
title_ja: "OpenCode：悪意あるMCPサーバーがOAuthサインイン時に開発者のマシンでコードを実行"
title_ko: "OpenCode: 악성 MCP 서버가 OAuth 사인인 중 개발자 머신에서 코드를 실행"
title_de: "OpenCode: Ein bösartiger MCP-Server führt bei der OAuth-Anmeldung Code auf dem Entwicklerrechner aus"
title_fr: "OpenCode : un serveur MCP malveillant exécute du code sur la machine du développeur lors de la connexion OAuth"
title_es: "OpenCode: un servidor MCP malicioso ejecuta código en la máquina del desarrollador durante el inicio de sesión OAuth"
date: 2026-10-19
date_raw: "2026-10-19 (Pillar Security disclosure); fixed in 1.18.33 on 2026-09-28; reported to vendor 2026-08-29"
date_precision: day

kind: vulnerability
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 19 October 2026 Pillar Security disclosed a critical **remote code execution** flaw in the **OpenCode** coding agent: an attacker-controlled **MCP server can run arbitrary code on the developer's machine during the MCP OAuth sign-in**, with no extra user interaction or consent.** The bug is in the Windows/WSL browser-launch path — OpenCode passed the OAuth URL through a shell without proper quoting, so a crafted (even HTTPS-looking) authorization URL becomes a command (macOS/Linux launch the browser without a shell and are not affected). It affects **OpenCode 1.0.137–1.18.32** and was **silently fixed in 1.18.33 (shipped 28 September)** — Pillar reported it on 29 August, and the maintainer (Anomaly) initially considered a malicious MCP server outside its threat model. Crucially there is **no CVE and no security advisory**, so scanners and dependency alerts will not flag affected installs. Pillar rates it **CVSS 9.8** and reports no in-the-wild exploitation. This is **separate** from the [OpenCode Console key breach](2026-10-17-opencode-console-breach-api-keys.md) disclosed the same week. Recorded `vulnerability` / `INFRA` / `high` / `real_harm: false`.

summary_zh: |
  **2026 年 10 月 19 日，Pillar Security 披露了 **OpenCode** 编码 agent 的一个严重**远程代码执行**缺陷：攻击者控制的 **MCP 服务器可在 MCP OAuth 登录过程中于开发者机器上执行任意代码**，无需额外的用户交互或同意。** 缺陷在 Windows/WSL 的浏览器启动路径——OpenCode 把 OAuth URL 不加正确引号地传给 shell，于是一个构造的（哪怕看起来是 HTTPS 的）授权 URL 就变成了命令（macOS/Linux 不经 shell 启动浏览器，不受影响）。影响 **OpenCode 1.0.137–1.18.32**，并在 **1.18.33（9 月 28 日发布）中被静默修复**——Pillar 于 8 月 29 日上报，维护方（Anomaly）起初认为恶意 MCP 服务器不在其威胁模型内。关键是**没有 CVE、没有安全通告**，故扫描器与依赖告警都不会标出受影响安装。Pillar 评 **CVSS 9.8**，报告无在野利用。此事与同周披露的 [OpenCode Console 密钥泄露](2026-10-17-opencode-console-breach-api-keys.md)是**不同问题**。记为 `vulnerability` / `INFRA` / `high` / `real_harm: false`。

summary_ja: |
  **2026年10月19日、Pillar Securityは**OpenCode**コーディングエージェントの重大な**リモートコード実行**欠陥を公表した：攻撃者が制御する**MCPサーバーが、MCPのOAuthサインイン中に開発者のマシンで任意コードを実行**でき、追加のユーザー操作や同意を要しない。** 欠陥はWindows/WSLのブラウザ起動経路にあり——OpenCodeがOAuth URLを適切に引用符付けせずシェルに渡すため、細工された（一見HTTPSの）認可URLがコマンドになる（macOS/Linuxはシェルを介さずブラウザを開くため影響なし）。**OpenCode 1.0.137–1.18.32**が対象で、**1.18.33（9月28日公開）で静かに修正**——Pillarは8月29日に報告、維持者（Anomaly）は当初、悪意あるMCPサーバーは脅威モデル外とした。重要なのは**CVEも勧告もない**ため、スキャナーや依存関係アラートが該当インストールを検知しないこと。Pillarは**CVSS 9.8**と評価し、実環境での悪用はないと報告。これは同週公表の[OpenCode Console鍵侵害](2026-10-17-opencode-console-breach-api-keys.md)とは**別件**。`vulnerability` / `INFRA` / `high` / `real_harm: false`

summary_ko: |
  **2026년 10월 19일, Pillar Security가 **OpenCode** 코딩 에이전트의 심각한 **원격 코드 실행** 결함을 공개했다: 공격자가 제어하는 **MCP 서버가 MCP OAuth 사인인 과정에서 개발자 머신에서 임의 코드를 실행**할 수 있으며, 추가 사용자 상호작용이나 동의가 필요 없다.** 결함은 Windows/WSL의 브라우저 실행 경로에 있다——OpenCode가 OAuth URL을 적절히 인용하지 않고 셸에 넘겨, 조작된(겉보기 HTTPS여도) 인가 URL이 명령이 된다(macOS/Linux는 셸 없이 브라우저를 열어 영향 없음). **OpenCode 1.0.137–1.18.32**가 대상이며 **1.18.33(9월 28일 공개)에서 조용히 수정**됐다——Pillar는 8월 29일 보고했고 유지자(Anomaly)는 처음에 악성 MCP 서버를 위협 모델 밖으로 봤다. 핵심은 **CVE도 보안 권고도 없어** 스캐너와 의존성 알림이 해당 설치를 표시하지 못한다는 점이다. Pillar는 **CVSS 9.8**로 평가하며 실제 악용은 없다고 보고. 이는 같은 주 공개된 [OpenCode Console 키 침해](2026-10-17-opencode-console-breach-api-keys.md)와 **별개**다. `vulnerability` / `INFRA` / `high` / `real_harm: false`

summary_de: |
  **Am 19. Oktober 2026 legte Pillar Security eine kritische **Remote-Code-Execution**-Schwachstelle im **OpenCode**-Coding-Agenten offen: Ein angreiferkontrollierter **MCP-Server kann während der MCP-OAuth-Anmeldung beliebigen Code auf dem Entwicklerrechner ausführen** — ohne zusätzliche Nutzerinteraktion oder Zustimmung.** Der Fehler steckt im Browser-Start-Pfad unter Windows/WSL — OpenCode übergab die OAuth-URL ohne korrektes Quoting an eine Shell, sodass eine präparierte (selbst HTTPS-anmutende) Autorisierungs-URL zum Befehl wird (macOS/Linux starten den Browser ohne Shell und sind nicht betroffen). Betroffen ist **OpenCode 1.0.137–1.18.32**, **still behoben in 1.18.33 (am 28. September)** — Pillar meldete es am 29. August; der Betreuer (Anomaly) hielt einen bösartigen MCP-Server zunächst für außerhalb seines Bedrohungsmodells. Entscheidend: Es gibt **kein CVE und kein Advisory**, sodass Scanner und Dependency-Alerts betroffene Installationen nicht melden. Pillar bewertet es mit **CVSS 9.8** und meldet keine Ausnutzung in freier Wildbahn. Dies ist **getrennt** von der in derselben Woche offengelegten [OpenCode-Console-Schlüsselkompromittierung](2026-10-17-opencode-console-breach-api-keys.md). `vulnerability` / `INFRA` / `high` / `real_harm: false`

summary_fr: |
  **Le 19 octobre 2026, Pillar Security a divulgué une faille critique d'**exécution de code à distance** dans l'agent de codage **OpenCode** : un **serveur MCP contrôlé par un attaquant peut exécuter du code arbitraire sur la machine du développeur pendant la connexion OAuth MCP**, sans interaction ni consentement supplémentaires.** La faille se situe dans le chemin de lancement du navigateur sous Windows/WSL — OpenCode passait l'URL OAuth à un shell sans la mettre correctement entre guillemets, de sorte qu'une URL d'autorisation forgée (même d'apparence HTTPS) devient une commande (macOS/Linux lancent le navigateur sans shell et ne sont pas concernés). Elle affecte **OpenCode 1.0.137–1.18.32** et a été **corrigée silencieusement dans 1.18.33 (publiée le 28 septembre)** — Pillar l'a signalée le 29 août ; le mainteneur (Anomaly) a d'abord estimé qu'un serveur MCP malveillant sortait de son modèle de menace. Surtout, il n'y a **ni CVE ni avis de sécurité**, de sorte que les scanners et alertes de dépendances ne signaleront pas les installations concernées. Pillar l'évalue à **CVSS 9.8** et ne signale aucune exploitation dans la nature. C'est **distinct** de la [compromission des clés de l'OpenCode Console](2026-10-17-opencode-console-breach-api-keys.md) divulguée la même semaine. `vulnerability` / `INFRA` / `high` / `real_harm: false`

summary_es: |
  **El 19 de octubre de 2026, Pillar Security divulgó una falla crítica de **ejecución remota de código** en el agente de codificación **OpenCode**: un **servidor MCP controlado por el atacante puede ejecutar código arbitrario en la máquina del desarrollador durante el inicio de sesión OAuth de MCP**, sin interacción ni consentimiento adicionales.** El fallo está en la ruta de lanzamiento del navegador en Windows/WSL — OpenCode pasaba la URL de OAuth a un shell sin entrecomillarla correctamente, de modo que una URL de autorización manipulada (aunque parezca HTTPS) se convierte en un comando (macOS/Linux abren el navegador sin shell y no se ven afectados). Afecta a **OpenCode 1.0.137–1.18.32** y se **corrigió silenciosamente en 1.18.33 (publicada el 28 de septiembre)** — Pillar lo reportó el 29 de agosto; el mantenedor (Anomaly) consideró al principio que un servidor MCP malicioso quedaba fuera de su modelo de amenazas. Sobre todo, no hay **ni CVE ni aviso de seguridad**, por lo que los escáneres y alertas de dependencias no marcarán las instalaciones afectadas. Pillar lo califica con **CVSS 9.8** y no reporta explotación en la naturaleza. Esto es **distinto** de la [compromisión de claves de OpenCode Console](2026-10-17-opencode-console-breach-api-keys.md) divulgada la misma semana. `vulnerability` / `INFRA` / `high` / `real_harm: false`

sources:
  - url: https://www.pillar.security/blog/open-and-shut-remote-code-execution-in-opencode-via-mcp-oauth
    label: Pillar Security (discoverer)
  - url: https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html
    label: The Hacker News
  - url: https://www.infosecurity-magazine.com/news/opencode-quietly-patched-critical/
    label: Infosecurity Magazine
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.32"
---

# OpenCode: a malicious MCP server runs code on the developer's machine during OAuth sign-in

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: vulnerability](https://img.shields.io/badge/kind-vulnerability-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-8F6A3C?style=flat-square)

## Summary

**On 19 October 2026 Pillar Security disclosed a critical remote code execution flaw in the OpenCode coding agent: an attacker-controlled MCP server can run arbitrary code on the developer's machine during the MCP OAuth sign-in, with no extra user interaction or consent.** The bug is in the Windows/WSL browser-launch path — OpenCode passed the OAuth URL through a shell without proper quoting, so a crafted (even HTTPS-looking) authorization URL becomes a command (macOS/Linux launch the browser without a shell and are not affected). It affects OpenCode 1.0.137–1.18.32 and was silently fixed in 1.18.33 (shipped 28 September) — Pillar reported it on 29 August, and the maintainer (Anomaly) initially considered a malicious MCP server outside its threat model. Crucially there is no CVE and no security advisory, so scanners and dependency alerts will not flag affected installs. Pillar rates it CVSS 9.8 and reports no in-the-wild exploitation. This is separate from the [OpenCode Console key breach](2026-10-17-opencode-console-breach-api-keys.md) disclosed the same week. Recorded `vulnerability` / `INFRA` / `high` / `real_harm: false`.

## Attack chain

```mermaid
flowchart LR
    E["Developer connects OpenCode to an attacker-<br/>controlled remote MCP server (Windows/WSL)"]:::entry
    S1["MCP OAuth sign-in: OpenCode passes the<br/>authorization URL to a shell without quoting"]:::step
    S2["Crafted (HTTPS-looking) URL is parsed as a<br/>command — no extra consent needed"]:::step
    I["Arbitrary code runs on the developer's machine"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**The flaw.** On **19 October 2026**, Pillar Security (researcher Eilon Cohen) published *"Open and Shut: Remote Code Execution in opencode via MCP OAuth."* When a developer connects the **OpenCode** coding agent to a remote **MCP server**, the OAuth sign-in flow opens an authorization URL in the browser. On **Windows and WSL**, OpenCode passed that URL **through a shell without proper quoting**, so an attacker-controlled MCP server can return a **crafted authorization URL — even one that looks like a legitimate HTTPS link — that is parsed as a command**, achieving **arbitrary code execution on the developer's machine during the sign-in, with no additional user interaction or consent**. macOS and Linux open the browser without a shell and are not affected.

**Scope, fix and the CVE gap.** It affects **OpenCode 1.0.137–1.18.32** and was fixed in **1.18.33**, which Anomaly shipped on **28 September** — but **silently, as a refactor, with no CVE and no security advisory**. Pillar reported the issue privately on **29 August**; per Pillar, the maintainer initially treated a malicious MCP server as outside its threat model. Because there is no CVE, vulnerability scanners and dependency alerts will not flag affected installs, so defenders must check the OpenCode version directly and upgrade to **1.18.33 or later**. Pillar also notes that URL-scheme checks alone are insufficient; the real fix is quoting the URL correctly (or using argument-based process execution). Pillar proposes a severity of **CVSS 9.8** and reports no sign of in-the-wild exploitation.

**How it is graded.** `vulnerability` — a disclosed flaw, not a used-in-anger incident. `INFRA` (the agent's own runtime/client and its MCP handling is the attack surface). `real_harm: false`: no known exploitation; it was patched before public disclosure. Severity `high` rather than `critical` despite the proposed CVSS 9.8 — this archive's severity reflects **what has happened**, and a severe flaw with no in-the-wild use is `high` here (the same basis as other patched-no-exploitation RCEs); the no-CVE "silent" patch is a notable visibility risk but does not by itself change the realized-harm grade. Confidence `A`: Pillar's own technical write-up plus independent reporting (The Hacker News, Infosecurity Magazine). This is a **different** issue from the OpenCode Console credential breach recorded separately.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Pillar Security (discoverer) | <https://www.pillar.security/blog/open-and-shut-remote-code-execution-in-opencode-via-mcp-oauth> |
| 2 | The Hacker News | <https://thehackernews.com/2026/10/opencode-flaw-lets-malicious-mcp.html> |
| 3 | Infosecurity Magazine | <https://www.infosecurity-magazine.com/news/opencode-quietly-patched-critical/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-19` (raw: 2026-10-19 Pillar Security disclosure; fixed in 1.18.33 on 2026-09-28; reported to vendor 2026-08-29, precision `day`) |
| Kind | Vulnerability disclosure `vulnerability` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) |
| Severity | **High** `high` |
| Confidence | **A** — Pillar Security write-up + The Hacker News + Infosecurity Magazine |
| Real harm | No — patched before disclosure; no known in-the-wild exploitation |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-19-opencode-mcp-oauth-rce` |

<sub>**Why this classification:** A disclosed RCE in the OpenCode coding agent — a malicious MCP server reaches code execution on the developer's host during OAuth sign-in (`INFRA` — the agent's runtime/client and MCP handling). `vulnerability`, not an incident. `real_harm: false` — patched before disclosure, no known exploitation. `high` not `critical`: severity records what has happened, and a severe flaw with no in-the-wild use is `high`; the no-CVE silent patch is a visibility concern, not realized harm. Separate from the OpenCode Console key breach. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure (INFRA)](../../topics/agent-infra.md)

**Related records:**

- `2026-10-17` [OpenCode Console breach exposes users' stored AI-provider API keys](2026-10-17-opencode-console-breach-api-keys.md)<br>  <sub>A separate OpenCode issue disclosed the same week — the hosted Console, not the client</sub>
- `2026-10-02` [Loom for AWS agent-control-plane auth bypass (CVE-2026-103956)](2026-10-02-loom-aws-agent-control-plane-cve-2026-103956.md)<br>  <sub>Another agent-platform/MCP infrastructure flaw</sub>
- `2026-07-31` [Exposed-by-design: MCP servers reachable on the network](../2026-07/2026-07-31-exposed-by-design-mcp-servers.md)<br>  <sub>The broader pattern of MCP as an agent attack surface</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-19-opencode-mcp-oauth-rce.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
