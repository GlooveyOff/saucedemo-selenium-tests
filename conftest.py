import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption(
        "--url",
        action="store",
        default="https://www.saucedemo.com/",
        help="URL сайта SauceDemo",
    )
    parser.addoption(
        "--browser",
        action="store",
        default="chrome",
        help="Браузер для запуска теста: chrome или firefox",
    )


@pytest.fixture
def url(request):
    return request.config.getoption("--url")


@pytest.fixture
def browser(request):
    browser_name = request.config.getoption("--browser").lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome()
    elif browser_name == "firefox":
        driver = webdriver.Firefox()
    else:
        pytest.fail(
            f"Неизвестный браузер: {browser_name}. Используйте chrome или firefox."
        )

    driver.maximize_window()
    yield driver
    driver.quit()
