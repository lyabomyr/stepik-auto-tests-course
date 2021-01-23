import  time
from selenium import  webdriver
import math

link="http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()
browser.get(link)
try:
    button1=browser.find_element_by_xpath("/html/body/form/div/div/button").click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    x=browser.find_element_by_id("input_value").text
    result= (math.log (abs (12 * math.sin (float(x)))))
    result_input=browser.find_element_by_xpath("/html/body/form/div/div/div/input").send_keys(str(result))
    button2=browser.find_element_by_xpath("/html/body/form/div/div/button").click()
finally:
    time.sleep(5)
    browser.quit()


