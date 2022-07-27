from selene.core import command
from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser


class DropDown:
    def __init__(self, element: Element):
        self.element = element

    def select(self, option: str):
        self.element.perform(command.js.scroll_into_view).click()
        browser.all('[id^=react-select][id*=-option]').element_by(have.exact_text(option)).click()

    def autocomplete(self, option: str):
        self.element.element('input').send_keys(option).press_enter()
