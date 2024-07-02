import time

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.actions = ActionChains(self.driver)
        self.base_url = "https://zarina.ru"
        self.qr_modal = "popmechanic-form-90177"
        self.banner = "popmechanic-form-90355"
        self.modal_close = "//div[@class = 'popmechanic-close']"
        self.yourcity_change = "//div[@class = 'ui-button-content' and text() = 'Нет, изменить']"
        self.cookie_modal = "//div[@class = 'ui-button-content' and text() = 'Окей']"
        self.city = "choose-city__name"

    def open_site(self):
        return self.driver.get(self.base_url)

    def close_qr_modal(self):
        # qr = WebDriverWait(self.driver, 10).until(
        #             EC.presence_of_element_located((By.XPATH, self.qr_modal))
        #         )
        # qr.find_element(By.XPATH, self.modal_close).click()
        time.sleep(3)
        qr = self.driver.find_element(By.ID, self.qr_modal)
        qr.find_element(By.XPATH, self.modal_close).click()

    def close_banner(self):
        banner = self.driver.find_element(By.ID, self.banner)
        banner.find_element(By.XPATH, self.modal_close).click()

    def close_cookie_modal(self):
        self.driver.find_element(By.XPATH, self.cookie_modal).click()

    def click_btn_change(self):
        self.driver.find_element(By.XPATH, self.yourcity_change).click()

    def change_city(self, city):
        self.driver.find_element(By.XPATH, f"//div[@class='{self.city}' and text()='{city}']").click()

    def get_current_url(self):
        return self.driver.current_url

    def go_to_back(self):
        self.driver.back()
