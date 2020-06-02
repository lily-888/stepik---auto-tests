from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

"""Работа с выпадающим списком"""
"""Задачка:
1.Открыть страницу 
2.Посчитать сумму заданных чисел
3.Выбрать в выпадающем списке значение равное расчитанной сумме
4.Нажать кнопку "Submit"""

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/selects1.html')

try:
    element1 = browser.find_element_by_id('num1')   # созд переменную ложим одно из значений додаваемых чисел
    number1 = element1.text
    element2 = browser.find_element_by_id('num2')   # созд переменную ложим второе значен додаваемых чисел
    number2 = element2.text
    sum = int(number1) + int(number2)     # созд переменную,  додаем верхние два значен переводя в int
    value = str(sum)        # созд переменную, сумму переводим в str

    select = Select(browser.find_element_by_tag_name("select"))  # использ класс select
    select.select_by_value(value)            # ищем нашу перемен с суммой (у нас value)
    browser.find_element_by_id("dropdown").click()  # выбираем значение из выпадающего списка, делаем клик

    button = browser.find_element_by_xpath('//button[text()="Submit"]').click()  # ищем кнопку отправить

finally:
    time.sleep(2)

    browser.quit()    # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла


