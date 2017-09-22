from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def etnewsUrl(search):
    url = "http://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd={search}&pageNum=1&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=4%EC%B0%A8%EC%82%B0%EC%97%85%ED%98%81%EB%AA%85".format(search=search)    
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
search = input("검색 : ")
etnewsUrl(search)


