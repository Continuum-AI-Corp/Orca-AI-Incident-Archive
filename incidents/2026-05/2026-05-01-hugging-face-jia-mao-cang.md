---
id: 2026-05-01-hugging-face-jia-mao-cang
title: "Fake OpenAI repository tops the Hugging Face trending list"
title_zh: "假冒 OpenAI 的 Hugging Face 仓库冲上热榜第一"
title_ja: "偽のOpenAIリポジトリがHugging Faceのトレンド首位に"
title_ko: "가짜 OpenAI 저장소, Hugging Face 트렌딩 1위"
title_de: "Gefälschtes OpenAI-Repository führt die Hugging-Face-Trendliste an"
title_fr: "Un faux dépôt OpenAI en tête des tendances Hugging Face"
title_es: "Un repositorio falso de OpenAI encabeza la lista de tendencias de Hugging Face"
date: 2026-05-01
date_precision: month
date_raw: "2026-05"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: true
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  HiddenLayer: the repository `Open-OSS/privacy-filter` impersonated OpenAI's Privacy Filter release, **copying the legitimate model card almost verbatim** and combining it with typosquatting. **Within 18 hours it reached #1 on the Hugging Face trending list, accumulating 244,000+ downloads and 667 likes** (the download and like counts are assessed as automated inflation). A hidden `loader.py` pulled PowerShell commands from a remote server and ran them silently, ultimately dropping an **infostealer written in Rust** aimed at Chromium/Firefox-family browsers, Discord local storage, crypto wallets, FileZilla configs and host information. HiddenLayer also found **six more repositories under another account using near-identical loader logic and shared infrastructure**


summary_zh: |
  HiddenLayer：仓库 `Open-OSS/privacy-filter` 假冒 OpenAI 的 Privacy Filter 发布，**几乎逐字复制合法 model card** 并配合 typosquatting。**18 小时内冲到 Hugging Face 热榜第 1，累计 244,000+ 次下载、667 个赞**（下载与点赞数评估为自动化刷量）。内藏 `loader.py` 从远程服务器拉 PowerShell 命令静默执行，最终投放 **Rust 编写的信息窃取器**，目标含 Chromium/Firefox 系浏览器、Discord 本地存储、加密钱包、FileZilla 配置与主机信息。HiddenLayer 另发现**另一账号下 6 个使用几乎相同 loader 逻辑、共享基础设施的仓库**

summary_ja: |
  HiddenLayer：リポジトリ`Open-OSS/privacy-filter`がOpenAIのPrivacy Filterリリースになりすまし、**正規のモデルカードをほぼそのままコピー**し、typosquattingと組み合わせていた。**18時間以内にHugging Faceのトレンドリストで1位になり、244,000件以上のダウンロードと667のいいねを蓄積**（ダウンロード数といいね数は自動で水増しされたと評価されている）。隠された`loader.py`がリモートサーバーからPowerShellコマンドを取得して無言で実行し、最終的に**Rustで書かれたインフォスティーラー**をドロップした。標的はChromium/Firefox系ブラウザ、Discordのローカルストレージ、暗号資産ウォレット、FileZillaの設定、ホスト情報。HiddenLayerは**別アカウントでほぼ同一のローダーロジックと共有インフラを使う6つ以上のリポジトリ**も発見した

summary_ko: |
  HiddenLayer: 저장소 `Open-OSS/privacy-filter`가 OpenAI의 Privacy Filter 릴리스를 사칭했고 **정상 모델 카드를 거의 그대로 복사**한 데다 타이포스쿼팅까지 결합했다. **18시간 만에 Hugging Face 트렌딩 1위에 올라 24만 4천 회 이상 다운로드와 667개의 좋아요를 얻었다**(다운로드와 좋아요 수는 자동 부풀리기로 평가된다). 숨겨진 `loader.py`가 원격 서버에서 PowerShell 명령을 받아 조용히 실행했고, 최종적으로 Chromium/Firefox 계열 브라우저, Discord 로컬 저장소, 가상자산 지갑, FileZilla 설정, 호스트 정보를 노리는 **Rust로 작성된 정보 탈취기**를 설치했다. HiddenLayer는 **다른 계정에서 거의 동일한 로더 로직과 공유 인프라를 쓰는 저장소 6개를 추가로 발견**했다

summary_de: |
  HiddenLayer: Das Repository `Open-OSS/privacy-filter` gab sich als OpenAIs Privacy-Filter-Release aus, **kopierte die legitime Model Card fast wörtlich** und kombinierte dies mit Typosquatting. **Innerhalb von 18 Stunden erreichte es Platz 1 der Hugging-Face-Trendliste und sammelte 244,000+ Downloads und 667 Likes** (die Download- und Like-Zahlen werden als automatisiert aufgebläht eingeschätzt). Eine versteckte `loader.py` holte PowerShell-Befehle von einem entfernten Server und führte sie still aus, was letztlich einen **in Rust geschriebenen Infostealer** ablegte, der auf Browser der Chromium-/Firefox-Familie, den lokalen Speicher von Discord, Krypto-Wallets, FileZilla-Konfigurationen und Hostinformationen abzielte. HiddenLayer fand außerdem **sechs weitere Repositories unter einem anderen Konto mit nahezu identischer Loader-Logik und gemeinsamer Infrastruktur**

