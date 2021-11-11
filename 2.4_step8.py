from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


try:
    browser = webdriver.Chrome(ChromeDriverManager().install())

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.find_element_by_id
    WebDriverWait(browser, 15).until(EC.text_to_be_present_in_element((By.ID, "price"), "100"))
    browser.find_element_by_id("book").click()
    elem1 = browser.find_element_by_xpath('//*[@*="input_value"]')
    x = elem1.text
    y = calc(x)
    browser.find_element_by_xpath('//*[@type="text"]').send_keys(y)
    browser.find_element_by_xpath('//*[@type="submit"]').click()

finally:
    browser.close()
