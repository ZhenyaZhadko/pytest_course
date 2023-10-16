from selenium.webdriver.common.by import By
import time
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, ERROR_MESSAGE_CONTAINER
from data import VALID_LOGIN, INVALID_PASSWORD, MAIN_PAGE


def test_login_with_valid_credentials(driver, login):

    time.sleep(2)
    assert driver.current_url == "https://www.saucedemo.com/inventory.html"

def test_login_with_invalid_credentials(driver):
    driver.get(MAIN_PAGE)

    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(VALID_LOGIN)

    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(INVALID_PASSWORD)

    driver.find_element(By.XPATH, LOGIN_BUTTON).click()

    time.sleep(2)
    error_message = driver.find_element(By.XPATH, ERROR_MESSAGE_CONTAINER).text
    assert error_message == "Epic sadface: Username and password do not match any user in this service"


