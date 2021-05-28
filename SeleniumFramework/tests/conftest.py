import time
import pytest
from SeleniumFramework.base.DriverClass import WebDriverClass
from SeleniumFramework.base.BasePage import BaseClass

@pytest.yield_fixture(scope="class")
def beforeClass(request):
    print("Before class.")
    driver1 = WebDriverClass()
    driver = driver1.getWebDriver("chrome")
    bp = BaseClass(driver)
    bp.launchWebPage("https://you.sharecare.com/", "Sharecare")
    driver.maximize_window()

    if request.cls is not None:
        request.cls.driver = driver
    yield driver
    time.sleep(5)
    driver.quit()
    print("After class.")

@pytest.yield_fixture()
def setUp():
    print("This is a setup guide.")
    yield
    print("After method.")