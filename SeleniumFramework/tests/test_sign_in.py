import pytest
import unittest

from SeleniumFramework.pages.login_page import Login


@pytest.mark.usefixtures("beforeClass", "setUp")
class SignIn(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.si = Login(self.driver)

    @pytest.mark.run(order=1)
    def test_enter_user_data(self):
        self.si.fill_in_user_data()

    @pytest.mark.run(order=2)
    def test_decline_cookie(self):
        self.si.decline_cookie()

    @pytest.mark.run(order=3)
    def test_click_sign_in_button(self):
        self.si.click_sign_in_button()
