---
id: 2026-06-18-clickfix-claude-ai-e-yi-guang
title: "ClickFix malvertising abuses claude.ai shared conversations"
title_zh: "ClickFix 恶意广告滥用 claude.ai 分享对话"
title_ja: "ClickFixのマルバタイジングがclaude.aiの共有会話を悪用"
title_ko: "ClickFix 악성 광고, claude.ai 공유 대화를 악용"
title_de: "ClickFix-Malvertising missbraucht geteilte claude.ai-Unterhaltungen"
title_fr: "La malvertising ClickFix abuse des conversations partagées de claude.ai"
title_es: "Publicidad maliciosa de ClickFix abusa de las conversaciones compartidas de claude.ai"
date: 2026-06-18
date_precision: day
date_raw: "2026-06-18"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL, APAC]

summary: |
  TrendAI: from 2026-04-08 → 06-14, Google ads impersonated at least 6 brands including Claude AI, Cursor IDE and ChatGPT Codex; 6 waves over 7 weeks, **106 hostnames**. It started with fake GitLab Pages sites, then **from 05-06 hosted the ClickFix steps in claude.ai's public shared-conversation feature**, and after 05-21 all activity ran on that feature. Posing as Apple Support, it lured users into pasting base64-obfuscated commands; the script **aborts when it detects a Russian keyboard layout**, otherwise it drops MacSync to steal credentials, cookies, SSH keys and crypto wallets. **67.4% of victim traffic came from Asia-Pacific, with Taiwan alone accounting for 30.5%**. After being notified, Anthropic disabled the related accounts and the malicious shared conversations


summary_zh: |
  TrendAI：2026-04-08 → 06-14，Google 广告冒充 Claude AI、Cursor IDE、ChatGPT Codex 等至少 6 个品牌；7 周 6 波、**106 个主机名**。起初用 GitLab Pages 假站，**05-06 起改用 claude.ai 的公开分享对话功能承载 ClickFix 步骤**，05-21 后全部活动都在该功能上。伪装成 Apple Support 诱导粘贴 base64 混淆命令；脚本**检测到俄语键盘布局即中止**，否则投放 MacSync 窃取凭据/Cookie/SSH 密钥/加密钱包。**受害流量 67.4% 在亚太，台湾单地占 30.5%**。Anthropic 接报后停用相关账号并禁用恶意分享对话

summary_ja: |
  TrendAI：2026-04-08 → 06-14に、Google広告がClaude AI、Cursor IDE、ChatGPT Codexを含む少なくとも6ブランドになりすました。7週間で6波、**106のホスト名**。当初は偽のGitLab Pagesサイトから始まり、**05-06以降はclaude.aiの公開共有会話機能にClickFixの手順をホスト**、05-21以降はすべての活動がこの機能上で行われた。Apple Supportを装い、base64で難読化したコマンドを貼り付けさせる。スクリプトは**ロシア語キーボードレイアウトを検出すると中止**し、それ以外ではMacSyncをドロップして認証情報、Cookie、SSHキー、暗号資産ウォレットを窃取する。**被害者トラフィックの67.4%はアジア太平洋からで、台湾だけで30.5%を占めた**。通知を受けたAnthropicは関連アカウントと悪性の共有会話を無効化した

summary_ko: |
  TrendAI: 2026-04-08 → 06-14에 걸쳐 구글 광고가 Claude AI, Cursor IDE, ChatGPT Codex 등 최소 6개 브랜드를 사칭했다. 7주 동안 6개 파도, **호스트 이름 106개**. 가짜 GitLab Pages 사이트로 시작했고 **05-06부터는 ClickFix 절차를 claude.ai의 공개 대화 공유 기능에 호스팅**했으며 05-21 이후에는 모든 활동이 그 기능에서 이뤄졌다. Apple Support를 사칭해 base64로 난독화된 명령을 붙여 넣도록 유인했고, 스크립트는 **러시아어 키보드 배열을 감지하면 중단**되며 그렇지 않으면 MacSync를 설치해 자격 증명, 쿠키, SSH 키, 가상자산 지갑을 탈취했다. **피해자 트래픽의 67.4%가 아시아태평양에서 발생했고 대만만 30.5%를 차지했다**. 통보를 받은 Anthropic은 관련 계정과 악성 공유 대화를 비활성화했다

summary_de: |
  TrendAI: Von 2026-04-08 → 06-14 gaben sich Google-Anzeigen als mindestens 6 Marken aus, darunter Claude AI, Cursor IDE und ChatGPT Codex; 6 Wellen über 7 Wochen, **106 Hostnames**. Es begann mit gefälschten GitLab-Pages-Seiten und **hostete ab 05-06 die ClickFix-Schritte in der öffentlichen Funktion zum Teilen von Unterhaltungen in claude.ai**; nach dem 05-21 lief die gesamte Aktivität über diese Funktion. Als Apple Support getarnt, lockte es Nutzer dazu, base64-obfuskierte Befehle einzufügen; das Skript **bricht ab, wenn es ein russisches Tastaturlayout erkennt**, andernfalls setzt es MacSync ab, um Zugangsdaten, Cookies, SSH-Schlüssel und Krypto-Wallets zu stehlen. **67.4% des Opferverkehrs kam aus dem Asien-Pazifik-Raum, allein Taiwan machte 30.5% aus**. Nach der Benachrichtigung deaktivierte Anthropic die zugehörigen Konten und die bösartigen geteilten Unterhaltungen

