from selene.core.entity import SeleneElement
from selene.support.conditions import have
from selene.support.shared import browser

subject: SeleneElement = ...


def add(from_: str, /, *, autocomplete: str = None):
    subject.type(from_)
    (
        browser
        .all('.subjects-auto-complete__option')
        .element_by(have.exact_text(autocomplete or autocomplete != '' or from_))
        .click()
    )
