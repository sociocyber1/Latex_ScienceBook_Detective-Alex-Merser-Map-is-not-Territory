# -*- coding: utf-8 -*-
FIGS = {}
DOCS = {}

FIGS['post3'] = (r'''\begin{tikzpicture}[node distance=7mm,p/.style={box,text width=40mm,minimum height=16mm}]
\node[p] (a) {\textbf{1. Карта — не территория}\\слово и описание не равны тому, что они описывают};
\node[p,right=of a] (b) {\textbf{2. Карта не охватывает всей территории}\\всегда есть то, что я не упомянул};
\node[p,right=of b] (c) {\textbf{3. Карта самоотражающа}\\я могу описать своё описание, и так далее};
\node[soft,below=9mm of b,text width=60mm] (m) {Мерсер: «Запись “он злой” — это уровень 1 или уровень 3?»};
\draw[arr] (a)--(m); \draw[arr] (b)--(m); \draw[arr] (c)--(m);
\node[grp] at ($(b.north)+(0,4mm)$) {[Три положения — как я их записал]};
\node[soft,below=6mm of m,text width=72mm,dashed] {1937 год: «мир — война — свобода» --- этого пункта в моих записях нет (см. текст)};
\end{tikzpicture}''', 'Три положения общей семантики в записи Мерсера')

FIGS['sherlock'] = (r'''\begin{tikzpicture}[node distance=7mm,bx/.style={box,text width=29mm}]
\node[grp,anchor=west] at (0,3.2) {[Метод «Шерлока»]};
\node[bx] (s1) at (1.6,2.0) {Видит след};
\node[bx] (s2) at (5.6,2.0) {Первая пришедшая версия};
\node[bx] (s3) at (9.6,2.0) {«Очевидно!»};
\node[bx] (s4) at (13.6,2.0) {Арест};
\draw[arr] (s1)--(s2); \draw[arr] (s2)--(s3); \draw[arr] (s3)--(s4);
\node[grp,anchor=west] at (0,0.7) {[Метод Мерсера]};
\node[bx] (m1) at (1.6,-0.5) {Записываю след и дату};
\node[bx] (m2) at (5.6,-0.5) {Не меньше трёх версий};
\node[bx] (m3) at (9.6,-0.5) {Что опровергнет каждую?};
\node[bx] (m4) at (13.6,-0.5) {Проверка, затем вывод};
\draw[arr] (m1)--(m2); \draw[arr] (m2)--(m3); \draw[arr] (m3)--(m4);
\draw[arr,dashed] (m4.south) -- ++(0,-6mm) -| (m2.south) node[pos=0.25,below,font=\scriptsize]{не сошлось --- возвращаюсь};
\end{tikzpicture}''', 'Два способа получить вывод: прыжок и лестница')

FIGS['feyn'] = (r'''\begin{tikzpicture}[node distance=10mm,bx/.style={box,text width=30mm}]
\node[bx] (a) {Догадка (гипотеза)};
\node[bx,right=of a] (b) {Следствия: «если так, то должно быть…»};
\node[bx,right=of b] (c) {Сверка с опытом};
\node[bx,right=of c,fill=black!6] (d) {Не сошлось --- гипотеза неверна};
\node[bx,below=9mm of c,dashed] (e) {Сошлось --- пока не опровергнута};
\draw[arr] (a)--(b); \draw[arr] (b)--(c); \draw[arr] (c)--(d); \draw[arr] (c)--(e);
\draw[arr,dashed] (d.north) -- ++(0,6mm) -| (a.north) node[pos=0.25,above,font=\scriptsize]{следующая догадка};
\node[font=\scriptsize\itshape,text width=60mm,below=2mm of e] {Не важно, чья догадка и насколько она красива.};
\end{tikzpicture}''', 'Цикл проверки гипотезы (пересказ мысли Ричарда Фейнмана)')

FIGS['sd2d'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,
 thr/.style={line width=0.3pt,black!85},
 lv/.style={font=\scriptsize,anchor=west,align=left,text width=44mm}]
\def\pt{15.2}\def\pb{10.9}
\def\parab{(-3.0,\pt) .. controls (-2.2,11.7) and (-1.1,\pb) .. (0,\pb) .. controls (1.1,\pb) and (2.2,11.7) .. (3.0,\pt)}
% --- СОБЫТИЕ
\begin{scope}
  \clip \parab -- cycle;
  \fill[black!3] (-3.2,10.6) rectangle (3.2,15.4);
  \foreach \yy in {11.1,11.6,12.1,12.6,13.1,13.6,14.1,14.6,15.0}
    \foreach \xx in {-2.8,-2.3,-1.8,-1.3,-0.8,-0.3,0.2,0.7,1.2,1.7,2.2,2.7}
      {\fill (\xx,\yy) circle (0.9pt);}
  \foreach \yy in {11.35,11.85,12.35,12.85,13.35,13.85,14.35,14.85}
    \foreach \xx in {-2.55,-2.05,-1.55,-1.05,-0.55,-0.05,0.45,0.95,1.45,1.95,2.45}
      {\fill (\xx,\yy) circle (0.9pt);}
\end{scope}
\draw[line width=0.5pt] \parab;
\draw[line width=0.5pt,decorate,decoration={zigzag,segment length=5pt,amplitude=2pt}] (-3.0,\pt) -- (3.0,\pt);
% нитки от события
\foreach \sx/\sy/\ex/\ey in {-1.45/11.42/-0.62/10.02, -0.95/11.08/-0.3/10.3, -0.5/10.94/-0.1/10.41,
   0.5/10.94/0.1/10.41, 0.95/11.08/0.3/10.3, 1.45/11.42/0.62/10.02}
  {\draw[thr] (\sx,\sy) -- (\ex,\ey);}
