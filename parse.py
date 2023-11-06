from selenium import webdriver
from http_requests import HttpRequests
import page
import time
import itertools
from termcolor import colored
from selenium.webdriver.common.by import By
from helper import *


class PartsParser:
    """Parser Project for AutoParts"""

    def __init__(self, driver):
        self.driver = driver

    def parse(self):
        """Parses Auto Parts"""

        # setup initial configuration
        self.setUp()
        success('successfully initiated web driver')

        # define base page, so we could use base websites methods
        base_page = page.BasePage(self.driver)

        # change language ro Russian
        base_page.changeLang('Русский')
        base_page.closeCookieNotification()

        main_page = page.MainPage(self.driver)
        car_options = main_page.openCarMarkOptions(True)

        http_requests = HttpRequests()

        send_cars_list = http_requests.sendCarsList(car_options)
        success(f'Send Cars List To Server. Status code: {send_cars_list}')

        # while len(car_options):
        car_option = http_requests.getCarToBeParsed()
        main_page.openCarMarkOptions()
        main_page.clickToOption(car_option)
        # TODO: make wait instead of sleep
        mark_page = page.MarkPage(self.driver)
        mark_page.waitForPanel()
        mark_models = mark_page.getModelOptions()
        while len(mark_models):
            data = {
                'mark': car_option,
                'parameters': [],
                'categories': [],
                'grouped_details': [],
                'car_name': '',
            }

            mark_model = mark_models.pop(0)

            mark_page.selectMark(mark_model['text'])
            # TODO:Wait while it selects
            mark_page.waitForSubmitButton()
            current_url = self.driver.current_url
            selects_dic = mark_page.dictAllSelectOptions()
            all_combinations = self.getAllCombinations(selects_dic)
            selects_count = mark_page.countSelects()
            parsed_combos = []
            index = 0
            while all_combinations:
                combo = all_combinations.pop(0)
                index += 1
                result = mark_page.selectOption(combo)
                selects_count = mark_page.countSelects()
                warning(
                    f'Checking combo #{index} out of {len(all_combinations)}')
                if not selects_count and (combo not in parsed_combos):
                    success(f'Combo #{index} is valid')
                    
                    
                    parameters_list = mark_page.getParameters()

                    data['parameters'] = parameters_list
                    
                    mark_page.submit()

                    vehicle_page = page.VehiclePage(self.driver)
                    vehicle_rows = vehicle_page.vehicleRows()
                    vehicle_row_links = []
                    for row in vehicle_rows:
                        link = row.find_element(
                            By.CSS_SELECTOR, 'a').get_attribute('href')
                        vehicle_row_links.append(link)
                    for link in vehicle_row_links:
                        self.driver.get(link)
                        part_categories_page = page.PartCategoriesPage(
                            self.driver)
                        part_categories_page.parseEveryLeafCategory(data)

                    parsed_combos.append(combo)
                else:
                    if result['invalid_combination']:
                        all_combinations = filterCombinations(
                            all_combinations, result['invalid_combination'])
                    danger(f'Combo #{index} is invalid')
                    warning('Trying another combo')
                mark_page.goToBasePage(current_url)
            # while selects_count:
            #     while all_combinations:
            #         combination = all_combinations.pop(0)
            #         result = mark_page.selectOption(combination)
            #         # if result['invalid_combination']:
            #         #     all_combinations = filterCombinations(
            #         #         all_combinations, result['invalid_combination'])
            #         selects_count = mark_page.countSelects()
            #         if not selects_count:
            #             vehicle_page = page.VehiclePage(self.driver)
            #             vehicle_rows = vehicle_page.vehicleRows()
            #             for row in vehicle_rows:
            #                 row.click()
            #                 part_categories_page = page.PartCategoriesPage(
            #                     self.driver)
            #                 part_categories_page.parseEveryLeafCategory()
            #             mark_page.goToBasePage(current_url)
        mark_page.cleanSelections()

    def setUp(self):
        """initial setup"""

        url = "https://emexdwc.ae/"
        warning(f'Trying to open: {url}')

        try:
            self.driver.get(url)
            success(f'Successfully opened: {url}')
        except:
            danger(f'Couldn\'t open page: {url}')
            self.driver.close()
            pass

        self.driver.maximize_window()
        success('maximixed window')

    def getAllCombinations(self, d={}):
        keys, values = zip(*d.items())

        all_combinations = [dict(zip(keys, v))
                            for v in itertools.product(*values)]

        return all_combinations


def filterCombinations(combinations=[], invalid_combination={}):
    popped_combos = []

    for index, combo in enumerate(combinations):
        results = []
        for key in invalid_combination.keys():
            result = (combo[key]['text'] == invalid_combination[key])
            results.append(result)

        if False not in results:
            popped_combos.append(combinations.pop(index))

    success(
        f'Removed {len(popped_combos)} invalid combos. {len(combinations)} combos left')

    filtered_combinations = combinations

    return filtered_combinations
