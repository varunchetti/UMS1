import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='PUMS',
    user='root',
    password='sandy123'
)
cur=conn.cursor()
class Read:
    def departmentread(x,col_name,val):
        cur.execute(f"select * from department where {col_name}={val}")
        print(cur.fetchall())

    def courseread(x,col_name,val):
        cur.execute(f"select * from course where {col_name}={val}")
        print(cur.fetchall())
    
    def studentread(x,col_name,val):
        cur.execute(f"select * from student where {col_name}={val}")
        print(cur.fetchall())

    def facultyread(x,col_name,val):
        cur.execute(f"select * from faculty where {col_name}={val}")
        print(cur.fetchall())