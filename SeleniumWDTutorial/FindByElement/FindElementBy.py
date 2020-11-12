from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome("/Users/candichiu/Documents/workspace_python/driver/chromedriver86")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

#driver.find_element(By.ID,"user_input").send_keys("Candi Chiu")
#driver.find_element(By.CLASS_NAME,"entertext").send_keys("Candi Chiu_ClassName")
driver.find_element(By.NAME,"textbox").send_keys("Candi Chiu_Name")

time.sleep(5)
driver.quit()