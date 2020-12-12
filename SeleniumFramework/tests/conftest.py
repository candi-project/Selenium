import time
import pytest
from SeleniumFramework.base.DriverClass import WebDriverClass
from SeleniumFramework.base.BasePage import BaseClass
from SeleniumFramework.pages.LoginPage import SignInProGlove

@pytest.yield_fixture(scope="class")
def beforeClass(request):
    print("Before class.")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://d36o9jt7i3m1do.cloudfront.net/home", "ProGlove Insight")
    if request.cls is not None:
        request.cls.driver = driver

    lg = SignInProGlove(driver)
    time.sleep(3)
    lg.verifyPage()
    time.sleep(2)
    lg.enterCustomerID()
    lg.enterEmail()
    lg.enterPassword()
    time.sleep(2)
    lg.clickLoginBtn()
    time.sleep(10)
    lg.afterLogin()
    #lg.releaseNote()

    yield driver
    time.sleep(5)
    driver.quit()
    print("After class.")

@pytest.yield_fixture()
def setUp():
    print("This is a setup guide.")
    yield
    print("After method.")



