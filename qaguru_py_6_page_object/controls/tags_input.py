from selene.support.conditions import have
from selene.support.shared import browser


def add(selector: str, /, *, from_: str, to: str = None):
    browser.element(selector).type(from_)
    browser.all('.subjects-auto-complete__option').element_by(have.exact_text(to or to != '' or from_)).click()
