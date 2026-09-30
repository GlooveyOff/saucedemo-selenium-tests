# Автотест покупки на SauceDemo

Проект проверяет полный сценарий покупки товара Sauce Labs Backpack на сайте SauceDemo с помощью Selenium и pytest.

## Установка

```bash
pip install -r requirements.txt
```

## Запуск

```bash
pytest
```

По умолчанию используется Chrome. Выбор браузера:

```bash
pytest --browser=chrome
pytest --browser=firefox
```

URL сайта можно передать параметром (по умолчанию используется `https://www.saucedemo.com/`):

```bash
pytest --url=https://www.saucedemo.com/
```

Параметры браузера и URL можно использовать вместе:

```bash
pytest --browser=firefox --url=https://www.saucedemo.com/
```
