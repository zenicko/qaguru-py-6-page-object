from selene.core.entity import Collection
from selene.support.conditions import have
from selene.support.shared import browser


def cells_of_row(index: int) -> Collection:
    return browser.element("table").element('tbody').all("tr")[index].all('td')


def cells_of_row_should_have_texts(index: int, *texts1: str):
    browser.element("table").element('tbody').all("tr")[index].all('td').should(have.exact_texts(*texts1))


def cells_of_row_(index: int, should_have_texts: list):
    browser.element("table").element('tbody').all("tr")[index].all('td').should(have.exact_texts(*should_have_texts))


def get_texts_from_row(index: int) -> str:
    return browser.element("table").element('tbody').all("tr")[index].text
