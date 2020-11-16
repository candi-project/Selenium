from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")

driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(2)

driver.get("http://dummypoint.com/Form.html")
time.sleep(2)

driver.back()
time.sleep(3)

driver.forward()
time.sleep(3)

driver.refresh()
time.sleep(5)

driver.quit()


