from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_remove_product_from_cart_on_product_card_page():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)
    add_backpack_to_cart_from_catalog = driver.find_element(By.XPATH,
                                                            '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_backpack_to_cart_from_catalog.click()

    time.sleep(2)
    link_to_open_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    link_to_open_cart.click()

    lst_of_products_in_cart = driver.find_elements(By.XPATH, '// div[@class ="cart_item"]')

    assert len(lst_of_products_in_cart) > 0

    time.sleep(2)
    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()

    time.sleep(2)
    reset_sidebar_link = driver.find_element(By.XPATH, '//a[@id="reset_sidebar_link"]')
    reset_sidebar_link.click()

    driver.refresh()
    lst_of_products_in_cart_after_reset = driver.find_elements(By.XPATH, '// div[@class ="cart_item"]')

    assert len(lst_of_products_in_cart_after_reset) == 0

    driver.quit()
