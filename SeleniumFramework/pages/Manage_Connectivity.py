from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time


class ManageConnectivity(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _connectivityBtn = "Connectivity"  # link
    _checkbox2 = "mat-checkbox-3"  # id
    _editPen = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-table-gateways > mat-card > mat-card-content > table > tbody > tr:nth-child(1) > td.action-column.mat-cell.cdk-column-action.mat-column-action.ng-star-inserted > a > img"  # css

    def clickOnConnectivity(self):
        self.clickOnElement(self._connectivityBtn, "link")

    def selectOnCheckBox(self):
        time.sleep(10)
        self.clickOnElement(self._checkbox2, "id")
        self.isElementSelected(self._checkbox2, "id")


