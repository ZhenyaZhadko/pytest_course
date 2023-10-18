from selenium.webdriver.common.by import By
import time
from locators import (INVENTORY_BACKPACK_ITEM_TITLE, INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON,
                      HEADER_SHOPPING_CART_BADGE, HEADER_OPEN_SHOPPING_CART_LINK,
                      INVENTORY_REMOVE_SAUCE_LABS_BACKPACK_BUTTON, SHOPPING_CART_BACKPACK_ITEM_TITLE,
                      INVENTORY_BACKPACK_ITEM_TITLE_LINK, PRODUCT_TITLE_IN_PRODUCT_CARD,
                      PRODUCT_CARD_BACKPACK_ADD_TO_CART_BUTTON)


def test_add_product_to_cart_from_catalog_page(driver, login):
    backpack_title_in_catalog = driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE).text

    driver.find_element(By.XPATH, INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON).click()

    time.sleep(2)
    shopping_cart_badge = driver.find_element(By.XPATH, HEADER_SHOPPING_CART_BADGE)
    text_of_backpack_button = driver.find_element(By.XPATH, INVENTORY_REMOVE_SAUCE_LABS_BACKPACK_BUTTON).text
    assert text_of_backpack_button == 'Remove'
    assert shopping_cart_badge.text == '1'

    driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK).click()

    backpack_title_in_cart = driver.find_element(By.XPATH, SHOPPING_CART_BACKPACK_ITEM_TITLE).text
    assert backpack_title_in_cart == backpack_title_in_catalog


def test_add_product_to_cart_from_product_card(driver, login):
    driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE_LINK).click()

    time.sleep(2)
    backpack_title_in_product_card = driver.find_element(By.XPATH, PRODUCT_TITLE_IN_PRODUCT_CARD).text

    driver.find_element(By.XPATH, PRODUCT_CARD_BACKPACK_ADD_TO_CART_BUTTON).click()

    time.sleep(2)
    shopping_cart_badge = driver.find_element(By.XPATH, HEADER_SHOPPING_CART_BADGE)
    text_of_backpack_button = driver.find_element(By.XPATH, INVENTORY_REMOVE_SAUCE_LABS_BACKPACK_BUTTON).text
    assert text_of_backpack_button == 'Remove'
    assert shopping_cart_badge.text == '1'

    driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK).click()

    backpack_title_in_cart = driver.find_element(By.XPATH, SHOPPING_CART_BACKPACK_ITEM_TITLE).text
    assert backpack_title_in_cart == backpack_title_in_product_card
