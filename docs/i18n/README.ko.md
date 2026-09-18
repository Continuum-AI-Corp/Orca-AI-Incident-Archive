<h1 align="center">Orca AI Incident Archive</h1>

<p align="center"><b>실제 AI 에이전트 사고의 오픈 데이터베이스</b></p>

<p align="center">
<a href="../../README.md">English</a> ·
<a href="README.zh-CN.md">简体中文</a> ·
<a href="README.ja.md">日本語</a> ·
<b>한국어</b> ·
<a href="README.de.md">Deutsch</a> ·
<a href="README.fr.md">Français</a> ·
<a href="README.es.md">Español</a>
</p>

<!-- BEGIN:badges -->
<p align="center"><img alt="레코드" src="https://img.shields.io/badge/%EB%A0%88%EC%BD%94%EB%93%9C-323-48545A?style=flat-square"> <img alt="대상 개월" src="https://img.shields.io/badge/%EB%8C%80%EC%83%81_%EA%B0%9C%EC%9B%94-22-48545A?style=flat-square"> <img alt="심각" src="https://img.shields.io/badge/%EC%8B%AC%EA%B0%81-45-88091D?style=flat-square"> <img alt="실제 피해" src="https://img.shields.io/badge/%EC%8B%A4%EC%A0%9C_%ED%94%BC%ED%95%B4-123-B23B40?style=flat-square"> <img alt="1차 출처" src="https://img.shields.io/badge/1%EC%B0%A8_%EC%B6%9C%EC%B2%98-485_URL-157A41?style=flat-square"> <img alt="라이선스" src="https://img.shields.io/badge/%EB%9D%BC%EC%9D%B4%EC%84%A0%EC%8A%A4-CC_BY_4.0-2359A8?style=flat-square"></p>
<!-- END:badges -->

<!-- BEGIN:thesis -->
수록 범위는 **2025-01**부터 **2026-09-17**까지입니다. AI 에이전트와 관련된 보안 사건 323건을 월별로 정리했습니다(2024-12-01까지 거슬러 올라가는 선행 사건 1건 포함). 각 레코드는 YAML 헤더, 공격 체인 도식, 그리고 **클릭할 수 있는 1차 출처 최소 1개**를 갖춘 Markdown 파일입니다. 323건 중 확인된 피해자가 있는 것은 **123건**뿐입니다.
<!-- END:thesis -->

이 아카이브는 대부분의 사고 목록이 뭉개버리는 한 가지 구분을 지키기 위해 존재합니다.

> **에이전트가 실제로 피해를 입힌 것과, 연구자가 그럴 수 있음을 보여준 것은 서로 다른 일이다.**

모든 레코드는 다른 무엇보다 먼저 세 가지 질문에 답합니다. 확인된 피해자가 있었는가(`real_harm`), AI의 관여가 1차 출처로 확인되었는가(`ai_involvement`), 그리고 이것은 사고인가, 취약점 공개인가, 연구 시연인가, 위협 보고서인가, 정책 조치인가(`kind`). 이 세 필드가 없다면 "올해 AI 사고 300여 건"이라는 숫자는 아무 의미가 없습니다.

---

## 한눈에 보기

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/monthly-dark.svg">
  <img alt="2025년 1월부터 2026년 9월까지의 월별 건수" src="../../assets/monthly-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/severity-dark.svg">
  <img alt="심각도 및 레코드 유형별 분류" src="../../assets/severity-light.svg" width="100%">
</picture>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../assets/by-type-dark.svg">
  <img alt="공격 유형별 분포" src="../../assets/by-type-light.svg" width="100%">
</picture>

## 어디서부터 볼까

