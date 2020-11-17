from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

# 1. find the list of CheckBoxes using locator
ele_r = driver.find_elements(By.NAME, "checkbox")
time.sleep(3)

# 2. Using for loop iterate the list object and click on required option
for rbutton in ele_r:
    rbutton_t = rbutton.get_attribute("value")
    print(rbutton_t)

    if rbutton_t == "c2":
        rbutton.click()
        print("Is selected: ", rbutton.is_selected())
        break

time.sleep(2)
driver.quit()