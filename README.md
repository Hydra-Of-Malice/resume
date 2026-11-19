# Aditya Arnav — Resume

One repository for the master resume and all company-specific, job-tailored versions.

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

## Initial status

The repository structure is ready. A master resume and the first job profile are needed before a tailored resume can be created.
