from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, SAUCELABS_COM_PAGE
from locators import (LOGOUT_SIDEBAR_LINK, LOGIN_LOGO_TEXT, ABOUT_SIDEBAR_LINK,
                      INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON, HEADER_OPEN_SHOPPING_CART_LINK, ALL_CART_ITEMS,
                      BURGER_MENU_BUTTON, RESET_SIDEBAR_LINK)


def test_logout_sidebar_link(driver, login, open_burger_menu):
    time.sleep(2)
    driver.find_element(By.XPATH, LOGOUT_SIDEBAR_LINK).click()

    login_logo_text_after_logout = driver.find_element(By.XPATH, LOGIN_LOGO_TEXT).text

    url_after_logout = driver.current_url

    assert url_after_logout == MAIN_PAGE
    assert login_logo_text_after_logout == 'Swag Labs'


def test_about_sidebar_link(driver, login, open_burger_menu):

    time.sleep(2)
    driver.find_element(By.XPATH, ABOUT_SIDEBAR_LINK).click()

    time.sleep(2)
    assert driver.current_url == SAUCELABS_COM_PAGE


def test_remove_product_from_cart_on_product_card_page(driver, login):

    add_backpack_to_cart_from_catalog = driver.find_element(By.XPATH,
                                                            INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON)
    add_backpack_to_cart_from_catalog.click()

    time.sleep(1)
    link_to_open_cart = driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK)
    link_to_open_cart.click()

    lst_of_products_in_cart = driver.find_elements(By.XPATH, ALL_CART_ITEMS)

    assert len(lst_of_products_in_cart) > 0

    time.sleep(2)
    burger_menu = driver.find_element(By.XPATH, BURGER_MENU_BUTTON)
    burger_menu.click()

    time.sleep(2)
    reset_sidebar_link = driver.find_element(By.XPATH, RESET_SIDEBAR_LINK)
    reset_sidebar_link.click()

    driver.refresh()
    lst_of_products_in_cart_after_reset = driver.find_elements(By.XPATH, ALL_CART_ITEMS)

    assert len(lst_of_products_in_cart_after_reset) == 0
