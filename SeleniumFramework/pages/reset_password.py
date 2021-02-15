import time

from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class ResetPassword(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values on Reset Password page
    _forgot_your_password = "Forgot your password?"  # link
    _enter_your_email_address = "#recover-form > input"  # css
    _I_am_not_a_robot = "//*[@id='recaptcha-anchor']/div[1]"  # xpath
    _reCaptcha_iFrame = "//*[@id='rc-anchor-container']"  # xpath

    def reset_password(self):
        self.clickOnElement(self._forgot_your_password, "link")
        self.sendText("c@gmail.com", self._enter_your_email_address, "css")

    def check_recaptcha(self):
        iFrame = self.getWebElement(self._reCaptcha_iFrame, "xpath")
        self.driver.switchTo().frame(iFrame)
        self.clickOnElement(self._I_am_not_a_robot, "xpath")

