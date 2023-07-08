from insert import Insert
from update import Update
from delete import Delete
from read import Read
v=Insert()
s=Update()
i=Delete()
j=Read()
#v.departmentinsert(1,'mechanical')
print('welcome to the University Management System')
print('Database Information:')
print('No.of tables:4')
print("table name:Student,Department,Course,Faculty")

print('Student Table Information')
print('Number of records:4')
print('columns:student_id,student_name,course_id,department_id')

print('Student Department Information')
print('Number of records:2')
print('columns:department_id,department_name')

print('Student Course Information')
print('Number of records:4')
print('columns:course_id,course_name,course_fee,duration')

print('Student Faculty information')
print('Number of records:5')
print('columns:faculty_id,faculty_name,department_id,salary,course_id')

print('for inserting the data type insert')
print('for updating the data type update')
print('for deleting the data type delete')
print('for reading the data type read')
opr=input('from the above choose an option for operation')
print('press 1 for inserting in the department table')
print('press 2 for inserting in the student table')
print('press 3 for inserting in the course table')
print('press 4 for inserting in the faculty table')


if opr=='insert':
    tab=int(input('choose an option from the above'))
    if tab==1:
        dpt_id=int(input('enter the department_id'))
        dpt_name=input('enter the department_name')
        v.departmentinsert(dpt_id,dpt_name)

if opr=='update':
    tab=int(input('choose an option from the above'))
    if tab==1:
        col=input('enter the column name')
        newval=input('enter new value')
        oldval=input('enter old value')
        s.departmentupdate(col,newval,oldval)

if opr=='delete':
    tab=int(input('choose an option from the above'))
    if tab==1:
        col=input('enter column name')
        value=input('enter the department_id')
        i.departmentdelete(col,value)

if opr=='read':
    tab=int(input('choose an option from the above '))
    if tab==1:
        col=input('enter column name')
        value=input('enter the department_id')
        j.departmentread(col,value)

if opr=='insert':
    if tab==3:
        c_id=int(input('enter course id'))
        c_n=input('enter course name')
        c_f=int(input('enter course fee'))
        du=int(input('enter duration'))
        v.courseinsert(c_id,c_n,c_f,du)


if opr=='update':
    if tab==3:
        col=input('enter the column name')
        newval=input('enter new value')
        oldval=input('enter old value')
        s.courseupdate(col,newval,oldval)

if opr=='delete':
    if tab==3:
        col=input('enter column name')
        value=input('enter the course_id')
        i.coursedelete(col,value)

if opr=='read':
    if tab==3:
        col=input('enter column name')
        value=input('enter the course_id')
        j.courseread(col,value)

if opr=='insert':
    if tab==2:
        s_id=input('enter student id')
        s_n=input('enter student name')
        c_id=input('enter course id')
        d_id=input('enter department_id')
        v.studentinsert(s_id,s_n,c_id,d_id)

if opr=='update':
    if tab==2:
        col=input('enter the column name')
        newval=input('enter new value')
        oldval=input('enter old value')
        s.studentupdate(col,newval,oldval)

if opr=='delete':
    if tab==2:
        col=input('enter column name')
        value=input('enter the student_id')
        i.studentdelete(col,value)

if opr=='read':
    if tab==2:
        col=input('enter column name')
        value=input('enter the student_id')
        j.studentread(col,value)

if opr=='insert':
    if tab==4:
        f_id=input('enter faculty id')
        f_n=input('enter faculty name')
        d_id=input('enter department id')
        sa=input('enter salary')
        c_id=input('enter course id')
        v.facultyinsert(f_id,f_n,d_id,sa,c_id)

if opr=='update':
    if tab==4:
        col=input('enter the column name')
        newval=input('enter new value')
        oldval=input('enter old value')
        s.facultyupdate(col,newval,oldval)

if opr=='delete':
    if tab==4:
        col=input('enter column name')
        value=input('enter the faculty_id')
        i.facultydelete(col,value)


if opr=='read':
    if tab==4:
        col=input('enter column name')
        value=input('enter the faculty_id')
        j.facultyread(col,value)