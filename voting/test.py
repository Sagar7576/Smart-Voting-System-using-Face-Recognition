import mysql.connector
from mysql.connector import Error
connection = mysql.connector.connect(host='localhost',
                                             database='fvoting',
                                             user='root',
                                             password='root')
cursor = connection.cursor()
cursor.execute("insert into candidates(name,party,image,votes)values('{}','{}','{}','{}')".format('arun','bjp','sgiaayur',0))
connection.commit()
connection.close()
