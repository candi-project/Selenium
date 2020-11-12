from selenium import webdriver
import time

class SafariDriverMac():

    def test(self):
        driver = webdriver.Safari()
        driver.get("https://www.google.com")

sf = SafariDriverMac()
sf.test()
time.sleep(5)