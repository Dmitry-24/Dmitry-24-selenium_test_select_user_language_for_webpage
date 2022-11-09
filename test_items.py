from selenium.webdriver.common.by import By
from selenium import webdriver
import pytest
import time


link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_select_user_language_for_webpage(browser):
    browser.get(link)
    browser.implicitly_wait(10)
    basket_button = browser.find_elements(By.CSS_SELECTOR, ".add-to-basket>[type='submit']")
    assert basket_button, 'basket_button not found'
