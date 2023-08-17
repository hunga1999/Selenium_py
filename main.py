from selenium import webdriver
from selenium.webdriver.common.by import By

# Khởi tạo trình duyệt
driver = webdriver.Edge()

# Mở một trang web
driver.get("file:///C:/Users/HUNGA-PC/Desktop/Selenium_py/index.html")

# Tìm phần tử theo tên lớp và thực hiện click
element = driver.find_element(By.ID, "username")
element.send_keys('admin')

element2 = driver.find_element(By.ID,"password")
element2.send_keys('admin')

element3 = driver.find_element(By.TAG_NAME,"button")
if element3.text == 'Đăng nhập':
    element3.click()

element4 = driver.find_element(By.ID, "loginResult")
if element4.text == 'Đăng nhập thành công!':
    print("ok")
else:
    print("Element is not visible.")

# Đóng trình duyệt
driver.quit()