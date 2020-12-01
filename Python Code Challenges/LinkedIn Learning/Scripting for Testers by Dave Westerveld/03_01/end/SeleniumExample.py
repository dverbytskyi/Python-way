from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome()
driver = webdriver.Firefox()

driver.get('https://google.com')

element = driver.find_element_by_name('q')
element.send_keys("test")
element.send_keys(Keys.RETURN)
