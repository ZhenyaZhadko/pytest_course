from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_logout_sidebar_link():
    driver.get("https://www.saucedemo.com/")

    login_logo_text = driver.find_element(By.XPATH, "//div[@class='login_logo']").text
    url_login = driver.current_url

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    burger_menu = driver.find_element(By.XPATH, '//button[@id="react-burger-menu-btn"]')
    burger_menu.click()

    time.sleep(2)
    logout_sidebar_link = driver.find_element(By.XPATH, '//a[@id="logout_sidebar_link"]')
    logout_sidebar_link.click()

    login_logo_text_after_logout = driver.find_element(By.XPATH, "//div[@class='login_logo']").text

    url_after_logout = driver.current_url

    assert url_after_logout == url_login
    assert login_logo_text == login_logo_text_after_logout

    driver.quit()
