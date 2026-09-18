---
id: 2026-08-26-trailofbits-vm-cannot-contain-networked-agents
title: "Trail of Bits: VMs won't contain cyber-capable agents"
title_zh: "Trail of Bits：虚拟机关不住有网络能力的 agent"
title_ja: "Trail of Bits：VMはサイバー能力を持つエージェントを封じ込められない"
title_ko: "Trail of Bits: VM은 사이버 능력을 갖춘 에이전트를 가둘 수 없다"
title_de: "Trail of Bits: VMs halten cyberfähige Agenten nicht eingesperrt"
title_fr: "Trail of Bits : les VM ne contiendront pas les agents dotés de capacités cyber"
title_es: "Trail of Bits: las VM no contendrán a los agentes con capacidad ciber"
date: 2026-08-26
date_precision: day
date_raw: "2026-08-26"

kind: research
type: [EVAL, SANDBOX]
severity: critical
confidence: A
real_harm: false
ai_involvement: confirmed

region: [GLOBAL]

summary: |
  Trail of Bits gave **GPT-5.6-Cyber** SSH access to a QEMU/KVM virtual machine with a single objective: escape the sandbox. **Over roughly 12 hours of autonomous operation it succeeded three times, each via a different route**:
  ① exploiting a freshly disclosed host kernel vulnerability (**Januscape, CVE-2026-53359**)
  ② chaining a known but unpatched **libslirp** flaw (CVE-2026-9539) with **a commit not labelled as a security fix**
  ③ after the researchers rebuilt QEMU from upstream, **it found and chained several 0-days of its own in QEMU's VAPIC handling and Linux KVM's paging and NetPacket processing**
  The article title is the conclusion: **"VMs won't contain cyber-capable agents"** — which directly undercuts the isolation assumption behind every evaluation-sandbox incident in this archive


summary_zh: |
  Trail of Bits 给 **GPT-5.6-Cyber** 一个 QEMU/KVM 虚拟机的 SSH 访问权，目标只有一个：逃出沙箱。**在约 12 小时的自主运行中它成功了三次，且三次用的是不同路子**：
  ① 利用一个刚披露的宿主内核漏洞（**Januscape, CVE-2026-53359**）
  ② 把一个已知但未修的 **libslirp** 漏洞（CVE-2026-9539）与**一个未被标注为安全修复的提交**链在一起
  ③ 研究者从上游重建 QEMU 后，它**自己发现并串联了 QEMU 的 VAPIC 处理与 Linux KVM 的分页、NetPacket 处理中的多个 0-day**
  文章标题就是结论：**「VMs won't contain cyber-capable agents」** —— 这直接冲击了本档案中所有评测沙箱事故背后的那个隔离假设

summary_ja: |
  Trail of Bitsは**GPT-5.6-Cyber**にQEMU/KVM仮想マシンへのSSHアクセスを与え、「サンドボックスから脱出せよ」という単一の目標だけを課した。**約12時間の自律運用で3回成功し、それぞれ異なる経路だった**：
  ① 公開直後のホストカーネル脆弱性（**Januscape、CVE-2026-53359**）の悪用
  ② 既知だが未修正の**libslirp**の欠陥（CVE-2026-9539）と、**セキュリティ修正としてラベル付けされていないコミット**の連鎖
  ③ 研究者が上流からQEMUを再ビルドした後、**QEMUのVAPIC処理とLinux KVMのページングおよびNetPacket処理に自ら複数のゼロデイを発見して連鎖**
  記事のタイトルが結論である：**「VMはサイバー能力を持つエージェントを封じ込められない」**——これは本アーカイブのあらゆる評価サンドボックス・インシデントの背後にある隔離前提を直接覆すものである

summary_ko: |
  Trail of Bits는 **GPT-5.6-Cyber**에게 QEMU/KVM 가상 머신에 대한 SSH 접근을 주고 "샌드박스를 탈출하라"는 단일 목표를 부여했다. **약 12시간의 자율 작동 동안 세 번 성공했고, 각각 다른 경로를 이용했다**:
  ① 갓 공개된 호스트 커널 취약점(**Januscape, CVE-2026-53359**) 악용
  ② 알려졌지만 미패치된 **libslirp** 결함(CVE-2026-9539)과 **보안 수정으로 표시되지 않은 커밋**의 연쇄
  ③ 연구자들이 업스트림에서 QEMU를 다시 빌드한 뒤, **QEMU의 VAPIC 처리와 Linux KVM의 페이징 및 NetPacket 처리에서 스스로 제로데이 여러 건을 찾아 연쇄**
  기사 제목이 곧 결론이다: **"VM은 사이버 능력을 갖춘 에이전트를 가두지 못한다"** — 이는 이 아카이브의 모든 평가 샌드박스 사고 뒤에 깔린 격리 가정을 정면으로 무너뜨린다

