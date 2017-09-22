search = "태양광"

연합url2 = "http://www.yonhapnews.co.kr/home09/7091000000.html?query={search}&ctype=A".format(search=search)
for pageNo in range(1,10): #1페이지까지
    url = 연합url2 + "&page_no={pageNo}".format(pageNo=pageNo)
    print(url)


url2 = "http://search.chosun.com/search/news.search?query={search}&orderby=news&naviarraystr=&kind=&cont1=&cont2=&cont5=&categoryname=조선일보&categoryd2=&c_scope=navi&sdate=&edate=&premium=".format(search=search)

for page in range(1,11):
    url = url2 + "&pageno=" + str(page)
    print(url)

