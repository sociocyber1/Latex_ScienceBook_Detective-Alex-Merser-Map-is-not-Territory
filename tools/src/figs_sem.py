# -*- coding: utf-8 -*-
# Схемы к циклу «Семинар 1937» — в духе рисунков самих лекций.
FIGS = {}
DOCS = {}

FIGS['eval'] = (r'''\begin{tikzpicture}[node distance=7mm,bx/.style={box,text width=24mm}]
\node[bx] (a) {«нравится»};
\node[bx,below=3mm of a] (b) {«не нравится»};
\node[bx,below=3mm of b] (c) {«страх»};
\node[bx,below=3mm of c] (d) {«голод»};
\node[box,right=16mm of b,text width=26mm,minimum height=16mm,fill=black!6] (e) {\textbf{ОЦЕНКА}};
\node[bx,right=14mm of e,yshift=6mm] (f) {следующий поступок};
\node[bx,right=14mm of e,yshift=-10mm] (g) {следующее слово};
\foreach \n in {a,b,c,d} {\draw[arr] (\n.east) -- ++(3mm,0) |- (e.west);}
\draw[arr] (e.east) -- ++(3mm,0) |- (f.west);
\draw[arr] (e.east) -- ++(3mm,0) |- (g.west);
\node[grp] at ($(b.north)+(0,14mm)$) {[Старые слова]};
\node[grp] at ($(e.north)+(0,5mm)$) {[Научный термин]};
\node[grp] at ($(f.north)+(0,5mm)$) {[Что из этого выходит]};
\end{tikzpicture}''', 'Один термин вместо четырёх: всё, что мы называем чувствами, профессор переводит в оценку')

FIGS['mapord'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
\node[anchor=east,font=\footnotesize\bfseries] at (-0.3,1.6) {ТЕРРИТОРИЯ:};
\node[anchor=east,font=\footnotesize\bfseries] at (-0.3,0.4) {КАРТА:};
\draw[arr] (-0.1,1.6)--(7.3,1.6); \draw[arr] (-0.1,0.4)--(7.3,0.4);
\foreach \x/\t in {0.6/{С.-Ф.},3.4/{Ч.},6.2/{Н.-Й.}} {\node[box,minimum width=18mm] at (\x,1.6) {\t};}
\foreach \x/\t in {0.6/{Ч.},3.4/{С.-Ф.},6.2/{Н.-Й.}} {\node[box,minimum width=18mm,fill=black!6] at (\x,0.4) {\t};}
\node[font=\scriptsize,anchor=west,text width=52mm] at (7.6,1.0) {Порядок городов на карте не совпадает с порядком на местности. Прогноза такая карта не даёт.};
\node[font=\scriptsize,align=left,anchor=north west] at (-1.6,-0.5) {\textbf{ТРИ ПОЛОЖЕНИЯ}};
\node[font=\scriptsize,align=left,anchor=north west,text width=100mm] at (-1.6,-1.0) {1. Карта \textbf{не есть} территория.\\2. Карта охватывает \textbf{не всю} территорию.\\3. Карта \textbf{само-рефлексивна}: на карте есть карта.};
\end{tikzpicture}''', 'Доска профессора: та самая карта, на которой Сан-Франциско стоит между Чикаго и Нью-Йорком')

FIGS['chain'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\foreach \i in {1,...,6} {\draw[line width=0.7pt] (\i*1.5,1.6) ellipse [x radius=0.52,y radius=0.3];}
\node[font=\scriptsize,anchor=east] at (1.0,1.6) {цепь:};
\foreach \i in {1,...,6} {\node[font=\footnotesize] at (\i*1.5,0.5) {\i};}
\node[font=\scriptsize,anchor=east] at (1.0,0.5) {язык:};
\draw[arr] (1.2,0.5)--(9.6,0.5);
\draw[dashed,line width=0.3pt] (3.0,1.3)--(3.0,0.75);
\node[draw,rounded corners=2pt,fill=yellow!14,font=\scriptsize,text width=62mm,align=center] at (5.2,-0.7)
 {Прогноз, сделанный \emph{до} того, как посмотрели: «звено 2 лежит между 1 и 3». Смотрим --- так и есть.};
\node[font=\scriptsize,anchor=west,text width=40mm] at (10.0,1.1) {порядок в вещи и порядок в словах совпали --- отсюда прогноз};
\end{tikzpicture}''', 'Цепь и счёт: вся наука держится на том, что порядок слов повторяет порядок вещей')

