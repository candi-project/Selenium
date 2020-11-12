from selenium import webdriver
from selenium.webdriver.common.by import By

class ByDemo():

    def test(self):
        baseUrl="https://insight.proglove.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        ElementByClass = driver.find_element(By.CLASS_NAME, "big-icon")


        if ElementByClass is not None:
            print("We found an element by Class name.")

        ElementByXPATH = driver.find_element(By.XPATH, "//div[@id='registration-cta']/mat-card/div[2]/div[2]/div[4]/div[2]" )

        if ElementByXPATH is not None:
            print("We found an element by XPATH.")

a = ByDemo()
a.test()
