from selenium import webdriver
import time
import math

"""Поиск картинки с помощью get_attribute"""
"""Задачка:
1.Открыть страницу.
2.Найти на ней элемент-картинку, который является изображением сундука с сокровищами.
3.Взять у этого элемента значение атрибута valuex, которое является значением x для задачи.
4.Посчитать математическую функцию от x.
5.Ввести ответ в текстовое поле.
6.Отметить checkbox "I'm the robot".
7.Выбрать radiobutton "Robots rule!".
8.Нажать на кнопку "Submit"."""

link = "http://suninjuly.github.io/get_attribute.html"

browser = webdriver.Chrome()
browser.get(link)

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))     # создаем функцию для просчета

try:
    x_element = browser.find_element_by_xpath('//img[@id="treasure"]')   # ищем изображение img
    x = x_element.get_attribute('valuex')   # получаем атрибут valuex
    y = calc(x)    # создаем новую переменную, вставляем значение атрибута valuex

    input1 = browser.find_element_by_id("answer")   # ищем поле ввода
    input1.send_keys(y)               # в поля ввода вставляем наше значение посчитан на калькул
    checkbox = browser.find_element_by_id("robotCheckbox")    # ищем checkbox
    checkbox.click()
    radiobutton = browser.find_element_by_id("robotsRule")  # ищем radiobutton
    radiobutton.click()

    button = browser.find_element_by_xpath('//button[text()="Submit"]')   # ищем кнопку отправить
    button.click()

finally:
    time.sleep(5)

    browser.quit()         # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
