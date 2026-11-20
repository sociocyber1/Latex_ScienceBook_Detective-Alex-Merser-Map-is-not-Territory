#!/usr/bin/env python3
import re, sys, os, shutil

SRC = '/mnt/user-data/uploads/Merser.txt'
OUT = '/home/claude/build28'
os.makedirs(OUT, exist_ok=True)
if os.path.isdir('/home/claude/img'):
    shutil.copytree('/home/claude/img', os.path.join(OUT,'img'), dirs_exist_ok=True)

L = open(SRC, encoding='utf-8').read().split('\n')
N = len(L)

# ---- ending moved indoors (кабинет Грея), по просьбе автора ----
def _patch_ending():
    try:
        a = L.index('Мерсер вышел из здания один.')
        b = L.index('И было событие, которое не исчезало оттого, что кому-то хотелось назвать его иначе.')
    except ValueError:
        return
    NEW = """Мерсер не ушёл.

Он поднялся на второй этаж, в библиотечное крыло, и остановился перед дверью с табличкой, на которой не было ни должности, ни звания --- только фамилия.

В кармане у него лежала старая карта города, на которой некоторые улицы всё ещё назывались по-старому.

Он вспомнил фразу Томаса:

*«Запись --- не событие».*

Потом постучал и вошёл.

Кабинет был тот самый. Книжные полки до потолка, жалюзи на окне, узкая полоса света на полу. Стол, на котором месяц назад лежала коробка с бумагами Томаса, и стопка книг с краю, сдвинутая так, будто её часто перекладывали.

Мерсер не закрыл за собой дверь.

Это было не рассеянностью. После февраля он завёл себе правило и записал его в блокнот: с человеком, который проходит по делу, не разговаривать за закрытой дверью. Разговор за закрытой дверью существует только в двух пересказах, и оба пересказа принадлежат участникам. Хейл называл это занудством. Мерсер называл это протоколом.

В приёмной за дверью печатала мисс Уоррен. В коридоре, у лестницы, курил сержант и ждал Хейл --- Мерсер попросил их подняться вместе с ним и остаться снаружи.

Грей поднял голову от бумаг.

— Вы могли бы уехать, --- сказал священник.

— А вы могли бы рассказать правду.

— Вы всё ещё думаете, что правда обязательно победит?

— Нет. Я думаю, что она существует независимо от того, победит ли.

Грей медленно поднялся из-за стола.

— Вы разрушили жизни людей своими подозрениями.

— А вы разрушили жизнь Томаса.

Лицо священника изменилось.

Всего на мгновение.

Но Мерсер увидел.

— Вы не знаете, что произошло в библиотеке, --- произнёс Грей.

— Тогда расскажите.

— Он не понимал последствий. Он хотел обнародовать документы, которые могли уничтожить университет, лишить сотни студентов помощи, разрушить репутации людей, не знавших всей картины.

— Поэтому вы его убили?

Грей не ответил.

Мерсер сделал шаг к столу.

— Вы могли остановить его иначе.

— Я пытался.

— И когда он отказался?

Грей посмотрел ему прямо в глаза.

— Он решил, что знание даёт ему право разрушать.

— Нет. Он решил, что знание обязывает его проверить то, что вы скрывали.

Впервые Грей перестал выглядеть усталым.

— Вы не понимаете, что такое порядок.

— А вы не понимаете, что порядок, основанный на лжи, --- это просто удобное название для страха.

Мерсер повернулся к двери.

— Джек, --- позвал Грей.

Мерсер остановился.

— Вы могли бы остаться в живых, если бы умели вовремя остановиться.

Мерсер обернулся.

Ящик стола был уже открыт.

Выстрел прозвучал неожиданно громко --- громче, чем бывает в комнате с книгами, потому что книги звук не гасят, а возвращают.

Мерсера отбросило назад. Он задел плечом жалюзи и осел в кресло у окна; полосы света качнулись и легли ему на лицо.

[[PIC:c_shot|Кабинет в библиотечном крыле. Дверь, которую Мерсер не стал закрывать, --- единственная причина, по которой эта сцена попала в протокол, а не в чей-то пересказ]]

Грей стоял над ним, сжимая оружие обеими руками. На его лице не было ни ярости, ни облегчения. Только ужас человека, который наконец совершил поступок, после которого уже нельзя было спрятаться за формулировками.

Мерсер попытался что-то сказать, но не смог.

Грей опустил пистолет.

— Он сам выбрал этот путь, --- прошептал священник.

Однако дверь была открыта.

В проёме стояла мисс Уоррен, не успевшая снять руки с клавиш. В трёх шагах за ней --- сержант. Хейл был уже на пороге.

Их было трое, и они видели одно и то же.

И никто не мог изменить то, что они видели.

* * *

Хейл вошёл первым.

Он увидел Мерсера в кресле, оружие на столе и Грея, который не сопротивлялся аресту.

На следующий день газеты вышли с новыми заголовками.

Но на этот раз они не могли объявить, что убийства не было.

Были свидетели.

Было оружие.

Был арестованный.
"""
    L[a:b] = NEW.split('\n')
_patch_ending()

def _patch_lastentry():
    tgt = 'А люди продолжали рисовать его карты.'
    idx = [i for i, l in enumerate(L) if l.strip() == tgt]
    if not idx:
        return
    i = idx[-1]
    L.insert(i + 1, '')
    L.insert(i + 2, '[[PIC:c_lastentry|Последняя запись Мерсера, найденная мисс Уоррен в архиве: вопросы, которые он успел задать, и строка, которую он успел зачеркнуть]]')
_patch_lastentry()
N = len(L)   # пересчёт после вставок

# ---- mechanical fixes (typos, name unification, timeline) ----
FIXLOG = []
def fix_all(a, b):
    n = 0
    for i, l in enumerate(L):
        if a in l:
            L[i] = l.replace(a, b); n += 1
    FIXLOG.append('%s -> %s: %d строк' % (a, b, n))
for a, b in [('Олivетском', 'Оливетском'), ('Олivet', 'Оливет'), ('Олвит', 'Оливет'),
             ('Элианор', 'Элеанор'), ('Беннетт', 'Беннет'),
             ('Корзибски', 'Коржибски'), ('Корзибским', 'Коржибским'), ('Коржибским', 'Коржибским')]:
    fix_all(a, b)
import re as _re0
_RN = [(r'\bДжека\b', 'Алекса'), (r'\bДжеку\b', 'Алексу'), (r'\bДжеком\b', 'Алексом'), (r'\bДжеке\b', 'Алексе'), (r'\bДжек\b', 'Алекс')]
_n_ren = 0
for _i, _l in enumerate(L):
    _o = _l
    for _pat, _to in _RN:
        _l = _re0.sub(_pat, _to, _l)
    if _l != _o:
        L[_i] = _l; _n_ren += 1
FIXLOG.append('Джек -> Алекс: %d строк' % _n_ren)
assert L[66].startswith('Меня звали Алекс Мерсер.'), L[66][:40]
L[66] = L[66].replace('Меня звали Алекс Мерсер.', 'Меня звали Алекс Мерсер. По документам — Джулиан Александр: мать выбрала два имени, а ребёнок был один. Отсюда «J. M.» на бумагах и «Алекс» для всех остальных.', 1)
assert 'Jack Mercer' in L[12501]
L[12501] = L[12501].replace('Jack Mercer', 'Julian A. Mercer')
DATELINES = {
    53: '**Конец февраля 1937 года.**',
    718: '*Оливет, Мичиган. Февраль 1937 года. 23:40.*',
    1408: '*Оливет, Мичиган. 18 октября 1937 года. 02:17.*',
    2170: '*Оливет, Мичиган. 19 октября 1937 года. 23:51.*',
    13050: '*Оливет, Мичиган. 24 октября 1937 года.*',
    13742: '*Оливет, Мичиган. Ночь с 24 на 25 октября 1937 года.*',
    14602: '*Лансинг, Мичиган. 25 октября 1937 года.*',
    15539: '*Оливет, Мичиган. 26 октября 1937 года.*',
    16449: '*Оливет, Мичиган. 26 октября 1937 года. Вечер.*',
    17099: '*Оливет, Мичиган. 27 октября 1937 года. Утро.*',
    17967: '*Оливет, Мичиган. 28 октября 1937 года. Шесть часов утра.*',
}
for ln, txt in DATELINES.items():
    FIXLOG.append('строка %d: «%s» -> «%s»' % (ln, L[ln - 1].strip(), txt))
    L[ln - 1] = txt

# ---------------------------------------------------------------- headings
RE_SERIES = re.compile(r'^#\s*КАРТА НЕ ЕСТЬ ТЕРРИТОРИЯ\s*$')
RE_PART = re.compile(r'^#{1,6}\s*(?:Часть|ЧАСТЬ)\s+([IVXLC]+)\.?\s*(.*?)\s*$')
RE_CHAP = re.compile(r'^#{1,6}\s*ГЛАВА\s+([IVXLC]+)\.?\s*(.*?)\s*$')
RE_PROL = re.compile(r'^#{1,6}\s*ПРОЛОГ\.?\s*(.*?)\s*$')
RE_EPIC = re.compile(r'^#{1,6}\s*ЭПИЛОГ\.?\s*(.*?)\s*$')
RE_EPIP = re.compile(r'^#{1,6}\s*Эпилог\.?\s*(.*?)\s*$')
RE_FINAL = re.compile(r'^##\s*Последняя запись\s*$')
RE_SUBN = re.compile(r'^###\s*(\d+)\.\s*(.+?)\s*$')
RE_SUBL = re.compile(r'^###\s*Последняя запись\s*$')

