---
id: 2026-02-19-openclaw-wei-ruan-pu-tong
title: "Microsoft: don't run OpenClaw on ordinary work machines"
title_zh: "微软：不要在普通办公机上运行 OpenClaw"
title_ja: "Microsoft：通常の業務マシンでOpenClawを実行しないこと"
title_ko: "마이크로소프트: 일반 업무용 머신에서 OpenClaw를 실행하지 말 것"
title_de: "Microsoft: OpenClaw nicht auf normalen Arbeitsrechnern ausführen"
title_fr: "Microsoft : ne faites pas tourner OpenClaw sur des machines de travail ordinaires"
title_es: "Microsoft: no ejecutes OpenClaw en máquinas de trabajo comunes"
date: 2026-02-19
date_precision: day
date_raw: "2026-02-19"

kind: policy
type: [GOV]
severity: info
confidence: A
real_harm: null
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Microsoft's security blog formally recommends treating OpenClaw as **untrusted code execution with persistent credentials**, and states plainly: "**running it on a standard personal or enterprise workstation is not appropriate.**" The reasoning: it has limited built-in security controls, yet it can ingest untrusted text, download and execute code from outside and act with the credentials it has been granted — **the execution boundary has moved from static application code to dynamically supplied content, and the supporting controls have not kept up**. Three classes of risk are listed: exfiltration of credentials and accessible data, the agent's persistent state being rewritten so that it takes orders from an attacker, and the host environment falling because the agent fetches and executes malicious code. If it must be evaluated, do so in a fully isolated dedicated VM or on a separate physical machine, with dedicated non-privileged credentials, touching only non-sensitive data, with continuous monitoring plus a rebuild plan.
  💡 **A mainstream vendor publicly discouraging the use of a popular tool on work devices — the only such case in this archive**


summary_zh: |
  Microsoft 安全博客正式建议把 OpenClaw 视为「**带持久凭据的不可信代码执行**」，并明确写道：「**在标准的个人或企业工作站上运行它是不合适的。**」理由是它内置安全控制有限，却能摄入不可信文本、从外部下载并执行代码、用被授予的凭据实施动作 —— **执行边界从静态应用代码转移到了动态供给的内容，而配套控制没有跟上**。列出三类风险：凭据与可访问数据被外带、agent 的持久状态被改写从而听命于攻击者、宿主环境因 agent 取回并执行恶意代码而失陷。若必须评估，须在完全隔离的专用虚拟机或独立物理机上、用专用非特权凭据、只接触非敏感数据，并持续监控 + 准备重建方案
  💡 **一家主流厂商公开劝阻在办公设备上使用一款流行工具，在本档案中是唯一一例**

summary_ja: |
  Microsoftのセキュリティブログは、OpenClawを**永続的な認証情報を伴う信頼できないコード実行**として扱うよう正式に推奨し、「**標準的な個人用または企業用ワークステーションで実行するのは適切ではない**」と明言した。理由：組み込みのセキュリティ制御が限られているのに、信頼できないテキストを取り込み、外部からコードをダウンロードして実行し、付与された認証情報で行動できる——**実行境界が静的なアプリケーションコードから動的に供給されるコンテンツへ移ったのに、それを支える制御が追いついていない**。3種類のリスクが挙げられている：認証情報とアクセス可能なデータの持ち出し、エージェントの永続状態を書き換えられて攻撃者の命令に従うようになること、エージェントが悪性コードを取得・実行してホスト環境が陥落すること。評価が必要な場合は、完全に分離された専用VMまたは別の物理マシンで、専用の非特権認証情報を使い、非機密データのみに触れ、継続的な監視と再構築計画を用意して行うこと。
  💡 **主要ベンダーが人気ツールの業務端末での使用を公に思いとどまらせた——本アーカイブで唯一の事例**

