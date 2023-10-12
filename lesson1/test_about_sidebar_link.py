from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_about_sidebar_link():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()

    time.sleep(2)
    about_sidebar_link = driver.find_element(By.XPATH, '//a[@id="about_sidebar_link"]')
    about_sidebar_link.click()

    time.sleep(2)
    assert driver.current_url == "https://saucelabs.com/"

    driver.quit()
