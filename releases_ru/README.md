# Релизы — русская версия

| Файл | Версия | Страниц |
|---|---|---|
| [`karta-ne-est-territoriya-last_version.pdf`](karta-ne-est-territoriya-last_version.pdf) | **последняя (v28)** | 1231 |
| [`karta-ne-est-territoriya-v28.pdf`](karta-ne-est-territoriya-v28.pdf) | v28 | 1231 |
| [`karta-ne-est-territoriya-v27.pdf`](karta-ne-est-territoriya-v27.pdf) | v27 | 1162 |

**Постоянная ссылка на последнюю версию** — она не меняется от выпуска к выпуску:

```
https://github.com/sociocyber1/Latex_ScienceBook_Detective-Alex-Merser-Map-is-not-Territory/raw/main/releases_ru/karta-ne-est-territoriya-last_version.pdf
```

Скачать из консоли:

```sh
curl -L -o karta.pdf https://github.com/sociocyber1/Latex_ScienceBook_Detective-Alex-Merser-Map-is-not-Territory/raw/main/releases_ru/karta-ne-est-territoriya-last_version.pdf
```

## Как это устроено

При выпуске новой версии сюда кладутся два файла с одинаковым содержимым:
`...-vNN.pdf` (архивная копия) и `...-last_version.pdf` (всегда последняя). Git хранит
одинаковые файлы одним объектом, так что второй экземпляр места почти не занимает,
а ссылка выше остаётся рабочей всегда.

Имена файлов — латиницей и без пробелов, чтобы ссылки не ломались в скриптах
и загрузчиках.
