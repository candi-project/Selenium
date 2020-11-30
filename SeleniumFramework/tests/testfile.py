from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove
from SeleniumFramework.pages.Manage import ManageMark

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("https://insight.proglove.com/login", "ProGlove Insight")
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

time.sleep(10)
# lg.afterLogin()
# time.sleep(2)
# lg.releaseNote()

mm = ManageMark(driver)
mm.clickOnScanners()
mm.verifyPage()
mm.clickOnRefresh()
mm.verifyPage()


time.sleep(5)
driver.quit()
