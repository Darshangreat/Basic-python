# example :-

#Function without argument and without values


#
# def extract():
#     a = input('Enter the name:')
#     data = ''
#     for i in a:
#         if i in 'AEIOUaeiou':
#             data = data + i
#     print(data)
#
# extract()



#Function with arguments

# def extract(a:str,data=''):
#     for i in a:
#         if i in 'AEIOUaeiou':
#             data = data + i
#     print(data)
#
# extract('Darshan')
# extract('Rahul')





#Q.Wap to print prime numbers the between the specify limit


# a=int(input('Enter the number:'))
# b=int(input('Enter the number:'))
#
# for i in range(2,10):
#     if i % 2 == 0:
#         print(i)
#





#Q.Check the given number is prime number or not


# def extract(a:int):
#
#     for i in range(2, a):
#         if a % i == 0:
#             print('Prime number')
#             break
#     else:
#         print('Not prime')
#
# extract(5)







#Q. Function without arguments and funtion value

# def extract():
#     n = input("Enter the string:")
#     out = ""
#     for i in n:
#         if i in 'AEIOUaeiou':
#             out = out + i
#
#     return out
#
# # print(extract())
#
#
# result1=extract()
# print(result1)




#Q. Create a funtion to extract only integer data from the list

# def extract():
#     a=eval(input('Enter the list:'))
#
#     out = []
#
#     for i in a:
#         if type(i) == int:
#             print(i)
#             out.append(i)
#
#     return out
# result1 = extract()
# print(result1)



# def extract(a:list,out=[]):
#     for i in a:
#         if type(i) == int:
#             out.append(i)
#     return out
# result1 = extract([14,45,True,6+6j])
# print(result1)




#Get the following output

# a=['hai',45,2+4j,'bye']



# out = []
# for i in a:
#     if type(i) == str:
#         data = i[::-1] + i
#         out.append(data)
# print(out)





# Function Method :- 1


# def extract():
#     a = eval(input('Enter the list:'))
#     out = []
#
#     for i in a:
#         if type(i) == str:
#             data = i[::-1] + i
#             out.append(data)
#
#     print(out)
# extract()



# Function Method :- 2

#
# def extract(a:list):
#
#     out = []
#
#     for i in a:
#         if type(i) == str:
#             data = i[::-1] + i
#             out.append(data)
#     print(out)
# extract(['hai',45,2+4j,'bye'])




#Function Method :- 3


# def extract():
#     a = eval(input('Enter the list:'))
#
#     out = []
#     for i in a:
#          if type(i) == str:
#              data = i[::-1] + i
#              out.append(data)
#
#     return out
# result1=(extract())
# print(result1)


#Function Method :- 4

#
# def extract(a:list,out=[]):
#     for i in a:
#         if type(i) == str:
#             data = i[::-1] + i
#             out.append(data)
#     return out
# result1 = extract(['hai',45,2+4j,'bye'])
# print(result1)