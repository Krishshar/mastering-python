from selenium import webdriver

BASE_URL = 'https://unsplash.com/search/photos/'

search_term = input('Search Term: ')
browser = webdriver.Chrome()
browser.get(BASE_URL + search_term)
# resume_btn = browser.find_elements_by_link_text("Download")
# print(resume_btn)