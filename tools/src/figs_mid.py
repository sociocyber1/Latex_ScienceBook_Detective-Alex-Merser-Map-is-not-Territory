# -*- coding: utf-8 -*-
# Figures and facsimiles for the mid-book interludes. Facts only from the manuscript.

FIGS = {}
DOCS = {}

CARD = r'''card/.style={draw,fill=yellow!12,font=\scriptsize,align=center,text width=27mm,inner sep=3pt,rounded corners=1pt},
thr/.style={line width=0.8pt,red!60!black},
thrd/.style={line width=0.8pt,red!60!black,dash pattern=on 3pt off 2.2pt},
lab/.style={midway,fill=white,font=\tiny,inner sep=1pt,align=center,text width=15mm}'''

FIGS['board1'] = (r'''\begin{tikzpicture}[''' + CARD + r''']
\node[card] (mil) at (2.0,6.0) {\textbf{Эдвард Миллер}\\сосед; «убийца» по версии полиции};
\node[card] (vej) at (6.85,6.0) {\textbf{Артур Вейл}\\три чужих мнения о нём};
\node[card] (ric) at (11.7,6.0) {\textbf{Ричард Кроу}\\комиссия студенческого фонда};
\node[card] (k17) at (1.2,3.3) {\textbf{K-17}\\контейнер, 3 марта 1936};
\node[card] (rid) at (6.85,3.3) {\textbf{Томас Рид}\\убит 22.02.1937};
\node[card] (dan) at (12.4,3.3) {\textbf{Дэниел Кроу}\\тело найдено 23.02.1936};
\node[card] (r6) at (2.0,0.8) {\textbf{R-6}\\журнал движения комиссии};
\node[card] (jm) at (6.85,0.8) {\textbf{J. M.}\\инициалы в журнале R-6};
\node[card] (bel) at (11.7,0.8) {\textbf{Джозеф Белл}\\погиб при пожаре на складе};
\node[card] (mk) at (6.85,-1.6) {\textbf{М. К.}\\плащ, шляпа, записки};
\draw[thr] (rid)--(vej) node[lab]{фото у стены};
\draw[thrd] (rid)--(mil) node[lab]{версия полиции};
\draw[thr] (rid)--(dan) node[lab]{фото Дэниела и Рида};
\draw[thrd] (rid)--(bel) node[lab]{«посредник»?};
\draw[thrd] (ric)--(dan) node[lab]{возможная связь};
\draw[thr] (r6)--(jm) node[lab]{3 марта: J. M.};
\draw[thrd] (k17)--(r6) node[lab]{3 марта?};
\draw[thrd] (k17)--(jm) node[lab]{не подтверждено};
\draw[thr] (-0.3,-1.2)--(0.9,-1.2); \node[font=\tiny,anchor=west] at (1.0,-1.2) {есть документ};
\draw[thrd] (-0.3,-1.9)--(0.9,-1.9); \node[font=\tiny,anchor=west] at (1.0,-1.9) {моё желание};
\node[font=\tiny\itshape,anchor=west,text width=30mm] at (9.2,-1.6) {у М. К. нет ни одной нитки: пустое место на стене};
\end{tikzpicture}''', 'Стена Мерсера, версия первая: сплошные нитки держатся на документах, пунктирные — на желании')

