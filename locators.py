from selenium.webdriver.common.by import By


class BasePageLocators(object):
    """A class for all pages"""

    USER_DROPDOWN = (By.ID, 'userDropdown')
    CURRENT_LANG_IMAGE = (By.ID, 'ucHeader_ucLangFlagSelector_imgCurLangFlag')
    LANG_DROPDOWN = (By.XPATH, '//*[@id="userDropdown"]/ul/li[5]/div')
    COOKIE_NOTIFICATION = (By.CSS_SELECTOR, '#divCookiePolicy button')
    SEARCH_BUTTON = (By.CSS_SELECTOR, '.tabs .active .input-group-btn')


class MainPageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    CARS_TAB = (By.XPATH, '//*[@id="mainForm"]/div[7]/div/ul/li[2]/a')
    CARS_SELECT = (By.XPATH, '//*[@id="tab4"]/div/select')


class MarkPageLocators(object):
    """A class for mark page locators. All mark page locators should come here"""
    MODELS_SELECT = (
        By.CSS_SELECTOR, '.panel select:first-of-type')
    MODEL_SPAN = (
        By.CSS_SELECTOR, '.panel span:first-of-type')

    SUBMIT_BUTTON = (By.CSS_SELECTOR, '.panel-footer input')
    SELECTS = (By.CSS_SELECTOR, '.panel .form-group')
    FORM_GROUP_SELECTS = (By.CSS_SELECTOR, '.panel select')


class VehiclePageLocators(object):
    NOT_FIRST_ROW = (By.CSS_SELECTOR, '.guayaquil_table tr:not(:first-child)')
    CATEGORY_NODES = (By.CSS_SELECTOR, '#qgTree > ul > li')
    CATEGORY_LEAFS = (By.CSS_SELECTOR, '.qgExpandLeaf')
    CATEGORY_PARENT = (
        By.XPATH, ".//ancestor::li[@class='qgNode qgExpandOpen']")


class DetailPageLocators(object):
    FIRST_ROW = (
        By.CSS_SELECTOR, '.guayaquil_table .g_collapsed')
    
    # GROUP_NAME = (By.CSS_SELECTOR, '.gdCategory h3:first-child')
    # SUBGROUP_NAME = (By.CSS_SELECTOR, '.gdImageCol a')

    GROUP_CONTAINER = (By.CSS_SELECTOR, '.gdCategory')
    GROUP_NAME = (By.CSS_SELECTOR, 'h3')
    UNIT_CONTAINER = (By.CSS_SELECTOR, '.gdUnit')
    UNIT_NAME = (By.CSS_SELECTOR, '.gdImageCol a')
    UNIT_DETAILS = (By.CSS_SELECTOR, '.g_collapsed')
    
    DETAIL_NAME = (By.CSS_SELECTOR, 'td[name="c_name"]')
    DETAIL_OEM = (By.CSS_SELECTOR, 'td[name="c_oem"]')
    DETAIL_PNC = (By.CSS_SELECTOR, 'td[name="c_pnc"]')
    DETAIL_NOTE = (By.CSS_SELECTOR, 'td[name="c_note"]')