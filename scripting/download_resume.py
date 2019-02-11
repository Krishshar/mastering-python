from selenium import webdriver
browser = webdriver.Chrome()

browser.get('https://www.jysh.me')
resume_btn = browser.find_element_by_link_text("RESUME.")
resume_btn.click()