FIGS['board2'] = (r'''\begin{tikzpicture}[''' + CARD + r''']
\node[card] (mil) at (2.0,6.0) {\textbf{Генри Милтон}\\умер 3.03.1936};
\node[card] (mas) at (6.85,6.0) {\textbf{Мартин Дж. Мейсон}\\админотдел, допуск 18.01—12.02.1937};
\node[card] (mad) at (11.7,6.0) {\textbf{Джеймс Мэддокс}\\допуск от 28.02.1936};
\node[card] (k17) at (1.2,3.3) {\textbf{K-17}\\3 марта 1936, «получение на месте»};
\node[card] (mjm) at (6.85,3.3) {\textbf{M. J. M.}\\инициалы в журнале конторы};
\node[card] (jm) at (12.4,3.3) {\textbf{J. M.}\\регистрация, распоряжение 4.03.1936};
\node[card] (pri) at (6.85,0.8) {\textbf{Приложение 17-Б}\\номер есть, листа нет};
\node[card] (rid) at (11.7,0.8) {\textbf{Томас Рид}\\22.02.1937};
\draw[thr] (mil.north) to[bend left=22] node[lab,pos=0.5]{допуск подписан 28.02} (mad.north);
\draw[thrd] (mil)--(k17) node[lab]{оба 3 марта};
\draw[thr] (k17)--(mjm) node[lab]{журнал конторы};
\draw[thr] (k17)--(pri) node[lab]{приложения нет};
\draw[thrd] (mjm)--(mas) node[lab]{буквы совпали};
\draw[thrd] (mjm)--(jm) node[lab]{одно лицо?};
\draw[thrd] (mas)--(rid) node[lab]{10 дней после допуска};
\draw[thr] (-0.3,0.2)--(0.9,0.2); \node[font=\tiny,anchor=west] at (1.0,0.2) {есть документ};
\draw[thrd] (-0.3,-0.5)--(0.9,-0.5); \node[font=\tiny,anchor=west] at (1.0,-0.5) {моё желание};
\end{tikzpicture}''', 'Стена Мерсера, версия вторая: нитка от Мейсона слишком ровная, чтобы расти самой')

FIGS['k17'] = (r'''\begin{tikzpicture}[node distance=8mm,bx/.style={box,text width=28mm},
miss/.style={box,text width=28mm,dashed,fill=black!5}]
\node[bx] (a) {Административный отдел колледжа\\получатель уведомления};
\node[bx,right=of a] (b) {Контора перевозок\\(закрыта в 1938 году)};
\node[bx,right=of b] (c) {K-17, счёт клиента № 14\\временное хранение, 3 марта 1936};
\node[bx,right=of c] (d) {«Получение на месте»\\подтверждение: M. J. M.};
\draw[arr] (a)--(b); \draw[arr] (b)--(c); \draw[arr] (c)--(d);
\node[miss,below=9mm of c] (m1) {Опись содержимого\\отдельной бумагой: нет};
\node[miss,below=9mm of d] (m2) {Приложение 17-Б\\номер указан на полях, листа нет};
\draw[arr,dashed] (c)--(m1); \draw[arr,dashed] (d)--(m2);
\node[grp] at ($(a.north)+(0,4mm)$) {[Откуда]};
\node[grp] at ($(b.north)+(0,4mm)$) {[Кто возит]};
\node[grp] at ($(c.north)+(0,4mm)$) {[Что]};
\node[grp] at ($(d.north)+(0,4mm)$) {[Кто принял]};
\node[grp,anchor=east] at ($(m1.west)+(-6mm,0)$) {[Чего нет]};
\end{tikzpicture}''', 'Путь контейнера K-17 по записям: сплошные блоки записаны, пунктирные отсутствуют')

FIGS['jmtree'] = (r'''\begin{tikzpicture}[lf/.style={box,text width=29mm,font=\scriptsize}]
\node[box,text width=30mm] (root) at (7.2,4.9) {\textbf{J. M.}\\две буквы, много лиц};
\node[box] (A) at (3.6,3.0) {Человек};
\node[lf] (B) at (10.0,3.0) {\textbf{Должность или сокращение}\\проверка: справочник должностей};
\node[lf] (C) at (13.7,3.0) {\textbf{Кто-то вне моих папок}\\проверка: расширить поиск};
\node[lf] (a1) at (0.6,0.8) {\textbf{Джон Мерсер}\\проверка: почерк, даты};
\node[lf] (a2) at (4.0,0.8) {\textbf{Алекс (Julian A.) Мерсер}\\это я, но я не помню};
\node[lf] (a3) at (7.4,0.8) {\textbf{Мартин Дж. Мейсон}\\в бумагах — M. J.};
\draw[arr] (root)--(A); \draw[arr] (root)--(B); \draw[arr] (root)--(C);
\draw[arr] (A)--(a1); \draw[arr] (A)--(a2); \draw[arr] (A)--(a3);
\end{tikzpicture}''', 'Дерево гипотез о двух буквах: ни одна ветка не выбрана')

