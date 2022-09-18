import pytest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture()
def setup(browser):
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    return driver


def pytest_addoption(parser):  # This will get the value from CLI /hooks
    parser.addoption("--browser")


@pytest.fixture()
def browser(request):  # This will return the Browser value to setup method
    return request.config.getoption("--browser")


########## pytest HTML Report ################

# It is hooked for Adding Environment info to HTML Report
def pytest_configure(config):
    config._metadata['Project Name'] = '84 Word'
    config._metadata['Tester'] = 'Sudip Neupane'
