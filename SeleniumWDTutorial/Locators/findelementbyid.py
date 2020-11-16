from selenium import webdriver

class FindElementBy():

    def test(self):
        baseUrl="https://www.facebook.com/"
        driver = webdriver.Firefox()
        driver.get(baseUrl)
        elementbyid = driver.find_element_by_id("u_0_m")

        if elementbyid is not None:
            print("We found an element by id.")

        elementbyname = driver.find_element_by_name("birthday_year")

        if elementbyname is not None:
            print("We found an element by name.")

a = FindElementBy()
a.test()
