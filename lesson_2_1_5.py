from selenium import webdriver
import time
import math

"""Кликаем по checkboxes и radiobuttons"""
"""Задачка:
1.Открыть страницу.
2.Считать значение для переменной x.
3.Посчитать математическую функцию от x (код для этого приведён ниже).
4.Ввести ответ в текстовое поле.
5.Отметить checkbox "I'm the robot".
6.Выбрать radiobutton "Robots rule!".
7.Нажать на кнопку Submit."""

link = "http://suninjuly.github.io/math.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))    # создаем функцию для просчета

try:
    x_element = browser.find_element_by_id("input_value")    # ищем число (значение х)
    x = x_element.text   # возвращает текст между тегами
    y = calc(x)     # создаем перемен y, считаем математич функцию от х

    x_element = browser.find_element_by_id('answer')   # ищем поле ввода
    x_element.send_keys(y)   # в поля ввода вставляем наше значение посчитан на калькул

    checkbox = browser.find_element_by_id("robotCheckbox").click()    # ищем checkbox
    radiobutton = browser.find_element_by_id("robotsRule").click()     # ищем radiobutton

    button = browser.find_element_by_xpath('//button[text()="Submit"]').click()   # ищем кнопку отправить

finally:
    time.sleep(5)

    browser.quit()    # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла

