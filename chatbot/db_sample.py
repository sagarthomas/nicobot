import pymysql.cursors

db = pymysql.connect(host ="sql9.freesqldatabase.com", user = "sql9258105", 
                password = "6J17GtRrEI", port = 3306, db = "sql9258105", 
                cursorclass = pymysql.cursors.DictCursor)
cursor = db.cursor()

q1 = "SELECT * FROM NicoBot_LoginMap"

cursor.execute(q1)

result = cursor.fetchall() 
for r in result:
    print(r)