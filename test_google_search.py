import pytest
from selene import browser, be, have

@pytest.fixture
def search_for_result(test_browser_set):
    browser.element('[name="q"').should(be.blank).type("Pytest").press_enter()
    browser.element('[id="search"]').should(have.text("pytest documentation"))

@pytest.fixture
def search_for_no_result(test_browser_set):
    browser.element('[name="q"').should(be.blank).type("asfa12312azxeahgaewhqawhyg").press_enter()
    browser.element('[id="search"]').should(have.text(" ничего не найдено"))