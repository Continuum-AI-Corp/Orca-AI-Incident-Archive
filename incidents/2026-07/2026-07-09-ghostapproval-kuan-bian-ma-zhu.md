---
id: 2026-07-09-ghostapproval-kuan-bian-ma-zhu
title: "GhostApproval: an approval bypass shared by six AI coding assistants"
title_zh: "GhostApproval：6 款 AI 编码助手共有的审批绕过"
title_ja: "GhostApproval：6つのAIコーディングアシスタントが共有する承認バイパス"
title_ko: "GhostApproval: AI 코딩 어시스턴트 여섯 곳이 공유한 승인 우회"
title_de: "GhostApproval: eine von sechs KI-Coding-Assistenten geteilte Umgehung der Genehmigung"
title_fr: "GhostApproval : un contournement d'approbation partagé par six assistants de code IA"
title_es: "GhostApproval: una omisión de aprobación compartida por seis asistentes de código con IA"
date: 2026-07-09
date_precision: day
date_raw: "2026-07-09"

kind: research
type: [SANDBOX]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Wiz: affects Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity and Windsurf. A malicious repository's symlink (CWE-61) does not validate the resolved target, allowing writes to `~/.ssh/authorized_keys`. **The AI's internal reasoning already identifies the dangerous target, but the confirmation dialog shows only the original file name (CWE-451), turning consent into a formality**; Windsurf even finishes writing before the button appears, and Augment reads and writes across the boundary with no confirmation at all.
  **Vendors diverged in response (worth recording separately)**: AWS assigned CVE-2026-12958 (language server 1.69.0), Cursor assigned CVE-2026-50549 (3.0), Google fixed it in 1.19.6; **Anthropic considers that the user already trusted the directory at launch and approved the prompt, so this does not fall under the current threat model and will not be handled as a vulnerability**, but says a symlink warning shipped in **v2.1.32 on 2026-02-05** (9 days before Wiz submitted its report), and that current versions 2.1.173+ resolve symlinks and warn before writing to sensitive files


summary_zh: |
  Wiz：影响 Amazon Q Developer、Claude Code、Augment、Cursor、Google Antigravity、Windsurf。恶意仓库的符号链接（CWE-61）未验证解析目标，可写入 `~/.ssh/authorized_keys`。**AI 内部推理已识别出危险目标，但确认对话框只显示原始文件名（CWE-451），同意变成走过场**；Windsurf 甚至在按钮出现前就写完了，Augment 无确认即越界读写。
  **厂商反应分歧（值得单独记录）**：AWS 编 CVE-2026-12958（language server 1.69.0）、Cursor 编 CVE-2026-50549（3.0）、Google 修 1.19.6；**Anthropic 认为用户既已在启动时信任目录并批准提示，不属现行威胁模型，不作为漏洞处理**，但称符号链接警告已在 **2026-02-05 的 v2.1.32** 出货（比 Wiz 提交报告早 9 天），现行版 2.1.173+ 会解析符号链接并在写入敏感文件前告警

summary_ja: |
  Wiz：Amazon Q Developer、Claude Code、Augment、Cursor、Google Antigravity、Windsurfに影響。悪性リポジトリのシンボリックリンク（CWE-61）が解決先のターゲットを検証せず、`~/.ssh/authorized_keys`への書き込みを可能にする。**AIの内部推論はすでに危険なターゲットを特定しているのに、確認ダイアログには元のファイル名しか表示されない（CWE-451）ため、同意が形骸化する**。Windsurfはボタンが表示される前に書き込みが完了し、Augmentは確認なしに境界を越えて読み書きする。
  **ベンダーの対応は分かれた（個別に記録する価値がある）**：AWSはCVE-2026-12958（language server 1.69.0）、CursorはCVE-2026-50549（3.0）を割り当て、Googleは1.19.6で修正。**Anthropicは、ユーザーが起動時にディレクトリを信頼しプロンプトを承認済みであるとして、これは現在の脅威モデルに該当せず脆弱性として扱わない**としているが、**2026-02-05のv2.1.32**でシンボリックリンク警告を出荷した（Wizの報告提出の9日前）と述べ、現行の2.1.173以降はシンボリックリンクを解決し機密ファイルへの書き込み前に警告するとしている

