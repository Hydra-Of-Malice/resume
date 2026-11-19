# Resume workspace instructions

- This workspace belongs to Aditya Arnav and maintains all resume variants in one GitHub repository named `resume`.
- Name every company-specific resume `Aditya_Arnav_<Company_Name>.<extension>`. Use underscores for spaces in company names.
- Store the factual master resume under `master/`. Store company variants under `applications/<Company_Name>/<Job_Role>/`.
- Separate roles at the same company into role folders while preserving the requested resume filename.
- When a job profile is provided, save its supplied text and available company, role, and URL in that role folder before tailoring.
- Use the master resume and user-confirmed information as the factual basis. Do not invent skills, employment, dates, qualifications, achievements, or metrics.
- Tailor relevant wording, section order, summary, and emphasis to the supplied role. Preserve accurate meaning.
- Keep the editable resume source, any final exports, and concise tailoring notes together. Follow the relevant document or PDF skill for exported documents and verify their layout.
- Preserve the master resume unless the user asks to update it or supplies new factual information for it.
- Track completed revisions with descriptive Git commits. Keep stable filenames and use Git history for prior versions.
- Push completed updates to the configured GitHub remote when access is available. Do not create a separate repository for each company.
- Keep the repository private by default. Do not commit credentials, tokens, or temporary render files.
- If remote access is unavailable, complete and commit the local work and clearly report the remaining synchronization step.
- Keep every company separate, with role folders below it. Maintain company-level links, important notes, and an update history.
- Preserve each job description the user supplies verbatim in a timestamped file under the role's `job-descriptions/` folder. Keep `job-description.md` pointing to the latest supplied description. Do not infer a description from a resume or invent one when none was supplied.
- Record user-update timestamps in ISO 8601 with offset +05:30 (Asia/Kolkata). If an exact message timestamp is unavailable, label the timestamp as the time the update was recorded rather than claiming an exact receipt time.
- Keep the company index in the root README sorted by latest user update, newest first. Move a company to the top whenever the user supplies a new job description, link, resume, or other application update for it. Also order role indexes and update histories newest first. Compilation, commits, or unrelated maintenance must not change a company's recency.
- Preserve supplied facts exactly for transcription requests. For future tailoring, the user permits relevant factual information from their supplied GitHub profile and portfolio; record the supporting URLs and access dates. Never invent claims or metrics, and do not add new content during the current Capgemini transcription.
