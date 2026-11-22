# Proposed Manuscript Development Roadmap (Conditional on Proposal Acceptance)

> Status: DRAFT. Prepared for the TIIS Editing Staff together with the survey proposal.
> This roadmap applies only after the proposal is accepted. It describes how the authors will
> write the full survey with AI assistance while keeping the authors responsible for every claim and citation.

## 1. Principles

- **AI is a copilot, not the pilot.** The authors set the research questions, the taxonomy, and the conclusions. AI tools help with structuring, drafting, consistency checks, and citation verification.
- **No source the authors have not read.** Every reference enters the corpus only after an author has read it. AI may synthesize the authors' notes but may not add sources (`Do not add any sources I haven't provided`).
- **Gaps are marked, not filled.** Where evidence is missing, the draft carries a `[MATERIAL GAP]` marker instead of invented text.
- **Continuity with TIIS-S1-2025-Nov-1354.R1.** The new survey is framed as a follow-up of the authors' earlier TIIS survey. That paper is cited in the Introduction, revisited in the Conclusion, and listed in the References.
- **Transparent disclosure.** AI use is disclosed in the manuscript according to the TIIS and KSII policy in force at submission.

## 2. Stage-by-Stage Roadmap

| Stage | Weeks | Main activity | Tools / technique | Output (gate to next stage) |
|---|---|---|---|---|
| 0. Kick-off | W1 | Fix scope, research questions, and inclusion criteria from the accepted proposal; incorporate Editing Staff comments | Socratic planning (`/ars-plan`) | Scope memo, RQ list, author checkpoint |
| 1. Framing | W1 | Rank 3 candidate framings by novelty and defensibility; list the strongest counter-argument to each | Adversarial framing prompt | Final framing and contribution statement |
| 2. Literature corpus | W2-W3 | Systematic search and screening; authors read sources and take structured notes | PRISMA flow; Zotero; `/ars-lit-review` only to find gaps in the authors' corpus | PRISMA diagram, annotated corpus, Material Passport (corpus + provenance) |
| 2.5 Integrity gate I | W3 | Check every candidate citation for existence and metadata | DOI resolution; Semantic Scholar matching; hallucinated-citation check | Verified bibliography (zero unverified items) |
| 3. Taxonomy and synthesis | W3-W4 | Build the taxonomy; write thematic synthesis, disagreements, and open questions with (Author, Year) tags | Synthesis from author notes only | Taxonomy figure, comparison tables |
| 4. Section drafting | W4-W6 | Draft one section at a time (about 800-1,000 words per pass), each reviewed before the next | Paragraph-level outlines with purpose and evidence; TIIS template; style calibration on the authors' prior papers (incl. 1354.R1) | Full first draft in TIIS template |
| 4.5 Integrity gate II | W6 | Zero-tolerance re-check: fabricated citations, unsupported claims, numbers not in the sources, early frame-lock | Claim-to-source audit; figure checklist | Integrity report signed off by authors |
| 5. Internal review | W7 | Simulated peer review (editor + methodology, domain, cross-disciplinary reviewers + devil's advocate); logic-flow and abstract/conclusion consistency checks | Academic Paper Reviewer (0-100 rubric) | Prioritized revision list (top weaknesses by severity) |
| 6. Revision and language | W7-W8 | Revise; tighten wording without losing claims, numbers, or citations; human proofreading | Tracked changes; professional proofreading; reference manager formatting (TIIS style) | Camera-ready candidate |
| 7. Submission | W8 | AI-use disclosure, cover letter, final format check | TIIS submission checklist | Submitted manuscript |
| 8. Reviewer response | After review | Extract each reviewer comment; mark as Revise / Defend / Needs analysis; draft neutral responses | R&R traceability matrix (comment → change → location) | Response letter and revised manuscript |

## 3. Quality and Integrity Controls

- **Citation checks:** each reference is verified against its DOI or publisher page by an author; reference-manager output is used for formatting.
- **Number checks:** every figure or statistic in the text is traced to a cited source.
- **Consistency checks:** the Abstract, contribution list, and Conclusion state the same claims.
- **Voice checks:** the authors rewrite AI-assisted passages so the final text reads in their own voice; raw AI output is not submitted.
- **Model use:** a mid-size model for routine drafting and editing; a stronger model for whole-manuscript consistency and multi-source synthesis; fast models only for mechanical formatting, never for citations.

## 4. Responsibilities

- **Authors:** research questions, source reading, taxonomy, interpretation, final wording, and all verification sign-offs.
- **AI tools:** structuring, first-pass drafting from author notes, consistency and integrity checks, simulated review.
- **Editing Staff (requested):** feedback on scope and section structure at Stage 0, and on the draft outline before Stage 4.

## 5. References for This Roadmap

- ProofreaderPro, "How to use Claude for research writing." https://proofreaderpro.ai/ko/blog/how-to-use-claude-for-research-writing
- PyTorch Korea User Group, "Academic Research Skills for Claude Code." https://discuss.pytorch.kr/t/academic-research-skills-claude-code/10385
- Academic Research Skills repository. https://github.com/Imbad0202/academic-research-skills
