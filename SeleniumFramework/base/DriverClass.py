from selenium import webdriver
import SeleniumFramework.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver87")
            self.log.info("Chrome driver is initializing.")

        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari driver is initializing.")

        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/geckodriver")
            self.log.info("Firefox driver is initializing.")

        return driver

