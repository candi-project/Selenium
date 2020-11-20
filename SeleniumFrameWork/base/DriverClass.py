from selenium import webdriver

class WebDriverClass:

    def getWebDriver(self, browserName):
        driver = None
        if browserName == "chrome":
            driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
        elif browserName == "safari":
            driver = webdriver.Safari()
        elif browserName == "firefox":
            driver = webdriver.Firefox(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/geckodriver")

        return driver

