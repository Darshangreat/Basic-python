#Create a lambda function to check if a given number is even

# n=int(input('Enter the number:'))
# if n % 2 ==0:
#     print('True')





# def data(n):
#     return n % 2 == 0
# print(data(6))







# data = lambda n: n % 2 == 0
# print(data(5))




#Create a lambda funtion to check if the string start with vowel

# data = lambda a: a[0] in 'AEIOUaeiou'
# print(data('ice'))





#Create a lambda function to check if the give number is even or odd

# def check(n):
#     if n % 2 == 0:
#         return('even')
#     else:
#         return('odd')
# print(check(1))

# data=lambda n: 'Even' if n % 2 == 0 else 'odd'
# print(data(1))




#Q.  Create a lambda funtion to check if the given string is palindrome or not

# def check(a):
#     if a == a[::-1]:
#         return('palindrome')
#     else:
#         return('not palindrome')
# print(check('darshan'))


# data=lambda a:'Palindrome' if a==a[::-1] else 'Not palindrome'
# print(data('Dasha'))




#Q.  Wap to extract only integers from thr list

# a = [12,54,'Hii',36,5+5j]
#
# out = []
# for i in a:
#     if type(i) == int:
#         out.append(i)
# print(out)


# func=lambda a: type(a) == int
# result=filter(func,a)
# print(list(result))


#Q.  Extract all the string values from the tuple only if it is starting with uppercasse
#      ending with lowercase

# t = (10,2.3,'Supritha','home','pythoN','Ugadi')

# out = []
# for i in t:
#     if type(i) == str and 'A' <=i[0]<= 'Z' and 'a' <= i[-1] <='z':
#         out.append(i)
# print(out)


# func = lambda t : type(t) == str and 'A' <=t[0] <= 'Z' and 'a' <=t[-1]<= 'z'
# result=filter(func,t)
# print(list(result))









#Q. Program to extract all the collection values present
#    in a list which has even length

# l = [10,2.3,'sakshi',[10,20,30],(7,8),{1,2,3,4}]

# out = []
# for i in l:
#     # if (type(i) == str or type(i) == list or type(i) == tuple or type(i) == set or type(i) == dict) and len(i) % 2 == 0:
#     if type(i) in [str, list, set, tuple, dict] and len(i) % 2 == 0:
#         out.append(i)
# print(out)

# func=lambda l: type(l) in [str,list,set,tuple,dict] and len(l) % 2 == 0
# result=filter(func,l)
# print(list(result))

