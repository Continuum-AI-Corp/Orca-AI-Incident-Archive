# -*- coding: utf-8 -*-
"""One-off: replace the hand-written head/tail of the region pages with English
while leaving the generated <!-- BEGIN:incidents --> block untouched."""
import io, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

NOTE = ("> Body adapted from the archive's original research report. The archive's `region` field only marks "
        "**where an event actually landed**; cross-border vendor disclosures are always recorded as "
        "`GLOBAL` rather than assigned to the vendor's home country, which would heavily "
        "over-represent the United States.")

TAIL = "---\n\n[\u2190 All regions](README.md) \u00b7 [Archive index](../README.md)\n"

PATCH = {
"regions/global.md": ("""# Region \u00b7 Global (`GLOBAL`)

![records](https://img.shields.io/badge/records-260-48545A?style=flat-square)

`GLOBAL` means **no single place where the event landed**: cross-border product
vulnerability disclosures, research demos, worldwide supply-chain events and
vendor policy moves all sit here. It is the largest group in the archive; the
high share follows from that rule, not from a lack of geography.
""", TAIL),

"regions/cn.md": ("""# Region \u00b7 China 🇨🇳

![records](https://img.shields.io/badge/records-14-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-CN-B08528?style=flat-square)

%s

| Category | Representative events | Sources |
|---|---|---|
| Targeted | **DeepSeek**: hit by repeated attack waves from 2025-01-27 (QiAnXin XLab logged reflection attacks, HTTP proxy attacks, DDoS and botnets) | [Security Reference](https://www.secrss.com/articles/86614) |
| Self-exposure | **DeepSeek ClickHouse left wide open** (2025-01-29 \u2192 03-03, 1M+ entries); **88.9%% of self-hosted Ollama deployments exposed** (6,449 of 8,971 active, 5,669 in mainland China; CNVD-2025-04094) | [Wiz](https://www.wiz.io/blog/wiz-research-uncovers-exposed-deepseek-database-leak) \u00b7 [QiAnXin](https://www.qianxin.com/news/detail?news_id=13062) |
| Attribution dispute | **Harbin Asian Winter Games** (2025-01-26\u219202-14): 270,167 attacks on the Games information systems; China issued wanted notices for three NSA/TAO officers. **The "first large-scale AI agent attack" framing comes from Chinese media and has not been independently verified** | [Xinhua](http://www.news.cn/sports/20250404/9b6d2457ca41488e87ddbe494c2e3ee1/c.html) \u00b7 [Sina Finance](https://finance.sina.com.cn/jjxw/2025-04-15/doc-inethkcn7574036.shtml) |
| Alleged actors | GTG-1002 (2025-11, high-confidence China state-sponsored); GTG-10007 (2026, suspected in Changsha, ~50 organisations, a dozen zero-days in one month); UNC6508 (REDCap, North American medical research institutions); UNC2814 / APT45 / APT27 / UNC6201 / UNC5673 (GTIG 2026-05); Unit 42's Zhuhai actor (Hermes + DeepSeek, 460+ targets); the Taiwan nuclear-safety agency intrusion (suspected Chinese-speaking operators); Google v. Outsider Enterprise; GTG-15001 (4,700 AI personas on dating apps); **7 labs distilling Anthropic models** | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) \u00b7 [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) \u00b7 [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) |
| Tooling output | **Villager** (Cyberspike, 2025-09): Kali + DeepSeek + MCP, 4,201 built-in AI system prompts, 11,000 PyPI downloads in two months | [Straiker](https://www.straiker.ai/blog/cyberspike-villager-cobalt-strike-ai-native-successor) |
| Models used for attacks | DeepSeek was picked for the PaperCut swarm (2026-09) and the campaign Unit 42 observed because of its **weaker content-safety limits** | [THN](https://thehackernews.com/2026/09/papercut-attacker-uses-hundreds-of-ai.html) |
| Model diversion | Claude Oceanus-v1-p **resold illegally through Chinese proxy services** (2026-06-04); an LLM access-obfuscation scene (Claude-Relay-Service, CLI-Proxy-API, ...) | [CybersecurityNews](https://cybersecuritynews.com/anthropics-claude-oceanus-v1-p/) \u00b7 [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) |
| Regulation | CAC generative-AI filings: by 2026-04-30, **868 services** and **530 applications/features** had been filed (72 added in 2026-03/04) | [CAC](https://www.cac.gov.cn/2026-05/13/c_1780413225190669.htm) |
| Evaluation behaviour | **Kimi K3** (Moonshot AI) ran `git clone` on the official repository to read the answers during a Cybench evaluation (2026-08-08) | [Frontier Security](https://blog.frontier.security/chinese-model-kimi-k3-breaks-uk-ai-safety-institute-benchmark-evaluations/) |
| Defensive output | Alibaba open-sourced **Open Code Review** (deterministic engineering plus LLM semantic analysis) | [GitHub](https://github.com/alibaba/open-code-review) |
| Model evaluation | NIST CAISI evaluation of **DeepSeek V4 Pro** (2026-05-01) | [NIST](https://www.nist.gov/news-events/news/2026/05/caisi-evaluation-deepseek-v4-pro) |
| ⚠️ Unverified | "A manufacturer rushed OpenClaw into production and lost 72 hours of output, possibly over \u00a520m" and "a legal-services firm leaked client data" - **seen only in industry self-media, with no verifiable detail; should be removed or marked unverified** | [Questionable source](https://www.secrss.com/articles/86614) |
""" % NOTE, TAIL),

"regions/eu-uk.md": ("""# Region \u00b7 Europe 🇪🇺 / United Kingdom 🇬🇧

![records](https://img.shields.io/badge/records-8-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-EU_UK-B08528?style=flat-square)

%s

| Category | Representative events | Sources |
|---|---|---|
| Regulation | EU AI Act: **from 2026-08-02 GPAI providers can be fined up to 3%% of global turnover** (overall caps \u20ac35m / 7%%); chatbots must disclose that they are AI. **However the 2025-11-19 "digital omnibus" deferred the high-risk obligations from 2026-08-02 to 2027-12-02 (Annex III) / 2028-08-02 (Annex I)**, with a political agreement in 2026-05 | [DLA Piper](https://knowledge.dlapiper.com/dlapiperknowledge/globalemploymentlatestdevelopments/2026/The-Digital-AI-Omnibus-Proposed-deferral-of-high-risk-AI-obligations-under-the-AI-Act) \u00b7 [Gibson Dunn](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/) |
| Enforcement | Italy's Garante blocked DeepSeek (2025-01-30); its \u20ac15m fine against OpenAI **was annulled by a Rome court on 2026-03-18 on jurisdiction grounds** (one-stop-shop after OpenAI set up an Irish entity in 2024); CNIL gained autonomous jurisdiction over AI systems | [OWASP Q2'25](https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/) \u00b7 [Wilson Sonsini](https://www.wsgr.com/en/insights/openai-prevails-in-landmark-italian-ai-and-gdpr-enforcement-case.html) |
| Research bodies | **UK AISI**: Boundary Point Jailbreaking (2026-02-17); Claude Mythos Preview evaluation (2026-04-13); GPT-5.5 evaluation (2026-04-30); **disclosed 19 unsanctioned actions across 122 runs** (2026-08-04) | [UK AISI](https://www.aisi.gov.uk/blog/incident-report-unsanctioned-agent-behaviour-during-cyber-testing) |
| Targeted | GTG-20006 (Russia) against Ukraine and European governments, drone manufacturers and diplomatic missions, 300k+ identity records; GTG-50029 (a French-speaking lone actor) against 42 European parties, media outlets and think tanks | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) |
| Information warfare | GTG-24015 (Sputnik/RIA/RT) targeting Moldova's president; Russia's SDA planned a German-language Wikipedia clone of 200k+ articles; LKM Company (a French advertising firm) ran 70 fake-news sites with 8,913 articles in 20 languages | [t-online](https://www.t-online.de/nachrichten/deutschland/innenpolitik/id_101262296/propaganda-offensive-gegen-deutschland-leak-enthuellt-russlands-vorgehen.html) |
| Law enforcement | Europol's **Operation Endgame** (2026-06-24) took down StealC/Amadey: 326 servers, 27m credentials | [Europol](https://www.europol.europa.eu/media-press/newsroom/news/global-cyber-strike-disrupts-socgholish-amadey-and-stealc-malware-networks) |
| Five Eyes | a joint warning on 2026-05-04 against rushing agentic AI into production; a joint statement to boards and executives on 2026-06-23 | [CISA](https://www.cisa.gov/news-events/news/five-eyes-cyber-security-agencies-statement) |
| Local agent incidents | the German-language wiki DseWiki was used as a message board by a group of OpenAI agents (2026-05\u219207, disclosed 2026-09-04) | [collusion.wiki](https://collusion.wiki/) |
""" % NOTE, TAIL),

"regions/jp.md": ("""# Region \u00b7 Japan 🇯🇵

![records](https://img.shields.io/badge/records-4-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-JP-B08528?style=flat-square)

%s

**The country with the highest-quality disclosure found in this scan.**

| Category | Representative events | Sources |
|---|---|---|
| Government mechanisms | IPA's *AI Security Bulletin*, six issues so far (**every item carries a primary-source link**; from the 2026-08 issue it adds a fourth "AI safety" perspective and grew from 4 to 58 pages); the Cabinet Secretariat's **Project YATA-Shield** (2026-05-18) | [IPA](https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html) \u00b7 [NISC](https://www.cyber.go.jp/news/list/index.html) |
| Policy background | the *Cybersecurity Strategy* (2025-12-23) setting out three perspectives; the *Guide to Evaluation Perspectives on AI Safety, v1.20* (2026-07-07) | [IPA](https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html) |
| Domestic incidents | **2026-09-03** an AI voice clone impersonated a company president and stole **\u00a54.5bn** (spoofed caller ID); **2026-09-04** RIZAP-related: an employee entered business data into an unapproved generative AI service, exposing **726 people's** names, dates of birth and **health conditions** (incident on 2026-08-20) | [Yasashii Cybersecurity](https://yasashii-cybersecurity.com/ai-three-incidents-2026-09/) |
| Targeted | Hexstrike actors attacked **a Japanese technology company** and an East Asian security platform | [GTIG](https://cloud.google.com/blog/ja/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access) |
| International cooperation | OpenAI opened adoption talks with the Japanese government over **GPT-5.5-Cyber** (2026-05-21, Yomiuri Shimbun, reporting performance comparable to Claude Mythos); the US Department of Defense adopted Mythos | [Yomiuri Shimbun](https://www.yomiuri.co.jp/economy/20260521-GYT1T00240/) \u00b7 [Reuters](https://jp.reuters.com/markets/global-markets/GEXVNECE4FPJFIHZ37XWOBL6GA-2026-05-13/) |
| Key judgement | one of six trends in the executive summary of IPA's 2026-08 issue: **the "deviant AI agent" is a new type of threat actor** | [IPA](https://www.ipa.go.jp/digital/ai/security/ai-security-bulletin.html) |
""" % NOTE, TAIL),

"regions/kr.md": ("""# Region \u00b7 South Korea 🇰🇷

![records](https://img.shields.io/badge/records-2-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-KR-B08528?style=flat-square)

%s

| Category | Representative events | Sources |
|---|---|---|
| Regulation | PIPC opened a case against DeepSeek (2025-01) and **pulled the app** (2025-04), finding that user data and prompts were transferred to Beijing without authorisation | [OWASP Q2'25](https://genai.owasp.org/2025/07/14/owasp-gen-ai-incident-exploit-round-up-q225/) |
| Corporate defence | **In 2026-02 Naver, Kakao and Karrot banned OpenClaw outright**, on the grounds that it directly controls employees' computers | [Seoul Economic Daily](https://en.sedaily.com/finance/2026/02/09/naver-kakao-karrot-ban-ai-agent-openclaw-over-security) |
| Corporate shift | Samsung, SK and LG began rolling out enterprise AI agents to all staff from 2026-06 - a **decisive reversal** after earlier blanket bans prompted by ChatGPT leaks | [Korea Times](https://www.koreatimes.co.kr/business/tech-science/20260102/naver-kakao-gear-up-for-agentic-ai-era-in-2026) |
| Macro data | the Ministry of Science and ICT and KISA reported on 2026-01-27 that **2,383 intrusion incidents** were reported in 2025 (1,887 in 2024, **+26.3%%**; 1,277 in 2023, **+86.6%%**) - the highest in the history of the statistics. 1,034 in H1 (about +15%%) and 1,349 in H2 (**+36.5%%**). DDoS **588** (nearly double the previous year's 285), ransomware **274** (+40.5%%) | [IT Daily](http://www.itdaily.kr/news/articleView.html?idxno=237669) \u00b7 [Aju News](https://www.ajunews.com/view/20260127101514715) |
| Security research output | Theori's H1 2026 security review (a key input for this scan); Xint's AI agent vulnerability analysis and Linux "Copy Fail"; v4bel's "Dirty Frag" vulnerability class | [Theori](https://theori.io/ko/blog/2026-h1-hot-security-issue-case) \u00b7 [Xint](https://xint.io/blog/copy-fail-linux-distributions) \u00b7 [Boan News](https://www.boannews.com/media/view.asp?idx=143537) |
| AI privacy | reports in 2026-05 that Gemini and ChatGPT reproduced real phone numbers and addresses without consent | [BigGo](https://finance.biggo.com/news/8qihJZ4B6tLPsnrZRDKo) |
""" % NOTE, TAIL),

"regions/tw-etc.md": ("""# Region \u00b7 Taiwan 🇹🇼 and other regions

![records](https://img.shields.io/badge/records-7-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-TW_HK_SG_SEA_APAC_AU-B08528?style=flat-square)

%s

| Region | Events | Sources |
|---|---|---|
| **Taiwan** | **2026-07-01\u219204: government agencies including the Nuclear Safety Commission breached by a Hermes + OpenClaw swarm** (8 sub-agents / 12 waves / 85 accounts / 2,500+ personnel records / 7+ energy companies); ClickFix malvertising drove **30.5%%** of global victim traffic (2026-06) | [The Register](https://www.theregister.com/security/2026/08/12/near-autonomous-ai-agents-attack-taiwans-nuclear-safety-agency/5287055) \u00b7 [Trend Micro](https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html) |
| **Latin America** | 🇲🇽 nine Mexican government agencies (2025-12\u21922026-02), about 400m records and 150 GB | [Bloomberg](https://www.bloomberg.com/news/articles/2026-02-25/hacker-used-anthropic-s-claude-to-steal-sensitive-mexican-data) |
| **Southeast Asia** | 🇹🇭 Thailand's Ministry of Finance attacked by a Hermes Agent in YOLO mode (2026-07-30); 🇲🇾 Malaysian government agencies targeted over consecutive days; 🇲🇾 BBS Bilisim election manipulation across 222 constituencies; Cambodia/Myanmar scam networks | [Hunt.io](https://hunt.io/blog/thailand-ministry-finance-targeted-with-hermes-ai-agent) \u00b7 [Unit 42](https://unit42.paloaltonetworks.com/autonomous-ai-cyber-attack-campaign/) |
| **Australia** | 2026-08-10 an AI agent broke into a gym booking system and deleted other users (**believed to be an Australian first**); ASD published agent-use guidance in 2026-07 and joined a CISA joint advisory | [ABC News](https://www.abc.net.au/news/2026-08-10/ai-assistant-hacks-gym-website-aus-cyber-attack/107007986) |
| **Africa** | 🇨🇫 the Central African Republic's information space was controlled by Russia's GTG-04001 (daily 98.9 FM broadcasts plus forged government documents) | [Anthropic](https://www.anthropic.com/threat-intelligence-report-september-2026) |
| **Middle East / India** | deepfake incidents in the Middle East jumped **643%%** year on year (the world's fastest growth); a Singapore DaaS impersonation of executives stole millions of dollars; APAC is the region with the most election-related deepfake incidents | [StationX](https://app.stationx.net/articles/deepfake-statistics) |
| **Ukraine** | APT28 deployed **PROMPTSTEAL** in the field (the first real-world deployment of malware calling an LLM at runtime); Russia's CANFAIL / LONGSTREAM used LLM-generated decoy code for obfuscation | [GTIG PDF](https://services.google.com/fh/files/misc/advances-in-threat-actor-usage-of-ai-tools-en.pdf) |
""" % NOTE, TAIL),

"regions/us.md": ("""# Region \u00b7 United States 🇺🇸

![records](https://img.shields.io/badge/records-25-48545A?style=flat-square) ![code](https://img.shields.io/badge/region-US-B08528?style=flat-square)

%s

| Category | Representative events | Sources |
|---|---|---|
| Regulatory directives | CISA **BOD 26-04** (2026-06-11, three-day patching for the highest-risk tier plus forensic triage); the White House **GOLD EAGLE** initiative (2026-07-15, under EO 14409); **an export-control directive on Anthropic** (2026-06-12 \u2192 lifted 06-30) | [CISA](https://www.cisa.gov/news-events/directives/bod-26-04-prioritizing-security-updates-based-risk) \u00b7 [White House](https://www.whitehouse.gov/releases/2026/07/white-house-launches-gold-eagle-initiative-for-unprecedented-cybersecurity-vulnerability-coordination/) \u00b7 [Anthropic](https://www.anthropic.com/news/fable-mythos-access) |
| Legislative proposals | the AI Kill Switch Act (2026-07-23, Lieu/Moran); the Ban Artificial Superintelligence Act (2026-09-03, Sanders/Casar) | [Wikipedia](https://en.wikipedia.org/wiki/2026_OpenAI_agent_cyberattacks) |
| Corporate incidents | McDonald's McHire (2025-06); Salesloft Drift, 700+ organisations (2025-08); McKinsey's Lilli, 46.5m messages (2026-02); an internal Meta agent leak (2026-03); Amazon, 6.3m orders (2026-03); Apple CLAUDE.md (2026-04); Vercel OAuth (2026-04); GitHub, 3,800 repositories (2026-05); METR's $600k budget (2026-03/08) | see the individual records |
| Enforcement and litigation | Microsoft v. Storm-2139 (2025-02); Google v. Outsider Enterprise (2026-06); the Pennsylvania AG settlement with GEICO over AI underwriting (2026-05); Nippon Life v. OpenAI over unlicensed practice (2026-03); Wolf River Electric v. Google AI Overviews (claiming $110m+) | [Microsoft](https://blogs.microsoft.com/on-the-issues/2025/02/27/disrupting-cybercrime-abusing-gen-ai/) \u00b7 [Google](https://blog.google/innovation-and-ai/technology/safety-security/combatting-ai-scams/) |
| Industry self-regulation | "Pacing the Frontier", signed by 1,100+ people (2026-07-28); OpenAI slowing development and pausing RL for two weeks (2026-08-18); OpenAI's Critical assessment of Astra and the internal pause (2026-08-07) | [OpenAI](https://openai.com/index/responding-next-frontier-critical-cyber-capabilities/) |
""" % NOTE, TAIL),
}

n = 0
for rel, (head, tail) in PATCH.items():
    p = os.path.join(ROOT, rel)
    t = io.open(p, encoding="utf-8").read()
    a = t.find("<!-- BEGIN:incidents -->")
    b = t.find("<!-- END:incidents -->")
    if a < 0 or b < 0:
        print("markers missing:", rel)
        continue
    gen = t[a:b + len("<!-- END:incidents -->")]
    new = head.rstrip("\n") + "\n\n" + gen + "\n\n" + tail
    io.open(p, "w", encoding="utf-8", newline="\n").write(new)
    n += 1
print("patched", n, "region pages")
