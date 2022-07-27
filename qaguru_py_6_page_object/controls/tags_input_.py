from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser

subject: Element = ...


def add(from_: str, /, *, autocomplete: str = None):
    subject.type(from_)
    (
        browser
        .all('.subjects-auto-complete__option')
        .element_by(have.exact_text(from_ if not autocomplete or autocomplete == '' else autocomplete))
        .click()
    )
