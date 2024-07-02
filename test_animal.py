import time

from animal_page import AnimalPage


def test_animal(browser):
    animal_page = AnimalPage(browser)
    animal_page.open_site()
    time.sleep(2)

    animal_page.close_qr_modal()
    time.sleep(1)
    animal_page.close_cookie_modal()
    time.sleep(1)

    animal_page.click_btn_change()
    time.sleep(1)
    animal_page.change_city('Казань')
    time.sleep(10)

    # animal_page.close_banner()
    time.sleep(3)
    animal_page.open_hamburger()
    time.sleep(5)