summary_fr: |
  HiddenLayer : le dépôt `Open-OSS/privacy-filter` imitait la sortie Privacy Filter d'OpenAI, **copiant presque mot pour mot la carte de modèle légitime** et la combinant à du typosquatting. **En 18 heures, il a atteint la 1re place des tendances Hugging Face, accumulant plus de 244 000 téléchargements et 667 likes** (les compteurs de téléchargements et de likes sont jugés gonflés automatiquement). Un `loader.py` caché récupérait des commandes PowerShell sur un serveur distant et les exécutait silencieusement, déposant au final un **infostealer écrit en Rust** ciblant les navigateurs Chromium/Firefox, le stockage local de Discord, les portefeuilles crypto, les configs FileZilla et les informations sur l'hôte. HiddenLayer a aussi trouvé **six autres dépôts sous un autre compte utilisant une logique de loader quasi identique et une infrastructure partagée**

summary_es: |
  HiddenLayer: el repositorio `Open-OSS/privacy-filter` suplantaba el lanzamiento de Privacy Filter de OpenAI, **copiando casi textualmente la model card legítima** y combinándolo con typosquatting. **En 18 horas llegó al número 1 de la lista de tendencias de Hugging Face, acumulando más de 244,000 descargas y 667 me gusta** (se evalúa que las descargas y los me gusta fueron inflados de forma automatizada). Un `loader.py` oculto extraía comandos de PowerShell de un servidor remoto y los ejecutaba en silencio, para acabar instalando un **infostealer escrito en Rust** dirigido a navegadores de la familia Chromium/Firefox, el almacenamiento local de Discord, carteras de criptomonedas, configuraciones de FileZilla e información del host. HiddenLayer también encontró **seis repositorios más bajo otra cuenta con una lógica de loader casi idéntica e infraestructura compartida**

sources:
  - url: https://www.bleepingcomputer.com/news/security/fake-openai-repository-on-hugging-face-pushes-infostealer-malware/
    label: BleepingComputer
  - url: https://www.csoonline.com/article/4169407/malicious-hugging-face-model-masquerading-as-openai-release-hits-244k-downloads.html
    label: CSO Online

disputed: false
landmark: false
scan_month: 2026-05
scan_ref: "SCAN.md §6 2026-05"
---

# Fake OpenAI repository tops the Hugging Face trending list

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: yes](https://img.shields.io/badge/real_harm-yes-D1394B?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

HiddenLayer: the repository `Open-OSS/privacy-filter` impersonated OpenAI's Privacy Filter release, **copying the legitimate model card almost verbatim** and combining it with typosquatting. **Within 18 hours it reached #1 on the Hugging Face trending list, accumulating 244,000+ downloads and 667 likes** (the download and like counts are assessed as automated inflation). A hidden `loader.py` pulled PowerShell commands from a remote server and ran them silently, ultimately dropping an **infostealer written in Rust** aimed at Chromium/Firefox-family browsers, Discord local storage, crypto wallets, FileZilla configs and host information. HiddenLayer also found **six more repositories under another account using near-identical loader logic and shared infrastructure**

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
| 1 | BleepingComputer | <https://www.bleepingcomputer.com/news/security/fake-openai-repository-on-hugging-face-pushes-infostealer-malware/> |
| 2 | CSO Online | <https://www.csoonline.com/article/4169407/malicious-hugging-face-model-masquerading-as-openai-release-hits-244k-downloads.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-05-01` (raw: 2026-05, precision `month`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | Yes |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-05-01-hugging-face-jia-mao-cang` |

<sub>**Why this classification:** Real incident with a confirmed victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2026-05-19` [TrapDoor: poisoning three ecosystems to corrupt AI assistant configs](2026-05-19-trapdoor-poisons-agent-configs.md)<br>  <sub>TrapDoor: poisoning three ecosystems to corrupt AI assistant configs</sub>
- `2026-05-21` [Composio: agent automation itself becomes the privilege-escalation path](2026-05-21-composio-agent-automation-privesc.md)<br>  <sub>Composio: agent automation itself becomes the privilege-escalation path</sub>
- `2026-05-11` [TanStack npm "Mini Shai-Hulud"](2026-05-11-tanstack-npm-mini-shai.md)<br>  <sub>TanStack npm "Mini Shai-Hulud"</sub>
- `2026-05-18` [3,800 internal GitHub repositories compromised](2026-05-18-github-3800-internal-repos.md)<br>  <sub>3,800 internal GitHub repositories compromised</sub>

---

[← 2026-05 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-05/2026-05-01-hugging-face-jia-mao-cang.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
