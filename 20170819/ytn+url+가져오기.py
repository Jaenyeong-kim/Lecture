from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def ytnConnect():
    url = "http://www.ytn.co.kr/search/?q=태양광&x=0&y=0#type=1&page=1"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
    urlLists(driver)
    
def urlLists(driver):
    driver.switch_to_frame('sList')
    time.sleep(2)
    
    newsLists_area = driver.find_elements_by_css_selector(".searchMain")
    newsLists = newsLists_area[2].find_elements_by_css_selector("dl")
    for no in range(len(newsLists)):
        urls = newsLists[no].find_elements_by_css_selector("dt a")
        url = urls[0].get_attribute("href")
        print("url :", url)
        
ytnConnect()


