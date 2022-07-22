from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser


def add(element: Element, /, *, from_: str, to: str = None):
    element.type(from_)
    (
        browser
        .all('.subjects-auto-complete__option')
        .element_by(have.exact_text(to or to != '' or from_))
        .click()
    )
