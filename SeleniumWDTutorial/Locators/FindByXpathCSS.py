from selenium import webdriver

class FindElementByXpathCSS():

    def test(self):
        baseUrl="https://www.facebook.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        elementbyxpath = driver.find_element_by_xpath("//input[@id='email']")

        if elementbyxpath is not None:
            print("We found an element by XPATH.")

        elementbycss = driver.find_element_by_css_selector("#content > div > div > div > div > div._5iyz.rfloat._ohf > div > div.pvl._52lp._59d- > div.mbs._52lq.fsl.fwb.fcb > span")

        if elementbycss is not None:
            print("We found an element by CSS.")

a = FindElementByXpathCSS()
a.test()
