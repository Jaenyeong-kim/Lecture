
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import Series, DataFrame
import pprint

def kmaConnect():
    url = "http://www.kma.go.kr/weather/forecast/mid-term_01.jsp"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    kmaWeather(driver)
    kmaTemperature(driver)
    
def kmaWeather(driver):
    dates = driver.find_elements_by_css_selector(".table_midterm thead .top_line")
    datesList =[]
    for dates_i in range(1,9):
        if dates_i < 6 :
            for mA in range(2):
                if mA == 0:
                    datesText = dates[dates_i].text
                    datesTextRe = datesText.replace("\n","")
                    datesList.append(datesTextRe+"(오전)") 
                else:
                    datesList.append(datesTextRe+"(오후)")
        else:
            datesText = dates[dates_i].text
            datesTextRe = datesText.replace("\n","")
            datesList.append(datesTextRe) 
            
    area = driver.find_elements_by_css_selector(".table_midterm tbody tr th")
    areaList =[]
    
    for area_i in range(10):
        result = (area[area_i].text).replace("\n",",")
        areaList.append(result)

    weather= driver.find_elements_by_css_selector(".table_midterm tbody .png24")
    weatherList_result = []
    
    for rows in range(0,130,13):
        weatherList=[]
        for columns in range(rows,rows+13):
                weatherList.append(weather[columns].get_attribute("alt"))
        weatherList_result.append(weatherList)
        
    weatherFrame = pd.DataFrame(weatherList_result,columns=datesList,index=areaList)
    
    return pprint.pprint(weatherFrame)

def kmaTemperature(driver):
    TemperatureDates = driver.find_elements_by_css_selector(".table_midterm .top_line ")
    TemperatureDateList = []
    
    for Temperature_i in range(11,len(TemperatureDates)):
        TemperatureDateList.append((TemperatureDates[Temperature_i].text).replace("\n",""))
        
    Temperatures = driver.find_elements_by_css_selector(".table_midterm tbody tr ul")
    TemperaturesList_result = []
    
    for rows02 in range(130,len(Temperatures),8):
        TemperaturesList = []
        for columns in range(rows02,rows02+8):
            TemperaturesList.append(Temperatures[columns].text)
        TemperaturesList_result.append(TemperaturesList)
    
    TemperatureArea = ['서울','인천','수원','파주','춘천','원주','강릉','청주','대전','서산','세종','전주','군산','광주','목포','여수','대구','안동','포항','부산','울산','창원','제주','서귀포']
    TemperatureFrame = pd.DataFrame(TemperaturesList_result,columns=TemperatureDateList,index=TemperatureArea)
    return pprint.pprint(TemperatureFrame)
    
kmaConnect()