\foreach \sx/\sy/\ey in {-2.3/12.3/9.9, -1.9/11.85/9.6, 1.9/11.85/9.6, 2.3/12.3/9.9}
  {\draw[thr] (\sx,\sy) -- (\sx,\ey); \fill (\sx,\ey) circle (0.9pt);}
% --- ОБЪЕКТ
\begin{scope}\clip (0,9.3) circle (1.12);
  \fill[white] (-1.2,8.1) rectangle (1.2,10.5);
  \foreach \yy in {8.4,8.75,9.1,9.45,9.8}\foreach \xx in {-0.9,-0.55,-0.2,0.15,0.5,0.85}{\fill (\xx,\yy) circle (0.9pt);}
\end{scope}
\draw[line width=0.5pt] (0,9.3) circle (1.12);
% объект животного
\begin{scope}\clip (-4.3,9.3) circle (0.95);
  \fill[white] (-5.3,8.3) rectangle (-3.3,10.3);
  \foreach \yy in {8.6,8.95,9.3,9.65}\foreach \xx in {-5.0,-4.65,-4.3,-3.95,-3.6}{\fill (\xx,\yy) circle (0.9pt);}
\end{scope}
\draw[line width=0.5pt] (-4.3,9.3) circle (0.95);
\node[font=\scriptsize,align=center,text width=26mm] at (-4.3,7.7) {объект животного:\\нитки вниз не идут};
% --- ЯРЛЫКИ
\foreach \y in {6.9,5.4,3.9,2.4} {
  \begin{scope}
    \clip (-1.05,\y+0.58) -- (1.05,\y+0.58) -- (1.05,\y-0.48) -- (0.32,\y-0.48) -- (0,\y-0.1) -- (-0.32,\y-0.48) -- (-1.05,\y-0.48) -- cycle;
    \fill[white] (-1.2,\y-0.7) rectangle (1.2,\y+0.7);
    \foreach \yy in {-0.28,0.02,0.32}\foreach \xx in {-0.82,-0.49,-0.16,0.17,0.5,0.83}{\fill (\xx,\y+\yy) circle (0.85pt);}
  \end{scope}
  \draw[line width=0.5pt] (-1.05,\y+0.58) -- (1.05,\y+0.58) -- (1.05,\y-0.48) -- (0.32,\y-0.48) -- (0,\y-0.1) -- (-0.32,\y-0.48) -- (-1.05,\y-0.48) -- cycle;
}
\draw[thr] (0,8.18) -- (0,7.48);
\foreach \a/\b in {6.9/5.4,5.4/3.9,3.9/2.4} {\draw[thr] (0,\a-0.48) -- (0,\b+0.58);}
\foreach \y/\sx/\dx in {6.9/-1.05/-2.1, 5.4/1.05/2.1, 3.9/-1.05/-2.1}
  {\draw[thr] (\sx,\y+0.1) -- (\dx,\y-0.55); \fill (\dx,\y-0.55) circle (0.9pt);}
