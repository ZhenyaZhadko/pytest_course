from selenium.webdriver.common.by import By
import time
from locators import INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON, HEADER_OPEN_SHOPPING_CART_LINK, \
    SHOPPING_CART_REMOVE_BACKPACK_ITEM_BUTTON, SHOPPING_CART_REMOVED_ITEM, INVENTORY_BACKPACK_ITEM_TITLE_LINK, \
    PRODUCT_CARD_REMOVE_SAUCE_LABS_BACKPACK_BUTTON, PRODUCT_CARD_BACKPACK_ADD_TO_CART_BUTTON, ALL_CART_ITEMS


def test_remove_product_from_cart_on_cart_page(driver, login):

    driver.find_element(By.XPATH, INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON).click()

    time.sleep(1)
    driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK).click()

    remove_backpack_button = driver.find_element(By.XPATH, SHOPPING_CART_REMOVE_BACKPACK_ITEM_BUTTON)
    remove_backpack_button.click()

    removed_element = driver.find_elements(By.XPATH, SHOPPING_CART_REMOVED_ITEM)

    assert len(removed_element) > 0


def test_remove_product_from_cart_on_product_card_page(driver, login):

    driver.find_element(By.XPATH, INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON).click()

    time.sleep(2)
    driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE_LINK).click()

    driver.find_element(By.XPATH, PRODUCT_CARD_REMOVE_SAUCE_LABS_BACKPACK_BUTTON).click()

    time.sleep(1)
    add_to_cart_backpack_button_text = driver.find_element(By.XPATH, PRODUCT_CARD_BACKPACK_ADD_TO_CART_BUTTON).text
    assert add_to_cart_backpack_button_text == 'Add to cart'

    driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK).click()

    lst_of_products_in_cart = driver.find_elements(By.XPATH, ALL_CART_ITEMS)

    assert len(lst_of_products_in_cart) == 0
