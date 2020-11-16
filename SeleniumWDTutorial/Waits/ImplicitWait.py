from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(2)

driver.implicitly_wait(10)

driver.find_element(By.CSS_SELECTOR, "input[class*=ter]").send_keys("Candi_Tag_ClassName_Substring")
time.sleep(2)
driver.quit()