---
id: 2026-08-26-gitlab-duo-claude-agent
title: "GitLab Duo's Claude agent can run arbitrary commands in CI"
title_zh: "GitLab Duo 的 Claude agent 可在 CI 中执行任意命令"
title_ja: "GitLab DuoのClaudeエージェントがCIで任意コマンドを実行可能"
title_ko: "GitLab Duo의 Claude 에이전트, CI에서 임의 명령 실행 가능"
title_de: "Der Claude-Agent von GitLab Duo kann beliebige Befehle in der CI ausführen"
title_fr: "L'agent Claude de GitLab Duo peut exécuter des commandes arbitraires dans la CI"
title_es: "El agente Claude de GitLab Duo puede ejecutar comandos arbitrarios en el CI"
date: 2026-08-26
date_precision: day
date_raw: "2026-08-26"

kind: research
type: [INFRA]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  CVE-2026-18252, **CVSS 7.3**. The Claude agent's configuration parameters were taken straight from user-controlled input without sanitisation, so **an authenticated user with the developer role** could inject a payload and run arbitrary commands in the CI context — and CI pipelines typically hold source code, build artifacts, deployment credentials, cloud tokens and package-repository credentials. Affects GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1, **fixed on 2026-08-26 with 19.3.1 / 19.2.5 / 19.1.7**. Reported via HackerOne by researcher thwin_htet; no evidence of in-the-wild exploitation


summary_zh: |
  CVE-2026-18252，**CVSS 7.3**。Claude agent 的配置参数直接取自用户可控输入而未做净化，**具有 developer 角色的已认证用户**即可注入载荷、在 CI 上下文中执行任意命令 —— 而 CI 流水线通常持有源码、构建产物、部署凭据、云令牌与包仓库凭据。影响 GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1，**2026-08-26 随 19.3.1 / 19.2.5 / 19.1.7 修复**。经 HackerOne 由研究者 thwin_htet 报告，无在野利用证据

summary_ja: |
  CVE-2026-18252、**CVSS 7.3**。Claudeエージェントの設定パラメータがサニタイズなしでユーザー制御の入力から直接取得されていたため、**developerロールを持つ認証済みユーザー**がペイロードを注入し、CIコンテキストで任意コマンドを実行できた——CIパイプラインは通常、ソースコード、ビルド成果物、デプロイ認証情報、クラウドトークン、パッケージリポジトリの認証情報を保持している。GitLab EE 18.9〜19.1.7／19.2〜19.2.5／19.3〜19.3.1が対象で、**2026-08-26に19.3.1／19.2.5／19.1.7で修正**。研究者thwin_htet氏がHackerOne経由で報告。実悪用の証拠はない

summary_ko: |
  CVE-2026-18252, **CVSS 7.3**. Claude 에이전트의 구성 매개변수가 정제 없이 사용자 제어 입력에서 그대로 가져와져, **개발자 역할을 가진 인증된 사용자**가 페이로드를 주입해 CI 컨텍스트에서 임의 명령을 실행할 수 있었다. CI 파이프라인은 일반적으로 소스 코드, 빌드 아티팩트, 배포 자격 증명, 클라우드 토큰, 패키지 저장소 자격 증명을 보유한다. GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1이 영향받고 **2026-08-26 19.3.1 / 19.2.5 / 19.1.7로 수정**되었다. 연구자 thwin_htet이 HackerOne을 통해 보고했으며 실제 악용 증거는 없다

summary_de: |
  CVE-2026-18252, **CVSS 7.3**. Die Konfigurationsparameter des Claude-Agenten wurden ohne Bereinigung direkt aus nutzerkontrollierter Eingabe übernommen, sodass **ein authentifizierter Nutzer mit der Rolle Developer** eine Nutzlast einschleusen und im CI-Kontext beliebige Befehle ausführen konnte — und CI-Pipelines enthalten üblicherweise Quellcode, Build-Artefakte, Deployment-Zugangsdaten, Cloud-Token und Zugangsdaten für Paket-Repositories. Betrifft GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1, **behoben am 2026-08-26 mit 19.3.1 / 19.2.5 / 19.1.7**. Über HackerOne vom Forscher thwin_htet gemeldet; keine Hinweise auf Ausnutzung in freier Wildbahn

