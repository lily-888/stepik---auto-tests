from selenium import webdriver
import time
import math
"""Клик на элементе, который перекрыт другим элементом.
Проскроллить страницу вниз."""
"""Задачка:
1.Открыть страницу.
2.Считать значение для переменной x.
3.Посчитать математическую функцию от x.
4.Проскроллить страницу вниз.
5.Ввести ответ в текстовое поле.
6.Выбрать checkbox "I'm the robot".
7.Переключить radiobutton "Robots rule!".
8.Нажать на кнопку "Submit"."""

browser = webdriver.Chrome()
browser.get('http://SunInJuly.github.io/execute_script.html')

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))       # создаем функцию для просчета

try:
    x_element = browser.find_element_by_id('input_value')        # ищем число (значение х)
    x = x_element.text      # возвращает текст между тегами
    y = calc(x)      # созд перемен y, считаем математич функцию от х

    button = browser.find_element_by_tag_name("button")   # ищем кнопку
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    # передаем текст скрипта и найденный элем button, к которому нужно будет проскролить страницу
    button.click()

    x_element = browser.find_element_by_id('answer')   # ищем поле ввода по id
    x_element.send_keys(y)    # в поля ввода вставляем наше значение посчитан на калькул

    checkbox = browser.find_element_by_id('robotCheckbox').click()     # ищем checkbox
    radiobutton = browser.find_element_by_id('robotsRule').click()     # ищем radiobutton

    button = browser.find_element_by_xpath('//button[text()="Submit"]')    # ищем кнопку отправить
    button.click()

finally:
    time.sleep(5)

    browser.quit()         # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла

