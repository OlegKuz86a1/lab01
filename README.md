<div align="center">
<h1><a id="intro">Лабораторная работа №1</a><br></h1>
<a href="https://docs.github.com/en"><img src="https://img.shields.io/static/v1?logo=github&logoColor=fff&label=&message=Docs&color=36393f&style=flat" alt="GitHub Docs"></a>
<a href="https://daringfireball.net/projects/markdown"><img src="https://img.shields.io/static/v1?logo=markdown&logoColor=fff&label=&message=Markdown&color=36393f&style=flat" alt="Markdown"></a>
<a href="https://shields.io"><img src="https://img.shields.io/static/v1?logo=shieldsdotio&logoColor=fff&label=&message=Shields&color=36393f&style=flat" alt="Shields"></a>
<img src="https://img.shields.io/badge/Course-AppSec-D51A1A?style=flat" alt="Course: AppSec">
<img src="https://img.shields.io/badge/git-%23F05033.svg?style=flat&logo=git&logoColor=white" alt="Git">
<img src="https://img.shields.io/badge/GitHub_CLI-181717?style=flat&logo=github&logoColor=white" alt="GitHub CLI">
<img src="https://img.shields.io/badge/Contributor-Кузнецов_О._А.-8b9aff?style=flat" alt="Contributor"></div>

***

Салют :wave:,<br>
Данная лабораторная работа посвящена освоению рабочего цикла Git. Работа позволит ознакомиться с базовыми навыками необходимыми для произведения `commit changes`, публикации изменений в удаленный репозиторий, обновлениями данных для них, `fork`, ветвлением, подписанными коммитами, Pull Request и разрешением конфликтов слияния через rebase.

Для сдачи данной работы также будет требоваться ответить на дополнительные вопросы по описанным темам.

***

## Структура репозитория лабораторной работы

```bash
meFolder
├── hello.py
└── README.md
```

***

## Материал

Git — распределённая система контроля версий. Ключевые концепции:

- **Working tree** — файлы на диске, с которыми вы работаете
- **Staging area (index)** — промежуточная область: `git add` переносит изменения сюда
- **Commit** — снимок состояния, сохранённый в локальном репозитории
- **Remote** — удалённый репозиторий (GitHub), синхронизация через `push` / `pull`

> Поток: `edit` → `git add` → `git commit` → `git push` — это базовый цикл, который вы будете повторять в каждой лабораторной

- **Ветки (branches)** — параллельные линии разработки. `master` / `main` — основная ветка, `develop` — рабочая, `patch*` — для исправлений
- **Pull Request** — запрос на слияние ветки в основную. Используется для code review и согласования изменений
- **Rebase** — перенос коммитов на другую базу. Создаёт линейную историю, но переписывает SHA-хеши
- **GPG-подпись** — криптографическое подтверждение авторства коммита. GitHub показывает зелёный бейдж `Verified`

### hello.py

Файл `hello.py` — пример Python-скрипта с использованием библиотеки `typer` для создания CLI-приложений. В задании вы будете модифицировать его: от простого "Hello World" до полноценного CLI с аргументами и опциями.

***

## Задание

- [x] 1. Модификация исходного кода и первый подписанный коммит
- [x] 2. Ветка patch1, добавление комментария
- [x] 3. Ветка patch2, улучшение стиля и моделирование конфликта
- [x] 4. Разрешение конфликта через rebase и слияние PR

***

## Tutorial

> Перед началом выполните подготовительные инструкции:
>
> - [Подготовка рабочего окружения](https://course.geminishkv.tech/labs/intro/vmbox_tutorial/) — VirtualBox, установка Linux
> - [Настройка Git, GPG и GitHub CLI](https://course.geminishkv.tech/labs/intro/git_setup/) — git config, SSH, GnuPG, gh

- [x] 1. Модификация исходного кода и первый подписанный коммит: Добавлен запрос имени пользователя и вывод приветствия `Hello appsec world from @name`. Изменения закоммичены с криптографической подписью и отправлены в удалённый репозиторий.

```bash
git add hello.py
git commit -S -m "output Hello appsec world from @name"
git push origin master
```

- [x] 2. Ветка patch1, добавление комментария: Создана ветка patch1. Исходный код заменён на CLI-утилиту на базе typer, добавлен поясняющий комментарий к импорту. Выполнен последовательный подписанный коммит и публикация.

```bash
git checkout -b patch1
git add hello.py
git commit -S -m "migrate to typer CLI with formal greeting support"
git commit -S -m "add explanatory comment to typer import"
git push -u origin patch1
```

- [x] 3. Ветка patch2, улучшение стиля и моделирование конфликта: Создана ветка patch2 с финальной стилизацией (PEP 8, docstrings, type hints). Отправлен PR в master. Для симуляции расхождений в master напрямую изменён комментарий, что привело к конфликту слияния в интерфейсе GitHub.

```bash
git checkout -b patch2
git commit -S -m "improve code style, add docstrings & type hints"
git push -u origin patch2
git checkout master
git commit -S -m "direct comment change in master"
git push origin master
```

- [x] 4. Разрешение конфликта через rebase и слияние PR: Локально выполнен rebase ветки patch2 на актуальный master. Вручную удалены маркеры конфликта в файле. Изменения опубликованы безопасным force-push, после чего PR успешно смёржен через веб-интерфейс.

```bash
git checkout patch2
git fetch origin
git rebase origin/master
git add hello.py
git rebase --continue
git push origin patch2 --force-with-lease
```

***

## Результаты

Полностью отработан цикл разработки с Git: ветвление, подписанные коммиты, работа с PR, разрешение конфликтов слияния через rebase, финальный merge.

Были использованы инструменты: Git CLI, GPG/SSH для подписи коммитов (-S), GitHub Web UI для Pull Request, typer для CLI-утилиты.

Возник конфликт слияния из-за изменения одной и той же строки в master и patch2. Решён через `git rebase origin/master`, ручное редактирование конфликтных маркеров и безопасный force-push с флагом `--force-with-lease`.

## Выводы

В ходе работы освоены ключевые практики безопасной и профессиональной работы с Git. Использование флага `-S` гарантирует аутентичность и неизменяемость истории коммитов. Разрешение конфликтов через rebase позволяет сохранять линейную и читаемую историю проекта, в отличие от стандартного merge, который создаёт дополнительные merge-коммиты. Работа с Pull Request обеспечивает контроль качества и код-ревью перед интеграцией изменений в основную ветку. Полученные навыки полностью соответствуют современным командным workflow и CI/CD стандартам.

## История коммитов

```
1885ee6 (origin/master) Merge pull request #2 from OlegKuz86a1/patch2 |\
| * 66942e2 (origin/patch2, patch2) improve code style, add docstrings & type hints |/
7fa843a (HEAD -> master) direct comment change in master
fe7abaa Merge pull request #1 from OlegKuz86a1/patch1 |\
| * 07708f4 (origin/patch1, patch1) add explanatory comment to typer import | * 25fb7b0 migrate to typer CLI with formal greeting support |/
ec54848 output Hello appsec world from @name
dadd213 Add hello.py with dirty AppSec code examples
61373c7 Add empty README.md
```</content>
<parameter name="filePath">/home/oem/sec_course_labs/course_labs/meFolder/README.md
