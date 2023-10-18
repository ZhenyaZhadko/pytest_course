from selenium.webdriver.common.by import By
from locators import A_Z_SORTING_OPTION, INVENTORY_ANY_ITEM_NAME, INVENTORY_ANY_ITEM, Z_A_SORTING_OPTION, HIGH_LOW_SORTING_OPTION, LOW_HIGH_SORTING_OPTION, INVENTORY_ANY_ITEM_PRICE


def test_sorting_a_z(driver, login):
    driver.find_element(By.XPATH, A_Z_SORTING_OPTION).click()

    lst_products = driver.find_elements(By.XPATH, INVENTORY_ANY_ITEM_NAME)
    lst_sorted_a_z_products_titles = []

    # creating list of titles of sorted products
    for product in range(1, len(lst_products) + 1):
        lst_sorted_a_z_products_titles.append(driver.find_element(By.XPATH,
                                                                  f'{INVENTORY_ANY_ITEM}[{product}]{INVENTORY_ANY_ITEM_NAME}').text)

    # creating sorted list from lst_sorted_a_z_products_titles, flag reverse=False
    check_lst_sorted_a_z_products_titles = sorted(lst_sorted_a_z_products_titles, reverse=False)

    assert lst_sorted_a_z_products_titles == check_lst_sorted_a_z_products_titles


def test_sorting_z_a(driver, login):
    driver.find_element(By.XPATH, Z_A_SORTING_OPTION).click()

    lst_products = driver.find_elements(By.XPATH, INVENTORY_ANY_ITEM_NAME)
    lst_sorted_z_a_products_titles = []

    # creating list of titles of sorted products
    for product in range(1, len(lst_products) + 1):
        lst_sorted_z_a_products_titles.append(driver.find_element(By.XPATH,
                                                                  f'{INVENTORY_ANY_ITEM}[{product}]{INVENTORY_ANY_ITEM_NAME}').text)

    # creating sorted list from lst_sorted_a_z_products_titles, flag reverse=False
    check_lst_sorted_z_a_products_titles = sorted(lst_sorted_z_a_products_titles, reverse=True)

    assert lst_sorted_z_a_products_titles == check_lst_sorted_z_a_products_titles


def test_sorting_low_high(driver, login):

    driver.find_element(By.XPATH, LOW_HIGH_SORTING_OPTION).click()

    lst_products = driver.find_elements(By.XPATH, INVENTORY_ANY_ITEM_NAME)
    lst_sorted_low_high_products_prices = []

    # creating list of titles of sorted products
    for product in range(1, len(lst_products) + 1):
        product_price = driver.find_element(By.XPATH,
                                            f'{INVENTORY_ANY_ITEM}[{product}]{INVENTORY_ANY_ITEM_PRICE}').text
        product_price = product_price.strip('$')
        lst_sorted_low_high_products_prices.append(float(product_price))

    # creating sorted list from lst_sorted_low_high_products_prices, flag reverse=False
    check_lst_sorted_low_high_products_prices = sorted(lst_sorted_low_high_products_prices, reverse=False)

    assert lst_sorted_low_high_products_prices == check_lst_sorted_low_high_products_prices


def test_sorting_high_low(driver, login):

    driver.find_element(By.XPATH, HIGH_LOW_SORTING_OPTION).click()

    lst_products = driver.find_elements(By.XPATH, INVENTORY_ANY_ITEM_NAME)
    lst_sorted_high_low_products_prices = []

    # creating list of titles of sorted products
    for product in range(1, len(lst_products) + 1):
        product_price = driver.find_element(By.XPATH,
                                            f'{INVENTORY_ANY_ITEM}[{product}]{INVENTORY_ANY_ITEM_PRICE}').text
        product_price = product_price.strip('$')
        lst_sorted_high_low_products_prices.append(float(product_price))

    # creating sorted list from lst_sorted_low_high_products_prices, flag reverse=False
    check_lst_sorted_high_low_products_prices = sorted(lst_sorted_high_low_products_prices, reverse=True)

    assert lst_sorted_high_low_products_prices == check_lst_sorted_high_low_products_prices
