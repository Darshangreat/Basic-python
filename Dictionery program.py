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

a=['Python.py','basic.html','loop.py','st.css','normal.html','static.py']

# output={'py':3,'html':2,'css':1}

out = {}
for i in a:
    data = i.split('.')
    key=data[1]
    if key not in out:
        out[key] = 1
    else:
        out[key] = out[key] + 1
print(out)