from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time


class Login(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _email = "input.username"  # id
    _password = "input.password"  # id
    _sign_in_button = "#app > div > div > div > div > div > div.css-1d25gjj.e1axqgse0 > div.css-8w8ls9.e1axqgse0 > " \
                      "div.css-4m9xbk.e1axqgse0 > div.css-14y05fe.e1axqgse0 > button > div"  # css
    # cookies
    _decline_button = "div.css-1ynyhby:nth-child(1) > button:nth-child(1) > div:nth-child(1)"  # css

    def fill_in_user_data(self):
        self.sendText("cchiu615@gmail.com", self._email, "id")
        cl.allureLogs("Entered email.")
        self.sendText("Candi_test", self._password, "id")
        cl.allureLogs("Entered password.")

    def decline_cookie(self):
        self.clickOnElement(self._decline_button, "css")
        cl.allureLogs("Declined cookie.")

    def click_sign_in_button(self):
        self.clickOnElement(self._sign_in_button, "css")
        cl.allureLogs("Clicked sign_in button.")
