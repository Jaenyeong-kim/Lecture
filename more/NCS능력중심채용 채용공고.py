import pandas as pd
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen
from selenium import webdriver
import pprint
import requests
from selenium.webdriver.common.keys import Keys
import time
import pymysql


def NCS_Search():
    url = "http://www.ncs.go.kr/onspec/recrtinfo/selectPuborgRecrtinfoList.do"
    driver = webdriver.Chrome("./chromedriver.exe") 
    driver.get(url) 
    time.sleep(1)

    search = "채용"
    inputncs= driver.find_element_by_id("searchKeyword")
    inputncs.send_keys(search)
    inputncs.send_keys(Keys.ENTER)

    NCSMove(driver)

def NCS_Info(driver):

    timetableLists = driver.find_elements_by_css_selector("#content .board_list tr")

    for no in range(1,len(timetableLists)):
        contentstd = timetableLists[no].find_elements_by_css_selector("td") 
        contentsth = timetableLists[no].find_elements_by_css_selector("th")
        contentsimg = timetableLists[no].find_elements_by_css_selector("img")
        #가로줄을 f12로 보게되면 "제목, 기관명, 조회수, 마감일" 은 td로 되어있으며
        # "번호" 는 th 로 되어있고 "진행상태" 같은 경우에는 img로 되어있기 때문에

        # css_selector 로 "td" "th" "img" 로 나눠서 적어주면 적힌다.
        
        
        numbers = contentsth[0].text   
        print("번호 :", numbers)     
        
        indexs = contentstd[0].text
        print("제목 :",indexs)
        
        projects = contentsimg[0].get_attribute("alt")
        print("진행상태 :",projects) 
        
        names = contentstd[2].text
        print("기관명 :",names)
        
        clicks = contentstd[3].text
        print("조회수 :",clicks)
        
        finishs = contentstd[4].text
        print("마감일 :",finishs)
        print("=============================================")

def NCSMove(driver):  

    NCS_Info(driver)

    while True:
        pageLen = driver.find_elements_by_css_selector(".paging a")  
        nextBtn = driver.find_elements_by_css_selector(".paging btn_page")
        pageLen[len(pageLen)-2].get_attribute("href")  

        for no in range(2,len(pageLen)-2): 
            pageBtn = driver.find_elements_by_css_selector(".paging a")
            pageBtn[no].click()
            time.sleep(2)
            print("다음페이지")

            NCS_Info(driver)

        if isinstance(nextBtn,str): 
            pageBtn = driver.find_elements_by_css_selector(".paging a")
            pageBtn[len(pageLen)-2].click()
        else:                    
            print("마지막 페이지")
            break

NCS_Search()  

