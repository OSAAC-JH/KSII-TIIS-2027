# Proposed Writing Roadmap for the Editing Staff (Conditional on Proposal Acceptance)

> Status: REVISED DRAFT (2026-11-22). This is the same text as the Attachment in `TIIS_Craft_GenAI_Proposal_Draft.docx`.
> It applies only if the proposal is accepted. It describes how the authors will write the full survey with AI assistance while staying responsible for every claim and citation.
> Week numbers count from the acceptance notice. Calendar dates and the submission deadline are [TBD].

## 1. Principles

- **AI is a copilot, not the pilot.** The authors set the research questions, the taxonomy, and the conclusions. AI tools help with structuring, drafting, consistency checks, and citation verification.
- **No source the authors have not read.** A reference enters the corpus only after an author has read it. AI may synthesize the authors' notes but may not add sources ("Do not add any sources I haven't provided").
- **Gaps are marked, not filled.** Where evidence is missing, the draft carries a `[MATERIAL GAP]` or `[TBD]` marker instead of invented text.
- **Continuity with TIIS-S1-2025-Nov-1354.R1.** The survey is framed as a follow-up to the authors' previous TIIS survey (vol. 20, no. 4, 2026; DOI 10.3837/tiis.2026.04.027). It is cited in the Introduction, revisited in the Conclusion, and listed in the References.
- **Delivery, not claims.** Prose-editing tools may change how a claim is worded, never what it says. Apparent scientific errors are flagged for the authors, not silently rewritten.
- **Transparent disclosure.** AI use is disclosed in the manuscript according to the TIIS and KSII policy in force at submission.

## 2. Stage-by-Stage Roadmap

| Stage | Weeks | Main activity | Tools / technique | Output (gate to next stage) |
|---|---|---|---|---|
| 0. Kick-off | W1 | Fix scope, RQs, and inclusion criteria from the accepted proposal. Incorporate Editing Staff comments. Confirm the page limit and deadline [TBD]. Set the time budget (about 70% pre-writing, 10% drafting, 20% revision). | Socratic planning (`/ars-plan`); `sciwrite-process`; review-article guidance in `sciwrite-proposals` | Scope memo, RQ list, schedule |
| 1. Framing | W1 | Rank three candidate framings by novelty and defensibility. List the strongest counter-argument to each. | Adversarial framing prompt | Final framing and contribution statement |
| 2. Literature corpus | W2-W3 | Run the systematic search described in proposal Section 3.1 (ACM, IEEE, Scopus, Web of Science, plus backward tracing), starting from the 30 seed studies. Authors read the sources and take structured notes. | PRISMA-style flow; Zotero; `/ars-lit-review` only to find gaps in the authors' corpus | Flow diagram, annotated corpus, query and provenance log |
| 2.5 Integrity gate I | W3 | Check every candidate citation for existence and metadata. | DOI resolution (Crossref, JaLC); Semantic Scholar matching | Verified bibliography (zero unverified items) |
| 3. Taxonomy and synthesis | W3-W4 | Apply the extraction scheme (proposal Table 4). Build the four syntheses (proposal Section 3.3). Fix a controlled vocabulary for terms and acronyms. | Synthesis from author notes only; SWiM reporting items | Taxonomy figure, comparison tables, glossary |
| 4. Section drafting | W4-W6 | Draft figures and tables first, then body sections, then Introduction, Conclusion, and Abstract. One section per pass, no more than about 800-1,000 words, each reviewed before the next. | Paragraph-level outlines with purpose and evidence; `sciwrite-manuscript` (section order and tense, adapted to a survey); TIIS template; style calibration on the authors' prior papers, including 1354.R1 | Full first draft in the TIIS template |
| 4.5 Integrity gate II | W6 | Zero-tolerance re-check for fabricated citations, unsupported claims, and numbers not found in the sources. This covers every figure carried over from the proposal slides. | Claim-to-source audit; figure and table checklist | Integrity report signed off by the authors |
| 5. Internal review | W7 | Simulated peer review by an editor, methodology, domain, and cross-disciplinary reviewers, plus a devil's advocate. Logic-flow and Abstract/Conclusion consistency checks. | `academic-paper-reviewer` (0-100 rubric); hostile-reviewer prompt | Prioritized revision list |
| 6. Revision and language | W7-W8 | Revise. Tighten wording without losing claims, numbers, or citations. Run mechanical audits. Human proofreading. | `sciwrite-prose`; `prose_audit.py`, `keyword_consistency.py`, `numeric_consistency.py`; tracked changes; professional proofreading | Audit report with each flag resolved or justified |
| 7. Submission | W8 | AI-use disclosure, cover letter, format check, authorship and similarity checks. Update online-first references. | TIIS submission checklist; `sciwrite-publish`; separate similarity checker | Submitted manuscript |
| 8. Reviewer response | After review | Extract each reviewer comment and mark it Revise, Defend, or Needs analysis. Draft neutral responses. | `sciwrite-publish`; traceability matrix (comment → change → location) | Response letter and revised manuscript |

