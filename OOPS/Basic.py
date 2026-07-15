# class Key:
#     a = 10
#     b = 20
#
# obj1 = Key()
# obj2 = Key()


 # Method 1

# print(Key.a)
# print(Key.b)

 # Method 2

# print(obj1.a)
# print(obj1.b)
# print(obj2.b)






# class School:
#     principal = 'Mr Shyam'
#     total_class = 10
#     total_subjects = 8
#
# naman = School()
# divyansh = School()


# print(School.principal,School.total_class,School.total_subjects)
# print(naman.principal,naman.total_class,naman.total_subjects,sep = '\n')









# class School:
#     principal = 'Mr Shyam'
#     total_class = 10
#     total_subjects = 8
#
# naman = School()
# divyansh = School()
#
# print('Before',School.principal)
# School.principal = 'Mr Devansh'
# print('After',School.principal)
# print(naman.principal)
# print(divyansh.principal)






#Create a class bank and also create 4 properties as well as 2 objects


class Bank:

    Manager = 'Mr Ram'
    Address = 'Ulhasnagar 3'
    Branch = 'Kalyan'
    Bank_name = 'SBI'

obj1 = Bank()
obj2 = Bank()
print(obj1.Manager,obj1.Address,obj1.Branch,obj1.Bank_name)
print(obj2.Manager,obj2.Address,obj2.Branch,obj2.Bank_name)
print(Bank.Manager,Bank.Address,Bank.Branch,Bank.Bank_name, sep = '\n')



obj1.Manager = 'Mr Darshan'
print(obj1.Manager,obj1.Address,obj1.Branch,obj1.Bank_name)

Bank.Manager = 'Mr Darshan'
print(Bank.Manager,Bank.Address,Bank.Branch,Bank.Bank_name)
