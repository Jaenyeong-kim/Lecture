import pymysql
import csv

def dbConnect():
    conn = pymysql.connect(host='127.0.0.1',
                           user='root', password='autoset',
                           db='python', charset='utf8')

    curs = conn.cursor()

    sql = "select * from chosunnews"
    curs.execute(sql)

    rows = curs.fetchall()
    conn.close()
    
    csvCreate(rows)
    
def csvCreate(rows):
    csv_file = open("dbData.csv", "w",newline='',encoding='euc_kr')
    cw = csv.DictWriter(csv_file ,['no','title','subject','content'])
    cw.writeheader()
    listTest = []

    for i in range(0,10):  # 임시로 10개의 행만 가져오게 설정
        listTest = []
        no = rows[i][0]
        title = rows[i][1]
        subject = rows[i][2]
        content = rows[i][3]
        listTest.append({'no':no,'title':title,'subject':subject,'content':content})
        cw.writerows(listTest)
    csv_file.close()
    
dbConnect()    


