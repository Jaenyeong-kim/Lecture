from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# 뉴스검색 함수
def 뉴스검색(search):
    url = "http://search.khan.co.kr/search.html?stb=khan&q={search}&pg=1&sort=1".format(search=search)
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)

    뉴스리스트보기(driver)

# 뉴스리스트 보여주는 화면
def 뉴스리스트보기(driver):
    뉴스URL들 = driver.find_elements_by_css_selector(".news .phArtc dt a")
    for 뉴스URL in 뉴스URL들:
        print("Url은 ",뉴스URL.get_attribute("href"))
#        print("Url :",urlList.get_text())
 
   
#검색어 = input("검색 : ")
검색어 = "태양광"
뉴스검색(검색어)

