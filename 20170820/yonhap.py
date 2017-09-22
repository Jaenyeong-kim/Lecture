
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymysql


def 연합뉴스(search):
    url = "http://www.yonhapnews.co.kr/home09/7091000000.html?query={search}&ctype=A".format(search=search)
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
    yonhapnewsUrlList(driver)

def yonhapnewsUrlList(driver):
    url2 = driver.current_url
    yonhapnewsUrs_List = []
    for pageNo in range(1,2): #2페이지까지
        url = url2 + "&page_no={pageNo}".format(pageNo=pageNo)
        driver.get(url)
        
        yonhapnewsUrs= driver.find_elements_by_css_selector(".cts_atclst li a")
    
        for urlList in yonhapnewsUrs:
            yonhapnewsUrs_List.append(urlList.get_attribute("href"))
    yonhapnewsInfo(driver,yonhapnewsUrs_List)

def yonhapnewsInfo(driver,yonhapnewsUrs_List):
    for urlList in yonhapnewsUrs_List:
        driver.get(urlList)
        newsDate = driver.find_element_by_css_selector(".share-info .tt em").text
        newsTitle = driver.find_element_by_css_selector(".tit-article").text
        newsSubtitles = driver.find_elements_by_css_selector(".stit strong")
        newSubtitle_result = ""
        for newsSubtitle in newsSubtitles:
            newSubtitle_result+=newsSubtitle.text
        newsContents = driver.find_elements_by_css_selector(".article p")
        newsDate = driver.find_element_by_css_selector(".share-info .tt em").text
        print("- url - : \n",urlList)
        print("- 날짜 - : \n",newsDate)        
        print("- 기사 제목 - : \n",newsTitle)
        print("- 기사 부제목 - \n:",newSubtitle_result)
#        print("- 기사 본문 - \n")
        content_result = ""
        for content in newsContents:
            content_result+=content.text
#        print(content_result)
            
        dbData = [[urlList,newsDate,newsTitle,newSubtitle_result,content_result]]
        connectDB(dbData)
        
def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into news(url,newsDate, newsTitle,newsSubtitle,content)
         values (%s, %s, %s, %s, %s)"""
    curs.executemany(sql,dbData)
    
    conn.commit()

    conn.close()
    
#search = input("검색 : ")
#yonhapnewsUrl(search)


