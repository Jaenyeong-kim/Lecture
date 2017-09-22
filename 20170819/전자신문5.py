from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pymysql

def etnewsUrl(search):
    url = "http://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd={search}&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=4%EC%B0%A8%EC%82%B0%EC%97%85%ED%98%81%EB%AA%85".format(search=search)    
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
    return etnewsUrlList(driver)

def etnewsUrlList(driver):
    url2 = driver.current_url
    etnewsUrs_List = []
    for pageNo in range(1,3): #2페이지까지
        url = url2 + "&pageNum={pageNo}".format(pageNo=pageNo)
        driver.get(url)
        
        etnewsUrs= driver.find_elements_by_css_selector(".list_news .clearfix dt a")
    
        for urlList in etnewsUrs:
            etnewsUrs_List.append(urlList.get_attribute("href"))
    return etnewsInfo(driver,etnewsUrs_List)

def etnewsInfo(driver,etnewsUrs_List):
    for urlList in etnewsUrs_List:
        driver.get(urlList)
        newsTitle = driver.find_element_by_css_selector(".article_title").text
        newsSubtitles = driver.find_elements_by_css_selector("#articleBody h3")
        newSubtitle_result = ""
        for newsSubtitle in newsSubtitles:
            newSubtitle_result+=newsSubtitle.text
        newsContents = driver.find_elements_by_css_selector("#articleBody p")
        print("- 기사 제목 - : \n",newsTitle)
        print("- 기사 부제목 - \n:",newSubtitle_result)
        print("- 기사 본문 - \n")
        content_result = ""
        for content in newsContents:
            content_result+=content.text
        print(content_result)
            
        dbData = [[newsTitle,newSubtitle_result,content_result]]
        connectDB(dbData)
        
def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into etnews(newsTitle,newSubtitle_result,content)
         values (%s, %s, %s)"""
    curs.executemany(sql,dbData)
    
    conn.commit()

    conn.close()

search = "4차산업혁명"
#search = input("검색 : ")
etnewsUrl(search)




