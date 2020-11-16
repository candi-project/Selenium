from selenium import webdriver
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager
import time


class Wiesn():
    def test(self):
        baseUrl = "https://master-qa-experience.apps.moti.us/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)

        # OrderNumber = driver.find_element_by_css_selector('#ember510')
        # salutation = driver.find_element_by_id('ember439')
        # title = driver.find_element_by_id('ember442')
        # firstname = driver.find_element_by_id('ember540')
        # surname = driver.find_element_by_id('ember542')
        # day = driver.find_element_by_id('ember469')
        # month = driver.find_element_by_id('ember471')
        # year = driver.find_element_by_id('ember473')
        # placeofbirth = driver.find_element_by_id('ember848')
        # nationality = driver.find_element_by_id('ember478')
        # street = driver.find_element_by_id('ember1014')
        # house_no = driver.find_element_by_id('ember1016')
        # zip = driver.find_element_by_id('ember1018')
        # city = driver.find_element_by_id('ember1020')
        # country = driver.find_element_by_id('ember489')
        # email = driver.find_element_by_id('ember489')
        # mobile_no = driver.find_element_by_id('ember1536')
        # consent = driver.find_element_by_name('start-has-webcam')
        # continue_button = driver.find_element_by_css_selector('#contract-application-start > button')
        #
        # OrderNumber.send_keys('001')
        # salutation.click()
        # select_fr = Select(driver.find_element_by_id("ember526"))
        # title.click()
        # select_dr = Select(driver.find_element_by_id("ember533"))
        # firstname.send_keys('Hello')
        # surname.send_keys('World')
        # day.click()
        # select_day = Select(driver.find_element_by_id("ember556"))
        # month.click()
        # select_month = Select(driver.find_element_by_id("ember620"))
        # year.click()
        # select_year = Select(driver.find_element_by_id("ember645"))
        # placeofbirth.send_keys('UK')
        # nationality.click()
        # select_nationality = Select(driver.find_element_by_id("ember855"))
        # street.send_keys('Auenstrase ')
        # house_no.send_keys('100')
        # zip.send_keys('80469')
        # city.send_keys('Muenchen')
        # country.click()
        # select_country = Select(driver.find_element_by_id("ember1027"))
        # email.send_keys('idnow@gmail.com')
        # mobile_no.send_keys('012345678')
        # consent.click()
        # time.sleep(3)
        # continue_button.click()


a = Wiesn()
a.test()
