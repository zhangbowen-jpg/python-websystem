# -*- coding: utf-8 -*-
from selenium import webdriver
from urllib import request
import time
from lxml import html
from lsql.models import Operator
from bs4 import BeautifulSoup as BS

# chrome_options = Options()
# chrome_options.add_argument('--headless')



headers = {
     'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36'
 }


driver = webdriver.Chrome(executable_path = 'chromedriver.exe')  #声明谷歌浏览器对象
first_url = 'http://ak.mooncell.wiki/w/%E5%B9%B2%E5%91%98%E4%B8%80%E8%A7%88'  #入口url
driver.get(first_url)
driver.maximize_window()


height = 0
for i in range(1,13):
    js = 'var q=document.documentElement.scrollTop=%s' % height
    height += 800
    driver.execute_script(js)
    time.sleep(1)
soup=BS(driver.page_source,'html.parser')
results = soup.find_all('tr',class_='result-row')
for i in results:
    j = 0
    print('*'*100)
    content = html.etree.HTML(i)
    id = j
    name = content.find_element_by_xpath('./td[1]')
    place = content.find_element_by_xpath('./td[2]')
    health = content.find_element_by_xpath('./td[3]')
    attack = content.find_element_by_xpath('./td[4]')
    defined = content.find_element_by_xpath('./td[5]')
    magic = content.find_element_by_xpath('./td[6]')
    a_time = content.find_element_by_xpath('./td[7]')
    s_cost = content.find_element_by_xpath('./td[8]')
    blocked = content.find_element_by_xpath('./td[9]')
    between = content.find_element_by_xpath('./td[10]')

