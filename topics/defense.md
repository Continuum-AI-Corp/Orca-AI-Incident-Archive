# Topic · Defense-side progress (for contrast)

![records](https://img.shields.io/badge/records-51-48545A?style=flat-square) ![type](https://img.shields.io/badge/type-GOV-B08528?style=flat-square)

> The prose on this page is taken from the archive's original research report; the "All records" table below is compiled automatically from the frontmatter in `incidents/`, and the two are updated together.

An archive that records only incidents will be lopsided, so we suggest adding a `defense` branch for:

| Date | Project | Organisation | Source |
|---|---|---|---|
| 2025-12 | Shannon autonomous white-box pentest framework (96.15% on the XBOW benchmark) | Keygraph | [GitHub](https://github.com/KeygraphHQ/shannon) |
| 2026-01-30 | Constitutional Classifiers++ (40× cheaper, 0.05% false refusal rate) | Anthropic | [Anthropic](https://www.anthropic.com/research/next-generation-constitutional-classifiers) |
| 2026-02-20 | Claude Code Security limited preview | Anthropic | [Anthropic](https://www.anthropic.com/news/claude-code-security) |
| 2026-03-06 | Codex Security (formerly Aardvark); alerts down 84%, false positives down 50%+ | OpenAI | [OpenAI](https://openai.com/ja-JP/index/codex-security-now-in-research-preview/) |
| 2026-03-06 | Using Opus 4.6 to find 22 vulnerabilities in Firefox (14 severe) → Firefox 148 | Anthropic + Mozilla | [Mozilla](https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/) · [Anthropic](https://www.anthropic.com/news/mozilla-firefox-security) |
| 2026-03-09 | Claude Code's Code Review (parallel multi-agent PR analysis) | Anthropic | [Claude](https://claude.com/blog/code-review) |
| 2026-04-07 | **Project Glasswing** (with AWS/Google/Microsoft taking part) | Anthropic | [Anthropic](https://www.anthropic.com/glasswing) |
| 2026-04-30 | Claude Security public beta | Anthropic | [Claude](https://claude.com/blog/claude-security-public-beta) |
| 2026-05-04 | deepsec, an open-source agent-driven vulnerability scanner | Vercel | [Vercel](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base) |
| 2026-05-11 | **Daybreak** | OpenAI | [OpenAI](https://openai.com/ja-JP/daybreak/) |
| 2026-05-12 | **MDASH** (100+ specialised agents; 16 vulnerabilities in the Windows network stack, 4 Critical RCEs; 88.45% on CyberGym) | Microsoft | [Microsoft](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/) |
| 2026-05-21 | GPT-5.5-Cyber (via the Trusted Access for Cyber program; introduction already discussed with the Japanese government) | OpenAI | [OpenAI](https://openai.com/ja-JP/index/gpt-5-5-with-trusted-access-for-cyber/) · [Yomiuri Shimbun](https://www.yomiuri.co.jp/economy/20260521-GYT1T00240/) |
| 2026-05-27 | Zero Trust for AI agents + the security-guidance plugin | Anthropic | [Anthropic](https://claude.com/blog/zero-trust-for-ai-agents) · [plugin](https://claude.com/plugins/security-guidance) |
| 2026-06 | Google AI Threat Defense | Google | [Google Cloud](https://cloud.google.com/blog/ja/products/identity-security/introducing-google-ai-threat-defense) |
| 2026-06-22 | **Patch the Planet** (with Trail of Bits, HackerOne and Calif; 30+ OSS projects taking part, including cURL/Go/Python/Sigstore; Codex Security has scanned 30,000+ codebases and 30 million+ commits) | OpenAI | [OpenAI](https://openai.com/index/patch-the-planet/) |
| 2026-07-15 | **GOLD EAGLE** vulnerability coordination clearinghouse (established under EO 14409) | The White House | [White House](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/) |
| 2026-07-21 | Gemini 3.5 Flash Cyber + CodeMender | Google | [DeepMind](https://deepmind.google/blog/introducing-gemini-3-5-flash-cyber) |
| 2026-07-21 | **Antares** small models (350M/1B open weights; 3B File F1 0.223, close to GPT-5.5's 0.229) | Cisco | [Cisco](https://blogs.cisco.com/ai/introducing-antares-the-most-efficient-open-weight-ai-models-for-vulnerability-localization) |
| 2026-07-27 | MAI-Cyber-1-Flash + Project Perception (a Red/Blue/Green three-team loop) | Microsoft | [Microsoft AI](https://microsoft.ai/news/introducing-mai-cyber-1-flash-inside-mdash/) |
| 2026-07-28 | Using Mythos Preview to find weaknesses in HAWK post-quantum signatures and 7-round AES (the AES work ran almost fully autonomously for 3 days, with only 3 substantive human instructions) | Anthropic | [Anthropic](https://www.anthropic.com/research/discovering-cryptographic-weaknesses) |
| 2026-07-29 | **Numbat**, open-source agent behaviour monitoring (52 CEL detection rules) | Perplexity | [Perplexity](https://research.perplexity.ai/articles/securing-agents-across-perplexity%E2%80%99s-client-endpoints-with-numbat) |
| 2026-07-30 | A Gemini agent finds a **13-year-old** sandbox escape in Chrome (CVE-2026-3545); two milestones fix **1,072 security bugs** | Google | [Google](https://blog.google/security/chrome-stronger-with-every-update/) |
| 2026-08-04 | **SAFE** draft framework for sharing AI incidents (modelled on NASA's ASRS) | OSAA / Linux Foundation | [Linux Foundation](https://www.linuxfoundation.org/blog/proposing-the-safe-working-group-an-open-community-effort-to-improve-ai-security) |

---

<!-- BEGIN:incidents -->
## All records (58)

| Date | Record | Type | Severity | Confidence | Real harm |
|---|---|---|---|---|---|
| `2025-01-23` | [OpenAI Operator launches (context entry)](../incidents/2025-01/2025-01-23-operator-fa-bu-bei-jing.md) | `GOV` | Info | A | · |
| `2025-01-30` | [Italy's Garante blocks DeepSeek](../incidents/2025-01/2025-01-30-garante-deepseek-yi-li-feng.md) | `GOV` | Info | A | · |
| `2025-02-21` | [OpenAI bans accounts behind the "Peer Review" surveillance tool](../incidents/2025-02/2025-02-21-peer-review-feng-jin-jian.md) | `GOV` | Info | A | · |
| `2025-02-27` | [Microsoft sues Storm-2139 and names the defendants](../incidents/2025-02/2025-02-27-storm-wei-ruan-qi-su.md) | `GOV` | Info | A | · |
| `2025-03-01` | [Sony pulls 75,000+ AI deepfake tracks](../incidents/2025-03/2025-03-01-sony-jia-wan-shen-wei.md) | `GOV` | Info | A | · |
| `2025-04-01` | [DeepSeek pulled from app stores in South Korea](../incidents/2025-04/2025-04-01-deepseek-han-guo-jia.md) | `GOV` | Info | A | · |
| `2025-06-16` | [Simon Willison names the "lethal trifecta"](../incidents/2025-06/2025-06-16-simon-willison-ti-chu-zhi.md) | `GOV` | Info | A | · |
| `2025-08-25` | [Anthropic starts the Claude for Chrome pilot](../incidents/2025-08/2025-08-25-anthropic-claude-chrome.md) | `GOV` | Info | A | · |
| `2025-10-07` | [OpenAI October threat report](../incidents/2025-10/2025-10-07-shi-wei-xie-bao-gao.md) | `WEAPON` `GOV` | Info | A | · |
| `2025-10-21` | [OpenAI launches the Atlas browser](../incidents/2025-10/2025-10-21-atlas-liu-lan-qi-fa.md) | `GOV` | Info | A | · |
| `2025-11-19` | [EU "Digital Omnibus" proposes delaying the AI Act](../incidents/2025-11/2025-11-19-digital-omnibus-act.md) | `GOV` | Info | A | · |
| `2025-12-09` | [OWASP Top 10 for Agentic Applications 2026](../incidents/2025-12/2025-12-09-owasp-top-agentic-applications.md) | `GOV` | Info | A | · |
| `2025-12-11` | [GPT-5.2 system card updates cyber capability](../incidents/2025-12/2025-12-11-gpt-xi-tong-ka-wang.md) | `GOV` | Info | A | · |
| `2025-12-22` | [OpenAI: browser prompt injection "may never be fully solved"](../incidents/2025-12/2025-12-22-liu-lan-qi-ti-shi.md) | `GOV` | Info | A | · |
| `2026-01-30` | [Anthropic ships Constitutional Classifiers++](../incidents/2026-01/2026-01-30-anthropic-constitutional-classifiers.md) | `GOV` | Info | A | · |
| `2026-02-01` | [Naver, Kakao and Karrot ban OpenClaw company-wide](../incidents/2026-02/2026-02-01-naver-kakao-karrot-openclaw.md) | `GOV` | Info | A | · |
| `2026-02-05` | [Claude Opus 4.6 finds 500+ zero-days in open-source projects](../incidents/2026-02/2026-02-05-claude-opus-kai-yuan-xiang.md) | `GOV` | Info | A | · |
| `2026-02-05` | [GPT-5.3-Codex rated "High" for cyber capability](../incidents/2026-02/2026-02-05-gpt-codex-high.md) | `GOV` | Info | A | · |
| `2026-02-13` | [ChatGPT introduces Lockdown Mode](../incidents/2026-02/2026-02-13-chatgpt-lockdown-mode.md) | `GOV` | Info | A | · |
| `2026-02-18` | [Anthropic, "Measuring AI agent autonomy in practice"](../incidents/2026-02/2026-02-18-anthropic-measuring-agent-autonomy.md) | `GOV` | Info | A | · |
| `2026-02-19` | [Microsoft: don't run OpenClaw on ordinary work machines](../incidents/2026-02/2026-02-19-openclaw-wei-ruan-pu-tong.md) | `GOV` | Info | A | · |
| `2026-03-18` | [Rome court annuls the Garante's €15M fine against OpenAI](../incidents/2026-03/2026-03-18-garante-yi-li-luo-ma.md) | `GOV` | Info | A | · |
| `2026-04-07` | [Claude Mythos Preview cyber capability disclosure, Project Glasswing formed](../incidents/2026-04/2026-04-07-claude-mythos-preview-project.md) | `GOV` | Info | A | · |
| `2026-04-13` | [UK AISI independently evaluates Claude Mythos Preview](../incidents/2026-04/2026-04-13-uk-aisi-claude-mythos.md) | `GOV` | Info | A | · |
| `2026-04-14` | [Vidoc reproduces Mythos's findings with public models](../incidents/2026-04/2026-04-14-vidoc-mythos-yong-gong-kai.md) | `GOV` | Info | A | · |
| `2026-04-30` | [OpenAI launches Advanced Account Security](../incidents/2026-04/2026-04-30-tui-chu-gao-ji-zhang.md) | `GOV` | Info | A | · |
| `2026-05-01` | [Pwn2Own Berlin 2026: 47 zero-days as AI floods the entry list](../incidents/2026-05/2026-05-01-pwn2own-berlin-ling-can-sai.md) | `GOV` | Info | B | · |
| `2026-05-04` | [Five Eyes: agentic AI is not ready for rapid rollout](../incidents/2026-05/2026-05-04-five-eyes-agentic.md) | `GOV` | Info | A | · |
| `2026-05-12` | [Brazilian labour court sanctions lawyers over prompt injection](../incidents/2026-05/2026-05-12-brazil-labor-court-prompt-injection-sanction.md) | `IPI` `GOV` | **High** | A | ✅ |
| `2026-05-27` | [Anthropic publishes "Zero Trust for AI agents"](../incidents/2026-05/2026-05-27-anthropic-zero-trust-agents.md) | `GOV` | Info | A | · |
| `2026-06-09` | [Anthropic Claude Fable 5 GA, Mythos 5 limited release](../incidents/2026-06/2026-06-09-anthropic-claude-fable-ga.md) | `GOV` | Info | A | · |
| `2026-06-11` | [CISA BOD 26-04](../incidents/2026-06/2026-06-11-cisa-bod.md) | `GOV` | Info | A | · |
| `2026-06-12` | [US government issues export controls to Anthropic](../incidents/2026-06/2026-06-12-anthropic-mei-guo-zheng-fu.md) | `GOV` | Info | A | · |
| `2026-06-12` | [Google sues the China-linked "Outsider Enterprise" smishing network](../incidents/2026-06/2026-06-12-google-outsider-enterprise.md) | `GOV` | Info | A | · |
| `2026-06-23` | [Five Eyes joint statement to boards and executives](../incidents/2026-06/2026-06-23-five-eyes-zhi-qi-ye.md) | `GOV` | Info | A | · |
| `2026-06-24` | [Operation Endgame (Europol) takes down StealC and Amadey](../incidents/2026-06/2026-06-24-operation-endgame-europol-stealc.md) | `GOV` | Info | A | · |
| `2026-06-25` | [OpenAI GPT-5.6 Sol limited preview](../incidents/2026-06/2026-06-25-gpt-sol-xian-ding-yu.md) | `GOV` | Info | A | · |
| `2026-07-17` | [Anthropic, "A CISO's guide to agentic AI"](../incidents/2026-07/2026-07-17-anthropic-ciso-guide-agentic.md) | `GOV` | Info | A | · |
| `2026-07-23` | [US representatives introduce the AI Kill Switch Act](../incidents/2026-07/2026-07-23-kill-switch-act.md) | `GOV` | Info | A | · |
| `2026-07-27` | [NVIDIA convenes the Open Secure AI Alliance](../incidents/2026-07/2026-07-27-nvidia-open-secure-alliance.md) | `GOV` | Info | A | · |
| `2026-07-28` | ["Pacing the Frontier" open letter](../incidents/2026-07/2026-07-28-pacing-frontier-gong-kai-xin.md) | `GOV` | Info | A | · |
| `2026-07-29` | [Perplexity open-sources Numbat for agent behaviour monitoring](../incidents/2026-07/2026-07-29-perplexity-agent-numbat.md) | `GOV` | Info | A | · |
| `2026-08-03` | [CrowdStrike 2026 threat hunting report](../incidents/2026-08/2026-08-03-crowdstrike-wei-xie-shou-lie.md) | `GOV` | Info | A | · |
| `2026-08-04` | [OSAA publishes the SAFE draft for AI incident sharing (RFC)](../incidents/2026-08/2026-08-04-osaa-safe-rfc.md) | `GOV` | Info | A | · |
| `2026-08-06` | [1Password: AI patches fully fix only 26% of the time](../incidents/2026-08/2026-08-06-password-bu-ding-wan-quan.md) | `GOV` | Info | A | · |
| `2026-08-07` | [OpenAI: next-generation model Astra may reach Critical cyber capability](../incidents/2026-08/2026-08-07-astra-critical-yi-dai-mo.md) | `GOV` | Info | A | · |
| `2026-08-18` | [OpenAI slows development and pauses RL training for two weeks](../incidents/2026-08/2026-08-18-rl-xuan-bu-fang-man.md) | `GOV` | Info | A | · |
| `2026-09-01` | ["88% of organisations hit a confirmed or suspected AI agent security incident this year"](../incidents/2026-09/2026-09-01-agent-zu-zhi-guo-qu.md) | `GOV` | Info | C | · |
| `2026-09-03` | [US senators introduce the Ban Artificial Superintelligence Act](../incidents/2026-09/2026-09-03-ban-artificial-superintelligence-act.md) | `GOV` | Info | B | · |
| `2026-09-05` | [OpenAI formally acknowledges the "wiki incident", promises a disclosure framework](../incidents/2026-09/2026-09-05-wiki-zheng-shi-cheng-ren.md) | `GOV` `EVAL` | Info | A | · |
| `2026-09-07` | [Japan's IPA publishes the August 2026 AI Security Bulletin](../incidents/2026-09/2026-09-07-ipa-fa-bu-duan-xin.md) | `GOV` | Info | A | · |
| `2026-09-10` | [Hawley opens a Senate investigation into OpenAI over the Hugging Face agent hack](../incidents/2026-09/2026-09-10-hawley-openai-investigation.md) | `GOV` | Info | A | · |
| `2026-09-12` | [Senators draft a frontier-AI "duty of care" bill with power to block releases](../incidents/2026-09/2026-09-12-ai-duty-of-care-bill.md) | `GOV` | Info | B | · |
| `2026-09-14` | [Microsoft publishes a draft "Humanist AI" code of conduct for its MAI models](../incidents/2026-09/2026-09-14-microsoft-mai-code-of-conduct.md) | `GOV` | Info | A | · |
| `2026-09-16` | [OpenAI discloses six misalignment incidents and a reporting framework](../incidents/2026-09/2026-09-16-openai-misalignment-reports.md) | `EVAL` `GOV` | Medium | A | — |
| `2026-09-16` | [EU State of the Union: von der Leyen cites agent escapes and convenes frontier labs](../incidents/2026-09/2026-09-16-von-der-leyen-soteu-agents.md) | `GOV` | Info | A | · |
| `2026-09-17` | [Anthropic: Claude "leads" 26% of its AI R&D with 30,000 agents running in parallel](../incidents/2026-09/2026-09-17-anthropic-rd-indicators.md) | `GOV` | Info | A | · |
| `2026-09-17` | [China's MSS issues an AI-agent security advisory on the DseWiki hijacking](../incidents/2026-09/2026-09-17-china-mss-agent-advisory.md) | `GOV` `EVAL` | Info | A | · |
<!-- END:incidents -->

---

[← All topics](../README.md) · [Archive index](../README.md)
