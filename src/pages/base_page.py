from deprecated import deprecated
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains, Chrome, Edge, Firefox
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.expected_conditions import StaleElementReferenceException
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    """Wrapper for selenium operations."""

    def __init__(self, driver: Chrome | Firefox | Edge, wait: WebDriverWait):
        self.driver = driver
        self.wait = wait

    def edit_cookie(self, cookie_key: str, cookie_value: str):
        cookie = self.wait.until(
            lambda d: d.get_cookie(cookie_key),
            message=f"Cookie '{cookie_key}' does not exist within the given timeout",
        )
        self.driver.delete_cookie(cookie_key)
        self.driver.add_cookie(
            {
                "name": cookie["name"],
                "value": cookie_value,
                "domain": cookie["domain"],
                "path": cookie["path"],
                "secure": cookie["secure"],
                "expiry": (cookie["expiry"]),
            }
        )

    def set_geo_location(self, latitude: float, longitude: float) -> None:
        """Sets the geolocation for the web browser using the Chrome DevTools
        Protocol (CDP).

        Parameters
        ----------
        - latitude (float): The latitude of the desired geolocation.
        - longitude (float): The longitude of the desired geolocation.

        Returns
        -------
        None

        Note:
        This method uses the Chrome DevTools Protocol (CDP) to override the geolocation
        in the web browser, allowing simulation of a specific geographic location for testing purposes.
        The accuracy is set to 1 for simplicity in this method.

        """
        self.driver.execute_cdp_cmd(
            "Emulation.setGeolocationOverride",
            {"latitude": latitude, "longitude": longitude, "accuracy": 1},
        )

    def click(self, locator: tuple[str, str]) -> None:
        el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        self._highlight_element(el, "green")
        el.click()

    def fill_text(self, locator: tuple[str, str], txt: str) -> None:
        el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        el.clear()
        self._highlight_element(el, "green")
        el.send_keys(txt)

    def clear_text(self, locator: tuple[str, str]) -> None:
        el: WebElement = self.wait.until(expected_conditions.element_to_be_clickable(locator))
        el.clear()

    def scroll_to_bottom(self) -> None:
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    def submit(self, webelement: WebElement) -> None:
        self._highlight_element(webelement, "green")
        webelement.submit()

    def get_text(self, locator: tuple[str, str]) -> str:
        el: WebElement = self.wait.until(expected_conditions.visibility_of_element_located(locator))
        self._highlight_element(el, "green")
        return el.text

    def move_to_element(self, webelement: WebElement) -> None:
        action = ActionChains(self.driver)
        self.wait.until(expected_conditions.visibility_of(webelement))
        action.move_to_element(webelement).perform()

    def is_elem_displayed(self, webelement: WebElement) -> bool:
        try:
            return webelement.is_displayed()
        except StaleElementReferenceException:
            return False
        except NoSuchElementException:
            return False

    @deprecated(reason="You should use another function")
    def _highlight_element(self, webelement: WebElement, color: str) -> None:
        original_style = webelement.get_attribute("style")
        new_style = f"background-color:yellow;border: 1px solid {color}{original_style}"
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + new_style
            + "');},0);",
            webelement,
        )
        self.driver.execute_script(
            "var tmpArguments = arguments;setTimeout(function () {tmpArguments[0].setAttribute('style', '"
            + original_style
            + "');},400);",
            webelement,
        )
