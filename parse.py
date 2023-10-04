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
        base_page.closeCookieNotification()

        main_page = page.MainPage(self.driver)
        car_options = main_page.openCarMarkOptions(True)

        while len(car_options):
            car_option = car_options.pop(0)
            main_page.openCarMarkOptions()
            main_page.clickToOption(car_option)

        # Tap To Models Tab and open options

        # Visit every options page and go back

        # Sleep for 10 seconds, for analyzing purposes
        time.sleep(10)

        pass

    def setUp(self):
        """initial setup"""
        self.driver.get("https://emexdwc.ae/")
        self.driver.maximize_window()
