import requests
from bs4 import BeautifulSoup
import re
import pymysql

def joins_search():
    search = "문재인"
    url = "http://search.joins.com/TotalNews?Keyword={search}&SortType=New&SourceGroupType=Joongang&SearchCategoryType=TotalNews".format(search=search)
    urls = []
    for page in range(1,3):
        urlAddPage = url + "&page=" + str(page)
        req_getUrl = requests.get(urlAddPage)
        req_bs = BeautifulSoup(req_getUrl.content,"html.parser")
        urlsLists = req_bs.select(".headline.mg")
        for no in range(len(urlsLists)):
            urls.append(urlsLists[no].select_one("a").attrs.get("href"))
    return joins_newsInfo(urls)

def joins_newsInfo(urls):
    for url_add in urls:
        req_getUrl_add = requests.get(url_add)
        req_bs_add = BeautifulSoup(req_getUrl_add.content,"html.parser")
        newsTitle = req_bs_add.select_one("#article_title").text
        re_compile = re.compile("\d\d\d\d\.\d\d\.\d\d")
        dateText = req_bs_add.select(".byline em")[1].text
        result_date = re_compile.findall(dateText)
        content = req_bs_add.select_one("#article_body").text
        print("  --  제목  -- \n",newsTitle)
        print("  --  등록일  -- \n",dateText)
        print("  --  본문  -- \n",content)
#        dbData = [[newsTitle,result_date[0],content]]
#        connectDB(dbData)
        
def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')         

    curs = conn.cursor()

    sql = """insert into joinsnews(title,date,content)  
         values (%s, %s, %s)"""         

    curs.executemany(sql,dbData)    
    conn.commit()

    conn.close()
    
joins_search()





