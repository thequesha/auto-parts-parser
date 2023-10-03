from selenium.webdriver.support.wait import WebDriverWait


class BasePageElement(object):
    """Base page class that is initialized on every page object class."""

    def __set__(self, obj, value):
        """Sets the text to the value supplied"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element('name', self.locator))  # type: ignore
        driver.find_element('name', self.locator).clear()  # type: ignore
        driver.find_element('name',
                            self.locator).send_keys(value)  # type: ignore

    def __get__(self, obj, owner):
        """Gets the text of the specified object"""

        driver = obj.driver
        WebDriverWait(driver, 100).until(
            lambda driver: driver.find_element('name', self.locator))  # type: ignore
        element = driver.find_element('name', self.locator)  # type: ignore
        return element.get_attribute("value")
