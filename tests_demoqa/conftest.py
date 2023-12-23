import pytest
from selene import browser


@pytest.fixture()
def browser_management_demoqa():
    browser.config.base_url = 'https://demoqa.com'
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()



@pytest.fixture()
def browser_management_qaguru():
    browser.config.base_url = 'https://app.qa.guru/automation-practice-form/'
    browser.config.timeout = 2.0
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    yield
    browser.quit()
