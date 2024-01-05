import pytest
from selene import browser
from utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
from dotenv import load_dotenv



def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Браузер в котором будут запущены тесты',
        choices=['firefox', 'chrome'],
        default='chrome'
    )

@pytest.fixture(scope='session')
def selenoid_browser(request):
    return request.config.getoption('--browser')


@pytest.fixture(scope='session', autouse=True)
def load_env():
    load_dotenv()
@pytest.fixture(scope='function')
def setup_browser(selenoid_browser):
    browser.config.window_width = 1080
    browser.config.window_height = 1920
    browser.config.base_url = 'https://demoqa.com'
    options = Options()
    selenoid_capabilities = {
        "browserName": selenoid_browser,
        "browserVersion": "100.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options
    )

    browser.config.driver = driver

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