# part starts: (line index, label, title)
starts = []
for i, l in enumerate(L):
    m = RE_PROL.match(l)
    if m:
        starts.append((i, 'Часть I', ''))      # implicit Part I (no heading in source)
        continue
    m = RE_PART.match(l)
    if m:
        starts.append((i, 'Часть ' + m.group(1), m.group(2).strip()))
        continue
    m = RE_EPIP.match(l)
    if m:
        starts.append((i, 'Эпилог', m.group(1).strip()))
        continue
    if RE_FINAL.match(l):
        starts.append((i, '', 'Последняя запись'))

# ---------------------------------------------------------------- story end triggers
TRIG = re.compile(
    r'^(?:\*{0,2}Продолжение следует'
    r'|Далее[,.]?\s*$'
    r'|\*\*Конец части'
    r'|\*\*Конец\.\*\*\s*$'
    r'|Нам нужен убийца'
    r'|Да боже закончи'
    r'|Усилить связь темы'
    r'|Сделатт интригу'
    r'|Теперь сделать заворот'
    r'|Я придумал концовку'
    r'|Почему он всё знает'
    r'|Сколько ещё до конца'
    r'|А мой финальные фразы'
    r')')

# superseded versions (replaced after the author's feedback) -> appendix file
SUPERSEDED_LINES = {54281, 55696}   # 1-based start lines: LXXX "Последняя ложь", LXXXIV "Приговор"

parts = []
log = []      # removed fragments
for k, (s, label, title) in enumerate(starts):
    e = starts[k + 1][0] if k + 1 < len(starts) else N
    end = e   # exclusive
    trig = None
    for j in range(s + 1, e):
        if TRIG.match(L[j]):
            trig = j
            break
    if trig is not None:
        end = trig
    elif k + 1 < len(starts) or True:
        trig = None
    parts.append(dict(s=s, e=e, end=end, label=label, title=title, trig=trig,
                      sup=(s + 1) in SUPERSEDED_LINES))
    # log removed tail
    tail = [(j + 1, L[j]) for j in range(end, e) if L[j].strip() and not RE_SERIES.match(L[j])]
    if tail:
        log.append((label or title, tail))

# ---------------------------------------------------------------- inline conversion
def esc(s):
    rep = {'\\': r'\textbackslash{}', '&': r'\&', '%': r'\%', '$': r'\$', '#': r'\#',
           '_': r'\_', '{': r'\{', '}': r'\}', '~': r'\textasciitilde{}', '^': r'\textasciicircum{}'}
    return ''.join(rep.get(c, c) for c in s)

stray = []

def inline(s, lineno=None):
    s = s.strip()
    s = s.replace('\t', ' ')
    s = re.sub(r'"([^"]*)"', r'«\1»', s)
    s = esc(s)
    s = s.replace('\u2192', '\u00a0$\\to$\u00a0').replace('\u2190', '\u00a0$\\gets$\u00a0')
    s = re.sub(r'\*\*\*(.+?)\*\*\*', r'\\textbf{\\textit{\1}}', s)
    s = re.sub(r'\*\*(.+?)\*\*', r'\\textbf{\1}', s)
    s = re.sub(r'\*(.+?)\*', r'\\textit{\1}', s)
    if '*' in s:
        stray.append((lineno, s[:80]))
        s = s.replace('*', '')
    s = s.replace(' — ', '\u00a0— ')
    s = re.sub(r'(?<=\s)(и|в|на|с|к|о|а|но|не|по|за|из|от|до|у|я|же|ли|бы)\s', lambda m: m.group(1) + '\u00a0', s)
    return s

CAPS_KEEP = {'оливет': 'Оливет', 'мичиган': 'Мичиган'}

def title_case(t):
    """ALL-CAPS heading -> sentence case (first letter, after «, proper names kept)."""
    if not t or t != t.upper():
        return t
    t = t.lower()
    t = re.sub(r'\b(оливет|мичиган)\b', lambda m: CAPS_KEEP[m.group(1)], t)
    t = t[0].upper() + t[1:]
    t = re.sub(r'«(\w)', lambda m: '«' + m.group(1).lower(), t)
    return t

def tex_arg(t):
    return inline(t)

# ---------------------------------------------------------------- body emitter
FIGS_AFTER = {5326: 'timeline', 12504: 'sign', 19146: 'r6'}

def fig_tex(name):
    if name in FIGS:
        code, cap = FIGS[name]
        return '\\figblock{%s}{%s}' % (code, inline(cap))
    if name in DOCS and name + '_cap' in DOCS:
        return '\\docblock{%s}{%s}' % (DOCS[name], inline(DOCS[name + '_cap']))
    raise KeyError(name)

GAPN = [0]

def emit_body(a, b):
    out = []
    for j in range(a, b):
        l = L[j]
        if (j) in FIGS_AFTER and False:
            pass
        if not l.strip() or RE_SERIES.match(l):
            continue
        m = RE_CHAP.match(l)
        if m:
            if any(x.strip() for x in out):
                out.append('\\gap{%d}' % (GAPN[0] % 24)); GAPN[0] += 1
                out.append('\\clearpage')
            out.append('\\storysection{Глава %s}{%s}' % (m.group(1), tex_arg(title_case(m.group(2)))))
            continue
        m = RE_PROL.match(l)
        if m:
            out.append('\\storysection{Пролог}{%s}' % tex_arg(title_case(m.group(1))))
            continue
        m = RE_EPIC.match(l)
        if m:
            out.append('\\storysection{Эпилог}{%s}' % tex_arg(title_case(m.group(1))))
            continue
        m = RE_SUBN.match(l)
        if m:
            out.append('\\storysub{%s}{%s}' % (m.group(1), tex_arg(m.group(2))))
            continue
        if RE_SUBL.match(l):
            out.append('\\storysub{}{Последняя запись}')
            continue
        if re.match(r'^\s*(\*\s*\*\s*\*|\*{3,}|-{3,}|_{3,})\s*$', l):
            out.append('\\scenebreak')
            continue
        if re.match(r'^#{1,6}\s', l):
            out.append('%% UNHANDLED HEADING line %d: %s' % (j + 1, l))
            continue
        s = l.strip()
        if re.match(r'^\*[^*]{5,90}\*$', s) and re.search(r'\d{4}|\d\d:\d\d', s):
            out.append('\\dateline{%s}' % inline(s[1:-1], j + 1))
            continue
        bold = False
        if s.count('**') == 1:
            if s.startswith('**'):
                s, bold = s[2:], True
            elif s.endswith('**'):
                s, bold = s[:-2], True
        t = inline(s, j + 1)
        if bold:
            t = '\\textbf{%s}' % t
        out.append(t + '\n')
        if (j + 1) in FIGS_AFTER:
            out.append(fig_tex(FIGS_AFTER[j + 1]))
    return '\n'.join(out)

def part_header(p):
    label, title = p['label'], p['title']
    title = title_case(title)
    if label and title:
        toc = '%s. %s' % (label, title)
        return '\\storypart{%s}{%s}{%s}' % (tex_arg(label), tex_arg(title), tex_arg(toc))
    if label:
        return '\\storypartL{%s}' % tex_arg(label)
    return '\\storypartT{%s}' % tex_arg(title)

