from selenium.webdriver.common.by import By
import time
from locators import INVENTORY_BACKPACK_ITEM_TITLE_LINK, INVENTORY_BACKPACK_ITEM_IMAGE, PRODUCT_TITLE_IN_PRODUCT_CARD

def test_open_product_cart_after_product_image_click(driver, login):

    backpack_title_in_catalog = driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE_LINK).text

    driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_IMAGE).click()

    time.sleep(2)
    backpack_title_in_product_card = driver.find_element(By.XPATH, PRODUCT_TITLE_IN_PRODUCT_CARD).text

    assert backpack_title_in_catalog == backpack_title_in_product_card


def test_open_product_card_after_product_title_click(driver, login):

    backpack_title_in_catalog = driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE_LINK).text

    driver.find_element(By.XPATH, INVENTORY_BACKPACK_ITEM_TITLE_LINK).click()

    time.sleep(2)
    backpack_title_in_product_card = driver.find_element(By.XPATH, PRODUCT_TITLE_IN_PRODUCT_CARD).text
    assert backpack_title_in_product_card == backpack_title_in_catalog
