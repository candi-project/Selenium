import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.EnterTextPage import EnterText
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class EnterTextPage(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.et = EnterText(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_verifyPage(self):
        time.sleep(2)
        self.et.verifySection()

    @pytest.mark.run(order=2)
    def test_enterText(self):
        self.et.enterText()

    @pytest.mark.run(order=3)
    def test_clickSubmit(self):
        time.sleep(1)
        self.et.clickOnSubmitButton()
