import mysql.connector
#
# con=mysql.connector.connect(user='root',password='root',host='localhost')
# #establish connection between python code and mysql server
# # it returns a connection object
#
# print(con)
#
# c=con.cursor() #cursor object used to execute sql queries/commands
#
#
# # c.execute(command)
#
# #create database file
#
# c.execute('create database school_db')
# print('database file created')

con=mysql.connector.connect(user='root',password='root',host='localhost',database='school_db')

c=con.cursor()
#
# c.execute('''create table student(roll_no int not null primary key,
#                                   name varchar(20),
#                                   age int,
#                                   place varchar(20),
#                                   phone varchar(20),
#                                   total_mark int)''')
#
# print('table created')

# c.execute('''insert into student(roll_no,name,age,place,phone,total_mark)
#                           values(101,'arun',11,'ekm',79298,145),
#                           (102,'amal',12,'ekm',79246,140),
#                           (103,'anu',11,'tvm',67354,147),
#                           (104,'hari',12,'tcr',98698,144),
#                           (105,'manu',11,'ekm',90029,141)
#                           ''')

# query='insert into student(roll_no,name,age,place,phone,total_mark) values(%s,%s,%s,%s,%s,%s)'
# data=(106,'kiran',12,'ekm','7683947829',140)
#
# c.execute(query,data)
#
# con.commit() #to save data permenatly inside db
#
# print('data inserted successfully')

#READ operation

# query='select * from student'
# c.execute(query)

# records=c.fetchall()
#
# if records:
#     for row in records:
#         print(row)
# else:
#     print('no records found')

#read all attributes of a student with roll number = roll number entered by user

# number =int(input('enter the roll number : '))
# query='select * from student where roll_no=%s'
# data=(number,)
# c.execute(query,data)
# record=c.fetchone()
# if record:
#     print(record)
# else:
#     print('no record found')

#update mark of a student with roll number = roll number entered by user

# number=int(input('enter the roll number : '))
# mark=int(input('enter new mark : '))
# query='update student set total_mark=%s where roll_no=%s'
# data=(mark,number)
# c.execute(query,data)
# record=c.fetchone()
# con.commit()
# print('updated')




#delete a record with roll number = roll number entered by user
#
# number=int(input('enter the roll number : '))
# query='delete from student where roll_no=%s'
# data=(number,)
# c.execute(query,data)
# con.commit()
# print('deleted')

#create a new record using values entered by the user

number=int(input('enter roll number : '))
name=input('enter name : ')
age=int(input('enter age : '))
place=input('enter location : ')
phone=int(input('enter phone number : '))
total_mark=int(input('enter total mark : '))

query='insert into student (roll_no,name,age,place,phone,total_mark)values(%s,%s,%s,%s,%s,%s)'
data=(number,name,age,place,phone,total_mark)
c.execute(query,data)
con.commit()
print('inserted')
