# sqlite3

import sqlite3

var = sqlite3.connect('marks.db')
write = var.cursor()
# write.execute("CREATE TABLE students(id integer primary key autoincrement, name varchar, roll no int, marks int)")

data1 = ('Darshan',1,100)
data2 = ('Rahul',2,00)
data3 = ('Sahil',3,10)



# MEtHOD 1:- 

query = '''INSERT INTO students (name,roll,marks) values(?,?,?)'''
write.executemany(query,(data1,data2,data3))


#METHOD 2:-

query2 = '''INSERT INTO students (name,roll,marks) values ('Raj',45,50),('Janu',52,60),('Jay',56,35)'''
write.execute(query2)


var.commit()
var.close()