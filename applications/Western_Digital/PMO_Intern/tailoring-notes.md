# Western Digital PMO tailoring notes

## Repository and factual basis

The repository was audited before this variant was authored. `AGENTS.md` requires company/role folders, stable filenames, preserved job evidence, factual tailoring, editable sources, verified exports, update histories and descriptive commits. The master PDF and its faithful Capgemini transcription remain unchanged. Existing Swish and Rox layout fixes were used as the visual authority: one column, section rules, hanging bullets and right-aligned dates.

Employment, dates, education, skills and metrics are taken from the factual master and existing variants. The candidate's portfolio, GitHub and LinkedIn URLs were already verified in the repository's prior work. No PMO title, budget ownership, tool proficiency or project-management credential was invented.

## Tailoring decisions

- Headline: `AI Engineer | Project Delivery and Technical Operations`, so the candidate's current title remains accurate while the resume speaks to PMO work.
- Summary translates AI/backend delivery into PMO-relevant evidence: workflow design, implementation, validation, documentation, operational handoff, issue triage and measurable delivery outcomes.
- Skills prioritize Agile, SDLC, technical documentation, quality gates, issue triage, data reporting and Excel/CSV analysis. The employer's desired MS Project, Visio, Smartsheet and Jira tools are omitted because the baseline does not verify them.
- Zapper bullets emphasize end-to-end ownership, workflow stages, operational checks, reliability, concurrent delivery and human-review routing.
- BlankSage emphasizes user-facing delivery, issue resolution and CI/CD; E Soft demonstrates workflow automation.
- Projects emphasize ORQUIS for Excel/CSV/KPI reporting, Defect Forge for quality gates and cost/latency logs, Kavach for approvals/auditability, and AI Teacher for structured document/retrieval evaluation.
- Omit patents, computer-vision details, school marks and hackathon/open-source lists to keep this one-page PMO resume readable. They remain in the master and other variants.

## Limits

The PMO listing was a third-party copy marked expired. The official Western Digital pages confirm the application route and student eligibility guidance but do not expose a live PMO requisition in the pages checked. The role asks for office/productivity tools that are not verified in the baseline. The candidate's exact internship availability and term remaining after the program must be confirmed before submission.

## Verification

The resume is compiled directly from LaTeX with XeLaTeX through `build_resume.py`, twice, with shell escape disabled. The builder rejects overflow warnings. The final PDF is one A4 page with five section dividers, selectable text, aligned dates, profile/project links and no replacement characters. The text export is extracted from the final PDF. Rendered PNGs and logs remain in ignored `build/`.
