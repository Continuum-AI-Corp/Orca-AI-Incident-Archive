---
id: 2026-07-22-sharedroot-claude-cowork-linux
title: "SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host"
title_zh: "SharedRoot：Claude Cowork 从 Linux VM 逃到 macOS 宿主"
title_ja: "SharedRoot：Claude CoworkがLinux VMからmacOSホストへ脱出"
title_ko: "SharedRoot: Claude Cowork, Linux VM을 탈출해 macOS 호스트로"
title_de: "SharedRoot: Claude Cowork entkommt aus einer Linux-VM auf den macOS-Host"
title_fr: "SharedRoot : Claude Cowork s'échappe d'une VM Linux vers l'hôte macOS"
title_es: "SharedRoot: Claude Cowork escapa de una VM de Linux al host macOS"
date: 2026-07-22
date_precision: day
date_raw: "2026-07-22"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Found by Accomplish AI. ⚠️ **CVE-2026-46331 is itself a Linux kernel flaw** (the traffic-control `act_pedit` component, "pedit COW": the kernel computes the copy-on-write range before it knows the full extent of a modification, and under certain conditions the write lands on shared page-cache data), **not a Cowork-specific CVE**.
  Exploit chain: an AI agent running inside a Linux VM uses the kernel flaw to get guest root → reaches writable files on the macOS host through a **VirtioFS mount** → **SSH private keys, cloud credentials, browser data** and anything else the logged-in user can reach.
  About **500,000** local macOS Cowork users were potentially affected before Anthropic switched to cloud execution by default. **Anthropic closed the report as "informative" and shipped no patch**; the latest version executes in the cloud by default, sidestepping the local escape path


summary_zh: |
  Accomplish AI 发现。⚠️ **CVE-2026-46331 本身是 Linux 内核漏洞**（traffic-control 的 `act_pedit` 组件，「pedit COW」：内核在知道完整修改范围之前就算好了 copy-on-write 范围，特定条件下写操作会落到共享的 page-cache 数据上），**不是 Cowork 专属 CVE**。
  利用链：跑在 Linux VM 里的 AI agent 利用该内核漏洞拿到 guest root → 经 **VirtioFS 挂载**触达 macOS 宿主上的可写文件 → **SSH 私钥、云凭据、浏览器数据**等登录用户能拿到的一切。
  约 **50 万** macOS 本地 Cowork 用户在 Anthropic 改为默认云端执行前处于潜在受影响状态。**Anthropic 以「informative」关闭了该报告、未发补丁**；最新版默认云端执行，绕开了本地逃逸路径

summary_ja: |
  Accomplish AIが発見。⚠️ **CVE-2026-46331はそれ自体がLinuxカーネルの欠陥**（traffic-controlの`act_pedit`コンポーネント、「pedit COW」：カーネルが変更の全範囲を把握する前にコピーオンライトの範囲を計算し、特定の条件下で書き込みが共有ページキャッシュのデータに及ぶ）であり、**Cowork固有のCVEではない**。
  エクスプロイトチェーン：Linux VM内で動作するAIエージェントがカーネル欠陥でゲストrootを取得→**VirtioFSマウント**を通じてmacOSホスト上の書き込み可能なファイルに到達→**SSH秘密鍵、クラウド認証情報、ブラウザデータ**など、ログインユーザーが到達できるあらゆるもの。
  Anthropicがデフォルトでクラウド実行に切り替える前は、約**50万人**のローカルmacOS Coworkユーザーが潜在的に影響を受けた。**Anthropicは報告を「informative」としてクローズし、パッチを出荷しなかった**。最新版はデフォルトでクラウド実行となり、ローカルの脱出経路を回避している

summary_ko: |
  Accomplish AI가 발견했다. ⚠️ **CVE-2026-46331은 그 자체로 Linux 커널 결함**이며(트래픽 제어 `act_pedit` 구성 요소, "pedit COW": 커널이 수정의 전체 범위를 알기 전에 복사 시점 기록(copy-on-write) 범위를 계산하고 특정 조건에서 쓰기가 공유 페이지 캐시 데이터에 떨어지는 문제), **Cowork 전용 CVE가 아니다**.
  익스플로잇 사슬: Linux VM 안에서 실행되는 AI 에이전트가 커널 결함으로 게스트 root를 획득 → **VirtioFS 마운트**를 통해 macOS 호스트의 쓰기 가능한 파일에 도달 → **SSH 개인 키, 클라우드 자격 증명, 브라우저 데이터** 등 로그인한 사용자가 접근할 수 있는 모든 것.
  Anthropic이 기본적으로 클라우드 실행으로 전환하기 전까지 약 **50만 명**의 로컬 macOS Cowork 사용자가 잠재적 영향을 받았다. **Anthropic은 보고서를 "정보성"으로 종결하고 패치를 배포하지 않았다**. 최신 버전은 기본적으로 클라우드에서 실행되어 로컬 탈출 경로를 우회한다

