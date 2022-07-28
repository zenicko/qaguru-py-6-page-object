from selene.core import command
from selene.support.conditions import have
from selene.support.shared import browser

from qaguru_py_6_page_object.controls import calendar, tags_input_advanced
from qaguru_py_6_page_object.controls.calendar import Calendar
from qaguru_py_6_page_object.controls.dropdown import DropDown
from qaguru_py_6_page_object.controls.table import Table
from qaguru_py_6_page_object.helpers import resource, upload_resource



def test_student_registration_form():
    birth_day: str = '01.09.2000'
    browser.open('/automation-practice-form')

    browser.element('#firstName').type('Nick')
    browser.element('#lastName').type('Ivanov')
    browser.element('#userEmail').type('a@a.com')

    GENDER_MALE: str = '[for = gender-radio-1]'
    browser.element(GENDER_MALE).click()

    browser.element("#userNumber").type("1234567890")
    Calendar(browser.element('#dateOfBirthInput')).year('2000').month('09').day('01')
    '''
    # OR the straight path
    Calendar(browser.element('#dateOfBirthInput'), date_of_birth=birth_day)
    '''
    tags_input_advanced.subject = browser.element('#subjectsInput')
    tags_input_advanced.set_subject(name='Maths', by_autocomplete=True)
    tags_input_advanced.set_subject(name='Chemistry', by_autocomplete=False)

    '''
    OR The POM style
    subject = TagsInput(browser.element('#subjectsInput'))
    subject.add('Ma', autocomplete='Maths')
    subject.autocomplete('Chemistry')
    '''

    '''
    # Variable style
    subject = browser.element('#subjectsInput')
    tags_input.add(subject, from_='Ma', to='Maths')
    tags_input.add(subject, from_='Chem', to='Chemistry')
    
    # Straight style
    tags_input.add(browser.element('#subjectsInput'), from_='Ma', to='Maths')
    tags_input.add(browser.element('#subjectsInput'), from_='Chem', to='Chemistry')
    '''

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

    DropDown(browser.element('#state')).select('NCR')
    DropDown(browser.element('#city')).autocomplete('Delhi')
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
    result_table = Table(browser.element("table").element('tbody'))
    result_table.row(0).should_have_exact_texts(['Student Name', 'Nick' + ' ' + 'Ivanov'])
    result_table.row(1).should_have_exact_texts(['Student Email', 'a@a.com'])
    result_table.row(2).should_have_exact_texts(['Gender', 'Male'])
    result_table.row(3).should_have_exact_texts(['Mobile', '1234567890'])

    BIRTH_DAY: str = birth_day[:2] + ' ' + calendar.NAME_OF_MONTH[birth_day[3:5]][0] + ',' + birth_day[6:]
    result_table.row(4).should_have_exact_texts(['Date of Birth', BIRTH_DAY])

    result_table.row(5).should_have_exact_texts(['Subjects', 'Maths, Chemistry'])
    result_table.row(6).should_have_exact_texts(['Hobbies', 'Sports, Reading, Music'])
    result_table.row(7).should_have_exact_texts(['Picture', 'athlant.jpg'])
    result_table.row(8).should_have_exact_texts(['Address', 'Current address'])
    result_table.row(9).should_have_exact_texts(['State and City', 'NCR Delhi'])

    '''
    OR The straight path
    
    table_row = browser.element("table").element('tbody').all("tr")
    table_row[0].all('td').should(have.exact_texts(
        'Student Name',
        'Nick' + ' ' + 'Ivanov'))

    table_row[1].all('td')[1].should(have.exact_text('a@a.com'))

    cells_of_row_should_have_texts(2, 'Gender', 'Male')

    cells_of_row_(index=3, should_have_texts=['Mobile', '1234567890'])

    BIRTH_DAY: str = birth_day[:2] + ' ' + calendar.NAME_OF_MONTH[birth_day[3:5]][0] + ',' + birth_day[6:]
    cells_of_row_(index=4, should_have_texts=['Date of Birth', BIRTH_DAY])
    cells_of_row_(index=5, should_have_texts=['Subjects', 'Maths, Chemistry'])
    cells_of_row_(index=6, should_have_texts=['Hobbies', 'Sports, Reading, Music'])
    cells_of_row_(index=7, should_have_texts=['Picture', 'athlant.jpg'])
    cells_of_row_(index=8, should_have_texts=['Address', 'Current address'])

    assert get_texts_from_row(9) == f'{"State and City"} {"NCR Delhi"}
    '''