FIGS['intext'] = (r'''\begin{tikzpicture}[node distance=8mm,bx/.style={box,text width=30mm}]
\node[box,text width=20mm,fill=black!6] (f) {\textbf{ФАКТЫ}};
\node[bx,above right=6mm and 18mm of f] (i) {\textbf{INT}: определение по свойствам\\«беспёрое двуногое»};
\node[bx,below right=6mm and 18mm of f] (e) {\textbf{EXT}: показать индивидуумов\\Смит$_1$, Смит$_2$, Смит$_3$\dots};
\draw[arr] (f)--(i); \draw[arr] (f)--(e);
\node[bx,right=16mm of i,fill=black!4] (i2) {охвачен \emph{никто}};
\node[bx,right=16mm of e,fill=black!4] (e2) {охвачен \emph{каждый}};
\draw[arr] (i)--(i2); \draw[arr] (e)--(e2);
\node[font=\scriptsize,text width=92mm,align=center,below=9mm of e] {«Автомобили полезны» $\to$ автомобиль$_1$, автомобиль$_2$\dots $\to$ видны неисправные тормоза и пьяные водители $\to$ «вы высказались слишком широко».};
\end{tikzpicture}''', 'Два пути от одних и тех же фактов: по определению и по индивидуумам')

FIGS['canal'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=0.9pt] (0.4,2.4) -- (8.0,2.4); \draw[line width=0.9pt] (0.4,1.8) -- (8.0,1.8);
\node[font=\footnotesize,anchor=east] at (0.2,2.1) {ткань A};
\draw[line width=0.4pt] (0.4,0.9) -- (3.4,0.9); \draw[line width=0.4pt] (0.4,0.5) -- (3.4,0.5);
\node[font=\footnotesize,anchor=east] at (0.2,0.7) {ткань X};
\draw[arr,line width=0.8pt] (0.8,2.1) -- (7.6,2.1) node[midway,above,font=\scriptsize]{импульс A$'$};
\draw[arr,line width=0.8pt] (0.8,0.7) -- (2.6,0.7);
\draw[arr,line width=0.8pt,dashed] (2.6,0.7) .. controls (3.6,0.75) and (3.8,1.6) .. (4.4,2.05)
  node[pos=0.6,right,font=\scriptsize,text width=34mm]{импульс X$'$ сворачивает в проторённую ткань};
\node[font=\scriptsize,text width=96mm,align=center] at (4.2,-0.4) {Так образуется привычка. Так же трудно её переделать: новая мысль каждый раз сворачивает в старое русло.};
\end{tikzpicture}''', 'Канализация, она же «проторение»: импульс идёт туда, где уже ходили')

FIGS['happy'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm,bx/.style={box,text width=31mm}]
\node[box,text width=16mm,fill=black!8] (f) at (5.0,3.4) {\textbf{ФАКТЫ}};
\node[bx] (e1) at (0.9,5.0) {\textbf{E$_1$} ждать максимум};
\node[bx] (e2) at (0.9,3.0) {\textbf{E$_2$} ждать минимум \emph{без} горького опыта};
\node[bx] (e3) at (0.9,1.0) {\textbf{E$_3$} ждать минимум \emph{после} горького опыта};
\node[bx] (r1) at (9.2,5.0) {разочарование, цинизм, придирки};
\node[bx] (r2) at (9.2,3.0) {«вышло лучше, чем я ждал»: интерес, надежда};
\node[bx] (r3) at (9.2,1.0) {обида, мстительность, недоверие};
\foreach \a/\b in {e1/r1,e2/r2,e3/r3} {\draw[arr] (\a)--(\b);}
\draw[arr,dashed] (f)--(e1.east); \draw[arr,dashed] (f)--(e2.east); \draw[arr,dashed] (f)--(e3.east);
\node[font=\scriptsize,anchor=north,text width=70mm,align=center] at (5.0,0.2) {Факты в трёх строках одни и те же. Разное --- только то, чего человек ждал заранее.};
\end{tikzpicture}''', 'Экстенсиональная теория счастья: одни и те же факты и три разных ожидания')

FIGS['fan'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}[shift={(0,0)}]
\foreach \a in {0,90,180,270} {\draw[line width=0.6pt,fill=black!8] (\a:0.25) -- (\a+12:1.9) -- (\a-12:1.9) -- cycle;}
\fill (0,0) circle (2pt);
\node[font=\scriptsize,anchor=north] at (0,-2.3) {что есть: четыре лопасти};
\end{scope}
\draw[arr,line width=0.7pt] (2.6,0) -- (4.4,0) node[midway,above,font=\scriptsize]{раскрутить};
\begin{scope}[shift={(7.0,0)}]
\shade[inner color=black!18,outer color=black!6] (0,0) circle (1.9);
\draw[line width=0.6pt] (0,0) circle (1.9);
\node[font=\scriptsize,anchor=north] at (0,-2.3) {что видно: сплошной диск};
\end{scope}
\node[font=\scriptsize,text width=100mm,align=center] at (3.5,-3.2) {Диска нет нигде, кроме как у меня в голове. Так же устроены «твёрдые» вещи: процесс внизу, объект наверху.};
\end{tikzpicture}''', 'Вентилятор профессора: объект --- это то, что нервная система делает из процесса')

FIGS['twoval'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\begin{scope}
\draw[line width=0.6pt,fill=black!5] (0,0) circle (0.9); \node[font=\small] at (0,0) {A};
\draw[line width=0.6pt,fill=black!5] (2.0,0) circle (0.9); \node[font=\small] at (2.0,0) {B};
\node[font=\scriptsize,anchor=north,text width=42mm,align=center] at (1.0,-1.3) {\textbf{Дву-значно:} соприкасаются или нет. Третьего не дано.};
\end{scope}
\begin{scope}[shift={(7.4,0)}]
\foreach \r/\o in {0.9/0, 0.9/2.0} {\draw[line width=0.4pt,dashed] (\o,0) circle (\r);}
\foreach \x in {-0.7,-0.3,0.1,0.5,0.9,1.3,1.7,2.1,2.5} {\foreach \y in {-0.5,-0.1,0.3,0.7} {\fill[black!55] (\x+0.08*\y,\y) circle (0.7pt);}}
\node[font=\scriptsize,anchor=north,text width=50mm,align=center] at (1.0,-1.3) {\textbf{Бесконечно-значно:} два процесса соприкасаются в бесконечном числе степеней.};
\end{scope}
\end{tikzpicture}''', '«Либо-либо» как частный случай: у процессов нет границы, у определений есть')

