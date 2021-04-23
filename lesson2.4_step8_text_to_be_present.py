from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))
 
try: 
    browser = webdriver.Chrome()

    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    # говорим Selenium ждать пока цена не станет равна 100 $
    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"),"100")
        )
    
    #Нажать на кнопку "Book"    
    button = browser.find_element_by_id("book")
    button.click()
    
    # Считываем значение для переменной x
    x_element = browser.find_element_by_id("input_value")
    
    # записываем в переменную x текст из элемента x_element
    x = x_element.text
    
    # Считаем математическую функцию от x
    y = calc(x)
        
    # Ваш код, который заполняет обязательное поле
    input = browser.find_element_by_id("answer")
    input.send_keys(y)

    #Нажать на кнопку "Submit"    
    button = browser.find_element_by_id("solve")
    button.click()

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    
    