# ---------------------------------------------------------------- preamble
PRE = r'''% !TEX program = xelatex
\documentclass[b5paper,11pt,twoside,openany]{book}
\usepackage{fontspec}
\usepackage{polyglossia}
\setmainlanguage{russian}
\setotherlanguage{english}
\defaultfontfeatures{Ligatures=TeX}
\usepackage[table]{xcolor}
\definecolor{accent}{HTML}{B08D3F}
\definecolor{coverbg}{HTML}{111113}
\definecolor{coverfg}{HTML}{EFE9DE}
% ---- Шрифты. Если рядом лежит папка fonts/ — берём Lora + Montserrat.
\IfFileExists{fonts/Lora-Regular.ttf}{%
  \setmainfont{Lora-Regular.ttf}[Path=fonts/,BoldFont=Lora-Bold.ttf,ItalicFont=Lora-Italic.ttf,
     BoldItalicFont=Lora-BoldItalic.ttf,Ligatures=TeX]
  \newfontfamily\disp{Mont-Regular.ttf}[Path=fonts/,BoldFont=Mont-Bold.ttf,ItalicFont=Mont-Italic.ttf,
     FontFace={k}{n}{Mont-Black.ttf},Ligatures=TeX]
  \newcommand{\blackface}{\fontseries{k}\selectfont}%
}{%
  \IfFontExistsTF{Libertinus Serif}{\setmainfont{Libertinus Serif}}{%
  \IfFontExistsTF{Liberation Serif}{\setmainfont{Liberation Serif}}{\setmainfont{DejaVu Serif}}}
  \IfFontExistsTF{Liberation Sans}{\newfontfamily\disp{Liberation Sans}}{\newfontfamily\disp{DejaVu Sans}}
  \newcommand{\blackface}{\bfseries}%
}
\addto\captionsrussian{\renewcommand{\figurename}{Рисунок}\renewcommand{\tablename}{Таблица}}
\usepackage[inner=20mm,outer=16mm,top=19mm,bottom=20mm]{geometry}
\usepackage{microtype}
\usepackage{indentfirst}
\usepackage{needspace}
\usepackage{fancyhdr}
\usepackage[breakable,skins]{tcolorbox}
\tcbuselibrary{skins}
\usepackage{graphicx}
\newcommand{\pageimg}[2]{\clearpage\thispagestyle{plain}%
\begin{center}\vspace*{\fill}%
\makebox[\linewidth][c]{\includegraphics[width=1.16\linewidth,height=0.86\textheight,keepaspectratio]{#1}}\par
\vspace{3mm}{\footnotesize\itshape #2\par}%
\vspace*{\fill}\end{center}\clearpage}
\newcommand{\pageimgrot}[2]{\clearpage\thispagestyle{empty}%
\begin{center}\vspace*{\fill}%
\rotatebox{90}{\begin{minipage}{0.90\textheight}\centering
\includegraphics[width=\linewidth,height=1.14\textwidth,keepaspectratio]{#1}\par
\vspace{2.5mm}{\footnotesize\itshape #2\par}\end{minipage}}%
\vspace*{\fill}\end{center}\clearpage}
\newcommand{\inlineimg}[3]{\begin{center}%
\includegraphics[width=#2\linewidth]{#1}\par
\vspace{2mm}{\footnotesize\itshape #3\par}\end{center}}
\usepackage{tikz}
\usetikzlibrary{arrows.meta,positioning,fit,calc,decorations.pathmorphing,decorations.pathreplacing}
\usepackage{adjustbox}
\usepackage{tabularx,array}
\usepackage{booktabs}
\usepackage[font=small,labelsep=colon,skip=4pt]{caption}
\DeclareCaptionFont{caplab}{\disp\bfseries\small}
\captionsetup{labelfont=caplab,justification=centering}
\captionsetup[table]{justification=centering}
\IfFontExistsTF{CMU Typewriter Text}{\newfontfamily\docfont{CMU Typewriter Text}}{%
\IfFontExistsTF{Liberation Mono}{\newfontfamily\docfont{Liberation Mono}}{%
\IfFontExistsTF{DejaVu Sans Mono}{\newfontfamily\docfont{DejaVu Sans Mono}}{\newfontfamily\docfont{Latin Modern Mono}}}}
\makeatletter
\renewcommand\normalsize{\@setfontsize\normalsize{10.3}{13.7}}
\makeatother
\newcommand{\spaced}[2]{{\disp\fontsize{#1}{#1}\selectfont\addfontfeature{LetterSpace=35}#2}}
\tikzset{
  box/.style={draw,rounded corners=3pt,align=center,font=\footnotesize,minimum height=7mm,inner xsep=4pt,inner ysep=3pt,fill=white},
  grp/.style={font=\footnotesize\bfseries,inner sep=2pt},
  soft/.style={draw,rounded corners=3pt,align=center,font=\footnotesize,fill=black!6,inner sep=3pt},
  arr/.style={-{Latex[length=1.8mm,width=1.4mm]},line width=0.4pt},
}
\newcolumntype{S}{>{\raggedright\arraybackslash\hspace{0pt}}p{23mm}}
\newcolumntype{M}{>{\raggedright\arraybackslash\hspace{0pt}}p{32mm}}
\newcolumntype{Y}{>{\raggedright\arraybackslash\hspace{0pt}}X}
\newcommand{\thd}[1]{{\disp\bfseries\footnotesize #1}}
\newcommand{\tabblock}[3]{%
  \par\addvspace{12pt plus 5pt minus 3pt}%
  \begin{lrbox}{\blkbox}\begin{minipage}{\linewidth}\centering
  \captionof{table}{#3}\vspace{3pt}\par
  \begingroup\footnotesize\renewcommand{\arraystretch}{1.35}\setlength{\tabcolsep}{6pt}%
  \hyphenpenalty=10000\exhyphenpenalty=10000\relax
  \rowcolors{2}{black!4}{white}%
  \begin{tabularx}{\linewidth}{#1}\toprule
#2\\ \bottomrule\end{tabularx}\endgroup
  \end{minipage}\end{lrbox}%
  \needspace{\dimexpr\ht\blkbox+\dp\blkbox+0.5\baselineskip\relax}%
  \noindent\usebox{\blkbox}\par\addvspace{12pt plus 5pt minus 3pt}\noindent\ignorespaces}
\newcommand{\crosssym}{{\tikz[baseline=0pt]{\draw[line width=0.5pt](0,-0.15ex)--(0,1.15ex)(-0.35ex,0.75ex)--(0.35ex,0.75ex);}}}
\newsavebox{\blkbox}
\newcommand{\caprule}{\par\vspace{3.5pt}{\color{black!22}\rule{26mm}{0.3pt}}\par\vspace{1.5pt}}
% Блок со схемой: измеряем высоту и, если не влезает, переносим целиком на новую страницу.
\newcommand{\pullquote}[1]{\par\addvspace{9pt}\begin{center}\begin{minipage}{0.84\linewidth}\centering
{\color{accent}\rule{16mm}{0.5pt}}\par\vspace{4pt}{\itshape #1\par}\vspace{4pt}{\color{accent}\rule{16mm}{0.5pt}}
\end{minipage}\end{center}\addvspace{9pt}}
\newcommand{\figblock}[2]{%
  \par\addvspace{12pt plus 5pt minus 3pt}%
  \begin{lrbox}{\blkbox}\begin{minipage}{\linewidth}\centering
  \adjustbox{max width=\linewidth,max totalheight=0.76\textheight}{#1}\caprule
  \captionof{figure}{#2}\end{minipage}\end{lrbox}%
  \needspace{\dimexpr\ht\blkbox+\dp\blkbox+0.5\baselineskip\relax}%
  \noindent\usebox{\blkbox}\par\addvspace{12pt plus 5pt minus 3pt}\noindent\ignorespaces}
\newtcolorbox{docbox}[1]{enhanced,breakable=false,colback=black!4,colframe=black!70,boxrule=0.5pt,arc=0pt,
  left=8pt,right=8pt,top=6pt,bottom=6pt,fontupper=\docfont\small,title={#1},fonttitle=\docfont\bfseries\footnotesize,
  coltitle=white,colbacktitle=black!70,before skip=4pt,after skip=4pt,width=0.86\linewidth,center}
\newcommand{\docblock}[2]{%
  \par\addvspace{12pt plus 5pt minus 3pt}%
  \begin{lrbox}{\blkbox}\begin{minipage}{\linewidth}\centering
  #1\caprule\captionof{figure}{#2}\end{minipage}\end{lrbox}%
  \needspace{\dimexpr\ht\blkbox+\dp\blkbox+0.5\baselineskip\relax}%
  \noindent\usebox{\blkbox}\par\addvspace{12pt plus 5pt minus 3pt}\noindent\ignorespaces}
\newtcolorbox{diarybox}[1]{enhanced,breakable,colback=yellow!9!white,colframe=brown!55!black,boxrule=0.4pt,arc=2pt,
  left=8pt,right=8pt,top=6pt,bottom=6pt,before skip=10pt,after skip=10pt,fontupper=\itshape,
  title={#1},fonttitle=\itshape\small,coltitle=brown!60!black,colbacktitle=yellow!25!white,
  borderline west={2.2pt}{0pt}{red!50!black}}
\newtcolorbox{slipbox}{enhanced,colback=blue!3!white,colframe=blue!40!black,boxrule=0.3pt,arc=0pt,left=6pt,right=6pt,top=4pt,bottom=4pt,
  before skip=8pt,after skip=8pt,width=0.8\linewidth,center,
  underlay={\begin{tcbclipinterior}\draw[step=3.5mm,blue!14,line width=0.2pt] (interior.south west) grid (interior.north east);\end{tcbclipinterior}}}
\newcommand{\slip}[2]{\begin{slipbox}\itshape #1\hfill\upshape\bfseries #2\end{slipbox}}
\usepackage{tocloft}
\renewcommand{\cftchapfont}{\disp\fontsize{9.4}{12}\selectfont}
\renewcommand{\cftchappagefont}{\disp\fontsize{8.8}{12}\selectfont}
\renewcommand{\cftsecfont}{\itshape\small}
\renewcommand{\cftsecpagefont}{\small}
\setlength{\cftbeforechapskip}{1.5pt}
\usepackage[hidelinks]{hyperref}
\usepackage{xurl}
\urlstyle{same}
\setlength{\parindent}{1.3em}
\setlength{\parskip}{0pt}
\linespread{1.0}
\widowpenalty=10000
\clubpenalty=10000
\displaywidowpenalty=10000
\sloppy
\emergencystretch=2em
\raggedbottom
\setcounter{tocdepth}{2}

\pagestyle{fancy}
\fancyhf{}
\fancyhead[LE]{\disp\fontsize{7.4}{9}\selectfont\addfontfeature{LetterSpace=22}КАРТА НЕ ЕСТЬ ТЕРРИТОРИЯ}
\fancyhead[RO]{\disp\fontsize{7.4}{9}\selectfont\rightmark}
\fancyfoot[C]{\disp\fontsize{8.6}{10}\selectfont\thepage}
\renewcommand{\headrulewidth}{0pt}
\fancypagestyle{plain}{\fancyhf{}\fancyfoot[C]{\disp\fontsize{8.6}{10}\selectfont\thepage}\renewcommand{\headrulewidth}{0pt}}

\newtcolorbox{notebox}[1]{breakable, enhanced, colback=black!4, colframe=black!45, boxrule=0.4pt, arc=1pt,
  left=6pt,right=6pt,top=4pt,bottom=4pt, before skip=10pt, after skip=10pt,
  title={#1}, fonttitle=\bfseries\small, coltitle=black, colbacktitle=black!12, attach boxed title to top left={yshift=-2mm,xshift=4mm}, boxed title style={arc=1pt,boxrule=0.3pt}}
\newcommand{\storypartopen}[1]{\clearpage\phantomsection
  \addcontentsline{toc}{chapter}{#1}\markright{#1}\thispagestyle{plain}%
  \vspace*{0.075\textheight}}
\newcommand{\storypartclose}{\vspace{1.5\baselineskip}\par\nopagebreak}
\newcommand{\partrule}{\par\vspace{2.8mm}{\color{accent}\rule{17mm}{0.6pt}}\par\vspace{3.4mm}}
\newcommand{\storypart}[3]{\storypartopen{#3}%
  \begin{center}{\disp\fontsize{8.4}{10}\selectfont\addfontfeature{LetterSpace=42}\MakeUppercase{#1}}\partrule
  {\disp\bfseries\fontsize{15.5}{18.5}\selectfont #2\par}\end{center}\storypartclose}
\newcommand{\storypartL}[1]{\storypartopen{#1}%
  \begin{center}{\disp\blackface\fontsize{15.5}{18.5}\selectfont #1\par}\partrule\end{center}\storypartclose}
\newcommand{\storypartT}[1]{\storypartopen{#1}%
  \begin{center}{\disp\bfseries\fontsize{15.5}{18.5}\selectfont #1\par}\partrule\end{center}\storypartclose}
\newsavebox{\gapbox}
\newcommand{\gaptext}[1]{\ifcase#1\relax
Третье положение общей семантики разрешает описывать описание. Пользуюсь разрешением: ниже этой строки --- пустое место. Оно возникло потому, что глава кончилась раньше страницы. Я мог бы долить воды, но вода в протоколе --- это подлог.
\or Эту пустоту заметил даже автор и предложил растянуть последний абзац. Я напомнил ему про карту карт: если описать пустоту, она становится частью карты и перестаёт быть дырой. Готово. Читайте дальше.
\or Пустое место внизу страницы --- честная единица измерения: ровно столько мне не хватило, чтобы договорить. Сью называет это полями для сомнений. Хейл называет это «бумага кончилась».
\or Коржибски сказал бы: карта может содержать карту самой себя, и тогда внизу всегда остаётся место ещё для одной. Вот оно. Не заполняйте.
\or Я спросил автора, зачем он оставил здесь дыру. Он ответил, что глава кончилась. Я записал: «причина названа, проверке не поддаётся».
\or Это место можно было занять ещё одним выводом. Я не стал: выводов у меня и так больше, чем документов.
\or Здесь мог бы быть ещё один допрос, но свидетель ушёл обедать, а страница осталась.
\or Карта карт: если вы сейчас решили, что это пустое место что-то значит, вы делаете ровно то, за что я весь роман ругаю Хейла.
\or Пустота внизу страницы --- единственное место в этой книге, где я ничего не утверждаю. Поберегите её.
\or Третье положение: описание можно описать. Описываю: белое, прямоугольное, без даты и без индекса. Уровень --- факт. Редкий для меня случай.
\or Автор хотел поставить сюда эпиграф. Я возразил: эпиграф --- это чужая бирка на моей главе. Он согласился, и место осталось.
\or Если вам неуютно от пустого места, попробуйте так же отнестись к пропускам в чужих показаниях. Там пустоты ровно столько же, просто её не видно.
\or Здесь кончилась глава, а не мысль. Расстояние между этими двумя событиями --- примерно сантиметр бумаги.
\or Я предложил напечатать внизу страницы таблицу. Сью спросила какую. Я не придумал. Это и есть ответ.
\or Моя карта описала саму себя и обнаружила, что внизу у неё поля. Поля --- тоже территория, просто очень скучная.
\or Здесь мог быть рисунок, но он не влез. Рисунок, который не влез, честнее рисунка, который растянули.
\or Хейл утверждает, что пустое место на бумаге --- это непотраченные деньги налогоплательщика. Я ответил, что враньё обходится дороже.
\or Пауза. В общей семантике паузу советуют делать перед ответом. На бумаге она выглядит именно так.
\or В этом месте я обычно сверяюсь: что я уже доказал, а что только громко сказал. Сверьтесь и вы, место как раз есть.
\or Если бы я заполнил это поле словами, вы бы их прочитали. Прочитав, решили бы, что они зачем-то нужны. От этой цепочки я вас и избавил.
\or Карта не есть территория, а страница не есть глава. Глава кончилась раньше. Страница терпит.
\or Я заметил, что замечаю. Коржибски называет это третьим положением, Сью --- занудством, а Хейл --- «Мерсер, вы опять».
\or Внизу осталось место ровно на один неподтверждённый вывод. Именно поэтому я его туда не пишу.
\or Здесь был бы диалог, но оба собеседника уже легли спать. Утро вечера, как известно, индекснее.
\fi}
\newcommand{\gap}[1]{\par
  \sbox{\gapbox}{\begin{minipage}{0.80\linewidth}\small\itshape\raggedright\gaptext{#1}\end{minipage}}%
  \ifdim\pagegoal=\maxdimen\else
    \ifdim\dimexpr\pagegoal-\pagetotal\relax>\dimexpr\ht\gapbox+\dp\gapbox+5\baselineskip\relax
      \vfill\begin{center}{\color{accent}\rule{20mm}{0.4pt}}\par\vspace{2.6mm}%
      \usebox{\gapbox}\par\vspace{1mm}\end{center}%
    \fi
  \fi}
\newcommand{\storysection}[2]{\par\needspace{5\baselineskip}\vspace{1.4\baselineskip}\phantomsection
  \addcontentsline{toc}{section}{#1. #2}%
  \begin{center}{\disp\bfseries\fontsize{9.4}{11}\selectfont\addfontfeature{LetterSpace=20}\MakeUppercase{#1}}\\[0.3em]{\itshape #2}\end{center}\nopagebreak\vspace{0.45\baselineskip}}
\newcommand{\storysub}[2]{\par\needspace{4\baselineskip}\vspace{0.9\baselineskip}%
  \begin{center}{\disp\fontsize{8.6}{10.5}\selectfont\addfontfeature{LetterSpace=18}#1\ifx\relax#1\relax\else.\ \fi #2}\end{center}\nopagebreak\vspace{0.35\baselineskip}}
\newcommand{\sbdiamond}{\tikz[baseline=-0.4ex]{\fill[accent,rotate=45] (0,0) rectangle (1.5mm,1.5mm);}}
\newcommand{\scenebreak}{\par\vspace{0.7\baselineskip plus 3pt minus 2pt}\begin{center}\sbdiamond\hspace{3.2mm}\sbdiamond\hspace{3.2mm}\sbdiamond\end{center}\vspace{0.5\baselineskip}}
\newcommand{\dateline}[1]{\par\vspace{0.35\baselineskip plus 2pt}\begin{center}\itshape\small #1\end{center}\vspace{0.15\baselineskip}}
'''

