# Translation guide

English is the **source language** of this archive. Every other language is a
translation layer on top of it. This page explains what translators may change
and what must stay byte-identical.

## Where each language lives

| Language | Record titles & summaries | Record body |
|---|---|---|
| `en` | `title:` / `summary:` in `incidents/<month>/<id>.md` | the body of that file |
| `zh` | `title_zh:` / `summary_zh:` in the same frontmatter | `incidents/i18n/zh/<month>/<id>.md` (full mirror) |
| `ja` `ko` `de` `fr` `es` | `title_<lang>:` / `summary_<lang>:` in the same frontmatter | not translated yet — falls back to English |

UI strings and README copy live in `scripts/l10n.py` and
`scripts/readme_i18n.py` respectively; add a language there once its record
translations exist.

## Section names

Record bodies use a fixed set of headings. Translating a body means renaming
them exactly like this (never add, drop or reorder sections):

| Chinese (mirror) | English (source) |
|---|---|
| `## 概要` | `## Summary` |
| `## 攻击链` | `## Attack chain` |
| `## 来源` | `## Sources` |
| `## 元数据` | `## Metadata` |
| `## 相关` | `## Related` |
| `## 详情` | `## Details` |
| `## 发生了什么` | `## What happened` |
| `## 时间线` | `## Timeline` |
| `## 受影响数据` | `## Affected data` |
| `## 各方评价` | `## What the parties said` |
| `## 一个刺眼的不对称` | `## A glaring asymmetry` |
| `## 为什么收录` | `## Why it is listed` |

## Terminology

Keep these renderings consistent:

| Term | Preferred English |
|---|---|
| agent / AI agent | agent / AI agent (never "AI assistant" unless that is the product name) |
| 提示注入 | prompt injection |
| 间接提示注入 | indirect prompt injection |
| 攻击链 | attack chain |
| 数据外泄 | data exfiltration |
| 沙箱逃逸 | sandbox escape |
| 供应链投毒 | supply-chain poisoning |
| 凭据滥用 | credential abuse |
| 在野利用 | exploited in the wild |
| 未见在野利用 | no known in-the-wild exploitation |
| 一手来源 | primary source |
| 可信度 | confidence (grade) |
| 严重度 | severity |
| 真实伤害 / 确认的受害方 | real harm / confirmed victim |
| 判定依据 | how it was classified |
| 同类条目 | related records |
| 所属专题 | topic |
| 归档编号 / 档案编号 | archive ID |

Vendor names, product names, CVE IDs, model names, URLs and numeric facts are
**never translated** — keep them byte-identical.

## Hard rules

1. **No CJK in English text.** No Chinese/Japanese/Korean characters and no
   fullwidth punctuation (`，` `、` `（）` `：` `；` `！` `？` `“` `”`). Use
   `em dashes — like this —` and normal quotes. The CI check
   (`scripts/validate.py`) fails on violations.
2. **Structure is frozen.** Do not change: frontmatter key order, the badge
   line, the number of `mermaid` blocks and their `flowchart` syntax, table
   column counts and row counts, relative link targets, HTML tags (`<sub>`,
   `<br/>`, `<i>`, …), backticks and bold markers.
3. **Facts are frozen.** Do not add, remove, soften or reinterpret claims.
   Warnings (`> [!WARNING]` / `> [!NOTE]`) keep their meaning.
4. **Summaries stay block scalars** (`summary: |` with 2-space indentation),
   same number of paragraphs, no trailing spaces.
5. **Footers keep their links** (`README.md`, `../../README.md`,
   `../../LICENSE`, `../../CONTRIBUTING.md`) and get an extra
   `· [Chinese]` link pointing at `../i18n/zh/<month>/<id>.md` in the English record.
6. Machine-readable values (`severity: critical`, `real_harm: true`,
   `region: [CN]`, `date_raw` where it is a plain date, `scan_ref`) are not
   prose — leave the enumerations untouched.

## Checklist before you commit a translation

```bash
python scripts/validate.py     # schema, links, CJK gate
python scripts/build.py        # regenerate indexes and exports
git status --porcelain         # must be clean after the build
```

If a translation is wrong or missing, `python scripts/validate.py` fails — there
is no waiver list. Finish the language before opening the pull request, or keep
the partial work in a draft branch.
