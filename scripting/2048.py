from selenium import webdriver
from selenium.webdriver.common.keys import Keys

BASE_URL = 'https://gabrielecirulli.github.io/2048/'

driver = webdriver.Chrome()
driver.get(BASE_URL)
html = driver.find_element_by_tag_name('html')
while True:
	html.send_keys(Keys.UP)
	html.send_keys(Keys.RIGHT)
	html.send_keys(Keys.DOWN)
	html.send_keys(Keys.LEFT)