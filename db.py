import pymysql

mydb=pymysql.connect(

    host="localhost",
    user="root",
    password="stockstreet",
    database="SCHOOL",
    port=3306
)
write=mydb.cursor()

# write.execute("""CREATE TABLE students(id INTEGER PRIMARY KEY AUTO_INCREMENT ,Name VARCHAR(100), roll_no INTEGER,marks INTEGER)""")

# query = '''INSERT INTO students(Name,roll_no,marks)values('Darshan',01,50),('Rahul',02,53),('Sahil',03,45)'''
# write.execute(query)




# write.execute('''SELECT * FROM students''')
# data = write.fetchall()
#  print(data)

# for i in data:
#     print(i[1])


# query='''delete from students where id = 2'''
# write.execute(query)


# query = '''UPDATE  students SET marks = 500 where id=1'''
# write.execute(query)


# query = '''alter table students add column subject varchar(25)'''
# write.execute(query)

mydb.commit()
mydb.close()