from SeleniumFrameWork.base.DriverClass import WebDriverClass
import time
import SeleniumFrameWork.utilities.CustomLogger as cl

wd = WebDriverClass()
driver = wd.getWebDriver("chrome")
driver.get("http://dummypoint.com/Windows.html")

log = cl.customLogger()
log.info("Web page launched.")

time.sleep(2)
driver.quit()