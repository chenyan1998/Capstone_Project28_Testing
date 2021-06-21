from selenium import webdriver
import time 

driver = webdriver.Chrome(executable_path= './drivers/chromedriver')
driver.get('http://localhost:8080/')
time.sleep(2)
driver.maximize_window()
time.sleep(2)

elem = driver.find_element_by_name("login")
elem.clear()
elem.send_keys("chenyan")
time.sleep(3)

elem = driver.find_element_by_name("password")
elem.clear()
elem.send_keys("chenyan password")
time.sleep(3)

button = driver.find_element_by_id("nav")
button.click()
time.sleep(2)

report_button =driver.find_element_by_class_name("el-icon-document") 
report_button.click()
time.sleep(2)

report_button =driver.find_element_by_class_name("el-icon-document") 
report_button.click()
time.sleep(2)

report_button =driver.find_element_by_class_name("el-icon-setting") 
report_button.click()
time.sleep(2)

report_button =driver.find_element_by_name("signout") 
report_button.click()


print("success")


