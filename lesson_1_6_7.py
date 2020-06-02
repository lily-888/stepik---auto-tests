from selenium import webdriver
import time

"""Заполняем поля с помощью цикла for"""

browser = webdriver.Chrome()
browser.get("http://suninjuly.github.io/huge_form.html")

try:
    elements = browser.find_elements_by_css_selector('div [type="text"]')

    for element in elements:  # запускаем цикл for
        element.send_keys("Магия")  # в поле ввода пишем любое слово

    button = browser.find_element_by_css_selector("button.btn")  # ищем кнопку отправить
    button.click()

finally:
    time.sleep(30)

    browser.quit()  # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла
