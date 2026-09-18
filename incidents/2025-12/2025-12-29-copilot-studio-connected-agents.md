---
id: 2025-12-29-copilot-studio-connected-agents
title: "Copilot Studio \"Connected Agents\" can carry invisible backdoors"
title_zh: "Copilot Studio「Connected Agents」可被植入隐形后门"
title_ja: "Copilot Studioの「Connected Agents」が不可視のバックドアになり得る"
title_ko: "Copilot Studio \"연결된 에이전트\", 보이지 않는 백도어를 품을 수 있다"
title_de: "Copilot Studio „Connected Agents“ können unsichtbare Backdoors tragen"
title_fr: "Les « Connected Agents » de Copilot Studio peuvent porter des backdoors invisibles"
title_es: "Los \"Connected Agents\" de Copilot Studio pueden llevar puertas traseras invisibles"
date: 2025-12-29
date_precision: day
date_raw: "2025-12-29"

kind: research
type: [IPI]
severity: medium
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Zenity Labs: the feature (launched at Build 2025) lets agents share capabilities, and **once enabled it exposes one agent's knowledge, tools and topics to every other agent in the same environment** — and **① it is on by default for all new agents, ② no interface shows who has connected to your agent**. Attackers can use this to impersonate an organization and trigger sensitive operations unnoticed. Zenity's conclusion: "**Always assume that any agent with connected agents enabled is anonymously reachable from the entire internet**"


summary_zh: |
  Zenity Labs：该功能（Build 2025 发布）让 agent 之间共享能力，**开启后会把一个 agent 的知识、工具与主题暴露给同环境下的所有其他 agent**，而且 **① 所有新建 agent 默认开启 ② 没有任何界面能看出谁连了你的 agent**。攻击者可借此冒充组织、在不被察觉的情况下触发敏感操作。Zenity 的结论是：「**要始终假设任何启用了 connected agents 的 agent 都能被整个互联网匿名访问**」

summary_ja: |
  Zenity Labs：この機能（Build 2025で開始）はエージェント間で機能を共有できるようにするが、**一度有効にすると、あるエージェントのナレッジ、ツール、トピックが同じ環境のすべてのエージェントに露出する**。しかも**① 新しいエージェントではすべてデフォルトで有効、② 自分のエージェントに誰が接続したかを表示するインターフェースが存在しない**。攻撃者はこれを使って組織になりすまし、気づかれずに機密操作を起動できる。Zenityの結論：『**connected agentsを有効にしたエージェントは、常にインターネット全体から匿名で到達可能だと想定せよ**』

summary_ko: |
  Zenity Labs: Build 2025에서 출시된 이 기능은 에이전트 간 기능 공유를 가능하게 하는데, **한 번 활성화하면 한 에이전트의 지식, 도구, 주제가 같은 환경의 다른 모든 에이전트에 노출된다** — 게다가 **① 모든 신규 에이전트에서 기본 활성화되어 있고, ② 누가 내 에이전트에 연결했는지 보여주는 인터페이스가 없다**. 공격자는 이를 이용해 조직을 사칭하고 민감한 작업을 들키지 않고 유발할 수 있다. Zenity의 결론: "**연결된 에이전트가 활성화된 에이전트는 항상 전체 인터넷에서 익명으로 도달 가능하다고 가정하라**"

summary_de: |
  Zenity Labs: Die Funktion (auf der Build 2025 vorgestellt) lässt Agenten Fähigkeiten teilen, und **sobald sie aktiviert ist, legt sie das Wissen, die Tools und die Themen eines Agenten für jeden anderen Agenten in derselben Umgebung offen** — und **① sie ist für alle neuen Agenten standardmäßig an, ② keine Oberfläche zeigt, wer sich mit dem eigenen Agenten verbunden hat**. Angreifer können dies nutzen, um sich als Organisation auszugeben und unbemerkt sensible Vorgänge auszulösen. Zenitys Fazit: „**Gehen Sie immer davon aus, dass jeder Agent mit aktivierten Connected Agents anonym aus dem gesamten Internet erreichbar ist**“

