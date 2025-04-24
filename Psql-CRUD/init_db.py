import psycopg2
conn=psycopg2.connect(database="flask_db",host="localhost",user="postgres",password="pass",port="5432")
cur=conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS courses(id serial PRIMARY KEY,name varchar(100),fees integer,duration integer);")
cur.execute("INSERT INTO courses(name,fees,duration)VALUES('Python',6000,40)('Java',4500,45)('Javascript',7000,50);")
conn.commit()
cur.close()
conn.close()