import time

from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages import sms_authentication
import SeleniumFramework.utilities.CustomLogger as cl


class SignInPage(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values on Sign in page
    _user_name = "signin-email"  # id
    _password = "signin-password"  # id
    _sign_in_to_account = "#signin-form > button"  # css
    _enter_authentication_code = "#authcode-form > input"  # css
    _verify_button = "#authcode-form > button"  # css
    _tool_bar = "#header > div.toolbar.button-group"  # css
    _remember_email_address = "signin-remember"  # id
    _tool_bar_settings = "toolbar-settings"  # id
    _settings_profile = "profileSettingsTrigger"  # id
    _sign_out_link = "Sign Out"  # link
    _sign_out_button = "#modal > div > div > div > div > div > div.modal-content-buttons.buttons > " \
                       "button.tempo-btn.button.done.positive.tempo-btn--primary"  # css

    def enter_user_data(self):
        self.sendText("cchiu615@gmail.com", self._user_name, "id")
        self.sendText("0Apob6059!", self._password, "id")
        self.clickOnElement(self._sign_in_to_account, "css")

    def enter_user_data_remember_email(self):
        self.sendText("cchiu615@gmail.com", self._user_name, "id")
        self.sendText("0Apob6059!", self._password, "id")
        self.clickOnElement(self._remember_email_address, "id")
        self.clickOnElement(self._sign_in_to_account, "css")

    def enter_authentication_code(self):
        time.sleep(5)
        code = sms_authentication.get_verification_code()
        self.sendText(code, self._enter_authentication_code, "css")
        self.clickOnElement(self._verify_button, "css")

    def after_sign_in(self):
        time.sleep(5)
        self.isElementDisplayed(self._tool_bar, "css")

    def sign_out(self):
        time.sleep(5)
        self.clickOnElement(self._tool_bar_settings, "id")
        self.clickOnElement(self._settings_profile, "id")
        time.sleep(1)
        self.clickOnElement(self._sign_out_link, "link")
        self.clickOnElement(self._sign_out_button, "css")

    def after_sign_out_remember_email(self):
        time.sleep(2)
        user_email = self.getText(self._user_name, "id")
        if user_email == "cchiu615@gmail.com":
            assert True
