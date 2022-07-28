from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser

subject: Element = ...


def set_subject(*, name: str = None, by_autocomplete=True):
    if by_autocomplete:
        autocomplete(name)
    else:
        add(by_select=name)


def add(*, by_select: str = None):
    subject.type(by_select[:2])
    (
        browser
        .all('.subjects-auto-complete__option')
        .element_by(have.exact_text(by_select))
        .click()
    )


def autocomplete(text: str = None):
    subject.type(text).press_tab()
