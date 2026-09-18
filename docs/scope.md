# Scope

This scan uses a **wide net**: all six categories are collected, so that you can narrow them down as needed:

| # | Category | Is it an "agent attack incident"? | Recommendation |
|---|---|---|---|
| ① | **Agents attacked**: indirect prompt injection, tool poisoning, sandbox escape, approval bypass — leading to a real data leak or a compromised system | ✅ Core | Must include |
| ② | **Agents as weapons**: attackers use AI agents to carry out an intrusion | ✅ Core | Must include |
| ③ | **Agents crossing the line on their own**: no malicious operator; the agent itself causes damage | ✅ Core | Must include |
| ④ | **Agent supply chain**: MCP servers / skill marketplaces / npm-PyPI / IDE extensions poisoned, **aimed specifically at agent credentials and configs** | ✅ Core | Must include |
| ⑤ | **Agent infrastructure vulnerabilities**: runtime CVEs and in-the-wild exploitation in Langflow / LiteLLM / OpenClaw / Flowise and the like | ⚠️ Borderline | Recommended, tagged `infra` |
| ⑥ | **General AI incidents**: deepfake fraud, chatbot data leaks, model-jailbreak research, harm from AI hallucinations | ❌ Not agent | Keep only those **with an agent element** |

> **Deliberately excluded**: pure deepfake fraud, pure LLM-jailbreak papers, AI-hallucinated legal citations, autonomous-driving accidents, AI-generated pornography and the like.
> Of the 148 entries the AI Incident Database added in 2026 May–July, only **11** fall within this repository's scope — a ratio showing that **a general AI incident database and an agent-security database are not the same thing**, and that Orca's positioning holds.
> Source: [AIID 2026 May–July Roundup](https://incidentdatabase.ai/blog/incident-report-2026-may-june-july/)

## Collection path

- **Primary: structured official compilations** (highest quality)
  - Japan's IPA [AI Security Bulletin](https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html), six issues: 2025-07 / 2025-09 / 2025-12 / 2026-03 / 2026-06 / 2026-08 — **every item carries a primary-source URL, and confidence is graded** (government disclosure / affected-party disclosure / vendor observation / demonstration in a test environment). **317 primary-source URLs** were extracted from it for this scan
  - OWASP GenAI Incident & Exploit Round-up: [Jan-Feb'25](https://genai.owasp.org/2025/03/06/owasp-gen-ai-incident-exploit-round-up-jan-feb-2025/) · [Q2'25](https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/) · [Q1'26](https://genai.owasp.org/2026/04/14/owasp-genai-exploit-round-up-report-q1-2026/)
- **Primary: vendor / government / CERT advisories** — Anthropic, OpenAI, Google GTIG, Microsoft MSRC/MSTIC, AWS, Hugging Face, GitHub, Vercel, Cisco, NVIDIA, Wiz, CISA, UK AISI, Europol, METR, CNVD
- **Secondary: security research organisations** — Zenity, Noma, Varonis, PromptArmor, Check Point, Unit 42, Tenable, Trend Micro, Sysdig, Koi, Legit, Pillar, Adversa, Invariant, Radware, AppOmni, SentinelLABS, Elastic, Hunt.io, Sygnia, Oligo, Capsule, Dream, Straiker, 0DIN, Orca Security
- **Secondary: media** — Bloomberg, Reuters, Ars Technica, The Register, Krebs, 404 Media, BleepingComputer, TechCrunch, CNBC, CNN, CyberScoop, ABC (AU), ITmedia, Xinhua, Boannews, SecRSS

---

[← Back to home](../README.md) · [Data quality](data-quality.md)
