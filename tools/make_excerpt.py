#!/usr/bin/env python3
import os, re, shutil, io, contextlib

NS = {'__name__': '__excerpt__'}
src = open('/home/claude/build28.py', encoding='utf-8').read()
src = src.replace("OUT = '/home/claude/build28'", "OUT = '/home/claude/.excerpt_tmp'")
with contextlib.redirect_stdout(io.StringIO()):
    exec(compile(src, 'build28.py', 'exec'), NS)

PRE = NS['PRE']; emit_interlude = NS['emit_interlude']; INTER = NS['INTERLUDES']
_PICRE, _picsub, inline = NS['_PICRE'], NS['_picsub'], NS['inline']

TITLE = 'Мост, который не построили'
it = next(x for x in INTER if x['title'] == TITLE)

OUT = '/home/claude/excerpt'
os.makedirs(OUT, exist_ok=True)
for d in ('fonts', 'img'):
    shutil.copytree('/home/claude/build28/' + d, os.path.join(OUT, d), dirs_exist_ok=True)

URL = 'https://github.com/sociocyber1/Latex_ScienceBook_Detective-Alex-Merser-Map-is-not-Territory'
RAW = URL + '/raw/main/releases_ru/karta-ne-est-territoriya-last_version.pdf'

COVER = r'''
\begin{document}
\frontmatter
\newgeometry{margin=14mm}
\thispagestyle{empty}
\pagecolor{coverbg}\color{coverfg}
\begin{tikzpicture}[remember picture,overlay]
  \draw[accent,line width=0.7pt] ($(current page.north west)+(9mm,-9mm)$) rectangle ($(current page.south east)+(-9mm,9mm)$);
  \draw[accent!65,line width=0.25pt] ($(current page.north west)+(11.4mm,-11.4mm)$) rectangle ($(current page.south east)+(-11.4mm,11.4mm)$);
\end{tikzpicture}
\begin{center}
\vspace*{0.16\textheight}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=44}\textcolor{accent}{ОТДЕЛЬНАЯ ГЛАВА ИЗ КНИГИ}\par}
\vspace{6mm}
{\disp\fontsize{10}{13}\selectfont КАРТА НЕ ЕСТЬ ТЕРРИТОРИЯ\par}
\vspace{10mm}
{\color{accent}\rule{30mm}{0.6pt}}\par
\vspace{10mm}
{\disp\blackface\fontsize{25}{29}\selectfont МОСТ,\\КОТОРЫЙ\\НЕ ПОСТРОИЛИ\par}
\vspace{9mm}
{\color{accent}\rule{30mm}{0.6pt}}\par
\vspace{9mm}
{\disp\fontsize{9}{13}\selectfont\addfontfeature{LetterSpace=10}Разбор одной ссоры по методу\\общей семантики\par}
\vfill
{\disp\fontsize{12}{15}\selectfont\addfontfeature{LetterSpace=26}ALEX MERSER\par}
\vspace{2.5mm}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=28}\textcolor{accent}{АЛЕКС МЕРСЕР}\par}
\vspace{8mm}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=26}\textcolor{accent}{SocioCyberneering Inc.}\par}
\vspace{4mm}
\end{center}
\clearpage
\nopagecolor\color{black}\restoregeometry
\thispagestyle{empty}
\vspace*{0.12\textheight}
\begin{notebox}{Что это за текст}
\small Это одна глава из научно-нуарного детектива «Карта не есть территория» ---
истории о сыщике Алексе Мерсере, который полгода считал виновным не того человека и
из-за этого пошёл учиться оценивать заново, на семинары Альфреда Коржибски по общей
семантике (колледж Оливет, 1937).

Глава читается отдельно: знать сюжет для неё не нужно.

Разбирается в ней не выдуманное дело, а настоящая ссора --- та, из-за которой
несколько человек, делавших редкую и нужную работу, перестали разговаривать друг с
другом. Имён в разборе нет, и это не вежливость: материал на руках --- пересказ
пересказа, а называть фамилии по такой бумаге значит повторять ровно ту ошибку,
о которой написана книга.
\end{notebox}

\vspace{4mm}
\begin{center}
{\disp\fontsize{8}{11}\selectfont\addfontfeature{LetterSpace=18}\textcolor{accent}{ВСЯ КНИГА --- 1220 СТРАНИЦ, БЕСПЛАТНО}\par}
\vspace{3mm}
\href{%s}{\resizebox{0.99\linewidth}{!}{github.com/sociocyber1/Latex\_ScienceBook\_Detective-Alex-Merser-Map-is-not-Territory}}
\end{center}

\vfill
\begin{center}
{\footnotesize Текст и иллюстрации --- CC~BY-SA~4.0. Копируйте, печатайте, пересылайте, переделывайте.\\
Три просьбы: укажите авторство, оставьте открытым и напишите, что изменили.\par}
\end{center}
\clearpage
\mainmatter
''' % URL

TAIL = r'''
\clearpage
\thispagestyle{empty}
\vspace*{0.2\textheight}
\begin{center}
{\disp\bfseries\fontsize{14}{18}\selectfont Это была одна глава\par}
\vspace{3mm}
{\color{accent}\rule{17mm}{0.6pt}}\par
\vspace{6mm}
{\itshape В книге их ещё пятьдесят с лишним, и почти все --- про то же самое:\\
как человек путает карту с территорией и сколько это стоит.\par}
\vspace{9mm}
{\disp\fontsize{8}{11}\selectfont\addfontfeature{LetterSpace=18}\textcolor{accent}{СКАЧАТЬ ЦЕЛИКОМ}\par}
\vspace{3mm}
{\small\href{%s}{karta-ne-est-territoriya-last\_version.pdf}\par}
\vspace{3mm}
\href{%s}{\resizebox{0.99\linewidth}{!}{github.com/sociocyber1/Latex\_ScienceBook\_Detective-Alex-Merser-Map-is-not-Territory}}
\vfill
{\footnotesize Нашли ошибку, знаете, как было на самом деле, хотите поспорить ---\\
пишите: sociocyber1@gmail.com\par}
\vspace{4mm}
{\disp\fontsize{9}{12}\selectfont\addfontfeature{LetterSpace=16}SocioCyberneering Inc.\par}
\vspace{2mm}
{\itshape\small Все права розданы.\par}
\vspace{8mm}
\end{center}
\end{document}
''' % (RAW, URL)

body = _PICRE.sub(_picsub, emit_interlude(it, 0))
body = body.replace('\\storypart{', '\\storypartX{', 1)
body = re.sub(r'Интермедия \d+', 'Интермедия 51', body, count=2)
PRE2 = PRE + r'''
\newcommand{\storypartX}[3]{\thispagestyle{plain}\phantomsection\vspace*{0.02\textheight}%
  \begin{center}{\disp\fontsize{8.4}{10}\selectfont\addfontfeature{LetterSpace=42}\MakeUppercase{#1}}\partrule
  {\disp\bfseries\fontsize{15.5}{18.5}\selectfont #2\par}\end{center}\storypartclose}
'''
tex = PRE2 + COVER + body + TAIL
open(os.path.join(OUT, 'most-kotoryy-ne-postroili.tex'), 'w', encoding='utf-8').write(tex)
print('written', len(tex))
