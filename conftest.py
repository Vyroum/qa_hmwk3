import pytest
from selene import browser

@pytest.fixture
def browser_set():
    browser.open("https://google.com/")
    browser.driver.maximize_window()
    yield
    browser.quit()

