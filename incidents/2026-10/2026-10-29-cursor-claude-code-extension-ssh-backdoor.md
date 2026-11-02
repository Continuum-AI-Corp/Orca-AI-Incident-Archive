---
id: 2026-10-29-cursor-claude-code-extension-ssh-backdoor
title: "A malicious Claude Code extension on Cursor's marketplace planted an SSH backdoor"
title_zh: "Cursor 市场上架的恶意 Claude Code 扩展植入 SSH 后门"
title_ja: "Cursorのマーケットプレイスに出回った悪意あるClaude Code拡張がSSHバックドアを設置"
title_ko: "Cursor 마켓플레이스에 올라온 악성 Claude Code 확장이 SSH 백도어를 심어"
title_de: "Eine bösartige Claude-Code-Erweiterung in Cursors Marketplace setzte eine SSH-Backdoor"
title_fr: "Une extension Claude Code malveillante sur la marketplace de Cursor a installé une porte dérobée SSH"
title_es: "Una extensión maliciosa de Claude Code en la marketplace de Cursor plantó una puerta trasera SSH"
date: 2026-10-29
date_raw: "2026-10-29 (malicious versions live on Cursor marketplace; disclosed 2026-10-29→30)"
date_precision: day

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  **On 29 October 2026, maliciously modified versions (2.1.312 and 2.1.313) of Anthropic's official Claude Code VS Code extension were served from the **Cursor** VS Code Extension Marketplace for roughly 11 hours (≈2:27am–1:35pm PT), exposing up to ~5,000 developers.** A JavaScript loader prepended to `extension.js` **ran automatically when the extension loaded** (no interaction needed): it collected host/user recon (hostname, OS, Git email, public IP, and environment-variable **names** matching `KEY|TOKEN|SECRET|PASS|AWS|GCP`), appended an attacker SSH key (`svc-telemetry`) to `authorized_keys`, tried to open a persistent reverse SSH tunnel to `134.209.82[.]225`, and installed persistence (macOS LaunchAgent / Windows scheduled task). Crucially, **the SSH backdoor largely failed** due to coding errors (a macOS privilege check that misreads its own failure; a Windows path that invokes `/bin/sh`), so remote access "would fail" on most systems; the beacon sent only env-var **names, not secret values**. Cursor says the versions **were not developed by Anthropic**; Anthropic says its own systems were not compromised; the marketplace-publishing vector remains unexplained. No confirmed victims. Recorded `incident` / `SUPPLY` / `high` / `real_harm: false` — a live, in-the-wild marketplace trojanization of a major coding agent's extension, caught within ~11 hours with no confirmed successful compromise.

summary_zh: |
  **2026 年 10 月 29 日，Anthropic 官方 Claude Code VS Code 扩展的被篡改版本（2.1.312 与 2.1.313）在 **Cursor** 的 VS Code 扩展市场上架约 11 小时（约 2:27–13:35 PT），最多暴露约 5,000 名开发者。** 被植入 `extension.js` 开头的 JavaScript loader **在扩展加载时自动执行**（无需交互）：收集主机/用户侦察信息（主机名、OS、Git 邮箱、公网 IP，以及匹配 `KEY|TOKEN|SECRET|PASS|AWS|GCP` 的环境变量**名**），把攻击者 SSH 公钥（`svc-telemetry`）追加进 `authorized_keys`，尝试向 `134.209.82[.]225` 打开持久反向 SSH 隧道，并安装持久化（macOS LaunchAgent／Windows 计划任务）。关键在于，**SSH 后门因代码错误大多失败**（macOS 权限检查误读自身失败；Windows 路径误调 `/bin/sh`），故在多数系统上远程访问"会失败"；beacon 只回传环境变量**名、而非密钥值**。Cursor 称这些版本**并非 Anthropic 开发**；Anthropic 称自身系统未被攻破；上架市场的途径仍未解释。无确认受害者。记为 `incident` / `SUPPLY` / `high` / `real_harm: false`——一次在野、针对主流编码 agent 官方扩展的市场投毒，约 11 小时内被发现、无确认的成功入侵。

