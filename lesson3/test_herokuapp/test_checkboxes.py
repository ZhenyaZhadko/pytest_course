from selenium.webdriver.common.by import By
from data import CHECKBOXES_PAGE
from locators import TICKED_CHECKBOX_ANY, NOT_TICKED_CHECKBOX_ANY


def test_tick_checkbox(driver):
    driver.get(CHECKBOXES_PAGE)
    num_ticked_checkboxes_before = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))

    driver.find_element(By.XPATH, NOT_TICKED_CHECKBOX_ANY).click()
    num_ticked_checkboxes_after = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))
    assert num_ticked_checkboxes_after == num_ticked_checkboxes_before + 1


def test_untick_checkbox(driver):
    driver.get(CHECKBOXES_PAGE)
    num_ticked_checkboxes_before = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))

    driver.find_element(By.XPATH, TICKED_CHECKBOX_ANY).click()
    num_ticked_checkboxes_after = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))
    assert num_ticked_checkboxes_after == num_ticked_checkboxes_before - 1


def test_untick_all_checkboxes(driver):
    driver.get(CHECKBOXES_PAGE)
    num_ticked_checkboxes_before = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))

    driver.find_element(By.XPATH, NOT_TICKED_CHECKBOX_ANY).click()
    list_ticked_checkboxes_after = driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY)
    assert len(list_ticked_checkboxes_after) == num_ticked_checkboxes_before + 1

    for checkbox in range(1, len(list_ticked_checkboxes_after) + 1):
        driver.find_element(By.XPATH, f'{TICKED_CHECKBOX_ANY}[1]').click()

    num_ticked_checkboxes_after_unticking_all = len(driver.find_elements(By.XPATH, TICKED_CHECKBOX_ANY))
    assert num_ticked_checkboxes_after_unticking_all == 0
