import pymysql

def connectDB(data):
    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWD = 'autoset'
    DB_NAME = 'python'
    
    conn = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWD,
                       db=DB_NAME, charset='utf8')
    
    curs = conn.cursor()

    sql = """insert into fortest(test,test2)
         values (%s,%s)"""
    curs.executemany(sql,data)
    conn.commit()

    conn.close()
    
f = open("./test_05.txt","w")
a = ["one","two","three","four","five","six",
     "seven","eight","nine","ten"]
b = ["first","secend","third","fourth","fifth",
     "sixth","seventh","eighth","ninth","tenth"]
for i in range(10):
    print(a[i]  ,  b[i])
    f.write(a[i]+"\t"+b[i]+"\n")
    c = [  [  a[i],  b[i]  ]  ]
    connectDB(c)
f.close()


