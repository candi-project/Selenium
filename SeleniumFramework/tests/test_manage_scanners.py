import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.Manage_Scanners import ManageScanners
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class Scanners(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.ms = ManageScanners(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_clickOnScanners(self):
        time.sleep(3)
        self.ms.clickOnScanners()

    @pytest.mark.run(order=2)
    def test_verifyPage(self):
        self.ms.verifyPage()

    @pytest.mark.run(order=3)
    def test_clickOnRefresh(self):
        self.ms.clickOnRefresh()

    @pytest.mark.run(order=4)
    def test_verifyPage2(self):
        self.ms.verifyPage()
