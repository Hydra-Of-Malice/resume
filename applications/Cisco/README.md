# Cisco

Latest application-content update recorded: **2026-11-22T15:19:39+05:30**, Asia/Kolkata. This is processing time; exact message receipt time was unavailable.

| Role | Latest update recorded | Resume | Job description |
| --- | --- | --- | --- |
| Software Engineer 2025113 | 2026-11-22T15:19:39+05:30 | [PDF](Software_Engineer_2025113/Aditya_Arnav_Cisco.pdf) / [LaTeX](Software_Engineer_2025113/Aditya_Arnav_Cisco.tex) | [Supplied link and retrieved summary](Software_Engineer_2025113/job-description.md) |

- [Application notes and open questions](notes.md)
- [Official links](links.md)
- [Tailoring rationale and verification](Software_Engineer_2025113/tailoring-notes.md)
- [Update history](updates.md)

Build from `Software_Engineer_2025113`:

```sh
mkdir -p build
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=build Aditya_Arnav_Cisco.tex
xelatex -interaction=nonstopmode -halt-on-error -no-shell-escape -output-directory=build Aditya_Arnav_Cisco.tex
cp build/Aditya_Arnav_Cisco.pdf Aditya_Arnav_Cisco.pdf
```

On PowerShell, use `New-Item -ItemType Directory -Force build` and `Copy-Item build/Aditya_Arnav_Cisco.pdf Aditya_Arnav_Cisco.pdf` for the first/last steps. `main.tex` is an alternate editor entry point. The source uses Calibri, with Carlito and TeX Gyre Heros fallbacks. Temporary compilation and preview files stay in ignored `build/`.
