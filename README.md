# KSII-TIIS-2027

This repository holds the working files for a follow-up survey proposal to **KSII Transactions on Internet and Information Systems (TIIS)**.

> **Internet-Connected Generative AI for Human Making in Craft: A Critical Review of In-Process Feedback and Learning**
> JooHyun Lee (Yonsei University) and Junheon Lee (KB Securities)

The proposal follows up our previous TIIS survey, *Generative AI Features and Limitations in Support of Inclusive XR Immersive Learning Environments for Aging and Creative Community Applications* (TIIS-S1-2025-Nov-1354.R1; vol. 20, no. 4, 2026; [doi:10.3837/tiis.2026.04.027](http://doi.org/10.3837/tiis.2026.04.027)). It takes the earlier survey's questions about multimodal alignment, feedback reliability, and learning evaluation and applies them to physical craft making.

## Status

| Item | Status |
|---|---|
| Proposal slides | Discussed with Dr. JooHyun Lee |
| Proposal draft (TIIS template) | Draft, 2026-11-22. Open items are highlighted as `[TBD]` |
| Writing roadmap | Revised draft, to be applied only if the proposal is accepted |
| Review request to the Editing Staff | Email draft, not sent |

## Research Questions

- **RQ1. Observation and representation.** How does AI observe and represent making actions, material states, and maker intent?
- **RQ2. Feedback and judgment.** What supports AI advice, and how does the maker decide to change, preserve, or extend a variation?
- **RQ3. Performance and learning.** What changes in independent understanding, judgment, or skill do studies test after AI support?

## Repository Layout

```
proposal/
  TIIS_Craft_GenAI_Proposal_Draft.docx    Proposal draft in the TIIS Word template (14 pages)
  TIIS_Craft_GenAI_Proposal_Slides.html   Original proposal slides (source of the draft)
docs/
  writing-roadmap-for-editing-staff.md    Stage-by-stage writing roadmap (also the Attachment of the draft)
  email/editing-staff-review-request.md   Review request email draft (English and Korean)
figures/
  fig1_analytical_frame.png               Fig. 1: analytical frame (RQ1-RQ3)
data/
  seed_dois.txt                           DOIs of the 30 seed studies (R01-R30)
  crossref_check.json                     Crossref metadata used for the reference list
tools/
  build_proposal_docx.py                  Builds the .docx on top of the TIIS template package
  draw_fig1.py                            Draws Fig. 1
  check_dois.py                           Looks up DOIs in Crossref
```

## Proposal Draft Notes

- **Template:** The draft follows `TIIS_Template_final_2020.docx` and keeps the template's own styles. The template itself is not redistributed in this repository.
- **Citations:** Reference formatting follows `TIIS_Template_final_2020_References.docx`. Citations are numbered in order of first appearance, and every reference carries an `Article (CrossRef Link)`.
- **Follow-up framing:** The draft identifies the paper as a follow-up to 1354.R1 in three places: Introduction (Section 1.2 and Table 1), Conclusion (Section 6), and References ([6]).
- **Reference checks:**
  - All 30 seed references were checked by DOI on 2026-11-22: 29 in Crossref and R12 in JaLC (`10.20668/adada.29.2_45`).
  - Four references still need final volume or page data before submission: R09, R10, R23, and R29 (pages).
- **Open items (`[TBD]`):** author order and corresponding author, funding, search period and query strings, final corpus size, schedule, and the AI-use disclosure statement.

## Rebuilding the Draft

```bash
# 1) unzip your own copy of the TIIS template
python -c "import zipfile; zipfile.ZipFile('TIIS_Template_final_2020.docx').extractall('tpl')"
# 2) draw the figure and build the document
python tools/draw_fig1.py
python tools/build_proposal_docx.py tpl fig1.png TIIS_Craft_GenAI_Proposal_Draft.docx
```

All proposal text and reference metadata are in `tools/build_proposal_docx.py`. Edit that file and rebuild, or edit the `.docx` directly.

## Writing Principles

The full survey will be written with AI assistance under author control. See [docs/writing-roadmap-for-editing-staff.md](docs/writing-roadmap-for-editing-staff.md).

- No source enters the corpus unless an author has read it.
- Gaps are marked, not filled.
- Every citation and number is verified before submission.
- AI use is disclosed according to TIIS policy.
