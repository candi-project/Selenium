from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/Actions.html")
time.sleep(2)
assert "Selenium Template — DummyPoint" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
ele = wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Windows")))
time.sleep(2)

# Import the ActionChains Class

# 1. Create the object for ActionChains class
actions = ActionChains(driver)

# 2. Double click Operation
actions.double_click(ele).perform()
time.sleep(5)

# 3. Right click Operation
#actions.context_click().perform()

ele1 = wait.until(ec.presence_of_element_located((By.XPATH, "//*[@id='app']/div/div[3]/section/div[1]/div/div[3]/a")))
actions.context_click(ele1).perform()


time.sleep(3)
driver.quit()