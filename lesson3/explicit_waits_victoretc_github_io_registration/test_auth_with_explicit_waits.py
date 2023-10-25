from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from locators import HEADER_MAIN_PAGE, BUTTON_START_TEST, INPUT_FIELD_LOGIN, INPUT_FIELD_PASSWORD, \
    CHECKBOX_AGREE_TO_RULES, BUTTON_REGISTER, TEXT_REGISTRATION_SUCCESS, LOADER
from data import VALID_LOGIN, MAIN_PAGE, VALID_PASSWORD


def test_auth_with_explicit_waits(driver, wait):
    driver.get(MAIN_PAGE)
    header_text = driver.find_element(By.XPATH, HEADER_MAIN_PAGE).text

    assert header_text == "Практика с ожиданиями в Selenium"

    visible_after_button = wait.until(EC.element_to_be_clickable((By.XPATH, BUTTON_START_TEST)))
    visible_after_button.click()

    driver.find_element(By.XPATH, INPUT_FIELD_LOGIN).send_keys(VALID_LOGIN)

    driver.find_element(By.XPATH, INPUT_FIELD_PASSWORD).send_keys(VALID_PASSWORD)

    driver.find_element(By.XPATH, CHECKBOX_AGREE_TO_RULES).click()

    driver.find_element(By.XPATH, BUTTON_REGISTER).click()

    assert driver.find_element(By.XPATH, LOADER).is_displayed() == True

    visible_after_start_test_button = wait.until(EC.element_to_be_clickable((By.XPATH, BUTTON_START_TEST)))
    visible_after_start_test_button.click()

    text_registration_success = wait.until(EC.element_to_be_clickable((By.XPATH, TEXT_REGISTRATION_SUCCESS)))
    assert text_registration_success.text == "Вы успешно зарегистрированы!"
