from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

ele = driver.find_elements(By.CLASS_NAME, "section-header-breadcrumb")

for menu in ele:
    print(menu.text)

time.sleep(2)
driver.quit()