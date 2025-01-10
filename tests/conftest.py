import pytest
from selenium import webdriver
from selene import browser


@pytest.fixture(autouse=True)
def browser_config():
    driver_options = webdriver.ChromeOptions()
    driver_options.page_load_strategy = 'eager'
    browser.config.window_width = 1920
    browser.config.window_height = 1080
    driver_options.add_argument("--headless")
    browser.config.driver_options = driver_options
    browser.config.base_url = 'https://demoqa.com'
    yield
    browser.quit()
