from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/Windows.html")
time.sleep(2)
assert "Selenium Template — DummyPoint" in driver.title

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])

# To get the current window name
window_name = driver.current_window_handle
print("Before switching: ", window_name)
time.sleep(2)

# click on popup button to open new window
ele_list = driver.find_elements(By.TAG_NAME, "input")
time.sleep(2)

for popup_bs in ele_list:
    popup_b = popup_bs.get_attribute("value")
    if popup_b == "Open a Popup Window2":
        popup_bs.click()

# Print the list of windows are present on the screen in present session.
time.sleep(3)
window_names = driver.window_handles
time.sleep(1)

for window in window_names:
    print("Current windows: ", window)

# switch to required window
driver.switch_to.window(window_names[1])
time.sleep(2)
window_name = driver.current_window_handle
print("After switching: ", window_name)
time.sleep(2)
driver.maximize_window()

""" 
Here switching to new window and performing action on frame
"""
time.sleep(2)
driver.switch_to.frame("farme3")
data = driver.find_element(By.ID, "framename")
print("Frame name is: ", data.text)
time.sleep(2)
driver.close()


time.sleep(3)
driver.quit()