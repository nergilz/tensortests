import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


def scenario_1():

    try:
        driver = webdriver.Firefox()
        driver.get('https://ya.ru')
        time.sleep(3)

        elem_find = driver.find_element_by_id("text")
        elem_find.clear()
        elem_find.send_keys("тензор")
        time.sleep(3)

        elem_suggest = driver.find_element_by_class_name('popup__getposoffix')
        elem_find.send_keys(Keys.RETURN)
        time.sleep(3)

        url = driver.find_element_by_link_text('tensor.ru')
        driver.close()

        return True

    except NoSuchElementException:
        driver.close()
        return False


def scenario_2():

    try:
        driver = webdriver.Firefox()
        driver.get('https://yandex.ru')
        time.sleep(5)

        images_elem = driver.find_element_by_link_text('Картинки')
        images_elem.click()
        time.sleep(5)

        image = driver.find_element_by_class_name('cl-teaser__link')
        image.click()
        time.sleep(5)

        src_image_first = driver.find_element_by_class_name(
            'image__image').get_attribute("src")
        time.sleep(5)

        right_img = driver.find_element_by_class_name('layout__nav__right')
        right_img.click()
        time.sleep(5)

        left_img = driver.find_element_by_class_name('layout__nav__left')
        left_img.click()
        time.sleep(5)

        src_image_second = driver.find_element_by_class_name(
            'image__image').get_attribute("src")
        time.sleep(5)

        if src_image_first == src_image_second:
            driver.close()
            return True
        else:
            return False

    except NoSuchElementException:
        driver.close()
        return False


if __name__ == '__main__':

    test1 = scenario_1()
    test2 = scenario_2()
    print(test1)
    print(test2)