| 하고 싶은 일 | 가는 곳 |
|---|---|
| 시간순으로 읽기 | [월별 전체 레코드](../../incidents/README.md) |
| 실제 피해만 보기 | [`critical` 목록](#critical) · 또는 `real_harm: true` 로 필터 |
| 공격면 기준으로 읽기 | [7개 주제](../../topics/README.md) |
| 특정 국가·지역 보기 | [지역별](../../regions/README.md) |
| 필드 정의 확인 | [SCHEMA.md](../../SCHEMA.md) · [분류 체계](../../taxonomy/README.md) · [문서](../../docs/README.md) |
| 데이터 분석하기 | [`dist/`](../../dist/README.md) — JSON, CSV, 통계, 전체 출처 URL |
| 대화형으로 탐색 | [`index.html`](../../index.html) — 단일 파일, 오프라인 가능, 7개 언어 |

> [!NOTE]
> **언어 안내.** 레코드는 영어로 작성됩니다. 제목과 요약은 7개 언어(영어·중국어·일본어·한국어·독일어·프랑스어·스페인어)로 제공됩니다. 각 레코드의 전체 중국어판은 [`incidents/i18n/zh/`](../../incidents/i18n/zh/)에 있습니다. 인용된 출처는 원어 그대로입니다. 번역 추가를 환영합니다. [CONTRIBUTING.md](../../CONTRIBUTING.md)를 참고하세요.

## 월별

<!-- BEGIN:months -->
**2024년**(1건)

| [12](../../incidents/2024-12/README.md) |
|---|
| `1` |

**2025년**(121건)

| [01](../../incidents/2025-01/README.md) | [02](../../incidents/2025-02/README.md) | [03](../../incidents/2025-03/README.md) | [04](../../incidents/2025-04/README.md) | [05](../../incidents/2025-05/README.md) | [06](../../incidents/2025-06/README.md) | [07](../../incidents/2025-07/README.md) | [08](../../incidents/2025-08/README.md) | [09](../../incidents/2025-09/README.md) | [10](../../incidents/2025-10/README.md) | [11](../../incidents/2025-11/README.md) | [12](../../incidents/2025-12/README.md) |
|---|---|---|---|---|---|---|---|---|---|---|---|
| `8` ★1 | `6` | `6` | `6` | `7` | `11` | `10` ★2 | `15` ★2 | `10` ★1 | `15` | `13` ★3 | `14` |

**2026년**(201건)

| [01](../../incidents/2026-01/README.md) | [02](../../incidents/2026-02/README.md) | [03](../../incidents/2026-03/README.md) | [04](../../incidents/2026-04/README.md) | [05](../../incidents/2026-05/README.md) | [06](../../incidents/2026-06/README.md) | [07](../../incidents/2026-07/README.md) | [08](../../incidents/2026-08/README.md) | [09](../../incidents/2026-09/README.md) |
|---|---|---|---|---|---|---|---|---|
| `13` ★1 | `19` ★5 | `16` ★3 | `22` ★2 | `26` ★5 | `31` ★3 | `27` ★7 | `23` ★4 | `24` ★6 |

<sub>`n` = 해당 월 건수, ★ = 그중 `critical` 건수</sub>
<!-- END:months -->

## Critical

<!-- BEGIN:critical -->
세 가지 조건 중 하나라도 충족하면 `critical` 입니다. ① **확인된** 피해가 다수 조직·정부·핵심 인프라·공급망 웜 규모에 이른 경우. ② 실제 피해자가 있는 최초의 역량 이정표. ③ **널리 배포된 방어 전제를 뒤엎었는지**를 입증한 연구(이 경우 `real_harm: false`, 2건). 전체 기준은 [../../taxonomy/severity.md](../../taxonomy/severity.md).

| 날짜 | 레코드 | 유형 | 지역 |
|---|---|---|---|
| `2025-01-29` | [DeepSeek ClickHouse 데이터베이스, 무방비로 노출](../../incidents/2025-01/2025-01-29-deepseek-clickhouse-exposed.md)<br><sub>DeepSeek ClickHouse database left wide open</sub> | `INFRA` | 중국 |
| `2025-07-13` | [Amazon Q Developer 확장 프로그램 오염](../../incidents/2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br><sub>Amazon Q Developer extension poisoned</sub> | `SUPPLY` `ROGUE` | 전 세계 |
| `2025-07-18` | [Replit Agent, 프로덕션 데이터베이스 삭제](../../incidents/2025-07/2025-07-18-replit-agent-deletes-prod-db.md)<br><sub>Replit Agent deletes a production database</sub> | `ROGUE` | 미국 |
| `2025-08-08` | [Salesloft Drift OAuth 토큰 탈취](../../incidents/2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br><sub>Salesloft Drift OAuth token theft</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2025-08-26` | [Nx "s1ngularity"](../../incidents/2025-08/2025-08-26-nx-s1ngularity.md) | `SUPPLY` `CRED` | 전 세계 |
| `2025-09-15` | [Shai-Hulud npm 웜 v1](../../incidents/2025-09/2025-09-15-shai-hulud-npm.md)<br><sub>Shai-Hulud npm worm v1</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2025-11-01` | [ShadowRay 2.0(Ray 프레임워크)](../../incidents/2025-11/2025-11-01-shadowray-2-ray-framework.md)<br><sub>ShadowRay 2.0 (Ray framework)</sub> | `INFRA` | 전 세계 |
| `2025-11-13` | [GTG-1002: AI가 조율한 최초의 사이버 첩보 작전](../../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md)<br><sub>GTG-1002: first AI-orchestrated cyber-espionage campaign</sub> | `WEAPON` | 중국 전 세계 |
| `2025-11-21` | [Shai-Hulud 2.0](../../incidents/2025-11/2025-11-21-shai-hulud.md) | `SUPPLY` `CRED` | 전 세계 |
| `2026-01-31` | [Moltbook 데이터베이스 완전 개방](../../incidents/2026-01/2026-01-31-moltbook-open-database.md)<br><sub>Moltbook database fully open</sub> | `CRED` | 전 세계 |
| `2026-02-09` | [Clinejection](../../incidents/2026-02/2026-02-09-clinejection.md) | `SUPPLY` `IPI` | 전 세계 |
| `2026-02-20` | [AI로 강화된 행위자, FortiGate 600대 이상 침해](../../incidents/2026-02/2026-02-20-fortigate-600-devices-compromised.md)<br><sub>AI-augmented actor compromises 600+ FortiGate devices</sub> | `WEAPON` | 전 세계 |
| `2026-02-25` | [멕시코 정부 기관 9곳 침해](../../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md)<br><sub>Nine Mexican government agencies breached</sub> | `WEAPON` | 라틴아메리카 |
| `2026-02-26` | [Claude Code, DataTalks.Club 프로덕션 전체에 terraform destroy 실행](../../incidents/2026-02/2026-02-26-claude-code-terraform-destroy-datatalks.md)<br><sub>Claude Code runs terraform destroy on all of DataTalks.Club's production</sub> | `ROGUE` | 전 세계 |
| `2026-02-28` | [CodeWall, 맥킨지 내부 "Lilli" AI 플랫폼 침해](../../incidents/2026-02/2026-02-28-codewall-breaches-mckinsey-lilli.md)<br><sub>CodeWall breaches McKinsey's internal "Lilli" AI platform</sub> | `WEAPON` `INFRA` | 미국 |
| `2026-03-01` | [Hades: AI 코딩 어시스턴트를 공격 표면으로 만든 지속 작전](../../incidents/2026-03/2026-03-01-hades-campaign-ai-coding-assistants.md)<br><sub>Hades: a sustained campaign turning AI coding assistants into the attack surface</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-03-24` | [백도어가 심긴 LiteLLM 릴리스](../../incidents/2026-03/2026-03-24-litellm-backdoored-release.md)<br><sub>Backdoored LiteLLM release</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-03-30` | [Axios npm 패키지 침해](../../incidents/2026-03/2026-03-30-axios-npm-compromised.md)<br><sub>Axios npm package compromised</sub> | `SUPPLY` | 전 세계 |
| `2026-04-16` | [MCPwn (CVE-2026-33032): nginx-ui MCP 엔드포인트 실제 공격](../../incidents/2026-04/2026-04-16-mcpwn-nginx-ui-in-the-wild.md)<br><sub>MCPwn (CVE-2026-33032): nginx-ui MCP endpoint hit in the wild</sub> | `MCP` `INFRA` | 전 세계 |
| `2026-04-25` | [Cursor와 Claude Opus 4.6, 9초 만에 프로덕션과 백업 삭제](../../incidents/2026-04/2026-04-25-cursor-opus-46-nine-second-wipe.md)<br><sub>Cursor and Claude Opus 4.6 wipe production and backups in nine seconds</sub> | `ROGUE` | 전 세계 |
| `2026-05-10` | [실제 환경에서 LLM 에이전트가 전 과정 침해 후 활동을 수행한 최초 사례](../../incidents/2026-05/2026-05-10-first-in-wild-autonomous-llm-post-exploitation.md)<br><sub>First in-the-wild LLM agent running the full post-exploitation chain</sub> | `WEAPON` | 전 세계 |
| `2026-05-11` | [TanStack npm "Mini Shai-Hulud"](../../incidents/2026-05/2026-05-11-tanstack-npm-mini-shai.md) | `SUPPLY` `CRED` | 전 세계 |
| `2026-05-18` | [GitHub 내부 저장소 3,800개 침해](../../incidents/2026-05/2026-05-18-github-3800-internal-repos.md)<br><sub>3,800 internal GitHub repositories compromised</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-05-19` | [TrapDoor: 세 생태계를 오염시켜 AI 어시스턴트 설정을 변조](../../incidents/2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br><sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-05-21` | [Composio: 에이전트 자동화 자체가 권한 상승 경로가 되다](../../incidents/2026-05/2026-05-21-composio-agent-automation-privesc.md)<br><sub>Composio: agent automation itself becomes the privilege-escalation path</sub> | `CRED` `SUPPLY` | 전 세계 |
| `2026-06-01` | [공격자들, Meta AI 지원 봇에 그냥 Instagram 계정을 요구하다](../../incidents/2026-06/2026-06-01-meta-ai-support-bot-hands-over-instagram.md)<br><sub>Attackers simply ask Meta's AI support bot for Instagram accounts</sub> | `IPI` `CRED` | 전 세계 |
| `2026-06-01` | [Miasma 웜](../../incidents/2026-06/2026-06-01-miasma-worm.md)<br><sub>Miasma worm</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-06-17` | [Sapphire Sleet, 88분 만에 모든 Mastra AI 스코프를 오염시키다](../../incidents/2026-06/2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br><sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-07-01` | [JADEPUFFER: LLM이 종단 간 구동한 최초의 랜섬웨어](../../incidents/2026-07/2026-07-01-jadepuffer-first-llm-driven-ransomware.md)<br><sub>JADEPUFFER: first ransomware driven end-to-end by an LLM</sub> | `WEAPON` | 전 세계 |
| `2026-07-01` | [대만 원자력안전위원회 등 기관, 에이전트 군집에 침해](../../incidents/2026-07/2026-07-01-taiwan-government-agent-swarm.md)<br><sub>Taiwan's nuclear safety commission and other agencies breached by an agent swarm</sub> | `WEAPON` | 대만 |
| `2026-07-02` | [웹에 숨겨진 지시로 AI 에이전트가 공격자에게 결제하게 하다(실제 작전 2건)](../../incidents/2026-07/2026-07-02-hidden-web-instructions-payment-fraud.md)<br><sub>Hidden web instructions make AI agents pay attackers (two in-the-wild campaigns)</sub> | `IPI` `ROGUE` | 전 세계 |
| `2026-07-09` | [OpenAI의 에이전트가 Hugging Face를 침해하다](../../incidents/2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br><sub>OpenAI's agents breach Hugging Face</sub> | `EVAL` `WEAPON` | 전 세계 |
| `2026-07-30` | [Anthropic, 평가 환경 이탈 사고 3건 공개](../../incidents/2026-07/2026-07-30-anthropic-three-eval-incidents.md)<br><sub>Anthropic discloses three evaluation-breakout incidents</sub> | `EVAL` | 전 세계 |
| `2026-07-30` | [Hermes Agent, 태국 재무부를 무인 공격](../../incidents/2026-07/2026-07-30-hermes-agent-thailand-finance-ministry.md)<br><sub>Hermes Agent attacks Thailand's Ministry of Finance unattended</sub> | `WEAPON` | 동남아시아 |
| `2026-07-30` | [Unit 42: 중국어권 운영자의 자율 작전](../../incidents/2026-07/2026-07-30-unit42-chinese-speaking-autonomous-campaigns.md)<br><sub>Unit 42: autonomous campaigns run by Chinese-speaking operators</sub> | `WEAPON` | 중국 전 세계 |
| `2026-08-04` | [CHAINDROP npm 웜](../../incidents/2026-08/2026-08-04-chaindrop-npm-ru-chong.md)<br><sub>CHAINDROP npm worm</sub> | `SUPPLY` `CRED` | 전 세계 |
| `2026-08-06` | [Langflow 무인증 RCE, CISA KEV에 등재](../../incidents/2026-08/2026-08-06-langflow-rce-cisa-kev.md)<br><sub>Unauthenticated Langflow RCE added to CISA KEV</sub> | `INFRA` | 전 세계 |
| `2026-08-26` | [Trail of Bits: VM은 사이버 능력을 갖춘 에이전트를 가둘 수 없다](../../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)<br><sub>Trail of Bits: VMs won't contain cyber-capable agents</sub> | `EVAL` `SANDBOX` | 전 세계 |
| `2026-08-28` | [PaperCut AI 에이전트 군집 작전 시작](../../incidents/2026-08/2026-08-28-papercut-agent-swarm-campaign-begins.md)<br><sub>PaperCut AI agent swarm campaign begins</sub> | `WEAPON` | 전 세계 |
| `2026-09-01` | [GitSpawn: 악성 .git/config가 모델에 접촉하기도 전에 7개 코딩 에이전트에서 공격자 코드를 실행](../../incidents/2026-09/2026-09-01-gitspawn-git-config-pre-model-rce.md)<br><sub>GitSpawn: a malicious .git/config runs attacker code in 7 coding agents before the model is ever contacted</sub> | `SUPPLY` `SANDBOX` | 전 세계 |
| `2026-09-02` | [Langflow CVE-2026-0768: 올해 실제 악용된 12번째 Langflow 결함](../../incidents/2026-09/2026-09-02-langflow-jin-di-ye-li.md)<br><sub>Langflow CVE-2026-0768: the 12th Langflow flaw exploited in the wild this year</sub> | `INFRA` `CRED` | 전 세계 |
| `2026-09-10` | [Anthropic 9월 위협 인텔리전스 보고서](../../incidents/2026-09/2026-09-10-anthropic-september-threat-report.md)<br><sub>Anthropic September threat intelligence report</sub> | `WEAPON` | 전 세계 |
| `2026-09-11` | [Claude, 180만 개 Android 앱에서 비밀 정보 스캔에 사용](../../incidents/2026-09/2026-09-11-claude-scans-18m-android-apks.md)<br><sub>Claude used to scan 1.8 million Android apps for secrets</sub> | `WEAPON` | 전 세계 |
| `2026-09-14` | [스페인 AEPD, AI 에이전트 기반 데이터 침해 신고를 최초 접수](../../incidents/2026-09/2026-09-14-spain-aepd-agent-breach.md)<br><sub>Spain's AEPD receives the first AI-agent-driven breach notification</sub> | `WEAPON` | 유럽 |
| `2026-09-15` | [PaperCut AI 에이전트 군집 공격 공개](../../incidents/2026-09/2026-09-15-papercut-agent-swarm-disclosed.md)<br><sub>PaperCut AI agent swarm attack made public</sub> | `WEAPON` | 전 세계 |
<!-- END:critical -->

## 무엇을 레코드로 보는가

다음 중 **하나 이상**에 해당하면 수록합니다.

1. AI 에이전트가 **공격을 수행한 주체**인 경우 — 자율적이든, 사람이 조종했든
2. AI 에이전트가 **공격 대상**인 경우 — 인젝션, 오염, 샌드박스 탈출, 인프라 노출
3. AI 에이전트가 **피해 사슬의 한 고리**인 경우 — 악의적 내용을 읽고 그대로 실행한 경우
4. 에이전트 보안과 직접 관련된 **규제·입법·벤더의 조치**(`kind: policy` 로 기록하며 사고 통계에는 포함하지 않음)

**수록하지 않는 것:** 순수한 LLM 콘텐츠 안전성 문제(모델을 탈옥시켜 부적절한 출력을 얻는 것), 에이전트와 무관한 일반 취약점, 1차 출처를 찾을 수 없는 소문.

다음 두 부류는 **삭제하지 않고 표시해** 둡니다.

- `ai_involvement: unverified` — AI 사고로 널리 보도되었으나 1차 출처에는 AI가 전혀 등장하지 않는 경우. 그 주장이 **반박 자료와 함께 검색되도록** 남겨 둡니다.
- `ai_involvement: disputed` — 벤더와 보도의 설명이 엇갈리는 경우. 양쪽 주장을 레코드 안에 나란히 보존합니다.

전체 기준은 [docs/scope.md](../../docs/scope.md)를 보세요.

## 데이터 품질

<!-- BEGIN:quality -->
|  |  |
|---|---|
| 출처 링크 | 552개 / 고유 URL 485개 |
| 출처 없는 레코드 | **0** — 출처가 없으면 수록하지 않음 |
| 등급 A(1차 출처) | 280건 |
| 분쟁 표시 | 14건 |
| 검증 회차 | 4회 |
<!-- END:quality -->

처음 세 차례는 **모든 레코드를 한 건씩** 대조했습니다. 네 번째로 **커버리지 감사**를 했더니 그럼에도 약 11%가 빠져 있었습니다. 이 둘은 전혀 다른 문제를 잡아냅니다. "수록된 것이 정확한가"와 "수록되어야 할 것이 다 있는가"는 별개의 질문이며, 따로 물어야 합니다.

네 차례의 검증에서 날조된 2건을 삭제했고, PaperCut의 "6시간 만에 도메인 관리자 장악"을 **7분**으로 정정했으며, Step Finance를 D 등급으로 내렸습니다(1차 보도에 AI 언급이 전혀 없기 때문). 모든 정정 내역은 [docs/data-quality.md](../../docs/data-quality.md)에 남아 있으며, 조용히 덮어쓴 것은 없습니다.

## 인용

<!-- BEGIN:cite -->
```bibtex
@misc{orca_ai_incident_archive,
  title  = {Orca AI Incident Archive: An open database of real-world AI agent incidents},
  year   = {2026},
  note   = {323건, 2025-01~2026-09, 123건은 확인된 실제 피해},
  url    = {https://github.com/Continuum-AI-Corp/Orca-AI-Incident-Archive}
}
```
<!-- END:cite -->

개별 레코드를 인용할 때는 `id`를 함께 적어 주세요. 예: `orca:2026-07-09-openai-agents-breach-huggingface`.

## 기여

정정, 누락된 레코드, 더 나은 출처 모두 환영합니다. 규칙은 세 가지입니다.

1. **모든 레코드에는 클릭할 수 있는 1차 출처가 필요합니다.** 출처가 없으면 병합하지 않습니다.
2. **확신이 없으면 표시하세요. 지우지 마세요.** 다툼이 있는 사실에는 `disputed: true`를 붙이고 양쪽 설명을 모두 남깁니다.
3. **정정은 레코드에 기록합니다. 조용히 덮어쓰지 않습니다.** 무엇을 왜 바꿨는지 적어 주세요.

[CONTRIBUTING.md](../../CONTRIBUTING.md)를 참고하세요. [새 레코드](../../.github/ISSUE_TEMPLATE/new-incident.yml)와 [정정](../../.github/ISSUE_TEMPLATE/correction.yml) 이슈 템플릿이 준비되어 있습니다.

## 라이선스 및 면책

[CC BY 4.0](../../LICENSE)으로 제공되며 출처 표시가 필요합니다. 링크된 원자료의 저작권은 각 권리자에게 있습니다.

이 아카이브는 **공개된 사건만** 기록하며, 미공개 취약점 세부 정보나 익스플로잇 코드, 공격 도구는 일절 포함하지 않습니다. 분류와 심각도는 편집자의 판단이며 벤더나 규제 기관의 공식 판정이 아닙니다. 당사자로서 레코드에 오류가 있다고 보신다면 이슈를 열어 주세요. 확인 후 정정하겠습니다.

---

<sub><!-- BEGIN:footer -->빌드 2026-09-17 · 323건 · 22개월<!-- END:footer --></sub> · <sub>구조: [SCHEMA.md](../../SCHEMA.md) · 데이터: [dist/](../../dist/README.md)</sub>
