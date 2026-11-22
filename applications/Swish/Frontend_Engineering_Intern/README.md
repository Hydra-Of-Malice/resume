# Swish internship resume

Upload [Aditya_Arnav_Swish.pdf](Aditya_Arnav_Swish.pdf). The candidate headline is AI Engineer with React applications and workflow automation; the supplied opening is an in-office frontend internship.

- [Editable LaTeX](Aditya_Arnav_Swish.tex)
- [Extracted text](Aditya_Arnav_Swish.txt)
- [Application pitch with full and short versions](application-pitch.txt)
- [Supplied job evidence](job-description.md)
- [Tailoring notes](tailoring-notes.md)

Build the verified PDF with `python build_resume.py`, which runs XeLaTeX twice with shell escape disabled and copies the compiled PDF to the stable filename. MiKTeX or TeX Live is required. The source controls typography, horizontal section dividers, hanging bullets and right-aligned dates directly; there is no separate layout conversion. The builder rejects horizontal or vertical overflow warnings. Re-render and inspect the PDF after changes; previews belong in ignored `build/`.
