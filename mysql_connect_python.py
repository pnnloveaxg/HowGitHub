import mysql.connector
mydb = mysql.connector.connect(  # 连接数据库
    host='localhost',
    user='root',
    passwd='root'
)
sql = 'SHOW DATABASES;'  # 查看数据库，注意要大写
mycursor = mydb.cursor()  # 获得光标
mycursor.execute(sql)   # 执行sql语句
for i in mycursor:
    print(i)