## 3. Quality and Integrity Controls

- **Citation checks:** An author verifies each reference against its DOI or publisher page. The 30 seed references were checked against Crossref and JaLC on 2026-11-22. Four of them must be updated before submission because they are online-first or have no page numbers yet: [R09], [R10], [R23], and [R29] pages.
- **Number checks:** Every figure or statistic in the text is traced to a cited source.
- **Consistency checks:** The Abstract, contribution list, and Conclusion state the same claims. Scripts check terms, acronyms, and numbers. Their output is a list of candidates for the authors to judge, not automatic fixes.
- **Voice checks:** The authors rewrite AI-assisted passages in their own voice. Raw AI output is not submitted.
- **Model use:** A mid-size model handles routine drafting and editing. A stronger model handles whole-manuscript consistency and multi-source synthesis. Fast models are used only for mechanical formatting, never for citations.

## 4. How the Three Sources Divide the Work

| Source | Main role in this roadmap | Not covered |
|---|---|---|
| ProofreaderPro guide [S1] | Prompting techniques: framing, synthesis without added sources, section-by-section drafting, hostile-reviewer self-review | No automated checks or pipeline |
| Academic Research Skills (ARS), as summarized in [S2] | Research pipeline: literature search, citation verification, integrity gates, simulated peer review | Sentence-level style. Licensed CC BY-NC 4.0 (non-commercial use only) |
| Scientific Writing Skills (`sciwrite`) [S3] | Writing craft: process planning, section order and tense, prose editing, term and number consistency scripts, publication ethics | Citation verification, plagiarism checks, judgment of scientific claims |

ARS checks that each citation exists and supports its claim. `sciwrite` checks that the text states the claim clearly and consistently. The two complement each other and are used at different stages.

## 5. Responsibilities and Requests to the Editing Staff

- **Authors:** research questions, source reading, taxonomy, interpretation, final wording, and all verification sign-offs.
- **AI tools:** structuring, first-pass drafting from author notes, consistency and integrity checks, and simulated review.
- **Editing Staff (requested):** feedback on scope and section structure at Stage 0 and on the draft outline before Stage 4. We also ask the Editing Staff to confirm the page limit for survey papers, the submission timeline, and the policy on disclosing AI-assisted writing.

## 6. Sources for This Roadmap

- [S1] Moe, "Claude for Academic Research Writing: A Practical Guide" (in Korean), ProofreaderPro.ai, 2026-08-10. https://proofreaderpro.ai/ko/blog/how-to-use-claude-for-research-writing
- [S2] 9bow, "Academic Research Skills" (in Korean), PyTorch Korea User Group, 2026-05-28. https://discuss.pytorch.kr/t/academic-research-skills-claude-code/10385. The post describes https://github.com/Imbad0202/academic-research-skills, which was not checked directly.
- [S3] dvdsosa, Scientific Writing Skills (based on K. Sainani, *Writing in the Sciences*, Stanford University). https://github.com/dvdsosa/scientific-writing-skills

## Changes from the Previous Draft (branch `claude/vibrant-hawking-l3nb7h`)

- Linked the stages to the actual proposal: the search sources from Section 3.1, the 30 seed studies, the extraction scheme in Table 4, and the SWiM synthesis.
- Changed the word limit in Stage 4 to "no more than about 800-1,000 words" per pass, to match S1's point that quality drops above that length.
- Added the DOI check already done (Crossref/JaLC) and the four references that are not final yet.
- Added the requests to the Editing Staff (page limit, timeline, AI-disclosure policy) and marked dates as [TBD].
- S2 is now cited as a secondhand summary of the ARS repository, since the repository itself was not checked.
