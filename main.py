from helper import *
from parse import PartsParser
from selenium import webdriver

chromedriver_path = r'C:\bin\chromedriver.exe'

service = webdriver.ChromeService(executable_path=chromedriver_path)
driver = webdriver.Chrome(service=service)

parser = PartsParser(driver)


while True:
    try:
        parser.parse()
    except:
        driver.quit()
        danger('Something went wrong')
        parser.parse()
