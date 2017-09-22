# coding: utf-8

import pandas as pd
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import pprint
import requests
from selenium.webdriver.common.keys import Keys
import time

URL = 'http://www.11st.co.kr'

def st(URL,keyword):
    driver = webdriver.Chrome("./chromedriver")
    driver.get(URL)
    inputNews= driver.find_element_by_id("AKCKwd")
#    keyword = input("검색: ")
    inputNews.send_keys(keyword)
    inputNews.send_keys(Keys.ENTER)

keyword = input("검색: ")
st(URL,keyword)

    