% --- обратная связь: ярлык снова становится событием
\draw[thr,dashed,-{Latex[length=2mm]}] (0,1.9) -- (0,1.05) -- (3.95,1.05) -- (3.95,13.0) -- (2.75,13.4);
% --- подписи уровней
\node[lv] at (4.5,14.4) {\textbf{I}~~СОБЫТИЕ в пространстве-времени. Уровень процесса};
\node[lv] at (4.5,11.3) {\textbf{II}~~Прямое воздействие события на нервную систему};
\node[lv] at (4.5,9.2) {\textbf{III}~~«Ощущение», «восприятие». УРОВЕНЬ ОБЪЕКТА};
\node[lv] at (4.5,6.9) {\textbf{IV}~~СЛОВЕСНЫЙ уровень. Описание};
\node[lv] at (4.5,5.4) {Уровень заключения 1};
\node[lv] at (4.5,3.9) {Уровень заключения 2};
\node[lv] at (4.5,2.4) {И так далее};
\node[font=\scriptsize,align=center,text width=86mm] at (0.3,0.1) {Пунктир: вывод сам становится событием --- его слышат, на него отвечают, и всё начинается заново};
\end{tikzpicture}""", 'Структурный дифференциал --- перерисовка схемы 7-1 из «Верните себе здравомыслие» Кодишей: событие, объект, ярлыки; свободные нитки --- то, что не вошло')

FIGS['sd3d'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,
 thr/.style={line width=0.3pt,black!85},
 pl/.style={draw,line width=0.4pt},
 lv/.style={font=\scriptsize,anchor=west,align=left,text width=34mm}]
% --- событие: чаша в изометрии
\def\parab{(-3.0,15.2) .. controls (-2.2,11.7) and (-1.1,10.9) .. (0,10.9) .. controls (1.1,10.9) and (2.2,11.7) .. (3.0,15.2)}
\begin{scope}\clip \parab -- cycle;
  \fill[black!5] (-3.2,10.6) rectangle (3.2,15.4);
  \foreach \yy in {11.2,11.7,12.2,12.7,13.2,13.7,14.2,14.7}
    \foreach \xx in {-2.7,-2.2,-1.7,-1.2,-0.7,-0.2,0.3,0.8,1.3,1.8,2.3,2.7}{\fill (\xx,\yy) circle (0.9pt);}
\end{scope}
\foreach \h/\rx/\ry in {14.2/2.58/0.86, 13.1/2.03/0.68, 12.2/1.48/0.49, 11.5/0.95/0.32}
  {\draw[black!30,line width=0.3pt] (0,\h) ellipse [x radius=\rx, y radius=\ry];}
\draw[line width=0.5pt] \parab;
\draw[line width=0.6pt,fill=black!2,fill opacity=0.3] (0,15.2) ellipse [x radius=3.0, y radius=1.0];
\draw[line width=0.5pt,decorate,decoration={zigzag,segment length=5pt,amplitude=1.6pt}] (-3.0,16.2) -- (3.0,16.2);
\node[font=\scriptsize,anchor=south] at (0,16.4) {край не закрыт: характеристик бесконечно много};
% нитки
\foreach \sx/\sy in {-1.3/11.25,-0.7/10.97,0.7/10.97,1.3/11.25} {\draw[thr] (\sx,\sy) -- (0,10.4);}
\foreach \sx/\sy/\ey in {-2.2/12.2/9.9, 2.2/12.2/9.9} {\draw[thr] (\sx,\sy) -- (\sx,\ey); \fill (\sx,\ey) circle (0.9pt);}
% --- объект: шар
\shade[ball color=black!12] (0,9.3) circle (1.05);
\draw[line width=0.4pt] (0,9.3) circle (1.05);
\shade[ball color=black!12] (-4.2,9.3) circle (0.85);
\draw[line width=0.4pt] (-4.2,9.3) circle (0.85);
\node[font=\scriptsize,align=center,text width=26mm] at (-4.2,7.9) {объект животного:\\ярлыков нет};
% --- ярлыки: плитки в изометрии
\foreach \y/\sx in {6.9/0, 5.4/0.22, 3.9/0.44, 2.4/0.66} {
  \filldraw[pl,fill=white] (\sx-0.95,\y-0.3) rectangle (\sx+0.95,\y+0.3);
  \filldraw[pl,fill=black!14] (\sx+0.95,\y-0.3) -- (\sx+1.25,\y-0.08) -- (\sx+1.25,\y+0.52) -- (\sx+0.95,\y+0.3) -- cycle;
  \filldraw[pl,fill=black!6] (\sx-0.95,\y+0.3) -- (\sx-0.65,\y+0.52) -- (\sx+1.25,\y+0.52) -- (\sx+0.95,\y+0.3) -- cycle;
  \foreach \xx in {-0.7,-0.35,0,0.35,0.7}{\fill[black!70] (\sx+\xx,\y) circle (0.7pt);}
}
\draw[thr] (0,8.25) -- (0,7.2);
\draw[thr] (0,6.6) -- (0.22,5.7); \draw[thr] (0.22,5.1) -- (0.44,4.2); \draw[thr] (0.44,3.6) -- (0.66,2.7);
\draw[thr,dashed,-{Latex[length=2mm]}] (0.66,2.1) -- (0.66,1.4) -- (4.2,1.4) -- (4.2,13.2) -- (2.8,13.6);
% --- подписи
\node[lv] at (5.4,14.6) {\textbf{I} Событие (процесс)};
\node[lv] at (5.4,11.2) {\textbf{II} Воздействие на нервную систему};
\node[lv] at (5.4,9.3) {\textbf{III} Объект};
\node[lv] at (5.4,6.9) {\textbf{IV} Слово, описание};
\node[lv] at (5.4,5.4) {Заключение 1};
\node[lv] at (5.4,3.9) {Заключение 2};
\node[lv] at (5.4,2.4) {И так далее};
\end{tikzpicture}""", 'Тот же прибор в изометрии: у чаши видна глубина, а плоский чертёж --- её вид сверху')

FIGS['unicorn'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,thr/.style={line width=0.35pt,black!85},
 tg/.style={draw,line width=0.45pt,fill=white,font=\scriptsize,minimum width=20mm,minimum height=6mm}]
