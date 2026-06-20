#a = 12
# b = 54
# print(type(a), type(b))
# print(a,b,sep=' $ ')
from platform import mac_ver
from tempfile import tempdir

# import keyword
# print(keyword.kwlist)





# a=int(input('Enter a number:'))
# if a % 2 == 0:
#     print('Even number:')


# a=(input('Enter the character:'))
# if a in 'aeiouAEIOU':
#     print('It is a vowel:')



# a=(input('Enter the character":'))
# if ord(a)>=65 and ord(a)<=90:
#     print('It is a upper character')





# a=int(input('Enter the number:'))
# if a % 3 == 0:
#     print("It can be divisible")






#Q. Wap to check the whether the given integer is 3 digit number.


# a=int(input('Enter the number:'))
# if a >= 0 and a <=9:
#     print('It is an single digit number:')
# else:
#     print('It is an double digit number:')








#Q. wap to check the whether the last digit  of a given number is 5


# a=int(input('enter first number:'))
# if a % 10 == 5:
#     print('It is last digit number is 5:')
# else:
#     print('It is last digit number is not 5:')







#Q. Wap to check the whether the given data is float


# a=eval(input('Enter a data: '))
# if type(a) == float:
#     print('It is a float')
# else:
#     print('It is not a float')







#Q. Wap to check the whether the data is single value data


# a=eval(input('Enter the data:'))
# if type(a)== int or type(a)== float or type(a)== complex or type(a)== bool:
#     print('It is a single value data:')







#Q. Wap to check whether the given character is digit or not

# a=(input('Enter the character:'))
# if '0' <= a <= '9':
#     print('It is digit ' )







#Q. Wap to check whether the given integer is multiple of 3

# a=int(input('Enter the number:'))
# if a % 3 == 0:
#        print('It is multiple of 3')







#Q. Wap to check whether the data is mutable or not


# a=eval(input('Enter the number:'))
# if type(a) in [int,float,complex,bool,str,tuple]:
#     print('It is a immutable  datatype')
# else:
#     print('It is a mutable datatype:')







#Q. wap to check whether the given character is digit  or  not


# a=(input('Enter the character:'))
# if '0' <= a <= '9':
#     print('It is digit')
# else:
#     print('It is not digit:')






#Q. Wap to check whether the given character is special or not


# a=(input('Enter the special character:'))
# if 'A' <= a <= 'Z' or '0' <= a <= '9' or 'a' <= 'z':
#     print('It is not a special character')
# else:
#     print('It is a special character')







#Q. Wap to check whether a list consists of middle value or not


# a=eval(input('Enter the list:'))
# if  len(a)% 2 == 0:
#     print('It have not a middle value')
# else:
#     print('It have a middle value')







#Q.Consider a tuple of length  2 and check whether the tuple is homogenous or not


# a=eval(input('Enter the number: '))
# if type(a[0]) == type(a[1]):
#     print('It is homogenus')
# else:
#     print('It is not a homogenenus')







#Q, Wap to check whether the string is palindrome or not


# a=(input('Enter the character:'))
# if a==a[::-1]:
#     print(a,'It is palindrome')
# else:
#     print('It is not palindrome')





#Q. Possitive and negative

# a=int(input('Enter the number:'))
# if a >= 0 :
#     print('It is possitive')
# else:
#     print('Negative')




#Q. Wap to check if the given number is single digit number or double digit number or three digit number
# or greater then three digit number


# a=int(input('Enter the number:'))
# if 0 <= a <= 9:
#     print('It is single digit number')
# elif 10 <= a <= 99:
#     print('It is double digit number:')
# elif 100 <= a <= 999:
#     print('It is three digit number:')
# elif 1000 <= a <= 9999:
#     print('It is four digit number:')
# else:
#     print('It is greater then four number')







#Q. Wap to find the greatest of three number

# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
# c=int(input('Enter the number:'))
# if a > b and a > c:
#     print('a is greatest')
# elif b >a and b > c:
#     print('b is greatest')
# elif c > a and c > b:
#     print('c is greatest')
# else:
#     print('Every number is equal')





