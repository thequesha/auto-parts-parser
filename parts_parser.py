from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time
# Opening chrome webdriver
driver = webdriver.Chrome()
driver.get('https://emexdwc.ae/')

# clicking to tab (By car)
wait = WebDriverWait(driver, 10)
by_car_tab = wait.until(EC.element_to_be_clickable((driver.find_element(By.XPATH, '//*[@id="mainForm"]/div[7]/div/ul/li[2]/a'))))
ActionChains(driver).click(by_car_tab).perform()


cars_select = wait.until(EC.element_to_be_clickable((driver.find_element(By.XPATH, '//*[@id="tab4"]/div/select'))))
ActionChains(driver).click(cars_select).perform()

all_car_options = cars_select.find_elements(By.TAG_NAME, 'option')
for option in all_car_options:
    val = option.get_attribute("value").strip()
    if(val):
        print(f"Value is: {val}")


time.sleep(10)

# assert "Python" in driver.title
# elem = driver.find_element(By.NAME, "q")
# elem.clear()
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
driver.close()
