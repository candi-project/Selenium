import os
import time
from pathlib import Path
from traceback import print_stack

import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.base.BasePage import BaseClass


class ManageConnectivity(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _connectivityBtn = "Connectivity"  # link
    _checkbox2 = "mat-checkbox-3"  # id
    _editPen = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-table-gateways > mat-card > mat-card-content > table > tbody > tr:nth-child(1) > td.action-column.mat-cell.cdk-column-action.mat-column-action.ng-star-inserted > a > img"  # css
    _registrationFile = "#mat-expansion-panel-header-0 > span > mat-panel-description > div > div:nth-child(2) > mat-icon > svg"  # css

    def clickOnConnectivity(self):
        self.clickOnElement(self._connectivityBtn, "link")

    def selectOnCheckBox(self):
        time.sleep(10)
        self.clickOnElement(self._checkbox2, "id")
        self.isElementSelected(self._checkbox2, "id")

    def clickOnRegistrationFile(self):
        self.clickOnElement(self._registrationFile, "css")
        time.sleep(5)

    def is_download_finished(self, temp_folder):

        chrome_temp_file = sorted(Path(temp_folder).glob('insight_provisioning*'))
        downloaded_files = sorted(Path(temp_folder).glob('insight_provisioning*'))
        if len(downloaded_files) >= 1:
            self.log.info("File is downloaded.")
            print(len(chrome_temp_file))
            print(len(downloaded_files))
            assert True

        else:
            self.log.info("File is not downloaded.")
            print(len(chrome_temp_file))
            print(len(downloaded_files))
            print_stack()
            assert False

    def remove_download(self, path):
        time.sleep(3)
        # path = "/home/candi/Downloads/insight_provisioning.zip"
        if os.path.exists(path):
            os.remove(path)
            print("The file is removed.")
        else:
            print("The file does not exist")
