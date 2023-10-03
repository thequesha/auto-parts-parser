from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """A class for all pages"""

    USER_DROPDOWN = (By.ID, 'userDropdown')
    CURRENT_LANG_IMAGE = (By.ID, 'ucHeader_ucLangFlagSelector_imgCurLangFlag')
    LANG_DROPDOWN = (By.XPATH, '//*[@id="userDropdown"]/ul/li[5]/div')


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    pass


class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""

    pass
