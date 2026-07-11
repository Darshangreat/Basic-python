import sqlite3




import sqlite3

var = sqlite3.connect('marks.db')
write = var.cursor()

write.execute('''INSERT INTO students (name,roll,marks) values('Yashraj',40,80),
              ('Himesh',41,70),('Sujit',42,85),('Raj',43,35),('Janu',44,45),('Jay',45,100)''')

var.commit()
var.close()






# var = sqlite3.connect('marks.db')
# reader = var.cursor()

# reader.execute('''SELECT * FROM students''')
# data = reader.fetchall()




# for i in data:
#         print(i[1])



# name of students whose marks 