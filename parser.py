from bs4 import BeautifulSoup as bs
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from time import sleep

def par():
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get(
                'https://www.dns-shop.ru/catalog/markdown/')

        txt = []
        # while True:
        #         try:
        #                 driver.find_element(by=By.CLASS_NAME, value='pagination-widget__show-more-btn').click()
        #                 sleep(2)
        #         except NoSuchElementException:
        #                 print(2)
        #                 break
        for i in driver.find_elements(by=By.CLASS_NAME, value='catalog-product'):
                txt.append(i.find_element(by=By.CLASS_NAME, value='catalog-product__name').text.replace('\n',' ') + " - " +
                           i.find_element(by=By.CLASS_NAME, value='catalog-product__price-actual').text + '\n')
        print(''.join(txt), end='\n\n')
        while True:
                new_txt = []
                driver.refresh()
                time.sleep(10)
                for i in driver.find_elements(by=By.CLASS_NAME, value='catalog-product'):
                        if (i.find_element(by=By.CLASS_NAME, value='catalog-product__name').text.replace('\n', ' ') + " - " + i.find_element(
                                by=By.CLASS_NAME, value='catalog-product__price-actual').text + '\n') not in txt:
                                txt.append(i.find_element(by=By.CLASS_NAME, value='catalog-product__name').text.replace('\n', ' ') + " - " + i.find_element(by=By.CLASS_NAME, value='catalog-product__price-actual').text + '\n')
                                new
        return new_txt


