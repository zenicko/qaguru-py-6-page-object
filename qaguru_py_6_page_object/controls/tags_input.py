from selene.core.entity import SeleneElement
from selene.support.conditions import have
from selene.support.shared import browser

subject: SeleneElement = ...


def add(element: SeleneElement, /, *, from_: str, to: str = None):
    element.type(from_)
    (
        browser
        .all('.subjects-auto-complete__option')
        .element_by(have.exact_text(to or to != '' or from_))
        .click()
    )