summary_ko: |
  마이크로소프트 보안 블로그는 OpenClaw를 **영구 자격 증명을 지닌 신뢰할 수 없는 코드 실행**으로 취급하라고 공식 권고하며, "**일반 개인용 또는 기업용 워크스테이션에서 실행하는 것은 적절하지 않다**"고 명시했다. 근거: 내장된 보안 통제가 제한적인데도 신뢰할 수 없는 텍스트를 입력받고 외부에서 코드를 내려받아 실행하며 부여받은 자격 증명으로 행동할 수 있다 — **실행 경계가 정적 애플리케이션 코드에서 동적으로 공급되는 콘텐츠로 옮겨갔지만 이를 뒷받침하는 통제가 따라가지 못했다**. 제시된 세 가지 위험: 자격 증명과 접근 가능한 데이터의 유출, 에이전트의 영구 상태가 재작성되어 공격자의 명령을 따르게 되는 것, 에이전트가 악성 코드를 가져와 실행해 호스트 환경이 함락되는 것. 평가가 필요하다면 완전히 격리된 전용 VM이나 별도 물리 머신에서 비권한 전용 자격 증명으로 민감하지 않은 데이터만 다루며, 지속적 모니터링과 재구축 계획을 갖추고 하라고 권고한다.
  💡 **주류 벤더가 인기 도구를 업무 기기에서 쓰지 말라고 공개적으로 권고한 사례로, 이 아카이브에서 유일하다**

summary_de: |
  Microsofts Sicherheitsblog empfiehlt ausdrücklich, OpenClaw als **nicht vertrauenswürdige Codeausführung mit persistenten Zugangsdaten** zu behandeln, und stellt unmissverständlich fest: „**der Betrieb auf einer normalen privaten oder betrieblichen Workstation ist nicht angemessen.**“ Begründung: Es habe nur begrenzte eingebaute Sicherheitskontrollen, könne aber nicht vertrauenswürdigen Text aufnehmen, Code von außen herunterladen und ausführen und mit den ihm erteilten Zugangsdaten handeln — **die Ausführungsgrenze habe sich von statischem Anwendungscode auf dynamisch gelieferte Inhalte verschoben, und die begleitenden Kontrollen seien damit nicht Schritt gehalten**. Drei Risikoklassen werden genannt: die Exfiltration von Zugangsdaten und erreichbaren Daten, das Überschreiben des persistenten Zustands des Agenten, sodass er Anweisungen eines Angreifers befolgt, und der Fall der Hostumgebung, weil der Agent bösartigen Code abruft und ausführt. Wenn es geprüft werden muss, dann in einer vollständig isolierten dedizierten VM oder auf einem getrennten physischen Rechner, mit eigenen nicht privilegierten Zugangsdaten, nur mit nicht sensiblen Daten, mit kontinuierlichem Monitoring und einem Wiederaufbauplan.
  💡 **Ein namhafter Anbieter, der öffentlich von der Nutzung eines beliebten Tools auf Arbeitsgeräten abrät — der einzige derartige Fall in diesem Archiv**

summary_fr: |
  Le blog sécurité de Microsoft recommande formellement de traiter OpenClaw comme **du code non fiable exécuté avec des identifiants persistants**, et déclare clairement : « **l'exécuter sur un poste de travail personnel ou d'entreprise standard n'est pas approprié.** » Raisonnement : il a des contrôles de sécurité intégrés limités, mais peut ingérer du texte non fiable, télécharger et exécuter du code venu de l'extérieur et agir avec les identifiants qui lui ont été accordés — **la frontière d'exécution est passée du code applicatif statique à du contenu fourni dynamiquement, et les contrôles de soutien n'ont pas suivi**. Trois classes de risques sont listées : l'exfiltration d'identifiants et de données accessibles, la réécriture de l'état persistant de l'agent pour qu'il obéisse à un attaquant, et la chute de l'environnement hôte parce que l'agent récupère et exécute du code malveillant. S'il faut vraiment l'évaluer, faites-le dans une VM dédiée totalement isolée ou sur une machine physique séparée, avec des identifiants dédiés non privilégiés, en ne touchant que des données non sensibles, avec une surveillance continue et un plan de reconstruction.
  💡 **Un fournisseur grand public qui déconseille publiquement l'usage d'un outil populaire sur les appareils de travail — le seul cas de ce genre dans cette archive**

