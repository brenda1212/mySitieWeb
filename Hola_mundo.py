from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome(executable_path="C:\\Users\\sairaf\\Downloads\\Chomedriver\\chromedriver.exe")
driver.get("https://cinepolis.com/")

driver.close()

