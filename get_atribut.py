
3from selenium import webdriver
import time
import math

try:
    link = " http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)
    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_element = browser.find_element_by_id("treasure")

    x = x_element.get_attribute("valuex")
    y = calc(x)

    text1 = browser.find_element_by_id("answer").send_keys(y)
    print(y)

    text2 = browser.find_element_by_id("robotCheckbox").click()
    text3=browser.find_element_by_id("robotsRule").click()
    text4=browser.find_element_by_xpath('/html/body/div/form/div/div/button').click()
finally:
    time.sleep(10)
    browser.quit()

