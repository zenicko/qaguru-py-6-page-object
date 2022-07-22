from selene.core import command
from selene.core.entity import SeleneElement
from selene.support.conditions import have
from selene.support.shared import browser


'''
    # Before POM 
def select_by(selector: str, /, *, option: str):
    select(browser.element(selector), option=option)


def select(element: Element, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=-option]').element_by(have.exact_text(option)).click()
'''


def select(element: SeleneElement, /, *, option: str):
    element.perform(command.js.scroll_into_view).click()
    browser.all('[id^=react-select][id*=-option]').element_by(have.exact_text(option)).click()


def autocomplete(element: SeleneElement, /, *, option: str):
    element.element('input').send_keys(option).press_enter()
