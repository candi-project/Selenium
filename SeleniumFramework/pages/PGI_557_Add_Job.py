import time

import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.base.BasePage import BaseClass


class AddJob(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _understand_job = "Jobs"  # link
    _add_button = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > " \
                  "app-job-table > mat-card > div > div.title-button.ng-star-inserted > app-add-button > div"  # css
    _job_name = "#name-input > div > div.input-wrapper > input"  # css
    _start_pattern = "#start-pattern-input > div > div.input-wrapper > input"  # css
    _end_pattern = "#end-pattern-input > div > div.input-wrapper > input"  # css
    _station_checkbox = "#gateway-list-container > mat-selection-list > mat-list-option:nth-child(1) > div > " \
                        "mat-pseudo-checkbox"  # css
    _add_job_configuration = "#add-job > button"  # css
    _job_name_already_exists = "body > app-root > div > app-alert > div > mat-card > div"  # css

    def click_job_link(self):
        self.clickOnElement(self._understand_job, "link")
        time.sleep(5)

    def add_job(self):
        self.clickOnElement(self._add_button, "css")
        self.sendText("test", self._job_name, "css")
        self.sendText("123", self._start_pattern, "css")
        self.sendText("45", self._end_pattern, "css")
        self.clickOnElement(self._station_checkbox, "css")
        self.clickOnElement(self._add_job_configuration, "css")

    def check_error_message(self):
        self.isElementDisplayed(self._job_name_already_exists, "css")