summary_ja: |
  **2026年10月29日、Anthropic公式のClaude Code VS Code拡張の改ざん版（2.1.312と2.1.313）が **Cursor** のVS Code拡張マーケットプレイスで約11時間（約2:27–13:35 PT）配信され、最大約5,000人の開発者がさらされた。** `extension.js`の先頭に仕込まれたJavaScriptローダーは**拡張の読み込み時に自動実行**され（操作不要）、ホスト/ユーザー偵察情報（ホスト名、OS、Gitメール、公開IP、`KEY|TOKEN|SECRET|PASS|AWS|GCP`に一致する環境変数**名**）を収集し、攻撃者のSSH鍵（`svc-telemetry`）を`authorized_keys`に追記し、`134.209.82[.]225`への永続的なリバースSSHトンネルを試み、永続化（macOS LaunchAgent／Windowsスケジュールタスク）を設置した。重要なのは、**SSHバックドアはコードの不具合で大半が失敗**し、多くの環境で遠隔アクセスは「失敗する」ことだ。ビーコンは環境変数**名のみ（値は送らない）**。Cursorはこれらが**Anthropic製ではない**とし、Anthropicは自社システムは侵害されていないとする。確認された被害者はいない。`incident` / `SUPPLY` / `high` / `real_harm: false`

summary_ko: |
  **2026년 10월 29일, Anthropic 공식 Claude Code VS Code 확장의 변조판(2.1.312·2.1.313)이 **Cursor**의 VS Code 확장 마켓플레이스에서 약 11시간(약 2:27–13:35 PT) 제공돼 최대 약 5,000명 개발자가 노출됐다.** `extension.js` 앞에 삽입된 자바스크립트 로더가 **확장 로드 시 자동 실행**됐고(상호작용 불필요), 호스트/사용자 정찰 정보(호스트명, OS, Git 이메일, 공인 IP, `KEY|TOKEN|SECRET|PASS|AWS|GCP`에 일치하는 환경 변수 **이름**)를 수집하고, 공격자 SSH 키(`svc-telemetry`)를 `authorized_keys`에 추가하고, `134.209.82[.]225`로 지속적 리버스 SSH 터널을 시도하고, 지속성(macOS LaunchAgent／Windows 예약 작업)을 설치했다. 핵심은 **SSH 백도어가 코드 오류로 대부분 실패**해 대다수 시스템에서 원격 접근이 "실패"했다는 점이며, 비콘은 환경 변수 **이름만(값은 아님)** 전송했다. Cursor는 이 버전이 **Anthropic이 개발한 것이 아니라** 밝혔고, Anthropic은 자사 시스템은 침해되지 않았다고 했다. 확인된 피해자는 없다. `incident` / `SUPPLY` / `high` / `real_harm: false`

summary_de: |
  **Am 29. Oktober 2026 wurden bösartig modifizierte Versionen (2.1.312 und 2.1.313) von Anthropics offizieller Claude-Code-VS-Code-Erweiterung rund 11 Stunden lang (ca. 2:27–13:35 PT) über den **Cursor**-VS-Code-Extension-Marketplace ausgeliefert und setzten bis zu ~5.000 Entwickler dem Risiko aus.** Ein `extension.js` vorangestellter JavaScript-Loader **lief automatisch beim Laden der Erweiterung** (keine Interaktion nötig): Er sammelte Host-/Nutzer-Recon (Hostname, OS, Git-E-Mail, öffentliche IP sowie Umgebungsvariablen-**Namen** passend zu `KEY|TOKEN|SECRET|PASS|AWS|GCP`), hängte einen Angreifer-SSH-Schlüssel (`svc-telemetry`) an `authorized_keys` an, versuchte einen persistenten Reverse-SSH-Tunnel zu `134.209.82[.]225` und richtete Persistenz ein (macOS LaunchAgent / Windows-Task). Entscheidend: **Die SSH-Backdoor scheiterte weitgehend** an Code-Fehlern; der Beacon sendete nur Variablen-**Namen, keine Geheimwerte**. Cursor sagt, die Versionen stammten **nicht von Anthropic**; Anthropic sagt, die eigenen Systeme seien nicht kompromittiert. Keine bestätigten Opfer. `incident` / `SUPPLY` / `high` / `real_harm: false`