% ---- слева: ЛОШАДЬ
\begin{scope}
\draw[line width=0.5pt] (-2.1,5.4) .. controls (-1.5,3.2) and (-0.7,2.8) .. (0,2.8) .. controls (0.7,2.8) and (1.5,3.2) .. (2.1,5.4);
\draw[line width=0.5pt,decorate,decoration={zigzag,segment length=4pt,amplitude=1.6pt}] (-2.1,5.4) -- (2.1,5.4);
\foreach \yy in {3.2,3.7,4.2,4.7,5.1}\foreach \xx in {-1.6,-1.1,-0.6,-0.1,0.4,0.9,1.4}{\fill (\xx,\yy) circle (0.8pt);}
\draw[line width=0.5pt,fill=white] (0,1.9) circle (0.6);
\foreach \xx in {-0.3,0,0.3}{\fill (\xx,1.9) circle (0.8pt);}
\draw[thr] (0,2.8)--(0,2.5);
\node[tg] (h) at (0,0.5) {ЛОШАДЬ};
\draw[thr] (0,1.3)--(0,0.8);
\node[font=\scriptsize,align=center,text width=40mm] at (0,-0.6) {нитка держится: есть объект, есть событие --- можно пойти и потрогать};
\end{scope}
% ---- справа: ЕДИНОРОГ
\begin{scope}[shift={(7.4,0)}]
\draw[line width=0.4pt,dashed,black!35] (-2.1,5.4) .. controls (-1.5,3.2) and (-0.7,2.8) .. (0,2.8) .. controls (0.7,2.8) and (1.5,3.2) .. (2.1,5.4);
\node[font=\scriptsize\itshape,black!55] at (0,4.3) {пусто};
\draw[line width=0.4pt,dashed,black!35] (0,1.9) circle (0.6);
\node[font=\scriptsize\itshape,black!55] at (0,1.9) {пусто};
\node[tg] (u) at (0,0.5) {ЕДИНОРОГ};
\draw[thr] (0,0.8) -- (0,1.55);
\fill (0,1.55) circle (1.1pt);
\node[font=\scriptsize,align=center,text width=42mm] at (0,-0.6) {ярлык есть, нитка обрывается: ни объекта, ни события --- трогать нечего};
\end{scope}
\end{tikzpicture}""", 'Два ярлыка одного вида: у одного нитка доходит до территории, у другого обрывается в воздухе')

FIGS['planecube'] = (r"""\begin{tikzpicture}[scale=0.92,font=\scriptsize]
% ---- слева: поверхность (лист)
\begin{scope}[shift={(0,0)}]
\filldraw[fill=black!4,line width=0.5pt] (0,0) rectangle (4.0,3.4);
\draw[-{Latex[length=1.6mm]},line width=0.45pt] (0,0) -- (4.3,0) node[right,font=\tiny]{дата};
\draw[-{Latex[length=1.6mm]},line width=0.45pt] (0,0) -- (0,3.7) node[above,font=\tiny]{уровень};
\fill (2.4,2.2) circle (2pt);
\node[font=\tiny,anchor=west] at (2.55,2.45) {запись};
\node[font=\tiny,anchor=north,text width=38mm,align=center] at (2.0,-0.35) {\textbf{поверхность}: два числа, и место найдено};
\end{scope}
% ---- стрелка
\draw[-{Latex[length=2mm]},line width=0.6pt] (5.0,1.7) -- (6.2,1.7) node[midway,above,font=\tiny]{$+1$};
% ---- справа: куб
\begin{scope}[shift={(7.0,0)}]
\def\dx{1.05}\def\dy{0.72}
\filldraw[fill=black!4,line width=0.5pt] (0,0) rectangle (3.4,3.0);
\filldraw[fill=black!10,line width=0.5pt] (0,3.0) -- (\dx,3.0+\dy) -- (3.4+\dx,3.0+\dy) -- (3.4,3.0) -- cycle;
\filldraw[fill=black!16,line width=0.5pt] (3.4,0) -- (3.4+\dx,\dy) -- (3.4+\dx,3.0+\dy) -- (3.4,3.0) -- cycle;
\draw[-{Latex[length=1.6mm]},line width=0.45pt] (0,0) -- (3.9,0) node[right,font=\tiny]{дата};
\draw[-{Latex[length=1.6mm]},line width=0.45pt] (0,0) -- (0,3.5) node[above,font=\tiny]{уровень};
\draw[-{Latex[length=1.6mm]},line width=0.45pt] (0,0) -- (1.35,0.93) node[right,font=\tiny,xshift=-2mm,fill=white,inner sep=1pt]{кто проверил};
\fill (2.0,2.0) circle (2pt);
\draw[dashed,line width=0.3pt] (2.0,2.0) -- (2.55,2.38); \fill (2.55,2.38) circle (2pt);
\node[font=\tiny,anchor=south,align=center,text width=34mm] at (2.1,3.95) {та же запись, но с источником};
\node[font=\tiny,anchor=north,text width=42mm,align=center] at (1.9,-0.35) {\textbf{объём}: три числа; поверхность --- это его стенка};
\end{scope}
\end{tikzpicture}""", 'Поверхность и объём: добавить измерение --- значит потребовать ещё одно число к каждой записи')

FIGS['shadow'] = (r"""\begin{tikzpicture}[scale=0.92,font=\scriptsize]
% ---- панель 1: свет сверху -> круг
\begin{scope}
\node[font=\tiny] at (1.5,4.5) {лампа сверху};
\draw[line width=0.4pt] (1.5,4.3) -- (1.5,3.95);
\foreach \a in {-30,-15,0,15,30} {\draw[line width=0.25pt,black!55] (1.5,3.95) -- ++(\a-90:2.0);}
\draw[line width=0.5pt,fill=black!6] (0.75,2.1) rectangle (2.25,3.3);
\draw[line width=0.5pt,fill=black!10] (1.5,3.3) ellipse [x radius=0.75,y radius=0.26];
\draw[line width=0.5pt] (1.5,2.1) ellipse [x radius=0.75,y radius=0.26];
\draw[line width=0.5pt] (-0.4,0.6) -- (3.4,0.6);
\filldraw[fill=black!35,draw=none] (1.5,0.6) ellipse [x radius=0.75,y radius=0.26];
\node[font=\tiny,anchor=north,text width=34mm,align=center] at (1.5,0.15) {тень --- круг};
\end{scope}
% ---- панель 2: свет сбоку -> прямоугольник
\begin{scope}[shift={(6.2,0)}]
\node[font=\tiny,anchor=east] at (-0.6,3.0) {лампа сбоку};
\foreach \y in {2.2,2.7,3.2} {\draw[line width=0.25pt,black!55,-{Latex[length=1.2mm]}] (-0.5,\y) -- (0.6,\y);}
\draw[line width=0.5pt,fill=black!6] (0.75,2.1) rectangle (2.25,3.3);
\draw[line width=0.5pt,fill=black!10] (1.5,3.3) ellipse [x radius=0.75,y radius=0.26];
\draw[line width=0.5pt] (1.5,2.1) ellipse [x radius=0.75,y radius=0.26];
\draw[line width=0.5pt] (3.5,0.9) -- (3.5,4.0);
\filldraw[fill=black!35,draw=none] (3.55,2.1) rectangle (3.95,3.3);
\node[font=\tiny,anchor=north,text width=36mm,align=center] at (2.6,0.6) {тень --- прямоугольник};
\end{scope}
\node[font=\tiny\itshape,text width=120mm,align=center] at (5.0,-0.65) {Один и тот же предмет. Обе тени правдивы. Ни по одной из них предмет не восстановить.};
\end{tikzpicture}""", 'Две тени одного цилиндра: проекция всегда теряет измерение')

FIGS['cube'] = (r'''\begin{tikzpicture}[x={(1cm,0cm)},y={(0cm,1cm)},z={(0.5cm,0.35cm)}]
\def\s{4.2}
\draw[fill=black!4] (0,0,0)--(\s,0,0)--(\s,\s,0)--(0,\s,0)--cycle;
\draw[fill=black!10] (0,\s,0)--(\s,\s,0)--(\s,\s,\s)--(0,\s,\s)--cycle;
\draw[fill=black!18] (\s,0,0)--(\s,\s,0)--(\s,\s,\s)--(\s,0,\s)--cycle;
\draw[arr,line width=0.8pt] (0,0,0)--(\s+1,0,0) node[right,font=\scriptsize]{\textbf{время}: дата};
\draw[arr,line width=0.8pt] (0,0,0)--(0,\s+1,0) node[font=\scriptsize,anchor=south east,xshift=9mm]{\textbf{уровень}: факт\,--\,вывод\,--\,оценка};
\draw[arr,line width=0.8pt] (0,0,0)--(0,0,\s+1.5) node[left,font=\scriptsize,xshift=-1mm]{\textbf{индекс}: кто, где};
\node[font=\scriptsize,align=center,fill=white,draw,inner sep=2pt] at (2.6,3.6,4.2) {«Он злой»\\(без даты, без индекса,\\уровень: оценка)};
\fill (0.9,0.5,0) circle (1.6pt);
\node[font=\tiny,align=left,fill=white,inner sep=1.5pt,anchor=south west] at (1.75,0.12,0) {«ключ на столе,\\22.02, 21:10, видел сам»};
\draw[line width=0.3pt] (1.7,0.42,0) -- (0.98,0.52,0);
\end{tikzpicture}''', 'Куб карты: любая моя запись --- точка внутри куба. Чем ближе к началу осей, тем меньше в ней выдумки')

FIGS['weather'] = (r'''\begin{tikzpicture}[node distance=9mm,bx/.style={box,text width=30mm}]
\node[bx] (w1) {Дождь, серый свет};
\node[bx,right=of w1] (m1) {Мерсер видит: мрак, боль, подвох};
\node[bx,right=of m1] (o1) {Слова людей читаются «по-серому»};
\node[bx,below=10mm of w1] (w2) {Солнце, тёплый день};
\node[bx,right=of w2] (m2) {Мерсер видит: добро, шанс, «всё образуется»};
\node[bx,right=of m2] (o2) {Слова читаются «по-золотому»};
\draw[arr] (w1)--(m1); \draw[arr] (m1)--(o1); \draw[arr] (w2)--(m2); \draw[arr] (m2)--(o2);
\node[soft,text width=95mm,below=7mm of m2] {Правило: прежде чем записать «он лжёт», запиши --- какая сегодня погода у меня внутри. Над облаками всё равно светит солнце (если бы я умел летать, я бы проверил).};
\end{tikzpicture}''', 'Среда, настроение и чтение чужих слов')

FIGS['forecast'] = (r'''\begin{tikzpicture}
\draw[arr] (0,0)--(10.5,0) node[right,font=\scriptsize]{даты}; \draw[arr] (0,0)--(0,5) node[above,font=\scriptsize]{измерение};
\foreach \x/\y in {1/1.0,2/1.5,3/1.9,4/2.2,5/2.8} {\fill (\x,\y) circle (2pt);}
\draw[thick] (1,1.0)--(5,2.8);
\draw[thick,dashed] (5,2.8)--(9.5,4.6) node[right,font=\scriptsize,text width=24mm]{прогноз: линия продолжится};
\draw[dashed] (5,2.8)--(9.5,2.2) node[right,font=\scriptsize,text width=24mm]{или упрётся в потолок};
\node[draw,rounded corners=2pt,fill=yellow!12,font=\scriptsize,text width=40mm,align=center] at (3.0,4.3) {Проверочная дата: 12 февраля\\что должно быть, если прогноз верен?};
\draw[arr,dotted] (3.0,3.8)--(5.2,3.0);
\end{tikzpicture}''', 'Прогноз по карте: точки измерены, линия --- предположение, проверка назначена на дату')

FIGS['chair'] = (r'''\begin{tikzpicture}[node distance=8mm,bx/.style={box,text width=31mm}]
\node[bx] (a) {Стул летит};
\node[bx,right=of a] (b) {Сначала --- расстояние и дверь};
\node[bx,right=of b] (c) {Пауза: одно спокойное предложение};
\node[bx,below=8mm of c] (d) {Не спорить о «правоте»};
\node[bx,left=of d] (e) {Назвать факт: «вы кричите, стулья в воздухе»};
\node[bx,left=of e] (f) {Предложить действие: вода, сесть, говорить завтра};
\draw[arr] (a)--(b); \draw[arr] (b)--(c); \draw[arr] (c)--(d); \draw[arr] (d)--(e); \draw[arr] (e)--(f);
\node[font=\scriptsize\itshape,text width=100mm,below=3mm of e] {Проверка любой реплики: можно ли её подтвердить глазами?};
\end{tikzpicture}''', 'Порядок действий, когда на тебя кидают стулья (сначала безопасность, потом семантика)')

FIGS['alice'] = (r'''\begin{tikzpicture}[node distance=8mm,bx/.style={box,text width=29mm}]
\node[bx] (a) {Алиса: кролик с часами};
\node[bx,right=of a] (b) {Нео: красная таблетка};
\node[bx,right=of b] (c) {Мерсер: красная таблетка, но с датой и индексом};
\node[bx,below=8mm of b] (d) {Лестница вниз: вывод $\to$ оценка $\to$ факт};
\node[bx,right=of d] (e) {Лестница вверх: факт $\to$ \dots};
\draw[arr] (a)--(b); \draw[arr] (b)--(c); \draw[arr] (c)--(e); \draw[arr] (d)--(b);
\end{tikzpicture}''', 'Карта сна Алекса: каждый уровень заменяет предыдущую декорацию (и жалобы автору)')

FIGS['bonus'] = (r"""\begin{tikzpicture}[node distance=9mm,bx/.style={box,text width=31mm}]
\node[bx] (a) {Приложение 17-Б\\в журнале: номер на полях};
\node[bx,right=of a,dashed] (b) {В папках и в описи: листа нет};
\node[bx,right=of b,fill=black!8] (c) {Сложен вчетверо и вклеен в корешок журнала R-6};
\draw[arr] (a)--(b); \draw[arr,dashed] (b)--(c);
\node[font=\scriptsize\itshape,text width=80mm,below=6mm of b] {Разница толщины корешков: R-5 --- 34 мм, R-7 --- 33 мм, R-8 --- 34 мм, \textbf{R-6 --- 41 мм}.};
\end{tikzpicture}""", 'Где всё это время лежало приложение 17-Б')

DOCS['roster'] = r"""\begin{docbox}{Приложение 17-Б · График дежурств по архиву, февраль--март 1936}
\noindent\begin{tabular}{@{}llll@{}}
\textbf{Число} & \textbf{Дежурный} & \textbf{Часы} & \textbf{Подпись}\\
28 февр. & J. Maddox      & 9--18 & J. M.\\
1 марта  & M. J. Mason    & 9--18 & M. J. M.\\
2 марта  & M. J. Mason    & 9--18 & M. J. M.\\
3 марта  & J. A. Mercer   & 9--18 & J. M.\\
4 марта  & J. Maddox      & 9--18 & J. M.\\
\end{tabular}\\[2mm]
\noindent\textit{Дежурный расписывается инициалами. Полная фамилия не требуется.}
\end{docbox}"""
DOCS['roster_cap'] = 'Тот самый лист: не перечень полномочий, а график дежурств'

FIGS['atom'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,
  kn/.style={box,text width=33mm,align=left,font=\scriptsize},
  ch/.style={box,text width=33mm,align=center,font=\scriptsize,fill=black!10},
  op/.style={box,text width=33mm,align=left,font=\scriptsize,dashed,fill=white}]
% ---- колонка 1
\node[kn] (k1) at (0,5.7) {вещество \textbf{не сплошное}: у него есть устройство};
\node[kn] (k2) at (0,3.4) {в устройстве держится \textbf{огромная связь}};
\node[kn] (k3) at (0,1.1) {переставь частицу --- \textbf{получится другое вещество}};
% ---- колонка 2
\node[ch] (c) at (6.3,3.4) {Что сделали первым делом:\\[1mm]\textbf{разорвать связь как можно громче}};
% ---- колонка 3
\node[op] (o1) at (12.6,5.7) {\textbf{научиться собирать}, а не только рвать};
\node[op] (o2) at (12.6,3.4) {молекула еды, волокно ткани, материал под задачу};
\node[op] (o3) at (12.6,1.1) {нужны приборы, деньги, годы --- и сперва понять, как сложились частицы};
% ---- связи
\foreach \n in {k1,k2,k3} {\draw[arr] (\n.east) -- ++(4mm,0) |- (c.west);}
\foreach \n in {o1,o2,o3} {\draw[arr,dashed] (c.east) -- ++(4mm,0) |- (\n.west);}
% ---- заголовки колонок
\node[grp] at (0,7.3) {[Что известно]};
\node[grp] at (6.3,7.3) {[Что выбрали]};
\node[grp] at (12.6,7.3) {[Что осталось несделанным]};
\draw[black!25,line width=0.3pt] (-1.9,6.95) -- (1.9,6.95);
\draw[black!25,line width=0.3pt] (4.4,6.95) -- (8.2,6.95);
\draw[black!25,line width=0.3pt] (10.7,6.95) -- (14.5,6.95);
% ---- легенда
\draw[arr] (-1.9,-0.7) -- (-0.7,-0.7); \node[font=\tiny,anchor=west] at (-0.55,-0.7) {сделано};
\draw[arr,dashed] (3.6,-0.7) -- (4.8,-0.7); \node[font=\tiny,anchor=west] at (4.95,-0.7) {гипотеза: дата проверки не назначена};
\end{tikzpicture}""", 'Что мы знаем об атоме, что из этого выбрали и что осталось несделанным')

