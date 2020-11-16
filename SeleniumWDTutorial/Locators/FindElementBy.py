from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

#driver.find_element(By.ID,"user_input").send_keys("Candi Chiu")
#driver.find_element(By.CLASS_NAME,"entertext").send_keys("Candi Chiu_ClassName")
#driver.find_element(By.NAME,"textbox").send_keys("Candi Chiu_Name")
#driver.find_element(By.TAG_NAME,"input").send_keys("Candi Chiu_TagName")
#driver.find_element(By.LINK_TEXT,"Form").click()
driver.find_element(By.PARTIAL_LINK_TEXT,"For").click()

time.sleep(5)
driver.quit()