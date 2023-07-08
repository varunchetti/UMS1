import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='PUMS',
    user='root',
    password='sandy123'
)
cur=conn.cursor()
class Update:
    def departmentupdate(x,col_name,new_value,old_value):
        cur.execute(f"update department set {col_name}='{new_value}' where {col_name}='{old_value}'")
        conn.commit()
        print('data updated successfully')
    
    def courseupdate(x,col_name,new_value,old_value):
        cur.execute(f"update course set {col_name}='{new_value}' where {col_name}='{old_value}'")
        conn.commit()
        print('data updated successfully')

    def studentupdate(x,col_name,new_value,old_value):
        cur.execute(f"update student set {col_name}='{new_value}' where {col_name}='{old_value}'")
        conn.commit()
        print('data updated successfully')

    def facultyupdate(x,col_name,new_value,old_value):
        cur.execute(f"update faculty set {col_name}='{new_value}' where {col_name}='{old_value}'")
        conn.commit()
        print('data updated successfully')