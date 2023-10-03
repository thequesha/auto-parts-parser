from element import BasePageElement
from locators import MainPageLocators
from locators import BasePageLocators
from selenium.webdriver.common.by import By


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

        # if alt attr is == lang then do nothing

        # else
        if (current_lang != lang):
            user_dropdown.click()
            lang_dropdown = self.driver.find_element(
                *BasePageLocators.LANG_DROPDOWN)
            lang_dropdown.click()
            lang_dropdown_options = lang_dropdown.find_elements(
                By.TAG_NAME, 'li')
            print(lang_dropdown_options)

            for lang_option in lang_dropdown_options:
                print(lang_option)

        # click to dropdown

        # find element with img(attr == lang) and click to it


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    # Declares a variable that will contain the retrieved text
    search_text_element = SearchTextElement()

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""

        return "Python" in self.driver.title

    def click_go_button(self):
        """Triggers the search"""

        # element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        # element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source
