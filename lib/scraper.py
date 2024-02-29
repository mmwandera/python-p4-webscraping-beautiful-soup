from turtle import ht
from bs4 import BeautifulSoup
import requests

headers = {'user-agent': 'my-app/0.0.1'}
html = requests.get("https://moringaschool.com/courses/", headers=headers)

doc = BeautifulSoup(html.text, 'html.parser')
# print (doc.prettify())

print(doc.select('.page-title.leading-tight')[0].contents)
print(doc.select('.page-title.leading-tight')[0].name)
print(doc.select('.page-title.leading-tight')[0].attrs)