FIGS['birdname'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\small]
\draw[line width=0.6pt,fill=black!5] (0,0) ellipse [x radius=1.5,y radius=1.0];
\node[font=\scriptsize,align=center] at (0,0) {живая птица:\\клюёт, ходит, дерётся};
\foreach \y/\t in {2.4/{по-английски},1.6/{по-немецки},0.8/{по-китайски},0.0/{по-японски},-0.8/{на латыни}}
  {\node[box,font=\scriptsize,text width=24mm,anchor=west] at (3.6,\y) {\t: своё слово};}
\foreach \y in {2.4,1.6,0.8,0.0,-0.8} {\draw[line width=0.3pt,dashed] (1.5,0) -- (3.5,\y);}
\node[font=\scriptsize,text width=86mm,align=center] at (3.0,-2.2) {Выучив все пять слов, вы не узнаете о птице ровно ничего. Узнать можно, только если смотреть на птицу.};
\end{tikzpicture}""", 'Урок, который отец дал мальчику: имя вещи и вещь --- разные уровни')

FIGS['chrono'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,
  d/.style={box,text width=30mm,align=center,font=\scriptsize},
  lo/.style={box,text width=34mm,align=left,font=\scriptsize,fill=black!10},
  hi/.style={box,text width=34mm,align=left,font=\scriptsize,dashed}]
\node[d] (c1) at (0,4.3) {\textbf{Хронометр}\\точнейший прибор своего века};
\node[lo] (a1) at (5.6,5.5) {колоть орехи:\\громко, сразу видно результат};
\node[hi] (b1) at (5.6,3.1) {найти долготу:\\тихо, нужен расчёт, спасает корабли};
\draw[arr] (c1) -- (a1); \draw[arr,dashed] (c1) -- (b1);
\node[d] (c2) at (0,0.6) {\textbf{Атом}\\точнейший прибор нашего века};
\node[lo] (a2) at (5.6,1.5) {самое громкое применение: видно всем и сразу};
\node[hi] (b2) at (5.6,-0.9) {собрать вещество: еда, ткань, материал --- тихо, долго, дорого};
\draw[arr] (c2) -- (a2); \draw[arr,dashed] (c2) -- (b2);
\draw[black!30,line width=0.3pt] (-1.8,2.1) -- (7.6,2.1);
\node[font=\scriptsize\itshape,anchor=west,text width=48mm] at (8.0,4.3) {Прибор один и тот же. Разное --- возраст того, кто держит его в руках.};
\node[font=\scriptsize\itshape,anchor=west,text width=48mm] at (8.0,0.4) {Сплошная стрелка --- что выбрали. Пунктирная --- для чего прибор и сделан.};
\end{tikzpicture}""", 'Один и тот же прибор в двух руках: детской и взрослой')

