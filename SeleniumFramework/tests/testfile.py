from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.sign_up_page import SignUpPage
from SeleniumFramework.pages.sign_in_page import SignInPage
from SeleniumFramework.pages.reset_password import ResetPassword

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("https://my.symphony.com/", "Symphony | Secure Seamless Communication")
driver.maximize_window()
time.sleep(2)

# su = SignUpPage(driver)
# su.click_sign_up_link()
# su.fill_in_form()
# su.check_password()
# su.after_sign_up_same_email()

# si = SignInPage(driver)
# si.enter_user_data()
# si.enter_authentication_code()
# si.after_sign_in()

re = ResetPassword(driver)
re.reset_password()
re.check_recaptcha()

# cf = ContactUsForm(driver)
# cf.clickOnForm()
# time.sleep(2)
# cf.verifyFormPage()
# cf.enterName()
# cf.enterEmail()
# cf.selectGenderFemale()
# cf.enterMessage()
# cf.getCaptcha()
# cf.passCaptcha()
# cf.clickOnPostButton()


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

# bp.clickOnElement("DragAndDro", "link")


# log = cl.customLogger()
# log.info("Web page launched.")

time.sleep(3)
driver.quit()