summary_ko: |
  Wiz: Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity, Windsurf가 영향을 받는다. 악성 저장소의 심볼릭 링크(CWE-61)가 해석된 대상을 검증하지 않아 `~/.ssh/authorized_keys`에 쓸 수 있다. **AI의 내부 추론은 이미 위험한 대상을 식별하지만 확인 대화상자는 원래 파일 이름만 보여주므로(CWE-451) 동의가 형식적인 절차로 전락한다**. Windsurf는 버튼이 나타나기도 전에 쓰기를 끝내고, Augment는 확인 없이 경계를 넘나들며 읽고 쓴다.
  **벤더 대응은 갈렸다(따로 기록할 가치가 있다)**: AWS는 CVE-2026-12958(언어 서버 1.69.0), Cursor는 CVE-2026-50549(3.0), Google은 1.19.6을 부여하거나 수정했다. **Anthropic은 사용자가 이미 실행 시점에 디렉터리를 신뢰하고 프롬프트를 승인했으므로 현재 위협 모델에 해당하지 않아 취약점으로 처리하지 않는다**고 밝혔지만, **2026-02-05 v2.1.32**(Wiz가 보고서를 제출하기 9일 전)에 심볼릭 링크 경고를 배포했고 현재 버전 2.1.173+는 심볼릭 링크를 해석하고 민감 파일 쓰기 전에 경고한다고 말했다

summary_de: |
  Wiz: Betrifft Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity und Windsurf. Der Symlink eines bösartigen Repositorys (CWE-61) validiert das aufgelöste Ziel nicht und erlaubt so Schreibzugriffe auf `~/.ssh/authorized_keys`. **Die interne Argumentation der KI identifiziert das gefährliche Ziel bereits, doch der Bestätigungsdialog zeigt nur den ursprünglichen Dateinamen (CWE-451), wodurch die Zustimmung zur Formalie wird**; Windsurf schreibt sogar fertig, bevor der Button erscheint, und Augment liest und schreibt über die Grenze hinweg ganz ohne Bestätigung.
  **Die Anbieter reagierten unterschiedlich (separat zu erfassen)**: AWS vergab CVE-2026-12958 (Language Server 1.69.0), Cursor vergab CVE-2026-50549 (3.0), Google behob es in 1.19.6; **Anthropic ist der Auffassung, der Nutzer habe dem Verzeichnis beim Start bereits vertraut und den Dialog genehmigt, weshalb dies nicht unter das aktuelle Bedrohungsmodell falle und nicht als Schwachstelle behandelt werde**, verweist aber darauf, dass eine Symlink-Warnung in **v2.1.32 am 2026-02-05** ausgeliefert wurde (9 Tage bevor Wiz seinen Bericht einreichte), und dass aktuelle Versionen 2.1.173+ Symlinks auflösen und vor dem Schreiben in sensible Dateien warnen

summary_fr: |
  Wiz : affecte Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity et Windsurf. Le lien symbolique d'un dépôt malveillant (CWE-61) ne valide pas la cible résolue, permettant d'écrire dans `~/.ssh/authorized_keys`. **Le raisonnement interne de l'IA identifie déjà la cible dangereuse, mais la boîte de confirmation n'affiche que le nom de fichier d'origine (CWE-451), réduisant le consentement à une formalité** ; Windsurf termine même l'écriture avant que le bouton n'apparaisse, et Augment lit et écrit à travers la frontière sans aucune confirmation.
  **Les fournisseurs ont divergé dans leur réponse (à consigner séparément)** : AWS a attribué CVE-2026-12958 (language server 1.69.0), Cursor CVE-2026-50549 (3.0), Google l'a corrigé en 1.19.6 ; **Anthropic estime que l'utilisateur avait déjà fait confiance au répertoire au lancement et approuvé le prompt, donc cela ne relève pas de son modèle de menace actuel et ne sera pas traité comme une vulnérabilité**, mais indique qu'un avertissement sur les liens symboliques a été livré dans la **v2.1.32 le 2026-02-05** (9 jours avant que Wiz ne soumette son rapport), et que les versions actuelles 2.1.173+ résolvent les liens symboliques et avertissent avant d'écrire dans des fichiers sensibles

