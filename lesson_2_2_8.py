from selenium import webdriver
import time
import os
"""Загрузка файла"""
"""Задачка:
1.Открыть страницу 
2.Заполнить текстовые поля: имя, фамилия, email
3.Загрузить файл. Файл должен иметь расширение .txt и может быть пустым
4.Нажать кнопку "Submit"."""

browser = webdriver.Chrome()
browser.get('http://suninjuly.github.io/file_input.html')

try:
    input1 = browser.find_element_by_name('firstname')
    input1.send_keys('Tanya')
    input2 = browser.find_element_by_name('lastname')
    input2.send_keys('Ivanova')
    input3 = browser.find_element_by_name('email')
    input3.send_keys('desroom@mail.ru')

    with open('file.txt', 'tw', encoding='utf-8') as f:    # создаем файл автоматически
        pass                    # пропуск, пустой файл ничего не записываем

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'file.txt')  # добавляем к этому пути имя файла
    button1 = browser.find_element_by_id('file')  # создаем переменную на кнопку Выбрать файл
    button1.send_keys(file_path)     # в поля ввода вставляем наше значение

    button = browser.find_element_by_tag_name('div [type="submit"]')
    button.click()
    os.remove(file_path)    # созданный нами файл удаляется автоматически

finally:
    time.sleep(5)

    browser.quit()    # закрываем браузер после всех манипуляций

# не забываем оставить пустую строку в конце файла



