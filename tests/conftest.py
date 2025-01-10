import pytest
from selenium import webdriver
from selene import Browser, Config
from selenium.webdriver.chrome.options import Options


@pytest.fixture(autouse=True)
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    # driver_options.add_argument("--headless")

    options = Options()
    selenoid_capabilities = {
        "browserName": "chrome",
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
    browser = Browser(Config(driver))
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com'

    yield browser

    browser.quit()
