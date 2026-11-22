# Rezerv AI Engineer application guide

Research checked 22 November 2026. The application is prepared, not sent. The public hiring post is discoverable, but no employer confirmation establishes that the vacancy is still open.

## Application route and eligibility

The [AI Engineer hiring post](https://www.linkedin.com/posts/ngarte_were-hiring-an-ai-engineer-remote-position-activity-7492366264531615745-Vj0D) requests a CV and a brief account of an agent system delivered, emailed to **careers@rezerv.co**. It describes Myanmar-based remote work and at least two years of engineering. Your baseline lists Bengaluru and a B.Tech ending in 2027; the dated employment record does not establish two years. These are material screening gaps, regardless of resume formatting. The prepared email asks whether India-based applications are considered without pretending eligibility is confirmed.

Send the one-page `Aditya_Arnav_Rezerv.pdf` and the body in `application-email.txt`. Confirm the location and employment/education details are still current, and add your actual availability if requested. Do not invent a start date, notice period, salary expectation, nationality or work authorization. If the recruiter confirms Myanmar-only hiring, ask whether future India-eligible roles may be considered.

Use one short email. The project paragraph supplies the requested evidence; a second cover-letter attachment adds little. A brief follow-up after five to seven business days is reasonable if there is no response. Do not send repeated messages to multiple staff members or apply through customer support channels. A message has not been sent on your behalf.

## What to emphasize

The [role post](https://www.linkedin.com/posts/ngarte_were-hiring-an-ai-engineer-remote-position-activity-7492366264531615745-Vj0D) makes agents and MCP central. Lead with a published MCP tool integration, production LLM delivery, and concrete evaluation work. Kavach supports a discussion about controlling actions and auditing tool calls; its hackathon evaluation is not evidence of production-wide security guarantees. Your strongest professional proof is Zapper's deployed pipeline and measured processing improvement.

Rezerv's [product site](https://www.rezerv.co/) covers bookings, payments, memberships and studio operations. Its [release notes](https://www.rezerv.co/blogs/rezerv-feature-release-notes) document an AI analytics feature. ORQUIS supplies a relevant example of grounding business answers in calculated metrics, although it remains in progress. This relevance is an assessment, not prior employment in fitness SaaS.

## Honest fit assessment

| Role signal | Evidence used | Limit |
| --- | --- | --- |
| Production LLM delivery | Zapper meeting intelligence, Azure OpenAI, async pipeline | Python/FastAPI experience does not establish production Node.js ownership |
| MCP and agent tools | Published ChatGPT-SketchUp bridge, 18 tools, installer and docs | Do not claim customer counts or adoption |
| Agent controls and evals | Kavach policy/reviewer/approval flow; 51 scenarios | Hackathon project; attack-result claim is limited to the scripted test agent |
| Grounded assistants | AI Teacher citation-based retrieval; ORQUIS KPI grounding | ORQUIS is still being built |
| Latency and cost | Defect Forge per-call logs and approximate per-sample cost | No token-saving percentage or production LLM latency claim is established |
| TypeScript and Node.js | Explicit skills in the master resume | The baseline does not demonstrate strong production Node.js delivery |
| 2+ years engineering | Internships and current AI role retain actual dates | Requirement not established; do not total overlapping roles as separate years |
| Remote from Myanmar | Candidate location remains Bengaluru, India | Eligibility requires employer clarification |

## Links to include

Use the [portfolio](https://www.adityaarnav.site/), [LinkedIn](https://www.linkedin.com/in/aditya-arnav-76a0222a1), [GitHub profile](https://github.com/Hydra-Of-Malice) and [MCP project](https://github.com/Hydra-Of-Malice/SketchUp-2022-ChatGPT-MCP). These were checked against the baseline and public profile/repositories. The resume includes all three profile links and embedded project links.

Keep the private resume-repository URL out of recruiter-facing correspondence; attach the PDF directly. The [Defect Forge demo](https://defect-forge-kappa.vercel.app) is a recorded replay according to its [README](https://github.com/Hydra-Of-Malice/defect_forge); do not introduce it as a live inference service. No public Kavach URL was verified, so none was invented.

## ATS readiness

This resume uses one column, selectable text, conventional section headings, explicit dates, visible contact information, and relevant terms supported by the factual baseline. A plain-text export is included for extraction review. No external scoring service received your resume, and no numerical ATS score or guaranteed ranking is claimed. Keyword coverage cannot resolve location, tenure or demonstrable Node.js depth.

## Preparing for the technical conversation

Be ready to walk through one real tool invocation from request to execution and result, explain how failures/retries are handled in your actual implementation, and distinguish shipped production work from hackathon projects. Prepare examples of the evaluation cases and measurements already documented in your repos.

For Rezerv, a useful design discussion would consider tenant-scoped data access, read versus write permissions, approval before consequential changes, duplicate-booking prevention, human escalation, and response-time/cost measurements. These are proposed interview topics, not claims that you already implemented Rezerv's architecture. Likewise, WhatsApp integration and studio booking/payment agents are employer goals, not candidate accomplishments.

## Evidence sources

- User-provided master: `master/Aditya_Arnav_Master.pdf` and its faithful Capgemini LaTeX transcription.
- User-provided recruiter screenshot: preserved under `job-descriptions/` with a visible-text transcription.
- [AI Engineer post by Adrian Ng](https://www.linkedin.com/posts/ngarte_were-hiring-an-ai-engineer-remote-position-activity-7492366264531615745-Vj0D): role scope, engineering expectations, location and email route. Exact opening date and continued vacancy status not confirmed.
- [Rezerv product site](https://www.rezerv.co/): company and product context. Search results for the insurance company Reserv at reserv.com were excluded.
- [Rezerv release notes](https://www.rezerv.co/blogs/rezerv-feature-release-notes): published AI feature context.
- [Candidate portfolio](https://www.adityaarnav.site/) and [LinkedIn](https://www.linkedin.com/in/aditya-arnav-76a0222a1): identity and professional links. The portfolio's broader patent-status and Zapper-title wording differs from the master; the resume retains the master's employment history and omits patents for role relevance.
- [MCP bridge README](https://github.com/Hydra-Of-Malice/SketchUp-2022-ChatGPT-MCP): published integration, 18 tools, installer and documentation. This is repository documentation, not independently measured adoption.
- [Defect Forge README](https://github.com/Hydra-Of-Malice/defect_forge): evaluation transparency, model-call latency/cost logs, and replay-demo limit.
