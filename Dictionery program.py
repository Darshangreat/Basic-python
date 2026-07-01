#Q Print name of student more then 50 marks


# a={'Aman':70, 'Atharva': 90, 'Nayan': 56, 'Jyoti': 30}

# for i in a:
#     if a[i] > 50:
#         print(i,a[i])






#Q. Extract the data of student whose name start with A




# out = {}
# for i in a:
#     if i[0] == 'A':
#         print(i,a[i])
#         out[i] = a[i]
# print(out)



#Q. Extract the key value pair from the dictionery only if the key is of
# string data type

# data ={'python':8,12 : 'Hii',56 :'Data'}
#
# out = {}
# for i in data:
#     if type(i) == str:
#         print(i,data[i])
#         out[i] = data[i]
# print(out)



#Q. Wap to get the following output

# a=['Python','Hii','holiday','Byee']

# output={'Python':6,'Hii': 3,'Holiday': 7,'Byee': 4}

# out = {}
# for i in a:
#     print(i)
#     out[i] = len(i)
# print(out)





# output={'Python':6,'Hii':'iiH','holiday':'yadiloh','Byee':4}

# out = {}
# for i in a:
#     if len(i) % 2 == 0:
#         out[i] = len(i)
#     else:
#         out[i] = i[::-1]
#
# print(out)







#Q. Wap to count occurences of the character in the string


#agar nhi toh add karo or agar hai toh update karo

# a='banana'
# out = {}
# for i in a:
#     if i not in out:
#         out[i] = 1
#     else:
#         out[i] = out[i] + 1
# print(out)



#Q.

# a='Python is easy Python is dynamically typed'
#output={'Python':2,'is':2,'easy':1,'dynamically':1,'typed':1}


# out = {}
# data=a.split()
#
# for i in data:
#     if i not in out:
#         out[i] = 1
#     else:
#         out[i] = out[i] + 1
# print(out)



#Q.

# a=(12,3,4,'hello',2+3j,'python','bye',False)
#output={'hello : 5,'python' : 6, 'bye' : 3}

# out = {}
#
# for i in a:
#     if type(i) == str:
#         out[i] = len(i)
# print(out)





#Q.

# a=(12,3,4,'hello',2+3j,'python','bye',False)
# output={'hello':'ho','python':'pn','bye':'be'}

# out ={}
# for i in a:
#     if type(i) == str:
#         out[i] = i[0] + i[-1]
# print(out)





#Q. Wap to replace the space with underscore in the below string

# a='Python is easy Python is dynamically typed'

# out = ''
#
# for i in a:
#     if i == ' ':
#         out = out + '_'
#     else:
#         out = out + i
# print(out)



#Q.

# a=['python.py','basic.html','loop.py','st.css']
# out=['py','html','py','css']

# out = []
#
# for i in a:
#     data = i.split('.')
#     out.append(data[1])
#     print(i)
# print(out)





#.Q

# a=['Python.py','basic.html','loop.py','st.css','normal.html','static.py']

# output={'py':3,'html':2,'css':1}

# out = {}
# for i in a:
#     data = i.split('.')
#     key=data[1]
#     if key not in out:
#         out[key] = 1
#     else:
#         out[key] = out[key] + 1
# print(out)








# a=int(input('Enter the number:'))
# for i in range(2,a):
#     if a % i == 0:
#         print('It is not a prime number')
#         break
# else:
#     print('It is a prime number')








#Q. Wap to check if a giver number is perfect number or not


# a=int(input('Enter the number:'))
# out = 0
# for i in range(1,a):
#     if a % i == 0:
#         print(i)
#         out = out + i
# if a == out:
#     print(a,'It is perfect number')
# else:
#     print(a,'It is not a perfect number')








#Q. Wap to check whether the list is homogeneus or hetrogeneus

# a=[12,45,56,True]
#
# check = a[0]
# for i in a:
#     if type(i) != type(check):
#         print('Hetrogeneus')
#         break
# else:
#     print('Homogenues')




# Q1.

# a=1,2,3,4,5,6,7,8,9,10
#
# for i in a:
#     if i % 2 == 0:
#         print(i)





# Q2.

# a=1,2,3,4,5,6,7,8,9,10
#
# for i in a:
#     if i % 2 != 0:
#         print(i)



# Q3.

# a=0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20
#
# for i in range(0,10):
#     print(i)




# Q. wap to print the factorial of the number

# a=int(input('Enter the number:'))
#
# out = 1
# for i in range(a,0,-1):
#     out = out*i
# print(out)




#Q. wap to fetch only even values of the keys from the dictionery

# n={'val1':10,'val2':20,'val3':23,'val4':22}
# out = []
#
# for i in n:
#     if n[i] % 2 == 0:
#         out.append(n[i])
# print(out)



# Q.55

# n='abcd'
# out = {}
#
# for i in n:
#     if i in n:
#         out[i] = ord(i)
# print(out)




#Q.56

# a = 'hello'
# out = {}
#
# data = 0
# for i in a:
#     out[data] = i
#     data += 1
# print(out)



#Q.wap to extract all the int from the list only if integer starting
# with even number and ending as odd number and having lenth more than 3

a=[12,8+9j,'Hii',True,241,437,838]

out = []
for i in a:
    if type(i) == int:
        data=str(i)
        fd=data[0]
        ld=data[-1]
        if(100<= i <=999) and int(fd) %2 == 0 and int(ld) % 2 != 0:
            out.append(i)
print(out)
