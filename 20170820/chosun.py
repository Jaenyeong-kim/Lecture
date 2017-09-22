import pymysql
import requests
from bs4 import BeautifulSoup

urlLists = []

def 조선일보(search):
    URL = "http://search.chosun.com/search/news.search?query={search}&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=조선일보&categoryd2=&c_scope=navi&sdate=&edate=&premium=".format(search=search) 
    for page in range(1,51):
        urlAddPage = URL + "&pageno=" + str(page)
        html = requests.get(urlAddPage) 
        bs = BeautifulSoup(html.content,"html.parser")  
        chosun = bs.select(".search_news dt ")  
        for name in chosun :     
            urlLists.append(name.select_one("a").attrs.get("href"))
            
    return chosunLinks(urlLists)
        
def chosunLinks(urlLists):
    for urlList in urlLists:
        html_news = requests.get(urlList)  
        bs_news = BeautifulSoup(html_news.content,"html.parser")

        newsDate = bs_news.select_one(".date_ctrl_2011 #date_text").text.replace("입력 : ", "").replace(".", "/")

        print("- url - : \n",urlList)
        print("- 날짜 - : \n",newsDate)        

        title = bs_news.select_one(".news_title_text #news_title_text_id").text
        print("- 제목 - \n",title)
        subtitle = bs_news.select_one("#news_body_id .news_subtitle").text
        print("- 부제목 - \n",subtitle)

        pars = len(bs_news.select("#news_body_id .par")[:]) 
        content = ""
        for i in range(pars) :  
            content+= bs_news.select("#news_body_id .par")[i].text
        print("- 본문 - \n",content)

        dbData = [[urlList,newsDate, title,subtitle,content]]
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
#chosun(search)






