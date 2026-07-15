# class Bank:
#
#     Manager = 'Mr Ram'
#     Address = 'Ulhasnagar 3'
#     Branch = 'Kalyan'
#     Bank_name = 'SBI'
#
# darshan = Bank()
# darshan.Mob_number = 564556425
# darshan.age = 22
# darshan.balance = 5200
#
# rahul = Bank()
# rahul.Mob_number = 454745454
# rahul.age = 12
# rahul.balance = 22
#
#
# darshan.balance = 10000
# print(darshan.Mob_number,darshan.age,darshan.balance)
# rahul.balance = 1
# print(rahul.Mob_number,rahul.age,rahul.balance)




#Q. Create a class company which consist of 3 class members , 3 objects and 4 object members

# class Company:
#
#     Total_employee = 50
#     Company_name = 'Jio'
#     Contact = 1234565
#
# darshan = Company()
# rahul = Company()
# sahil = Company()
#
# darshan.id_no = 1
# darshan.salary = 50000
# darshan.performance = 'great'
# darshan.bank = 'SBI'
#
# print(darshan.id_no,darshan.salary,darshan.performance,darshan.bank)
#
# rahul.id_no = 2
# rahul.salary = 40000
# rahul.performance = 'good'
# rahul.bank = 'SBI'
#
# print(rahul.id_no,rahul.salary,rahul.performance,rahul.bank)
#
# sahil.id_no = 3
# sahil.salary = 30000
# sahil.performance = 'bad'
# sahil.bank = 'SBI'
#
# print(sahil.id_no,sahil.salary,sahil.performance,sahil.bank)




#Q. Create a class collage which consist of  4 class member 3 objects and 3 object members


class College:

    Collage_name = 'R.K.T'
    Address = 'Ulhasnagar 3'
    Computer_lab = 3
    Professor = 6

darshan = College()
vedant = College()
pathak = College()

def obj_member(obj_name,roll_no,phone_no,stream):
    obj_name.ROLL_NO= roll_no
    obj_name.PHONE_NO = phone_no
    obj_name.STREAM = stream

obj_member(darshan,1,202020,'IT')
print(darshan.ROLL_NO,darshan.PHONE_NO,darshan.STREAM)

obj_member(vedant,2,3030303,'IT')
print(vedant.ROLL_NO,vedant.PHONE_NO,vedant.STREAM)

obj_member(pathak,3,4040404,'IT')
print(pathak.ROLL_NO,pathak.PHONE_NO,pathak.STREAM)
