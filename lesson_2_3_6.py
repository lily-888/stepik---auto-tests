from selenium import webdriver
import time
import math

"""Переход на новую вкладку"""
"""Задачка:
1.Открыть страницу 
2.Нажать на кнопку
3.Переключиться на новую вкладку
4.Пройти капчу для робота"""

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/redirect_accept.html')

def calc(x):
    return str(math.log(abs(12*math.sin(int(x)))))     # создаем функцию для просчета

try:
    button1 = browser.find_element_by_class_name('trollface.btn.btn-primary').click()    # ищем кнопку

    new_window = browser.window_handles[1]     # созд перемен, выбираем новую вкладку (расчет с 0)
    browser.switch_to.window(new_window)       # переключаемся на новую вкладку

    x_element = browser.find_element_by_id('input_value')   # ищем число (значение х)
    x = x_element.text    # возвращает текст между тегами
    y = calc(x)     # создаем переменную y, считаем математическую функцию от х

    input = browser.find_element_by_id('answer')   # ищем поле ввода
    input.send_keys(y)   # в поля ввода вставляем наше значение посчитан на калькул

    button = browser.find_element_by_xpath('//button[text()="Submit"]').click()  # ищем кнопку отправить, клик

finally:
    time.sleep(5)

    browser.quit()      # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла

