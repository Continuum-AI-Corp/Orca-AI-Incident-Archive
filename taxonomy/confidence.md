# Confidence grading (`confidence`)

The grade rates **source quality**, not incident severity. Grade D does not mean false — it means "the accounts disagree; do not cite just one side".

| Grade | Records | Criterion |
|---|---|---|
| ![A](https://img.shields.io/badge/confidence-A-157A41?style=flat-square) **A** | 317 | Primary source: a vendor advisory, an affected party's disclosure, a law-enforcement filing, an official report PDF |
| ![B](https://img.shields.io/badge/confidence-B-2359A8?style=flat-square) **B** | 50 | Reporting by a research organisation or mainstream media, with checkable technical detail |
| ![C](https://img.shields.io/badge/confidence-C-9A6008?style=flat-square) **C** | 2 | Seen only in second-hand retellings, with no primary source |
| ![D](https://img.shields.io/badge/confidence-D-A82B39?style=flat-square) **D** | 3 | Key facts or attribution are disputed; all sides must be presented side by side |

| Grade | Meaning | Requirement to enter |
|---|---|---|
| **A** | First-hand disclosure by the party involved / vendor / government / CERT, or an official IPA·OWASP compilation (with links to primary sources) | Add directly |
| **B** | Blog by a well-known security research organisation, or mainstream media reporting | Add directly, labelled with the source |
| **C** | Seen only on aggregator sites / search snippets / AI-generated blogs, **with no primary source found** | ⛔ Must be re-verified before entry, see §9 |
| **D** | Attribution or the facts themselves are disputed | Present all sides, tag `disputed` |

---

## Why this column exists

In 2026 a fair share of "AI incident round-up" pages are **themselves AI-generated SEO content at scale**, inventing CVE numbers, inventing victim organisations, and writing demo PoCs up as real damage.

This review confirmed 3 specific contamination cases:

| Claim | What actually happened |
|---|---|
| "EchoLeak caused about US$200 million in financial impact" | **Fabricated.** Microsoft confirmed no known in-the-wild exploitation, and no primary report carries this figure. Removed in v2 |
| "Step Finance's AI trading agent had approval-free authority to move large transfers" | **No primary source supports it.** CoinDesk states plainly that "how the attacker gained access was not explained", and AI appears nowhere in the article. The AI framework appears only in AI marketing blogs. Downgraded in v2 |
| "Attackers used Claude Code as a C2 server for 18 days" | **No such event exists.** Suspected garbling of a Check Point CVE disclosure dated 2026-02-27. Removed in v2 |

**Therefore: every grade C entry must be re-verified before it enters the archive.**

---

---

[← Back to home](../README.md) · [Types](types.md) · [Severity](severity.md)
