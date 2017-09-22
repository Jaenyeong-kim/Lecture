
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


# In[2]:


#search = input("검색 :")
#search = "다이소"
search = "메이크업 포에버 아이브로우"
#search = "다이소 기름종이 파우더"
url = "https://www.unpa.me/search?q={search}&verb=minireview&sort=score".format(search=search)
driver = webdriver.Chrome("./chromedriver.exe")
driver.get(url)

while True:
    try:
        a = driver.find_elements_by_css_selector(".unpa-load-more-button")
        if a[0].text == '':
            print("더보기 없음")
            break
        else:
            a[0].click()
            time.sleep(1)
            print("더보기 클릭")
    except:
        print("더보기 없음")
        break


# In[ ]:





