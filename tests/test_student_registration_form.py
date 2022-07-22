from selene.core import command
from selene.core.entity import Element
from selene.support.conditions import have
from selene.support.shared import browser

from qaguru_py_6_page_object.controls import dropdown
from qaguru_py_6_page_object.controls.table import cells_of_row_should_have_texts, cells_of_row_, get_texts_from_row
from qaguru_py_6_page_object.controls import tags_input
from qaguru_py_6_page_object.helpers import resource, upload_resource

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

    GENDER_MALE: str = '[for = gender-radio-1]'
    browser.element(GENDER_MALE).click()

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

    tags_input.add('#subjectsInput', from_='Ma', to='Maths')
    tags_input.add('#subjectsInput', from_='Chem', to='Chemistry')

    '''
    # Like a workaround and KISS style
    browser.element('#subjectsInput').type('Maths').press_enter()
    browser.element('#subjectsInput').type('Chemistry')
    browser.element('#react-select-2-option-0').click()
    '''

    browser.element('#submit').perform(command.js.scroll_into_view)

    hobby_sport: str = '[for = hobbies-checkbox-1]'
    browser.element('#hobbiesWrapper').element(hobby_sport).click()
    hobby_reading: str = '[for = hobbies-checkbox-2]'
    browser.element('#hobbiesWrapper').element(hobby_reading).click()
    (
        browser.element('#hobbiesWrapper')
        .all('.custom-checkbox')
        .element_by(have.exact_text('Music')).click()
    )

    browser.element("#uploadPicture").send_keys(resource('corn.jpg'))
    browser.element("#uploadPicture").perform(upload_resource('athlant.jpg'))

    browser.element("#currentAddress").type("Current address")

    '''
    # Step 1
    select.select_by_choosing(browser.element('#state'), option='NCR')
    select.select_by_autocomplete(browser.element('#city'), option='Delhi')
    
    # Step 2
    select.by_choosing(browser.element('#state'), option='NCR')
    select.by_autocomplete(browser.element('#city'), option='Delhi')
    '''
    dropdown.select(browser.element('#state'), option='NCR')
    dropdown.autocomplete(browser.element('#city'), option='Delhi')
    '''
    # Like a workaround and KISS style
    SET_STATE_OF_NCR: str = '#react-select-3-option-0'
    (
        browser.element("#state")
        .click()
        .element(SET_STATE_OF_NCR)
        .click()
    )

    city: str = 'Delhi'
    (
        browser.element("#city")
        .element('input')
        .type(city)
        .press_tab()
    )
    '''

    browser.element('#submit').click()

    # Assert
    table_row = browser.element("table").element('tbody').all("tr")
    table_row[0].all('td').should(have.exact_texts(
        'Student Name',
        'Nick' + ' ' + 'Ivanov'))

    table_row[1].all('td')[1].should(have.exact_text('a@a.com'))

    cells_of_row_should_have_texts(2, 'Gender', 'Male')

    cells_of_row_(index=3, should_have_texts=['Mobile', '1234567890'])

    BIRTH_DAY: str = birth_day[:2] + ' ' + NAME_OF_MONTH[birth_day[3:5]] + ',' + birth_day[6:]
    cells_of_row_(index=4, should_have_texts=['Date of Birth', BIRTH_DAY])
    cells_of_row_(index=5, should_have_texts=['Subjects', 'Maths, Chemistry'])
    cells_of_row_(index=6, should_have_texts=['Hobbies', 'Sports, Reading, Music'])
    cells_of_row_(index=7, should_have_texts=['Picture', 'athlant.jpg'])
    cells_of_row_(index=8, should_have_texts=['Address', 'Current address'])

    assert get_texts_from_row(9) == f'{"State and City"} {"NCR Delhi"}'
