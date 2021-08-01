from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get('http://127.0.0.1:8000/')
assert "Welcome, You Are Not Logged In" in driver.page_source
time.sleep(2)

print("OK")


driver.quit()