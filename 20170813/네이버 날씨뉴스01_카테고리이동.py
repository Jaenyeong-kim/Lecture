from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

url = "https://www.naver.com/"
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)

naverService = driver.find_elements_by_css_selector("#PM_ID_serviceNavi li") 
naverService[1].click()  ###메인카테고리 중 뉴스 이동
time.sleep(1)

naverCategory = driver.find_elements_by_css_selector("#lnb li") 
naverCategory[5].click()   ###뉴스카테고리 중 생활/문화 이동    
time.sleep(1)

naverSub_ca = driver.find_elements_by_css_selector("#snb li")  
naverSub_ca[9].click()   ###생활/문화 카테고리 중 날씨 이동
time.sleep(1)

   
#     search = input("검색 : ")
#     inputBox = driver.find_element_by_css_selector("#_inqueryInput")  
#     inputBox.send_keys(search)
#     inputBox.send_keys(Keys.ENTER)
    





