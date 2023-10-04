from element import BasePageElement
from locators import MainPageLocators
from locators import BasePageLocators
from selenium.webdriver.common.by import By
import time


class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    # The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    def __init__(self, driver):
        self.driver = driver

    def changeLang(self, lang='Русский'):
        # find user dropdown

        user_dropdown = self.driver.find_element(
            *BasePageLocators.USER_DROPDOWN)

        # check img tag for alt attribute
        current_lang = self.driver.find_element(
            *BasePageLocators.CURRENT_LANG_IMAGE).get_attribute('alt')

        if current_lang != lang:
            user_dropdown.click()
            lang_dropdown = self.driver.find_element(
                *BasePageLocators.LANG_DROPDOWN)
            lang_dropdown.click()
            lang_dropdown_options = lang_dropdown.find_elements(
                By.TAG_NAME, 'li')

            for lang_option in lang_dropdown_options:
                lang_option_value = lang_option.find_element(
                    By.TAG_NAME, 'img').get_attribute('alt')
                if lang_option_value == lang:
                    lang_option.click()
                    break

    def closeCookieNotification(self):
        """Closes Cookie notification"""
        notification = self.driver.find_element(
            *BasePageLocators.COOKIE_NOTIFICATION)

        if notification:
            notification.click()


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def openCarMarkOptions(self, get_options=False):
        """Opens Car Mark Options"""
        carsTab = self.driver.find_element(*MainPageLocators.CARS_TAB)
        carsTab.click()
        carsSelect = self.driver.find_element(*MainPageLocators.CARS_SELECT)
        carsSelect.click()
        time.sleep(5)

        all_car_options = carsSelect.find_elements(By.TAG_NAME, 'option')

        car_options = []

        if get_options:
            for option in all_car_options:
                val = option.get_attribute("value").strip()
                if val:
                    car = {
                        'name': option.text,
                        'code': val
                    }
                    car_options.append(car)

                    print(f"Car is: {car['name']}")

            return car_options

        return []

    def clickToOption(self, car_option):
        """clicks to option"""
        carsSelect = self.driver.find_element(*MainPageLocators.CARS_SELECT)
        all_car_options = carsSelect.find_elements(By.TAG_NAME, 'option')
        for option in all_car_options:
            val = option.get_attribute("value").strip()
            if val == car_option['code']:
                option.click()
                break
