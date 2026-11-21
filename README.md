<p align="center">
<img width="532" height="755" alt="Screenshot 2026-11-21 at 00-23-14 Karta_ne_est_territoriya_v28-2 pdf" src="https://github.com/user-attachments/assets/11a89f31-cdd6-4212-a846-ed5985e35662" />
</p>

# Карта не есть территория

**Научно-нуарный детектив по мотивам семинаров Альфреда Коржибски по общей семантике
(колледж Оливет, 1937).** Герой — Алекс Мерсер, сыщик, который полгода считал виновным
не того человека и из-за этого начал учиться оценивать заново.

Книга одновременно детектив и учебник: сюжет идёт «Частями», разбор метода — «Интермедиями»,
а четырнадцать лекций Коржибски вынесены в отдельный слой «Семинар», который можно читать
подряд как короткий курс.

Объём: ~1200 страниц, B5, XeLaTeX.

---

## Где что лежит

```
ru/                       русская версия
  karta-ne-est-territoriya.tex   весь текст книги одним файлом
  img/                    иллюстрации (комиксы и портреты)
  fonts/                  Lora и Montserrat (статические начертания)
  cover.jpg, logo.png     обложка и логотип SocioCyberneering Inc.
en/                       английская версия — перевод пока не сделан
releases_ru/              готовые PDF русской версии (и last_version)
releases_en/              готовые PDF английской версии
tools/                    генератор, из которого собирается .tex
  build.py                сборщик
  src/                    исходные интермедии (markdown) и схемы TikZ (python)
```

## Скачать готовый PDF

**Последняя версия, постоянная ссылка:**

[`releases_ru/karta-ne-est-territoriya-last_version.pdf`](releases_ru/karta-ne-est-territoriya-last_version.pdf)

```sh
curl -L -o karta.pdf https://github.com/sociocyber1/Latex_ScienceBook_Detective-Alex-Merser-Map-is-not-Territory/raw/main/releases_ru/karta-ne-est-territoriya-last_version.pdf
```

Все версии по номерам — в папке [`releases_ru/`](releases_ru/); английские сборки,
когда появятся, будут в [`releases_en/`](releases_en/).

## Как собрать

Нужен TeX Live с XeLaTeX и пакетами `polyglossia`, `fontspec`, `tcolorbox`, `tikz`,
`tabularx`, `booktabs`, `microtype`, `tocloft`, `hyperref`, `xurl`, `needspace`, `adjustbox`.

```sh
cd ru
xelatex karta-ne-est-territoriya.tex
xelatex karta-ne-est-territoriya.tex     # второй проход — оглавление и ссылки
```

Папки `img/` и `fonts/` должны лежать рядом с `.tex`. Второй проход обязателен.

## Перевод

Папка `en/` пока пустая. Перевод планируется; структура репозитория уже разделена,
чтобы русская и английская версии собирались независимо и не мешали друг другу.

Если хотите взяться за перевод — пишите, адреса ниже. Отдельная сложность: у Коржибски
термины держатся на структуре, а не на значении. Дефисы в «семантических-реакциях» стоят
не для красоты, «не есть» — не стилистическая неловкость. Перевод, который это «причешет»,
уничтожит ровно то, ради чего текст написан.

## Лицензии

- **Текст и иллюстрации** — [CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/deed.ru).
  Копируйте, печатайте, переводите, переделывайте. Три просьбы: укажите авторство,
  оставьте результат открытым и напишите, что именно вы изменили.
- **Код сборки** (`tools/`) — GPL-3.0, см. `LICENSE`.
- **Шрифты** — Lora и Montserrat, SIL Open Font License 1.1.

Печатать и продавать можно, запрета нет и процент платить не надо. Условия — ссылка на
оригинал, имя автора и список изменений. Подробности на странице лицензии в самой книге.

## Автор

SocioCyberneering Inc.

- Почта: sociocyber1@gmail.com
- Telegram: @sc_sinus *(аккаунты меняются часто, ответа может не быть — почта надёжнее)*
- Matrix: @cercell:4d2.org

Поддержать работу можно по реквизитам на второй странице лицензии в книге.
