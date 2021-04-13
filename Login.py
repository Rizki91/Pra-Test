from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

try:
	driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
	driver.get("https://accounts.bukalapak.com/register")
	a = driver.find_element(By.CLASS_NAME,"bl-link")
	a.click()
	a = driver.find_element(By.NAME,"user_session[username]")
	a.send_keys("fahmi.fathi2002@gmail.com")
	a = driver.find_element(By.ID,"user_session_password")
	a.send_keys("test123456")
	a = driver.find_element(By.NAME,"commit") 
	a.click()



	
	e = driver.find_element(By.CLASS_NAME,"bl-text-field__input")
	e.send_keys("fahrulrizki991@gmail.com")
	e = driver.find_element(By.CLASS_NAME,"bl-button--block") 
	e.click()
	f = driver.find_element(By.CLASS_NAME,"mb-8")
	f.click()
	g = driver.find_element(By.CLASS_NAME,"bl-text-field__input")
	g.send_keys("")
	g = driver.find_element(By.CLASS_NAME,"bl-button")
	g.click()
	driver = webdriver.Firefox(executable_path=r'C:\geckodriver.exe')
	driver.get("https://accounts.bukalapak.com/login")
	
finally:
	print("selesai")