FIGS['isfour'] = (r'''\begin{tikzpicture}[node distance=6mm,bx/.style={box,text width=36mm,align=left}]
\node[bx] (a) {\textbf{1. вспомогательное}\\«идёт дождь»};
\node[bx,right=10mm of a] (b) {\textbf{2. существования}\\«есть такое правило»};
\node[bx,below=7mm of a,fill=black!8] (c) {\textbf{3. предикации}\\«роза \emph{есть} красная»};
\node[bx,right=10mm of c,fill=black!8] (d) {\textbf{4. тождества}\\«роза \emph{есть} цветок»};
\node[box,below=8mm of c,text width=80mm,fill=white] (n) {Третье и четвёртое всегда ложны по фактам: красного нет в розе, оно в нервной системе; характеристики цветка не равны характеристикам розы$_1$};
\draw[arr] (c)--(n); \draw[arr] (d)--(n);
\node[grp,anchor=west] at ($(a.north west)+(0,4mm)$) {[Четыре разных «есть» --- одно слово]};
\end{tikzpicture}''', 'Четыре «есть», которые мы пишем одинаково; два последних всегда лгут')

FIGS['pavlov'] = (r'''\begin{tikzpicture}[node distance=8mm,bx/.style={box,text width=26mm}]
\node[bx] (a) {звонок};
\node[bx,right=of a] (b) {слюна};
\node[bx,right=of b,fill=black!6] (c) {пищи нет};
\draw[arr] (a)--(b); \draw[arr] (b)--(c);
\node[grp] at ($(b.north)+(0,5mm)$) {[Собака: сигнальная реакция]};
\node[bx,below=14mm of a] (d) {звонок};
\node[bx,right=of d] (e) {пауза: что это значит? когда? кто звонил?};
\node[bx,right=of e] (f) {ответ по фактам};
\draw[arr] (d)--(e); \draw[arr] (e)--(f);
\node[grp] at ($(e.north)+(0,7mm)$) {[Человек: символьная реакция]};
\node[font=\scriptsize,text width=98mm,align=center,below=8mm of e] {Разница не в том, что реакции нет, а в её \emph{степени условности}: между звонком и слюной человек успевает вставить вопрос.};
\end{tikzpicture}''', 'Сигнальная реакция и символьная: вся разница в задержке')

