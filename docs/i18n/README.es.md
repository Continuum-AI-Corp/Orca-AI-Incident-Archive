<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>Una base de datos abierta de incidentes reales con agentes de IA</b></p>

<p align="center">
<a href="../../README.md">English</a> ·
<a href="README.zh-CN.md">简体中文</a> ·
<a href="README.ja.md">日本語</a> ·
<a href="README.ko.md">한국어</a> ·
<a href="README.de.md">Deutsch</a> ·
<a href="README.fr.md">Français</a> ·
<b>Español</b>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="registros" src="https://img.shields.io/badge/registros-330-48545A?style=flat-square"> <img alt="meses" src="https://img.shields.io/badge/meses-22-48545A?style=flat-square"> <img alt="críticos" src="https://img.shields.io/badge/cr%C3%ADticos-45-88091D?style=flat-square"> <img alt="con daño real" src="https://img.shields.io/badge/con_da%C3%B1o_real-124-B23B40?style=flat-square"> <img alt="fuentes primarias" src="https://img.shields.io/badge/fuentes_primarias-511_URL-157A41?style=flat-square"> <img alt="licencia" src="https://img.shields.io/badge/licencia-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
La cobertura va de **2025-01** a **2026-09-19**: 330 registros de incidentes de seguridad relacionados con agentes de IA, mes a mes, más un precursor que se remonta a 2024-12-01. Cada registro es un único archivo Markdown con cabecera YAML, diagrama de cadena de ataque y **al menos una fuente primaria en la que se puede hacer clic**. De los 330, solo **124 tienen una víctima confirmada**.
<!-- END:thesis -->

Este archivo gira en torno a una distinción que la mayoría de las listas de incidentes difumina:

> **Un agente que realmente causó daño no es lo mismo que un investigador demostrando que podría hacerlo.**

Cada registro responde primero a tres preguntas: si hubo una víctima confirmada (`real_harm`), si la participación de la IA está confirmada por una fuente primaria (`ai_involvement`), y si se trata de un incidente, una divulgación de vulnerabilidad, una demostración de investigación, un informe de amenazas o una acción regulatoria (`kind`). Sin esos tres campos, «300+ incidentes de IA este año» es un número que no significa nada.

---

## De un vistazo

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/monthly-dark.svg">
  <img alt="Registros por mes, enero de 2025 a septiembre de 2026" src="assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/severity-dark.svg">
  <img alt="Desglose por gravedad y tipo de registro" src="assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="assets/by-type-dark.svg">
  <img alt="Distribución por tipo de ataque" src="assets/by-type-light.svg" width="100%">
</picture>

## Por dónde empezar

