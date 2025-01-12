import pytest
from selenium import webdriver
from selene import browser
from selenium.webdriver.chrome.options import Options
from utils import attach

def pytest_addoption(parser):
    parser.addoption(
        '--browser',
        help='Выбери браузер на котором будут запущены тесты',
        choices=['chrome', 'firefox'],
        default='chrome'
    )

    parser.addoption(
        '--browser_version',
        help='Выбери версию браузеоа на котором будут запущены тесты',
        choices=['126.0', '125.0', '124.0', '123.0', '100.0'],
        default='125.0'
    )

@pytest.fixture(scope='function')
def browser_config(request):
    browser_name = request.config.getoption('--browser')
    browser_version = request.config.getoption('--browser_version')
    options = Options()
    selenoid_capabilities = {
        "browserName": browser_name,
        "browserVersion": browser_version,
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True
        }
    }
    options.page_load_strategy = 'eager'
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://user1:1234@selenoid.autotests.cloud/wd/hub",
        options=options)

    browser.config.driver = driver
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.base_url = 'https://demoqa.com'

    yield

    attach.add_screenshot(browser)
    attach.add_logs(browser)
    attach.add_html(browser)
    attach.add_video(browser)

    browser.quit()
