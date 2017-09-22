from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


def naverSearch():
    url = "https://www.naver.com/"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)

    naverService = driver.find_elements_by_css_selector("#PM_ID_serviceNavi li") 
    naverService[1].click()  

    time.sleep(1)
    naverCategory = driver.find_elements_by_css_selector("#lnb li") 
    naverCategory[5].click()       

    time.sleep(1)
    naverSub_ca = driver.find_elements_by_css_selector("#snb li")  
    naverSub_ca[9].click()   

    time.sleep(1)
#     search = input("검색 : ")
#     inputBox = driver.find_element_by_css_selector("#_inqueryInput")  
#     inputBox.send_keys(search)
#     inputBox.send_keys(Keys.ENTER)
    
    naverInfo(driver)

def naverInfo(driver):
    newsLists = driver.find_elements_by_css_selector(".list_body.newsflash_body  li") ##뉴스리스트 개수 확인
    for news in newsLists: ##뉴스 리스트의 개수만큼 for 문
        titles = news.find_elements_by_css_selector("dt") ###타이틀을 확인
        if len(titles) == 2: ###만약 타이틀이 2개일 경우;
            print("제목 :",titles[1].text)  #두번째 타이틀을 가져옴 ##첫 타이틀의 경우 null이거나 "동영상뉴스"라고 생김
            newsContent = news.find_elements_by_css_selector("dd")
            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
            print("등록일 :",newsDate[0].text)
            print("========================================================")
        else:   ##타이틀이 두개가 아닐 경우; 
            print("제목 :",titles[0].text)
            newsContent = news.find_elements_by_css_selector("dd")
            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
            print("등록일 :",newsDate[0].text)
            print("========================================================")


naverSearch()  


# In[ ]:





