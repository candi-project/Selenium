import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.sign_in_page import SignInPage
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class SignInPageTestRememberMyEmail(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.si = SignInPage(self.driver)

    @pytest.mark.run(order=1)
    def test_fill_in_data(self):
        self.si.enter_user_data_remember_email()
        self.si.enter_authentication_code()

    @pytest.mark.run(order=2)
    def test_after_sign_in(self):
        self.si.after_sign_in()

    @pytest.mark.run(order=3)
    def test_sign_out(self):
        self.si.sign_out()

    @pytest.mark.run(order=4)
    def test_after_sign_out(self):
        self.si.after_sign_out_remember_email()