| Quiero… | Ir aquí |
|---|---|
| Leerlo cronológicamente | [Todos los registros por mes](../../incidents/README.md) |
| Ver solo lo que realmente ocurrió | [La lista `critical`](#critical) · o filtrar `real_harm: true` |
| Leer por superficie de ataque | [Siete temas](../../topics/README.md) |
| Ver un país o una región | [Cortes regionales](../../regions/README.md) |
| Entender los campos | [SCHEMA.md](../../SCHEMA.md) · [Taxonomía](../../taxonomy/README.md) · [Documentación](../../docs/README.md) |
| Analizar los datos | [`dist/`](../../dist/README.md) — JSON, CSV, estadísticas, cada URL de origen |
| Navegar de forma interactiva | [`index.html`](../../index.html) — un solo archivo, funciona sin conexión, siete idiomas |

> [!NOTE]
> **Idioma.** Los registros se redactan en inglés. Los títulos y resúmenes existen en siete idiomas (inglés, chino, japonés, coreano, alemán, francés y español); la versión china completa de cada registro está en [`incidents/i18n/zh/`](../../incidents/i18n/zh/). Las fuentes citadas permanecen en su idioma original.

## Por mes

<!-- BEGIN:months -->
**2024** (1 registros)

| [12](../../incidents/2024-12/README.md) |
|---|
| `1` |

**2025** (121 registros)

| [01](../../incidents/2025-01/README.md) | [02](../../incidents/2025-02/README.md) | [03](../../incidents/2025-03/README.md) | [04](../../incidents/2025-04/README.md) | [05](../../incidents/2025-05/README.md) | [06](../../incidents/2025-06/README.md) | [07](../../incidents/2025-07/README.md) | [08](../../incidents/2025-08/README.md) | [09](../../incidents/2025-09/README.md) | [10](../../incidents/2025-10/README.md) | [11](../../incidents/2025-11/README.md) | [12](../../incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026** (208 registros)

| [01](../../incidents/2026-01/README.md) | [02](../../incidents/2026-02/README.md) | [03](../../incidents/2026-03/README.md) | [04](../../incidents/2026-04/README.md) | [05](../../incidents/2026-05/README.md) | [06](../../incidents/2026-06/README.md) | [07](../../incidents/2026-07/README.md) | [08](../../incidents/2026-08/README.md) | [09](../../incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `27` ★7 | `23` ★4 | `31` ★6 |

<sub>`n` = registros del mes, ★ = de ellos `critical`</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
Basta con uno de estos tres desencadenantes: ① daño **confirmado** que alcanza a varias organizaciones, un gobierno, infraestructura crítica o un gusano de cadena de suministro; ② un hito de capacidad inédito con víctimas reales; ③ investigación que **refuta una defensa ampliamente desplegada** — en ese caso `real_harm: false`, 2 casos. Criterios completos en [../../taxonomy/severity.md](../../taxonomy/severity.md).

| Fecha | Registro | Tipo | Región |
|---|---|---|---|
| `2025-01-29` | [Base de datos ClickHouse de DeepSeek expuesta sin protección](../../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br><sub>DeepSeek ClickHouse database left wide open</sub> | `INFRA` | China |
| `2025-07-13` | [Extensión de Amazon Q Developer envenenada](../../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br><sub>Amazon Q Developer extension poisoned</sub> | `SUPPLY` `ROGUE` | Global |
| `2025-07-18` | [Replit Agent borra una base de datos de producción](../../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br><sub>Replit Agent deletes a production database</sub> | `ROGUE` | Estados Unidos |
| `2025-08-08` | [Robo de tokens OAuth de Salesloft Drift](../../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br><sub>Salesloft Drift OAuth token theft</sub> | `SUPPLY` `CRED` | Global |
| `2025-08-26` | [Nx "s1ngularity"](../../incidents/2025-08/2025-08-26-nx-s1ngularity.md) | `SUPPLY` `CRED` | Global |
| `2025-09-15` | [Gusano npm Shai-Hulud v1](../../incidents/2025-09/2025-09-15-shai-hulud-npm.md)<br><sub>Shai-Hulud npm worm v1</sub> | `SUPPLY` `CRED` | Global |
| `2025-11-01` | [ShadowRay 2.0 (framework Ray)](../../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md)<br><sub>ShadowRay 2.0 (Ray framework)</sub> | `INFRA` | Global |
| `2025-11-13` | [GTG-1002: primera campaña de ciberespionaje orquestada por IA](../../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br><sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub> | `WEAPON` | China Global |
| `2025-11-21` | [Shai-Hulud 2.0](../../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | Global |
| `2026-01-31` | [La base de datos de Moltbook, totalmente abierta](../../incidents/2026-01/2026-01-31-moltbook-open-database.md)<br><sub>Moltbook database fully open</sub> | `CRED` | Global |
| `2026-02-09` | [Clinejection](../../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | Global |
| `2026-02-20` | [Un actor potenciado por IA compromete más de 600 dispositivos FortiGate](../../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br><sub>AI-augmented actor compromises 600+ FortiGate devices</sub> | `WEAPON` | Global |
| `2026-02-25` | [Nueve agencias del gobierno de México comprometidas](../../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br><sub>Nine Mexican government agencies breached</sub> | `WEAPON` | Latinoamérica |
| `2026-02-26` | [Claude Code ejecuta terraform destroy en toda la producción de DataTalks.Club](../../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br><sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub> | `ROGUE` | Global |
| `2026-02-28` | [CodeWall vulnera la plataforma interna de IA "Lilli" de McKinsey](../../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br><sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub> | `WEAPON` `INFRA` | Estados Unidos |
| `2026-03-01` | [Hades: una campaña sostenida que convierte a los asistentes de código con IA en la superficie de ataque](../../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br><sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub> | `SUPPLY` `CRED` | Global |
| `2026-03-24` | [Versión de LiteLLM con puerta trasera](../../incidents/2026-03/2026-03-24-litellm-backdoored-release.md)<br><sub>Backdoored LiteLLM release</sub> | `SUPPLY` `CRED` | Global |
| `2026-03-30` | [El paquete npm Axios comprometido](../../incidents/2026-03/2026-03-30-axios-npm-compromised.md)<br><sub>Axios npm package compromised</sub> | `SUPPLY` | Global |
| `2026-04-16` | [MCPwn (CVE-2026-33032): el endpoint MCP de nginx-ui golpeado en entornos reales](../../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br><sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub> | `MCP` `INFRA` | Global |
| `2026-04-25` | [Cursor y Claude Opus 4.6 borran producción y las copias de seguridad en nueve segundos](../../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br><sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub> | `ROGUE` | Global |
| `2026-05-10` | [Primer agente LLM en entornos reales que ejecuta toda la cadena de post-explotación](../../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br><sub>First in-the-wild LLM agent running the full post-exploitation chain</sub> | `WEAPON` | Global |
| `2026-05-11` | [TanStack npm "Mini Shai-Hulud"](../../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md) | `SUPPLY` `CRED` | Global |
| `2026-05-18` | [3,800 repositorios internos de GitHub comprometidos](../../incidents/2026-05/2026-05-18-github-3800-internal-repos.md)<br><sub>3,800 internal GitHub repositories compromised</sub> | `SUPPLY` `CRED` | Global |
| `2026-05-19` | [TrapDoor: envenenar tres ecosistemas para corromper las configuraciones de asistentes de IA](../../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br><sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub> | `SUPPLY` `CRED` | Global |
| `2026-05-21` | [Composio: la propia automatización de agentes se convierte en la vía de escalada de privilegios](../../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md)<br><sub>Composio: agent automation itself becomes the privilege-escalation path</sub> | `CRED` `SUPPLY` | Global |
| `2026-06-01` | [Los atacantes simplemente piden cuentas de Instagram al bot de soporte de IA de Meta](../../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br><sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub> | `IPI` `CRED` | Global |
| `2026-06-01` | [El gusano Miasma](../../incidents/2026-06/2026-06-01-miasma-worm.md)<br><sub>Miasma worm</sub> | `SUPPLY` `CRED` | Global |
| `2026-06-17` | [Sapphire Sleet envenena todo el ámbito de Mastra AI en 88 minutos](../../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br><sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub> | `SUPPLY` `CRED` | Global |
| `2026-07-01` | [JADEPUFFER: el primer ransomware dirigido de extremo a extremo por un LLM](../../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br><sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub> | `WEAPON` | Global |
| `2026-07-01` | [La comisión de seguridad nuclear de Taiwán y otras agencias vulneradas por un enjambre de agentes](../../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br><sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub> | `WEAPON` | Taiwán |
| `2026-07-02` | [Instrucciones web ocultas hacen que los agentes de IA paguen a los atacantes (dos campañas en entornos reales)](../../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br><sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub> | `IPI` `ROGUE` | Global |
| `2026-07-09` | [Los agentes de OpenAI vulneran Hugging Face](../../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br><sub>OpenAI's agents breach Hugging Face</sub> | `EVAL` `WEAPON` | Global |
| `2026-07-30` | [Anthropic divulga tres incidentes de fuga de evaluaciones](../../incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br><sub>Anthropic discloses three evaluation-breakout incidents</sub> | `EVAL` | Global |
| `2026-07-30` | [Hermes Agent ataca el Ministerio de Finanzas de Tailandia sin supervisión](../../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br><sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub> | `WEAPON` | Sudeste asiático |
| `2026-07-30` | [Unit 42: campañas autónomas dirigidas por operadores de habla china](../../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br><sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub> | `WEAPON` | China Global |
| `2026-08-04` | [Gusano npm CHAINDROP](../../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br><sub>CHAINDROP npm worm</sub> | `SUPPLY` `CRED` | Global |
| `2026-08-06` | [El RCE sin autenticación de Langflow añadido al KEV de CISA](../../incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br><sub>Unauthenticated Langflow RCE added to CISA KEV</sub> | `INFRA` | Global |
| `2026-08-26` | [Trail of Bits: las VM no contendrán a los agentes con capacidad ciber](../../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br><sub>Trail of Bits: VMs won't contain cyber-capable agents</sub> | `EVAL` `SANDBOX` | Global |
| `2026-08-28` | [Comienza la campaña del enjambre de agentes de IA contra PaperCut](../../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br><sub>PaperCut AI agent swarm campaign begins</sub> | `WEAPON` | Global |
| `2026-09-01` | [GitSpawn: un `.git/config` malicioso ejecuta código del atacante en 7 agentes de código antes de contactar siquiera con el modelo](../../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br><sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub> | `SUPPLY` `SANDBOX` | Global |
| `2026-09-02` | [Langflow CVE-2026-0768: el 12.º fallo de Langflow explotado en entornos reales este año](../../incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br><sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub> | `INFRA` `CRED` | Global |
| `2026-09-10` | [Informe de inteligencia de amenazas de Anthropic de septiembre](../../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md)<br><sub>Anthropic September threat intelligence report</sub> | `WEAPON` | Global |
| `2026-09-11` | [Se usó Claude para escanear 1.8 millones de apps de Android en busca de secretos](../../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br><sub>Claude used to scan 1.8 million Android apps for secrets</sub> | `WEAPON` | Global |
| `2026-09-14` | [La AEPD registra la primera notificación de brecha ejecutada por un agente de IA](../../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md)<br><sub>Spain's AEPD receives the first AI-agent-driven breach notification</sub> | `WEAPON` | Europa |
| `2026-09-15` | [Se hace público el ataque del enjambre de agentes de IA contra PaperCut](../../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br><sub>PaperCut AI agent swarm attack made public</sub> | `WEAPON` | Global |
<!-- END:critical -->

## Qué cuenta como registro

Un registro entra si se cumple **al menos una** de estas condiciones:

1. El agente de IA fue **el atacante** — de forma autónoma o dirigido por una persona
2. El agente de IA fue **el objetivo** — inyección, envenenamiento, escape, infraestructura expuesta
3. El agente de IA fue **un eslabón de la cadena de daño** — leyó contenido hostil y actuó en consecuencia
4. Es una **acción regulatoria, legislativa o de un proveedor** directamente sobre seguridad de agentes (registrada como `kind: policy`, no contada como incidente)

**Fuera de alcance:** hallazgos de seguridad de contenido puramente de LLM (conseguir que un modelo diga algo que no debería), vulnerabilidades ordinarias sin relación con agentes, y afirmaciones sin fuente primaria verificable.

Dos categorías se **etiquetan en lugar de eliminarse**:

- `ai_involvement: unverified` — ampliamente reportado como incidente de IA, pero la fuente primaria no menciona IA. Se conserva para que la afirmación sea **buscable junto con su refutación**.
- `ai_involvement: disputed` — el proveedor y la cobertura discrepan; ambas versiones se conservan una al lado de la otra en el registro.

Criterios completos: [docs/scope.md](../../docs/scope.md).

## Calidad de los datos

<!-- BEGIN:quality -->
|  |  |
|---|---|
| Enlaces de fuentes | 578 enlaces de 511 URL únicas |
| Registros sin fuente | **0** — sin fuente no hay registro |
| Grado A (fuente primaria) | 284 |
| Marcados como en disputa | 14 |
| Rondas de verificación | 4 |
<!-- END:quality -->

Las tres primeras rondas comprobaron **cada registro individualmente**. La cuarta hizo una **auditoría de cobertura** y aún encontró alrededor de un 11 % de vacíos. Estas rondas detectan problemas muy distintos: «¿es correcto lo que tenemos?» y «¿está aquí lo que debería estar?» son preguntas separadas y hay que formularlas por separado.

Esas cuatro rondas eliminaron dos entradas inventadas, corrigieron el «administrador de dominio en seis horas» de PaperCut a **siete minutos**, y degradaron Step Finance a grado D porque la cobertura primaria no menciona la IA en absoluto. Cada corrección queda registrada en [docs/data-quality.md](../../docs/data-quality.md) — nada se sobrescribió en silencio.

## Citar

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {330 registros, de 2025-01 a 2026-09; 124 con daño real confirmado},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

Para citar un registro individual, use su `id`; por ejemplo `orca:2026-07-09-openai-agents-breach-huggingface`.

## Contribuir

Las correcciones, los registros faltantes y mejores fuentes son bienvenidos. Tres reglas estrictas:

1. **Cada registro necesita una fuente primaria en la que se pueda hacer clic.** Sin fuente, no hay fusión.
2. **Si tiene dudas, etiquete — no elimine.** Los hechos en disputa reciben `disputed: true` y ambas versiones permanecen en el registro.
3. **Las correcciones van dentro del registro, nunca por encima en silencio.** Diga qué cambió y por qué.

Véase [CONTRIBUTING.md](../../CONTRIBUTING.md). Hay plantillas de issue para [un nuevo registro](../../.github/ISSUE_TEMPLATE/new-incident.yml) y [una corrección](../../.github/ISSUE_TEMPLATE/correction.yml).

## Licencia y descargo de responsabilidad

Con licencia [CC BY 4.0](../../LICENSE) — se requiere atribución. El material de origen enlazado sigue siendo propiedad de sus respectivos titulares.

Este archivo registra **únicamente eventos divulgados públicamente**. No contiene detalles de vulnerabilidades no divulgadas, ni código de explotación, ni herramientas de ataque. La clasificación y la gravedad son el criterio de los editores, no una conclusión oficial de ningún proveedor o regulador. Si usted es una parte afectada y cree que un registro es erróneo, abra un issue — se verificará y se corregirá.

---

<sub><!-- BEGIN:footer -->Generado el 2026-09-19 · 330 registros · 22 meses<!-- END:footer --></sub> · <sub>Estructura: [SCHEMA.md](../../SCHEMA.md) · Datos: [dist/](../../dist/README.md)</sub>
