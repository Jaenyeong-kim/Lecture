import pymysql

def connectDB(data):
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into fortest(test)
         values (%s)"""
    curs.execute(sql,data)
    conn.commit()

    conn.close()

    
print("공백 입력 시 반복문 종료!!")

while True:
    search = input("추가 단어 : ")
    f = open("./test_06.txt","a")
    f.write(search+"\n")
    if search == "":
        print(search)
        f.close()
        break
    connectDB(search)

        



