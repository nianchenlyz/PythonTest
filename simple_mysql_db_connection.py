import MySQLdb

Con = MySQLdb.Connect(host="localhost",
                      port=3306,
                      user="user_name",
                      passwd="p*a*s*s*w*o*r*d*",
                      db="test"
                      )
Cursor = Con.cursor()
sql = "SELECT * FROM test.testing"
Cursor.execute(sql)

