
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import pymysql


def kyoboSearch():
    url = "https://www.kyobobook.co.kr/"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)

    kyoboMain = driver.find_elements_by_css_selector(".gnb_main.add_1 li") 
    kyoboMain[1].click()  
    
    time.sleep(1)
    kyoboMenu = driver.find_elements_by_css_selector(".section li")
    kyoboMenu2 = kyoboMenu[0].find_elements_by_css_selector("li")
    kyoboMenu2[0].click()
    
    time.sleep(1)
    kyoboCategory = driver.find_elements_by_css_selector(".path_bar.clear .location_zone.pathGroup")
    kyoboCategory[2].click()
    kyoboCategory_sub = driver.find_elements_by_css_selector(".list_zone.clear li a")
    kyoboCategory_sub[23].click()

    time.sleep(1)
    search = input("검색 : ")
    inputBox = driver.find_element_by_css_selector("#query")  
    inputBox.click()
    inputBox.send_keys(search)
    inputBox.send_keys(Keys.ENTER)
    
    driver.switch_to_window(driver.window_handles[1])
    time.sleep(1)
    pageNext(driver)

def kyoboInfo(driver):
    time.sleep(1)      
    productTitle = driver.find_elements_by_css_selector(".title.list-center a")
    productPrice = driver.find_elements_by_css_selector(".real")
    for no in range(len(productTitle)):
        title =  productTitle[no].text
        print("상품 명 :" , title)
        price = productPrice[no].text
        print("최저가 : " ,price)
        print("==================================================================")
        dbData = [[title,price]]
        #connectDB(dbData)
                        
def pageNext(driver):
    pageNo = driver.find_elements_by_css_selector(".pagingN02 a")
    while True:
        nextBtn = driver.find_elements_by_css_selector(".pagenation .rightNext02")
        if len(nextBtn) == 2:
            for no in range(len(pageNo)):
                pageNo = driver.find_elements_by_css_selector(".pagingN02 a")
                pageNo[no].click()
                time.sleep(1)
                kyoboInfo(driver)
            nextBtn = driver.find_elements_by_css_selector(".pagenation .rightNext02")
            nextBtn[0].click()
        else:
            if len(pageNo) == 0:
                kyoboInfo(driver)
            else:
                for no in range(len(pageNo)):
                    pageNo = driver.find_elements_by_css_selector(".pagingN02 a")
                    pageNo[no].click()
                    time.sleep(1)
                    kyoboInfo(driver)
            break
            
def connectDB(dbData):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'

    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                           db=DB_NAME, charset='utf8')

    curs = conn.cursor()

    sql = """insert into kyobomore(title,price)
         values (%s, %s)"""
    curs.executemany(sql ,dbData)

    conn.commit()

    conn.close()
    
kyoboSearch()   


