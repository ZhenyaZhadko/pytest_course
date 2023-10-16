from selenium.webdriver.common.by import By
import time
from data import MAIN_PAGE, SAUCELABS_COM_PAGE
from locators import LOGOUT_SIDEBAR_LINK, LOGIN_LOGO_TEXT, ABOUT_SIDEBAR_LINK


def test_logout_sidebar_link(driver, login, open_burger_menu):
    time.sleep(2)
    driver.find_element(By.XPATH, LOGOUT_SIDEBAR_LINK).click()

    login_logo_text_after_logout = driver.find_element(By.XPATH, LOGIN_LOGO_TEXT).text

    url_after_logout = driver.current_url

    assert url_after_logout == MAIN_PAGE
    assert login_logo_text_after_logout == 'Swag Labs'


def test_about_sidebar_link(driver, login, open_burger_menu):

    time.sleep(2)
    driver.find_element(By.XPATH, ABOUT_SIDEBAR_LINK).click()

    time.sleep(2)
    assert driver.current_url == SAUCELABS_COM_PAGE
