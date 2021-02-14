from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class SignUpPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values in Sign up page
    _sign_up_link = "Sign up"  # link
    _first_name = "signup-first"  # id
    _last_name = "signup-last"  # id
    _email = "signup-email"  # id
    _password = "signup-password"  # id
    _next_button = "#authentication > div > div.getting-started-footer > div.getting-started-center-aligned > " \
                   "div.buttons > button"  # css

    _lower_case_letter = "#passphrase-form > ul > li.passcode-low.checked"  # css
    _upper_case_letter = "#passphrase-form > ul > li.passcode-cap.checked"  # css
    _special_character = "#passphrase-form > ul > li.passcode-spec.checked"  # css
    _numbers = "#passphrase-form > ul > li.passcode-num.checked"  # css

    _alert_same_email = "sysMsg"  # id

    # Locators  values after signup
    _invite_your_team = "invitation-header"  # class
    _invitation_content = "invitation-content"  # class

    def click_sign_up_link(self):
        self.clickOnElement(self._sign_up_link, "link")

    def fill_in_form_same_email(self):
        self.sendText("Candi", self._first_name, "id")
        self.sendText("Chiu", self._last_name, "id")
        self.sendText("cchiu615@gmail.com", self._email, "id")
        self.sendText("0Apob6059!", self._password, "id")

    def fill_in_form_new_email(self):
        self.sendText("Candi", self._first_name, "id")
        self.sendText("Chiu", self._last_name, "id")
        self.sendText("cc@gmail.com", self._email, "id")
        self.sendText("0Apob6059!", self._password, "id")

    def check_password(self):
        self.isElementEnabled(self._lower_case_letter, "css")
        self.isElementEnabled(self._upper_case_letter, "css")
        self.isElementEnabled(self._special_character, "css")
        self.isElementEnabled(self._numbers, "css")

    def after_sign_up(self):
        self.clickOnElement(self._next_button, "css")
        self.isElementDisplayed(self._invite_your_team, "class")
        self.isElementDisplayed(self._invitation_content, "class")

    def after_sign_up_same_email(self):
        self.clickOnElement(self._next_button, "css")
        self.isElementDisplayed(self._alert_same_email, "id")
