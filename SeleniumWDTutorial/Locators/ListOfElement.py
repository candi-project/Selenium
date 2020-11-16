from selenium import webdriver
from selenium.webdriver.common.by import By

class ListOfElement():

    def test(self):
        baseUrl = "https://insight.proglove.com/"
        driver = webdriver.Chrome()
        driver.get(baseUrl)
        ElementsByClass = driver.find_elements_by_class_name("message-row")
        length1 = len(ElementsByClass)

        if ElementsByClass is not None:
            print("Class name> Size of the list: "+str(length1))

        ElementsByTag = driver.find_elements(By.TAG_NAME, "span")
        length2 = len(ElementsByTag)

        if ElementsByTag is not None:
            print("Tag name> Size of the list: "+str(length2))

a = ListOfElement()
a.test()