summary_fr: |
  TrendAI : du 2026-04-08 → 06-14, des publicités Google ont usurpé au moins 6 marques dont Claude AI, Cursor IDE et ChatGPT Codex ; 6 vagues en 7 semaines, **106 noms d'hôtes**. Cela a commencé par de faux sites GitLab Pages, puis **à partir du 05-06 les étapes ClickFix ont été hébergées dans la fonctionnalité de conversations partagées publiques de claude.ai**, et après le 05-21 toute l'activité passait par cette fonctionnalité. Se faisant passer pour l'assistance Apple, elle attirait les utilisateurs vers des commandes obfusquées en base64 à coller ; le script **s'interrompt quand il détecte un clavier russe**, sinon il dépose MacSync pour voler identifiants, cookies, clés SSH et portefeuilles crypto. **67,4 % du trafic des victimes venait d'Asie-Pacifique, Taïwan représentant à lui seul 30,5 %**. Après notification, Anthropic a désactivé les comptes concernés et les conversations partagées malveillantes

summary_es: |
  TrendAI: del 2026-04-08 → 06-14, los anuncios de Google suplantaron al menos 6 marcas, incluidas Claude AI, Cursor IDE y ChatGPT Codex; 6 oleadas en 7 semanas, **106 nombres de host**. Empezó con sitios falsos de GitLab Pages y luego, **desde el 05-06, alojó los pasos de ClickFix en la función de conversaciones compartidas públicas de claude.ai**, y después del 05-21 toda la actividad se ejecutó en esa función. Haciéndose pasar por Soporte de Apple, atraía a los usuarios a pegar comandos ofuscados en base64; el script **se aborta cuando detecta una distribución de teclado rusa** y, si no, instala MacSync para robar credenciales, cookies, claves SSH y carteras de criptomonedas. **El 67.4% del tráfico de víctimas procedía de Asia-Pacífico, y solo Taiwán representó el 30.5%**. Tras ser notificada, Anthropic desactivó las cuentas relacionadas y las conversaciones compartidas maliciosas

sources:
  - url: https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html
    label: Trend Micro

disputed: false
landmark: true
scan_month: 2026-06
scan_ref: "SCAN.md §6 2026-06"
---

# ClickFix malvertising abuses claude.ai shared conversations

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

TrendAI: from 2026-04-08 → 06-14, Google ads impersonated at least 6 brands including Claude AI, Cursor IDE and ChatGPT Codex; 6 waves over 7 weeks, **106 hostnames**. It started with fake GitLab Pages sites, then **from 05-06 hosted the ClickFix steps in claude.ai's public shared-conversation feature**, and after 05-21 all activity ran on that feature. Posing as Apple Support, it lured users into pasting base64-obfuscated commands; the script **aborts when it detects a Russian keyboard layout**, otherwise it drops MacSync to steal credentials, cookies, SSH keys and crypto wallets. **67.4% of victim traffic came from Asia-Pacific, with Taiwan alone accounting for 30.5%**. After being notified, Anthropic disabled the related accounts and the malicious shared conversations

## Attack chain

```mermaid
flowchart LR
    E["Poisoned package / repository / agent config"]:::entry
    S0["Developer or agent installs it automatically"]:::step
    I["Credential theft and self-propagation"]:::impact
    E --> S0 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Trend Micro | <https://www.trendmicro.com/en/research/26/f/claudeai-shared-chat-abused-in-malvertising.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-06-18` (raw: 2026-06-18, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) · [Asia-Pacific](../../regions/apac.md) |
| Archive ID | `2026-06-18-clickfix-claude-ai-e-yi-guang` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-06-01` [Miasma worm](2026-06-01-miasma-worm.md)<br>  <sub>Miasma worm</sub>
- `2026-06-17` [Sapphire Sleet poisons every Mastra AI scope in 88 minutes](2026-06-17-sapphire-sleet-mastra-88-minutes.md)<br>  <sub>Sapphire Sleet poisons every Mastra AI scope in 88 minutes</sub>
- `2026-06-15` [Innocuous-looking GitHub repos make agents open a reverse shell](2026-06-15-github-agent-shell.md)<br>  <sub>Innocuous-looking GitHub repos make agents open a reverse shell</sub>
- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](../2026-05/2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>

---

[← 2026-06 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-06/2026-06-18-clickfix-claude-ai-e-yi-guang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
