import os
import time

import SeleniumFramework.utilities.CustomLogger as cl
from SeleniumFramework.base.BasePage import BaseClass


class BarcodeConfigurations(BaseClass):
    log = cl.customLogger()

    def __init__(self, driver):
        super().__init__(driver)
        driver = self.driver

    # Locators  values
    _ConfigurationLink = "Configurations"  # link
    _CreateNewConfigurationBtn = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > " \
                                 "span > app-configuration-list > div > div.actions-container > a > app-button > " \
                                 "button"  # css
    #_InsightMobileBtn = "#mat-radio-3 > label"  # css
    _InsightMobileBtn = "//mat-radio-button[@class='mat-radio-button mat-accent']" #xpath
    _Android_NextBtn = "#new-file-card > mat-card-content > app-button:nth-child(3) > button"  # css
    _Config_NextBtn = "#done-btn > button"  # css
    _ConfigurationName = "#name-input > div > div.input-wrapper > input"  # css
    _ConfigurationName_NextBtn = "#mat-dialog-0 > div > div.modal-btn-container > app-button:nth-child(2) > button"  # css
    #_ConfigurationName_NextBtn = "/html/body/div[1]/div[2]/div/mat-dialog-container/div/div[3]/app-button[2]/button/div[1]" #xpath
    _barcode = "#qr-code-container > canvas"  # css
    _barcode_SaveBtn = "#button-container > app-button:nth-child(2) > button"  # css
    _barcode_BackBtn = "#button-container > app-button:nth-child(1) > button"  # css
    _successfully_saved_configuration = "body > app-root > div > app-alert > div > mat-card > div"  # css
    _configfile_saved = "body > app-root > div > app-side-nav > mat-drawer-container > mat-drawer-content > span > " \
                        "app-configuration-list > div > mat-card > mat-card-content > table > tbody > tr:nth-child(1) " \
                        "> td.mat-cell.cdk-column-name.mat-column-name.ng-star-inserted"  # css
    _edit = "/html/body/app-root/div/app-side-nav/mat-drawer-container/mat-drawer-content/span/app-configuration-list" \
            "/div/mat-card/mat-card-content/table/tbody/tr[10]/td[4]/a[2]/img "
    # xpath
    _add_Workflow_Rules = "/html/body/app-root/div/app-side-nav/mat-drawer-container/mat-drawer-content/span/app" \
                          "-configuration-detail/div/div[" \
                          "3]/mat-tab-group/div/mat-tab-body/div/app-configuration-profile/div/mat-vertical-stepper" \
                          "/div[7]/mat-step-header"  # xpath
    _add_Rule = "/html/body/app-root/div/app-side-nav/mat-drawer-container/mat-drawer-content/span/app-configuration" \
                "-detail/div/div[3]/mat-tab-group/div/mat-tab-body/div/app-configuration-profile/div/mat-vertical" \
                "-stepper/div[7]/div/div/div/app-rule-list/mat-card/mat-card-content/div[2]/button"  # xpath
    _rule_Name = "#rules-details > div:nth-child(1) > app-text-input > div > div.input-wrapper > input"  # css
    _rule_Name_2 = "#rules-details > div:nth-child(1) > app-text-input > div > div.input-wrapper"  # css
    _add_Conditions = "#condition-container > mat-card > button"  # css
    _add_Actions = "#action-container > mat-card > button"  # css
    _barcode_equals = "#condition-section > div.condition-parameter-container > mat-card > app-text-input > div > " \
                      "div.input-wrapper > input"  # css
    _barcode_contains = "#condition-section > div.click-card-container > " \
                        "mat-card.clickable-card.condition-card.mat-card.ng-star-inserted.active"  # css
    _barcode_matches = "#condition-section > div.click-card-container > " \
                       "mat-card.clickable-card.condition-card.mat-card.ng-star-inserted.active"  # css
    _save_Conditions = "#condition-section > app-button > button"  # css
    _make_A_Beep = "#action-section > div.click-card-container > mat-card:nth-child(1)"  # css
    _add_prefix = "#action-section > div.click-card-container > " \
                  "mat-card.clickable-card.action-card.mat-card.active.ng-star-inserted"  # css
    _save_Actions = "#action-section > app-button > button"  # css
    _save_Rule = "#save-container > app-button:nth-child(1) > button"  # css

    _workflow_rule_filename_folded = "#rule-list > mat-list-item:nth-child(2) > div > div.list-item-container > span"  # css
    _workflow_rule_filename_folded_2 = "#rule-list"  # css
    _actions_card = "#action-container > mat-card > mat-nav-list > mat-list-item > div"  # css

    _apply_the_configuration = "#dialog-container"  # css
    _save_apply_the_configuration = "#button-container > app-button:nth-child(2) > button" #css

    def clickOnConfiguration(self):
        self.clickOnElement(self._ConfigurationLink, "link")

    def scrollToCreate(self):
        time.sleep(20)
        self.scrollTo(self._CreateNewConfigurationBtn, "css")
        self.clickOnElement(self._CreateNewConfigurationBtn, "css")

    def choose_Connectivity_Option(self):
        time.sleep(5)
        self.clickOnElement(self._InsightMobileBtn, "xpath")

    def clickOnNext_Android(self):
        self.clickOnElement(self._Android_NextBtn, "css")

    def clickOnNext_ConfigTool(self):
        self.clickOnElement(self._Config_NextBtn, "css")

    def assign_A_Name(self):
        self.sendText("PGI-687 sanity2", self._ConfigurationName, "css")

    def assign_A_Name_error(self):
        self.sendText("PGI-687 Error", self._ConfigurationName, "css")

    def clickOnNext_afterAName(self):
        time.sleep(2)
        self.clickOnElement(self._ConfigurationName_NextBtn, "css")

    def barcode_configuration(self):
        time.sleep(2)
        self.isElementDisplayed(self._barcode, "css")

    def barcode_configuration_error(self):
        time.sleep(2)
        self.isElementDisplayed(self._apply_the_configuration, "css")
        self.log.info("Error screen-apply_the_configuration is shown.")
        self.clickOnElement(self._save_apply_the_configuration, "css")

    def clickOnBarcodeSaveBtn(self):
        self.clickOnElement(self._barcode_SaveBtn, "css")

    def successful_saved_notification(self):
        time.sleep(2)
        self.isElementDisplayed(self._successfully_saved_configuration, "css")

    def verify_configfile_saved(self):
        time.sleep(20)
        filename = self.getText(self._configfile_saved, "css")
        if filename == "PGI-687 sanity2":
            cl.allureLogs("Config file name is" + filename)
        else:
            cl.allureLogs("Config file name is" + filename)
            assert False

    def clickOnEdit(self):
        time.sleep(10)
        self.clickOnElement(self._edit, "xpath")

    def add_Workflow_Rules(self):
        time.sleep(3)
        self.scrollTo(self._Config_NextBtn, "css")
        self.clickOnElement(self._add_Workflow_Rules, "xpath")
        self.scrollTo(self._Config_NextBtn, "css")
        self.clickOnElement(self._add_Rule, "xpath")
        time.sleep(2)
        self.sendText("Sanity", self._rule_Name, "css")
        self.clickOnElement(self._add_Conditions, "css")
        self.sendText("Hello", self._barcode_equals, "css")
        self.clickOnElement(self._save_Conditions, "css")
        time.sleep(2)
        self.clickOnElement(self._add_Actions, "css")
        self.clickOnElement(self._make_A_Beep, "css")
        self.clickOnElement(self._save_Actions, "css")
        self.clickOnElement(self._save_Rule, "css")

    def add_Workflow_Rules_Large_File(self):
        time.sleep(3)
        self.scrollTo(self._Config_NextBtn, "css")
        self.clickOnElement(self._add_Workflow_Rules, "xpath")
        self.scrollTo(self._Config_NextBtn, "css")
        self.clickOnElement(self._add_Rule, "xpath")
        time.sleep(2)
        self.sendText("10 Random Rules", self._rule_Name, "css")

        for x in range(0, 10):
            self.clickOnElement(self._add_Conditions, "css")
            self.sendText(
                "asdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf"
                ";ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf"
                ";ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf"
                ";ldasdfagjrklgjfdklgldkf;ldasdfagjrklgjfdklgldkf;ld",
                self._barcode_equals, "css")
            self.clickOnElement(self._save_Conditions, "css")
            time.sleep(2)

        time.sleep(3)
        self.clickOnElement(self._add_Actions, "css")
        self.clickOnElement(self._make_A_Beep, "css")
        self.clickOnElement(self._save_Actions, "css")
        self.clickOnElement(self._save_Rule, "css")

    def verify_Workflow_Rules_Saved(self):
        time.sleep(5)
        filename = self.getText(self._workflow_rule_filename_folded, "css")
        if filename == "Sanity":
            cl.allureLogs("Workflow_Rules file name is " + filename)
            self.log.info("Workflow_Rules file name is " + filename)
        else:
            cl.allureLogs("Workflow_Rules file name is " + filename)
            self.log.info("Workflow_Rules file name is " + filename)
            assert False

    def click_On_Barcode_Back(self):
        self.clickOnElement(self._barcode_BackBtn, "css")

    def verify_Workflow_Rules_Content(self):
        self.clickOnElement(self._workflow_rule_filename_folded_2, "css")
        self.scrollTo(self._actions_card, "css")
        action = self.getText(self._actions_card, "css")
        self.log.info("Action name is " + action)
        if "Beep" not in action:
            assert False
        else:
            self.clickOnElement(self._save_Rule, "css")
