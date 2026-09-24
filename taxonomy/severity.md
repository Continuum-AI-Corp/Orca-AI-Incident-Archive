# Severity and kind

Severity here is **not** CVSS. CVSS scores a vulnerability's theoretical exploitability; this field records **what has already happened**. A CVSS 9.8 vulnerability that was never exploited is `high` + `real_harm: false` in this archive; an operation that punched through nine government agencies of one country is `critical` whether or not a CVE exists.

## `severity`

| Value | Records | Criterion | Example |
|---|---|---|---|
| ![critical](https://img.shields.io/badge/severity-critical-88091D?style=flat-square) **Critical** | 47 | Any of three triggers: ① confirmed real damage at the **multi-organisation / government / critical-infrastructure / supply-chain worm** level; ② a **first-of-its-kind** capability milestone with a real victim; ③ a research demonstration that **overturns a widely deployed defensive assumption** (here `real_harm: false`) | ① [GTG-1002](../incidents/2025-11/2025-11-13-gtg-1002-first-ai-orchestrated-espionage.md) · ② [Nine Mexican government agencies](../incidents/2026-02/2026-02-25-mexico-nine-agencies-breached.md) · ③ [Trail of Bits: VMs won't contain cyber-capable agents](../incidents/2026-08/2026-08-26-trailofbits-vm-cannot-contain-networked-agents.md) |
| ![high](https://img.shields.io/badge/severity-high-B23B40?style=flat-square) **High** | 145 | Confirmed real damage of limited scope; or a severe flaw at CVSS 9+ (even with no known exploitation in the wild); or a significant capability demonstration | [EchoLeak](../incidents/2025-06/2025-06-11-echoleak.md) (CVSS 9.3, no known in-the-wild exploitation) |
| ![medium](https://img.shields.io/badge/severity-medium-C4615F?style=flat-square) **Medium** | 80 | A controlled demonstration, a moderate flaw, or an incident scoped to a single user / single machine | Most research demos and single-machine rogue incidents |
| ![low](https://img.shields.io/badge/severity-low-8C6A6A?style=flat-square) **Low** | 8 | Background entries | Background entries kept only for timeline continuity |
| ![info](https://img.shields.io/badge/severity-info-6B7175?style=flat-square) **Info** | 85 | Policy, regulation, vendor announcements and intelligence reports; **excluded from incident counts** | Regulatory actions, vendor announcements, threat-intelligence reports |

## `kind`

| Value | Records | Meaning | Counted as an incident |
|---|---|---|---|
| `incident` Incident | 145 | A real-world event (whether or not there was an attacker) | Yes |
| `vulnerability` Vulnerability disclosure | 47 | A vulnerability disclosure. `real_harm` depends on evidence of exploitation in the wild | Yes |
| `research` Research demo | 88 | A controlled demonstration by a research organisation or a vendor. Listed to mark **when an attack surface became public** | No |
| `report` Threat report | 15 | A threat-intelligence report aggregating several events; not counted as a single incident in itself | No |
| `policy` Policy & regulation | 70 | Regulation, legislation, vendor policy and defensive-side moves | No |

## `real_harm`

**This is the single most important field in the archive.** The most common distortion in projects of this kind is mixing lab demos and real intrusions into one table, and that is how a number like "300 AI incidents in 2026" appears.

| Value | Records | Meaning |
|---|---|---|
| `true` | 133 | There is a **confirmed victim**: an organisation, data, funds or a system suffered actual damage |
| `false` | 147 | A research demo, or a vulnerability that was fixed with no known exploitation in the wild |
| `null` | 85 | Not applicable (`policy` / `report`) |

## `ai_involvement`

Whether AI was actually involved is decided by the **primary source**, not by the headline.

| Value | Records | Meaning |
|---|---|---|
| `confirmed` Confirmed | 356 | A primary source confirms AI involvement |
| `unverified` Unverified | 2 | Widely passed around as an AI incident, but **no AI can be found** in the primary sources. Kept so that such claims **can be searched for and rebutted** |
| `disputed` Disputed | 5 | The vendor and the reporting party conflict; both accounts are kept side by side in the record |
| `not-applicable` Not applicable | 2 | No direct connection to agents; kept only as timeline background |

---

[← Back to home](../README.md) · [Types](types.md) · [Confidence](confidence.md)
