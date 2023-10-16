from selenium.webdriver.common.by import By
from locators import A_Z_SORTING_OPTION, INVENTORY_ANY_ITEM_NAME, INVENTORY_ANY_ITEM


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
