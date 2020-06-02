from selenium import webdriver
import time
import math
"""Всплывающие окно (alert)"""
"""Задачка:
1.Открыть страницу 
2.Нажать на кнопку
3.Принять confirm
4.На новой странице решить капчу для роботов"""

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/alert_accept.html')

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))   # создаем функцию для просчета

try:
    button_big = browser.find_element_by_class_name('btn.btn-primary').click()  # ищем кнопку
    confirm = browser.switch_to.alert    # переключаемся в окно
    confirm.accept()       # принимаем его с помощью команды accept

    x_element = browser.find_element_by_id('input_value')    # ищем число (значение х)
    x = x_element.text      # возвращает текст между тегами
    y = calc(x)        # создаем переменную y, считаем математич функцию от х

    x_element1 = browser.find_element_by_id('answer')     # ищем поле ввода
    x_element1.send_keys(y)      # в поля ввода вставляем наше значение посчитан на калькул

    button = browser.find_element_by_xpath('//button[text()="Submit"]').click()  # ищем кнопку отправить

finally:
    time.sleep(5)

    browser.quit()   # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла

