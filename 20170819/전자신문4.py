from selenium import webdriver
from selenium.webdriver.common.keys import Keys

def etnewsUrl(search):
    url = "http://search.etnews.com/etnews/search.php?category=CATEGORY1&kwd={search}&pageSize=10&reSrchFlag=false&sort=1&startDate=&endDate=&sitegubun=&jisikgubun=&preKwd%5B0%5D=4%EC%B0%A8%EC%82%B0%EC%97%85%ED%98%81%EB%AA%85".format(search=search)    
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    
    etnewsUrlList(driver,url)

def etnewsUrlList(driver,url2):
#    url2 = driver.current_url
    etnewsUrs_List = []
    for pageNo in range(1,3): #1페이지까지
        url = url2 + "&pageNum={pageNo}".format(pageNo=pageNo)
        driver.get(url)
        
        etnewsUrs= driver.find_elements_by_css_selector(".list_news .clearfix dt a")
    
        for urlList in etnewsUrs:
            etnewsUrs_List.append(urlList.get_attribute("href"))
    return etnewsInfo(driver,etnewsUrs_List)

def etnewsInfo(driver,etnewsUrs_List):
    for urlList in etnewsUrs_List:
        driver.get(urlList)
        newsTitle = driver.find_element_by_css_selector(".article_title").text
#        newsSubtitle = driver.find_element_by_css_selector("#articleBody h3").text
        newSubtitle_result = ""
    #    for newsSubtitle in newsSubtitles:
    #        newSubtitle_result+=newsSubtitle.text
        newsContents = driver.find_elements_by_css_selector("#articleBody p")
        print("- 기사 제목 - : \n",newsTitle)
#        print("- 기사 부제목 - \n:",newSubtitle_result)
        print("- 기사 본문 - \n")
        for content in newsContents:
            print(content.text,end=" ")

search = input("검색 : ")
etnewsUrl(search)


