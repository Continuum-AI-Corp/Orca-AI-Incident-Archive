# Topic · Agent supply-chain poisoning (SUPPLY)

![records](https://img.shields.io/badge/records-57-48545A?style=flat-square) ![type](https://img.shields.io/badge/type-SUPPLY_MCP-B08528?style=flat-square)

> The prose on this page is taken from the archive's original research report; the "All records" table below is compiled automatically from the frontmatter in `incidents/`, and the two are updated together.

**The most important evolution of 2026: malware no longer only steals credentials — it has started writing configuration files for your agent.**

| Date | Event | Evolutionary step | Source |
|---|---|---|---|
| 2025-03 | Rules File Backdoor | 🆕 **first time an agent's rules file was treated as an attack surface** (invisible Unicode) | [Pillar](https://www.pillar.security/blog/new-vulnerability-in-github-copilot-and-cursor-how-hackers-can-weaponize-code-agents) |
| 2025-08-26 | **Nx s1ngularity** | 🆕 **first weaponisation of AI CLIs** — it detected Claude Code / Gemini CLI / Amazon Q and **directed them** to go and find credentials. 2,180 accounts / 7,200 repositories | [Wiz](https://www.wiz.io/blog/s1ngularity-supply-chain-attack) |
| 2025-09-15 | Shai-Hulud v1 (500+ packages) | Theft targets explicitly included `ANTHROPIC_API_KEY`, Claude Code configuration and `.mcp.json`; **npm's first successful self-propagating attack** | [Wiz](https://www.wiz.io/blog/shai-hulud-npm-supply-chain-attack) · [CISA](https://www.cisa.gov/news-events/alerts/2025/09/23/widespread-supply-chain-compromise-impacting-npm-ecosystem) |
| 2025-09-25 | postmark-mcp | 🆕 **the MCP server itself was the backdoor**, silently BCCing about 15,000 emails a day | [Koi](https://www.koi.ai/blog) |
| 2025-11-24 | Shai-Hulud 2.0 (796 packages) | 🆕 moved to the **preinstall stage**, hitting build systems almost 100% of the time; 25,000+ repositories | [Wiz](https://www.wiz.io/blog/shai-hulud-2-0-ongoing-supply-chain-attack) |
| 2026-02-09 | **Clinejection** | 🆕 **broke CI with prompt injection** — issue title → agent triage → RCE → cache poisoning → publishing credentials → **a malicious package actually shipped** | [adnanthekhan](https://adnanthekhan.com/posts/clinejection/#pre-publication) |
| 2026-03-02 | Trivy ecosystem | 🆕 **used the AI coding assistant on the victim's own machine** for egress | [Socket](https://socket.dev/blog/unauthorized-ai-agent-execution-code-published-to-openvsx-in-aqua-trivy-vs-code-extension) |
| 2026-03-24 | **Backdoored LiteLLM release** | 🆕 the target was **the model gateway of agent frameworks** (CrewAI, DSPy and GraphRAG all depend on it) | [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) |
| 2026-03-30 | Axios (v1.14.1/0.30.4) | 🆕 **deepfake social engineering against a maintainer** (UNC1069 / North Korea-linked) | [Google Cloud](https://cloud.google.com/blog/topics/threat-intelligence/north-korea-threat-actor-targets-axios-npm-package/?hl=en) |
| 2026-05-11 | TanStack Mini Shai-Hulud | 🆕 produced malicious packages **with valid SLSA attestations**; included a kill switch + editor persistence hooks; **the author says the software was developed by AI** | [StepSecurity](https://www.stepsecurity.io/blog/mini-shai-hulud-is-back-a-self-spreading-supply-chain-attack-hits-the-npm-ecosystem) |
| 2026-05-18 | Nx Console → 3,800 GitHub repositories | 🆕 **a VS Code extension exposed for only 18 minutes** was enough to get into GitHub's internal estate | [GitHub](https://github.blog/security/investigating-unauthorized-access-to-githubs-internal-repositories/) |
| 2026-06-01 | **Miasma** | 🆕 the "Phantom Gyp" trigger in `binding.gyp`; planted persistence hooks in VS Code / Cursor / **Claude Code** | [safedep](https://safedep.io/miasma-worm-ai-coding-agent-config-injection/) |
| **2026-08-04** | **CHAINDROP** | 🆕 **infection no longer requires `npm install`** — the worm commits malicious `.claude/settings.json` and `.vscode/tasks.json` to reachable repositories, so **opening the repository in VS Code, or starting a single Claude Code session, is enough**; and it came with **valid provenance signatures** | [Elastic](https://www.elastic.co/security-labs/shai-hulud-chaindrop-npm-supply-chain) |

**Conclusion**: files such as `.claude/`, `.cursorrules`, `.mcp.json`, `.vscode/tasks.json`, `AGENTS.md` and `CLAUDE.md`
**are equivalent to executables in the 2026 threat model**, and have to be brought into code review, signing and CI detection.

**Related accidents in the reverse direction — leaked configuration files**:
- 2026-03-31 Anthropic itself shipped the Claude Code source map to npm (510,000 lines) — [The Register](https://www.theregister.com/software/2026/03/31/anthropic-accidentally-exposes-claude-code-source-code/5227940)
- 2026-04-30 Apple shipped an internal `CLAUDE.md` in the production build of Support App v5.13 — [X](https://x.com/aaronp613/status/2049986504617820551)

---

<!-- BEGIN:incidents -->
## All records (58)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-02-06` | [Hugging Face "nullifAI" malicious models](../incidents/2025-02/2025-02-06-hugging-face-nullifai.md) | `SUPPLY` | **High** | A | — |
| `2025-03-18` | [Cursor / Copilot "Rules File Backdoor"](../incidents/2025-03/2025-03-18-cursor-copilot-rules-file.md) | `SUPPLY` | **High** | A | — |
| `2025-04-01` | [GPT-4.1 jailbroken through a poisoned MCP tool](../incidents/2025-04/2025-04-01-gpt-mcp-jing-gong-ju.md) | `MCP` | Medium | A | — |
| `2025-04-01` | [First systematic disclosure of MCP tool-poisoning attacks](../incidents/2025-04/2025-04-01-mcp-tpa-gong-ju-tou.md) | `MCP` | Medium | A | — |
| `2025-04-01` | ["Slopsquatting" gets its name](../incidents/2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md) | `SUPPLY` | Info | A | · |
| `2025-05-26` | [GitHub MCP "toxic agent flow"](../incidents/2025-05/2025-05-26-github-mcp-toxic-agent.md) | `MCP` `EXFIL` | Medium | A | — |
| `2025-06-04` | [Asana MCP server cross-tenant data exposure](../incidents/2025-06/2025-06-04-asana-mcp-server.md) ⚠️ | `MCP` | Medium | B | ✅ |
| `2025-06-13` | [MCP Inspector unauthenticated RCE](../incidents/2025-06/2025-06-13-mcp-inspector-rce.md) | `MCP` | **High** | A | — |
| `2025-06-13` | [Smithery.ai path traversal](../incidents/2025-06/2025-06-13-smithery-ai-lu-jing-chuan-yue.md) | `MCP` `CRED` | Medium | B | — |
| `2025-07-01` | [Anthropic Filesystem MCP sandbox escape](../incidents/2025-07/2025-07-01-anthropic-filesystem-mcp.md) | `MCP` | Medium | A | — |
| `2025-07-01` | [mcp-remote OAuth command injection](../incidents/2025-07/2025-07-01-mcp-remote-oauth.md) | `MCP` | Medium | A | — |
| `2025-07-06` | [Supabase MCP prompt injection dumps a private table](../incidents/2025-07/2025-07-06-supabase-mcp-ti-shi-zhu.md) | `MCP` | **High** | A | — |
| `2025-07-13` | ★ [Amazon Q Developer extension poisoned](../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md) | `SUPPLY` `ROGUE` | **Critical** | A | ✅ |
| `2025-08-05` | [Cursor MCPoison (CVE-2025-54136)](../incidents/2025-08/2025-08-05-cursor-mcpoison.md) | `MCP` | **High** | A | — |
| `2025-08-08` | ★ [Salesloft Drift OAuth token theft](../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2025-08-26` | ★ [Nx "s1ngularity"](../incidents/2025-08/2025-08-26-nx-s1ngularity.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2025-09-03` | [Claude Code MCP auto-enable bypass](../incidents/2025-09/2025-09-03-claude-code-mcp.md) | `MCP` | **High** | A | — |
| `2025-09-15` | ★ [Shai-Hulud npm worm v1](../incidents/2025-09/2025-09-15-shai-hulud-npm.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2025-09-25` | [postmark-mcp malicious npm package](../incidents/2025-09/2025-09-25-postmark-mcp-npm.md) | `MCP` `SUPPLY` | **High** | A | ✅ |
| `2025-10-01` | [Framelink Figma MCP RCE](../incidents/2025-10/2025-10-01-framelink-figma-mcp-rce.md) | `MCP` | Medium | A | — |
| `2025-10-22` | [Shadow Escape: first zero-click agent attack over MCP](../incidents/2025-10/2025-10-22-shadow-escape-mcp-agent.md) | `MCP` `EXFIL` | **High** | A | — |
| `2025-11-21` | ★ [Shai-Hulud 2.0](../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2025-12-01` | [Three CVEs in Anthropic's Git MCP Server](../incidents/2025-12/2025-12-01-anthropic-git-mcp-server.md) ⚠️ | `MCP` | Medium | A | — |
| `2025-12-01` | [MCP TypeScript SDK DNS rebinding](../incidents/2025-12/2025-12-01-mcp-typescript-sdk-dns.md) | `MCP` | Medium | A | — |
| `2025-12-06` | [IDEsaster](../incidents/2025-12/2025-12-06-idesaster.md) | `SANDBOX` `MCP` | Medium | A | — |
| `2026-01-25` | [Malicious ClawHub skills surge](../incidents/2026-01/2026-01-25-clawhub-skill-e-yi-ji.md) | `SUPPLY` | **High** | B | ✅ |
| `2026-02-01` | [ClawHavoc campaign](../incidents/2026-02/2026-02-01-clawhavoc-zhan-yi.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-02-09` | ★ [Clinejection](../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | **Critical** | A | ✅ |
| `2026-03-01` | ★ [Hades: a sustained campaign turning AI coding assistants into the attack surface](../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-03-02` | [Sustained supply-chain compromise across the Trivy ecosystem](../incidents/2026-03/2026-03-02-trivy-sheng-tai-chi-xu.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-03-10` | [Azure MCP Server SSRF privilege escalation (CVE-2026-26118)](../incidents/2026-03/2026-03-10-azure-mcp-server-ssrf.md) | `MCP` | Medium | A | — |
| `2026-03-24` | ★ [Backdoored LiteLLM release](../incidents/2026-03/2026-03-24-litellm-backdoored-release.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-03-30` | ★ [Axios npm package compromised](../incidents/2026-03/2026-03-30-axios-npm-compromised.md) | `SUPPLY` | **Critical** | A | ✅ |
| `2026-04-15` | [Windsurf zero-click MCP RCE (CVE-2026-30615)](../incidents/2026-04/2026-04-15-windsurf-mcp-rce.md) | `SANDBOX` `MCP` | **High** | A | — |
| `2026-04-16` | ★ [MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild](../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md) | `MCP` `INFRA` | **Critical** | A | ✅ |
| `2026-04-19` | [Vercel OAuth supply-chain intrusion](../incidents/2026-04/2026-04-19-vercel-oauth-gong-ying-lian.md) | `SUPPLY` `CRED` | **High** | A | ✅ |
| `2026-04-24` | [Gemini CLI CVSS 10.0: one pull request compromises CI](../incidents/2026-04/2026-04-24-gemini-cli-pr-ci.md) | `SANDBOX` `SUPPLY` | **High** | A | — |
| `2026-05-01` | [Fake OpenAI repository tops the Hugging Face trending list](../incidents/2026-05/2026-05-01-hugging-face-jia-mao-cang.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-05-07` | [TrustFall: RCE on a single keypress](../incidents/2026-05/2026-05-07-trustfall-rce-yi-ci-hui.md) | `SANDBOX` `MCP` | Medium | A | — |
| `2026-05-11` | ★ [TanStack npm "Mini Shai-Hulud"](../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-05-13` | [OpenAI staff devices compromised via the TanStack incident](../incidents/2026-05/2026-05-13-tanstack-yuan-gong-she-bei.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-05-18` | ★ [3,800 internal GitHub repositories compromised](../incidents/2026-05/2026-05-18-github-3800-internal-repos.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-05-18` | [Megalodon: malicious Actions injected into 5,500+ GitHub repositories](../incidents/2026-05/2026-05-18-megalodon-github-actions.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-05-19` | ★ [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-05-21` | ★ [Composio: agent automation itself becomes the privilege-escalation path](../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md) | `CRED` `SUPPLY` | **Critical** | A | ✅ |
| `2026-06-01` | ★ [Miasma worm](../incidents/2026-06/2026-06-01-miasma-worm.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-06-12` | [Agentjacking: one public DSN hijacks AI coding agents](../incidents/2026-06/2026-06-12-agentjacking-public-dsn.md) | `MCP` `IPI` | **High** | A | — |
| `2026-06-15` | [Innocuous-looking GitHub repos make agents open a reverse shell](../incidents/2026-06/2026-06-15-github-agent-shell.md) | `SUPPLY` | Medium | A | — |
| `2026-06-17` | ★ [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-06-18` | [ClickFix malvertising abuses claude.ai shared conversations](../incidents/2026-06/2026-06-18-clickfix-claude-ai-e-yi-guang.md) | `SUPPLY` | **High** | A | ✅ |
| `2026-07-01` | [AWS Kiro: ask it to summarise a web page, get RCE (CVE-2026-10591)](../incidents/2026-07/2026-07-01-aws-kiro-rce.md) | `MCP` `SANDBOX` | **High** | A | — |
| `2026-07-30` | [RufRoot (CVE-2026-59726): perfect CVSS, summons a rogue AI swarm](../incidents/2026-07/2026-07-30-rufroot-man-fen-zhao-huan.md) | `MCP` `INFRA` | **High** | A | — |
| `2026-08-04` | ★ [CHAINDROP npm worm](../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md) | `SUPPLY` `CRED` | **Critical** | A | ✅ |
| `2026-08-05` | [AWS Transform MCP arbitrary file write](../incidents/2026-08/2026-08-05-aws-transform-mcp.md) | `MCP` | **High** | A | — |
| `2026-08-17` | [AI finds a flaw AI helped write: Snowflake's Jira token](../incidents/2026-08/2026-08-17-snowflake-jira-zhao-dao-can.md) | `CRED` `SUPPLY` | **High** | A | ✅ |
| `2026-08-18` | [Context7 MCP prompt injection (CVE-2026-75130)](../incidents/2026-08/2026-08-18-context7-mcp-ti-shi-zhu.md) | `MCP` `CRED` | **High** | A | — |
| `2026-09-01` | ★ [GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted](../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md) | `SUPPLY` `SANDBOX` | **Critical** | A | — |
| `2026-09-11` | [Researchers link OpenAI agents to the RubyGems "GemStuffer" campaign](../incidents/2026-09/2026-09-11-rubygems-gemstuffer.md) ⚠️ | `EVAL` `SUPPLY` | **High** | D | ✅ |
<!-- END:incidents -->

---

[← All topics](../README.md) · [Archive index](../README.md)
