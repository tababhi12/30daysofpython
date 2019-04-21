import os
import requests
from selenium import webdriver
from bs4 import BeautifulSoup
filepath = os.path.dirname(__file__) + '/chromedriver_win32/chromedriver.exe'
print(filepath)

url = 'https://www.google.com/search?q=avengers&safe=active&source=lnms&tbm=isch&sa=X&ved=0ahUKEwilgYXLgN_hAhWf6nMBHTKYB8EQ_AUIDygC&biw=1920&bih=975'

web_r = requests.get(url)
print(web_r.status_code)
soup = BeautifulSoup(web_r.text,'html.parser')
print(len(soup.findAll('img')))

driver = webdriver.Chrome(filepath)
driver.get(url)
html = driver.execute_script("return document.documentElement.outerHTML")
sel_soup = BeautifulSoup(html,'html.parser')
print(len(sel_soup.findAll('img')))

images = []
for i in sel_soup.findAll('img'):
    print(i)
    src = i['src']
    images.append(src)
print(images)