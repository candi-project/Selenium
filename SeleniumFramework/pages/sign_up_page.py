from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class SignUpPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values on Sign up page
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
        cl.allureLogs("Clicked on element-sign up link.")

    def fill_in_form_same_email(self):
        self.sendText("Candi", self._first_name, "id")
        cl.allureLogs("Text sent-Candi.")

        self.sendText("Chiu", self._last_name, "id")
        cl.allureLogs("Text sent-Chiu.")

        self.sendText("cchiu615@gmail.com", self._email, "id")
        cl.allureLogs("Text sent-cchiu615@gmail.com.")

        self.sendText("0Apob6059!", self._password, "id")
        cl.allureLogs("Text sent-0Apob6059!.")

    def fill_in_form_new_email(self):
        self.sendText("Candi", self._first_name, "id")
        cl.allureLogs("Text sent-Candi.")

        self.sendText("Chiu", self._last_name, "id")
        cl.allureLogs("Text sent-Chiu.")

        self.sendText("cc@gmail.com", self._email, "id")
        cl.allureLogs("Text sent-cc@gmail.com.")

        self.sendText("0Apob6059!", self._password, "id")
        cl.allureLogs("Text sent-0Apob6059!.")

    def check_password(self):
        self.isElementEnabled(self._lower_case_letter, "css")
        cl.allureLogs("Element enabled-lower case letter.")

        self.isElementEnabled(self._upper_case_letter, "css")
        cl.allureLogs("Element enabled-upper case letter.")

        self.isElementEnabled(self._special_character, "css")
        cl.allureLogs("Element enabled-special character.")

        self.isElementEnabled(self._numbers, "css")
        cl.allureLogs("Element enabled-numbers.")

    def after_sign_up(self):
        self.clickOnElement(self._next_button, "css")
        cl.allureLogs("Element clicked-next button.")

        self.isElementDisplayed(self._invite_your_team, "class")
        cl.allureLogs("Element displayed-invite your team.")

        self.isElementDisplayed(self._invitation_content, "class")
        cl.allureLogs("Element displayed-invitation content.")

    def after_sign_up_same_email(self):
        self.clickOnElement(self._next_button, "css")
        cl.allureLogs("Element clicked-next button.")

        self.isElementDisplayed(self._alert_same_email, "id")
        cl.allureLogs("Element displayed-same email alert.")
