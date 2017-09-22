
import requests
from bs4 import BeautifulSoup
import re

search = input("검색 : ")
url = "http://www2.hm.com/ko_kr/search-results.html?q={search}&page-size=1000".format(search=search)
req = requests.get(url)
reqBs = BeautifulSoup(req.content,"html.parser")
productLists = reqBs.select(".product-item-details")

for no in range(len(productLists)):
    title = productLists[no].select(".product-item-heading a")[0].text
    print("상품 :", title)
    
    price = productLists[no].select(".price")
    priceBlank = str(price).replace(" ","")
    price_compile = re.compile("\d?\d?\d?\,\d?\d?\d?")
    priceResult = price_compile.findall(priceBlank)[0]
    print("가격:",priceResult)