def titlepage(title, subtitle, note):
    return r'''
\begin{document}
\frontmatter
\thispagestyle{empty}
\begin{center}
\vspace*{0.13\textheight}
{\disp\fontsize{8}{10}\selectfont\addfontfeature{LetterSpace=45}НАУЧНО-НУАРНЫЙ ДЕТЕКТИВ\par}
\vspace{9mm}
{\disp\blackface\fontsize{25}{28}\selectfont %s\par}
\vspace{5mm}
{\color{accent}\rule{0.36\linewidth}{0.6pt}}\par
\vspace{7mm}
{\disp\fontsize{15}{18}\selectfont\addfontfeature{LetterSpace=24}ALEX MERSER\par}
\vspace{2mm}
{\disp\fontsize{8.5}{10}\selectfont\addfontfeature{LetterSpace=24}\textcolor{accent}{АЛЕКС МЕРСЕР}\par}
\vspace{10mm}
{\itshape %s\par}
\vfill
{\footnotesize %s\par}
\vspace{6mm}
\end{center}
\clearpage
''' % (title, subtitle, note)


# ---------------------------------------------------------------- interludes
import re as _re
def load_interludes(path):
    s = open(path, encoding='utf-8').read()
    items = []
    for blk in _re.split(r'(?m)^(?==== after=)', s):
        if not blk.strip():
            continue
        head, _, body = blk.partition('\n')
        m = _re.match(r'=== after=(.+?) \| title=(.+)$', head.strip())
        items.append(dict(after=m.group(1).strip(), title=m.group(2).strip(), body=body))
    return items

INUM = [0]

