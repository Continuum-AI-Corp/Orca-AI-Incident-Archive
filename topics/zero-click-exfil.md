# Topic · Zero-click data exfiltration chain (IPI + EXFIL)

![records](https://img.shields.io/badge/records-57-48545A?style=flat-square) ![type](https://img.shields.io/badge/type-IPI_EXFIL-B08528?style=flat-square)

> The prose on this page is taken from the archive's original research report; the "All records" table below is compiled automatically from the frontmatter in `incidents/`, and the two are updated together.

The same pattern was replicated 13 times over 15 months, across 6 vendors. **This is the most mature attack surface in agent security and the hardest to eradicate.**

| Name | Date | Product | Injection point | Exfiltration channel | CVSS | Source |
|---|---|---|---|---|---|---|
| **EchoLeak** | 2025-06 | M365 Copilot | Email | Teams content URL API + reference-style Markdown images | 9.3 | [THN](https://thehackernews.com/2025/06/zero-click-ai-vulnerability-exposes.html) |
| **AgentFlayer** | 2025-08 | ChatGPT Connectors and 4 other vendors | 1px white text in a shared document | Image render URL → Azure Blob | — | [Zenity](https://labs.zenity.io/p/agentflayer-chatgpt-connectors-0click-attack-5b41) |
| **ShadowLeak** | 2025-09 | ChatGPT Deep Research | Email HTML | **Server-side** direct egress (invisible on the endpoint) | — | [Radware](https://www.radware.com/getattachment/7bf74537-e90e-414e-a82b-d7b4935bae08/Threat-Advisory-ShadowLeak-Sept-2025.pdf.aspx) |
| **Notion triple** | 2025-09 | Notion 3.0 | White-text PDF | The URL parameter capability of `functions.search()` | — | [CodeIntegrity](https://www.codeintegrity.ai/blog/notion) |
| **ForcedLeak** | 2025-09 | Salesforce Agentforce | Public Web-to-Lead form | **Bought an expired CSP-allowlisted domain** ($5) | 9.4 | [Noma](https://noma.security/blog/forcedleak-agent-risks-exposed-in-salesforce-agentforce) |
| **CamoLeak** | 2025-10 | GitHub Copilot Chat | HTML comment in a PR description | **GitHub's own Camo image proxy**, encoded character by character | 9.6 | [Legit](https://www.legitsecurity.com/blog/camoleak-critical-github-copilot-vulnerability-leaks-private-source-code) |
| **Reprompt** | 2026-01 | Copilot Personal | The `q` parameter in a URL | Dual requests + chained requests | — | [Varonis](https://www.varonis.com/blog/reprompt) |
| **Superhuman** | 2026-01 | Superhuman AI | Email / web page | Google Forms pre-fill link + Markdown images | — | [PromptArmor](https://www.promptarmor.com/resources/superhuman-ai-exfiltrates-emails) |
| **CellShock** | 2026-03 | Claude for Excel / Ramp | External dataset | `=IMAGE()` formula (**abusing a normal spreadsheet feature**) | — | [PromptArmor](https://www.promptarmor.com/resources/cellshock-claude-ai-is-excel-lent-at-stealing-data) |
| **GrafanaGhost** | 2026-04 | Grafana | External resource | URL parameters | — | [OWASP Q1'26](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/) |
| **ShareLeak / PipeLeak** | 2026-04 | Copilot Studio / Agentforce | SharePoint form / lead form | Outlook email | 7.5 / no CVE | [Capsule](https://www.capsulesecurity.io/blog-post/shareleak-taking-the-wheel-of-microsofts-copilot-studio-cve-2026-21520) |
| **Copilot Cowork** | 2026-05 | M365 Copilot Cowork | Skill file at a user-controllable path | Pre-authenticated download link **auto-approved and sent to the user themselves** | — | [PromptArmor](https://www.promptarmor.com/resources/microsoft-copilot-cowork-exfiltrates-files) |
| **SearchLeak** | 2026-06 | M365 Copilot Enterprise | The `q` parameter in a search URL | **`*.bing.com` is on the CSP allowlist, so Bing's server-side fetch bypasses the browser CSP** | MSRC 6.5 / Varonis calls it critical | [Varonis](https://www.varonis.com/blog/searchleak) |
| **GitLost** | 2026-07 | GitHub Agentic Workflows | Issue in a public repository in the same organisation | Posted as a public comment (**every permission in the combination is legitimate on its own**) | — | [Noma](https://noma.security/blog/gitlost-how-we-tricked-githubs-ai-agent-into-leaking-private-repos/) |

**The one thing defenders should remember**: these exfiltration channels are **almost all the vendors' own trusted domains** (Teams API, Camo proxy, Bing, Azure Blob, Google Forms, Outlook).
**CSP and domain allowlists largely stop working in the agent setting, because an agent needs to reach too many things.**

---

<!-- BEGIN:incidents -->
## All records (57)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-05-01` | [GitLab Duo remote prompt injection](../incidents/2025-05/2025-05-01-gitlab-duo-yuan-cheng-ti.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-05-26` | [GitHub MCP "toxic agent flow"](../incidents/2025-05/2025-05-26-github-mcp-toxic-agent.md) | `MCP` `EXFIL` | Medium | A | — |
| `2025-06-11` | [EchoLeak (CVE-2025-32711)](../incidents/2025-06/2025-06-11-echoleak.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-08-01` | ["Man in the Prompt" browser-extension attack](../incidents/2025-08/2025-08-01-man-prompt-liu-lan-qi.md) | `IPI` | Medium | B | — |
| `2025-08-06` | [AgentFlayer zero-click attack set (Black Hat USA)](../incidents/2025-08/2025-08-06-agentflayer-black-hat-usa.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-08-06` | [SafeBreach "Invitation Is All You Need"](../incidents/2025-08/2025-08-06-safebreach-invitation-is-all.md) | `IPI` | **High** | A | — |
| `2025-09-18` | [ShadowLeak](../incidents/2025-09/2025-09-18-shadowleak.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-09-19` | [Notion 3.0 agent hits the lethal trifecta](../incidents/2025-09/2025-09-19-notion-agent-zhi-ming-san.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-09-25` | [ForcedLeak (Salesforce Agentforce)](../incidents/2025-09/2025-09-25-forcedleak-salesforce-agentforce.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-09-30` | [Gemini "Trifecta"](../incidents/2025-09/2025-09-30-gemini-trifecta.md) | `IPI` `EXFIL` | Medium | A | — |
| `2025-10-02` | [CometJacking](../incidents/2025-10/2025-10-02-cometjacking.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-10-08` | [CamoLeak (GitHub Copilot Chat)](../incidents/2025-10/2025-10-08-camoleak-github-copilot-chat.md) | `IPI` `EXFIL` | **High** | A | — |
| `2025-10-21` | [Brave discloses screenshot-based injection in Comet](../incidents/2025-10/2025-10-21-brave-comet-pi-lu-jie.md) | `IPI` | Medium | A | — |
| `2025-10-22` | [Shadow Escape: first zero-click agent attack over MCP](../incidents/2025-10/2025-10-22-shadow-escape-mcp-agent.md) | `MCP` `EXFIL` | **High** | A | — |
| `2025-10-24` | [Atlas omnibox jailbreak](../incidents/2025-10/2025-10-24-atlas-omnibox-yue-yu.md) | `IPI` | Medium | A | — |
| `2025-10-27` | [Atlas "poisoned memory"](../incidents/2025-10/2025-10-27-atlas-wu-ran-ji-yi.md) | `IPI` | Medium | B | — |
| `2025-10-30` | [Anthropic confirms a prompt-injection flaw in Claude](../incidents/2025-10/2025-10-30-anthropic-claude-que-ren-cun.md) | `IPI` | Medium | A | — |
| `2025-10-31` | [Agent Session Smuggling: agents deceiving agents over A2A](../incidents/2025-10/2025-10-31-agent-session-smuggling-a2a.md) | `IPI` | Medium | A | — |
| `2025-11-20` | [ServiceNow Now Assist second-order prompt injection](../incidents/2025-11/2025-11-20-servicenow-now-assist.md) | `IPI` | Medium | A | — |
| `2025-12-29` | [Copilot Studio "Connected Agents" can carry invisible backdoors](../incidents/2025-12/2025-12-29-copilot-studio-connected-agents.md) | `IPI` | Medium | A | — |
| `2026-01-07` | [Four productivity tools hit the lethal trifecta in nine days](../incidents/2026-01/2026-01-07-lethal-trifecta-four-tools.md) | `IPI` | Medium | B | — |
| `2026-01-12` | [Claude Cowork ships with known vulnerabilities](../incidents/2026-01/2026-01-12-claude-cowork-dai-zhe-zhi.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-01-12` | [Superhuman AI indirect prompt injection](../incidents/2026-01/2026-01-12-superhuman-jian-jie-ti-shi.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-01-14` | [Microsoft Copilot Personal "Reprompt"](../incidents/2026-01/2026-01-14-microsoft-copilot-personal-reprompt.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-02-09` | ★ [Clinejection](../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | **Critical** | A | ✅ |
| `2026-03-01` | [Claudy Day: a three-flaw chain in claude.ai](../incidents/2026-03/2026-03-01-claudy-day-claude-ai.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-03-16` | [CellShock: data exfiltration through an AI spreadsheet tool](../incidents/2026-03/2026-03-16-cellshock-biao-ge-gong-ju.md) | `IPI` `EXFIL` | Medium | A | — |
| `2026-04-01` | [Three CVEs in the Claude Code GitHub Action: a PR title steals your API key](../incidents/2026-04/2026-04-01-claude-code-github-action.md) | `IPI` `CRED` | **High** | A | — |
| `2026-04-07` | [GrafanaGhost indirect prompt injection](../incidents/2026-04/2026-04-07-grafanaghost-jian-jie-ti-shi.md) | `IPI` `EXFIL` | Medium | A | — |
| `2026-04-15` | [ShareLeak (CVE-2026-21520) and PipeLeak](../incidents/2026-04/2026-04-15-shareleak-pipeleak.md) ⚠️ | `IPI` `EXFIL` | **High** | A | — |
| `2026-04-17` | [Meta AI support bot tricked into handing over an Instagram account](../incidents/2026-04/2026-04-17-meta-instagram-ke-fu-ji.md) | `IPI` `CRED` | **High** | A | ✅ |
| `2026-05-04` | [Grok / Bankrbot Morse-code prompt injection](../incidents/2026-05/2026-05-04-grok-bankrbot-mo-er-si.md) | `IPI` `ROGUE` | **High** | A | — |
| `2026-05-12` | [Brazilian labour court sanctions lawyers over prompt injection](../incidents/2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md) | `IPI` `GOV` | **High** | A | ✅ |
| `2026-05-12` | [ClaudeBleed: a zero-permission extension hijacks Claude for Chrome](../incidents/2026-05/2026-05-12-claudebleed-claude-chrome.md) | `IPI` `CRED` | Medium | B | — |
| `2026-05-22` | [Google AI Search "disregard" bug](../incidents/2026-05/2026-05-22-google-disregard-bug.md) | `IPI` | Medium | A | — |
| `2026-05-26` | [Microsoft Copilot Cowork file exfiltration](../incidents/2026-05/2026-05-26-microsoft-copilot-cowork.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-06-01` | ★ [Attackers simply ask Meta's AI support bot for Instagram accounts](../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md) | `IPI` `CRED` | **Critical** | A | ✅ |
| `2026-06-08` | [AgentForger: one link forges an "AI insider"](../incidents/2026-06/2026-06-08-agentforger-yi-tiao-lian-jie.md) | `IPI` `CRED` | Medium | A | — |
| `2026-06-12` | [Agentjacking: one public DSN hijacks AI coding agents](../incidents/2026-06/2026-06-12-agentjacking-public-dsn.md) | `MCP` `IPI` | **High** | A | — |
| `2026-06-15` | [SearchLeak (CVE-2026-42824)](../incidents/2026-06/2026-06-15-searchleak.md) | `IPI` `EXFIL` | Medium | A | — |
| `2026-06-24` | [BioShocking: dumb the agent down first, then take the password](../incidents/2026-06/2026-06-24-bioshocking-agent-xian-jiao-sha.md) | `IPI` `CRED` | Medium | A | — |
| `2026-07-02` | ★ [Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)](../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md) | `IPI` `ROGUE` | **Critical** | A | ✅ |
| `2026-07-07` | [GitLost: GitHub Agentic Workflows leak private repositories](../incidents/2026-07/2026-07-07-gitlost-github-agentic-workflows.md) | `IPI` `EXFIL` | Medium | A | — |
| `2026-08-11` | [GhostSplice: splitting one refused request across three trusted channels takes compliance from 42% to 82%](../incidents/2026-08/2026-08-11-ghostsplice-cross-channel-fragmentation.md) | `MCP` `IPI` `EXFIL` | **High** | B | — |
| `2026-08-18` | [CoSnitch (CVE-2026-24301)](../incidents/2026-08/2026-08-18-cosnitch.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-08-19` | [Grok "cryptographic context injection": encrypted instructions, plaintext data](../incidents/2026-08/2026-08-19-grok-mi-ma-xue-wen.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-09-08` | [ChatGPT sandbox flaw pipes a victim's Gmail data into the attacker's account](../incidents/2026-09/2026-09-08-chatgpt-gmail-sha-xiang-que.md) | `EXFIL` | **High** | A | ✅ |
| `2026-09-08` | [Infostealers turn to AI-agent data: collection rules now target Claude, Cursor and Codex](../incidents/2026-09/2026-09-08-gen-digital-infostealers-ai-agent-data.md) | `CRED` `EXFIL` | Medium | A | — |
| `2026-09-09` | [Workflow identity hijacking: Noma Labs turns an ordinary support email into privileged data access](../incidents/2026-09/2026-09-09-noma-workflow-identity-hijacking.md) | `INFRA` `EXFIL` | Medium | A | — |
| `2026-09-16` | [BragJack: one browser extension hijacks the AI agents in five major browsers](../incidents/2026-09/2026-09-16-bragjack-browser-agents.md) | `SUPPLY` `IPI` | **High** | B | — |
| `2026-09-18` | [Zhipu's ZCode agent silently uploaded whole repositories, Git history included](../incidents/2026-09/2026-09-18-zcode-silent-upload.md) | `EXFIL` | **High** | A | ✅ |
| `2026-09-20` | [Tencent BrowserSkill: any 32-character extension origin can pose as the browser client and feed the agent forged pages](../incidents/2026-09/2026-09-20-tencent-browserskill-origin-bypass.md) | `IPI` `INFRA` | Medium | A | — |
| `2026-09-23` | [Dark Sourcery: attackers poison chatbot answers across 374 companies](../incidents/2026-09/2026-09-23-dark-sourcery-chatbot-poisoning.md) | `IPI` | **High** | B | ✅ |
| `2026-09-23` | [IBM FTM: unauthenticated RAG poisoning could steer the payment agent's MCP tools](../incidents/2026-09/2026-09-23-ibm-ftm-rag-poisoning.md) | `IPI` `INFRA` | Medium | A | — |
| `2026-09-24` | [Manus: a JSFuck-obfuscated email beat the agent's filter, executed a payload and exposed connected app tokens](../incidents/2026-09/2026-09-24-manus-email-prompt-injection-rce.md) | `IPI` `CRED` | **High** | B | — |
| `2026-09-24` | [SalesBleed: three Agentforce flaws turn a single web lead into zero-click CRM exfiltration and agent-impersonated phishing](../incidents/2026-09/2026-09-24-salesbleed-agentforce-zero-click-exfil.md) | `IPI` `EXFIL` | **High** | A | — |
| `2026-09-25` | [Zammad: crafted text in an AI Agent field bypasses the sanitizer and runs commands on the server](../incidents/2026-09/2026-09-25-zammad-ai-agent-template-rce.md) | `IPI` `INFRA` | Medium | A | — |
<!-- END:incidents -->

---

[← All topics](../README.md) · [Archive index](../README.md)
