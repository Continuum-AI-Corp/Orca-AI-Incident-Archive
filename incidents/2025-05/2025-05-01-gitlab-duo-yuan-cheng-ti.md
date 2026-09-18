---
id: 2025-05-01-gitlab-duo-yuan-cheng-ti
title: "GitLab Duo remote prompt injection"
title_zh: "GitLab Duo 远程提示注入"
title_ja: "GitLab Duoのリモートプロンプトインジェクション"
title_ko: "GitLab Duo 원격 프롬프트 인젝션"
title_de: "GitLab Duo: Remote-Prompt-Injection"
title_fr: "Injection de prompt à distance dans GitLab Duo"
title_es: "Inyección remota de prompt en GitLab Duo"
date: 2025-05-01
date_precision: month
date_raw: "2025-05"

kind: incident
type: [IPI, EXFIL]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Legit Security: hidden instructions in a merge request can steal private project source code, manipulate the code suggestions other people see, and exfiltrate **an undisclosed zero-day**. Reported 2025-02-12; GitLab confirmed the HTML injection and acknowledged prompt injection as a security issue, and the patch stops Duo from rendering `<img>`/`<form>` that point to domains other than gitlab.com


summary_zh: |
  Legit Security：merge request 中的隐藏指令可窃取私有项目源码、操纵他人看到的代码建议、外带**未披露的零日**。2025-02-12 报告；GitLab 确认 HTML 注入并承认提示注入为安全问题，补丁禁止 Duo 渲染指向 gitlab.com 以外域的 `<img>`/`<form>`

summary_ja: |
  Legit Security：マージリクエストに隠された指示により、非公開プロジェクトのソースコードを窃取し、他のユーザーに見えるコード提案を操作し、**未公開のゼロデイ**を外部送信できた。2025-02-12に報告。GitLabはHTMLインジェクションを確認し、プロンプトインジェクションをセキュリティ問題として認め、パッチはgitlab.com以外のドメインを指す`<img>`/`<form>`をDuoが描画しないようにするもの

summary_ko: |
  Legit Security: 머지 리퀘스트에 숨겨진 지시로 비공개 프로젝트 소스 코드를 탈취하고, 다른 사람이 보는 코드 제안을 조작하며, **공개되지 않은 제로데이**까지 유출할 수 있었다. 2025-02-12에 신고되었고 GitLab은 HTML 인젝션을 확인하고 프롬프트 인젝션을 보안 문제로 인정했다. 패치는 Duo가 gitlab.com이 아닌 도메인을 가리키는 `<img>`/`<form>`을 렌더링하지 못하게 한다

summary_de: |
  Legit Security: Versteckte Anweisungen in einem Merge Request können privaten Projektquellcode stehlen, die Codevorschläge anderer Nutzer manipulieren und **einen nicht offengelegten Zero-Day** exfiltrieren. Gemeldet am 2025-02-12; GitLab bestätigte die HTML-Injection und erkannte Prompt-Injection als Sicherheitsproblem an, und der Patch verhindert, dass Duo `<img>`/`<form>` rendert, die auf andere Domains als gitlab.com zeigen

summary_fr: |
  Legit Security : des instructions cachées dans une merge request peuvent voler le code source privé d'un projet, manipuler les suggestions de code vues par les autres et exfiltrer **un zero-day non divulgué**. Signalé le 2025-02-12 ; GitLab a confirmé l'injection HTML et reconnu l'injection de prompt comme un problème de sécurité, et le correctif empêche Duo de rendre les `<img>`/`<form>` pointant vers des domaines autres que gitlab.com

summary_es: |
  Legit Security: instrucciones ocultas en una merge request pueden robar el código fuente de proyectos privados, manipular las sugerencias de código que ven otras personas y exfiltrar **un zero-day no divulgado**. Reportado el 2025-02-12; GitLab confirmó la inyección de HTML y reconoció la inyección de prompt como un problema de seguridad, y el parche impide que Duo renderice `<img>`/`<form>` que apunten a dominios distintos de gitlab.com

sources:
  - url: https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo
    label: Legit Security
  - url: https://thehackernews.com/2025/05/gitlab-duo-vulnerability-enabled.html
    label: THN

disputed: false
landmark: true
scan_month: 2025-05
scan_ref: "SCAN.md §5 2025-05"
---

# GitLab Duo remote prompt injection

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square) ![type: EXFIL](https://img.shields.io/badge/type-EXFIL-B08528?style=flat-square)

## Summary

Legit Security: hidden instructions in a merge request can steal private project source code, manipulate the code suggestions other people see, and exfiltrate **an undisclosed zero-day**. Reported 2025-02-12; GitLab confirmed the HTML injection and acknowledged prompt injection as a security issue, and the patch stops Duo from rendering `<img>`/`<form>` that point to domains other than gitlab.com

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    S1["Exfiltration via the vendor's trusted domain<br/>image rendering · API · proxy"]:::step
    I["Data ends up with the attacker"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Legit Security | <https://www.legitsecurity.com/blog/remote-prompt-injection-in-gitlab-duo> |
| 2 | THN | <https://thehackernews.com/2025/05/gitlab-duo-vulnerability-enabled.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-05-01` (raw: 2025-05, precision `month`) |
| Kind | Incident `incident` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection · [`EXFIL`](../../taxonomy/types.md#exfil) Data exfiltration |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-05-01-gitlab-duo-yuan-cheng-ti` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2025-05-26` [GitHub MCP "Toxic Agent Flow"](2025-05-26-github-mcp-toxic-agent.md)<br>  <sub>GitHub MCP "toxic agent flow"</sub>
- `2025-06-11` [EchoLeak (CVE-2025-32711)](../2025-06/2025-06-11-echoleak.md)<br>  <sub>EchoLeak (CVE-2025-32711)</sub>
- `2025-08-06` [AgentFlayer zero-click attack set (Black Hat USA)](../2025-08/2025-08-06-agentflayer-black-hat-usa.md)<br>  <sub>AgentFlayer zero-click attack set (Black Hat USA)</sub>
- `2025-08-06` [SafeBreach "Invitation Is All You Need"](../2025-08/2025-08-06-safebreach-invitation-is-all.md)<br>  <sub>SafeBreach "Invitation Is All You Need"</sub>

---

[← 2025-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-05/2025-05-01-gitlab-duo-yuan-cheng-ti.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