def emit_interlude(it, num):
    out = []
    _t = it['title']
    if '::' in _t:
        _lab, _t = _t.split('::', 1)
    else:
        INUM[0] += 1
        _lab = 'Интермедия %d' % INUM[0]
        _t = it['title']
    out.append('\\storypart{%s}{%s}{%s}' % (inline(_lab), inline(_t),
                                          inline('%s. %s' % (_lab, _t))))
    lines = it['body'].split('\n')
    i = 0
    while i < len(lines):
        l = lines[i]
        if not l.strip():
            i += 1; continue
        if l.startswith('~ '):
            out.append('\\dateline{%s}' % inline(l[2:]))
            i += 1; continue
        if l.startswith('@@IMG'):
            _rest = l[len('@@IMG'):].strip()
            _nm, _, _cap = _rest.partition('|')
            _nm = _nm.strip()
            if _nm.endswith('!rot'):
                out.append('\\pageimgrot{img/%s.png}{%s}' % (_nm[:-4].strip(), inline(_cap.strip())))
            elif _nm.endswith('!in'):
                out.append('\\inlineimg{img/%s.png}{0.52}{%s}' % (_nm[:-3].strip(), inline(_cap.strip())))
            else:
                out.append('\\pageimg{img/%s.png}{%s}' % (_nm, inline(_cap.strip())))
            i += 1; continue
        if l.startswith('@@TABLE'):
            cap, _, spec = l[len('@@TABLE'):].partition('||')
            i += 1; rows = []
            while i < len(lines) and not lines[i].startswith('@@END'):
                if lines[i].strip():
                    rows.append([inline(c.strip()) for c in lines[i].split('|')])
                i += 1
            i += 1
            rr = [(' & '.join(r'\thd{%s}' % c for c in r) if k == 0 else ' & '.join(r)) for k, r in enumerate(rows)]
            body_t = (rr[0] + ' \\\\\n\\midrule\n' + ' \\\\\n'.join(rr[1:])) if len(rr) > 1 else rr[0]
            _wt = {'S': 0.70, 'M': 0.95, 'X': 1.30, 'Y': 1.30}
            _cols = [c for c in spec.strip().split() if c]
            _ws = [_wt.get(c, 1.0) for c in _cols]
            _k = len(_ws) / sum(_ws)
            _spec = ''.join(r'>{\hsize=%.3f\hsize\raggedright\arraybackslash\hspace{0pt}}X' % (w * _k) for w in _ws)
            out.append('\\tabblock{%s}{%s}{%s}' % (_spec, body_t, inline(cap.strip())))
            continue
        if l.startswith('> '):
            out.append('\\pullquote{%s}' % inline(l[2:])); i += 1; continue
        if l.startswith('@@SRC'):
            lab, _, url = l[len('@@SRC'):].partition('||')
            if url.strip():
                _fn = '\\footnote{%s \\url{%s}}' % (inline(lab.strip()), url.strip())
            else:
                _fn = '\\footnote{%s}' % inline(lab.strip())
            _BLK = ('\\figblock', '\\docblock', '\\tabblock', '\\dateline', '\\scenebreak',
                    '\\begin', '\\end', '\\pullquote', '\\slip', '\\gap', '\\storysection',
                    '\\storysub', '\\storypart', '\\item')
            if out and out[-1].strip() and not out[-1].lstrip().startswith(_BLK):
                out[-1] = out[-1].rstrip('\n') + _fn + '\n'
            else:
                out.append(_fn)
            i += 1; continue
        if l.startswith('@@FIG '):
            out.append(fig_tex(l[6:].strip())); i += 1; continue
        if l.startswith('@@SLIP '):
            txt, _, sig = l[7:].partition('|')
            out.append('\\slip{%s}{%s}' % (inline(txt.strip()), inline(sig.strip()))); i += 1; continue
        if l.startswith('@@DIARY'):
            title = l[len('@@DIARY'):].strip()
            out.append('\\begin{diarybox}{%s}' % inline(title))
            i += 1
            _items = []
            def _flush2():
                if _items:
                    out.append('\\begin{itemize}\\setlength\\itemsep{1pt}')
                    out.extend('\\item ' + inline(x) for x in _items)
                    out.append('\\end{itemize}')
                    _items.clear()
            while i < len(lines) and not lines[i].startswith('@@END'):
                t2 = lines[i].strip()
                if t2.startswith('- '):
                    _items.append(t2[2:])
                elif t2:
                    _flush2()
                    out.append('\\noindent ' + inline(t2) + '\n')
                i += 1
            _flush2()
            out.append('\\end{diarybox}')
            i += 1
            continue
        if l.startswith('@@NOTE'):
            title = l[len('@@NOTE'):].strip()
            out.append('\\begin{notebox}{%s}' % inline(title))
            i += 1
            items = []
            def flush():
                if items:
                    out.append('\\begin{itemize}\\setlength\\itemsep{2pt}')
                    out.extend('\\item ' + inline(x) for x in items)
                    out.append('\\end{itemize}')
                    items.clear()
            while i < len(lines) and not lines[i].startswith('@@END'):
                t = lines[i].strip()
                if t.startswith('- '):
                    items.append(t[2:])
                elif t:
                    flush()
                    out.append('\\noindent ' + inline(t) + '\n')
                i += 1
            flush()
            out.append('\\end{notebox}')
            i += 1
            continue
        if _re.match(r'^\d+\. ', l):
            out.append('\\begin{enumerate}\\setlength\\itemsep{1pt}')
            while i < len(lines) and _re.match(r'^\d+\. ', lines[i]):
                out.append('\\item ' + inline(_re.sub(r'^\d+\. ', '', lines[i])))
                i += 1
            out.append('\\end{enumerate}')
            continue
        if _re.match(r'^\s*(\*\s*\*\s*\*|\*{3,})\s*$', l):
            out.append('\\scenebreak'); i += 1; continue
        t = l.strip()
        bold = False
        out.append(inline(t) + '\n')
        i += 1
    return '\n'.join(out)

import sys as _sys
_sys.path.insert(0, '/home/claude')
from figs import FIGS, DOCS
import figs_mid, figs_w3, figs_sem
FIGS.update(figs_mid.FIGS); DOCS.update(figs_mid.DOCS)
FIGS.update(figs_w3.FIGS); DOCS.update(figs_w3.DOCS)
FIGS.update(figs_sem.FIGS); DOCS.update(figs_sem.DOCS)
INTERLUDES = load_interludes('/home/claude/interludes.md') + load_interludes('/home/claude/mid_interludes.md') + load_interludes('/home/claude/w3_interludes.md') + load_interludes('/home/claude/sem_interludes.md')
for _it in INTERLUDES:
    for _a, _b in [('Джека', 'Алекса'), ('Джеку', 'Алексу'), ('Джеком', 'Алексом'), ('Джеке', 'Алексе'), ('Джек', 'Алекс')]:
        _it['body'] = _it['body'].replace(_a, _b)


# ---------------------------------------------------------------- assemble main book
main_parts = [p for p in parts if not p['sup']]
_order = {}
for _i, _p in enumerate(main_parts):
    _order.setdefault(_p['label'], _i)
INTERLUDES.sort(key=lambda it: _order.get(it['after'], 10**6))
sup_parts = [p for p in parts if p['sup']]

