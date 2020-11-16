"""
Below are some of the ways to find WebElement using CssSelector

1. To write id name in css selector you need to add "#" before id value

2. To write class name in css selector you need to add "." before class name

3. Using " Tag name("input") and name " Attribute value as css_selector

4. Using " Tag name("input"),className and name " Attribute value as css_selector

5. “^” - Find elements using starts with a string value

6. “$” - Find elements using Ends with a string value

7. “*” - Find elements using contains a substring.

"""
from selenium import webdriver
import time

from selenium.webdriver.common.by import By

driver = webdriver.Chrome(executable_path="/home/candi/Desktop/Selenium/Selenium/driver/chromedriver84")
driver.get("http://dummypoint.com/seleniumtemplate.html")
time.sleep(3)

# 1. Using ID name in CSS Selector (To write id name in css selector you need to add "#" before id value)
#driver.find_element(By.CSS_SELECTOR, "#user_input").send_keys("Candi_id")

# 2. Using Class Name in CSS Selector (To write class name in css selector you need to add "." before class name)
#driver.find_element(By.CSS_SELECTOR, ".entertext").send_keys("Candi_ClassName")

# 3. Using " Tag name("input") and name " Attribute value as css_selector
#driver.find_element(By.CSS_SELECTOR, "input[name=textbox]").send_keys("Candi_TagName")

# 4. Using " Tag name("input"),className and name " Attribute value as css_selector
#driver.find_element(By.CSS_SELECTOR, "input.entertext[name=textbox]").send_keys("Candi_Tag_ClassName_name")

# 5. “^” - Find elements using starts with a string value
#driver.find_element(By.CSS_SELECTOR, "input[class^=en]").send_keys("Candi_Tag_ClassName_StartWith")

# 6. “$” - Find elements using Ends with a string value
#driver.find_element(By.CSS_SELECTOR, "input[class$=xt]").send_keys("Candi_Tag_ClassName_EndsWith")

# 7. “*” - Find elements using contains a substring.
driver.find_element(By.CSS_SELECTOR, "input[class*=ter]").send_keys("Candi_Tag_ClassName_Substring")

time.sleep(3)
driver.quit()