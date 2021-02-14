from traceback import print_stack

from allure_commons.types import AttachmentType
from selenium.common.exceptions import ElementNotVisibleException, NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
import SeleniumFramework.utilities.CustomLogger as cl
import allure


class BaseClass:
    log = cl.customLogger()

    def __init__(self, driver):
        self.driver = driver

    def launchWebPage(self, url, title):
        try:
            self.driver.get(url)
            assert title in self.driver.title
            self.log.info("Web page launched with url: " + url)
        except:
            self.log.info("Web page not launched with url: " + url)

    def getLocatorType(self, locatorType):
        locatorType = locatorType.lower()

        if locatorType == "id":
            return By.ID
        elif locatorType == "name":
            return By.NAME
        elif locatorType == "class":
            return By.CLASS_NAME
        elif locatorType == "xpath":
            return By.XPATH
        elif locatorType == "css":
            return By.CSS_SELECTOR
        elif locatorType == "tag":
            return By.TAG_NAME
        elif locatorType == "link":
            return By.LINK_TEXT
        elif locatorType == "plink":
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.error("Locator Type: " + locatorType + "entered is not found.")
            return False

    def getWebElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            webElement = self.driver.find_element(locatorByType, locatorValue)
            self.log.info(
                "Web element found with locator value: " + locatorValue + " using locator Type: " + locatorType)
        except:
            self.log.error(
                "Web element not found with locator value: " + locatorValue + " using locator Type: " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def waitForElement(self, locatorValue, locatorType="id"):
        webElement = None
        try:
            locatorType = locatorType.lower()
            locatorByType = self.getLocatorType(locatorType)
            wait = WebDriverWait(self.driver, 25, poll_frequency=1,
                                 ignored_exceptions=[ElementNotVisibleException, NoSuchElementException])
            webElement = wait.until(ec.presence_of_element_located((locatorByType, locatorValue)))
            self.log.info(
                "Web element found with locator value: " + locatorValue + " using locator Type: " + locatorType)
        except:
            self.log.error(
                "Web element not found with locator value: " + locatorValue + " using locator Type: " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return webElement

    def clickOnElement(self, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.click()
            self.log.info(
                "Clicked on WebElement with locator value " + locatorValue + " using locator Type: " + locatorType)
        except:
            self.log.error(
                "Unable to click on WebElement with locator value " + locatorValue + " using locator Type: " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def sendText(self, text, locatorValue, locatorType="id"):
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            webElement.send_keys(text)
            self.log.info(
                "Sent the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to send the text " + text + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def getText(self, locatorValue, locatorType="id"):
        ElementText = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            ElementText = webElement.text
            self.log.info(
                "Got the text " + ElementText + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to get the text " + ElementText + " in WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return ElementText

    def isElementDisplayed(self, locatorValue, locatorType="id"):
        ElementDisplayed = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            ElementDisplayed = webElement.is_displayed()
            self.log.info(
                "WebElement is Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement is not Displayed on web page with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return ElementDisplayed

    def isElementEnabled(self, locatorValue, locatorType="id"):
        ElementEnabled = None
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            ElementEnabled = webElement.is_enabled()
            self.log.info(
                "WebElement is Enabled on web page with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "WebElement is not Enabled on web page with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False
        return ElementEnabled

    def scrollTo(self, locatorValue, locatorType="id"):
        actions = ActionChains(self.driver)
        try:
            locatorType = locatorType.lower()
            webElement = self.waitForElement(locatorValue, locatorType)
            actions.move_to_element(webElement).perform()
            self.log.info(
                "Scrolled to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
        except:
            self.log.error(
                "Unable to scroll to WebElement with locator value " + locatorValue + " using locatorType " + locatorType)
            print_stack()
            self.takeScreenshot(locatorType)
            assert False

    def takeScreenshot(self, text):
        allure.attach(self.driver.get_screenshot_as_png(), name=text, attachment_type=AttachmentType.PNG)
