from element import BasePageElement
from locators import *
from helper import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from termcolor import colored
from selenium.webdriver.common.keys import Keys


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
        warning(f'Trying to change language to: {lang}')

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
                    success('Successfully switched language to: ' + lang)
                    break
        else:
            success(f'Already in {lang} language')

    def closeCookieNotification(self):
        """Closes Cookie notification"""
        notification = self.driver.find_element(
            *BasePageLocators.COOKIE_NOTIFICATION)

        if notification:
            notification.click()
            success('Closed Cookie notification')
        else:
            warning('Could\'t find notification')


class MainPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def openCarMarkOptions(self, get_options=False):
        """Opens Car Mark Options"""
        wait = WebDriverWait(self.driver, 100)

        carsTab = self.driver.find_element(*MainPageLocators.CARS_TAB)
        carsTab.click()
        carsSelect = self.driver.find_element(*MainPageLocators.CARS_SELECT)
        if not get_options:
            carsSelect.click()

        wait.until(EC.presence_of_element_located(
            (By.CSS_SELECTOR, '#tab4 select :not(:first-child)')))

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

            return car_options

        return []

    def clickToOption(self, car_option):
        """clicks to option"""
        carsSelect = self.driver.find_element(*MainPageLocators.CARS_SELECT)
        all_car_options = carsSelect.find_elements(By.TAG_NAME, 'option')
        # for option in all_car_options:
        #     val = option.get_attribute("value").strip()
        #     if val == car_option['code']:
        #         option.click()
        #         break

        for option in all_car_options:
            # val = option.get_attribute("value").strip()
            text = option.text
            if text == car_option:
                option.click()
                break


class MarkPage(BasePage):
    """Mark Page objeck. Interacting with mark page"""

    def getModelOptions(self):
        """Obtain first select's options save it to nested list"""
        wait = WebDriverWait(self.driver, 100)

        models_select = Select(wait.until(EC.presence_of_element_located(
            (MarkPageLocators.MODELS_SELECT))))

        all_model_options = models_select.options

        return optionsToArray(all_model_options)

    def selectMark(self, text):
        """select option by text"""
        wait = WebDriverWait(self.driver, 100)

        models_select = Select(wait.until(EC.presence_of_element_located(
            (MarkPageLocators.MODELS_SELECT))))

        models_select.select_by_visible_text(text)

    def waitForModelSelection(self, text=''):
        wait = WebDriverWait(self.driver, 100)
        element = wait.until(EC.text_to_be_present_in_element(
            (MarkPageLocators.MODEL_SPAN), text))

    def cleanSelections(self):
        search_button = self.driver.find_element(
            *BasePageLocators.SEARCH_BUTTON)

        search_button.click()

    def waitForSubmitButton(self):
        wait = WebDriverWait(self.driver, 100)

        wait.until(EC.visibility_of_element_located(
            (MarkPageLocators.SUBMIT_BUTTON)
        ))

        wait.until(EC.element_attribute_to_include(
            (MarkPageLocators.SUBMIT_BUTTON), 'disabled'
        ))

        wait.until_not(EC.element_attribute_to_include(
            (MarkPageLocators.SUBMIT_BUTTON), 'disabled'
        ))

        print(colored('waited for selection', 'green'))

    def dictAllSelectOptions(self):

        wait = WebDriverWait(self.driver, 1)

        selects = self.driver.find_elements(*MarkPageLocators.SELECTS)
        selects_dic = {}

        for select in selects:
            if select.find_elements(By.TAG_NAME, 'select'):
                s = Select(select.find_element(By.TAG_NAME, 'select'))
                # dic = {}
                label = select.find_element(By.TAG_NAME, 'label').text
                options = s.options
                dic_options = optionsToArray(options)
                selects_dic[label] = dic_options

        return selects_dic

    def countSelects(self):
        return len(self.driver.find_elements(*MarkPageLocators.FORM_GROUP_SELECTS))

    def selectOption(self, combination={}):
        keys = list(combination.keys())
        keys.sort()
        result = {
            'success': False,
            'invalid_combination': {}
        }

        for key in keys:
            select_form_control = self.findSelectFormControl(key)
            text = combination[key]['text']

            warning(f'Checking {key}: {text}')
            try:
                if select_form_control:
                    if select_form_control.find_elements(By.TAG_NAME, 'select'):
                        select = Select(select_form_control.find_element(
                            By.TAG_NAME, 'select'))
                        if (self.checkOptionExistance(select, text)):
                            select.select_by_visible_text(text)
                            self.waitForSubmitButton()
                            success(f'Selected {key}: {text}')
                            result['invalid_combination'][key] = combination[key]['text']

                        else:
                            danger(f'Option {key}: {text} does not exists')

                    else:
                        warning(f'Already auto-selected option')

                        result['status'] = True
                        # return result
                else:
                    result['status'] = True
                    return result
            except:
                result['status'] = True
                return result
        result['status'] = True
        return result

    def submit(self):
        wait = WebDriverWait(self.driver, 100)

        warning('waiting for submit button')
        submit_button = wait.until(EC.element_to_be_clickable(
            (MarkPageLocators.SUBMIT_BUTTON)
        ))

        submit_button.click()

    def waitForPanel(self):
        wait = WebDriverWait(self.driver, 1000)
        wait.until(EC.visibility_of_element_located(
            MarkPageLocators.MODELS_SELECT))

    def checkOptionExistance(self, select, text):
        try:
            if (select.options):
                for option in select.options:
                    if option.text == text:
                        return True
        except print(0):
            return False

    def findSelectFormControl(self, label=''):
        select_form_controls = self.driver.find_elements(
            *MarkPageLocators.SELECTS)

        for select_form_control in select_form_controls:

            try:
                select_form_control_label = select_form_control.find_element(
                    By.TAG_NAME, 'label')
                select_label = select_form_control_label.text or ''
                if select_form_control_label and select_label == label:
                    return select_form_control
            except:
                return False

        return False

    def goToBasePage(self, url):
        self.driver.get(url)
        self.waitForPanel()

    def getParameters(self):
        parameters = []
        
        form_groups = self.driver.find_elements(By.CSS_SELECTOR, '.panel .form-group')
        for group in form_groups:
        
        
        
        return


