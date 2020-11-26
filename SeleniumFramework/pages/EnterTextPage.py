from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time

class EnterText(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _enterText = "user_input" #id
    _submitButton = "submitbutton" #id
    _section = "section-body" #class

    def verifySection(self):
        element = self.isElementDisplayed(self._section, "class")
        assert element == True
        cl.allureLogs("Page is verified.")

    def enterText(self):
        time.sleep(3)
        self.sendText("Candi is cute.", self._enterText, "id")
        cl.allureLogs("Text entered.")

    def clickOnSubmitButton(self):
        self.clickOnElement(self._submitButton, "id")
        cl.allureLogs("Clicked on submit button.")