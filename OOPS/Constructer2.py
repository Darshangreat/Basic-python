# class Company:
#
#     Total_employee = 50
#     Company_name = 'Jio'
#     Contact = 1234565
#
#     def __init__(self, id_no, salary, performance, bank):
#         self.ID_NO = id_no
#         self.SALARY = salary
#         self.PERFORMANCE = performance
#         self.BANK = bank
#
#
# darshan = Company(1,50000,'Great','SBI')
# print(darshan.ID_NO,darshan.SALARY,darshan.PERFORMANCE,darshan.BANK)
# rahul = Company(2,40000,'Good','ICICI')
# print(rahul.ID_NO,rahul.SALARY,rahul.PERFORMANCE,rahul.BANK)
# sahil = Company(3,30000,'Fail','Baroda')
# print(sahil.ID_NO,sahil.SALARY,sahil.PERFORMANCE,sahil.BANK)






class College:

    Collage_name = 'R.K.T'
    Address = 'Ulhasnagar 3'
    Computer_lab = 3
    Professor = 6

    def __init__(self,name,roll_no,phone_no,stream):
        self.NAME = name
        self.ROLL_NO = roll_no
        self.PHONE_NO = phone_no
        self.STREAM = stream



    def change_phone_no(self,phone_no):
        self.PHONE_NO= phone_no


    def change_stream(self,stream):
        self.STREAM = stream


student1=College('Darshan',12,5875282725,'CS')
student2=College('Vedant',13,4448472456,'IT')
# print(student2.PHONE_NO)
# student2.change_phone_no(65567757654)
# print(student2.PHONE_NO)
#
# print(student1.PHONE_NO)
# student1.change_phone_no(123456852145)
# print(student1.PHONE_NO)

print(student1.STREAM)
student1.change_stream('IT')
print(student1.STREAM)


# print(student1.NAME,student1.ROLL_NO,student1.PHONE_NO,student1.STREAM)
# print(student1.Collage_name,student1.Address,student1.Computer_lab,student1.Professor,sep = '\n')

# print(student2.NAME,student2.ROLL_NO,student2.PHONE_NO,student2.STREAM)
# print(student2.Collage_name,student2.Address,student2.Computer_lab,student2.Professor,sep = '\n')