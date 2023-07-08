import mysql.connector
conn=mysql.connector.connect(
    host='localhost',
    database='PUMS',
    user='root',
    password='sandy123'
)

cur=conn.cursor()
class Insert:
    def departmentinsert(x,department_id,department_name):
        cur.execute(f"insert into department values({department_id},'{department_name}')")
        conn.commit()
        print('data entered succesfully')
    
    def courseinsert(x,cid,cn,cf,dur):
        cur.execute(f"insert into course values({cid},'{cn}',{cf},{dur})")
        conn.commit()
        print('data inserted successfully')
    
    def studentinsert(x,sid,sn,cid,did):
        cur.execute(f"insert into student values({sid},'{sn}',{cid},{did})")
        conn.commit()
        print('data inserted successfully')
    
    def facultyinsert(x,fid,fn,did,sal,cid):
        cur.execute(f"insert into faculty values ({fid},'{fn}',{did},{sal},{cid})")
        conn.commit()
        print('data inserted successfully')
