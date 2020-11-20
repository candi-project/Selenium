from selenium import webdriver
import time

from selenium.webdriver.common.by import By

#driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver = webdriver.Firefox(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/geckodriver")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(5)
#assert "Selenium Template — DummyPoint" in driver.title

# driver.maximize_window()
# time.sleep(2)
driver.minimize_window()
time.sleep(5)
driver.maximize_window()
time.sleep(5)

driver.quit()

