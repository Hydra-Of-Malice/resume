# Aditya Arnav — Resume

One repository for the master resume and all company-specific, job-tailored versions.

## Companies — latest user update first

Times use Asia/Kolkata (UTC+05:30). Timestamps are recorded processing times when exact message receipt times are unavailable. File edits and commits do not change this order.

| Company | Latest user update recorded | Role / resume | Job description |
| --- | --- | --- | --- |
| [Cisco](applications/Cisco/README.md) | 2026-11-22 15:19:39 +05:30 | [Software Engineer 2025113](applications/Cisco/Software_Engineer_2025113/) | Official frontend / UX role; supplied application link preserved |
| [Commonwealth Bank of Australia (CBA)](applications/CBA/README.md) | 2026-11-20 03:17:26 +05:30 | [Campus graduate technology](applications/CBA/Campus_Graduate_Technology/) | Campus notice supplied; no specific JD |
| [Capgemini](applications/Capgemini/README.md) | 2026-11-20 02:51:45 +05:30 | [GenAI](applications/Capgemini/GenAI/) | Awaiting user |

Each company folder contains links, notes, and an update history. Each role folder contains resume sources and exports, tailoring notes, and the job descriptions supplied for that role. Future descriptions are preserved verbatim in timestamped files, with the latest linked from `job-description.md`.

## Naming convention

Use `Aditya_Arnav_<Company_Name>` for each tailored resume, with the appropriate extension:

- `Aditya_Arnav_Microsoft.pdf`
- `Aditya_Arnav_Microsoft.docx`
- `Aditya_Arnav_Microsoft.md`

Replace spaces with underscores in company names. Keep the same filename when revising a resume; Git records its history. For multiple roles at the same company, keep separate role folders so filenames remain consistent.

## Layout

```text
master/
  Aditya_Arnav_Master.<extension>
applications/
  <Company_Name>/
    <Job_Role>/
      job-description.md
      tailoring-notes.md
      Aditya_Arnav_<Company_Name>.<extension>
```

Keep the editable source and final export together in each role folder. The `master` folder holds the factual baseline; tailoring a company version does not replace it.

## Workflow

1. Add Aditya's current resume to `master/`.
2. Save the supplied job profile, company, role, and job link (if provided) in the relevant application folder.
3. Tailor the summary, skills, and experience emphasis using verified resume facts. Record material edits and any missing information in `tailoring-notes.md`.
4. Save the resume using the naming convention above and review the final export.
5. Commit each completed revision with a descriptive message, such as `resume(Microsoft): tailor for Software Engineer`.
6. Push the commits to the single GitHub repository named `resume` when authenticated access is available.

Use Git history for revisions rather than filenames such as `final_v2`. Keep the GitHub repository private by default because resumes may contain personal contact information.

## Current baseline

`master/Aditya_Arnav_Master.pdf` is an unchanged copy of the Capgemini PDF supplied by Aditya. It is the initial factual baseline, not a newly generalized resume. The Capgemini LaTeX version preserves its content without adding claims. The CBA variant adapts the summary, skills order and project order for a broad graduate technology application using the same factual baseline and documented official company research. A CBA campus notice has been supplied; no specific role JD or portfolio website has been provided.

The Cisco variant targets Software Engineer requisition 2025113 using the live official description, emphasizing React/JavaScript delivery, debugging, CI/CD and security/evaluation projects while retaining Zapper Edge AI and document-intelligence experience. It does not add unverified Figma skills or claim 2027 graduation eligibility.