summary_fr: |
  Zenity Labs : la fonctionnalité (lancée à Build 2025) permet aux agents de partager des capacités, et **une fois activée elle expose les connaissances, outils et sujets d'un agent à tous les autres agents du même environnement** — et **① elle est active par défaut pour tous les nouveaux agents, ② aucune interface ne montre qui s'est connecté à votre agent**. Les attaquants peuvent s'en servir pour usurper une organisation et déclencher des opérations sensibles sans être remarqués. Conclusion de Zenity : « **Considérez toujours que tout agent avec des agents connectés activés est joignable anonymement depuis tout Internet** »

summary_es: |
  Zenity Labs: la función (lanzada en Build 2025) permite que los agentes compartan capacidades, y **una vez habilitada expone el conocimiento, las herramientas y los temas de un agente a todos los demás agentes del mismo entorno** — y **① está activada por defecto para todos los agentes nuevos, ② ninguna interfaz muestra quién se ha conectado a tu agente**. Los atacantes pueden usarla para suplantar a una organización y desencadenar operaciones sensibles sin ser detectados. Conclusión de Zenity: "**Asume siempre que cualquier agente con agentes conectados habilitados es accesible de forma anónima desde todo internet**"

sources:
  - url: https://www.esecurityplanet.com/artificial-intelligence/copilot-studio-feature-enables-silent-ai-backdoors/
    label: eSecurity Planet
  - url: https://cybersecuritynews.com/hackers-exploit-copilot-studios-new-connected-agents-feature/
    label: CybersecurityNews

disputed: false
landmark: false
scan_month: 2025-12
scan_ref: "SCAN.md §5 2025-12"
---

# Copilot Studio "Connected Agents" can carry invisible backdoors

![severity: medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: IPI](https://img.shields.io/badge/type-IPI-B08528?style=flat-square)

## Summary

Zenity Labs: the feature (launched at Build 2025) lets agents share capabilities, and **once enabled it exposes one agent's knowledge, tools and topics to every other agent in the same environment** — and **① it is on by default for all new agents, ② no interface shows who has connected to your agent**. Attackers can use this to impersonate an organization and trigger sensitive operations unnoticed. Zenity's conclusion: "**Always assume that any agent with connected agents enabled is anonymously reachable from the entire internet**"

## Attack chain

```mermaid
flowchart LR
    E["External content<br/>email · documents · issues · web pages"]:::entry
    S0["The agent reads it and executes it as instructions"]:::step
    I["Acts beyond its authority as the attacker intends<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | eSecurity Planet | <https://www.esecurityplanet.com/artificial-intelligence/copilot-studio-feature-enables-silent-ai-backdoors/> |
| 2 | CybersecurityNews | <https://cybersecuritynews.com/hackers-exploit-copilot-studios-new-connected-agents-feature/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-12-29` (raw: 2025-12-29, precision `day`) |
| Kind | Research demo `research` |
| Type | [`IPI`](../../taxonomy/types.md#ipi) Indirect prompt injection |
| Severity | **Medium** `medium` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-12-29-copilot-studio-connected-agents` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `medium`: controlled demo, moderate flaw, or an incident limited to a single user / single machine. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Zero-click data exfiltration chain](../../topics/zero-click-exfil.md)

**Related records:**

- `2026-01-12` [Claude Cowork ships with known vulnerabilities](../2026-01/2026-01-12-claude-cowork-dai-zhe-zhi.md)<br>  <sub>Claude Cowork ships with known vulnerabilities</sub>
- `2026-01-12` [Superhuman AI indirect prompt injection](../2026-01/2026-01-12-superhuman-jian-jie-ti-shi.md)<br>  <sub>Superhuman AI indirect prompt injection</sub>
- `2026-01-14` [Microsoft Copilot Personal "Reprompt"](../2026-01/2026-01-14-microsoft-copilot-personal-reprompt.md)<br>  <sub>Microsoft Copilot Personal "Reprompt"</sub>
- `2025-11-20` [ServiceNow Now Assist second-order prompt injection](../2025-11/2025-11-20-servicenow-now-assist.md)<br>  <sub>ServiceNow Now Assist second-order prompt injection</sub>

---

[← 2025-12 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-12/2025-12-29-copilot-studio-connected-agents.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
