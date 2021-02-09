import os
import time
from pathlib import Path
from traceback import print_stack

import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.base.BasePage import BaseClass


class OpenSourceLicense(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _open_source_license = "Open Source Licenses"  # link
    _download_link_mark = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > " \
                          "app-open-source-licenses > div > mat-card > mat-card-content > div:nth-child(1) > div > a"
    # css
    _download_link_gateway = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span " \
                             "> app-open-source-licenses > div > mat-card > mat-card-content > div:nth-child(2) > div" \
                             " > a"  # css

    def click_open_source_license(self):
        time.sleep(5)
        self.clickOnElement(self._open_source_license, "link")
        time.sleep(2)

    def click_download_mark(self):
        self.clickOnElement(self._download_link_mark, "css")

    def click_download_gateway(self):
        self.clickOnElement(self._download_link_gateway, "css")

    def is_download_finished(self, temp_folder):
        chrome_temp_file = sorted(Path(temp_folder).glob('mark_legal_notice*'))
        downloaded_files = sorted(Path(temp_folder).glob('mark_legal_notice*'))
        if (len(chrome_temp_file) == 1) and (len(downloaded_files) >= 1):
            self.log.info("File is downloaded.")
            print(len(chrome_temp_file))
            print(len(downloaded_files))
            assert True

        else:
            self.log.info("File is not downloaded.")
            print(len(chrome_temp_file))
            print(len(downloaded_files))
            print_stack()
            assert False

    def remove_download(self, path):
        time.sleep(3)

        if os.path.exists(path):
            os.remove(path)
            print("The file is removed.")
        else:
            print("The file does not exist")