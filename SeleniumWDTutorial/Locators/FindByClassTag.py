from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

class FindByClassTag():

    def test(self):
        baseUrl="https://insight.proglove.com/"
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(baseUrl)
        ElementByClass = driver.find_element_by_class_name("body-rs")
        text = ElementByClass.text

        if ElementByClass is not None:
            print("We found an element by class name and the text is : "+ text)

        ElementByTag = driver.find_element_by_tag_name("div")

        if ElementByTag is not None:
            print("We found an element by tag name.")

a = FindByClassTag()
a.test()
