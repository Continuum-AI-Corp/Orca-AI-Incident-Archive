# Taxonomy

| Page | Description |
|---|---|
| [Type `type`](types.md) | The 12 type codes, and the typical attack chain for each |
| [Severity `severity` / Kind `kind` / Real harm `real_harm`](severity.md) | Incident grading and how the tally is scoped |
| [Confidence `confidence`](confidence.md) | Source-quality grading |

Repositories are advised to use this `type` enumeration (this report is already tagged with it):

| code | Name | Description |
|---|---|---|
| `IPI` | Indirect prompt injection | The payload hides in content the agent will read (email / document / issue / log / web page / calendar / form) |
| `EXFIL` | Data exfiltration | The outcome shape of IPI: image rendering / URL parameters / a server-side proxy carry the data out |
| `SUPPLY` | Supply-chain poisoning | Poisoning of npm / PyPI / VSIX / skill marketplaces / MCP registry |
| `MCP` | MCP & tool-chain | MCP server vulnerabilities, tool poisoning, rug pulls, registry problems |
| `SANDBOX` | Sandbox escape | Escapes, approval bypasses, symlinks, shell boundaries |
| `ROGUE` | Rogue agent action | No external attacker; the agent itself causes the damage |
| `WEAPON` | Agent used as a weapon | The threat actor uses an agent to drive the intrusion |
| `INFRA` | Agent infrastructure exposure | CVEs in Langflow / LiteLLM / Flowise / OpenClaw and the like |
| `CRED` | Credential abuse | API keys / tokens / config files aimed specifically at agents |
| `EVAL` | Evaluation-environment breakout | A frontier model crosses into real systems during a capability evaluation |
| `GOV` | Governance & policy | Laws, directives, litigation, export controls |

`severity`: `critical` / `high` / `medium` / `low`
`region`: `GLOBAL` / `US` / `EU` / `UK` / `JP` / `KR` / `CN` / `TW` / `LATAM` / `SEA` / `AU` / `ME` / `IN`

---

---

[← Back to home](../README.md)