FIGS['natord'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm,st/.style={box,text width=62mm}]
\node[st] (a) at (0,4.8) {\textbf{1. Физико-химический процесс} --- то, что происходит};
\node[st] (b) at (0.7,3.6) {\textbf{2. Объект} --- то, что из него построила нервная система};
\node[st] (c) at (1.4,2.4) {\textbf{3. Описание} --- то, что я записал};
\node[st] (d) at (2.1,1.2) {\textbf{4. Вывод низкого порядка}};
\node[st] (e) at (2.8,0.0) {\textbf{5. Вывод высокого порядка, и т. д.}};
\foreach \x/\y in {a/b,b/c,c/d,d/e} {\draw[arr] (\x.south) -- (\y.north);}
\draw[-{Latex[length=2mm]},line width=0.5pt] (-3.6,5.2) -- (-3.6,-0.4);
\node[font=\scriptsize,rotate=90,anchor=south] at (-3.9,2.4) {надёжность убывает};
\node[font=\scriptsize,text width=52mm,anchor=west,align=left] at (4.2,3.0) {Так идёт \textbf{естественный} порядок.\\[2mm] В жизни мы его \textbf{обращаем}: сначала вывод, потом описание, а до процесса не доходим вовсе.};
\end{tikzpicture}''', 'Естественный порядок оценки: что важнее чего, и в какую сторону мы его обычно переворачиваем')

FIGS['flatpi'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=0.7pt] (0,0) circle (2.6);
\draw[line width=0.4pt,dashed] (0,0) circle (1.3);
\draw[line width=0.5pt] (0,0) -- (55:2.6) node[midway,above,font=\scriptsize,sloped]{R (по шару)};
\draw[line width=0.5pt] (0,0) -- (-35:1.3) node[midway,below,font=\scriptsize,sloped]{r (по плоскости)};
\fill (0,0) circle (1.5pt);
\node[font=\scriptsize,anchor=west,text width=58mm] at (3.2,0.8) {Плоское существо чертит окружность C и меряет радиус. Делит одно на другое.};
\node[font=\scriptsize,anchor=west,text width=58mm] at (3.2,-0.8) {Получает $\pi$ меньше школьного --- и узнаёт, что у мира есть измерение, которого оно не видит.};
\node[font=\scriptsize] at (0,-3.1) {поверхность шара};
\end{tikzpicture}''', 'Как измерением находят измерение: опыт, который двумерный житель может поставить сам')

FIGS['orders'] = (r'''\begin{tikzpicture}[node distance=9mm,bx/.style={box,text width=34mm}]
\node[bx] (h1) {\textbf{Ненависть$_1$}\\к человеку};
\node[bx,right=18mm of h1,fill=black!6] (h2) {\textbf{Ненависть$_2$}\\к самой ненависти};
\draw[arr] (h1)--(h2) node[midway,above,font=\scriptsize]{шаг вверх};
\node[bx,below=8mm of h1] (d1) {\textbf{Сомнение$_1$}\\в чужих словах};
\node[bx,right=18mm of d1,fill=black!6] (d2) {\textbf{Сомнение$_2$}\\в собственном сомнении};
\draw[arr] (d1)--(d2) node[midway,above,font=\scriptsize]{шаг вверх};
\node[bx,below=8mm of d1] (w1) {\textbf{Тревога$_1$}\\о деле};
\node[bx,right=18mm of w1] (w2) {\textbf{Тревога$_2$}\\о собственной тревоге};
\draw[arr] (w1)--(w2) node[midway,above,font=\scriptsize]{шаг вниз};
\node[font=\scriptsize,text width=46mm,anchor=west,align=left] at (7.6,0) {Первые два шага гасят механизм первого порядка. Третий --- раскручивает его. Разница и есть всё дело.};
\end{tikzpicture}''', 'Механизмы второго порядка: одни гасят, другой раскручивает')

