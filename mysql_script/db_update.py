import pymysql

conn = pymysql.connect(host='localhost', user='root', password='1234', db='eliceproject', charset='utf8') 
cursor = conn.cursor() 


print("dbconnection!!")
# sql = "update book set " + 

for data in range(5,30):
    sql = "update book set book_id = " + str(data) +  " where book_id = " + str(data+1)
    print(sql)
    cursor.execute(sql)
    
conn.commit() 
conn.close() 