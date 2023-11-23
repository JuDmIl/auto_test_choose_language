import pytest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException  

# Проверяемая страница
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

# Тест на наличие кнопки "Добавить в корзину"
def test_should_see_button_add(browser):
    browser.get(link)
    # Пауза 30 с для оценки текста на кнопке
    #time.sleep(30)

# При отсутствии кнопки - исключение
    try:
        # Для ожидания загрузки страницы при низкой скорости соединения
        #time.sleep(1)
        # Поиск кнопки
        browser.find_element(By.XPATH, '//button[@class="btn btn-lg btn-primary btn-add-to-basket"]')
        print('Button - ok!')
        result = True
    except NoSuchElementException:
        print('No button!')
        result = False
    assert result, "No button!"
