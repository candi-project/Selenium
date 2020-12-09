import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.PGI_687_Barcode_Configuration import BarcodeConfigurations
import SeleniumFramework.utilities.CustomLogger as cl

# Remember to change the _edit xpath everytime before executing this test.

@pytest.mark.usefixtures("beforeClass", "setUp")
class barcode_configurations(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.bc = BarcodeConfigurations(self.driver)
        self.bp = BaseClass(self.driver)

    @pytest.mark.run(order=1)
    def test_clickOnConfigurations(self):
        time.sleep(3)
        self.bc.clickOnConfiguration()

    @pytest.mark.run(order=2)
    def test_edit_config_file(self):
        self.bc.clickOnEdit()
        self.bc.add_Workflow_Rules()
        self.bc.verify_Workflow_Rules_Saved()
        self.bc.clickOnNext_ConfigTool()
        self.bc.barcode_configuration()
        self.bc.click_On_Barcode_Back()
        self.bc.verify_Workflow_Rules_Content()

    @pytest.mark.run(order=3)
    def test_save_config_file(self):
        self.bc.clickOnNext_ConfigTool()
        self.bc.barcode_configuration()
        self.bc.clickOnBarcodeSaveBtn()
