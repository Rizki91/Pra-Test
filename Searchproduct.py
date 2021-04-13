from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
	driver.get("https://bukalapak.com")
	b = driver.find_element(By.ID,"home")
	b = driver.find_element(By.ID,"v-omnisearch__input")
	b.send_keys("xiomi redmi")
	b = driver.find_element(By.CLASS_NAME,"v-omnisearch__submit") 
	b.click()
	
finally:
	print("selesai")