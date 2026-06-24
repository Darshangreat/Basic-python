# for i in 'hii':
#     print(i)

# for i in [12,45,89]:
#     print(i)


# for i in ('hii',12,54,4+4j):
#     print(i)

# for i in {12,'hi',12.3,4+8j,True}:
#     print(i)

# b = {'name': 'Darshan', 'age': 12}
# for i in b:
#     print(i, b[i])






#Q. Wap to print only the numbers divisible by 5 between 100 to 300



# for i in range(100,300 + 1):
#     if  i % 5 == 0:
#         print(i)


#Q Wap to print only vowels from the string

# a=input('Enter the string:')
#
# i = 0
# while i < len(a):
#     if a[i] in 'AEIOUaeiou':
#         print(a[i])
#     i += 1
#
# for i in a:
#     if i in 'AEIOUaeiou':
#         print(i)







#
# Q. Wap to only extract integer data type from the below list
#
# a=[12,'hi',8+9j,True,45]
#
# out = []
# for i in a:
#     if type(i) == int:
#         out.append(i)
# print(out)






#Q. Wap to get the following output

# g = 'PyTHON@12#'

# upper = 'PTH'
# lower = 'y'
# special = '@#'
# digits = '12'

# upper = ''
# lower = ''
# sc = ''
# digits = ''
#
# for i in g:
#     if 'A' <= i <= 'Z':
#         upper += i
#     elif 'a' <= i <= 'z':
#         lower += i
#     elif '0' <= i <= '9':
#         digits += i
#     else:
#         sc += i
# print(upper)
# print(lower)
# print(digits)
# print(sc)







# Wap to extract vowels and consonants from string


# a='Darshan'
# out1='aa'
# out2='Drshn'

# out1 = ''
# out2 = ''
#
# for i in a:
#     if i in 'AEIOUaeiou':
#         out1 = out1 + i
#     else:
#         out2 = out2 + i
#
# print(out1)
# print(out2)






#Q. Wap to extract only the character present at odd index


# a=input('Enter the character:')
# out = ''
# for i in range(0,len(a)):
#     if i % 2 != 0:
#         out = out + a[i]
# print(out)








#Q. Wap to reverse the string without using slicing


# a=input('Enter the string:')
# out = ''
# for i in a:
#     out = i + out
# print(out)








#Q. Wap to check is given string is palindrome or not without using slicing


# a=input('Enter the string:')
#
# out = ''
# for i in a:
#     out = i + out
# if out == a:
#     print('Palindrome',a)
# else:
#     print('Not palindrome',a)






#Q. Wap to find factorial of number

# a=int(input('Enter the number:'))

# out = 1
# for i in range(a,0,-1):
#
#     out=out*i
# print(out)



#Q Wap to seprate possitive and negative numbers from the list



# a=[12,True,7.8,-134,7,'Hii',-3.5,9]
#
# out1 = []
# out2 = []
# for i in a:
#     if type(i) == int or type(i) == float:
#         if i >= 0:
#             out1.append(i)
#         else:
#             out2.append(i)
# print(out1)
# print(out2)



#Q. Wap to extract all the string data from the list only if it is palindrome


# a=[12,'Hii','mom',True,6.7,8+9j,'nayan','harsha']
#
# out = []
# for i in a:
#     if type(i) == str:
#         if i==i[::-1]:
#             out.append(i)
# print(out)







#Q. Wap to reverse the number using for loop

# a=int(input('Enter the number:'))
# number = str(a)
# # print(number,type(number))
#
# out = ''
# for i in number:
#     out = i + out
# out = int(out)
# print(out)


#Q. Wap to check if given number is palindrome or not


# a=int(input('Enter the number:'))
#
# number = str(a)
# out = ''
# for i in number:
#     out = i + out
# out = int(out)
# if a == out:
#     print('palindrome')
# else:
#     print('not palindrome')






#Q. Wap