#Q.  Wap to print grade of the student based on the marks
    # if marks are > 75 then grade 1
    # if marks are between 35 to 75 then grade 2
    # if marks are lesser than 35 than grade 3


# a=int(input('Enter the grade:'))
# if a > 75:
#     print('Grade is 1')
# elif a>=35  and a<=75:
#     print('Grade is 2')
# elif a < 35:
#     print('Grade is 3')





# n=input("Enter the character :")
# if len(n)==1:
#     if 'A'<=n<='Z' or 'a'<=n<='z':
#         if n in 'AEIOUaeiou':
#             print(n,'is a vowel')
#         else:
#             print(n,'is not a vowel')
#     else:
#         print('Give only uppercase or lowercase characters')
# else:
#     print('Give only one character')




# username='yashhh'
# passw='yash@123'


#Q.  Wap to login to instagram by entering the correct username or password

# user=input('Enter the username:')
# password=input('Enter the password:')
# if user==username:
#     if password==passw:
#       print('LOGIN DONE')
#     else:
#        print('password is incorrect')
# else:
#     print('Username is incorrect')









#Q.  Wap to print the middle character of the string only if it is uppercase
#    character.


# a=input('Enter the charcter:')
#
# if len(a)%2!=0:
#         mv=len(a)//2
#         #len(coll)//2 is used to get the middle value (index)
#         character=a[mv]
#         #now we can get the middle value using var[index]
#         if 'A'<=character<='Z':
#             print('Middle character is uppercase character')
#         else:
#             print(character,'Middle character is not a uppercase case character')
# else:
#         print('Middle value does not exist')







#Q. Wap to find the greatest of 3 number using nested if

# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
# c=int(input('Enter the number:'))
# if a > b and a > c:
#     print(a,' is greater')
# elif b > a and b > c:
#     print(b,' is greater:')
# elif c > a and c > b:
#     print(c,' is greater')
# else:
#     print('Equal number')


# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
# c=int(input('Enter the number:'))
# if a >= b:
#     if a >= c:
#         print(a, 'is greater')
#     else:
#         print(c,'is greater')
# else:
#     if b >= c:
#         print(b,'is greater')
#     else:
#         print(c,'is greater')






#Q. Wap to find the greatest of 4

# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
# c=int(input('Enter the number:'))
# d=int(input('Enter the number:'))
# if a >= b:
#     if a >= c:
#         if a >=d:
#             print(a,'is greatest')
#         else:
#             print('d is greatest')
#     else:
#         if c>=d:
#             print(c,'is greatest')
#         else:
#             print(d,'is greatest')
#
#
#
# #(here we are comparing b,c,d)
#
# else:
#     if b>=c:
#         if b>=d:
#             print(b,'is greatest')
#         else:
#             print(d,'is greatest')
#
#     else:
#         if c>=d:
#             print(c, 'is greatest')
#         else:
#             print(d, 'is greatest')







#Q. Wap to check if the given data is mutable or not if it is mutable then print the type of data

# a=eval(input('Enter the data:'))
# if type(a) in [list,set,dict]:
#     print(type(a),'Mutable data type')
# else:
#     print('it is immutable')







#Q. Wap to print last value of list only if the list is plaindroem string starting with vowel

# a=eval(input('Enter the character:'))
# if type(a) == list:
#     if type(a[-1])==str:
#         temp=a[-1]
#         if temp[0] in 'AEIOUaeiou':
#             if a==a[::-1]:
#                print(temp)
#             else:
#                 print('list is not palindrome')
#         else:
#             print('String first character is not vowel')
#     else:
#         print('last value is not string')
# else:
#     print('Ii is not a list')










#Q.  Wap to print the middle character of the string only if it is starting with vowel or
# else print the  last character