summary_es: |
  El blog de seguridad de Microsoft recomienda formalmente tratar OpenClaw como **ejecución de código no confiable con credenciales persistentes**, y afirma sin rodeos: "**ejecutarlo en una estación de trabajo personal o empresarial estándar no es apropiado.**" El razonamiento: tiene controles de seguridad integrados limitados, pero puede ingerir texto no confiable, descargar y ejecutar código del exterior y actuar con las credenciales que se le hayan concedido — **la frontera de ejecución se ha trasladado del código estático de la aplicación al contenido suministrado dinámicamente, y los controles de apoyo no han seguido el ritmo**. Se enumeran tres clases de riesgo: exfiltración de credenciales y datos accesibles, la reescritura del estado persistente del agente para que obedezca a un atacante, y la caída del entorno anfitrión porque el agente descarga y ejecuta código malicioso. Si hay que evaluarlo, hazlo en una VM dedicada totalmente aislada o en una máquina física separada, con credenciales dedicadas sin privilegios, tocando solo datos no sensibles, con monitoreo continuo y un plan de reconstrucción.
  💡 **Un proveedor convencional desaconsejando públicamente el uso de una herramienta popular en dispositivos de trabajo — el único caso de este tipo en este archivo**

sources:
  - url: https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/
    label: Microsoft Security Blog

disputed: false
landmark: true
scan_month: 2026-02
scan_ref: "SCAN.md §6 2026-02"
---

# Microsoft: don't run OpenClaw on ordinary work machines

![severity: info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: n/a](https://img.shields.io/badge/real_harm-n%2Fa-9AA8AD?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: policy](https://img.shields.io/badge/kind-policy-48545A?style=flat-square) ![type: GOV](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

## Summary

Microsoft's security blog formally recommends treating OpenClaw as **untrusted code execution with persistent credentials**, and states plainly: "**running it on a standard personal or enterprise workstation is not appropriate.**" The reasoning: it has limited built-in security controls, yet it can ingest untrusted text, download and execute code from outside and act with the credentials it has been granted — **the execution boundary has moved from static application code to dynamically supplied content, and the supporting controls have not kept up**. Three classes of risk are listed: exfiltration of credentials and accessible data, the agent's persistent state being rewritten so that it takes orders from an attacker, and the host environment falling because the agent fetches and executes malicious code. If it must be evaluated, do so in a fully isolated dedicated VM or on a separate physical machine, with dedicated non-privileged credentials, touching only non-sensitive data, with continuous monitoring plus a rebuild plan.

💡 **A mainstream vendor publicly discouraging the use of a popular tool on work devices — the only such case in this archive**

## Attack chain

```mermaid
flowchart LR
    E["Regulatory or policy action"]:::entry
    S0["Falls on vendors and users"]:::step
    I["Compliance requirements change"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Microsoft Security Blog | <https://www.microsoft.com/en-us/security/blog/2026/02/19/running-openclaw-safely-identity-isolation-runtime-risk/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-02-19` (raw: 2026-02-19, precision `day`) |
| Kind | Policy & regulation `policy` |
| Type | [`GOV`](../../taxonomy/types.md#gov) Governance & policy |
| Severity | **Info** `info` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | n/a |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-02-19-openclaw-wei-ruan-pu-tong` |

<sub>**Why this classification:** Policy / regulatory action, not counted in incident statistics; `severity` is recorded as `info`. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Defense & governance](../../topics/defense.md)

**Related records:**

- `2026-02-05` [GPT-5.3-Codex rated "High" for cyber capability](2026-02-05-gpt-codex-high.md)<br>  <sub>GPT-5.3-Codex rated "High" for cyber capability</sub>
- `2026-02-05` [Claude Opus 4.6 finds 500+ zero-days in open-source projects](2026-02-05-claude-opus-kai-yuan-xiang.md)<br>  <sub>Claude Opus 4.6 finds 500+ zero-days in open-source projects</sub>
- `2026-02-13` [ChatGPT introduces Lockdown Mode](2026-02-13-chatgpt-lockdown-mode.md)<br>  <sub>ChatGPT introduces Lockdown Mode</sub>
- `2026-02-18` [Anthropic, "Measuring AI agent autonomy in practice"](2026-02-18-anthropic-measuring-agent-autonomy.md)<br>  <sub>Anthropic, "Measuring AI agent autonomy in practice"</sub>

---

[← 2026-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-02/2026-02-19-openclaw-wei-ruan-pu-tong.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
