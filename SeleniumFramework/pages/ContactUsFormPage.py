from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl


class ContactUsForm(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values in Contact Us Form page
    _FormLink = "Form"  # link
    _FormColumn = "reused_form"  # id
    _EnterName = "name"  # id
    _EnterEmail = "email"  # id
    _GenderFemale = "input.form-radio[value=female]"  # css
    _EnterMessage = "message"  # id
    _Captcha = "captcha_image"  # id
    _PassCaptha = "captcha" # id
    _PostButton = "btnContactUs" # id

    def clickOnForm(self):
        self.clickOnElement(self._FormLink, "link")
        cl.allureLogs("Clicked on Form.")

    def verifyFormPage(self):
        element= self.isElementDisplayed(self._FormColumn, "id")
        assert element == True
        cl.allureLogs("Page is verified.")

    def enterName(self):
        self.sendText("Candi rocks!", self._EnterName, "id")
        cl.allureLogs("Entered name.")

    def enterEmail(self):
        self.sendText("cchiu615@gmail.com", self._EnterEmail, "id")
        cl.allureLogs("Entered email.")

    def selectGenderFemale(self):
        self.clickOnElement(self._GenderFemale, "css")
        cl.allureLogs("Selected gender-female.")

    def enterMessage(self):
        self.sendText("High Vibe", self._EnterMessage, "id")
        cl.allureLogs("Entered message.")

    def getCaptcha(self):
        cap = self.getText(self._Captcha, "id")
        return cap
        cl.allureLogs("Got captcha.")

    def passCaptcha(self):
        self.sendText(self.getCaptcha(), self._PassCaptha, "id")
        cl.allureLogs("Passed captcha to form.")

    def clickOnPostButton(self):
        self.scrollTo(self._PostButton, "id")
        self.clickOnElement(self._PostButton, "id")
        cl.allureLogs("Clicked on post it button.")