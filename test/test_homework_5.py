from selene import browser, have, be, by
import os

FILE = 'test.png'


def test_open(preparations):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.should(have.title_containing('DEMOQA'))
    browser.element("[id=firstName]").should(be.blank).type("First Name")
    browser.element("[id=lastName]").should(be.blank).type("Last Name")
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