FIGS['glass'] = (r'''\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize]
\begin{scope}
\fill[black!8] (0,0) rectangle (0.85,3.2); \draw[line width=0.5pt] (0,0) rectangle (0.85,3.2);
\node[anchor=north,text width=26mm,align=center] at (0.42,-0.2) {одна поверхность};
\draw[arr,line width=0.7pt] (-2.0,2.6) -- (-0.05,1.9);
\draw[arr,line width=0.7pt] (-0.05,1.9) -- (-2.0,1.2) node[anchor=east,xshift=-1mm] {\textbf{4 из 100}};
\draw[arr,line width=0.4pt,black!55] (0.05,1.9) -- (1.7,1.37);
\node[anchor=north west,font=\tiny,text width=15mm,black!55] at (1.5,1.25) {остальные проходят};
\end{scope}
\begin{scope}[shift={(8.6,0)}]
\fill[black!8] (0,0) rectangle (0.85,3.2); \draw[line width=0.5pt] (0,0) rectangle (0.85,3.2);
\node[anchor=north,text width=26mm,align=center] at (0.42,-0.2) {две поверхности\\(толщина меняется)};
\draw[arr,line width=0.7pt] (-2.0,2.6) -- (-0.05,1.9);
\draw[arr,line width=0.7pt] (-0.05,1.9) -- (-2.0,1.2) node[anchor=east,xshift=-1mm,text width=23mm,align=right] {\textbf{от 0 до 16 из 100}};
\draw[arr,line width=0.4pt,black!55] (0.05,1.9) -- (0.8,1.66);
\draw[arr,line width=0.4pt,black!55] (0.8,1.66) -- (0.1,1.42);
\end{scope}
\node[font=\scriptsize\itshape,text width=104mm,align=center] at (4.3,-2.35)
 {Один и тот же фотон. Ответ природы --- не «да» и не «нет», а доля. Спрашивать, какой именно фотон отразится, бесполезно: ответа такого вида нет.};
\end{tikzpicture}''', 'Частичное отражение: сколько света вернётся, зависит от толщины стекла')

