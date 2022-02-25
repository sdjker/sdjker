from urllib import request
from bs4 import BeautifulSoup as bs
import requests


url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EB%B2%A0%EC%9D%B4%EC%A7%95%EC%98%AC%EB%A6%BC%ED%94%BD'
response = requests.get(url)
html_text = response.text

soup = bs(html_text, 'html.parser')

a_tags = soup.select('a.news_tit')

for a in a_tags:
  title = a.get_text()
  link  = a.attrs['href']
  print(title, '링크:', link)