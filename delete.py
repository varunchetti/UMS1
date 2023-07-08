import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='PUMS',
    user='root',
    password='sandy123'
    )
cur=conn.cursor()
class Delete:
    def departmentdelete(x,col_name,val):
        cur.execute(f"delete from department where {col_name}={val}")
        conn.commit()
        print('data deleted successfully')

    def coursedelete(x,col_name,val):
        cur.execute(f"delete from course where {col_name}={val}")
        conn.commit()
        print('data deleted successfully')

    def studentdelete(x,col_name,val):
        cur.execute(f"delete from student where {col_name}={val}")
        conn.commit()
        print('data deleted successfully')

    def facultydelete(x,col_name,val):
        cur.execute(f"delete from faculty where {col_name}={val}")
        conn.commit()
        print('data deleted successfully')