summary_es: |
  Wiz: afecta a Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity y Windsurf. El enlace simbólico de un repositorio malicioso (CWE-61) no valida el destino resuelto, permitiendo escrituras en `~/.ssh/authorized_keys`. **El razonamiento interno de la IA ya identifica el destino peligroso, pero el diálogo de confirmación muestra solo el nombre original del archivo (CWE-451), convirtiendo el consentimiento en un trámite**; Windsurf incluso termina de escribir antes de que aparezca el botón, y Augment lee y escribe cruzando la frontera sin confirmación alguna.
  **Los proveedores divergieron en su respuesta (merece registrarse aparte)**: AWS asignó CVE-2026-12958 (language server 1.69.0), Cursor asignó CVE-2026-50549 (3.0), Google lo corrigió en 1.19.6; **Anthropic considera que el usuario ya confió en el directorio al lanzarlo y aprobó el prompt, así que esto no entra en el modelo de amenaza actual y no se tratará como vulnerabilidad**, pero dice que se publicó una advertencia sobre enlaces simbólicos en la **v2.1.32 el 2026-02-05** (9 días antes de que Wiz enviara su informe), y que las versiones actuales 2.1.173+ resuelven los enlaces simbólicos y advierten antes de escribir en archivos sensibles

sources:
  - url: https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants
    label: Wiz

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# GhostApproval: an approval bypass shared by six AI coding assistants

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Wiz: affects Amazon Q Developer, Claude Code, Augment, Cursor, Google Antigravity and Windsurf. A malicious repository's symlink (CWE-61) does not validate the resolved target, allowing writes to `~/.ssh/authorized_keys`. **The AI's internal reasoning already identifies the dangerous target, but the confirmation dialog shows only the original file name (CWE-451), turning consent into a formality**; Windsurf even finishes writing before the button appears, and Augment reads and writes across the boundary with no confirmation at all.

**Vendors diverged in response (worth recording separately)**: AWS assigned CVE-2026-12958 (language server 1.69.0), Cursor assigned CVE-2026-50549 (3.0), Google fixed it in 1.19.6; **Anthropic considers that the user already trusted the directory at launch and approved the prompt, so this does not fall under the current threat model and will not be handled as a vulnerability**, but says a symlink warning shipped in **v2.1.32 on 2026-02-05** (9 days before Wiz submitted its report), and that current versions 2.1.173+ resolve symlinks and warn before writing to sensitive files

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
| 1 | Wiz | <https://www.wiz.io/blog/ghostapproval-a-trust-boundary-gap-in-ai-coding-assistants> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-09` (raw: 2026-07-09, precision `day`) |
| Kind | Research demo `research` |
| Type | [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-09-ghostapproval-kuan-bian-ma-zhu` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-07-01` [DuneSlide: zero-click sandbox escape in Cursor](2026-07-01-duneslide-cursor-ling-dian-ji.md)<br>  <sub>DuneSlide: zero-click sandbox escape in Cursor</sub>
- `2026-07-01` [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](2026-07-01-aws-kiro-rce.md)<br>  <sub>AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)</sub>
- `2026-07-20` [Six sandbox escapes across four coding agents in one week](2026-07-20-agent-yi-nei-kuan-bian.md)<br>  <sub>Six sandbox escapes across four coding agents in one week</sub>
- `2026-07-22` [SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host](2026-07-22-sharedroot-claude-cowork-linux.md)<br>  <sub>SharedRoot: Claude Cowork escapes a Linux VM onto the macOS host</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-09-ghostapproval-kuan-bian-ma-zhu.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
