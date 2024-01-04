import pytest
from selene import browser
from utils import attach
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture()
def setup_browser():
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_html(browser)
    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_video(browser)
    browser.quit()
