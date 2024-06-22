import time

import pytest
from selenium import webdriver


def pytest_addoption(parser):
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")


@pytest.fixture()
def setup(browser):
    if browser == 'chrome':
        driver = webdriver.Chrome()
    elif browser == 'edge':
        driver = webdriver.Edge()
    else:
        chrome_option = webdriver.ChromeOptions()
        chrome_option.add_argument("headless")
        driver = webdriver.Chrome(options=chrome_option)

    driver.get("https://www.cricbuzz.com/")
    driver.maximize_window()
    driver.implicitly_wait(5)
    return driver
