from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def chosunnewsUrl(search):
    url = "http://search.chosun.com/search/total.search?query={search}&pageconf=total".format(search=search)
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
search = input("검색 : ")
chosunnewsUrl(search)


