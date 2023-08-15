from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
import time
driver = webdriver.Chrome(executable_path="C:\\Users\\sairaf\\Downloads\\Chomedriver\\chromedriver.exe")
driver.get("https://cinepolis.com/")
elementonombre=driver.find_element(By.NAME, 'ctl00$cmbCiudades')
drop=Select(elementonombre)

drop.select_by_visible_text("Chilpancingo")

nameplaces=driver.find_element(By.NAME,'ctl00$cmbComplejos')
list=Select(nameplaces)
list.select_by_visible_text("Cinépolis Galerías Chilpancingo")
time.sleep(4)


driver.close()



