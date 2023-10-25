from selenium.webdriver.common.by import By
import time
from locators import HEADER_MAIN_PAGE, BUTTON_START_TEST, INPUT_FIELD_LOGIN, INPUT_FIELD_PASSWORD, \
    CHECKBOX_AGREE_TO_RULES, BUTTON_REGISTER, TEXT_REGISTRATION_SUCCESS, LOADER
from data import VALID_LOGIN, MAIN_PAGE, VALID_PASSWORD


def test_auth_with_time_sleep(driver):
    driver.get(MAIN_PAGE)
    header_text = driver.find_element(By.XPATH, HEADER_MAIN_PAGE).text

    assert header_text == "Практика с ожиданиями в Selenium"
    time.sleep(5)

    driver.find_element(By.XPATH, BUTTON_START_TEST).click()

    driver.find_element(By.XPATH, INPUT_FIELD_LOGIN).send_keys(VALID_LOGIN)

    driver.find_element(By.XPATH, INPUT_FIELD_PASSWORD).send_keys(VALID_PASSWORD)

    driver.find_element(By.XPATH, CHECKBOX_AGREE_TO_RULES).click()

    driver.find_element(By.XPATH, BUTTON_REGISTER).click()

    time.sleep(0.5)
    assert driver.find_element(By.XPATH, LOADER).is_displayed() == True

    time.sleep(5)
    text_registration_success = driver.find_element(By.XPATH, TEXT_REGISTRATION_SUCCESS).text
    assert text_registration_success == "Вы успешно зарегистрированы!"
