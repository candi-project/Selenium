from SeleniumFramework.base.DriverClass import WebDriverClass
import time
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.login_page import Login

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")

bp = BaseClass(driver)
bp.launchWebPage("https://you.sharecare.com/", "Sharecare")
driver.maximize_window()


lg = Login(driver)
lg.fill_in_user_data()
lg.decline_cookie()
lg.click_sign_in_button()

time.sleep(10)
driver.quit()
