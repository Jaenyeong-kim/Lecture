from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
def yonhapnewsUrl(search):
    url = "http://search.khan.co.kr/search.html?q={serach}".format(search=search)
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)   
 
    return yonhapnewsUrlList(driver)
 
def yonhapnewsUrlList(driver):
    yonhapnewsUrs= driver.find_elements_by_css_selector(".news section .phArtc dt a")
    for urlList in yonhapnewsUrs:
        print("Url :",urlList.get_attribute("href"))
       
search = input("검색 : ")
yonhapnewsUrl(search)
