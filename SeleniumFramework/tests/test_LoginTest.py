import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class Login(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.lg = SignInProGlove(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_verifyPage(self):
        time.sleep(3)
        self.lg.verifyPage()

    @pytest.mark.run(order=2)
    def test_signIn(self):
        time.sleep(2)
        self.lg.enterCustomerID()
        self.lg.enterEmail()
        self.lg.enterPassword()
        time.sleep(2)
        self.lg.clickLoginBtn()

    @pytest.mark.run(order=3)
    def test_afterLogin(self):
        time.sleep(10)
        self.lg.afterLogin()
        self.lg.releaseNote()
