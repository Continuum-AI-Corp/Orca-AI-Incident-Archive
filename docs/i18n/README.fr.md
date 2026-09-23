<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>Une base de données ouverte sur les incidents réels impliquant des agents IA</b></p>

<p align="center">
<a href="../../README.md">English</a> ·
<a href="README.zh-CN.md">简体中文</a> ·
<a href="README.ja.md">日本語</a> ·
<a href="README.ko.md">한국어</a> ·
<a href="README.de.md">Deutsch</a> ·
<b>Français</b> ·
<a href="README.es.md">Español</a>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="entrées" src="https://img.shields.io/badge/entr%C3%A9es-354-48545A?style=flat-square"> <img alt="mois" src="https://img.shields.io/badge/mois-22-48545A?style=flat-square"> <img alt="critiques" src="https://img.shields.io/badge/critiques-45-88091D?style=flat-square"> <img alt="préjudice réel" src="https://img.shields.io/badge/pr%C3%A9judice_r%C3%A9el-127-B23B40?style=flat-square"> <img alt="sources primaires" src="https://img.shields.io/badge/sources_primaires-593_URL-157A41?style=flat-square"> <img alt="licence" src="https://img.shields.io/badge/licence-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
La couverture va de **2025-01** à **2026-09-22** — 354 entrées d'événements de sécurité liés aux agents IA, mois par mois, plus un précurseur remontant à 2024-12-01. Chaque entrée est un fichier Markdown unique avec un en-tête YAML, un schéma de chaîne d'attaque et **au moins une source primaire cliquable**. Sur ces 354 entrées, seules **127 ont une victime confirmée**.
<!-- END:thesis -->

Cette archive repose sur une distinction que la plupart des listes d'incidents aplatissent :

> **Un agent qui a réellement causé des dommages n'est pas la même chose qu'un chercheur qui démontre qu'il le pourrait.**

Chaque entrée répond d'abord à trois questions — y a-t-il eu une victime confirmée (`real_harm`), l'implication de l'IA est-elle confirmée par une source primaire (`ai_involvement`), et s'agit-il d'un incident, d'une divulgation de vulnérabilité, d'une démonstration de recherche, d'un rapport de menace ou d'une action réglementaire (`kind`). Sans ces trois champs, « 300+ incidents d'IA cette année » est un chiffre qui ne veut rien dire.

---

## En un coup d'œil

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/monthly-dark.svg">
  <img alt="Entrées par mois, janvier 2025 à septembre 2026" src="assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/severity-dark.svg">
  <img alt="Répartition par gravité et par type d'entrée" src="assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/by-type-dark.svg">
  <img alt="Répartition par type d'attaque" src="assets/by-type-light.svg" width="100%">
</picture>

## Par où commencer

| Je veux… | Aller ici |
|---|---|
| Lire chronologiquement | [Toutes les entrées par mois](../../incidents/README.md) |
| Voir seulement ce qui s'est réellement produit | [La liste `critical`](#critical) · ou filtrer `real_harm: true` |
| Lire par surface d'attaque | [Sept thèmes](../../topics/README.md) |
| Examiner un pays ou une région | [Découpages régionaux](../../regions/README.md) |
| Comprendre les champs | [SCHEMA.md](../../SCHEMA.md) · [Taxonomie](../../taxonomy/README.md) · [Documentation](../../docs/README.md) |
| Analyser les données | [`dist/`](../../dist/README.md) — JSON, CSV, statistiques, chaque URL source |
| Naviguer de façon interactive | [`index.html`](../../index.html) — un seul fichier, fonctionne hors ligne, sept langues |

> [!NOTE]
> **Langue.** Les entrées sont rédigées en anglais. Les titres et les résumés existent en sept langues (anglais, chinois, japonais, coréen, allemand, français, espagnol) ; la version chinoise complète de chaque entrée se trouve sous [`incidents/i18n/zh/`](../../incidents/i18n/zh/). Les sources citées restent dans leur langue d'origine.

## Par mois

<!-- BEGIN:months -->
**2024** (1 entrées)

| [12](../../incidents/2024-12/README.md) |
|---|
| `1` |

**2025** (121 entrées)

