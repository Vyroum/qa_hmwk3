import pytest
from selene import browser, be, have


def test_search_for_result(browser_set):
    browser.element('[name="q"').should(be.blank).type("Pytest").press_enter()
    browser.element('[id="search"]').should(have.text("pytest documentation"))



def test_search_for_no_result(browser_set):
    browser.element('[name="q"').should(be.blank).type("asfa12312azxeahgaewhqawhyg").press_enter()
    browser.element('[aria-level="3"]').should(have.text(" ничего не найдено"))