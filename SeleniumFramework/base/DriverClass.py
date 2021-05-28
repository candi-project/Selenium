from selenium import webdriver
import SeleniumFramework.utilities.CustomLogger as cl

class WebDriverClass:
    log = cl.customLogger()

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(executable_path="/Users/candichiu/Documents/Git/Selenium/driver/chromedriver91")
            self.log.info("Chrome driver is initializing.")

        elif browserName == "safari":
            driver = webdriver.Safari()
            self.log.info("Safari driver is initializing.")

        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="/Users/candichiu/Documents/Git/Selenium/driver/geckodriver-3")
            self.log.info("Firefox driver is initializing.")

        return driver

