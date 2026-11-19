# Capgemini

Latest user update recorded: **2026-11-20T02:51:45+05:30** (Asia/Kolkata).

This is the processing time recorded for the latest user instructions; exact message receipt timestamps are unavailable.

## Roles — latest user update first

| Folder | Context | Latest user update recorded | Job description |
| --- | --- | --- | --- |
| [GenAI](GenAI/) | Supplied resume filename identifies GenAI; exact vacancy title not supplied | 2026-11-20T02:51:45+05:30 | Awaiting user |

## Files and references

- [LaTeX resume](GenAI/Aditya_Arnav_Capgemini.tex)
- [Compiled PDF resume](GenAI/Aditya_Arnav_Capgemini.pdf)
- [Compile entry point](GenAI/main.tex)
- [Job description status](GenAI/job-description.md)
- [Transcription notes](GenAI/tailoring-notes.md)
- [Links](links.md)
- [Important notes](notes.md)
- [Updates, newest first](updates.md)

## Build

From the `GenAI` folder, run:

```sh
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape Aditya_Arnav_Capgemini.tex
```

The named `.tex` file is self-contained. `main.tex` is an alternative entry point for project editors. Calibri matches the supplied resume; font fallbacks are provided for systems without Calibri. Fonts are not distributed here.
