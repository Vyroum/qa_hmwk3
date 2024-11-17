import pytest
from selene import browser, be, have

@pytest.fixture(scope="session")
def browser_set():
    browser.open("htttps://gooogle.com/ncr")
    browser.driver.maximize_window()
    yield
    browser.quit()

