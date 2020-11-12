from selenium import webdriver

class RunFFRest():

    def testMethod(self):
        driver = webdriver.Firefox()
        driver.get("https://www.google.com")


ff = RunFFRest()
ff.testMethod()