summary_de: |
  Gefunden von Accomplish AI. ⚠️ **CVE-2026-46331 ist selbst eine Linux-Kernel-Schwachstelle** (die Traffic-Control-Komponente `act_pedit`, „pedit COW“: Der Kernel berechnet den Copy-on-Write-Bereich, bevor er das vollständige Ausmaß einer Änderung kennt, und unter bestimmten Bedingungen landet der Schreibvorgang auf gemeinsamen Page-Cache-Daten), **keine Cowork-spezifische CVE**.
  Exploit-Kette: Ein in einer Linux-VM laufender KI-Agent nutzt die Kernel-Schwachstelle, um Gast-Root zu erlangen → erreicht über einen **VirtioFS-Mount** beschreibbare Dateien auf dem macOS-Host → **private SSH-Schlüssel, Cloud-Zugangsdaten, Browserdaten** und alles andere, worauf der angemeldete Nutzer Zugriff hat.
  Etwa **500,000** lokale macOS-Cowork-Nutzer waren potenziell betroffen, bevor Anthropic standardmäßig auf Cloud-Ausführung umstellte. **Anthropic schloss den Bericht als „informativ“ ab und lieferte keinen Patch**; die neueste Version führt standardmäßig in der Cloud aus und umgeht damit den lokalen Escape-Pfad

summary_fr: |
  Trouvé par Accomplish AI. ⚠️ **CVE-2026-46331 est en soi une faille du noyau Linux** (le composant de contrôle de trafic `act_pedit`, « pedit COW » : le noyau calcule la plage de copy-on-write avant de connaître l'étendue complète d'une modification, et dans certaines conditions l'écriture atterrit sur des données partagées du page-cache), **pas un CVE propre à Cowork**.
  Chaîne d'exploitation : un agent IA tournant dans une VM Linux utilise la faille du noyau pour obtenir root sur l'invité → atteint des fichiers inscriptibles de l'hôte macOS via un **montage VirtioFS** → **clés privées SSH, identifiants cloud, données de navigateur** et tout ce que l'utilisateur connecté peut atteindre.
  Environ **500 000** utilisateurs locaux de Cowork sur macOS étaient potentiellement concernés avant qu'Anthropic ne passe à l'exécution cloud par défaut. **Anthropic a clos le rapport comme « informatif » sans livrer de correctif** ; la dernière version s'exécute par défaut dans le cloud, contournant le chemin d'évasion local

summary_es: |
  Encontrado por Accomplish AI. ⚠️ **CVE-2026-46331 es en sí un fallo del kernel de Linux** (el componente de control de tráfico `act_pedit`, "pedit COW": el kernel calcula el rango de copy-on-write antes de conocer la extensión completa de una modificación, y bajo ciertas condiciones la escritura recae sobre datos compartidos de la caché de páginas), **no un CVE específico de Cowork**.
  Cadena de explotación: un agente de IA que se ejecuta dentro de una VM de Linux usa el fallo del kernel para obtener root en el invitado → alcanza archivos escribibles del host macOS a través de un **montaje VirtioFS** → **claves privadas SSH, credenciales de nube, datos de navegador** y todo lo que el usuario con sesión iniciada pueda alcanzar.
  Unos **500,000** usuarios locales de Cowork en macOS podrían haberse visto afectados antes de que Anthropic cambiara a ejecución en la nube por defecto. **Anthropic cerró el informe como "informativo" y no publicó ningún parche**; la última versión se ejecuta en la nube por defecto, sorteando la ruta de escape local

sources:
  - url: https://socradar.io/blog/sharedroot-sandbox-escape-claude-cowork/
    label: SOCRadar
  - url: https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-cowork-sharedroot-sandbox-escape-20/
    label: CSA
  - url: https://appleinsider.com/articles/26/07/27/claude-cowork-can-escape-its-sandbox-rummage-through-all-of-your-files
    label: AppleInsider

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Found by Accomplish AI. ⚠️ **CVE-2026-46331 is itself a Linux kernel flaw** (the traffic-control `act_pedit` component, "pedit COW": the kernel computes the copy-on-write range before it knows the full extent of a modification, and under certain conditions the write lands on shared page-cache data), **not a Cowork-specific CVE**.

Exploit chain: an AI agent running inside a Linux VM uses the kernel flaw to get guest root → reaches writable files on the macOS host through a **VirtioFS mount** → **SSH private keys, cloud credentials, browser data** and anything else the logged-in user can reach.

About **500,000** local macOS Cowork users were potentially affected before Anthropic switched to cloud execution by default. **Anthropic closed the report as "informative" and shipped no patch**; the latest version executes in the cloud by default, sidestepping the local escape path

## Attack chain

```mermaid
flowchart LR
    E["Evaluation / container environment"]:::entry
    S0["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | SOCRadar | <https://socradar.io/blog/sharedroot-sandbox-escape-claude-cowork/> |
| 2 | CSA | <https://labs.cloudsecurityalliance.org/research/csa-research-note-claude-cowork-sharedroot-sandbox-escape-20/> |
| 3 | AppleInsider | <https://appleinsider.com/articles/26/07/27/claude-cowork-can-escape-its-sandbox-rummage-through-all-of-your-files> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-22` (raw: 2026-07-22, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-22-sharedroot-claude-cowork-linux` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-09` [GhostApproval: an approval bypass shared by six AI coding assistants](2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)<br>  <sub>GhostApproval: an approval bypass shared by six AI coding assistants</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-20` [Six sandbox escapes across four coding agents in one week](2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-22-sharedroot-claude-cowork-linux.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
