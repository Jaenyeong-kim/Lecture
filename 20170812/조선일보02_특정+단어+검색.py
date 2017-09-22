from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
def chosunnewsUrl(search):
    url = "http://search.chosun.com/search/total.search?query={serach}&pageconf=total".format(search=search)
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)   
 
    return chosunnewsUrlList(driver)
 
def chosunnewsUrlList(driver):
    chosunnewsUrs= driver.find_elements_by_css_selector(".search_news dt a")
    for urlList in chosunnewsUrs:
        print("Url :",urlList.get_attribute("href"))
       
search = input("검색 : ")
chosunnewsUrl(search)
