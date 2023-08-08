from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
driver = webdriver.Chrome(executable_path="C:\\Users\\sairaf\\Downloads\\Chomedriver\\chromedriver.exe")
driver.get("https://cinepolis.com/")

elemento_por_nombre = driver.find_element(By.NAME, "ctl00$cmbCiudades")

print(elemento_por_nombre.text)


driver.close()
