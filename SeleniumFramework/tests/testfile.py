from selenium.webdriver.common.by import By

from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.Manage_Scanners import ManageScanners
from SeleniumFramework.pages.Manage_Connectivity import ManageConnectivity
from SeleniumFramework.pages.PGI_687_Barcode_Configuration import BarcodeConfigurations
from SeleniumFramework.pages.PGI_248_Open_Source_License import OpenSourceLicense
wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("https://pr-728.d1n9mbbc8uh0el.amplifyapp.com/home", "ProGlove Insight")
time.sleep(2)

lg = SignInProGlove(driver)
#lg.verifyPage()
lg.enterCustomerID()
lg.enterEmail()
lg.enterPassword()
time.sleep(3)
lg.clickLoginBtn()

op = OpenSourceLicense(driver)
op.click_open_source_license()
op.click_download_mark()
op.click_download_gateway()
time.sleep(6)
op.is_download_finished("/home/candi/Downloads/")
op.remove_download("/home/candi/Downloads/mark_legal_notice_11_08_2020.pdf")



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

# bc = BarcodeConfigurations(driver)
# bc.clickOnConfiguration()
# bc.scrollToCreate()
#
# ele_r = driver.find_elements(By.XPATH, "//mat-radio-button[@class='mat-radio-button mat-accent']")
# time.sleep(3)
#
# for rbutton in ele_r:
#     rbutton_t = rbutton.text
#     print(rbutton_t)
#
#     if rbutton_t == "Insight Mobile (iOS)":
#         rbutton.click()
#         time.sleep(6)
#         print("Is selected: ", rbutton.is_selected())
#         break
#bc.choose_Connectivity_Option()
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

# bc.clickOnEdit()
# bc.add_Workflow_Rules_Large_File()
# bc.clickOnNext_ConfigTool()
# bc.barcode_configuration_error()


time.sleep(5)
driver.quit()
