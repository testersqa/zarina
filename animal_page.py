from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

from base_page import BasePage


class AnimalPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)
        self.hamburger = "//span[@class='hamburger-box']"

    def open_hamburger(self):
        hamb = self.driver.find_element(By.XPATH, self.hamburger)

        self.actions.move_to_element(hamb)
        self.actions.click(hamb)
        self.actions.perform()