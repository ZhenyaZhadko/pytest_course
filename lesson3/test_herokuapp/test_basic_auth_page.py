from selenium.webdriver.common.by import By
from data import BASIC_AUTH_PAGE_WITH_CORRECT_CREDENTIALS
from lesson3.test_herokuapp.locators import TITLE_BASIC_AUTH_PAGE, TEXT_SUCCESSFUL_AUTH


def test_basic_auth_with_correct_credentials(driver):
    driver.get(BASIC_AUTH_PAGE_WITH_CORRECT_CREDENTIALS)
    text_success_auth = driver.find_element(By.XPATH, TEXT_SUCCESSFUL_AUTH).text
    assert driver.find_element(By.XPATH, TITLE_BASIC_AUTH_PAGE).text == 'Basic Auth'
    assert text_success_auth == 'Congratulations! You must have the proper credentials.'
