import os
import time
from pathlib import Path
from traceback import print_stack

import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.base.BasePage import BaseClass
from selenium.webdriver.support.select import Select


class ManageConnectivity2(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _connectivityBtn = "Connectivity"  # link
    _checkbox2 = "mat-checkbox-3"  # id
    _editPen = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-table-gateways > mat-card > mat-card-content > table > tbody > tr:nth-child(2) > td.mat-cell.cdk-cell.action-column.cdk-column-action.mat-column-action.ng-star-inserted > a > img"  # css
    _registrationFile = "#mat-expansion-panel-header-0 > span > mat-panel-description > div > div:nth-child(2) > mat-icon > svg"  # css
    _station_name = "#editDialog > form > div:nth-child(2) > app-text-input > div > div.input-wrapper > input"  # css
    _device_name = "#editDialog > form > div:nth-child(4) > app-text-input > div > div.input-wrapper > input"  # css
    _edit_save_button = "#save > button"  # css
    _edit_option_use_case = "#usecase-selector > div > div.input-wrapper.ng-star-inserted > div.options.ng-star-inserted"  # css
    _edit_select_use_case = "#usecase-selector > div > div.input-wrapper.ng-star-inserted > div"  # css
    _packing = "#usecase-selector > div > div.input-wrapper.ng-star-inserted > div.options.ng-star-inserted > div:nth-child(2)"  # css
    _filter = "#gtw-filter-list-button"  # css

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

    def click_on_edit(self):
        self.clickOnElement(self._editPen, "css")
        time.sleep(1)

    def edit_device_content(self):
        self.clickOnElement(self._station_name, "css")
        self.sendText("test_station_name", self._station_name, "css")
        self.clickOnElement(self._device_name, "css")
        self.sendText("ProGlove", self._device_name, "css")
        time.sleep(2)
        self.clickOnElement(self._edit_select_use_case, "css")
        self.clickOnElement(self._packing, "css")

        # el = self.getWebElements(self._edit_option_use_case, "css")
        #
        # for rbutton in el:
        #     rbutton_t = rbutton.text
        #     print(rbutton_t)
        #     # rbutton.click()
        #     # self.clickOnElement(self._edit_select_use_case, "css")
        #     time.sleep(6)
        #
        #     if "Packing" in rbutton_t:
        #         rbutton.click()
        #         time.sleep(6)
        #         # print("Is selected: ", rbutton.is_selected())
        #         break

        # for option in el:
        #     option_t = option.text
        #     print(option_t)
        #     if option_t == 'Packing':
        #         option.click()
        #         break

        self.clickOnElement(self._edit_save_button, "css")
