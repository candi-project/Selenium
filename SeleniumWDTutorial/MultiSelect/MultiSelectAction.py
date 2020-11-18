from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.ID, "multiselect")))
time.sleep(1)


# import the Select class

# Create the object for Select class
ms_options =Select(ele)
print("Check whether it is multi select or not: ", ms_options.is_multiple)

# List the values in Multiple Select.
ms_list_options = ms_options.options
for ms_value in ms_list_options:
    print(ms_value.text)
    time.sleep(1)

# Click by Index
ms_options.select_by_index(1)
time.sleep(1)

# Click by Value
ms_options.select_by_value("mOptionTWo")
time.sleep(1)

# Click by Text
ms_options.select_by_visible_text("mOption3")
time.sleep(1)

# Deselect by Index
ms_options.deselect_by_index(1)
time.sleep(1)

# Deselect by Value
ms_options.deselect_by_value("mOptionTWo")
time.sleep(1)

# Deselect by Text
ms_options.deselect_by_visible_text("mOption3")
time.sleep(1)

# Click by Index
ms_options.select_by_index(1)
time.sleep(1)

# Click by Value
ms_options.select_by_value("mOptionTWo")
time.sleep(1)

# Click by Text
ms_options.select_by_visible_text("mOption3")
time.sleep(1)

# Deselect All
ms_options.deselect_all()


time.sleep(5)
driver.quit()
