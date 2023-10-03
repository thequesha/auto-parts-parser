from selenium import webdriver
import page
import time


class PartsParser:
    """Parser Project for AutoParts"""

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        """Parses Auto Parts"""

        # setup initial configuration
        self.setUp()

        # define base page, so we could use base websites methods
        base_page = page.BasePage(self.driver)

        # change language ro Russian
        base_page.changeLang('Русский')

        # Change language to Russian

        # Tap To Models Tab and open options

        # Visit every options page and go back

        # Sleep for 10 seconds, for analyzing purposes
        time.sleep(10)

        pass

    def setUp(self):
        """initial setup"""
        self.driver.get("https://emexdwc.ae/")
        self.driver.maximize_window