# a=(input('Enter the character:'))
# if  len(a)%2 != 0:
#     if a in 'AEIOUaeiou':
#         if a[0]:
#          character = a
#          print('It is a vowel')
#         else:
#          print('First is not vowel')
#      else:
#        print('It is not a vowel')
# else:
#     print('not a middle')









#Q. Wap to check if given character is upper case or lower case or special character or digit

# a=(input('Enter the character:'))
# if 'A' <= a <= 'Z':
#     print('Upper case')
# elif 'a' <= a <= 'z':
#     print('lower case')
# elif '0' <= a <= '9':
#     print('Digit')
# else:
#     print('It is a special character')











#Q. Wap to check if the given data type is mutable or immutable datatype

# a=eval(input('Enter thr list:'))
# if type(a) in [list,set,dict]:
#     print('Mutable')
# else:
#     print('immutable')








#Q. Wap to print the last character of the string only if the string is palindrome

# a=input('Enter the character:')
# if a==a[::-1]:
#     print(a[-1],'palindrome')
# else:
#     print('It is not a palindrome')







#Q. Wap to check if a given number is single digit or double digit or three digit or greater then

# a=int(input('Enter the digit:'))
# if 0 <= a <=9:
#     print('Single digit')
# elif 10 <= a <= 99:
#     print('double digit')
# elif 100 <= a <= 999:
#     print('Three digit')
# else:
#     print('Greater then three digit')




#Q. Wap to print the reverse string only if it is starting with
# vowel ending with consonant and having a middle value

# a=input('Enter the character:')
# if len(a)% 2!= 0:
#     if a[0] in 'AEIOUaeiou':
#         if a[-1] in 'AEIOUaeiou':
#             print(a[-1],'reversed string')
#         else:
#             print('last character is not consonant')
#     else:
#         print('First character is not vowel')
# else:
#     print('Middle value does not exist')





#Q. Wap to print middle character of the string only if it is upper case

# a=input('Enter the character:')
# if len(a) % 2 != 0:
#     mv = len(a) // 2
#     character = a[mv]
#     if 'A' <= character <= 'Z':
#         print('Upper case')
#     else:
#         print('Not upper case')
# else:
#     print('Not a middle value')




#   <----------------------- LOOP ------------------------>






#Q. Wap to print python for ten times

# i = 0
# while i < 10:
#     print('Python')
#     i = i + 1


#Q. Wap tp print natural numbers upto n

# n = int(input('Enter the number:'))
# i = 1
# while i <= n:
#     print(i)
#     i = i + 1


#Q. Wap to print even numbers upto n

# n = int(input('Enter the number:'))
# i = 2
# while i <= n:
#     print(i)
#     i = i + 2



#Q. Wap to print the numbers divisible 9 and 3 upto n

# n = int(input('Enter the number:'))
# i = 1
# while i <= n:
#       if (i % 3 == 0 and i % 9 == 0):
#         print(i)
#       i = i + 1





#Q. Wap to count number of values present in a collection and without using len function

# n=eval(input('Enter the number:'))
# counter = 0
# i = 0
# while i < len(n):
#     counter = counter + 1
#     i = i + 1
# print(counter)





#Q. Wap to count number of occurences a particular character in the string

# a=input('Enter the string:')
# b=input('Enter the character:')
# i = 0
# counter = 0
# while i < len(a):
#     if a[i] == b:
#         counter = counter + 1
#     i = i + 1
# print(counter)




#Q. Wap to count number of upper casse, lower case, digits and special
# character present in the given string


# w='PyThON@1*&'
#
# i = 0
# upper = 0
# lower = 0
# digit = 0
# Sc = 0
#
# while i < len(w):
#     if  'A' <= w[i] <= 'Z':
#         upper += 1
#     elif 'a' <= w[i] <= 'z':
#         lower += 1
#     elif '0' <= w[i] <= '9':
#         digit += 1
#     else:
#         Sc += 1
#     i += 1
#
# print(upper)
# print(lower)
# print(digit)
# print(Sc)













#Q Wap to count number of integer data type present in the below collection