summary_fr: |
  CVE-2026-18252, **CVSS 7.3**. Les paramètres de configuration de l'agent Claude étaient pris directement dans des entrées contrôlées par l'utilisateur sans sanitisation, si bien **qu'un utilisateur authentifié avec le rôle développeur** pouvait injecter une charge et exécuter des commandes arbitraires dans le contexte de la CI — et les pipelines de CI détiennent typiquement du code source, des artefacts de build, des identifiants de déploiement, des jetons cloud et des identifiants de dépôts de paquets. Affecte GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1, **corrigé le 2026-08-26 avec 19.3.1 / 19.2.5 / 19.1.7**. Signalé via HackerOne par le chercheur thwin_htet ; aucune preuve d'exploitation en conditions réelles

summary_es: |
  CVE-2026-18252, **CVSS 7.3**. Los parámetros de configuración del agente Claude se tomaban directamente de la entrada controlada por el usuario sin sanitización, así que **un usuario autenticado con el rol de desarrollador** podía inyectar una carga útil y ejecutar comandos arbitrarios en el contexto del CI — y las canalizaciones de CI suelen contener código fuente, artefactos de compilación, credenciales de despliegue, tokens de nube y credenciales de repositorios de paquetes. Afecta a GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1, **corregido el 2026-08-26 con 19.3.1 / 19.2.5 / 19.1.7**. Reportado vía HackerOne por el investigador thwin_htet; sin evidencia de explotación en entornos reales

sources:
  - url: https://app.opencve.io/cve/CVE-2026-18252
    label: OpenCVE
  - url: https://cybersecuritynews.com/gitlab-fixes-claude-ai-agent-flaw/
    label: CybersecurityNews

disputed: false
landmark: false
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# GitLab Duo's Claude agent can run arbitrary commands in CI

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: INFRA](https://img.shields.io/badge/type-INFRA-B08528?style=flat-square)

## Summary

CVE-2026-18252, **CVSS 7.3**. The Claude agent's configuration parameters were taken straight from user-controlled input without sanitisation, so **an authenticated user with the developer role** could inject a payload and run arbitrary commands in the CI context — and CI pipelines typically hold source code, build artifacts, deployment credentials, cloud tokens and package-repository credentials. Affects GitLab EE 18.9–19.1.7 / 19.2–19.2.5 / 19.3–19.3.1, **fixed on 2026-08-26 with 19.3.1 / 19.2.5 / 19.1.7**. Reported via HackerOne by researcher thwin_htet; no evidence of in-the-wild exploitation

## Attack chain

```mermaid
flowchart LR
    E["Agent infrastructure exposed to the internet"]:::entry
    S0["Unauthenticated access"]:::step
    I["RCE / data leak<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | OpenCVE | <https://app.opencve.io/cve/CVE-2026-18252> |
| 2 | CybersecurityNews | <https://cybersecuritynews.com/gitlab-fixes-claude-ai-agent-flaw/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-26` (raw: 2026-08-26, precision `day`) |
| Kind | Research demo `research` |
| Type | [`INFRA`](../../taxonomy/types.md#infra) Agent infrastructure exposure |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-26-gitlab-duo-claude-agent` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent infrastructure exposure](../../topics/agent-infra.md)

**Related records:**

- `2026-08-06` [Unauthenticated Langflow RCE added to CISA KEV](2026-08-06-langflow-rce-cisa-kev.md)<br>  <sub>Unauthenticated Langflow RCE added to CISA KEV</sub>
- `2026-08-25` [NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template](2026-08-25-nemoclaw-dns-zhong-bang-ding.md)<br>  <sub>NemoClaw (CVE-2026-65105): DNS rebinding rewrites the model's chat template</sub>
- `2026-08-01` [Azure SRE Agent privilege escalation (CVE-2026-62830)](2026-08-01-azure-sre-agent.md)<br>  <sub>Azure SRE Agent privilege escalation (CVE-2026-62830)</sub>
- `2026-09-02` [Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year](../2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br>  <sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-26-gitlab-duo-claude-agent.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