# front matter pulled from the first lines of the source
COVER = r'''
\newgeometry{margin=11mm}
\thispagestyle{empty}
\pagecolor{coverbg}\color{coverfg}
\begin{tikzpicture}[remember picture,overlay]
  \draw[accent,line width=0.7pt] ($(current page.north west)+(9mm,-9mm)$) rectangle ($(current page.south east)+(-9mm,9mm)$);
  \draw[accent!65,line width=0.25pt] ($(current page.north west)+(11.4mm,-11.4mm)$) rectangle ($(current page.south east)+(-11.4mm,11.4mm)$);
\end{tikzpicture}
\begin{center}
\vspace*{5mm}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=48}\textcolor{accent}{НАУЧНО-НУАРНЫЙ ДЕТЕКТИВ}\par}
\vspace{7mm}
{\disp\blackface\fontsize{29}{32}\selectfont\addfontfeature{LetterSpace=6}КАРТА\\НЕ ЕСТЬ\\ТЕРРИТОРИЯ\par}
\vspace{4.5mm}
{\color{accent}\rule{32mm}{0.6pt}}\par
\vspace{6mm}
{\setlength{\fboxsep}{0pt}\setlength{\fboxrule}{0.5pt}%
\textcolor{accent}{\fbox{\includegraphics[width=0.66\linewidth]{cover.jpg}}}\par}
\vspace{7mm}
{\disp\blackface\fontsize{20}{22}\selectfont\addfontfeature{LetterSpace=30}ALEX MERSER\par}
\vspace{3mm}
{\disp\fontsize{8.4}{10}\selectfont\addfontfeature{LetterSpace=32}\textcolor{accent}{АЛЕКС МЕРСЕР}\par}
\vfill
{\disp\fontsize{8}{11.5}\selectfont По мотивам семинаров Альфреда Коржибски\\по общей семантике\par}
\vspace{2.5mm}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=30}\textcolor{accent}{КОЛЛЕДЖ ОЛИВЕТ · 1937}\par}
\vspace{5mm}
\end{center}
\clearpage
\nopagecolor\color{black}\restoregeometry

% --- страница серии (в стиле «Вирусо-логии семантических-реакций»)
\thispagestyle{empty}
\vspace*{0.455\textheight}
\begin{center}
{\large\bfseries ОБЩАЯ-СЕМАНТИКА\par}
\vspace{2.2mm}
{\itshape\addfontfeature{LetterSpace=12}НАУКА ЧЕЛОВЕЧЕСКИХ ОЦЕНОК\par}
\end{center}
\clearpage
% --- издательский титул
\thispagestyle{empty}
\vspace*{0.40\textheight}
\begin{center}
{\large Карта не есть территория.\\[1.2ex]
Научно-нуарный детектив по мотивам семинаров\\Альфреда Коржибски, Оливет, 1937.,\par}
\vfill
\includegraphics[width=17mm]{logo.png}\par
\vspace{3.5mm}
{SocioCyberneering Inc.\par}
\vspace{2.5mm}
{19 ноября 2026 г.\par}
\vspace{6mm}
\end{center}
\clearpage
'''
LICPAGE = r"""
\clearpage\thispagestyle{empty}
\begin{center}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=40}\textcolor{accent}{СТРАНИЦА, КОТОРУЮ ОБЫЧНО НЕ ЧИТАЮТ}\par}
\vspace{3mm}
{\disp\bfseries\fontsize{15}{18}\selectfont Права, которые мы\\не стали защищать\par}
\vspace{2.5mm}
{\color{accent}\rule{17mm}{0.6pt}}\par
\end{center}
\vspace{3mm}
\begin{notebox}{Как обычно пишут на этом месте}
\small\itshape Все права защищены. Никакая часть настоящего издания не может быть воспроизведена, записана, перепечатана, пересказана вслух, пересказана шёпотом, процитирована за ужином, выучена наизусть, увидена во сне или помыслена без предварительного письменного разрешения правообладателя. Нарушители будут преследоваться по закону, а также взглядом.
\end{notebox}

\noindent Мы прочитали это вслух и услышали, как бирка ест территорию. Книга про то, что карта не есть территория, не может начинаться с обещания посадить вас за пересказ карты.

\medskip\noindent Поэтому по-человечески.

\vspace{1mm}
\medskip\noindent\textbf{Эта книга открыта.} Лицензия CC~BY-SA~4.0. Это значит:

\begin{itemize}\setlength{\itemsep}{0pt}
\item копируйте;
\item печатайте --- дома, в типографии, на работе, пока начальник не видит;
\item раздавайте бесплатно и дарите;
\item режьте на цитаты;
\item переводите на любой язык, включая те, на которых ещё не говорят;
\item читайте вслух, шёпотом и во сне --- отдельное разрешение на сон прилагается;
\item переделывайте, спорьте, дописывайте главы, которых здесь не хватает.
\end{itemize}

\medskip\noindent Три просьбы. Это и есть вся лицензия; остальное --- её перевод на юридический.

\begin{enumerate}\setlength{\itemsep}{1pt}
\item \textbf{Скажите, откуда взяли.} В лицензии это буквы BY: укажите авторство.
\item \textbf{Оставьте дальше открытым.} То, что выросло из открытого, закрытым не становится. В лицензии это буквы SA.
\item \textbf{Не выдавайте карту за территорию.} Изменили текст --- напишите, что изменили. Иначе читатель будет судить автора по вашей правке, а это уже не лицензия, это подлог.
\end{enumerate}

\medskip\noindent Исходники --- файлы вёрстки «.tex», схемы, весь набор --- на тех же правах. Если вам привычнее GPL, считайте, что у схем GPL: берите, меняйте, но передавайте вместе с исходником и не закрывайте. Разница между CC~BY-SA и GPL здесь ровно одна: первая написана для текстов, вторая --- для кода, а смысл у обеих общий и умещается в четыре слова: \textit{открытое остаётся открытым}.

\medskip
\noindent\textbf{Где лежат исходники.} Весь набор --- текст, схемы, файлы вёрстки --- здесь:

\begin{center}
\href{https://github.com/sociocyber1/Latex_ScienceBook_Detective-Alex-Merser-Map-is-not-Territory}%
{\resizebox{0.99\linewidth}{!}{github.com/sociocyber1/Latex\_ScienceBook\_Detective-Alex-Merser-Map-is-not-Territory}}
\end{center}

\noindent Скачивайте, собирайте у себя, исправляйте опечатки, присылайте правки, делайте свою версию.

\vspace{1mm}
\medskip\noindent\textbf{Чего всё-таки нельзя.} Нельзя закрыть то, что открыли (единственная оговорка --- на следующей странице). Нельзя подписать своим именем чужое. Нельзя продавать как «эксклюзивное издание»: эксклюзива нет, книга лежит в сети, бесплатно, и завтра будет лежать там же.

\vspace{1mm}
\medskip\noindent\textbf{Санкции.} За нарушение этой лицензии не предусмотрено ни штрафа, ни суда, ни коллекторов, ни взгляда. Предусмотрено только то, что вы будете человеком, который закрыл открытое. Это дороже.

\clearpage
\thispagestyle{empty}
\begin{center}
{\disp\fontsize{7.6}{9}\selectfont\addfontfeature{LetterSpace=40}\textcolor{accent}{ПРОДОЛЖЕНИЕ ТОЙ ЖЕ СТРАНИЦЫ}\par}
\vspace{3mm}
{\disp\bfseries\fontsize{13.5}{17}\selectfont Печатать, продавать\\и поддержать\par}
\vspace{2.5mm}
{\color{accent}\rule{17mm}{0.6pt}}\par
\end{center}
\vspace{2mm}

\noindent\textbf{Хотите печатать и продавать --- печатайте и продавайте.} Запрета нет, разрешения спрашивать не надо, процент автору платить не надо. Книга для того и открыта.

\noindent Три условия, и ни одно из них не про деньги:

\begin{enumerate}\setlength{\itemsep}{1pt}
\item \textbf{оставьте ссылку на оригинал} --- адрес исходников с предыдущей страницы;
\item \textbf{оставьте имя автора} и название --- не ради тщеславия, а чтобы читателю было с чем сравнить;
\item \textbf{приложите список изменений:} что сократили, что добавили, что исправили. Хоть одной страницей в конце. Это главное из трёх: без него ваш читатель будет судить об авторе по вашей правке и даже не узнает об этом.
\end{enumerate}

\medskip\noindent\textbf{Не закрывайте книгу.} Переиздание остаётся открытым --- это условие лицензии, а не пожелание.

Но бывает всякое. Если издательство требует закрытой лицензии и иначе не берёт --- берите и печатайте закрытым, пусть книга дойдёт до людей. Только сделайте одну вещь: \textbf{поставьте сноску на оригинал} и напишите прямо, что существует открытая версия, вот по этому адресу, бесплатно. Чтобы читатель знал, что у него есть выбор.

\noindent Закрытая книга, которая честно говорит, где лежит открытая, --- приемлемо. Закрытая книга, которая об этом молчит, --- нет.

\bigskip
\begin{center}{\disp\bfseries\fontsize{11}{14}\selectfont Поддержать автора и выход новых материалов\par}\end{center}

\noindent Если вы считаете эту работу полезной --- можно помочь деньгами. Коротко, без драматургии: автор делает всё сам, из своего кармана и бесплатно, а подписки, инструменты и время на них расходуются вполне материально.

\begin{center}
\fbox{\parbox{0.72\linewidth}{\centering\textbf{Сбер}\\[1.2mm]
{\disp\fontsize{12.5}{15}\selectfont\addfontfeature{LetterSpace=8}2202\hspace{2mm}2050\hspace{2mm}2451\hspace{2mm}1591}}}
\end{center}

\begin{notebox}{На полях, рукой Мерсера}
\small Автор раздал книгу даром, а страницей позже просит денег. Противоречие я отметил сразу и вслух.

Он ответил: «одно другому не мешает». Я проверил --- не мешает. В заложниках книга не сидит: не заплатите --- получите ровно то же самое, целиком, без сокращений, без «расширенной версии для поддержавших» и без вырезанной главы. Лимита на читателя нет.

Это называется просьбой, а не ценой, и разница та же, что между картой и территорией: выглядит похоже, работает совсем иначе.

Так что подавайте, если считаете нужным. Посмеяться я всё равно успел.

\textit{P.~S. Номер в рамке автор дописал последним, уже после того, как написал про деньги целую страницу и забыл указать, куда их слать. Я сверил: шестнадцать цифр, четыре группы по четыре, больше о нём сказать нечего. И отдельно, по привычке: это карта карты. Цифры --- не деньги, деньги --- не благодарность, благодарность --- не обязанность. Четыре разных уровня, и путать их не нужно ни автору, ни вам.}
\end{notebox}

\vspace{3mm}
\begin{center}
{\disp\fontsize{9}{12}\selectfont\addfontfeature{LetterSpace=16}SocioCyberneering Inc.\par}
\vspace{1.5mm}
{\itshape\small Все права розданы.\par}
\vspace{2mm}
{\footnotesize Связь с автором --- на странице «Благодарности» в конце книги.\par}
\end{center}
\clearpage
"""

