import pytest
from selenium import webdriver
from locators import USERNAME_FIELD, PASSWORD_FIELD, LOGIN_BUTTON, BURGER_MENU_BUTTON
from data import VALID_LOGIN, VALID_PASSWORD, MAIN_PAGE
from selenium.webdriver.common.by import By


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    yield driver
    print('\nquit browser...')
    driver.quit()


@pytest.fixture()
def login(driver):
    driver.get(MAIN_PAGE)
    driver.find_element(By.XPATH, USERNAME_FIELD).send_keys(VALID_LOGIN)
    driver.find_element(By.XPATH, PASSWORD_FIELD).send_keys(VALID_PASSWORD)
    driver.find_element(By.XPATH, LOGIN_BUTTON).click()
    yield


@pytest.fixture()
def open_burger_menu(driver, login):
    driver.find_element(By.XPATH, BURGER_MENU_BUTTON).click()
    yield


