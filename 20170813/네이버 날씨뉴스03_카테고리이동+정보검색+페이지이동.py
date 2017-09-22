
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
    
    searchPages(driver)

def naverInfo(driver):
    newsLists = driver.find_elements_by_css_selector(".list_body.newsflash_body  li")
    for news in newsLists:
        titles = news.find_elements_by_css_selector("dt")
        if len(titles) == 2:
            print("제목 :",titles[1].text)
            newsContent = news.find_elements_by_css_selector("dd")
            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
            print("등록일 :",newsDate[0].text)
            print("========================================================")
        else:
            print("제목 :",titles[0].text)
            newsContent = news.find_elements_by_css_selector("dd")
            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
            print("등록일 :",newsDate[0].text)
            print("========================================================")

def searchPages(driver):        
    naverInfo(driver)           
    while True:
        pageNo = driver.find_elements_by_css_selector("#main_content .paging a")  ##페이지번호가 있는...
        nextBtn = driver.find_elements_by_css_selector("#main_content .paging .next") ##다음으로 넘어가는 페이지
        if nextBtn != []: ###
            for no in range(len(pageNo)):
                pageNo = driver.find_elements_by_css_selector("#main_content .paging a")
                pageNo[no].click()
                time.sleep(1)
                naverInfo(driver)
        else:
            for no in range(len(pageNo)):   ##(1, len(pageNo)) 가능
                pageNo = driver.find_elements_by_css_selector("#main_content .paging a")
                pageNo[no].click()
                time.sleep(1)
                naverInfo(driver)
            break


naverSearch()  


# In[ ]:





