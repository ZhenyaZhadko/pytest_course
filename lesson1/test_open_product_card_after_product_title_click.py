from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()


def test_open_product_card_after_product_title_click():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    time.sleep(2)
    backpack_title_in_catalog = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]').text
    go_to_backpack_card_title_link = driver.find_element(By.XPATH, '//a[@id="item_4_title_link"]')
    go_to_backpack_card_title_link.click()

    time.sleep(2)
    backpack_title_in_product_card = driver.find_element(By.XPATH,
                                                         '//div[@class="inventory_details_name large_size"]').text
    assert backpack_title_in_product_card == backpack_title_in_catalog

    driver.quit()
