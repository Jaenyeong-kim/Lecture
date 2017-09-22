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
    
f = open("./test_04.txt","w")
a = ["one","two","three","four","five","six","seven","eight","nine","ten"]
for i in 0,1,2,3,4,5,6,7,8,9:
    print(a[i])
    f.write(a[i]+"\n")
    connectDB(a[i])
f.close()


