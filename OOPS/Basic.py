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









class School:
    principal = 'Mr Shyam'
    total_class = 10
    total_subjects = 8

naman = School()
divyansh = School()

print('Before',School.principal)
School.principal = 'Mr Devansh'
print('After',School.principal)
print(naman.principal)
print(divyansh.principal)

