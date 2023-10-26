from selenium.webdriver.common.by import By
from data import BROKEN_IMAGES_PAGE, STATUS_CODE_OK
from locators import IMG_ANY
import requests


def test_broken_images(driver):
    driver.get(BROKEN_IMAGES_PAGE)
    list_images = driver.find_elements(By.XPATH, IMG_ANY)
    list_img_links = []

    for image in range(1, len(list_images) + 1):
        image_link = driver.find_element(By.XPATH,
                                            f'{IMG_ANY}[{image}]').get_property("src")
        list_img_links.append(image_link)

    list_broken_links = []
    for link in list_img_links:
        response = requests.get(link)
        if response.status_code != STATUS_CODE_OK:
            list_broken_links.append(link)

    assert len(list_broken_links) == 0, f"Broken links: {list_broken_links}"
