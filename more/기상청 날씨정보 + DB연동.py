
# coding: utf-8

# In[1]:

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
from pandas import Series, DataFrame
import pprint
import pymysql


# In[59]:

def kmaConnect():
    url = "http://www.kma.go.kr/weather/forecast/mid-term_01.jsp"
    driver = webdriver.Chrome("./chromedriver.exe")
    driver.get(url)
    kmaWeather(driver)
    kmaTemperature(driver)
    
def kmaWeather(driver):
    dbShape = "Weather"
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
    date = datesList[0]+"~"+datesList[12]
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
    
    for areaLen in range(10):
        dbData = [[areaList[areaLen],date,weatherList_result[areaLen][0],weatherList_result[areaLen][1],             weatherList_result[areaLen][2],weatherList_result[areaLen][3],weatherList_result[areaLen][4],weatherList_result[areaLen][5],             weatherList_result[areaLen][6],weatherList_result[areaLen][7],weatherList_result[areaLen][8],weatherList_result[areaLen][9],             weatherList_result[areaLen][10],weatherList_result[areaLen][11],weatherList_result[areaLen][12]]]
        kmaDB(dbData,dbShape)
    return pprint.pprint(weatherFrame)

def kmaTemperature(driver):
    dbShape = "Temperature"
    TemperatureDates = driver.find_elements_by_css_selector(".table_midterm .top_line ")
    TemperatureDateList = []
    
    for Temperature_i in range(11,len(TemperatureDates)):
        TemperatureDateList.append((TemperatureDates[Temperature_i].text).replace("\n",""))
    date = TemperatureDateList[0]+"~"+TemperatureDateList[7]
    Temperatures = driver.find_elements_by_css_selector(".table_midterm tbody tr ul")
    TemperaturesList_result = []
    
    for rows02 in range(130,len(Temperatures),8):
        TemperaturesList = []
        for columns in range(rows02,rows02+8):
            TemperaturesList.append(Temperatures[columns].text)
        TemperaturesList_result.append(TemperaturesList)
    
    TemperatureArea = ['서울','인천','수원','파주','춘천','원주','강릉','청주','대전','서산','세종','전주','군산','광주','목포','여수','대구','안동','포항','부산','울산','창원','제주','서귀포']
    TemperatureFrame = pd.DataFrame(TemperaturesList_result,columns=TemperatureDateList,index=TemperatureArea)
    
    for i in range(24):
        dbData = [[TemperatureArea[i],date,TemperaturesList_result[i][0],TemperaturesList_result[i][1],TemperaturesList_result[i][2], TemperaturesList_result[i][3],TemperaturesList_result[i][4],TemperaturesList_result[i][5],TemperaturesList_result[i][6],                  TemperaturesList_result[i][7]]]
        kmaDB(dbData,dbShape)
        
    return pprint.pprint(TemperatureFrame)

def kmaDB(dbData,dbShape):
    DB_HOST = '127.0.0.1'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    kmaWeather_sql = """insert into kmaWeather(area,date,day1_Mo,day1_Af,day2_Mo,day2_Af,day3_Mo,day3_Af,day4_Mo,day4_Af,day5_Mo,day5_Af,day6,day7,day8)
         values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
   
    kmaTemperature_sql = """insert into kmaTemperature(area,date,day1,day2,day3,day4,day5,day6,day7,day8)
         values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    if dbShape == "Weather":
        curs.executemany(kmaWeather_sql,dbData)
    else:
        curs.executemany(kmaTemperature_sql,dbData)
    conn.commit()

    conn.close()
    
kmaConnect()