FIGS['qed'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize]
% --- панель А: источник, детектор, зеркало, пути
\fill (0,5.4) circle (2pt); \node[anchor=east] at (-0.15,5.4) {источник};
\fill (7.2,5.4) circle (2pt); \node[anchor=west] at (7.35,5.4) {детектор};
\draw[line width=0.8pt] (-0.5,2.7) -- (7.7,2.7);
\node[anchor=south east,font=\tiny] at (7.7,2.78) {зеркало};
\foreach \x in {0.3,1.5,2.7,3.6,4.5,5.7,6.9} {
  \draw[line width=0.3pt,black!60] (0,5.4) -- (\x,2.75) -- (7.2,5.4);
  \fill[black!60] (\x,2.75) circle (0.9pt);}
% --- стрелки-секундомеры
\foreach \x/\a in {0.3/200, 1.5/95, 2.7/25, 3.6/5, 4.5/25, 5.7/95, 6.9/200} {
  \draw[line width=0.4pt] (\x,1.75) circle (0.32);
  \draw[-{Latex[length=1.3mm]},line width=0.5pt] (\x,1.75) -- ++(\a:0.32);}
\node[anchor=north,font=\tiny,text width=30mm,align=center] at (3.6,1.32) {у каждого пути своя стрелка; в середине они смотрят почти одинаково};
\draw[line width=0.35pt,black!45] (-0.5,0.45) -- (7.7,0.45);
% --- панель Б: сложение встык
\coordinate (p0) at (2.3,-2.1);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p0) -- ++(-170:0.8) coordinate (p1);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p1) -- ++(-70:0.8) coordinate (p2);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p2) -- ++(10:0.8) coordinate (p3);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p3) -- ++(65:0.8) coordinate (p4);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p4) -- ++(90:0.8) coordinate (p5);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p5) -- ++(65:0.8) coordinate (p6);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p6) -- ++(10:0.8) coordinate (p7);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p7) -- ++(-70:0.8) coordinate (p8);
\draw[-{Latex[length=1.4mm]},line width=0.5pt] (p8) -- ++(-170:0.8) coordinate (p9);
\draw[-{Latex[length=2.4mm]},line width=1.1pt] (p0) -- (p9);
\fill (p0) circle (1.3pt);
\node[anchor=east,text width=26mm,align=right] at (0.0,-1.3) {\textbf{складываем встык:}\\конец одной --- к началу следующей};
\node[anchor=west,text width=34mm] at (5.0,-1.1) {итоговая стрелка --- жирная: от начала первой до конца последней};
\node[anchor=west,text width=34mm] at (5.0,-2.6) {\textbf{вероятность} = квадрат её длины};
\end{tikzpicture}""", 'Способ Фейнмана: у каждого пути своя стрелка; складываем встык, и длина итоговой даёт вероятность')

FIGS['retell'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize,
 bx/.style={draw,line width=0.5pt,align=center,inner sep=3pt,text width=24mm,rounded corners=1pt},
 add/.style={draw,line width=0.4pt,dash pattern=on 2.4pt off 1.8pt,align=center,inner sep=2.5pt,text width=22mm,rounded corners=1pt,fill=black!4}]
\node[bx,fill=black!8] (ter) at (0,0) {\textbf{Территория}\\то, что происходит};
\node[bx] (a) at (3.3,0) {\textbf{Оригинал}\\книга, семинар};
\node[bx] (b) at (6.6,0) {\textbf{Пересказ}\\лекция о книге};
\node[bx] (c) at (9.9,0) {\textbf{Пересказ пересказа}\\курс по лекции};
\node[bx] (d) at (13.2,0) {\textbf{Товар}\\то, что продают};
\draw[arr] (ter)--(a); \draw[arr] (a)--(b); \draw[arr] (b)--(c); \draw[arr] (c)--(d);
\node[add] (x1) at (8.25,-2.1) {+ выдумка автора курса};
\node[add] (x2) at (11.55,-2.1) {+ астрология, «энергия слов»};
\draw[arr,dash pattern=on 2.4pt off 1.8pt] (x1) -- (c);
\draw[arr,dash pattern=on 2.4pt off 1.8pt] (x2) -- (d);
\draw[arr,dash pattern=on 2.4pt off 1.8pt,black!55] (d.north) to[bend right=26] node[midway,above,font=\tiny,text width=42mm,align=center]{обратной проверки по территории нет ни на одном шаге} (ter.north);
\node[font=\scriptsize\itshape,text width=112mm,align=center] at (6.6,-3.5)
 {Каждая стрелка --- потеря. Проверить можно только в одну сторону: вернуться к оригиналу и к территории. Тот, кто продаёт последний ящик, этого шага не делает и вам не предлагает.};
\end{tikzpicture}""", 'Цепочка пересказов: карта карты карты, и ни одной обратной стрелки к территории')

