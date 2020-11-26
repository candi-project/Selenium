from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.ContactUsFormPage import ContactUsForm

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("http://dummypoint.com/seleniumtemplate.html", "Selenium Template — DummyPoint")
time.sleep(2)

cf = ContactUsForm(driver)
cf.clickOnForm()
time.sleep(2)
cf.verifyFormPage()
cf.enterName()
cf.enterEmail()
cf.selectGenderFemale()
cf.enterMessage()
cf.getCaptcha()
cf.passCaptcha()
cf.clickOnPostButton()


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

time.sleep(3)
driver.quit()
