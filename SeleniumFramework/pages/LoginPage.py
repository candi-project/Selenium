from SeleniumFramework.base.BasePage import BaseClass
import SeleniumFramework.utilities.CustomLogger as cl
import time


class SignInProGlove(BaseClass):

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values in Login page
    _signInToContinue = "#login-container > mat-card > div.interaction-container.ng-star-inserted"  # css
    _customerID = "#customer-id-field > div > div.input-wrapper > input"  # css
    _email = "#email-field > div > div.input-wrapper > input"  # css
    _password = "#password-field > div > div.input-wrapper.password-wrapper > input"  # css
    _loginBtn = "#login-btn > button"  # css
    _afterLogin = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > app-home > div"  # css
    _releaseNote = "Release Notes"  # link
    _releaseMainPage = "body > div.md-container > main > div > div.md-content"  # css
    _headerAndroidReleaseNote = "#insight-mobile-android-release-notes-v180"  # css
    _webPortalReleaseNote = "#cloud-card > div > span" # css

    def verifyPage(self):
        element = self.isElementDisplayed(self._signInToContinue, "css")
        assert element == True
        cl.allureLogs("Page is verified.")

    def enterCustomerID(self):
        self.sendText("dpucuicw", self._customerID, "css")
        #self.sendText("r17wdzko", self._customerID, "css")

        cl.allureLogs("Entered customer ID.")

    def enterEmail(self):
        self.sendText("candi.chiu@proglove.de", self._email, "css")
        cl.allureLogs("Entered email.")

    def enterPassword(self):
        self.sendText("0Apob6059!", self._password, "css")
        cl.allureLogs("Entered password.")

    def clickLoginBtn(self):
        self.clickOnElement(self._loginBtn, "css")
        cl.allureLogs("Clicked on Login button.")

    def afterLogin(self):
        element = self.isElementDisplayed(self._afterLogin, "css")
        assert element == True
        cl.allureLogs("Main page is verified.")

    def releaseNote(self):
        window_before = self.driver.window_handles[0]
        print(window_before)

        webReleaseNote = self.getWebElement(self._webPortalReleaseNote, "css")
        webHeader = webReleaseNote.text
        if webHeader == "ProGlove Insight Webportal (Dec 16, 2020)":
            print("Header is " + webHeader)
            cl.allureLogs("ProGlove Insight Webportal Release Note is verified.")
            assert True
        else:
            print("Header is " + webHeader)
            cl.allureLogs("Something wrong on ProGlove Insight Webportal Release Note.")
            assert False

        time.sleep(3)

        self.clickOnElement(self._releaseNote, "link")
        time.sleep(2)

        window_after = self.driver.window_handles[1]
        print(window_after)

        self.driver.switch_to.window(window_after)
        element_android = self.isElementDisplayed(self._releaseMainPage, "css")
        assert element_android == True

        ele = self.getWebElement(self._headerAndroidReleaseNote, "css")
        header = ele.text
        if header == "Insight Mobile (Android) release notes v1.9.0":
            print("Header is " + header)
            cl.allureLogs("Release Note is verified.")
            assert True
        else:
            print("Header is " + header)
            cl.allureLogs("Release Note is incorrect.")
            assert False

        self.driver.switch_to.window(window_before)
        # print(window_before)