MANIFESTO = r"""
\thispagestyle{empty}
\vspace*{0.26\textheight}
\begin{center}
{\disp\blackface\fontsize{17}{22}\selectfont\addfontfeature{LetterSpace=8}ВЕДЁМ РЕВОЛЮЦИЮ\\В ОЦЕНКЕ\par}
\vspace{9mm}
{\color{accent}\rule{24mm}{0.6pt}}\par
\vspace{9mm}
{\disp\blackface\fontsize{17}{22}\selectfont\addfontfeature{LetterSpace=8}КОНЕЦ ВОЙНЕ\par}
\vspace{9mm}
{\color{accent}\rule{24mm}{0.6pt}}\par
\vspace{9mm}
{\disp\blackface\fontsize{17}{22}\selectfont\addfontfeature{LetterSpace=8}ОТКРОЙ ЧЁРТОВ РАЗУМ\par}
\vfill
{\itshape\small Первый лозунг --- из тысяча девятьсот тридцать седьмого.\\
Второй --- оттуда же, и он до сих пор не выполнен.\\
Третий --- от автора, которому надоело просить вежливо.\par}
\vspace{10mm}
\end{center}
\clearpage
"""

PREFACE = r"""
\storypartT{Предисловие: о чём эта книга и зачем она}

\noindent Это детектив. Тысяча девятьсот тридцать седьмой год, маленький американский колледж, два трупа с разницей в год, сыщик по имени Алекс Мерсер и человек, который полгода считал виновным не того.

И это учебник. Только вместо параграфов --- дело, вместо контрольных --- ошибки Мерсера, а вместо преподавателя с указкой --- польский инженер Альфред Коржибски, который летом тридцать седьмого действительно читал в колледже Оливет семинар по общей семантике.

\medskip\noindent\textbf{Общая семантика --- это про то, как мы оцениваем.} Не про слова, хотя начинается со слов. Про зазор между тем, что есть, и тем, что мы об этом сказали. Между событием и фамилией. Между человеком и биркой, которую мы на него повесили, --- «убийца», «дурак», «враг», «наш».

Главная фраза Коржибски вынесена на обложку: \textit{карта не есть территория}. У неё есть продолжение, которое цитируют реже: карта покрывает не всю территорию, и хорошая карта похожа на территорию \textit{структурой}. Три строки. Из них растёт всё остальное: даты, индексы, кавычки, «и так далее», структурный дифференциал, отложенная реакция.

\medskip\noindent\textbf{Почему детектив.} Потому что сыщик --- это человек, чья профессия целиком состоит из оценки. Он смотрит на факты и говорит, что они значат. И он единственный, у кого цена ошибки видна сразу: не «неточная формулировка», а живой человек в камере. Когда Шерлок Холмс с одного взгляда называет вам профессию, биографию и мотив, это красиво. Когда так делает настоящий следователь, это называется иначе.

Мерсер начинает книгу именно таким. Он уверен, он быстр, он уже знает, кто виноват. Дальше ему придётся разбирать собственную уверенность на части --- по одной.

\medskip\noindent\textbf{Зачем это вам, если вы не сыщик.} Затем, что вы оцениваете каждый день, только без протокола. Начальник «придирается». Сосед «хамит». Страна «агрессивная». Врач «ничего не понимает». Каждая из этих фраз --- готовый приговор, вынесенный за полсекунды, и почти всегда по одному наблюдению, в котором участвовали освещение, усталость, чужой пересказ и ваше настроение.

Коржибски писал всё это после войны, на которой был. Он считал --- всерьёз, не как метафору, --- что люди убивают друг друга в том числе потому, что путают бирку с человеком, слово с вещью, год прошлый с годом нынешним. Отсюда и три лозунга на предыдущей странице. Они звучат громко. Они и задуманы громкими.

\medskip\noindent\textbf{Как читать.} В книге три вида глав, и вы вправе обращаться с ними как угодно.

\begin{itemize}\setlength{\itemsep}{1pt}
\item \textbf{Части} --- само дело. Если вам нужен только детектив, читайте одни их: история связная, без пропусков.
\item \textbf{Интермедии} --- остановки. Здесь Мерсер разбирает, что он только что сделал неправильно, и на чём именно сломалась его голова. Это та же история, только изнутри метода.
\item \textbf{Семинар} --- четырнадцать лекций, голосом Коржибски. Их можно читать подряд, отдельно от сюжета, как короткий курс. Порядок в них выстроен от простого к сложному.
\end{itemize}

Сквозной порядок --- рекомендованный: приём появляется в интермедии только после того, как его объяснили на семинаре, и только после того, как Мерсер на нём обжёгся.

\medskip\noindent\textbf{Честные оговорки, без которых книга была бы ровно тем, против чего написана.}

\begin{enumerate}\setlength{\itemsep}{1pt}
\item Коржибски --- реальный человек. Его биография и его идеи взяты из источников. Его \textit{реплики} в этой книге написаны автором. Это литературный персонаж, а не стенограмма.
\item Дело, колледж, убитые, свидетели, документы --- вымышлены целиком. Совпадения с настоящими делами не предполагались.
\item Факты из будущего (а такие в книге есть) проверялись. Как именно --- показано внутри, в одной из интермедий, вместе с тем, что проверку не прошло. Это не кокетство: книга про проверку обязана показать свою.
\item Четвёртая стена здесь регулярно ломается, и автор время от времени получает от собственного героя. Это сделано нарочно и ровно по третьему положению общей семантики, которое разрешает говорить о говорении.
\end{enumerate}

\medskip\noindent\textbf{Чего эта книга не делает.} Она не обещает, что вы перестанете ошибаться. Коржибски такого не обещал, а он был смелее. Она предлагает другое: заметить зазор. Между тем, что случилось, и тем, что вы об этом сказали. Между человеком и фамилией. Между картой и территорией.

Дальше зазор никуда не денется. Но в него можно перестать проваливаться каждый раз.

\vspace{2mm}
\medskip\noindent И последнее. Эта книга --- тоже карта. Со своими пробелами, своим масштабом и своей датой на обложке.

\begin{center}\itshape Проверяйте.\end{center}
\clearpage
"""

TITLE = 'Карта не есть территория'
SUBTITLE = 'Детектив по мотивам семинаров Альфреда Коржибски\\\\по общей семантике в колледже Оливет, 1937 год'
NOTE = 'Художественная история. Детектив, преступление и диалоги вымышлены; идеи Коржибски служат интеллектуальной основой сюжета.'

body = []
for p in main_parts:
    body.append('\n%% ------------------------------------------------ source lines %d-%d' % (p['s'] + 1, p['end']))
    body.append(part_header(p))
    # skip the heading line itself if it is a pure part heading, emit the rest
    a = p['s']
    if not RE_PROL.match(L[a]):
        a += 1
    _bt = emit_body(a, p['end'])
    if _re.search(r'Часть (LXX[VIX]+|LXXX|LXXX[VI]*|XC[IV]*)$', p['label'] or ''):
        _bt = _re.sub(r'(отц[а-я]+ Грей?[а-я]*)', lambda m: m.group(1) + '~\\crosssym{}', _bt, count=1)
    body.append(_bt)
    for it in INTERLUDES:
        if it['after'] == p['label'] and not p['sup']:
            _n = INTERLUDES.index(it) + 1
            body.append('\n%% ------------------------------------------------ INTERLUDE %d (after %s)' % (_n, p['label']))
            body.append(emit_interlude(it, _n))

# back matter: historical note (source lines 701-710)

VIDEOS = [
    ('Семинары 1937 года, лекция 1', 'https://www.youtube.com/watch?v=HxcPdrqJWPE'),
    ('Семинары 1937 года, лекция 2', 'https://www.youtube.com/watch?v=MjlgNhKoQds'),
    ('«Зрелость человечности», глава 1', 'https://youtu.be/ntBa9PE1n5A'),
    ('«Зрелость человечности», глава 2', 'https://youtu.be/_UlS9lbpWug'),
    ('«Зрелость человечности», глава 3', 'https://youtu.be/_p6cSoZ2dQA'),
]
def videolist():
    o = ['\\noindent Записи, на которые опирались сцены с Коржибски и главы о время-связывании (ссылки предоставлены автором; содержание записей в этой книге не цитируется дословно):\n',
         '\\begin{itemize}\\setlength\\itemsep{1pt}']
    for t, u in VIDEOS:
        o.append('\\item %s: \\url{%s}' % (inline(t), u))
    o.append('\\end{itemize}')
    return '\n'.join(o)

