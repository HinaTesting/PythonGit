from typing import List, Any

import openpyxl
from selenium.webdriver.chrome import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium import webdriver



book= openpyxl.load_workbook("C:\\Users\\hinan\\Desktop\\Rahul shetty academy python selenium\\PythonDemo.xlsx")
sheet=book.active
Dict = {}

fruitName="Apple"
service_obj = Service("C:/Users/hinan/Desktop/Rahul shetty academy python selenium/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
#1. download file
driver.find_element(By.ID,"downloadButton").click()
#2. edit file with updated file

#3. upload file
file_input=driver.find_element(By.ID,"fileinput")
file_input.send_keys("C:/Users/hinan/Downloads/download.xlsx")
wait=WebDriverWait(driver,10)
driver.get_screenshot_as_file("screen_shot.png")
wait.until(expected_conditions.presence_of_element_located((By.CLASS_NAME,"Toastify__toast-icon")))
driver.get_screenshot_as_file("test1.png")
#//div[text()='Apple']/parent::div/parent::div/div[@id="cell-4-undefined"]
priceColumn = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")

Actual_price=driver.find_element(By.XPATH,"//div[text()='"+fruitName+"']/parent::div/parent::div/div[@id='cell-4-undefined']").text
print(Actual_price)