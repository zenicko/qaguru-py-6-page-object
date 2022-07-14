import os

from selene.core import command
from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser

NAME_OF_MONTH = {
    "01": "January",
    "02": "February",
    "03": "March",
    "04": "April",
    "05": "May",
    "06": "June",
    "07": "July",
    "08": "August",
    "09": "September",
    "10": "October",
    "11": "November",
    "12": "December"
}


def test_student_registration_form():
    birth_day: str = "01.09.2000"
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Nick')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('a@a.com')
    browser.element('[for = gender-radio-1]').click()
    browser.element("#userNumber").type("1234567890")

    browser.element('#dateOfBirthInput').click()
    calendar: Element = browser.element(".react-datepicker")

    calendar.element(".react-datepicker__month-select").click()
    (
        calendar.element(".react-datepicker__month-select")
        .all('option')[int(birth_day[3:5]) - 1].click()
    )

    calendar.element(".react-datepicker__year-select").click()
    (
        calendar.element(".react-datepicker__year-select")
        .all('option')
        .filtered_by(have.text(birth_day[6:]))
        .first.click()
    )
    calendar.element(".react-datepicker__year-select").click()

    (
        calendar.element(".react-datepicker__month")
        .all(".react-datepicker__day:not(.react-datepicker__day--outside-month)")
        .element_by(have.text(str(int(birth_day[:2])))).click()
    )

    browser.element("#subjectsInput").click().type('Maths')
    browser.element('#react-select-2-option-0').click()

    browser.element('#submit').perform(command.js.scroll_into_view)

    SET_HOBBIES_SPORT: str = '[for = hobbies-checkbox-1]'
    browser.element(SET_HOBBIES_SPORT).click()

    ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    (
        browser.element("#uploadPicture")
        .send_keys(os.path.join(ROOT_DIR, "requirements.txt"))
    )

    browser.element("#currentAddress").type("Current address")
    SET_STATE_OF_NCR: str = '#react-select-3-option-0'
    (
        browser.element("#state")
        .click()
        .element(SET_STATE_OF_NCR)
        .click()
    )

    SET_STATE_OF_DELHI: str = '#react-select-4-option-0'
    (
        browser.element("#city")
        .click()
        .element(SET_STATE_OF_DELHI)
        .click()
    )
    browser.element('#submit').click()

    table_row = browser.element("table").element('tbody').all("tr")
    table_row[0].all('td')[1].should(have.text('Nick' + ' ' + 'Ivanov'))
    table_row[1].all('td')[1].should(have.text('a@a.com'))
    table_row[2].all('td')[1].should(have.text('Male'))
    table_row[3].all('td')[1].should(have.text('1234567890'))
    BIRTH_DAY: str = birth_day[:2] + ' ' + NAME_OF_MONTH[birth_day[3:5]] + ',' + birth_day[6:]
    table_row[4].all('td')[1].should(have.text(BIRTH_DAY))

    assert table_row[5].all('td').element_by(have.text('Maths')).text == 'Maths'
    assert table_row[6].all('td').element_by(have.text('Sports')).text == 'Sports'
    assert table_row[7].all('td').element_by(have.text('requirements.txt')).text == 'requirements.txt'
    assert table_row[8].all('td').element_by(have.text('Current address')).text == 'Current address'
    assert table_row[9].all('td').element_by(have.text('NCR Delhi')).text == 'NCR Delhi'
