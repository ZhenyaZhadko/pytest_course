from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_sorting_a_z():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    lst_products = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    lst_sorted_a_z_products_titles = []
    product_title = driver.find_element
    # creating list of titles of sorted products
    for product in range(1, len(lst_products) + 1):
        lst_sorted_a_z_products_titles.append(driver.find_element(By.XPATH, f'//div[@class="inventory_item"][{product}]//div[@class="inventory_item_name"]').text)
    check_lst_sorted_a_z_products_titles = sorted(lst_sorted_a_z_products_titles)

    assert lst_sorted_a_z_products_titles == check_lst_sorted_a_z_products_titles

    driver.quit()