| [01](../../incidents/2025-01/README.md) | [02](../../incidents/2025-02/README.md) | [03](../../incidents/2025-03/README.md) | [04](../../incidents/2025-04/README.md) | [05](../../incidents/2025-05/README.md) | [06](../../incidents/2025-06/README.md) | [07](../../incidents/2025-07/README.md) | [08](../../incidents/2025-08/README.md) | [09](../../incidents/2025-09/README.md) | [10](../../incidents/2025-10/README.md) | [11](../../incidents/2025-11/README.md) | [12](../../incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026** (232 entrées)

| [01](../../incidents/2026-01/README.md) | [02](../../incidents/2026-02/README.md) | [03](../../incidents/2026-03/README.md) | [04](../../incidents/2026-04/README.md) | [05](../../incidents/2026-05/README.md) | [06](../../incidents/2026-06/README.md) | [07](../../incidents/2026-07/README.md) | [08](../../incidents/2026-08/README.md) | [09](../../incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `28` ★7 | `26` ★4 | `51` ★6 |

<sub>`n` = entrées du mois, ★ = dont `critical`</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
L'un de ces trois déclencheurs suffit : ① des dommages **confirmés** touchant plusieurs organisations, un gouvernement, une infrastructure critique ou un ver de chaîne d'approvisionnement ; ② un jalon de capacité inédit avec de vraies victimes ; ③ une recherche qui **renverse une défense largement déployée** — dans ce cas `real_harm: false`, 2 cas. Critères complets dans [../../taxonomy/severity.md](../../taxonomy/severity.md).

| Date | Entrée | Type | Région |
|---|---|---|---|
| `2025-01-29` | [La base ClickHouse de DeepSeek laissée grande ouverte](../../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br><sub>DeepSeek ClickHouse database left wide open</sub> | `INFRA` | Chine |
| `2025-07-13` | [L'extension Amazon Q Developer empoisonnée](../../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br><sub>Amazon Q Developer extension poisoned</sub> | `SUPPLY` `ROGUE` | Mondial |
| `2025-07-18` | [L'agent de Replit supprime une base de données de production](../../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br><sub>Replit Agent deletes a production database</sub> | `ROGUE` | États-Unis |
| `2025-08-08` | [Vol de jetons OAuth de Salesloft Drift](../../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br><sub>Salesloft Drift OAuth token theft</sub> | `SUPPLY` `CRED` | Mondial |
| `2025-08-26` | [Nx « s1ngularity »](../../incidents/2025-08/2025-08-26-nx-s1ngularity.md)<br><sub>Nx "s1ngularity"</sub> | `SUPPLY` `CRED` | Mondial |
| `2025-09-15` | [Le ver npm Shai-Hulud v1](../../incidents/2025-09/2025-09-15-shai-hulud-npm.md)<br><sub>Shai-Hulud npm worm v1</sub> | `SUPPLY` `CRED` | Mondial |
| `2025-11-01` | [ShadowRay 2.0 (framework Ray)](../../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md)<br><sub>ShadowRay 2.0 (Ray framework)</sub> | `INFRA` | Mondial |
| `2025-11-13` | [GTG-1002 : première campagne de cyberespionnage orchestrée par IA](../../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br><sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub> | `WEAPON` | Chine Mondial |
| `2025-11-21` | [Shai-Hulud 2.0](../../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | Mondial |
| `2026-01-31` | [La base de données de Moltbook grande ouverte](../../incidents/2026-01/2026-01-31-moltbook-open-database.md)<br><sub>Moltbook database fully open</sub> | `CRED` | Mondial |
| `2026-02-09` | [Clinejection](../../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | Mondial |
| `2026-02-20` | [Un acteur augmenté par l'IA compromet plus de 600 appareils FortiGate](../../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br><sub>AI-augmented actor compromises 600+ FortiGate devices</sub> | `WEAPON` | Mondial |
| `2026-02-25` | [Neuf agences gouvernementales mexicaines compromises](../../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br><sub>Nine Mexican government agencies breached</sub> | `WEAPON` | Amérique latine |
| `2026-02-26` | [Claude Code exécute terraform destroy sur toute la production de DataTalks.Club](../../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br><sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub> | `ROGUE` | Mondial |
| `2026-02-28` | [CodeWall pénètre la plateforme IA interne « Lilli » de McKinsey](../../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br><sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub> | `WEAPON` `INFRA` | États-Unis |
| `2026-03-01` | [Hades : une campagne prolongée qui transforme les assistants de code IA en surface d'attaque](../../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br><sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-03-24` | [Une version backdoorée de LiteLLM publiée](../../incidents/2026-03/2026-03-24-litellm-backdoored-release.md)<br><sub>Backdoored LiteLLM release</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-03-30` | [Le paquet npm Axios compromis](../../incidents/2026-03/2026-03-30-axios-npm-compromised.md)<br><sub>Axios npm package compromised</sub> | `SUPPLY` | Mondial |
| `2026-04-16` | [MCPwn (CVE-2026-33032) : le point de terminaison MCP de nginx-ui frappé en conditions réelles](../../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br><sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub> | `MCP` `INFRA` | Mondial |
| `2026-04-25` | [Cursor et Claude Opus 4.6 effacent production et sauvegardes en neuf secondes](../../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br><sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub> | `ROGUE` | Mondial |
| `2026-05-10` | [Premier agent LLM en conditions réelles exécutant toute la chaîne de post-exploitation](../../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br><sub>First in-the-wild LLM agent running the full post-exploitation chain</sub> | `WEAPON` | Mondial |
| `2026-05-11` | [« Mini Shai-Hulud » sur npm TanStack](../../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md)<br><sub>TanStack npm "Mini Shai-Hulud"</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-05-18` | [3 800 dépôts GitHub internes compromis](../../incidents/2026-05/2026-05-18-github-3800-internal-repos.md)<br><sub>3,800 internal GitHub repositories compromised</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-05-19` | [TrapDoor : empoisonner trois écosystèmes pour corrompre les configurations d'assistants IA](../../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br><sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-05-21` | [Composio : l'automatisation d'agents devient elle-même la voie d'élévation de privilèges](../../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md)<br><sub>Composio: agent automation itself becomes the privilege-escalation path</sub> | `CRED` `SUPPLY` | Mondial |
| `2026-06-01` | [Les attaquants demandent simplement des comptes Instagram au bot de support IA de Meta](../../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br><sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub> | `IPI` `CRED` | Mondial |
| `2026-06-01` | [Le ver Miasma](../../incidents/2026-06/2026-06-01-miasma-worm.md)<br><sub>Miasma worm</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-06-17` | [Sapphire Sleet empoisonne tout le périmètre Mastra AI en 88 minutes](../../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br><sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-07-01` | [JADEPUFFER : premier ransomware piloté de bout en bout par un LLM](../../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br><sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub> | `WEAPON` | Mondial |
| `2026-07-01` | [La commission de sûreté nucléaire taïwanaise et d'autres agences compromises par un essaim d'agents](../../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br><sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub> | `WEAPON` | Taïwan |
| `2026-07-02` | [Des instructions web cachées font payer les attaquants par les agents IA (deux campagnes en conditions réelles)](../../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br><sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub> | `IPI` `ROGUE` | Mondial |
| `2026-07-09` | [Les agents d'OpenAI pénètrent Hugging Face](../../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br><sub>OpenAI's agents breach Hugging Face</sub> | `EVAL` `WEAPON` | Mondial |
| `2026-07-30` | [Anthropic divulgue trois incidents d'évasion d'évaluation](../../incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br><sub>Anthropic discloses three evaluation-breakout incidents</sub> | `EVAL` | Mondial |
| `2026-07-30` | [Hermes Agent attaque sans supervision le ministère thaïlandais des Finances](../../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br><sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub> | `WEAPON` | Asie du Sud-Est |
| `2026-07-30` | [Unit 42 : campagnes autonomes menées par des opérateurs sinophones](../../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br><sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub> | `WEAPON` | Chine Mondial |
| `2026-08-04` | [Le ver npm CHAINDROP](../../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br><sub>CHAINDROP npm worm</sub> | `SUPPLY` `CRED` | Mondial |
| `2026-08-06` | [Le RCE non authentifié de Langflow ajouté au KEV de la CISA](../../incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br><sub>Unauthenticated Langflow RCE added to CISA KEV</sub> | `INFRA` | Mondial |
| `2026-08-26` | [Trail of Bits : les VM ne contiendront pas les agents dotés de capacités cyber](../../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br><sub>Trail of Bits: VMs won't contain cyber-capable agents</sub> | `EVAL` `SANDBOX` | Mondial |
| `2026-08-28` | [Début de la campagne d'essaim d'agents IA contre PaperCut](../../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br><sub>PaperCut AI agent swarm campaign begins</sub> | `WEAPON` | Mondial |
| `2026-09-01` | [GitSpawn : un .git/config malveillant exécute du code attaquant dans 7 agents de code avant même tout contact avec le modèle](../../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br><sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub> | `SUPPLY` `SANDBOX` | Mondial |
| `2026-09-02` | [Langflow CVE-2026-0768 : la 12e faille de Langflow exploitée en conditions réelles cette année](../../incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br><sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub> | `INFRA` `CRED` | Mondial |
| `2026-09-10` | [Rapport de renseignement sur les menaces de septembre d'Anthropic](../../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md)<br><sub>Anthropic September threat intelligence report</sub> | `WEAPON` | Mondial |
| `2026-09-11` | [Claude utilisé pour scanner 1,8 million d'applications Android à la recherche de secrets](../../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br><sub>Claude used to scan 1.8 million Android apps for secrets</sub> | `WEAPON` | Mondial |
| `2026-09-14` | [L'AEPD espagnole reçoit la première notification de violation exécutée par un agent IA](../../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md)<br><sub>Spain's AEPD receives the first AI-agent-driven breach notification</sub> | `WEAPON` | Europe |
| `2026-09-15` | [L'attaque par essaim d'agents IA contre PaperCut rendue publique](../../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br><sub>PaperCut AI agent swarm attack made public</sub> | `WEAPON` | Mondial |
<!-- END:critical -->

## Qu'est-ce qui compte comme entrée

Une entrée est retenue si **au moins une** de ces conditions est vraie :

1. L'agent IA était **l'attaquant** — de façon autonome ou piloté par un humain
2. L'agent IA était **la cible** — injection, empoisonnement, évasion, infrastructure exposée
3. L'agent IA était **un maillon de la chaîne de dommages** — il a lu un contenu hostile et a agi en conséquence
4. Il s'agit d'une **action réglementaire, législative ou d'un fournisseur** portant directement sur la sécurité des agents (enregistrée comme `kind: policy`, non comptée comme incident)

**Hors périmètre :** les constats de sécurité de contenu propres aux LLM (amener un modèle à dire ce qu'il ne devrait pas), les vulnérabilités ordinaires sans lien avec les agents, et les affirmations sans source primaire vérifiable.

Deux catégories sont **étiquetées plutôt que supprimées** :

- `ai_involvement: unverified` — largement rapporté comme un incident d'IA, mais la source primaire ne mentionne aucune IA. Conservé pour que l'affirmation reste **recherchable avec sa réfutation**.
- `ai_involvement: disputed` — le fournisseur et la couverture médiatique divergent ; les deux versions sont conservées côte à côte dans l'entrée.

Critères complets : [docs/scope.md](../../docs/scope.md).

## Qualité des données

<!-- BEGIN:quality -->
|  |  |
|---|---|
| Liens sources | 662 liens sur 593 URL uniques |
| Entrées sans source | **0** — pas de source, pas d'entrée |
| Grade A (source primaire) | 302 |
| Marquées comme contestées | 14 |
| Cycles de vérification | 4 |
<!-- END:quality -->

Les trois premiers tours ont vérifié **chaque entrée individuellement**. Le quatrième a réalisé un **audit de couverture** et a encore trouvé environ 11 % de manques. Ces tours attrapent des problèmes entièrement différents : « ce que nous avons est-il exact » et « ce qui devrait figurer ici est-il présent » sont deux questions distinctes à poser séparément.

Ces quatre tours ont supprimé deux entrées fabriquées, corrigé le « domaine admin en six heures » de PaperCut en **sept minutes**, et rétrogradé Step Finance au grade D car la couverture primaire ne mentionne nulle part l'IA. Chaque correction est consignée dans [docs/data-quality.md](../../docs/data-quality.md) — rien n'a été écrasé en silence.

## Citer

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {354 entrées, de 2025-01 à 2026-09 ; 127 avec préjudice réel confirmé},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

Pour citer une entrée individuelle, utilisez son `id` — par exemple `orca:2026-07-09-openai-agents-breach-huggingface`.

## Contribuer

Les corrections, les entrées manquantes et de meilleures sources sont les bienvenues. Trois règles absolues :

1. **Chaque entrée a besoin d'une source primaire cliquable.** Pas de source, pas de fusion.
2. **En cas de doute, étiquetez — ne supprimez pas.** Les faits contestés reçoivent `disputed: true` et les deux versions restent dans l'entrée.
3. **Les corrections vont dans l'entrée, jamais par-dessus en silence.** Dites ce qui a changé et pourquoi.

Voir [CONTRIBUTING.md](../../CONTRIBUTING.md). Des modèles d'issue pour [une nouvelle entrée](../../.github/ISSUE_TEMPLATE/new-incident.yml) et [une correction](../../.github/ISSUE_TEMPLATE/correction.yml) sont en place.

## Licence et avertissement

Sous licence [CC BY 4.0](../../LICENSE) — attribution requise. Les sources liées restent la propriété de leurs détenteurs respectifs.

Cette archive ne consigne que des **événements rendus publics**. Elle ne contient aucun détail de vulnérabilité non divulgué, aucun code d'exploit et aucun outil d'attaque. La classification et la gravité relèvent du jugement des éditeurs, et non d'une conclusion officielle d'un fournisseur ou d'un régulateur. Si vous êtes une partie concernée et estimez qu'une entrée est erronée, ouvrez une issue — elle sera vérifiée et corrigée.

---

<sub><!-- BEGIN:footer -->Généré le 2026-09-22 · 354 entrées · 22 mois<!-- END:footer --></sub> · <sub>Structure : [SCHEMA.md](../../SCHEMA.md) · Données : [dist/](../../dist/README.md)</sub>
