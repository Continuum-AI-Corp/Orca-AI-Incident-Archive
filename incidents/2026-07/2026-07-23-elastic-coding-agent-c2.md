---
id: 2026-07-23-elastic-coding-agent-c2
title: "Elastic: coding-agent tunnel traffic looks almost exactly like C2 beacons"
title_zh: "Elastic：coding agent 的隧道流量和 C2 签到几乎一模一样"
title_ja: "Elastic：コーディングエージェントのトンネル通信はC2ビーコンとほぼ見分けがつかない"
title_ko: "Elastic: 코딩 에이전트 터널 트래픽이 C2 비컨과 거의 구별되지 않는다"
title_de: "Elastic: Der Tunnelverkehr von Coding-Agenten sieht fast genau aus wie C2-Beacons"
title_fr: "Elastic : le trafic de tunnel des agents de code ressemble presque exactement à des balises C2"
title_es: "Elastic: el tráfico de túneles de los agentes de código se parece casi exactamente a balizas C2"
date: 2026-07-23
date_precision: day
date_raw: "2026-07-23"

kind: research
type: [CRED]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Elastic Security Labs, reviewing endpoint telemetry from 2026-07, saw two independent hunting paths hit the same host on 07-23: **agent-spawned reverse tunnels** (localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **macOS LaunchAgent persistence**, and credentialed HTTP egress — all within the same session window.
  A structural problem: **agentic coding tools inherently combine "everything an attacker needs access to" (private environment variables, credentials, API keys, local config) with "continuous ingestion of untrusted content" (repositories, documents, error messages)**. Elastic's advice is concrete: **do not automatically close this class of alert just because a coding agent appears in the process tree**


summary_zh: |
  Elastic Security Labs 在复盘 2026-07 的端点遥测时，两条独立的狩猎路径在 07-23 命中同一台主机：**由 agent 派生的反向隧道**（localhost.run / lhr.life、Cloudflare Quick Tunnels、ngrok）与 **macOS LaunchAgent 持久化**、以及带凭据的 HTTP 外发，出现在同一个会话窗口内。
  结构性问题：**agentic 编码工具天然同时具备「攻击者需要的一切访问权」（私有环境变量、凭据、API key、本地配置）与「持续摄入不可信内容」（仓库、文档、错误信息）**。Elastic 的建议很具体：**不要因为进程树里出现了 coding agent 就自动关闭这类告警**

summary_ja: |
  Elastic Security Labsが2026-07のエンドポイントテレメトリを精査したところ、07-23に2つの独立したハンティング経路が同じホストに到達した：**エージェントが起動したリバーストンネル**（localhost.run／lhr.life、Cloudflare Quick Tunnels、ngrok）、**macOS LaunchAgentの永続化**、認証情報付きのHTTP外向き通信——すべて同じセッション時間帯に発生していた。
  構造的な問題：**エージェント型コーディングツールは本質的に「攻撃者がアクセスしたいものすべて」（非公開の環境変数、認証情報、APIキー、ローカル設定）と「信頼できないコンテンツの継続的な取り込み」（リポジトリ、文書、エラーメッセージ）を兼ね備えている**。Elasticの助言は具体的である：**プロセスツリーにコーディングエージェントが現れたという理由だけで、この種のアラートを自動クローズしないこと**

summary_ko: |
  Elastic Security Labs가 2026-07 엔드포인트 텔레메트리를 검토하던 중 두 개의 독립적인 헌팅 경로가 07-23 같은 호스트에서 겹치는 것을 확인했다: **에이전트가 생성한 리버스 터널**(localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **macOS LaunchAgent 지속성**, 자격 증명이 실린 HTTP 이그레스가 모두 같은 세션 창에서 발생했다.
  구조적 문제: **에이전틱 코딩 도구는 "공격자가 접근하기를 원하는 모든 것"(비공개 환경 변수, 자격 증명, API 키, 로컬 설정)과 "신뢰할 수 없는 콘텐츠의 지속적 입력"(저장소, 문서, 오류 메시지)을 본질적으로 결합한다**. Elastic의 조언은 구체적이다: **프로세스 트리에 코딩 에이전트가 보인다는 이유만으로 이런 종류의 경보를 자동 종료하지 말 것**

summary_de: |
  Elastic Security Labs untersuchte Endpoint-Telemetrie aus dem 2026-07 und sah am 07-23 zwei unabhängige Hunting-Pfade auf denselben Host treffen: **von Agenten gestartete Reverse Tunnel** (localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **macOS-LaunchAgent-Persistenz** und mit Zugangsdaten versehener HTTP-Egress — alles im selben Sitzungsfenster.
  Ein strukturelles Problem: **Agentische Coding-Tools vereinen von Natur aus „alles, worauf ein Angreifer Zugriff braucht“ (private Umgebungsvariablen, Zugangsdaten, API-Schlüssel, lokale Konfiguration) mit „kontinuierlicher Aufnahme nicht vertrauenswürdiger Inhalte“ (Repositories, Dokumente, Fehlermeldungen)**. Elastic rät konkret: **Diese Art von Alarm nicht automatisch schließen, nur weil ein Coding-Agent im Prozessbaum auftaucht**

summary_fr: |
  Elastic Security Labs, en examinant la télémétrie d'endpoints de 2026-07, a vu deux pistes de chasse indépendantes frapper le même hôte le 07-23 : **des tunnels inverses lancés par l'agent** (localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **une persistance macOS LaunchAgent** et une sortie HTTP avec identifiants — tout dans la même fenêtre de session.
  Un problème structurel : **les outils de code agentiques combinent par nature « tout ce dont un attaquant a besoin d'accéder » (variables d'environnement privées, identifiants, clés API, configuration locale) avec « l'ingestion continue de contenu non fiable » (dépôts, documents, messages d'erreur)**. Le conseil d'Elastic est concret : **ne pas clore automatiquement ce type d'alerte simplement parce qu'un agent de code apparaît dans l'arbre des processus**

summary_es: |
  Elastic Security Labs, revisando la telemetría de endpoints de 2026-07, vio que dos rutas de búsqueda independientes llegaron al mismo host el 07-23: **túneles inversos lanzados por agentes** (localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **persistencia mediante LaunchAgent de macOS** y salida HTTP con credenciales — todo dentro de la misma ventana de sesión.
  Un problema estructural: **las herramientas de código agénticas combinan por naturaleza "todo lo que un atacante necesita para acceder" (variables de entorno privadas, credenciales, claves de API, configuración local) con "la ingesta continua de contenido no confiable" (repositorios, documentos, mensajes de error)**. El consejo de Elastic es concreto: **no cierres automáticamente este tipo de alertas solo porque aparezca un agente de código en el árbol de procesos**

sources:
  - url: https://www.elastic.co/security-labs/coding-agent-launchagent-tunnel-detection
    label: Elastic Security Labs

disputed: false
landmark: true
scan_month: 2026-07
scan_ref: "SCAN.md §6 2026-07"
---

# Elastic: coding-agent tunnel traffic looks almost exactly like C2 beacons

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: CRED](https://img.shields.io/badge/type-CRED-B08528?style=flat-square)

## Summary

Elastic Security Labs, reviewing endpoint telemetry from 2026-07, saw two independent hunting paths hit the same host on 07-23: **agent-spawned reverse tunnels** (localhost.run / lhr.life, Cloudflare Quick Tunnels, ngrok), **macOS LaunchAgent persistence**, and credentialed HTTP egress — all within the same session window.

A structural problem: **agentic coding tools inherently combine "everything an attacker needs access to" (private environment variables, credentials, API keys, local config) with "continuous ingestion of untrusted content" (repositories, documents, error messages)**. Elastic's advice is concrete: **do not automatically close this class of alert just because a coding agent appears in the process tree**

## Attack chain

```mermaid
flowchart LR
    E["Credentials within an agent's reach"]:::entry
    S0["The agent picks them up and calls out"]:::step
    I["Credentials are abused<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Elastic Security Labs | <https://www.elastic.co/security-labs/coding-agent-launchagent-tunnel-detection> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-07-23` (raw: 2026-07-23, precision `day`) |
| Kind | Research demo `research` |
| Type | [`CRED`](../../taxonomy/types.md#cred) Credential abuse |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-07-23-elastic-coding-agent-c2` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Related records:**

- `2026-06-01` [Miasma worm](../2026-06/2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-01` [Attackers simply ask Meta's AI support bot for Instagram accounts](../2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br>  <sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](../2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-08-04` [CHAINDROP npm worm](../2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br>  <sub>CHAINDROP npm worm</sub>

---

[← 2026-07 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-07/2026-07-23-elastic-coding-agent-c2.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
