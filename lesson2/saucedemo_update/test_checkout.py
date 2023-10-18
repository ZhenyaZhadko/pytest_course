from selenium.webdriver.common.by import By
import time
from locators import INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON, HEADER_OPEN_SHOPPING_CART_LINK, \
    SHOPPING_CART_CHECKOUT_BUTTON, CHECKOUT_FIRST_NAME_INPUT, CHECKOUT_LAST_NAME_INPUT, CHECKOUT_POSTAL_CODE_INPUT, \
    CHECKOUT_CONTINUE_AFTER_FILLING_PERSONAL_DATA_BUTTON, CHECKOUT_FINISH_BUTTON, CHECKOUT_PAGE_TITLE, \
    CHECKOUT_COMPLETE_HEADER


def test_successful_checkout_complete(driver, login):

    driver.find_element(By.XPATH, INVENTORY_ADD_SAUCE_LABS_BACKPACK_BUTTON).click()

    driver.find_element(By.XPATH, HEADER_OPEN_SHOPPING_CART_LINK).click()

    driver.find_element(By.XPATH, SHOPPING_CART_CHECKOUT_BUTTON).click()

    time.sleep(1)
    driver.find_element(By.XPATH, CHECKOUT_FIRST_NAME_INPUT).send_keys('Mary')
    driver.find_element(By.XPATH, CHECKOUT_LAST_NAME_INPUT).send_keys('Smith')
    driver.find_element(By.XPATH, CHECKOUT_POSTAL_CODE_INPUT).send_keys('10010')

    driver.find_element(By.XPATH, CHECKOUT_CONTINUE_AFTER_FILLING_PERSONAL_DATA_BUTTON).click()

    time.sleep(1)
    driver.find_element(By.XPATH, CHECKOUT_FINISH_BUTTON).click()

    time.sleep(1)
    successul_checkout_title_text = driver.find_element(By.XPATH, CHECKOUT_PAGE_TITLE).text
    successful_checkout_header_text = driver.find_element(By.XPATH, CHECKOUT_COMPLETE_HEADER).text
    assert successul_checkout_title_text == 'Checkout: Complete!'
    assert successful_checkout_header_text == 'Thank you for your order!'
