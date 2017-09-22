import requests
from bs4 import BeautifulSoup
import pymysql
        
def 동아일보(search):
    for pageNo in range(1,16,15):
        url = "http://news.donga.com/search?p={pageNo}&query={search}&check_news=1&more=1&sorting=1&search_date=1&v1=&v2=&range=1".format(search=search,pageNo=pageNo)
        req = requests.get(url)
        reqBs = BeautifulSoup(req.content,"html.parser")
        urlLists = reqBs.select(".searchList .tit")
        for no in range(len(urlLists)):
            url = urlLists[no].find("a")['href']
            req_url = requests.get(url)
            reqBs_url = BeautifulSoup(req_url.content,"html.parser")
    
            newsDate = reqBs_url.select(".article_title .date01")
            resultDate = newsDate[0].text.replace("입력 ","").replace("-","/")
            title = reqBs_url.select(".article_title .title")
            resultTitle = title[0].text
            subtitle = ""
            content = reqBs_url.select(".article_txt")
            content_Text = content[0].text
            text_endPoint = content_Text.find("추천해요")
            result_content_text = content_Text[:text_endPoint]
            print("url :",url)
            print("date :",resultDate)
    #        print("제목 :",resultTitle)
    #        print("본문 :",result_content_text)
            print("====================")
    
            dbData = [[url,resultDate,resultTitle,subtitle, result_content_text]]
            connectDB(dbData)
def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into news(url, newsDate, newsTitle, newsSubtitle, content)
         values (%s, %s, %s, %s, %s)"""
    curs.executemany(sql,dbData)
    
    conn.commit()

    conn.close()

#search=""
#동아일보(search)
            

