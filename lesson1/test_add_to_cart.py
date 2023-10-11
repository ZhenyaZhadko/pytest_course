from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_backpack_add_to_cart():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    backpack_title_in_catalog = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text

    time.sleep(2)
    add_to_cart_backpack = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_backpack.click()

    time.sleep(2)
    shopping_cart_badge = driver.find_element(By.XPATH, '//span[@class="shopping_cart_badge"]')
    text_of_backpack_button = driver.find_element(By.XPATH, '//button[@data-test="remove-sauce-labs-backpack"]').text
    assert text_of_backpack_button == 'Remove'
    assert shopping_cart_badge.text == '1'

    link_to_open_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    link_to_open_cart.click()

    backpack_title_in_cart = driver.find_element(By.XPATH, '//div[contains(text(), "Sauce Labs Backpack")]').text
    assert backpack_title_in_cart == backpack_title_in_catalog

    driver.quit()
