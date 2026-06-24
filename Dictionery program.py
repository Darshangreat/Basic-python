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

a=['Python','Hii','holiday','Byee']

# output={'Python':6,'Hii': 3,'Holiday': 7,'Byee': 4}

# out = {}
# for i in a:
#     print(i)
#     out[i] = len(i)
# print(out)


# output={'Python':6,'Hii':'iiH','holiday':'yadiloh','Byee':4}

out = {}
for i in a:
    if len(i) % 2 == 0:
        out[i] = len(i)
    else:
        out[i] = i[::-1]

print(out)