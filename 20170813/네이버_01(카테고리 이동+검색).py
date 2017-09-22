from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time 

url = "https://www.naver.com/"
driver = webdriver.Chrome("../lib/chromedriver.exe")
driver.get(url)
time.sleep(1)

naverService = driver.find_elements_by_css_selector(".an_l li") # 네이버 메인 서비스 리스트 태그경로
naverService[4].click()  # 쇼핑 서비스 클릭
time.sleep(1)

naverCategory = driver.find_elements_by_css_selector("#home_category_area .co_category_menu .co_category_list li") # 쇼핑 서비스의 카테고리 리스트 경로
naverCategory[4].click()       # 쇼핑서비스의 전체 카테고리중 가구/인테리어 카테고리 클릭
time.sleep(1)

naverSub_ca = driver.find_elements_by_css_selector("#home_co_menu_interior_inner .co_position .co_col a")  # 가구/인테리어 카테고리의 리스트 태그 경로
naverSub_ca[18].click()   # 가구/인테리어 카테고리의 그릇장/컵보드 카테고리 클릭
time.sleep(1)

search = input("검색 : ")
inputBox = driver.find_element_by_css_selector("#_inqueryInput")  # 카테고리 내 검색 입력 태그 경로
inputBox.send_keys(search)
inputBox.send_keys(Keys.ENTER)


