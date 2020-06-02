from selenium import webdriver
import time

"""Заполняем форму"""

link = "http://suninjuly.github.io/simple_form_find_task.html"
browser = webdriver.Chrome()
browser.get(link)

try:
    input1 = browser.find_element_by_tag_name('div [name="first_name"]')
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_name('last_name')
    input2.send_keys("Ivanov")
    input3 = browser.find_element_by_class_name('form-control.city')
    input3.send_keys("Smolensk")
    input4 = browser.find_element_by_id('country')
    input4.send_keys("Russia")

    button = browser.find_element_by_xpath('//button[text()="Submit"]')
    button.click()

finally:
    time.sleep(4)

    browser.quit()      # закрываем браузер после всех манипуляций

# оставляем пустую строку в конце файла

