import pymysql
mydb=pymysql.connect(

    host="localhost",
    user="root",
    password="stockstreet",
    database="SCHOOL",
    port=3306
)

name=input("Enter the name :")
rollno=int(input("Enter the roll number :"))
marks=int(input("Enter the marks :"))
subject=input("Enter the subject :")

write=mydb.cursor()

query="""INSERT INTO STUDENTS (Name,roll_no,marks,subject) VALUES (%s,%s,%s,%s)"""

write.execute(query,(name,rollno,marks,subject))


mydb.commit()
mydb.close()

