from selenium import webdriver
import time
import math
from selenium.webdriver.support.ui import Select

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)
    a=browser.find_element_by_id("num1").text
    b=browser.find_element_by_id("num2").text
    x=int(a)+int(b)
    x=str(x)
    print(a,b,x)
    #answer=browser.find_element_by_xpath()
    select = Select(browser.find_element_by_id("dropdown"))
    print("find dropdown")
    select.select_by_visible_text(x)

    submit=browser.find_element_by_xpath("/html/body/div[1]/form/button").click()

finally:
    time.sleep(10)
    browser.quit()