from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

class ChromeDriverMac():

    def test(self):
        driver = webdriver.Chrome("/Users/candichiu/Documents/workspace_python/driver/chromedriver86")
        #driver = webdriver.Chrome(ChromeDriverManager().install())
        #driver = webdriver.Chrome()
        driver.get("https://master-qa-experience.apps.moti.us/")


cc = ChromeDriverMac()
cc.test()
time.sleep(5)




