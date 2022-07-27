from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser


class TagsInput:

    def __init__(self, element: Element):
        self.subject = element

    def add(self, from_: str, /, *, autocomplete: str = None):
        self.subject.type(from_)
        (
            browser
            .all('.subjects-auto-complete__option')
            .element_by(have.exact_text(from_ if not autocomplete or autocomplete == '' else autocomplete))
            .click()
        )

    def autocomplete(self, text: str = None):
        self.subject.type(text).press_tab()

