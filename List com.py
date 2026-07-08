#Q. Wap to create list of square of integer of between 1 to 20


# out = []
# for i in range(1,20 +1):
#     out.append(i**2)
# print(out)


# data = [i**2 for  i in range(1,20+1)]
# print(data)


#Q. wap to create of list of square of integers between 1 to 20 only if it is multiple of 3

# out = []
# for i in range(1,20 + 1):
#     if i % 3 == 0:
#         out.append(i**2)
# print(out)


# data = [i**2 for i in range(1,20+1) if i % 3 == 0]
# print(data)




#Q. Program to extarct string from the list only if it is palindrome

# l = ['hi',100,3.2,'madam','appa','bye']

# out = []
#
# for i in l:
#     if type(i) == str and i==i[::-1]:
#         out.append(i)
# print(out)

# data = [i for i in l if type(i) == str and i == i[::-1]]
# print(data)







#Q. Wap to store the square of integer if it is even or else store the cube of integer between 1 to 11

# out =  []
# for i in range(1,11+1):
#     if i % 2 == 0:
#         out.append(i**2)
#     else:
#         out.append(i**3)
# print(out)


data = [i**2 if i % 2 == 0 else i**3 for i in range(1,11+1)]
print(data)