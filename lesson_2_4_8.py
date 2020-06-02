from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

"""Ждем нужный текст на странице"""
"""Задачка:
1.Открыть страницу 
2.Дождаться, когда цена дома уменьшится до $100 (ожидание нужно установить не меньше 12 секунд)
3.Нажать на кнопку "Book"
4.Решить уже известную нам математическую задачу"""

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/explicit_wait2.html")

def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))     # создаемаем функцию для просчета

price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
# говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
button_book = browser.find_element_by_id('book').click()
# создаем перемен и ищем кнопку, когда цена будет 100 сработ кнопка book

x_element = browser.find_element_by_id('input_value')    # ищем число (значение х)
x = x_element.text       # возвращает текст между тегами
y = calc(x)     # созд перемен y, считаем математич функцию от х

input = browser.find_element_by_id('answer')    # ищем поле ввода
input.send_keys(y)     # в поля ввода вставляем наше значение посчитан на калькул

button = browser.find_element_by_xpath('//button[text()="Submit"]').click()    # ищем кнопку отправить

browser.quit()    # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла


