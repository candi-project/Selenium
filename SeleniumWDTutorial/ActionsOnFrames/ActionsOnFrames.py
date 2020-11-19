from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/Frame.html")
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = driver.find_elements(By.TAG_NAME, "iframe")
time.sleep(2)

# To display number of Iframes in web page
print("List of iframe: ", len(ele))

# Switch to iframe by index
# driver.switch_to.frame(0)
# data = driver.find_element(By.ID, "framename")
# print("Frame name is: ", data.text)

# Switch to iframe by name
# driver.switch_to.frame("farme3")
# data = driver.find_element(By.ID, "framename")
# print("Frame name is: ", data.text)

# Switch to iframe by id
# driver.switch_to.frame("f4")
# data = driver.find_element(By.ID, "framename")
# print("Frame name is: ", data.text)

# Switch to iframe by WebElement
ele2 = driver.find_element(By.ID, "f2")
driver.switch_to.frame(ele2)
data = driver.find_element(By.ID, "framename")
print("Frame name is: ", data.text)

# Switching back to normal content page from frame
driver.switch_to.default_content()
data = driver.find_element(By.ID, "framename")
print("Frame name is: ", data.text)


time.sleep(3)
driver.quit()
