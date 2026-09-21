<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>Eine offene Datenbank realer Vorfälle mit KI-Agenten</b></p>

<p align="center">
<a href="../../README.md">English</a> ·
<a href="README.zh-CN.md">简体中文</a> ·
<a href="README.ja.md">日本語</a> ·
<a href="README.ko.md">한국어</a> ·
<b>Deutsch</b> ·
<a href="README.fr.md">Français</a> ·
<a href="README.es.md">Español</a>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="Einträge" src="https://img.shields.io/badge/Eintr%C3%A4ge-340-48545A?style=flat-square"> <img alt="Monate" src="https://img.shields.io/badge/Monate-22-48545A?style=flat-square"> <img alt="kritisch" src="https://img.shields.io/badge/kritisch-45-88091D?style=flat-square"> <img alt="mit echtem Schaden" src="https://img.shields.io/badge/mit_echtem_Schaden-126-B23B40?style=flat-square"> <img alt="Primärquellen" src="https://img.shields.io/badge/Prim%C3%A4rquellen-548_URL-157A41?style=flat-square"> <img alt="Lizenz" src="https://img.shields.io/badge/Lizenz-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
Die Abdeckung reicht von **2025-01** bis **2026-09-19** — 340 Einträge zu Sicherheitsvorfällen mit KI-Agenten, Monat für Monat, dazu ein Vorläufer bis zurück zu 2024-12-01. Jeder Eintrag ist eine einzelne Markdown-Datei mit YAML-Kopf, Angriffsketten-Diagramm und **mindestens einer anklickbaren Primärquelle**. Von den 340 Einträgen haben nur **126 ein bestätigtes Opfer**.
<!-- END:thesis -->

Dieses Archiv dreht sich um eine Unterscheidung, die die meisten Vorfall-Listen verwischen:

> **Ein Agent, der tatsächlich Schaden angerichtet hat, ist nicht dasselbe wie ein Forscher, der zeigt, dass er es könnte.**

Jeder Eintrag beantwortet zuerst drei Fragen — gab es ein bestätigtes Opfer (`real_harm`), ist die KI-Beteiligung durch eine Primärquelle bestätigt (`ai_involvement`), und handelt es sich um einen Vorfall, eine Schwachstellen-Offenlegung, eine Forschungsdemo, einen Bedrohungsbericht oder einen regulatorischen Schritt (`kind`). Ohne diese drei Felder ist „300+ KI-Vorfälle dieses Jahr“ eine Zahl ohne Bedeutung.

---

## Auf einen Blick

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/monthly-dark.svg">
  <img alt="Einträge pro Monat, Januar 2025 bis September 2026" src="assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/severity-dark.svg">
  <img alt="Aufschlüsselung nach Schweregrad und Eintragstyp" src="assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/by-type-dark.svg">
  <img alt="Verteilung nach Angriffstyp" src="assets/by-type-light.svg" width="100%">
</picture>

## Wo anfangen

