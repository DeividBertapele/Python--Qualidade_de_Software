from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Chrome()

driver.get("https://www.google.com.br/")

print(driver.current_url)
print(driver.title)
print(driver.capabilities['browserVersion'])


element = driver.find_element(By.NAME,"q")
element.click()
element.send_keys("Python")
element.submit()

assert driver.title == "Python - Pesquisa Google"

driver.close()