def optionsToArray(options):
    """Creates array with dictionaries"""
    options_array = []
    for option in options:
        val = option.get_attribute("value").strip()
        if val:
            option_dict = {
                'text': option.text,
                'value': val
            }
            options_array.append(option_dict)

    return options_array


class VehiclePage(BasePage):
    def vehicleRows(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located(
            VehiclePageLocators.NOT_FIRST_ROW))
        rows = self.driver.find_elements(*VehiclePageLocators.NOT_FIRST_ROW)

        return rows


class PartCategoriesPage(BasePage):

    def parseEveryLeafCategory(self):
        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located(
            VehiclePageLocators.CATEGORY_NODES))

        nodes = self.driver.find_elements(*VehiclePageLocators.CATEGORY_NODES)
        leafs = self.driver.find_elements(*VehiclePageLocators.CATEGORY_LEAFS)
        for plus in self.driver.find_elements(By.CSS_SELECTOR, '.qgExpandClosed > .qgExpand'):
            wait.until(EC.element_to_be_clickable(plus))
            plus.click()

        for leaf in leafs:
            category_names = []
            temp_leaf = leaf

            try:
                parents = temp_leaf.find_elements(
                    *VehiclePageLocators.CATEGORY_PARENT)
            except:
                parents = []

            name_content = temp_leaf.find_element(
                By.CSS_SELECTOR, ':scope > .qgContent')

            name = name_content.text

            success(name)
            category_names.append(name)

            while parents:
                parent = parents.pop()

                name_content = parent.find_element(
                    By.CSS_SELECTOR, ':scope > .qgContent')

                name = name_content.text
                success(name)

                category_names.append(name)

            self.parseCategory(leaf, category_names)

    def parseCategory(self, node, category_names=[]):
        link = node.find_element(
            By.CSS_SELECTOR, ':scope > .qgContent > a').get_attribute('href')

        # self.driver.execute_script(f'''window.open("{link}","_blank");''')
        # detail_page = DetailPage(self.driver)
        # detail_page.parse()

        # self.driver.close()
        # self.driver.switch_to.window(self.driver.window_handles[0])


class DetailPage(BasePage):
    def parse(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

        wait = WebDriverWait(self.driver, 100)
        wait.until(EC.presence_of_element_located(
            DetailPageLocators.NOT_FIRST_ROW))

        group_name = self.driver.find_element(
            *DetailPageLocators.GROUP_NAME).text
        subgroup_name = self.driver.find_element(
            *DetailPageLocators.SUBGROUP_NAME).text

        detail_rows = self.driver.find_elements(
            *DetailPageLocators.NOT_FIRST_ROW)
        success(group_name)
        success(subgroup_name)
