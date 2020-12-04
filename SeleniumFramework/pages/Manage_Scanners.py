from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time


class ManageScanners(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _manageScanners = "Scanners"  # link
    _lastConnectivityDeviceName = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-graph-active-devices > mat-card > mat-card-content > table > tbody > tr:nth-child(1) > td.mat-cell.cdk-column-last_connected_gateway_name.mat-column-last_connected_gateway_name.ng-star-inserted"  # css
    _refreshButton = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-graph-active-devices > mat-card > div > div > app-refresh-button > div"  # css

    def clickOnScanners(self):
        self.clickOnElement(self._manageScanners, "link")
        cl.allureLogs("Clicked on Scanners.")

    def verifyPage(self):
        time.sleep(10)
        element = self.isElementDisplayed(self._lastConnectivityDeviceName, "css")
        assert element == True
        time.sleep(10)
        ele = self.getWebElement(self._lastConnectivityDeviceName, "css")
        data = ele.text
        if data != "Loading...":
            print("Last Connectivity Device Name: ", data)
            assert True
        else:
            print("Last Connectivity Device Name: ", data)
            assert False

        cl.allureLogs("Scanners page is verified.")

    def clickOnRefresh(self):
        self.clickOnElement(self._refreshButton, "css")
        cl.allureLogs("Clicked on Refresh Button.")