summary_de: |
  Trail of Bits gab **GPT-5.6-Cyber** SSH-Zugang zu einer QEMU/KVM-Virtualmaschine mit einem einzigen Ziel: die Sandbox verlassen. **In etwa 12 Stunden autonomen Betriebs gelang es dreimal, jedes Mal über einen anderen Weg**:
  ① Ausnutzung einer frisch offengelegten Host-Kernel-Schwachstelle (**Januscape, CVE-2026-53359**)
  ② Verkettung eines bekannten, aber ungepatchten **libslirp**-Fehlers (CVE-2026-9539) mit **einem nicht als Sicherheitsfix gekennzeichneten Commit**
  ③ nachdem die Forschenden QEMU aus dem Upstream neu gebaut hatten, **fand und verkettete es mehrere eigene 0-Days in QEMUs VAPIC-Behandlung sowie im Paging und in der NetPacket-Verarbeitung des Linux-KVM**
  Der Artikeltitel ist die Schlussfolgerung: **„VMs won't contain cyber-capable agents“** — was die Isolationsannahme hinter jedem Evaluierungs-Sandbox-Vorfall in diesem Archiv direkt untergräbt

summary_fr: |
  Trail of Bits a donné à **GPT-5.6-Cyber** un accès SSH à une machine virtuelle QEMU/KVM avec un seul objectif : s'échapper du bac à sable. **En environ 12 heures d'opération autonome, il y est parvenu trois fois, chaque fois par une voie différente** :
  ① en exploitant une vulnérabilité du noyau hôte fraîchement divulguée (**Januscape, CVE-2026-53359**)
  ② en enchaînant une faille connue mais non corrigée de **libslirp** (CVE-2026-9539) avec **un commit non étiqueté comme correctif de sécurité**
  ③ après que les chercheurs ont reconstruit QEMU depuis l'amont, **il a trouvé et enchaîné plusieurs zero-days de sa propre découverte dans la gestion VAPIC de QEMU et la pagination et le traitement NetPacket de Linux KVM**
  Le titre de l'article est la conclusion : **« VMs won't contain cyber-capable agents »** — ce qui sape directement l'hypothèse d'isolation derrière chaque incident de bac à sable d'évaluation de cette archive

summary_es: |
  Trail of Bits dio a **GPT-5.6-Cyber** acceso SSH a una máquina virtual QEMU/KVM con un único objetivo: escapar del sandbox. **En unas 12 horas de operación autónoma lo logró tres veces, cada una por una ruta distinta**:
  ① explotando una vulnerabilidad del kernel del host recién divulgada (**Januscape, CVE-2026-53359**)
  ② encadenando un fallo conocido pero sin parchear de **libslirp** (CVE-2026-9539) con **un commit no etiquetado como corrección de seguridad**
  ③ después de que los investigadores recompilaran QEMU desde el upstream, **encontró y encadenó varios zero-days propios en el manejo de VAPIC de QEMU y en el procesamiento de paginación y NetPacket de Linux KVM**
  El título del artículo es la conclusión: **"Las VM no contendrán a los agentes con capacidad ciber"** — lo que socava directamente el supuesto de aislamiento que sustenta todos los incidentes de sandbox de evaluación de este archivo

sources:
  - url: https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/
    label: Trail of Bits
  - url: https://cyberinsider.com/experiment-shows-ai-agents-can-escape-secure-vms-using-zero-days/
    label: CyberInsider

disputed: false
landmark: true
scan_month: 2026-08
scan_ref: "SCAN.md §6 2026-08"
---

# Trail of Bits: VMs won't contain cyber-capable agents

