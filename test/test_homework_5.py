from selene import browser, have, be, by
import os

FILE = 'test.png'


def test_open(preparations):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title_containing('DEMOQA'))
    browser.element("[id=firstName]").should(be.blank).type("Alesya")
    browser.element("[id=lastName]").should(be.blank).type("Family")
    browser.element("[id=userEmail]").should(be.blank).type("vititi5980@vootin.com")
    browser.element("[for='gender-radio-2']").click()
    browser.element("[id=userNumber]").should(be.blank).type("89234563234")
    browser.element("[id=dateOfBirthInput]").click()
    browser.element('.react-datepicker__month-select').click()
    browser.element('option[value="1"]').click()
    browser.element('.react-datepicker__year-select').click()
    browser.element('option[value="2008"]').click()
    browser.element('[class="react-datepicker__day react-datepicker__day--013"]').click()
    browser.element('[id="subjectsInput"]').type('e').press_enter()
    browser.element("[for=hobbies-checkbox-2]").click()
    browser.element('#uploadPicture').send_keys(os.getcwd() + f'/resources/{FILE}')
    browser.element("[id=currentAddress]").should(be.blank).type("test test test test test")
    browser.element("[id=state]").click()
    browser.element("[id=react-select-3-option-1]").click()
    browser.element("[id=city]").click()
    browser.element("[id=react-select-4-option-0]").click()
    browser.element("[id=submit]").submit()

    # проверка формы

    browser.element('#example-modal-sizes-title-lg').should(have.text('Thanks for submitting the form'))
    browser.all('tr').element_by_its('td', have.text('Student Name')).all('td')[1].should(have.text('Alesya Family'))
    browser.all('tr').element_by_its('td', have.text('Student Email')).all('td')[1].should(have.text(
        'vititi5980@vootin.com'))
    browser.all('tr').element_by_its('td', have.text('Gender')).all('td')[1].should(have.text('Female'))
    browser.all('tr').element_by_its('td', have.text('Mobile')).all('td')[1].should(have.text('8923456323'))
    browser.all('tr').element_by_its('td', have.text('Date of Birth')).all('td')[1].should(
        have.text('13 February,2008'))
    browser.all('tr').element_by_its('td', have.text('Subjects')).all('td')[1].should(have.text('English'))
    browser.all('tr').element_by_its('td', have.text('Hobbies')).all('td')[1].should(have.text('Reading'))
    browser.all('tr').element_by_its('td', have.text('Picture')).all('td')[1].should(have.text('test.png'))
    browser.all('tr').element_by_its('td', have.text('Address')).all('td')[1].should(
        have.text('test test test test test'))
    browser.all('tr').element_by_its('td', have.text('State and City')).all('td')[1].should(
        have.text('Uttar Pradesh Agra'))
    browser.element('#closeLargeModal').click()
