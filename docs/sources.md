# Sources

The archive currently cites **447** unique URLs across **513** links.

## Always subscribed (grade A)

| Source | Frequency | Why |
|---|---|---|
| **[IPA's AI Security Bulletin](https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html)** | about every 2 months | **The single highest-quality source in this scan.** Four viewpoints, every item with a primary-source URL, and confidence graded (government disclosure / affected-party disclosure / vendor observation / demonstration in a test environment). 317 primary-source URLs were extracted from it for this scan |
| **[Anthropic Threat Intelligence](https://www.anthropic.com/threat-intelligence)** | about every 6 months | The GTG numbering system; 2025-04 / 2025-08 / 2025-11 / 2026-09 |
| **[red.anthropic.com](https://red.anthropic.com/)** | irregular | N-day, exploit-evals, attack-navigator, zero-days, mythos-preview |
| **[OpenAI Disrupting Malicious Uses](https://openai.com/global-affairs/)** | quarterly | 2025-02 / 2025-06 / 2025-10 / 2026-02 |
| **[Google GTIG AI Threat Tracker](https://cloud.google.com/blog/topics/threat-intelligence/)** | about every 6 months | 2025-11 / 2026-02 / 2026-05; the naming authority for malware families |
| **[Microsoft Security Blog](https://www.microsoft.com/en-us/security/blog/)** | high frequency | AI as tradecraft, ChainDrop, AutoJack, SesameOp |
| **[OWASP GenAI Round-up](https://genai.owasp.org/category/articles/)** | quarterly | Aligned with the OWASP Top 10 categories |
| **[CISA KEV](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) + BOD** | continuous | Langflow, LiteLLM and others have entered KEV |
| **[UK AISI Blog](https://www.aisi.gov.uk/)** | irregular | BPJ, model evaluations, self-disclosed incidents |
| **[CSA Lab Space](https://labs.cloudsecurityalliance.org/)** | irregular | Cross-case analysis of incidents |
| **[Permission Protocol tracker](https://www.permissionprotocol.com/agent-incident-tracker)** | continuous | 135 entries, the most diligently updated, but **every one must be traced back to a primary source** |

## Research organisations (grade B)

**Focused on agent exfiltration chains**: PromptArmor, Zenity Labs, Noma Security, Varonis, CodeIntegrity, Capsule Security
**Coding agents / IDEs**: Wiz, Pillar Security, Adversa, Check Point Research, Orca Security, 0DIN (Mozilla)
**MCP / infrastructure**: Oligo, Invariant Labs, Tenable, General Analysis
**Threat intelligence**: Palo Alto Unit 42, Trend Micro / ZDI, Sysdig, SentinelLABS, Elastic Security Labs, Hunt.io, Sygnia, CrowdStrike, Dream
**Supply chain**: StepSecurity, Aikido, safedep, Socket, Koi Security
**Other**: Radware, AppOmni, Legit Security, Straiker, Rebora Security, Frontier Security, CodeWall, SafeBreach, LayerX, Brave, NeuralTrust, HiddenLayer

## Peer projects

| Project | Scale | Distinctive feature | Where Orca can differentiate |
|---|---|---|---|
| [`webpro255/awesome-ai-agent-attacks`](https://github.com/webpro255/awesome-ai-agent-attacks) | 50+ entries, 73 stars | Timeline-style README | Single file, no structured data, no API |
| [`h5i-dev/awesome-ai-agent-incidents`](https://github.com/h5i-dev/awesome-ai-agent-incidents) | 22 entries | Comes with a table | Small, **and includes unverified entries** (the "EchoLeak US$200M impact" claim comes from this table) |
| [`kindrat86/ai-agent-incident-database`](https://github.com/kindrat86/ai-agent-incident-database) | 95 records, $557M in losses | **Has JSON/CSV/JSONL exports**, CC BY 4.0 | Already good, **but weighted toward the "loss amount" dimension** |
| [`permissionprotocol.com`](https://www.permissionprotocol.com/agent-incident-tracker) | **135 entries** (60 real + 75 controlled demos) | Classified by permission gate, marking whether an independent gate would stop it | **The highest-quality competitor**, but a commercial site and not open source; and some entries cannot be traced back to a primary source |
| [`incidentdatabase.ai`](https://incidentdatabase.ai/) (AIID) | 1,600+ entries | Academic level, with a numbering system | **General AI incidents, with a very low agent share** (only 11 of the 148 entries in 2026 May–July) |
| [`rafter.so` timeline](https://rafter.so/blog/incidents/ai-agent-security-timeline-2025-2026) | about 15 entries | Mainly CVEs, neatly formatted | Commercial blog |

**Where Orca should sit (four unoccupied slots)**:
1. **Monthly granularity + coverage of six world regions** — no other project slices by region, and the China / Japan / Korea / Europe-US / Taiwan coverage is unique
2. **A clear distinction between "real victim" and "lab demo"** — permissionprotocol is the only one that does this, but it is a commercial site
3. **Confidence grading + conflicting numbers side by side + a corrections log** — a shared weakness of every existing project (a lot of AI-generated content copies one another; §13 of this report records 3 specific contamination cases)
4. **Archiving the original transcript** (following the `mythos-5-incident-transcript` convention) — no project does this

---

---

[← Back to home](../README.md) · [Data quality](data-quality.md)
