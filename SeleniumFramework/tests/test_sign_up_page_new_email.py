import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.sign_up_page import SignUpPage
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class SignUpPageTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.su = SignUpPage(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_sign_up_new_email(self):
        time.sleep(2)
        self.su.click_sign_up_link()
        self.su.fill_in_form_new_email()
        self.su.check_password()

    @pytest.mark.run(order=2)
    def test_after_sign_up(self):
        self.su.after_sign_up()