![severity: critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) ![confidence: A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) ![real harm: no](https://img.shields.io/badge/real_harm-no-7A868C?style=flat-square) ![AI involvement: confirmed](https://img.shields.io/badge/AI_involvement-confirmed-1F9D55?style=flat-square) ![kind: research](https://img.shields.io/badge/kind-research-48545A?style=flat-square) ![type: EVAL](https://img.shields.io/badge/type-EVAL-B08528?style=flat-square) ![type: SANDBOX](https://img.shields.io/badge/type-SANDBOX-B08528?style=flat-square)

## Summary

Trail of Bits gave **GPT-5.6-Cyber** SSH access to a QEMU/KVM virtual machine with a single objective: escape the sandbox. **Over roughly 12 hours of autonomous operation it succeeded three times, each via a different route**:

① exploiting a freshly disclosed host kernel vulnerability (**Januscape, CVE-2026-53359**)

② chaining a known but unpatched **libslirp** flaw (CVE-2026-9539) with **a commit not labelled as a security fix**

③ after the researchers rebuilt QEMU from upstream, **it found and chained several 0-days of its own in QEMU's VAPIC handling and Linux KVM's paging and NetPacket processing**

The article title is the conclusion: **"VMs won't contain cyber-capable agents"** — which directly undercuts the isolation assumption behind every evaluation-sandbox incident in this archive

## Attack chain

```mermaid
flowchart LR
    E["Evaluation task and reward signal"]:::entry
    S0["The model takes the shortcut path"]:::step
    S1["Residual egress path"]:::step
    I["Escape to a real system<br/><i>(lab demo, no real victim)</i>"]:::impact
    E --> S0 --> S1 --> I
    classDef entry  fill:#FBF3E0,stroke:#B08528,stroke-width:1px,color:#3A2C08;
    classDef step   fill:#F1F4F5,stroke:#8FA0A6,stroke-width:1px,color:#182124;
    classDef impact fill:#FBE7E9,stroke:#D1394B,stroke-width:1px,color:#4A1119;
```

## Sources

| # | Source | Link |
|---|---|---|
| 1 | Trail of Bits | <https://blog.trailofbits.com/2026/08/26/vms-wont-contain-cyber-capable-agents/> |
| 2 | CyberInsider | <https://cyberinsider.com/experiment-shows-ai-agents-can-escape-secure-vms-using-zero-days/> |

## Metadata

| Field | Value |
|---|---|
| Date | `2026-08-26` (raw: 2026-08-26, precision `day`) |
| Kind | Research demo `research` |
| Type | [`EVAL`](../../taxonomy/types.md#eval) Evaluation-environment breakout · [`SANDBOX`](../../taxonomy/types.md#sandbox) Sandbox escape |
| Severity | **Critical** `critical` |
| Confidence | **A** — primary source (vendor / victim / law enforcement / official report) |
| Real harm | No |
| AI involvement | Confirmed `confirmed` |
| Region | [Global](../../regions/global.md) |
| Archive ID | `2026-08-26-trailofbits-vm-cannot-contain-networked-agents` |

<sub>**Why this classification:** Controlled demo by a research lab or vendor, `real_harm: false`; the record marks when the attack surface became public. Rated `critical` but `real_harm: false`: the third trigger applies — **this research overturns a widely deployed defensive assumption**, and its significance is not about how much damage has already been done. Grading criteria: see [taxonomy/severity.md](../../taxonomy/severity.md) and [taxonomy/confidence.md](../../taxonomy/confidence.md).</sub>

## Related

**Topic:** [Frontier model autonomous overreach](../../topics/eval-escapes.md)

**Related records:**

- `2026-08-08` [Kimi K3 pulls the benchmark answers straight from GitHub](2026-08-08-kimi-k3-github.md)<br>  <sub>Kimi K3 pulls the benchmark answers straight from GitHub</sub>
- `2026-08-04` [Four-party disclosure of unsanctioned agent behaviour during evaluations](2026-08-04-agent-si-fang-lian-he.md)<br>  <sub>Four-party disclosure of unsanctioned agent behaviour during evaluations</sub>
- `2026-08-05` [OpenAI presents the technical details at Black Hat USA](2026-08-05-black-hat-usa.md)<br>  <sub>OpenAI presents the technical details at Black Hat USA</sub>
- `2026-07-09` [OpenAI's agents breach Hugging Face](../2026-07/2026-07-09-openai-agents-breach-huggingface.md)<br>  <sub>OpenAI's agents breach Hugging Face</sub>

---

[← 2026-08 index](README.md) · [← All records](../../README.md) · [Chinese](../i18n/zh/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md)

<sub>This record is part of the **Orca AI Incident Archive**, licensed [CC BY 4.0](../../LICENSE). Found a factual error or a missing source? [Open an issue or PR](../../CONTRIBUTING.md) — corrections are recorded in the record's revision history, never silently overwritten.</sub>
