from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql

def naverNews():
    url = "http://www.naver.com"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
    naverService = driver.find_elements_by_css_selector("#PM_ID_serviceNavi li")
    naverService[1].click()
    
    neaverCategort = driver.find_elements_by_css_selector(".section.section_wide a")
    neaverCategort[-1].click()
    
    driver.find_element_by_css_selector(".ranking_section.othbor .btn_more").click()
    
    newsUrlLists(driver)
    
def newsUrlLists(driver):
    contentUrls = driver.find_elements_by_css_selector(".content div dt a")
    urlLists = []
    for no in range(len(contentUrls)):
        urlLists.append(contentUrls[no].get_attribute("href"))
    #print(len(urlLists))
    newsContent(driver,urlLists)
        
def newsContent(driver,urlLists):
    for url in urlLists:  
        driver.get(url)
        newsTitle = driver.find_element_by_css_selector(".font1.tts_head").text
        print("뉴스 제목 :",newsTitle)
        newsDate = driver.find_element_by_css_selector(".t11").text
        print("뉴스 날짜 :",newsDate)
        newsKind = driver.find_element_by_css_selector(".press_logo a img").get_attribute("title")
        print("뉴스 종류 :",newsKind)
        newsContent = driver.find_element_by_css_selector("#articleBodyContents").text
        print("뉴스 내용 :",newsContent)

        dbData = [[newsTitle,newsDate,newsKind,newsContent]]
        content = "newsContent"
        connectDB(dbData,content)
        
        
def connectDB(dbData,content):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()
    
    sql_01 = """insert into newscontent(newsTitle,newsDate,newsKind,newsContent)
         values (%s, %s, %s, %s)"""
   
    sql_02 = """insert into newscomment(commentId,commentContent,commentDate)
         values (%s, %s, %s)"""
    
    sql_03 = """insert into newsreply(replyID,replyContent,replyDate)
         values (%s, %s, %s)"""
    
    if content == "newsContent":
        curs.executemany(sql_01,dbData) 
    elif content == "newsComment":
        curs.executemany(sql_02,dbData) 
    elif content == "newsreply":
        curs.executemany(sql_03,dbData) 
        
    conn.commit()

    conn.close()
    
naverNews()






