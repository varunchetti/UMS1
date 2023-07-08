create database PUMS;
use PUMS;
create table student(
student_id int primary key,
student_name varchar(30),
course_id int,
foreign key(course_id)references course(course_id),
department_id int,
foreign key(department_id)references department(department_id));
create table department(
department_id int primary key,
department_name varchar(30));
create table course(
course_id int primary key,
course_name varchar(30),
course_fee int,
duration int);
create table faculty(
faculty_id int primary key,
faculty_name varchar(30),
department_id int,
foreign key(department_id)references department(department_id),
salary int,
course_id int,
foreign key(course_id)references course(course_id));
describe student;
describe department;
describe faculty;
describe course;
select *from department;
select *from course;
select *from student;
select *from faculty;