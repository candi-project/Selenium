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
        cl.allureLogs("User name sent.- cchiu615@gmail.com")

        self.sendText("0Apob6059!", self._password, "id")
        cl.allureLogs("Password sent.- 0Apob6059!")

        self.clickOnElement(self._sign_in_to_account, "css")
        cl.allureLogs("Clicked on element-sign-in-to-account.")

    def enter_user_data_remember_email(self):
        self.sendText("cchiu615@gmail.com", self._user_name, "id")
        cl.allureLogs("User name sent.- cchiu615@gmail.com")

        self.sendText("0Apob6059!", self._password, "id")
        cl.allureLogs("Password sent.- 0Apob6059!")

        self.clickOnElement(self._remember_email_address, "id")
        cl.allureLogs("Clicked on element-Remember my email address")

        self.clickOnElement(self._sign_in_to_account, "css")
        cl.allureLogs("Clicked on element-sign-in-to-account.")

    def enter_authentication_code(self):
        time.sleep(5)
        code = sms_authentication.get_verification_code()
        self.sendText(code, self._enter_authentication_code, "css")
        cl.allureLogs("Text sent-authentication code.")

        self.clickOnElement(self._verify_button, "css")
        cl.allureLogs("Clicked on element-verify button.")

    def after_sign_in(self):
        time.sleep(5)
        self.isElementDisplayed(self._tool_bar, "css")
        cl.allureLogs("Displayed element-Tool Bar.")

    def sign_out(self):
        time.sleep(5)
        self.clickOnElement(self._tool_bar_settings, "id")
        cl.allureLogs("Clicked on element-tool bar settings.")

        self.clickOnElement(self._settings_profile, "id")
        cl.allureLogs("Clicked on element-settings profile.")
        time.sleep(1)

        self.clickOnElement(self._sign_out_link, "link")
        cl.allureLogs("Clicked on element-sign out link.")

        self.clickOnElement(self._sign_out_button, "css")
        cl.allureLogs("Clicked on element-sign out button.")

    def after_sign_out_remember_email(self):
        time.sleep(2)
        user_email = self.getText(self._user_name, "id")
        cl.allureLogs("Got text-user name.")

        if user_email == "cchiu615@gmail.com":
            assert True
