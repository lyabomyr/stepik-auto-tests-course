import  time
from selenium import  webdriver
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import text_to_be_present_in_element
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
link="http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()
browser.get(link)
wait = WebDriverWait(browser, 12)
try:
    #button = WebDriverWait(browser, 5).until(EC.element_to_be_clickable((By.ID, "verify"))# говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
    #browser.implicitly_wait(5) # говорим WebDriver искать каждый элемент в течение 5 секунд
    #button = WebDriverWait(browser, 5).until_not(EC.element_to_be_clickable((By.ID, "verify"))# говорим Selenium проверять в течение 5 секунд пока кнопка станет неактивной

    element=wait.until(EC.text_to_be_present_in_element((By.ID, "price"), "$100")) #нажать, если значение будет равно "100"
    browser.implicitly_wait(1)
    button23= browser.find_element_by_id("book").click()
    #new_window = browser.window_handles[1] # это второе окно  браузерк(есть код для того чтобы узнать имя окна)
    #browser.switch_to.window(new_window) # чтобы перейти нужно укаать конкретное окно
    #confirm = browser.switch_to.alert
    #confirm.accept()

    x=browser.find_element_by_id("input_value").text
    result= (math.log (abs (12 * math.sin (float(x)))))
    result_input=browser.find_element_by_xpath("/html/body/form/div/div/div/input").send_keys(str(result))
    button2=browser.find_element_by_xpath("/html/body/form/div/div/button").click()
finally:
    time.sleep(5)
    browser.quit()


