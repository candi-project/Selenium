from selenium import webdriver
import time

from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
assert "Selenium Template — DummyPoint" in driver.title
time.sleep(2)

wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
wait.until(ec.presence_of_element_located((By.LINK_TEXT, "Form"))).click()
wait.until(ec.presence_of_element_located((By.ID, "reused_form")))
time.sleep(2)

wait.until(ec.presence_of_element_located((By.ID, "name"))).send_keys("Candi")
wait.until(ec.presence_of_element_located((By.ID, "email"))).send_keys("cchiu615@gmail.com")
wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, "input.form-radio[value=female]"))).click()
wait.until(ec.presence_of_element_located((By.ID, "message"))).send_keys("Keeping up the good work.")
captcha = wait.until(ec.presence_of_element_located((By.ID, "captcha_image")))

wait.until(ec.presence_of_element_located((By.ID, "captcha"))).send_keys(captcha.text)

postBtn = wait.until(ec.presence_of_element_located((By.ID, "btnContactUs")))

action = ActionChains(driver)
action.move_to_element(postBtn).perform()
postBtn.click()

time.sleep(2)
driver.quit()
