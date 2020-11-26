import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.ContactUsFormPage import ContactUsForm
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class contactFormTest(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.cf = ContactUsForm(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=5)
    def test_verifyPage(self):
        time.sleep(3)
        self.cf.verifyFormPage()

    @pytest.mark.run(order=4)
    def test_clickOnForm(self):
        self.cf.clickOnForm()

    @pytest.mark.run(order=6)
    def test_fillInData(self):
        time.sleep(2)
        self.cf.verifyFormPage()
        self.cf.enterName()
        self.cf.enterEmail()
        self.cf.selectGenderFemale()
        self.cf.enterMessage()
        self.cf.getCaptcha()
        self.cf.passCaptcha()
        self.cf.clickOnPostButton()
