from selenium import webdriver
import time
import math
import os
try:
    link = " http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1=browser.find_element_by_xpath("/html/body/div[1]/form/div/input[1]").send_keys("Valera")
    input2=browser.find_element_by_xpath("/html/body/div[1]/form/div/input[2]").send_keys("Sanya")
    input3=browser.find_element_by_xpath("/html/body/div[1]/form/div/input[3]").send_keys("lyabomyr@gmail.com")

    #current_dir = os.path.abspath(os.path.dirname)  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(r"C:\Users\Любомир\PycharmProjects\pythonProject7", "Xiaomi_Redmi 5 Plus_sdk25_v4_0_new12_9_DB_w4_native_new_converter_reinit_plus_14_01_2021.txt")  # добавляем к этому пути имя файла
    #element.send_keys(file_path)

    input4=browser.find_element_by_xpath("/html/body/div[1]/form/input").send_keys(file_path)
    input5=browser.find_element_by_xpath("/html/body/div[1]/form/button").click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
