
from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/Windows.html")
assert "Selenium Template" in driver.title
time.sleep(3)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.NAME, "promtalertb"))).click()
time.sleep(2)

# Import Alert class

# Create the object for Alert class
a_button = Alert(driver)

# Using Alert class object call the methods to " 1. accept or 2. dismiss or 3. send text and get text " in Alert box
text_a = a_button.text
print(text_a)

a_button.send_keys("Candi is the best.")
time.sleep(1)
#a_button.accept()
a_button.dismiss()


time.sleep(3)
driver.quit()