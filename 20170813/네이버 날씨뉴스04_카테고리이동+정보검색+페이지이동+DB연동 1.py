from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql


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

    searchPages(driver) #36

def naverInfo(driver):
    time.sleep(2)
    newsLists = driver.find_elements_by_css_selector(".list_body.newsflash_body  li")
    for news in newsLists:
        titles = news.find_elements_by_css_selector("dt")
        if len(titles) == 2:
#            print("제목 :",titles[1].text)
            newsContent = news.find_elements_by_css_selector("dd")
#            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
#            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
#            print("등록일 :",newsDate[0].text)
#            print("========================================================")
            dbData = [[titles[1].text, newsContent[0].text, newsProducer[0].text, newsDate[0].text]]
            connectDB(dbData) ## if 문이라서 각각 DB연동
        else:
#            print("제목 :",titles[0].text)
            newsContent = news.find_elements_by_css_selector("dd")
#            print("기사 내용:",newsContent[0].text)
            newsProducer =  news.find_elements_by_css_selector("dd .writing")
#            print("제작사 :",newsProducer[0].text)
            newsDate = news.find_elements_by_css_selector("dd .date")
#            print("등록일 :",newsDate[0].text)
#            print("========================================================")
            dbData = [[titles[0].text, newsContent[0].text, newsProducer[0].text, newsDate[0].text]]
            connectDB(dbData) ## if 문이라서 각각 DB연동

           # dbData = [[titles, newsContent, newsProducer, newsDate]] 한번에 안됨
           # connectDB(dbData)

def searchPages(driver):        
    naverInfo(driver)           
    while True:
        pageNo = driver.find_elements_by_css_selector("#main_content .paging a")  ##페이지번호가 있는...
        print("pageNo : ", len(pageNo))
        nextBtn = driver.find_elements_by_css_selector("#main_content .paging .next") ##다음으로 넘어가는 페이지
        print("nextBtn : ", len(nextBtn))

        if nextBtn != []: ###
            for no in range(len(pageNo)):
                pageNo = driver.find_elements_by_css_selector("#main_content .paging a")
                print("if nextBtn != [] pageNo : ", len(pageNo))
                pageNo[no].click()
                time.sleep(1)
                naverInfo(driver)
        else:
            for no in range(len(pageNo)):   ##(1, len(pageNo)) 가능
                pageNo = driver.find_elements_by_css_selector("#main_content .paging a")
                print("if nextBtn != [] else: pageNo : ", len(pageNo))

                pageNo[no].click()
                time.sleep(1)
                naverInfo(driver)
            break



def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into naverweather(title, content, producer, date)
         values (%s, %s, %s, %s)"""
    curs.executemany(sql,dbData)
    
    conn.commit()

    conn.close()



naverSearch()  




