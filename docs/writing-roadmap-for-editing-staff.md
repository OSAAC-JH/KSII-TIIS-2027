# Proposed Manuscript Development Roadmap (Conditional on Proposal Acceptance)

> Status: DRAFT. Prepared for the TIIS Editing Staff together with the survey proposal.
> This roadmap applies only after the proposal is accepted. It describes how the authors will
> write the full survey with AI assistance while keeping the authors responsible for every claim and citation.

## 1. Principles

- **AI is a copilot, not the pilot.** The authors set the research questions, the taxonomy, and the conclusions. AI tools help with structuring, drafting, consistency checks, and citation verification.
- **No source the authors have not read.** Every reference enters the corpus only after an author has read it. AI may synthesize the authors' notes but may not add sources (`Do not add any sources I haven't provided`).
- **Gaps are marked, not filled.** Where evidence is missing, the draft carries a `[MATERIAL GAP]` marker instead of invented text.
- **Continuity with TIIS-S1-2025-Nov-1354.R1.** The new survey is framed as a follow-up of the authors' earlier TIIS survey. That paper is cited in the Introduction, revisited in the Conclusion, and listed in the References.
- **Delivery, not claims.** Prose-editing tools may change how a claim is worded, never what it says. Apparent scientific errors are flagged for the authors, not silently rewritten.
- **Transparent disclosure.** AI use is disclosed in the manuscript according to the TIIS and KSII policy in force at submission.

## 2. Stage-by-Stage Roadmap

| Stage | Weeks | Main activity | Tools / technique | Output (gate to next stage) |
|---|---|---|---|---|
| 0. Kick-off | W1 | Fix scope, research questions, and inclusion criteria from the accepted proposal; incorporate Editing Staff comments; set the time budget (about 70% pre-writing, 10% drafting, 20% revision) | Socratic planning (`/ars-plan`); `sciwrite-process`; review-article guidance in `sciwrite-proposals` | Scope memo, RQ list, schedule, author checkpoint |
| 1. Framing | W1 | Rank 3 candidate framings by novelty and defensibility; list the strongest counter-argument to each | Adversarial framing prompt | Final framing and contribution statement |
| 2. Literature corpus | W2-W3 | Systematic search and screening; authors read sources and take structured notes | PRISMA flow; Zotero; `/ars-lit-review` only to find gaps in the authors' corpus | PRISMA diagram, annotated corpus, Material Passport (corpus + provenance) |
| 2.5 Integrity gate I | W3 | Check every candidate citation for existence and metadata | DOI resolution; Semantic Scholar matching; hallucinated-citation check | Verified bibliography (zero unverified items) |
| 3. Taxonomy and synthesis | W3-W4 | Build the taxonomy; write thematic synthesis, disagreements, and open questions with (Author, Year) tags; fix a controlled vocabulary for key terms and acronyms | Synthesis from author notes only | Taxonomy figure, comparison tables, term/acronym glossary |
| 4. Section drafting | W4-W6 | Draft figures and tables first, then the body sections, then Introduction, Conclusion, and Abstract last. One section per pass (about 800-1,000 words), each reviewed before the next. Draft fast, revise later | Paragraph-level outlines with purpose and evidence; `sciwrite-manuscript` (section order, tense per section, adapted to the survey structure); TIIS template; style calibration on the authors' prior papers (incl. 1354.R1) | Full first draft in TIIS template |
| 4.5 Integrity gate II | W6 | Zero-tolerance re-check: fabricated citations, unsupported claims, numbers not in the sources, early frame-lock | Claim-to-source audit; figure checklist | Integrity report signed off by authors |
| 5. Internal review | W7 | Simulated peer review (editor + methodology, domain, cross-disciplinary reviewers + devil's advocate); logic-flow and abstract/conclusion consistency checks | Academic Paper Reviewer (0-100 rubric) | Prioritized revision list (top weaknesses by severity) |
| 6. Revision and language | W7-W8 | Revise; tighten wording without losing claims, numbers, or citations; run mechanical audits on the `.docx`; human proofreading | `sciwrite-prose` (clutter, active voice, nominalisations, parallelism); `prose_audit.py`, `keyword_consistency.py` (term drift across sections), `numeric_consistency.py` (abstract vs. body numbers, e.g., number of surveyed papers); tracked changes; professional proofreading; reference manager (TIIS style) | Audit report with each flag resolved or justified; camera-ready candidate |
| 7. Submission | W8 | AI-use disclosure, cover letter, final format check, authorship and plagiarism check | TIIS submission checklist; `sciwrite-process` pre-submission checklist; `sciwrite-publish`; similarity check (separate tool) | Submitted manuscript |
| 8. Reviewer response | After review | Extract each reviewer comment; mark as Revise / Defend / Needs analysis; draft neutral responses | `sciwrite-publish` (responding to reviewers); R&R traceability matrix (comment → change → location) | Response letter and revised manuscript |

## 3. Quality and Integrity Controls

- **Citation checks:** each reference is verified against its DOI or publisher page by an author; reference-manager output is used for formatting.
- **Number checks:** every figure or statistic in the text is traced to a cited source.
- **Consistency checks:** the Abstract, contribution list, and Conclusion state the same claims. Script checks cover terms, acronyms, and numbers; their output is a list of candidates for the authors to judge, not automatic fixes (for example, passive voice can be acceptable in the methodology section).
- **Voice checks:** the authors rewrite AI-assisted passages so the final text reads in their own voice; raw AI output is not submitted.
- **Model use:** a mid-size model for routine drafting and editing; a stronger model for whole-manuscript consistency and multi-source synthesis; fast models only for mechanical formatting, never for citations.

## 4. How the Three Sources Divide the Work

| Source | Main role in this roadmap | What it does not cover |
|---|---|---|
| ProofreaderPro guide | Prompting techniques: framing, synthesis without added sources, section-by-section drafting, adversarial self-review | No automated checks or pipeline |
| Academic Research Skills (ARS) | Research pipeline: literature search, PRISMA, citation verification, integrity gates, simulated peer review | Sentence-level style; licensed CC BY-NC 4.0 (non-commercial use only) |
| Scientific Writing Skills (`sciwrite`) | Writing craft: process planning, section order and tense, prose editing, term/number consistency scripts, publication ethics | Does not verify citations or check plagiarism; does not judge scientific claims |

ARS checks that each citation exists and supports its claim. `sciwrite` checks that the text says it clearly and consistently. The two are complementary and are used at different stages.

## 5. Responsibilities

- **Authors:** research questions, source reading, taxonomy, interpretation, final wording, and all verification sign-offs.
- **AI tools:** structuring, first-pass drafting from author notes, consistency and integrity checks, simulated review.
- **Editing Staff (requested):** feedback on scope and section structure at Stage 0, and on the draft outline before Stage 4.

## 6. References for This Roadmap

- ProofreaderPro, "How to use Claude for research writing." https://proofreaderpro.ai/ko/blog/how-to-use-claude-for-research-writing
- PyTorch Korea User Group, "Academic Research Skills for Claude Code." https://discuss.pytorch.kr/t/academic-research-skills-claude-code/10385
- Academic Research Skills repository. https://github.com/Imbad0202/academic-research-skills
- D. Sosa, Scientific Writing Skills (based on K. Sainani, *Writing in the Sciences*, Stanford University). https://github.com/dvdsosa/scientific-writing-skills