FIGS['fission'] = (r"""\begin{tikzpicture}[x=1cm,y=1cm,font=\scriptsize,
 nuc/.style={circle,draw,line width=0.5pt,fill=black!8,minimum size=7.5mm,inner sep=0pt,font=\tiny},
 frag/.style={circle,draw,line width=0.5pt,fill=black!4,minimum size=5.5mm,inner sep=0pt,font=\tiny},
 nn/.style={-{Latex[length=1.6mm]},line width=0.5pt}]
\node[nuc] (a) at (2.2,2.6) {ядро};
\draw[nn] (0.1,2.6) -- (a); \node[anchor=south,font=\tiny] at (1.1,2.72) {нейтрон};
\node[frag] (f1) at (4.3,3.5) {}; \node[frag] (f2) at (4.3,1.7) {};
\draw[nn] (a) -- (f1); \draw[nn] (a) -- (f2);
\node[font=\tiny,text width=21mm,align=center] at (5.8,2.6) {два осколка, вместе полегче исходного ядра};
\node[nuc] (b1) at (8.2,4.1) {ядро}; \node[nuc] (b2) at (8.2,1.1) {ядро};
\draw[nn] (a) to[bend left=12] node[pos=0.78,above,font=\tiny]{новый нейтрон} (b1);
\draw[nn] (a) to[bend right=12] node[pos=0.78,below,font=\tiny]{новый нейтрон} (b2);
\node[frag] at (10.3,4.8) {}; \node[frag] at (10.3,3.4) {};
\node[frag] at (10.3,1.8) {}; \node[frag] at (10.3,0.4) {};
\draw[nn] (b1) -- (10.0,4.8); \draw[nn] (b1) -- (10.0,3.4);
\draw[nn] (b2) -- (10.0,1.8); \draw[nn] (b2) -- (10.0,0.4);
\draw[nn,black!55] (b1) -- ++(25:1.5); \draw[nn,black!55] (b1) -- ++(-25:1.5);
\draw[nn,black!55] (b2) -- ++(25:1.5); \draw[nn,black!55] (b2) -- ++(-25:1.5);
\node[anchor=west,font=\tiny,text width=22mm] at (11.0,2.6) {и так далее --- за миллионные доли секунды};
\node[draw,line width=0.4pt,dash pattern=on 2.4pt off 1.8pt,fill=black!3,text width=104mm,align=center,font=\scriptsize,inner sep=4pt] at (5.6,-0.9)
 {Осколки вместе весят чуть меньше исходного ядра. Разница не пропадает: она и есть выделившаяся энергия. Если нейтроны находят новые ядра быстрее, чем разлетаются в стороны, --- процесс идёт сам и нарастает. Придержать его --- реактор. Не придерживать --- бомба.};
\end{tikzpicture}""", 'Цепная реакция: одно деление даёт два осколка и новые нейтроны, каждый из которых находит следующее ядро')
