from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_add_product_to_cart_from_catalog_page():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)
    add_to_cart_backpack = driver.find_element(By.XPATH, '//button[@data-test="add-to-cart-sauce-labs-backpack"]')
    add_to_cart_backpack.click()

    link_to_open_cart = driver.find_element(By.XPATH, '//a[@class="shopping_cart_link"]')
    link_to_open_cart.click()

    checkout_button = driver.find_element(By.XPATH, '//button[@data-test="checkout"]')
    checkout_button.click()

    time.sleep(1)
    first_name = driver.find_element(By.XPATH, '//input[@data-test="firstName"]')
    first_name.send_keys('Mary')
    last_name = driver.find_element(By.XPATH, '//input[@data-test="lastName"]')
    last_name.send_keys('Smith')
    zip_code = driver.find_element(By.XPATH, '//input[@data-test="postalCode"]')
    zip_code.send_keys('10010')

    continue_button = driver.find_element(By.XPATH, '//input[@data-test="continue"]')
    continue_button.click()

    time.sleep(2)
    finish_button = driver.find_element(By.XPATH, '//button[@data-test="finish"]')
    finish_button.click()

    time.sleep(1)
    checkout_title = driver.find_element(By.XPATH, '//span[@class="title"]')
    checkout_complete_header = driver.find_element(By.XPATH, '//h2[@class="complete-header"]')
    assert checkout_title.text == 'Checkout: Complete!'
    assert checkout_complete_header.text == 'Thank you for your order!'

    driver.quit()
