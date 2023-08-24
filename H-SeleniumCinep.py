from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver.get("https://cinepolis.com/")
elementonombre=driver.find_element(By.NAME,'ctl00$cmbCiudades')
drop=Select(elementonombre)
drop.select_by_visible_text("Chilpancingo")
nameplaces=driver.find_element(By.NAME,'ctl00$cmbComplejos')
list=Select(nameplaces)
list.select_by_visible_text("Cinépolis Galerías Chilpancingo")
opselect=driver.find_element(By.ID,'cmbFechas')
drlistt=Select(opselect)
drlistt.select_by_visible_text("25 agosto")
time.sleep(4)
driver.close()

