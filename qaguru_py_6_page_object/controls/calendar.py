from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser
from selenium.webdriver import Keys

NAME_OF_MONTH = {
    "01": ['January', 'Jan'],
    "02": ['February', 'Feb'],
    "03": ['March', 'Mar'],
    "04": ['April', 'Apr'],
    "05": ['May', 'May'],
    "06": ['June', 'Jun'],
    "07": ['July', 'Jul'],
    "08": ['August', 'Aug'],
    "09": ['September', 'Sep'],
    "10": ['October', 'Oct'],
    "11": ['November', 'Nov'],
    "12": ['December', 'Dec']
}


class Calendar:

    def __init__(self, element: Element, *, date_of_birth: str = None):
        element.click()
        if not date_of_birth:
            self.element: Element = browser.element(".react-datepicker")
        else:
            Calendar._set_date(element, date_of_birth)

    @staticmethod
    def _set_date(element: Element, date_of_birth: str):
        element.send_keys(Keys.CONTROL + 'a').send_keys(Calendar._format(date_of_birth))

    @staticmethod
    def _format(date_of_birth: str):
        day: str = date_of_birth[:2]
        month: str = date_of_birth[3:5]
        year: str = date_of_birth[-4:]
        return f'{day} {NAME_OF_MONTH[month][1]} {year}'

    def year(self, param: str):
        self.element.element(".react-datepicker__year-select").click()
        (
            self.element.element(".react-datepicker__year-select")
            .all('option')
            .filtered_by(have.text(param))
            .first.click()
        )
        return self

    def month(self, param: str):
        self.element.element(".react-datepicker__month-select").click()
        (
            self.element.element(".react-datepicker__month-select")
            .all('option')[int(param) - 1].click()
        )
        return self

    def day(self, param: str):
        self.element.element(".react-datepicker__year-select").click()

        (
            self.element.element(".react-datepicker__month")
            .all(".react-datepicker__day:not(.react-datepicker__day--outside-month)")
            .element_by(have.text(str(int(param)))).click()
        )
        return self