def hist_note():
    out = ['\\storypartT{Историческая справка}']
    out.append(inline(L[701]))   # "История использует..."
    out.append('\\begin{itemize}')
    for j in (702, 703, 704, 705, 706):
        t = L[j].lstrip('- ').strip()
        out.append('\\item ' + inline(t))
    out.append('\\end{itemize}')
    t707 = re.sub(r'\s+ERIC\s*$', '', L[707].strip())
    out.append(inline(t707) + '\n')
    out.append(inline(L[709]) + '\n')
    out.append('\\storysection{Источники}{и прототипы}')
    extra = [
        'Идеи общей семантики в романе опираются на книги Альфреда Коржибски («Наука и здравомыслие», 1933), на «Язык в мысли и действии» Сэмюэла Хаякавы, на «Людей в затруднении» Уэнделла Джонсона (там описана «болезнь ИФД»: от идеализма к фрустрации и деморализации) и на труды Брюса и Сьюзан Кодиш — биографию Коржибски (2011) и практическое руководство «Drive Yourself Sane».',
        'Бен и Сью Лоренц, доктор Вернон Хоукс, профессор Сэм Накамура и незнакомец М. К. — вымышленные прототипы, а не реальные люди. Их реплики придуманы автором и не являются цитатами. Профессор Коржибски в романе — литературный персонаж, его слова не следует считать подлинными.',
        'Шесть шагов решения проблем, которыми пользуется Мерсер (выбрать одну проблему, перечислить варианты, взвесить плюсы и минусы, выбрать, составить план, проверить результат), пересказаны по общедоступной рабочей тетради «Problem Solving» (TalkPlus, NHS, август 2023).',
        '«Полевой определитель ловушек оценки» составлен по документу «Вирусо-логия семантических-реакций» (SocioCyberneering Inc., версия 0.1v, 16 ноября 2026): это рабочие гипотезы, а не установленные факты. Проверяйте сами.',
        'Роман — художественное произведение, а не медицинский или психологический совет. Если вам тяжело, обратитесь к специалисту.',
        'VIDEOLIST',
    ]
    for t in extra:
        out.append(videolist() if t == 'VIDEOLIST' else (inline(t) + '\n'))
    return '\n'.join(out)

THANKS = r"""
\storypartT{Благодарности}

\begin{center}
{\disp\bfseries\fontsize{12}{15}\selectfont Михаилу Короткову --- и так далее.\par}
\end{center}

\medskip
\noindent Это не фигура вежливости и не способ сократить список. Это тот самый приём из этой книги, и здесь он стоит на своём месте.

\medskip\noindent\textbf{Михаилу Короткову} --- за переводы на русский язык работ по общей семантике. Перевести такой текст --- не то же самое, что перевести слова. У Коржибски термины держатся не на значении, а на структуре: дефисы в «семантических-реакциях» стоят не для красоты, «не есть» --- не стилистическая неловкость, а утверждение, и переводчик, который «причешет» это до гладкого русского, уничтожит ровно то, ради чего текст написан. Сохранить неудобство оригинала --- отдельная работа, которую читатель замечает в последнюю очередь, а чаще не замечает вовсе.

Без этой работы автор этой книги читал бы Коржибски в пересказе пересказа --- и написал бы ровно ту главу, которую Мерсер слушал в кабинете профессора, только изнутри, не заметив.

\medskip\noindent\textbf{И так далее} --- всем остальным, кто переводил, редактировал, сверял термины и выкладывал эти тексты в открытый доступ. Автор честно не знает их имён. Не потому, что они неважны, а потому, что он не проделал работу по их установлению, и приписывать себе эту работу он не станет: книга про проверку не имеет права врать на последней странице.

Поэтому здесь стоит «и так далее» --- в точном значении Коржибски: \textit{карта неполна, список открыт, продолжение существует и мне неизвестно}.

\medskip\noindent\textbf{Как это исправить.} Если вы знаете, кто ещё переводил или издавал общую семантику на русском, --- напишите. Имя встанет в этот список в следующей редакции. Лицензия на предыдущих страницах позволяет вам и просто дописать его самостоятельно: это не нарушение, это ровно то, для чего книга открыта.

\medskip\noindent Благодарность также:
\begin{itemize}\setlength{\itemsep}{0pt}
\item Альфреду Коржибски --- за метод, из-за которого эту книгу было тяжело писать честно;
\item Брюсу и Сьюзан Кодиш --- за биографию и за практическое руководство, по которым сверялись факты;
\item Сэмюэлу Хаякаве и Уэнделлу Джонсону --- за то, что сделали эти идеи читаемыми;
\item тем, кто выложил записи семинаров в сеть, --- без них у книги не было бы голоса Коржибски;
\item и читателю, который дойдёт до списка источников и проверит хотя бы один пункт. Таких немного. Эта книга написана ради них.
\end{itemize}

\bigskip
\begin{center}
{\color{accent}\rule{17mm}{0.6pt}}\par
\vspace{2.5mm}
{\disp\bfseries\fontsize{10.5}{13}\selectfont Куда писать\par}
\end{center}

\medskip\noindent Если вы знаете имя переводчика, которого здесь нет; если нашли ошибку в датах, фактах или схемах; если хотите переделать книгу под себя и хотите сказать об этом --- вот адреса.

\begin{itemize}\setlength{\itemsep}{1pt}
\item \textbf{Почта:} \href{mailto:sociocyber1@gmail.com}{sociocyber1@gmail.com} --- доходит точно, отвечаю медленно;
\item \textbf{Telegram:} @sc\_sinus --- \textit{с честной пометкой: аккаунты я меняю часто, так что ответа может не быть вовсе. Это не грубость, это смена аккаунта. По правилам этой книги: аккаунт\textsubscript{1} не есть аккаунт\textsubscript{2};}
\item \textbf{Matrix:} @cercell:4d2.org
\end{itemize}

\noindent Самый надёжный способ --- почта. Самый быстрый --- тот из трёх, который сегодня жив, и узнать это можно только опытом. Что, в общем, и есть основной метод этой книги.
\clearpage
"""

_PICRE = re.compile(r'\[\[PIC:([A-Za-z0-9_\\]+?)(!rot|!in)?\|([^\]]*)\]\]')
def _picsub(m):
    nm, mode, cap = m.group(1).replace('\\', ''), m.group(2) or '', m.group(3)
    if mode == '!rot':
        return '\\pageimgrot{img/%s.png}{%s}' % (nm, cap)
    if mode == '!in':
        return '\\inlineimg{img/%s.png}{0.52}{%s}' % (nm, cap)
    return '\\pageimg{img/%s.png}{%s}' % (nm, cap)
body = [_PICRE.sub(_picsub, b) for b in body]

FRONTISPIECE = r"""\clearpage\thispagestyle{empty}
\begin{center}\vspace*{\fill}
\includegraphics[width=0.94\textwidth,height=0.80\textheight,keepaspectratio]{img/p_mercer.png}\par
\vspace{4mm}
{\disp\fontsize{8}{10}\selectfont\addfontfeature{LetterSpace=30}АЛЕКС МЕРСЕР\par}
\vspace{1.5mm}
{\footnotesize\itshape В документах --- Джулиан Александр Мерсер, отсюда «J.~M.» на всех бумагах.\par}
\vspace*{\fill}\end{center}\clearpage
"""

main_tex = (PRE + titlepage(esc(TITLE), SUBTITLE, esc(NOTE)).replace('\\frontmatter\n', '', 1).replace('\\begin{document}\n', '\\begin{document}\n\\frontmatter\n' + COVER, 1) +
            FRONTISPIECE + LICPAGE + MANIFESTO + '\\tableofcontents\n' + PREFACE + '\\mainmatter\n' + '\n'.join(body) +
            '\n\\backmatter\n' + THANKS + hist_note() + '\n\\end{document}\n')
open(os.path.join(OUT, 'Karta_ne_est_territoriya_v28.tex'), 'w', encoding='utf-8').write(main_tex)

# ---------------------------------------------------------------- superseded drafts file
sbody = []
for p in sup_parts:
    sbody.append('\n%% ------------------------------------------------ source lines %d-%d' % (p['s'] + 1, p['end']))
    sbody.append(part_header(p))
    sbody.append(emit_body(p['s'] + 1, p['end']))
sup_tex = (PRE.replace('Карта не есть территория}', 'Заменённые версии}') +
           titlepage('Заменённые версии', 'Черновики из чата, которые были переписаны по вашим замечаниям',
                     'Не входят в основную рукопись') +
           '\\tableofcontents\n\\mainmatter\n' + '\n'.join(sbody) + '\n\\end{document}\n')
open(os.path.join(OUT, 'superseded_drafts.tex'), 'w', encoding='utf-8').write(sup_tex)

# ---------------------------------------------------------------- removal log
with open(os.path.join(OUT, 'chat_fragments_removed.txt'), 'w', encoding='utf-8') as f:
    f.write('Фрагменты чата, не вошедшие в рукопись (номера строк исходного Merser.txt)\n\n')
    f.write('[начало файла, строки 1-50: вступление чата и пробная сцена; вошли только подзаголовок и примечание]\n')
    for j in range(0, 50):
        if L[j].strip():
            f.write('%d: %s\n' % (j + 1, L[j][:200]))
    for name, tail in log:
        f.write('\n[после части «%s»]\n' % name)
        for no, t in tail:
            f.write('%d: %s\n' % (no, t[:200]))

# ---------------------------------------------------------------- report
print('parts total:', len(parts), ' main:', len(main_parts), ' superseded:', len(sup_parts))
print('parts WITHOUT trigger (story runs to next heading):')
for p in parts:
    if p['trig'] is None:
        print('  ', p['s'] + 1, p['label'], p['title'][:40])
print('stray asterisks:', len(stray), stray[:5])
bad = re.compile(r'Продолжай|Продолжи\b|Далее\b|Историческая основа|Художественн|Сократи|Напиши|ChatGPT|Усилить|Продолжение следует')
n = 0
for p in parts:
    for j in range(p['s'], p['end']):
        if bad.search(L[j]):
            n += 1
            print('SUSPICIOUS', j + 1, L[j][:120])
print('suspicious kept lines:', n)
kept = sum(len(L[j].split()) for p in main_parts for j in range(p['s'], p['end']))
print('words in main book (approx):', kept)
