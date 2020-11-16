from selenium import webdriver

class FindByLinkText():

    def test(self):
        baseUrl="https://insight.proglove.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        ElementByLinkText = driver.find_element_by_link_text("Privacy Policy")

        if ElementByLinkText is not None:
            print("We found an element by Link Text.")

        ElementByPartialLinkText = driver.find_element_by_partial_link_text("Impri")

        if ElementByPartialLinkText is not None:
            print("We found an element by partial link text.")

a = FindByLinkText()
a.test()