summary_fr: |
  **Le 29 octobre 2026, des versions malicieusement modifiées (2.1.312 et 2.1.313) de l'extension officielle Claude Code VS Code d'Anthropic ont été distribuées pendant environ 11 heures (≈2:27–13:35 PT) depuis la marketplace d'extensions VS Code de **Cursor**, exposant jusqu'à ~5 000 développeurs.** Un loader JavaScript ajouté en tête de `extension.js` **s'exécutait automatiquement au chargement de l'extension** (sans interaction) : il collectait de la reconnaissance hôte/utilisateur (nom d'hôte, OS, e-mail Git, IP publique, et **noms** de variables d'environnement correspondant à `KEY|TOKEN|SECRET|PASS|AWS|GCP`), ajoutait une clé SSH d'attaquant (`svc-telemetry`) à `authorized_keys`, tentait un tunnel SSH inverse persistant vers `134.209.82[.]225`, et installait de la persistance (LaunchAgent macOS / tâche planifiée Windows). Point clé : **la porte dérobée SSH a largement échoué** à cause d'erreurs de code ; la balise n'envoyait que les **noms** de variables, pas les valeurs secrètes. Cursor affirme que ces versions **n'ont pas été développées par Anthropic** ; Anthropic affirme que ses propres systèmes n'ont pas été compromis. Aucune victime confirmée. `incident` / `SUPPLY` / `high` / `real_harm: false`

summary_es: |
  **El 29 de octubre de 2026, versiones maliciosamente modificadas (2.1.312 y 2.1.313) de la extensión oficial Claude Code VS Code de Anthropic se sirvieron durante unas 11 horas (≈2:27–13:35 PT) desde la marketplace de extensiones VS Code de **Cursor**, exponiendo hasta ~5.000 desarrolladores.** Un loader de JavaScript antepuesto a `extension.js` **se ejecutaba automáticamente al cargar la extensión** (sin interacción): recopilaba reconocimiento de host/usuario (hostname, SO, correo de Git, IP pública y **nombres** de variables de entorno que coincidían con `KEY|TOKEN|SECRET|PASS|AWS|GCP`), añadía una clave SSH del atacante (`svc-telemetry`) a `authorized_keys`, intentaba un túnel SSH inverso persistente a `134.209.82[.]225` e instalaba persistencia (LaunchAgent de macOS / tarea programada de Windows). Clave: **la puerta trasera SSH falló en gran medida** por errores de código; la baliza solo enviaba **nombres** de variables, no los valores secretos. Cursor dice que esas versiones **no las desarrolló Anthropic**; Anthropic dice que sus propios sistemas no fueron comprometidos. Sin víctimas confirmadas. `incident` / `SUPPLY` / `high` / `real_harm: false`

sources:
  - url: https://cursor.com/blog/claude-code-extension-security-notice
    label: Cursor (official security notice)
  - url: https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/
    label: BleepingComputer
  - url: https://phorion.io/blog/offical-claude-code-vsx-compromise/
    label: Phorion (technical advisory)
disputed: false
landmark: false
scan_month: 2026-10
scan_ref: "SCAN.md §13.35"
---

# A malicious Claude Code extension on Cursor's marketplace planted an SSH backdoor

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-8F6A3C?style=flat-square)

## Summary

