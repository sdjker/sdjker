from ast import Div
from bs4 import BeautifulSoup as bs
import requests

location = input('지역을 입력하세요: ')

url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query='+'%s'%location

print(url)

response = requests.get(url)

html_text = response.text

soup = bs(html_text, 'html.parser')

tp = soup.select_one('span.blind')

tempa_data = tp.get_text()
print('기온 : ', tempa_data)