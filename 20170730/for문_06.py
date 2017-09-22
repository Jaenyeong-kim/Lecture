import pymysql

def connectDB(data):
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into fortest(test,test2,test3)
         values (%s,%s,%s)"""
    curs.executemany(sql,data)
    conn.commit()

    conn.close()
    
f = open("./test_06.txt","w")
a = ["one","two","three","four","five","six","seven","eight","nine","ten"]
b = ["first","secend","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
c = ["1","2","3","4","5","6","7","8","9","10"]
for i in range(10):
    f.write(a[i]+"\t"+b[i]+"\t"+c[i]+"\n")
    d = [   [   a[i], b[i], c[i]   ]   ]
    print(d)
    connectDB(d)
f.close()

