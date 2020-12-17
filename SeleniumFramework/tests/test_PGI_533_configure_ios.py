import pytest
import unittest
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.PGI_533_Configure_iOS import BarcodeConfigurations
import SeleniumFramework.utilities.CustomLogger as cl


@pytest.mark.usefixtures("beforeClass", "setUp")
class barcode_configurations(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classObjects(self):
        self.bc = BarcodeConfigurations(self.driver)

    @pytest.mark.run(order=1)
    def test_clickOnConfigurations(self):
        time.sleep(3)
        self.bc.clickOnConfiguration()

    @pytest.mark.run(order=2)
    def test_create_config_file(self):
        self.bc.scrollToCreate()
        self.bc.choose_Connectivity_Option()
        self.bc.clickOnNext_Android()
        self.bc.clickOnNext_ConfigTool()
        self.bc.assign_A_Name()
        self.bc.clickOnNext_afterAName()
        #self.bc.barcode_configuration()
        self.bc.barcode_configuration_error()
        self.bc.clickOnBarcodeSaveBtn()
        self.bc.successful_saved_notification()
        #self.bc.verify_configfile_saved()

