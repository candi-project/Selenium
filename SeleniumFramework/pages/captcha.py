from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
options.add_argument('disable-infobars')
driver = webdriver.Chrome(executable_path=r'/home/candi/Desktop/Selenium/Selenium/driver/chromedriver87',
                          chrome_options=options)
driver.get("https://my.symphony.com/#forgot-password")
WebDriverWait(driver, 10).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#recover-form > div.recover-form__captcha-container > div > div > div > iframe")))
WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@id='recaptcha-anchor']/div[1]"))).click()
