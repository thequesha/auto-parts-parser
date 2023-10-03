from parse import PartsParser
from selenium import webdriver

driver = webdriver.Chrome()

parser = PartsParser(driver)
parser.parse()
