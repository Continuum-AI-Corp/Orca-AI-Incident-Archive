---
id: 2025-02-06-hugging-face-nullifai
title: "Hugging Face \"nullifAI\" malicious models"
title_zh: "Hugging Face \"nullifAI\" 恶意模型"
title_ja: "Hugging Faceの「nullifAI」悪性モデル"
title_ko: "Hugging Face \"nullifAI\" 악성 모델"
title_de: "Hugging Face „nullifAI“: bösartige Modelle"
title_fr: "Modèles malveillants « nullifAI » sur Hugging Face"
title_es: "Modelos maliciosos \"nullifAI\" en Hugging Face"
date: 2025-02-06
date_precision: day
date_raw: "2025-02-06"

kind: incident
type: [SUPPLY]
severity: high
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  ReversingLabs found 2 malicious pickle models. The trick: PyTorch format but compressed with **7z instead of the default ZIP**, which stops `torch.load()` from loading them and thereby **evades Hugging Face's Picklescan detection**; they contain a reverse shell to a hardcoded IP


summary_zh: |
  ReversingLabs 发现 2 个恶意 pickle 模型。手法：PyTorch 格式但用 **7z 而非默认 ZIP 压缩**，使 `torch.load()` 无法加载，从而**绕过 Hugging Face 的 Picklescan 检测**；内含连向硬编码 IP 的反弹 shell

summary_ja: |
  ReversingLabsが悪性のpickleモデル2件を発見。手口は、PyTorch形式でありながらデフォルトのZIPではなく**7zで圧縮**することで`torch.load()`での読み込みを妨げ、それにより**Hugging FaceのPicklescan検出を回避**するもの。ハードコードされたIPへのリバースシェルを含んでいた

summary_ko: |
  ReversingLabs는 악성 pickle 모델 2개를 발견했다. 수법은 PyTorch 형식이지만 기본 ZIP 대신 **7z로 압축**해 `torch.load()`가 로드하지 못하게 함으로써 **Hugging Face의 Picklescan 탐지를 회피**하는 것이었다. 모델에는 하드코딩된 IP로 연결하는 리버스 셸이 들어 있었다

summary_de: |
  ReversingLabs fand 2 bösartige Pickle-Modelle. Der Trick: PyTorch-Format, aber mit **7z statt des standardmäßigen ZIP** komprimiert, wodurch `torch.load()` sie nicht laden kann und sie so **die Picklescan-Erkennung von Hugging Face umgehen**; sie enthalten eine Reverse Shell zu einer fest codierten IP

summary_fr: |
  ReversingLabs a trouvé 2 modèles pickle malveillants. L'astuce : un format PyTorch mais compressé en **7z au lieu du ZIP par défaut**, ce qui empêche `torch.load()` de les charger et **contourne ainsi la détection Picklescan de Hugging Face** ; ils contiennent un reverse shell vers une IP codée en dur

summary_es: |
  ReversingLabs encontró 2 modelos pickle maliciosos. El truco: formato PyTorch pero comprimidos con **7z en lugar del ZIP predeterminado**, lo que impide que `torch.load()` los cargue y así **elude la detección de Picklescan de Hugging Face**; contienen un reverse shell hacia una IP codificada de forma fija

sources:
  - url: https://www.reversinglabs.com/press-releases/reversinglabs-identifies-novel-ml-malware-hosted-on-leading-hugging-face-ai-model-platform
    label: ReversingLabs
  - url: https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html
    label: THN

disputed: false
landmark: false
scan_month: 2025-02
scan_ref: "SCAN.md §5 2025-02"
---

# Hugging Face "nullifAI" malicious models

![severity: high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: incident](https://img.shields.io/badge/kind-incident-48545A?style=flat-square) ![type: SUPPLY](https://img.shields.io/badge/type-SUPPLY-B08528?style=flat-square)

## Summary

ReversingLabs found 2 malicious pickle models. The trick: PyTorch format but compressed with **7z instead of the default ZIP**, which stops `torch.load()` from loading them and thereby **evades Hugging Face's Picklescan detection**; they contain a reverse shell to a hardcoded IP

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
| 1 | ReversingLabs | <https://www.reversinglabs.com/press-releases/reversinglabs-identifies-novel-ml-malware-hosted-on-leading-hugging-face-ai-model-platform> |
| 2 | THN | <https://thehackernews.com/2025/02/malicious-ml-models-found-on-hugging.html> |

## Metadata

| Field | Value |
|---|---|
| Date | `2025-02-06` (raw: 2025-02-06, precision `day`) |
| Kind | Incident `incident` |
| Type | [`SUPPLY`](../../taxonomy/types.md#supply) Supply-chain poisoning |
| Severity | **High** `high` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2025-02-06-hugging-face-nullifai` |

<sub>**Why this classification:** Real incident without a confirmed specific victim. Rated `high`: real damage is limited in scope, or it is a CVSS 9+ severe flaw, or a capability demonstration of significance. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Agent supply-chain poisoning](../../topics/agent-supply-chain.md)

**Related records:**

- `2025-03-18` [Cursor / Copilot "Rules File Backdoor"](../2025-03/2025-03-18-cursor-copilot-rules-file.md)<br>  <sub>Cursor / Copilot "Rules File Backdoor"</sub>
- `2025-04-01` ["Slopsquatting" gets its name](../2025-04/2025-04-01-slopsquatting-gai-nian-cheng-xing.md)<br>  <sub>"Slopsquatting" gets its name</sub>
- `2025-07-13` [Amazon Q Developer extension poisoned](../2025-07/2025-07-13-amazon-q-extension-poisoned.md)<br>  <sub>Amazon Q Developer extension poisoned</sub>
- `2025-08-08` [Salesloft Drift OAuth token theft](../2025-08/2025-08-08-salesloft-drift-oauth-theft.md)<br>  <sub>Salesloft Drift OAuth token theft</sub>

---

[← 2025-02 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2025-02/2025-02-06-hugging-face-nullifai.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
