# Rezerv AI Engineer tailoring notes

## Factual basis

The master PDF and its unchanged transcription at `applications/Capgemini/GenAI/Aditya_Arnav_Capgemini.tex` supply employment, dates, education, skills and metrics. The original master and other company variants are unchanged.

The verified portfolio URL, https://www.adityaarnav.site/, matches the baseline name, email, education, GitHub and LinkedIn identity. Supporting public repositories were read through GitHub on 22 November 2026. The MCP bridge README documents 18 modeling tools, Windows packaging and user/developer documentation; these specifics extend the master's existing published-bridge claim. This is not a claim of measured adoption or enterprise deployment. Relevant URLs are in `../links.md` and `application-guide.md`.

## Tailoring decisions

- Headline and summary focus on agentic AI, Model Context Protocol and production LLM systems.
- Preserve exact employment dates and the 2027 graduation year; do not claim two years of engineering or full-time availability.
- Bring TypeScript and Node.js forward in the skills section without rewriting Python employment as Node.js experience.
- Lead experience with production delivery and measured reliability, processing overhead, concurrent sessions and human review.
- Choose Kavach for tool-call controls and evaluations; retain its scripted-agent qualifier rather than presenting a 0% attack rate as a general security guarantee.
- Expand the published MCP bridge and provide a direct project link. Include citation-grounded AI Teacher, Defect Forge latency/cost logs, and in-progress ORQUIS for business-data grounding.
- Omit schooling, the less relevant computer-vision project, patents and hackathon participation lists to leave room for practical role evidence.
- Retain Bengaluru, India. The application email explicitly asks whether applicants outside Myanmar are considered.
- No WhatsApp/Meta Business integration, studio booking automation, payment-gateway experience, new framework, token-saving metric or agent customer count is claimed.
- No ATS score is invented. The result targets supported job terminology and straightforward extraction; location, tenure and production Node.js depth remain gaps.

## Build and verification

The editable `.tex` file follows the repository's LaTeX convention. Local XeLaTeX could not initialize because its registry/configuration paths were inaccessible in the sandbox. The delivered PDF was therefore generated from that same `.tex` content using `build_resume.py` and bundled Python/ReportLab. Its small parser recognizes the resume's commands and fails on unknown commands. It produces a one-column layout with dates inline for natural text extraction. XeLaTeX is an alternate source build, but that alternate layout was not compiled or verified here.

The final PDF is one A4 page with embedded Calibri fonts. Verification covers all-page visual inspection, selectable text, reading order, expected role/education dates and baseline metrics, and actual PDF link annotations for email, portfolio, LinkedIn, GitHub and the two linked projects. `Aditya_Arnav_Rezerv.txt` is extracted from the final PDF. Intermediate PNGs and logs stay in ignored `build/`.

Application materials are drafts. No email, LinkedIn message or job application has been sent.
