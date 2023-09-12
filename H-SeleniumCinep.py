from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.select import Select
import time
# from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=option)
driver.get("https://cinepolis.com/")
elementonombre = driver.find_element(By.NAME, 'ctl00$cmbCiudades')
drop = Select(elementonombre)
drop.select_by_visible_text("Chilpancingo")
nameplaces = driver.find_element(By.NAME, 'ctl00$cmbComplejos')
list = Select(nameplaces)
#Selección de sucursal
list.select_by_visible_text("Cinépolis Galerías Chilpancingo")
oopt = driver.find_element(By.ID,'cmbFechas')
drlistt = Select(oopt)
drlistt.select_by_visible_text("09 septiembre")
from_day=driver.find_element(By.XPATH,'//*[@id="43321-cinepolis-galerias-chilpancingo-shin-ultraman"]')
from_day.click()
time.sleep(8)
driver.close()
