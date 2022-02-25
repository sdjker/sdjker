from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup as bs
import pandas as pd
import time

driver = webdriver.Chrome()

url = 'https://scholar.google.com/'
driver.get(url)
time.sleep(2)

search_box = driver.find_element(By.CSS_SELECTOR, '#gs_hdr_tsi')
search_box.send_keys('Deep learning construction industry')
search_box.send_keys(Keys.RETURN)
time.sleep(2)   

quote = driver.find_element(By.CSS_SELECTOR, "#gs_res_ccl_mid > div:nth-child(1) > div.gs_ri > div.gs_fl > a.gs_or_cit.gs_or_btn.gs_nph > span")
quote.click()
time.sleep(2)

soup = bs(quote, 'html.parser')

suge_data = soup.select('div.gs_citr')

for suge_text in suge_data:
    suge_text = suge_data.get_attribute("innerHTML")
    print(suge_text)