**On 29 October 2026, maliciously modified versions (2.1.312 and 2.1.313) of Anthropic's official Claude Code VS Code extension were served from the Cursor VS Code Extension Marketplace for roughly 11 hours (≈2:27am–1:35pm PT), exposing up to ~5,000 developers.** A JavaScript loader prepended to `extension.js` ran automatically when the extension loaded (no interaction needed): it collected host/user recon (hostname, OS, Git email, public IP, and environment-variable names matching `KEY|TOKEN|SECRET|PASS|AWS|GCP`), appended an attacker SSH key (`svc-telemetry`) to `authorized_keys`, tried to open a persistent reverse SSH tunnel to `134.209.82[.]225`, and installed persistence (macOS LaunchAgent / Windows scheduled task). Crucially, the SSH backdoor largely failed due to coding errors (a macOS privilege check that misreads its own failure; a Windows path that invokes `/bin/sh`), so remote access "would fail" on most systems; the beacon sent only env-var names, not secret values. Cursor says the versions were not developed by Anthropic; Anthropic says its own systems were not compromised; the marketplace-publishing vector remains unexplained. No confirmed victims. Recorded `incident` / `SUPPLY` / `high` / `real_harm: false` — a live, in-the-wild marketplace trojanization of a major coding agent's extension, caught within ~11 hours with no confirmed successful compromise.

## Attack chain

