from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()


def test_sorting_high_low():
    driver.get("https://www.saucedemo.com/")

    username_field = driver.find_element(By.XPATH, '//input[@data-test="username"]')
    username_field.send_keys("standard_user")

    password_field = driver.find_element(By.XPATH, '//input[@data-test="password"]')
    password_field.send_keys("secret_sauce")

    login_button = driver.find_element(By.XPATH, '//input[@data-test="login-button"]')
    login_button.click()

    select_high_low_sorting = driver.find_element(By.XPATH,
                                                  '//select[@class="product_sort_container"]/option[@value="hilo"]')
    select_high_low_sorting.click()

    lst_products = driver.find_elements(By.XPATH, '//div[@class="inventory_item_name"]')
    lst_sorted_high_low_products_prices = []

    # creating list of prices of sorted high_low products
    for product in range(1, len(lst_products) + 1):
        product_price = driver.find_element(By.XPATH,
                                            f'//div[@class="inventory_item"][{product}]//div[@class="inventory_item_price"]').text
        product_price = product_price.strip('$')
        lst_sorted_high_low_products_prices.append(float(product_price))

    # creating sorted list from lst_sorted_high_low_products_prices, flag reverse=True
    check_lst_sorted_high_low_products_prices = sorted(lst_sorted_high_low_products_prices, reverse=True)

    assert lst_sorted_high_low_products_prices == check_lst_sorted_high_low_products_prices

    driver.quit()
