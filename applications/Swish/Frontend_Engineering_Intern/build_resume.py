"""Build the submission PDF from the repository's editable LaTeX source.

Usage: python build_resume.py
Requires reportlab. The small parser supports only this resume's known macros;
it fails on unknown commands rather than silently dropping resume content.
XeLaTeX remains an alternate build route for the .tex source.
"""
from pathlib import Path
import html
import re
from reportlab.pdfgen import canvas
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_CENTER
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.pagesizes import A4

ROOT = Path(__file__).resolve().parent

def group(s, pos):
    assert s[pos] == '{', s[pos:]
    start, level = pos + 1, 1
    pos += 1
    while level:
        if s[pos] == '{' and s[pos - 1] != '\\': level += 1
        if s[pos] == '}' and s[pos - 1] != '\\': level -= 1
        pos += 1
    return s[start:pos - 1], pos

def markup(s):
    out, i = '', 0
    while i < len(s):
        if s.startswith('\\href', i):
            url, j = group(s, i + 5)
            label, i = group(s, j)
            out += '<link href="' + html.escape(url, quote=True) + '">' + markup(label) + '</link>'
        elif s.startswith('\\textbf', i):
            value, i = group(s, i + 7)
            out += '<b>' + markup(value) + '</b>'
        elif s.startswith('\\textasciitilde', i):
            out += '~'; i += len('\\textasciitilde')
        elif s.startswith('\\par', i): i += 4
        elif s[i] == '\\' and s[i + 1:i + 2] in ('%', '&', '$', '_'):
            out += html.escape(s[i + 1]); i += 2
        elif s[i] == '\\': raise ValueError('Unknown command: ' + s[i:])
        elif s.startswith('--', i): out += '-'; i += 2
        else: out += html.escape(s[i]); i += 1
    return out

def build():
    fonts = Path('C:/Windows/Fonts')
    for face, file in [('Calibri', 'calibri.ttf'), ('Calibri-Bold', 'calibrib.ttf')]:
        pdfmetrics.registerFont(TTFont(face, str(fonts / file)))
    pdfmetrics.registerFontFamily('Calibri', normal='Calibri', bold='Calibri-Bold')
    body = ParagraphStyle('Body', fontName='Calibri', fontSize=10, leading=12, spaceAfter=0)
    center = ParagraphStyle('Contact', parent=body, fontSize=9, leading=11, alignment=TA_CENTER)
    heading = ParagraphStyle('Section', parent=body, fontName='Calibri-Bold', fontSize=10.6,
                             leading=12.6, spaceBefore=6, spaceAfter=3)
    entry = ParagraphStyle('Entry', parent=body, spaceBefore=2, keepWithNext=True)
    bullet = ParagraphStyle('Bullet', parent=body, leftIndent=11.5, firstLineIndent=-11.5)
    text = (ROOT / 'Aditya_Arnav_Swish.tex').read_text(encoding='utf-8')
    story = []
    # Header values are extracted from source, not separately maintained.
    header = text.split('\\resumesection{SUMMARY}')[0]
    for line in header.splitlines():
        if '\\fontsize{19bp}' in line or '\\fontsize{10.8bp}' in line:
            content = line.split('\\bfseries ', 1)[1].split('\\par', 1)[0]
            size = 19 if '19bp' in line else 10.8
            style = ParagraphStyle('Header', parent=center, fontName='Calibri-Bold',
                                   fontSize=size, leading=size + 3, spaceAfter=1)
            story.append(Paragraph(markup(content), style))
        elif '\\fontsize{9bp}' in line:
            content = line.split('\\selectfont ', 1)[1].split('\\par', 1)[0]
            story.append(Paragraph(markup(content), center))
    for line in ('\\resumesection{SUMMARY}' + text.split('\\resumesection{SUMMARY}', 1)[1]).splitlines():
        line = line.strip()
        if not line or line.startswith('%') or line == '\\end{document}': continue
        if line.startswith('\\resumesection'):
            value, _ = group(line, len('\\resumesection'))
            story.append(Paragraph(markup(value), heading))
        elif line.startswith(('\\entry', '\\nextentry')):
            prefix = '\\nextentry' if line.startswith('\\nextentry') else '\\entry'
            left, pos = group(line, len(prefix))
            right, _ = group(line, pos)
            # A single paragraph keeps ATS extraction in a natural reading order.
            suffix = ' | ' + markup(right) if right else ''
            story.append(Paragraph(markup(left) + suffix, entry))
        elif line.startswith('\\bulletitem'):
            value, _ = group(line, len('\\bulletitem'))
            story.append(Paragraph('- ' + markup(value), bullet))
        else: story.append(Paragraph(markup(line), body))
    target = ROOT / 'Aditya_Arnav_Swish.pdf'
    doc = SimpleDocTemplate(str(target), pagesize=A4, leftMargin=39.6, rightMargin=39.6,
                            topMargin=29, bottomMargin=29, title='Aditya Arnav Resume',
                            author='Aditya Arnav', subject='Swish Frontend Internship')
    doc.build(story)
    print(target)

if __name__ == '__main__': build()