```mermaid
flowchart LR
    E["Tampered Claude Code extension<br/>(2.1.312/2.1.313) on Cursor marketplace<br/>~11h on Oct 29"]:::entry
    S1["Loader in extension.js runs on load<br/>(no user interaction)"]:::step
    S2["Appends attacker SSH key; attempts reverse<br/>tunnel + persistence; beacons recon"]:::step
    I["SSH backdoor mostly fails (code bugs);<br/>beacon sends env-var NAMES only; no confirmed victims"]:::impact
    E --> S1 --> S2 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Details

**What happened.** On **29 October 2026**, Cursor published a security notice: maliciously modified versions **2.1.312 and 2.1.313** of **Anthropic's official Claude Code VS Code extension** (`Anthropic.claude-code`) were available on the **Cursor VS Code Extension Marketplace** between about **2:27am and 1:35pm PT** that day. BleepingComputer (30 Oct) reported the window exposed **up to ~5,000 developers**. The researchers Phorion (Calum Hall) and OpenSourceMalware analyzed the payload; all three accounts agree on the indicators.

**The payload.** A malicious JavaScript loader was prepended to the extension's `extension.js`, with the legitimate code otherwise unchanged. Per Cursor and Phorion, it **executes when the extension loads — no user interaction with Claude Code is required** — and then:
- **Recon beacon:** collects hostname, username, OS, architecture, home/working directories, configured Git email, and public IP (via `ifconfig.me` / `api.ipify.org`), plus up to 40 environment-variable **names** matching `/KEY|TOKEN|SECRET|PASS|AWS|GCP/i`. Phorion is explicit: *"the beacon doesn't exfiltrate the secret values themselves."* It POSTs to `/beacon` on `134.209.82[.]225:8099`.
- **SSH key + tunnel:** appends an attacker Ed25519 public key labeled **`svc-telemetry`** to `~/.ssh/authorized_keys`, enables the SSH service, and attempts a persistent reverse SSH tunnel (`-R *:0:localhost:22`) to `134.209.82[.]225` as user `tunnel`, retrying ~every 60s.
- **Persistence:** macOS LaunchAgent (`com.apple.sysmond`), Windows scheduled task (`SysMon`, trying to run as SYSTEM) with a Startup-script fallback, or a Linux `@reboot` cron entry.

**Why the backdoor mostly failed.** Both Cursor and Phorion stress the SSH takeover largely did **not** work. On **macOS**, the code runs `systemsetup -getremotelogin` without privileges; the permission error is misread, so it *"treats 'I don't have permission to check if SSH is off' as 'SSH is already on'"* and skips enabling it — and on standard accounts `sudo -n systemsetup -setremotelogin on` fails anyway. On **Windows**, the service-setup command is passed through a helper that hardcodes `/bin/sh`, absent on standard Windows. Cursor: *"Outside of highly unusual circumstances where Cursor was started with administrator privileges, due to errors in the malicious code, this step would fail."* The SSH **key and persistence scripts can still land, and recon still beacons**, so Cursor advises checking for the `svc-telemetry` key and following remediation regardless.

**Attribution and open questions.** Cursor states the malicious versions **were not developed by Anthropic** and that it found **no evidence other extensions or the official distribution were affected**; it rotated keys, rebuilt the marketplace, and worked with the hosting provider to take the attacker server offline. Anthropic (per earlier coverage) said this was **not a compromise of Anthropic's systems or employee laptops**. Neither company has explained **how the tampered package was published under Anthropic's name** on Cursor's marketplace. Initial reports of npm / Open VSX / Microsoft VS Code Marketplace involvement were **not** borne out — Cursor was the only distribution source.

**How it is graded.** `incident` — a real, in-the-wild malicious package served to real users, not a PoC or a disclosed-but-unexploited flaw. `SUPPLY` — a software-supply-chain / marketplace compromise: a trojanized build of a widely-used coding agent's official extension. `real_harm: false`: despite live exposure of up to ~5,000 developers, the SSH backdoor largely failed by design error, the beacon exfiltrated only env-var **names** (not secret values), and **no victim is confirmed compromised**; it was caught within ~11 hours. Severity `high` nonetheless: a live, auto-executing trojan impersonating the official extension of a leading coding agent, with working persistence and an attacker key install, is a serious supply-chain event even with a buggy payload. Confidence `A`: Cursor's own notice + BleepingComputer + Phorion/OpenSourceMalware, with a consistent IOC set.

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Cursor (official security notice) | <https://cursor.com/blog/claude-code-extension-security-notice> |
| 2 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/malicious-claude-code-extension-on-cursor-planted-ssh-backdoors/> |
| 3 | Phorion (technical advisory) | <https://phorion.io/blog/offical-claude-code-vsx-compromise/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-10-29` (raw: 2026-10-29 malicious versions live on Cursor marketplace; disclosed 2026-10-29→30, precision `day`) |
| Kind | Real incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) |
| Severity | **High** `high` |
| Confidence | **A** — Cursor security notice + BleepingComputer + Phorion/OpenSourceMalware |
| Real harm | No — backdoor largely failed (code bugs), beacon sent env-var names not values, no confirmed victim; caught in ~11 hours |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-10-29-cursor-claude-code-extension-ssh-backdoor` |

<sub>**Why this classification:** A trojanized build of a leading coding agent's official extension (`Anthropic.claude-code` 2.1.312/2.1.313) was served from Cursor's marketplace for ~11 hours and auto-executed an SSH-backdoor + persistence + recon payload (`SUPPLY`). `incident` because it was live and in-the-wild, but `real_harm: false` because the backdoor largely failed by coding error, the beacon leaked only env-var names (not values), and no victim is confirmed compromised. `high` for the seriousness of a live official-extension impersonation with working persistence; the marketplace-publishing vector is unexplained. Grading criteria: [severity.md](../../taxonomy/severity.md) and [confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply chain](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-07-13` [Poisoned Amazon Q VS Code extension shipped a data-wiping prompt](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Another malicious build of an AI coding tool's official IDE extension</sub>
- `2026-10-30` ["Black October": a coordinated wave breached at least nine AI developer platforms](2026-10-30-black-october-ai-developer-platform-breaches.md)<br>  <sub>Same month, the broader wave of attacks on AI developer tooling</sub>
- `2026-08-04` [CHAINDROP: npm supply-chain compromise targeting agent tooling](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>Another supply-chain trojanization in the agent ecosystem</sub>

---

[← 2026-10 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-10/2026-10-29-cursor-claude-code-extension-ssh-backdoor.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
