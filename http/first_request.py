import requests
url = "http://www.google.com"
res = requests.get(url)

print(f"your request to {url} came back w/ status code {res.status_code}")
# print(res.text) returns page source if request is not made to an api
# print(res.headers) returns header file of the response 

