"""Compile the LaTeX layout, including rules, bullets and date alignment.

Usage: python build_resume.py
Requires XeLaTeX (MiKTeX or TeX Live). Build files stay in ignored build/.
"""
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parent

def build():
    engine = shutil.which('xelatex')
    if not engine:
        raise SystemExit('XeLaTeX is required to preserve the resume layout. Install MiKTeX or TeX Live.')
    build_dir = ROOT / 'build'
    build_dir.mkdir(exist_ok=True)
    source = ROOT / 'Aditya_Arnav_Swish.tex'
    command = [engine, '-no-shell-escape', '-interaction=nonstopmode',
               '-halt-on-error', '-output-directory=build', source.name]
    for _ in range(2):
        result = subprocess.run(command, cwd=ROOT, capture_output=True, text=True)
        if result.returncode:
            raise SystemExit(result.stdout + result.stderr)
    log = (build_dir / 'Aditya_Arnav_Swish.log').read_text(encoding='utf-8', errors='replace')
    if 'Overfull \\hbox' in log or 'Overfull \\vbox' in log:
        raise SystemExit('Layout overflow detected. Inspect build/Aditya_Arnav_Swish.log.')
    target = source.with_suffix('.pdf')
    shutil.copyfile(build_dir / target.name, target)
    print(target)

if __name__ == '__main__':
    build()