FIGS['twowinters'] = (r'''\begin{tikzpicture}[ev/.style={box,font=\scriptsize,text width=24mm,inner sep=2pt}]
\node[grp,anchor=west] at (-0.2,5.6) {[Зима 1936]};
\draw[arr] (-0.2,3.4)--(11.0,3.4);
\foreach \x in {2.16,3.78,4.86,5.13,10.26} {\draw (\x,3.3)--(\x,3.5);}
\node[ev,above=3mm] at (2.16,3.4) {\textbf{22 фев}\\пакет Ричарда Кроу};
\node[ev,below=3mm] at (3.78,3.4) {\textbf{28 фев}\\допуск Мэддоксу};
\node[ev,above=3mm] at (5.0,3.4) {\textbf{3 мар}\\Милтон умирает; K-17};
\node[ev,below=3mm] at (6.7,3.4) {\textbf{4 мар}\\приказ о передаче полномочий};
\node[ev,above=3mm] at (10.26,3.4) {\textbf{23 мар}\\опись: оригиналов нет};
\node[grp,anchor=west] at (-0.2,0.4) {[Зима 1937]};
\draw[arr] (-0.2,-1.8)--(11.0,-1.8);
\foreach \x in {0.2,6.95,8.57,9.65} {\draw (\x,-1.9)--(\x,-1.7);}
\node[ev,above=3mm] at (0.9,-1.8) {\textbf{18 янв}\\Мейсон получает допуск};
\node[ev,below=3mm] at (6.95,-1.8) {\textbf{12 фев}\\допуск заканчивается};
\node[ev,above=3mm] at (8.57,-1.8) {\textbf{18 фев}\\сообщение о пакете};
\node[ev,below=3mm] at (10.0,-1.8) {\textbf{22 фев}\\умирает Томас Рид};
\draw[arr,<->,line width=0.4pt] (6.95,-4.2)--(9.65,-4.2) node[midway,below,font=\scriptsize]{10 дней};
\end{tikzpicture}''', 'Две зимы на одном листе: в 1936-м события идут одно за другим, в 1937-м — рядом со смертью Рида')

# ---- documents under the lens
DOCS['reg3'] = r'''\begin{docbox}{Копия распоряжения от 4 марта 1936 г.}
\noindent Распоряжение о временной передаче административных функций.\\[2mm]
\noindent Приложение (перечень передаваемых полномочий):
\begin{center}\fbox{\parbox{0.7\linewidth}{\centering\itshape [лист отсутствует]}}\end{center}
\noindent Регистрация: \textbf{J. M.}
\end{docbox}'''
DOCS['reg3_cap'] = 'Под лупой: регистрационная строка и пустое место, где должно быть приложение'

DOCS['rail'] = r'''\begin{docbox}{Журнал конторы перевозок · 3 марта}
\noindent\textit{Временное хранение, контейнер K-17. Счёт клиента № 14. Получатель уведомления --- административный отдел.}\\[1mm]
\noindent\textit{Передача внутреннему перевозчику отменена. Получение на месте.}\\[1mm]
\noindent Подтверждение: \textbf{M. J. M.} (3 марта)\\[1mm]
\noindent На полях: «Приложение 17-Б» --- \textit{самого приложения нет.}
\end{docbox}'''
DOCS['rail_cap'] = 'Страница журнала, как её держал Мерсер: подтверждение есть, описи нет'

DOCS['mason'] = r'''\begin{docbox}{Временные служащие · выписка}
\noindent \textbf{Мартин Дж. Мейсон.} Помощник административного отдела. Допуск к внутренней корреспонденции. С 18 января по 12 февраля 1937 года.\\[1mm]
\noindent\textit{В остальных документах значится как M. J. Mason.}
\end{docbox}'''
DOCS['mason_cap'] = 'Карточка Мейсона, переписанная слово в слово'