# a=[12,7.8,'Hii',6+7j,9,'Demo',6]
#
# i = 0
# counter = 0
# while i < len(a):
#     if type(a[i])==int:
#         print(a[i])
#         counter += 1
#     i+=1
# print('The count of integer values is ',counter)






#Q. Wap to check if the given list is homogeneus or hetrogeneus


# a=[12,23,45,56,2+3j,2.3]
#
# check = a[0]
# i = 0
# counter = 0
#
# while i < len(a):
#     if type(a[i]) != type(check):
#         counter += 1
#     i += 1
#
# print(counter)
# if counter == 0:
#     print('Homogeneus')
# else:
#     print('Hetrogeneus')









#Q. Wap to print characters present at odd index only


# a=input('Enter the string')
# i = 0
# while i < len(a):
#     if i % 2 != 0:
#         print(a[i])
#     i += 1









#Q. Wap to print the numbers divisible by 5 between the specified limits


# a=int(input('Enter the lower:'))
# b=int(input('Enter the upper:'))
#
# i = a
#
# while i <= b:
#     if i % 5 == 0:
#         print(i)
#     i += 1






#Q. Wap to print only upper case character from the string

# a=input('Enter the string:')
#
# i = 0
# while i < len(a):
#     if "A" <= a[i] <= 'Z':
#         print(a[i])
#     i += 1





#Q. Wap to reverse the string without using slicing


# a=(input('Enter the string:'))
#
# i = 0
# out = ''
#
# while i < len(a):
#     print('After',out)
#     out = a[i] + out
#     print('Before',out)
#     i += 1
# print(out)








#Q. Wap to check is given string is palindrome or not without using slicing


# a=input('Enter the string:')
#
# i = 0
# out = ""
#
# while i < len(a):
#     print(out)
#     out = a[i] + out
#     print(out)
#     i += 1
#
# if a == out:
#     print('Palindrome')
# else:
#     print('Not palindrome')








#Q. Wap to get the following output

g = 'PyTHON@12#'

# upper = 'PTH'
# lower = 'y'
# special = '@#'
# digits = '12'


#
# g=input('Enter the string:')

# i = 0
# upper = ''
# lower = ''
# special = ''
# digits = ''
#
# while i < len(g):
#     if 'A' <= g[i]<= 'Z':
#         upper += g[i]
#     elif "a" <= g[i] <= 'z':
#         lower += g[i]
#     elif '0' <= g[i] <= '9':
#         digits += g[i]
#     else:
#         special += g[i]
#     i += 1
#
# print(upper)
# print(lower)
# print(digits)
# print(special)







#Q. Wap to extract only integer datatype from the given list

# data=[12,45,8+9j,'Think',True]
#
# i = 0
# out = []
#
# while i < len(data):
#     if type(data[i]) == int:
#         out.append(data[i])
#     i += 1
# print(out)






#Q. Wap to extract vowels and consonants from string


# a='Darshan'
# out1='aa'
# out2='Drshn'



# a=input('Enter the sting:')

# i = 0
# out1 = ''
# out2 = ''
# while i < len(a):
#     if a[i] in 'AEIOUaeiou':
#         out1 = out1 + a[i]
#     else:
#         out2 = out2 + a[i]
#
#     i += 1
# print(out1)
# print(out2)









#Q. Wap to extract only the character present at odd index

# a=input('Enter the string:')
#
# i = 0
#
# while i < len(a):
#     if i % 2 != 0:
#         print(a[i])
#     i += 1







#Q. Wap to reverse the without using type casting


# a=int(input('Enter the number:'))
#
# i = 0
# out = 0
# while a > 0:
#     ld = a % 10
#     out = out * 10 + ld
#     a = a // 10
# print(out)




#Q. Wap to check if given number is palindrome or not



# a=int(input('Enter the number:'))
#
# i = 0
# out = 0
# backup = a
# while a > i:
#     ld = a % 10
#     out = out * 10 + ld
#     a = a // 10
# if backup == out:
#         print('Palindrome')
# else:
#         print('Not palindrome')



