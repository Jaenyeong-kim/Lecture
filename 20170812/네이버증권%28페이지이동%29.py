from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql

def naver_finance():
    search = input("검색 : ")
    url = "http://finance.naver.com/sise/"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    time.sleep(1)

    Input= driver.find_element_by_id("stock_items")
    Input.send_keys(search)
    Input.send_keys(Keys.ENTER)

    time.sleep(2)
    search_info(driver)
    
def search_info(driver):
    contentLists = driver.find_elements_by_css_selector(".tbl_search tbody tr")
    for no in range(len(contentLists)):
        contents = contentLists[no].find_elements_by_css_selector("td")
        title = contents[0].text
        print("종목명 :", title)
        currentprice = contents[1].text
        print("현재가 :", currentprice)
        daybefore = contents[2].text
        print("전일대비 :",daybefore)
        changerate = contents[3].text
        print("등락율 :", changerate)
        sellprice = contents[4].text
        print("매도호가 :", sellprice)
        buyprice = contents[5].text
        print("매수호가 :",buyprice)
        volume = contents[6].text
        print("거래량 :",volume)
        transactionprice = contents[7].text
        print("거래대금 :",transactionprice)
        print("=============================================")

naver_finance()