FIGS['fido'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=0.6pt] (-2.4,5.4) .. controls (-1.7,3.2) and (-0.9,2.8) .. (0,2.8) .. controls (0.9,2.8) and (1.7,3.2) .. (2.4,5.4);
\draw[line width=0.5pt,decorate,decoration={zigzag,segment length=5pt,amplitude=2pt}] (-2.4,5.4) -- (2.4,5.4);
\foreach \x/\y in {-1.5/4.4,-0.8/3.6,0.0/4.2,0.8/3.5,1.5/4.5,-0.4/5.0,0.9/4.9} {\fill (\x,\y) circle (1pt);}
\node[font=\scriptsize] at (0,5.9) {СОБЫТИЕ};
\draw[line width=0.5pt,fill=white] (-3.4,1.6) circle (0.65); \node[font=\scriptsize,anchor=east] at (-4.2,1.6) {Файдо};
\draw[line width=0.5pt,fill=white] (0,1.6) circle (0.75); \node[font=\scriptsize,anchor=west] at (0.95,1.6) {человек};
\foreach \sx in {-1.0,0,1.0} {\draw[line width=0.3pt] (\sx*0.6,2.85) -- (0,2.35);}
\draw[line width=0.3pt] (-1.9,3.3) -- (-3.4,2.25);
\foreach \y in {0.2,-0.9,-2.0} {\draw[line width=0.45pt,fill=white] (-0.9,\y-0.3) rectangle (0.9,\y+0.3);}
\draw[line width=0.3pt] (0,0.85)--(0,0.5); \draw[line width=0.3pt] (0,-0.1)--(0,-0.6); \draw[line width=0.3pt] (0,-1.2)--(0,-1.7);
\node[font=\scriptsize,anchor=west] at (1.2,0.2) {слово};
\node[font=\scriptsize,anchor=west] at (1.2,-0.9) {вывод};
\node[font=\scriptsize,anchor=west] at (1.2,-2.0) {и так далее};
\node[font=\scriptsize,align=center,text width=30mm] at (-3.4,0.3) {у собаки отсюда вниз ничего не идёт};
\node[font=\scriptsize,text width=92mm,align=center] at (-0.5,-3.2) {Собака абстрагирует и останавливается. Человек идёт дальше вниз --- и в этом же его беда: он может принять нижнюю бирку за верхнюю чашу.};
\end{tikzpicture}''', 'Мир животного и мир человека на одном приборе')

FIGS['worm'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm]
\draw[line width=0.8pt] (0,0) -- (4.0,0); \draw[line width=0.8pt] (0,0.9) -- (4.0,0.9);
\draw[line width=0.8pt] (4.0,0.9) -- (4.0,2.6); \draw[line width=0.8pt] (4.9,0.9) -- (4.9,2.6);
\draw[line width=0.8pt] (4.0,0) -- (4.0,-1.7); \draw[line width=0.8pt] (4.9,0) -- (4.9,-1.7);
\draw[line width=0.8pt] (4.9,0) -- (4.9,0.9);
\node[box,font=\scriptsize,fill=black!10] at (4.45,2.3) {E};
\node[box,font=\scriptsize,fill=black!4] at (4.45,-1.4) {S};
\node[font=\scriptsize,anchor=west,text width=34mm] at (5.4,2.3) {электрический мост: удар};
\node[font=\scriptsize,anchor=west,text width=34mm] at (5.4,-1.4) {наждачная бумага: предупреждение};
\draw[arr,line width=0.6pt] (0.4,0.45) -- (3.6,0.45);
\node[font=\scriptsize] at (1.9,0.78) {червь};
\node[font=\scriptsize,text width=96mm,align=center] at (3.0,-2.6) {Восемьдесят уроков --- и червь поворачивает правильно. Отрежьте ему голову: он всё равно повернёт правильно, только медленнее.};
\end{tikzpicture}''', 'Т-образный лабиринт: урок, который хранится не только в голове')