| Ich möchte … | Hier entlang |
|---|---|
| Chronologisch lesen | [Alle Einträge nach Monat](../../incidents/README.md) |
| Nur sehen, was wirklich passiert ist | [Die `critical`-Liste](#critical) · oder nach `real_harm: true` filtern |
| Nach Angriffsfläche lesen | [Sieben Themen](../../topics/README.md) |
| Ein Land oder eine Region ansehen | [Regionale Ausschnitte](../../regions/README.md) |
| Die Felder verstehen | [SCHEMA.md](../../SCHEMA.md) · [Taxonomie](../../taxonomy/README.md) · [Dokumentation](../../docs/README.md) |
| Die Daten auswerten | [`dist/`](../../dist/README.md) — JSON, CSV, Statistiken, jede Quell-URL |
| Interaktiv stöbern | [`index.html`](../../index.html) — eine Datei, offline nutzbar, sieben Sprachen |

> [!NOTE]
> **Sprache.** Die Einträge werden auf Englisch verfasst. Titel und Zusammenfassungen liegen in sieben Sprachen vor (Englisch, Chinesisch, Japanisch, Koreanisch, Deutsch, Französisch, Spanisch); die vollständige chinesische Fassung jedes Eintrags steht unter [`incidents/i18n/zh/`](../../incidents/i18n/zh/). Die zitierten Quellen bleiben in ihrer Originalsprache.

## Nach Monat

<!-- BEGIN:months -->
**2024** (1 Einträge)

| [12](../../incidents/2024-12/README.md) |
|---|
| `1` |

**2025** (121 Einträge)

| [01](../../incidents/2025-01/README.md) | [02](../../incidents/2025-02/README.md) | [03](../../incidents/2025-03/README.md) | [04](../../incidents/2025-04/README.md) | [05](../../incidents/2025-05/README.md) | [06](../../incidents/2025-06/README.md) | [07](../../incidents/2025-07/README.md) | [08](../../incidents/2025-08/README.md) | [09](../../incidents/2025-09/README.md) | [10](../../incidents/2025-10/README.md) | [11](../../incidents/2025-11/README.md) | [12](../../incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026** (218 Einträge)

| [01](../../incidents/2026-01/README.md) | [02](../../incidents/2026-02/README.md) | [03](../../incidents/2026-03/README.md) | [04](../../incidents/2026-04/README.md) | [05](../../incidents/2026-05/README.md) | [06](../../incidents/2026-06/README.md) | [07](../../incidents/2026-07/README.md) | [08](../../incidents/2026-08/README.md) | [09](../../incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `27` ★7 | `25` ★4 | `39` ★6 |

<sub>`n` = Einträge des Monats, ★ = davon `critical`</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
Einer von drei Auslösern genügt: ① **bestätigter** Schaden, der mehrere Organisationen, eine Regierung, kritische Infrastruktur oder einen Supply-Chain-Wurm erreicht; ② ein erstmaliger Fähigkeits-Meilenstein mit realen Opfern; ③ Forschung, die **eine weit verbreitete Verteidigungsannahme widerlegt** — dann `real_harm: false`, 2 Fälle. Vollständige Kriterien in [../../taxonomy/severity.md](../../taxonomy/severity.md).

| Datum | Eintrag | Typ | Region |
|---|---|---|---|
| `2025-01-29` | [DeepSeek-ClickHouse-Datenbank stand weit offen](../../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br><sub>DeepSeek ClickHouse database left wide open</sub> | `INFRA` | China |
| `2025-07-13` | [Amazon Q Developer-Erweiterung vergiftet](../../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br><sub>Amazon Q Developer extension poisoned</sub> | `SUPPLY` `ROGUE` | Global |
| `2025-07-18` | [Replit Agent löscht eine Produktionsdatenbank](../../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br><sub>Replit Agent deletes a production database</sub> | `ROGUE` | Vereinigte Staaten |
| `2025-08-08` | [Salesloft Drift: Diebstahl von OAuth-Token](../../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br><sub>Salesloft Drift OAuth token theft</sub> | `SUPPLY` `CRED` | Global |
| `2025-08-26` | [Nx „s1ngularity“](../../incidents/2025-08/2025-08-26-nx-s1ngularity.md)<br><sub>Nx "s1ngularity"</sub> | `SUPPLY` `CRED` | Global |
| `2025-09-15` | [Shai-Hulud npm-Wurm v1](../../incidents/2025-09/2025-09-15-shai-hulud-npm.md)<br><sub>Shai-Hulud npm worm v1</sub> | `SUPPLY` `CRED` | Global |
| `2025-11-01` | [ShadowRay 2.0 (Ray-Framework)](../../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md)<br><sub>ShadowRay 2.0 (Ray framework)</sub> | `INFRA` | Global |
| `2025-11-13` | [GTG-1002: erste KI-orchestrierte Cyber-Spionagekampagne](../../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br><sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub> | `WEAPON` | China Global |
| `2025-11-21` | [Shai-Hulud 2.0](../../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | Global |
| `2026-01-31` | [Moltbook-Datenbank vollständig offen](../../incidents/2026-01/2026-01-31-moltbook-open-database.md)<br><sub>Moltbook database fully open</sub> | `CRED` | Global |
| `2026-02-09` | [Clinejection](../../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | Global |
| `2026-02-20` | [KI-verstärkter Akteur kompromittiert 600+ FortiGate-Geräte](../../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br><sub>AI-augmented actor compromises 600+ FortiGate devices</sub> | `WEAPON` | Global |
| `2026-02-25` | [Neun mexikanische Regierungsstellen kompromittiert](../../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br><sub>Nine Mexican government agencies breached</sub> | `WEAPON` | Lateinamerika |
| `2026-02-26` | [Claude Code führt terraform destroy auf der gesamten Produktion von DataTalks.Club aus](../../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br><sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub> | `ROGUE` | Global |
| `2026-02-28` | [CodeWall dringt in McKinseys interne KI-Plattform „Lilli“ ein](../../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br><sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub> | `WEAPON` `INFRA` | Vereinigte Staaten |
| `2026-03-01` | [Hades: eine anhaltende Kampagne, die KI-Coding-Assistenten zur Angriffsfläche macht](../../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br><sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub> | `SUPPLY` `CRED` | Global |
| `2026-03-24` | [LiteLLM-Veröffentlichung mit Backdoor](../../incidents/2026-03/2026-03-24-litellm-backdoored-release.md)<br><sub>Backdoored LiteLLM release</sub> | `SUPPLY` `CRED` | Global |
| `2026-03-30` | [Axios npm-Paket kompromittiert](../../incidents/2026-03/2026-03-30-axios-npm-compromised.md)<br><sub>Axios npm package compromised</sub> | `SUPPLY` | Global |
| `2026-04-16` | [MCPwn (CVE-2026-33032): nginx-ui-MCP-Endpunkt in freier Wildbahn angegriffen](../../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br><sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub> | `MCP` `INFRA` | Global |
| `2026-04-25` | [Cursor und Claude Opus 4.6 löschen Produktion und Backups in neun Sekunden](../../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br><sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub> | `ROGUE` | Global |
| `2026-05-10` | [Erster LLM-Agent in freier Wildbahn, der die vollständige Post-Exploitation-Kette ausführt](../../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br><sub>First in-the-wild LLM agent running the full post-exploitation chain</sub> | `WEAPON` | Global |
| `2026-05-11` | [TanStack npm „Mini Shai-Hulud“](../../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br><sub>TanStack npm "Mini Shai-Hulud"</sub> | `SUPPLY` `CRED` | Global |
| `2026-05-18` | [3,800 interne GitHub-Repositories kompromittiert](../../incidents/2026-05/2026-05-18-github-3800-internal-repos.md)<br><sub>3,800 internal GitHub repositories compromised</sub> | `SUPPLY` `CRED` | Global |
| `2026-05-19` | [TrapDoor: Vergiftung dreier Ökosysteme zur Manipulation von KI-Assistenten-Konfigurationen](../../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br><sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub> | `SUPPLY` `CRED` | Global |
| `2026-05-21` | [Composio: Agentenautomatisierung selbst wird zum Pfad der Rechteerweiterung](../../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md)<br><sub>Composio: agent automation itself becomes the privilege-escalation path</sub> | `CRED` `SUPPLY` | Global |
| `2026-06-01` | [Angreifer bitten Metas KI-Support-Bot einfach um Instagram-Konten](../../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br><sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub> | `IPI` `CRED` | Global |
| `2026-06-01` | [Miasma-Wurm](../../incidents/2026-06/2026-06-01-miasma-worm.md)<br><sub>Miasma worm</sub> | `SUPPLY` `CRED` | Global |
| `2026-06-17` | [Sapphire Sleet vergiftet in 88 Minuten den gesamten Mastra-KI-Scope](../../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br><sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub> | `SUPPLY` `CRED` | Global |
| `2026-07-01` | [JADEPUFFER: erste durchgängig LLM-gesteuerte Ransomware](../../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br><sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub> | `WEAPON` | Global |
| `2026-07-01` | [Taiwans Atomaufsichtsbehörde und weitere Stellen von einem Agentenschwarm kompromittiert](../../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br><sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub> | `WEAPON` | Taiwan |
| `2026-07-02` | [Versteckte Web-Anweisungen bringen KI-Agenten dazu, Angreifer zu bezahlen (zwei Kampagnen in freier Wildbahn)](../../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br><sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub> | `IPI` `ROGUE` | Global |
| `2026-07-09` | [OpenAIs Agenten brechen in Hugging Face ein](../../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br><sub>OpenAI's agents breach Hugging Face</sub> | `EVAL` `WEAPON` | Global |
| `2026-07-30` | [Anthropic legt drei Evaluierungs-Ausbruchsvorfälle offen](../../incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br><sub>Anthropic discloses three evaluation-breakout incidents</sub> | `EVAL` | Global |
| `2026-07-30` | [Hermes Agent greift unbeaufsichtigt Thailands Finanzministerium an](../../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br><sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub> | `WEAPON` | Südostasien |
| `2026-07-30` | [Unit 42: autonome Kampagnen chinesischsprachiger Betreiber](../../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br><sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub> | `WEAPON` | China Global |
| `2026-08-04` | [CHAINDROP npm-Wurm](../../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br><sub>CHAINDROP npm worm</sub> | `SUPPLY` `CRED` | Global |
| `2026-08-06` | [Nicht authentifizierte Langflow-RCE in die CISA KEV aufgenommen](../../incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br><sub>Unauthenticated Langflow RCE added to CISA KEV</sub> | `INFRA` | Global |
| `2026-08-26` | [Trail of Bits: VMs halten cyberfähige Agenten nicht eingesperrt](../../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br><sub>Trail of Bits: VMs won't contain cyber-capable agents</sub> | `EVAL` `SANDBOX` | Global |
| `2026-08-28` | [PaperCut-Kampagne eines KI-Agentenschwarms beginnt](../../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br><sub>PaperCut AI agent swarm campaign begins</sub> | `WEAPON` | Global |
| `2026-09-01` | [GitSpawn: Eine bösartige .git/config führt Angreifercode in 7 Coding-Agenten aus, bevor das Modell überhaupt kontaktiert wird](../../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br><sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub> | `SUPPLY` `SANDBOX` | Global |
| `2026-09-02` | [Langflow CVE-2026-0768: die 12. in diesem Jahr in freier Wildbahn ausgenutzte Langflow-Schwachstelle](../../incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br><sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub> | `INFRA` `CRED` | Global |
| `2026-09-10` | [Anthropics Bedrohungsbericht September](../../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md)<br><sub>Anthropic September threat intelligence report</sub> | `WEAPON` | Global |
| `2026-09-11` | [Claude durchsucht 1.8 Millionen Android-Apps nach Secrets](../../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br><sub>Claude used to scan 1.8 million Android apps for secrets</sub> | `WEAPON` | Global |
| `2026-09-14` | [Spaniens AEPD erhält die erste Meldung einer von einem KI-Agenten ausgeführten Datenschutzverletzung](../../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md)<br><sub>Spain's AEPD receives the first AI-agent-driven breach notification</sub> | `WEAPON` | Europa |
| `2026-09-15` | [PaperCut-Angriff eines KI-Agentenschwarms veröffentlicht](../../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br><sub>PaperCut AI agent swarm attack made public</sub> | `WEAPON` | Global |
<!-- END:critical -->

## Was als Eintrag zählt

Ein Eintrag qualifiziert sich, wenn **mindestens eines** davon zutrifft:

1. Der KI-Agent war **der Angreifer** — autonom oder von einem Menschen gesteuert
2. Der KI-Agent war **das Ziel** — Injection, Vergiftung, Ausbruch, exponierte Infrastruktur
3. Der KI-Agent war **ein Glied in der Schadenskette** — er las feindselige Inhalte und handelte danach
4. Es ist eine **regulatorische, gesetzgeberische oder herstellerseitige Maßnahme** direkt zur Agentensicherheit (erfasst als `kind: policy`, nicht als Vorfall gezählt)

**Nicht erfasst:** reine LLM-Content-Safety-Befunde (ein Modell zum Aussprechen unerwünschter Inhalte zu bewegen), gewöhnliche Schwachstellen ohne Agentenbezug und Behauptungen ohne nachvollziehbare Primärquelle.

Zwei Kategorien werden **gekennzeichnet statt gelöscht**:

- `ai_involvement: unverified` — breit als KI-Vorfall berichtet, aber die Primärquelle enthält keine KI. Bleibt erhalten, damit die Behauptung **zusammen mit ihrer Widerlegung auffindbar** ist.
- `ai_involvement: disputed` — Hersteller und Berichterstattung widersprechen sich; beide Darstellungen bleiben nebeneinander im Eintrag erhalten.

Vollständige Kriterien: [docs/scope.md](../../docs/scope.md).

## Datenqualität

<!-- BEGIN:quality -->
|  |  |
|---|---|
| Quell-Links | 615 Links aus 548 eindeutigen URLs |
| Einträge ohne Quelle | **0** — keine Quelle, kein Eintrag |
| Grad A (Primärquelle) | 290 |
| Als umstritten markiert | 14 |
| Verifikationsrunden | 4 |
<!-- END:quality -->

Die ersten drei Runden prüften **jeden Eintrag einzeln**. Die vierte Runde war ein **Abdeckungs-Audit** und fand immer noch rund 11 % Lücken. Diese Runden fangen ganz unterschiedliche Probleme: „Ist das, was wir haben, korrekt“ und „Ist das, was hier stehen sollte, vorhanden“ sind getrennte Fragen und müssen getrennt gestellt werden.

Diese vier Runden löschten zwei erfundene Einträge, korrigierten PaperCuts „Domain-Admin in sechs Stunden“ auf **sieben Minuten** und stuften Step Finance auf Grad D herab, weil die Primärberichterstattung KI mit keinem Wort erwähnt. Jede Korrektur ist in [docs/data-quality.md](../../docs/data-quality.md) dokumentiert — nichts wurde still überschrieben.

## Zitieren

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {340 Einträge, 2025-01 bis 2026-09; 126 mit bestätigtem realen Schaden},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

Um einen einzelnen Eintrag zu zitieren, verwenden Sie dessen `id` — zum Beispiel `orca:2026-07-09-openai-agents-breach-huggingface`.

## Mitmachen

Korrekturen, fehlende Einträge und bessere Quellen sind willkommen. Drei harte Regeln:

1. **Jeder Eintrag braucht eine anklickbare Primärquelle.** Keine Quelle, kein Merge.
2. **Im Zweifel kennzeichnen statt löschen.** Umstrittene Fakten bekommen `disputed: true`, beide Darstellungen bleiben im Eintrag.
3. **Korrekturen gehören in den Eintrag, niemals still darüber hinweg.** Sagen Sie, was sich geändert hat und warum.

Siehe [CONTRIBUTING.md](../../CONTRIBUTING.md). Issue-Vorlagen für [einen neuen Eintrag](../../.github/ISSUE_TEMPLATE/new-incident.yml) und [eine Korrektur](../../.github/ISSUE_TEMPLATE/correction.yml) sind eingerichtet.

## Lizenz und Haftungsausschluss

Lizenziert unter [CC BY 4.0](../../LICENSE) — Namensnennung erforderlich. Verlinkte Quellen bleiben das Urheberrecht ihrer jeweiligen Inhaber.

Dieses Archiv erfasst **ausschließlich öffentlich bekannt gewordene Ereignisse**. Es enthält keine unveröffentlichten Schwachstellendetails, keinen Exploit-Code und keine Angriffswerkzeuge. Klassifizierung und Schweregrad sind die Einschätzung der Redaktion, keine offizielle Feststellung eines Herstellers oder Regulierers. Wenn Sie betroffen sind und glauben, dass ein Eintrag falsch ist, öffnen Sie ein Issue — er wird geprüft und korrigiert.

---

<sub><!-- BEGIN:footer -->Erstellt am 2026-09-19 · 340 Einträge · 22 Monate<!-- END:footer --></sub> · <sub>Struktur: [SCHEMA.md](../../SCHEMA.md) · Daten: [dist/](../../dist/README.md)</sub>
