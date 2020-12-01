from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome() 
driver.get('https://www.seleniumhq.org')

time.sleep(1)
element = driver.find_element_by_xpath('/html/body/section[2]/div/div[1]/div[2]/a/div')
element.click()

time.sleep(1)
driver.back()

time.sleep(1)
search_element = driver.find_element_by_id("gsc-i-id1")
search_element.send_keys("testing" + Keys.RETURN)

time.sleep(1)
driver.switch_to.frame('master-1')

link_elements = driver.find_element_by_tag_name('a')
print(link_elements.get_attribute('href'))

driver.close()