## Тест сценариев
---
Скрипт автоматизирует проверку сценариев поиска
---

### Описание
+ Проверка двух сценариев поиска
+ [ya](https://ya.ru)
+ Проверка наличия поля поиска
+ Проверка таблици с подсказками (suggest)
+ Ссылка ведет на сайт компании [TENSOR](https://tensor.ru/)
+ [yandex](https://yandex.ru)
+ Ссылка «Картинки» присутствует на странице
+ Переход на url "https://yandex.ru/images/"
+ Открытие первой картинки
+ Переход на вторую и возвращение на первую
+ Проверка что вернулись на туже картинку

---
+ Рекомендуется использовать [virtualenv](https://docs.python.org/3/library/venv.html)
+ Проект использует [selenium](https://github.com/SeleniumHQ/selenium/blob/master/py/docs/source/index.rst)

---
### Requirements

```bash
Python ver 3.5 (or higher)
```

```bash
pip install selenium
```

```bash
pip install -r reqirements.txt
```

### Пример запуска в консоли
```bash
python3 scenario_script.py
```

### Пример результата
```bash
True
True
```

### Пример запуска тестов
```bash
python3 -m unittest -v scenario_tests.py
```

### Пример результатов
```bash
test_run_images (scenario_tests.TestSearchInYandex) ... ok
test_search_in_ya (scenario_tests.TestSearchInYandex) ... ok

----------------------------------------------------------------------
Ran 2 tests in 120.937s

OK
```

---
## Project Goals

Тестовое задание на позицию разработчика в тестировании - [TENSOR](https://tensor.ru)
