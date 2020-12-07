from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

url = 'http://automationpractice.com/index.php?id_category=3&controller=category'
driver.get(url)

product_containers = driver.find_elements_by_class_name('product-container')

for index, product in enumerate(product_containers):
    hover = ActionChains(driver).move_to_element(product)
    hover.perform()
    driver.find_element_by_xpath('//*[@id="center_column"]/ul/li[%s]/div/div[2]/div[2]/a[1]/span' % (index+1)).click()
    time.sleep(1)
    element = WebDriverWait(driver, 2)

    driver.find_element_by_xpath('//*[@id="layer_cart"]/div[1]/div[2]/div[4]/span').click()
    time.sleep(1)
