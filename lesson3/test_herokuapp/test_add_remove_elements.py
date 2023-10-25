from selenium.webdriver.common.by import By
from locators import BUTTON_ADD_ELEMENT, BUTTON_DELETE_ANY
from data import ADD_REMOVE_ELEMENTS_PAGE


def test_add_element(driver, wait):
    driver.get(ADD_REMOVE_ELEMENTS_PAGE)
    driver.find_element(By.XPATH, BUTTON_ADD_ELEMENT).click()

    number_of_delete_buttons = driver.find_elements(By.XPATH, BUTTON_DELETE_ANY)
    assert len(number_of_delete_buttons) == 1


def test_delete_added_element(driver, wait):
    driver.get(ADD_REMOVE_ELEMENTS_PAGE)
    driver.find_element(By.XPATH, BUTTON_ADD_ELEMENT).click()

    number_of_delete_buttons_before = driver.find_elements(By.XPATH, BUTTON_DELETE_ANY)
    assert len(number_of_delete_buttons_before) == 1

    driver.find_element(By.XPATH, BUTTON_DELETE_ANY).click()
    number_of_delete_buttons_after = driver.find_elements(By.XPATH, BUTTON_DELETE_ANY)
    assert len(number_of_delete_buttons_after) == 0
