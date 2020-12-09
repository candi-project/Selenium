from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.Manage_Scanners import ManageScanners
from SeleniumFramework.pages.Manage_Connectivity import ManageConnectivity
from SeleniumFramework.pages.PGI_687_Barcode_Configuration import BarcodeConfigurations
wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("https://pr-666.d1n9mbbc8uh0el.amplifyapp.com/devices/configuration/details", "ProGlove Insight")
time.sleep(2)

lg = SignInProGlove(driver)
lg.verifyPage()
lg.enterCustomerID()
lg.enterEmail()
lg.enterPassword()
time.sleep(3)
lg.clickLoginBtn()



# ele = bp.getWebElement("user_input","id")
# ele.send_keys("Candi")

# ele = bp.waitForElement("user_inpu","id")
# ele.send_keys("Candi")
# ele = bp.isElementDisplayed("user_input", "id")
# print(ele)
# time.sleep(1)
# bp.sendText("Hello", "user_input", "id")
# time.sleep(2)
# ele2 = bp.getText("#app > div > div.main-content > section > div.section-body > div > form > label:nth-child(15) > b","css")
# print(ele2)
# time.sleep(1)
# bp.scrollTo("btnContactUs", "id")

#bp.clickOnElement("DragAndDro", "link")


# log = cl.customLogger()
# log.info("Web page launched.")

# time.sleep(10)
# lg.afterLogin()
# time.sleep(2)
# lg.releaseNote()

# mc = ManageConnectivity(driver)
# mc.clickOnConnectivity()
# mc.selectOnCheckBox()
# mc.clickOnRegistrationFile()
# mc.remove_download("/home/candi/Downloads/insight_provisioning.zip")

bc = BarcodeConfigurations(driver)
bc.clickOnConfiguration()
# bc.scrollToCreate()
# bc.choose_Connectivity_Option()
# bc.clickOnNext_Android()
# bc.clickOnNext_ConfigTool()
# bc.assign_A_Name()
# bc.clickOnNext_afterAName()
# bc.barcode_configuration()
# bc.clickOnSaveBtn()
# bc.successful_saved_notification()
# bc.verify_configfile_saved()
# bc.clickOnEdit()
# bc.add_Workflow_Rules()
# bc.verify_Workflow_Rules_Saved()
# bc.clickOnNext_ConfigTool()
# bc.barcode_configuration()
# bc.click_On_Barcode_Back()
# bc.verify_Workflow_Rules_Content()

bc.clickOnEdit()
bc.add_Workflow_Rules_Large_File()
bc.clickOnNext_ConfigTool()
bc.barcode_configuration_error()


time.sleep(5)
driver.quit()
